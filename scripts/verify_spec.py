#!/usr/bin/env python
"""
Specification Verifier for Knowledge Complex

VERIFICATION: Deterministic checking that a document satisfies a spec's structural requirements.
    - "Did we build the thing right?"
    - Structural correctness, required fields, type checking
    - Automated, deterministic, pass/fail

VALIDATION: Contextual assessment of fitness-for-purpose (handled separately).
    - "Did we build the right thing?"
    - Quality assessment against guidance documents
    - Requires judgment and expert assessment

This tool performs VERIFICATION only.

Usage:
    python scripts/verify_spec.py <document_to_verify> <spec_id_or_file> [--verbose] [--json]

Examples:
    # Verify spec-for-guidance against spec-for-spec
    python scripts/verify_spec.py 00_vertices/spec-for-guidance.md v:spec:spec

    # Verify with spec file path
    python scripts/verify_spec.py 00_vertices/spec-for-guidance.md 00_vertices/spec-for-spec.md

    # Get JSON output for verification edge
    python scripts/verify_spec.py 00_vertices/spec-for-spec.md v:spec:spec --json
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parse_chart import extract_frontmatter, ParseError


class VerificationError(Exception):
    """Error raised when verification fails."""
    def __init__(self, message: str, path: str = "", details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.path = path
        self.details = details or {}
        full_message = f"{path}: {message}" if path else message
        super().__init__(full_message)


class SpecVerifier:
    """Verifies documents against specification requirements."""

    def __init__(self, verbose: bool = False, repo_root: Path = None):
        self.verbose = verbose
        self.repo_root = repo_root or Path.cwd()
        self.checks: List[Dict[str, Any]] = []
        self.errors: List[str] = []

    def log(self, message: str):
        """Log if verbose mode."""
        if self.verbose:
            print(f"  [DEBUG] {message}")

    def add_check(self, name: str, passed: bool, details: str = ""):
        """Record a verification check."""
        self.checks.append({
            "check": name,
            "passed": passed,
            "details": details
        })
        if self.verbose:
            status = "✓" if passed else "✗"
            print(f"  {status} {name}" + (f": {details}" if details else ""))

    def add_error(self, message: str):
        """Record an error."""
        self.errors.append(message)
        if self.verbose:
            print(f"  ✗ ERROR: {message}")

    def load_document(self, file_path: Path) -> Dict[str, Any]:
        """Load and parse a markdown document with frontmatter."""
        if not file_path.exists():
            raise VerificationError(f"File not found: {file_path}")

        content = file_path.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        if frontmatter is None:
            raise VerificationError(f"No YAML frontmatter found in {file_path}")

        return {
            'frontmatter': frontmatter,
            'body': body,
            'file': str(file_path)
        }

    def resolve_spec(self, spec_ref: str) -> Path:
        """Resolve a spec reference to a file path."""
        # If it looks like a file path, use it
        spec_path = Path(spec_ref)
        if spec_path.exists():
            return spec_path

        # If it's an ID like v:spec:spec, resolve it
        if spec_ref.startswith('v:spec:'):
            spec_name = spec_ref.split(':')[2]
            # Try common locations
            candidates = [
                self.repo_root / '00_vertices' / f'spec-for-{spec_name}.md',
                self.repo_root / '00_vertices' / f'{spec_name}.md',
                self.repo_root / 'templates' / '00_vertices' / f'{spec_name}.md',
            ]
            for candidate in candidates:
                if candidate.exists():
                    return candidate
            raise VerificationError(f"Cannot resolve spec ID: {spec_ref}")

        raise VerificationError(f"Invalid spec reference: {spec_ref}")

    def verify_required_field(self, frontmatter: Dict[str, Any], field: str,
                              expected_type: type = None, expected_value: Any = None) -> bool:
        """Verify a required field exists and optionally check type/value."""
        if field not in frontmatter:
            self.add_error(f"Missing required field: {field}")
            self.add_check(f"Field '{field}' present", False, "Missing")
            return False

        value = frontmatter[field]

        # Check type if specified
        if expected_type and not isinstance(value, expected_type):
            self.add_error(f"Field '{field}' has wrong type: expected {expected_type.__name__}, got {type(value).__name__}")
            self.add_check(f"Field '{field}' type", False, f"Expected {expected_type.__name__}")
            return False

        # Check value if specified
        if expected_value is not None and value != expected_value:
            self.add_error(f"Field '{field}' has wrong value: expected '{expected_value}', got '{value}'")
            self.add_check(f"Field '{field}' value", False, f"Expected '{expected_value}'")
            return False

        self.add_check(f"Field '{field}'", True, f"{value}")
        return True

    def verify_tag_chain(self, frontmatter: Dict[str, Any], required_tags: List[str]) -> bool:
        """Verify tags array contains required inheritance chain."""
        if 'tags' not in frontmatter:
            self.add_error("Missing 'tags' field")
            self.add_check("Tags present", False)
            return False

        tags = frontmatter['tags']
        if not isinstance(tags, list):
            self.add_error(f"Tags must be a list, got {type(tags).__name__}")
            self.add_check("Tags type", False)
            return False

        missing_tags = [tag for tag in required_tags if tag not in tags]
        if missing_tags:
            self.add_error(f"Missing required tags: {missing_tags}")
            self.add_check("Tag inheritance chain", False, f"Missing: {missing_tags}")
            return False

        self.add_check("Tag inheritance chain", True, f"{tags}")
        return True

    def verify_spec_document(self, doc: Dict[str, Any], spec: Dict[str, Any]) -> bool:
        """Verify a spec document against spec-for-spec requirements."""
        frontmatter = doc['frontmatter']
        body = doc['body']

        # Required frontmatter fields for specs
        checks_passed = True

        checks_passed &= self.verify_required_field(frontmatter, 'type', str, 'vertex/spec')
        checks_passed &= self.verify_required_field(frontmatter, 'extends', str, 'doc')
        checks_passed &= self.verify_required_field(frontmatter, 'id', str)
        checks_passed &= self.verify_required_field(frontmatter, 'name', str)
        checks_passed &= self.verify_required_field(frontmatter, 'version', str)
        checks_passed &= self.verify_required_field(frontmatter, 'created')
        checks_passed &= self.verify_required_field(frontmatter, 'modified')

        # Verify ID format
        if 'id' in frontmatter:
            id_val = frontmatter['id']
            if not id_val.startswith('v:spec:'):
                self.add_error(f"Spec ID must start with 'v:spec:', got '{id_val}'")
                self.add_check("ID format", False, f"Must start with 'v:spec:'")
                checks_passed = False
            else:
                self.add_check("ID format", True, id_val)

        # Verify tag chain
        checks_passed &= self.verify_tag_chain(frontmatter, ['vertex', 'doc', 'spec'])

        # Check required body sections
        required_sections = [
            '## Purpose',
            '## Required Frontmatter Fields',
            '## Required Body Sections',
            '## Schema'
        ]

        for section in required_sections:
            if section in body:
                self.add_check(f"Section '{section}'", True)
            else:
                self.add_error(f"Missing required section: {section}")
                self.add_check(f"Section '{section}'", False, "Missing")
                checks_passed = False

        return checks_passed

    def verify_guidance_document(self, doc: Dict[str, Any], spec: Dict[str, Any]) -> bool:
        """Verify a guidance document against spec-for-guidance requirements."""
        frontmatter = doc['frontmatter']
        body = doc['body']

        checks_passed = True

        # Required frontmatter fields for guidance
        checks_passed &= self.verify_required_field(frontmatter, 'type', str, 'vertex/guidance')
        checks_passed &= self.verify_required_field(frontmatter, 'extends', str, 'doc')
        checks_passed &= self.verify_required_field(frontmatter, 'id', str)
        checks_passed &= self.verify_required_field(frontmatter, 'name', str)
        checks_passed &= self.verify_required_field(frontmatter, 'version', str)
        checks_passed &= self.verify_required_field(frontmatter, 'created')
        checks_passed &= self.verify_required_field(frontmatter, 'modified')

        # Verify ID format
        if 'id' in frontmatter:
            id_val = frontmatter['id']
            if not id_val.startswith('v:guidance:'):
                self.add_error(f"Guidance ID must start with 'v:guidance:', got '{id_val}'")
                self.add_check("ID format", False)
                checks_passed = False
            else:
                self.add_check("ID format", True, id_val)

        # Verify tag chain
        checks_passed &= self.verify_tag_chain(frontmatter, ['vertex', 'doc', 'guidance'])

        # Check required body sections
        required_sections = [
            '## Purpose',
            '## Document Overview',
            '## Quality Criteria',
            '## Section-by-Section Guidance'
        ]

        for section in required_sections:
            if section in body:
                self.add_check(f"Section '{section}'", True)
            else:
                self.add_error(f"Missing required section: {section}")
                self.add_check(f"Section '{section}'", False, "Missing")
                checks_passed = False

        # Check quality criteria count (should have ≥3)
        criteria_count = body.count('###') if '## Quality Criteria' in body else 0
        if criteria_count >= 3:
            self.add_check("Quality criteria count (≥3)", True, f"{criteria_count} criteria")
        else:
            self.add_error(f"Guidance should have ≥3 quality criteria, found {criteria_count}")
            self.add_check("Quality criteria count (≥3)", False, f"Only {criteria_count}")
            checks_passed = False

        return checks_passed

    def verify(self, doc_path: Path, spec_ref: str) -> Dict[str, Any]:
        """
        Verify a document against a specification.

        Returns verification result dictionary.
        """
        self.log(f"Loading document: {doc_path}")
        doc = self.load_document(doc_path)

        self.log(f"Resolving spec: {spec_ref}")
        spec_path = self.resolve_spec(spec_ref)

        self.log(f"Loading spec: {spec_path}")
        spec = self.load_document(spec_path)

        # Determine verification type based on spec ID
        spec_id = spec['frontmatter'].get('id', '')
        doc_type = doc['frontmatter'].get('type', '')

        self.log(f"Document type: {doc_type}")
        self.log(f"Spec ID: {spec_id}")

        # Perform type-specific verification
        if spec_id == 'v:spec:spec':
            success = self.verify_spec_document(doc, spec)
        elif spec_id == 'v:spec:guidance':
            success = self.verify_guidance_document(doc, spec)
        else:
            # Generic verification (minimal checks)
            self.log("Using generic verification (spec not recognized)")
            success = True
            self.verify_required_field(doc['frontmatter'], 'type', str)
            self.verify_required_field(doc['frontmatter'], 'id', str)
            self.verify_required_field(doc['frontmatter'], 'name', str)
            self.verify_required_field(doc['frontmatter'], 'version', str)

        # Build result
        result = {
            'status': 'PASS' if success and not self.errors else 'FAIL',
            'document': {
                'path': str(doc_path),
                'id': doc['frontmatter'].get('id'),
                'type': doc['frontmatter'].get('type'),
                'name': doc['frontmatter'].get('name')
            },
            'spec': {
                'path': str(spec_path),
                'id': spec['frontmatter'].get('id'),
                'name': spec['frontmatter'].get('name')
            },
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'checks': self.checks,
            'errors': self.errors,
            'summary': {
                'total_checks': len(self.checks),
                'passed': sum(1 for c in self.checks if c['passed']),
                'failed': sum(1 for c in self.checks if not c['passed']),
                'error_count': len(self.errors)
            }
        }

        return result


def format_result_text(result: Dict[str, Any]) -> str:
    """Format verification result as human-readable text."""
    lines = []
    lines.append(f"{'='*70}")
    lines.append(f"Verification Result: {result['status']}")
    lines.append(f"{'='*70}")
    lines.append("")

    lines.append("Document:")
    lines.append(f"  Path: {result['document']['path']}")
    lines.append(f"  ID:   {result['document']['id']}")
    lines.append(f"  Type: {result['document']['type']}")
    lines.append(f"  Name: {result['document']['name']}")
    lines.append("")

    lines.append("Spec:")
    lines.append(f"  Path: {result['spec']['path']}")
    lines.append(f"  ID:   {result['spec']['id']}")
    lines.append(f"  Name: {result['spec']['name']}")
    lines.append("")

    lines.append("Summary:")
    lines.append(f"  Total checks: {result['summary']['total_checks']}")
    lines.append(f"  Passed:       {result['summary']['passed']}")
    lines.append(f"  Failed:       {result['summary']['failed']}")
    lines.append(f"  Errors:       {result['summary']['error_count']}")
    lines.append("")

    if result['checks']:
        lines.append("Checks:")
        for check in result['checks']:
            status = "✓" if check['passed'] else "✗"
            details = f" - {check['details']}" if check.get('details') else ""
            lines.append(f"  {status} {check['check']}{details}")
        lines.append("")

    if result['errors']:
        lines.append("Errors:")
        for i, error in enumerate(result['errors'], 1):
            lines.append(f"  {i}. {error}")
        lines.append("")

    lines.append(f"Timestamp: {result['timestamp']}")
    lines.append(f"{'='*70}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Verify a document against a specification',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('document', type=Path, help='Path to document to verify')
    parser.add_argument('spec', help='Spec ID (e.g., v:spec:spec) or path to spec file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--root', type=Path, help='Repository root (default: current directory)')

    args = parser.parse_args()

    try:
        verifier = SpecVerifier(verbose=args.verbose, repo_root=args.root)
        result = verifier.verify(args.document, args.spec)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_result_text(result))

        return 0 if result['status'] == 'PASS' else 1

    except (VerificationError, ParseError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
