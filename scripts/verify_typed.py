#!/usr/bin/env python
"""
Type-Specific Verifier for Knowledge Complex

Verifies that elements conform to their type-specific template requirements.

This complements verify_spec.py:
- verify_spec.py: Checks if a doc satisfies a spec's structural requirements
- verify_typed.py: Checks if an element conforms to its type template

Usage:
    python scripts/verify_typed.py <element_file> [--verbose]

Examples:
    # Verify a verification edge against the verification template
    python scripts/verify_typed.py 01_edges/verification-spec-spec.md

    # Verify a spec vertex
    python scripts/verify_typed.py 00_vertices/spec-for-spec.md --verbose
"""

import sys
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).parent))
from parse_chart import extract_frontmatter, ParseError


class TypedVerificationError(Exception):
    """Error raised when typed verification fails."""
    pass


class TypedVerifier:
    """Verifies elements against their type-specific template requirements."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.checks: List[Dict[str, Any]] = []
        self.errors: List[str] = []

    def log(self, message: str):
        """Log if verbose mode."""
        if self.verbose:
            print(f"  [DEBUG] {message}")

    def add_check(self, name: str, passed: bool, details: str = ""):
        """Record a check."""
        self.checks.append({
            "check": name,
            "passed": passed,
            "details": details
        })
        status = "✓" if passed else "✗"
        print(f"  {status} {name}" + (f": {details}" if details else ""))

    def add_error(self, message: str):
        """Record an error."""
        self.errors.append(message)

    def load_element(self, file_path: Path) -> Dict[str, Any]:
        """Load and parse an element."""
        if not file_path.exists():
            raise TypedVerificationError(f"File not found: {file_path}")

        content = file_path.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        if frontmatter is None:
            raise TypedVerificationError(f"No YAML frontmatter in {file_path}")

        return {
            'frontmatter': frontmatter,
            'body': body,
            'file': str(file_path)
        }

    def verify_field(self, frontmatter: Dict[str, Any], field: str,
                     expected_type: type = None, expected_value: Any = None,
                     required: bool = True) -> bool:
        """Verify a field exists and optionally check type/value."""
        if field not in frontmatter:
            if required:
                self.add_error(f"Missing required field: {field}")
                self.add_check(f"Field '{field}'", False, "Missing")
                return False
            else:
                self.add_check(f"Field '{field}' (optional)", True, "Not present (ok)")
                return True

        value = frontmatter[field]

        if expected_type and not isinstance(value, expected_type):
            self.add_error(f"Field '{field}': expected {expected_type.__name__}, got {type(value).__name__}")
            self.add_check(f"Field '{field}' type", False, f"Wrong type")
            return False

        if expected_value is not None and value != expected_value:
            self.add_error(f"Field '{field}': expected '{expected_value}', got '{value}'")
            self.add_check(f"Field '{field}' value", False, f"Wrong value")
            return False

        self.add_check(f"Field '{field}'", True, f"{value}")
        return True

    def verify_vertex_base(self, element: Dict[str, Any]) -> bool:
        """Verify base vertex requirements."""
        fm = element['frontmatter']
        passed = True

        # Type must start with vertex/
        if not fm.get('type', '').startswith('vertex/'):
            self.add_error(f"Vertex type must start with 'vertex/', got '{fm.get('type')}'")
            self.add_check("Type format", False)
            passed = False
        else:
            self.add_check("Type format", True, fm['type'])

        # ID must start with v:
        if not fm.get('id', '').startswith('v:'):
            self.add_error(f"Vertex ID must start with 'v:', got '{fm.get('id')}'")
            self.add_check("ID format", False)
            passed = False
        else:
            self.add_check("ID format", True, fm['id'])

        # Tags must include 'vertex'
        if 'vertex' not in fm.get('tags', []):
            self.add_error("Tags must include 'vertex'")
            self.add_check("Tag 'vertex'", False)
            passed = False
        else:
            self.add_check("Tag 'vertex'", True)

        return passed

    def verify_edge_base(self, element: Dict[str, Any]) -> bool:
        """Verify base edge requirements."""
        fm = element['frontmatter']
        passed = True

        # Type must start with edge/
        if not fm.get('type', '').startswith('edge/'):
            self.add_error(f"Edge type must start with 'edge/', got '{fm.get('type')}'")
            self.add_check("Type format", False)
            passed = False
        else:
            self.add_check("Type format", True, fm['type'])

        # ID must start with e:
        if not fm.get('id', '').startswith('e:'):
            self.add_error(f"Edge ID must start with 'e:', got '{fm.get('id')}'")
            self.add_check("ID format", False)
            passed = False
        else:
            self.add_check("ID format", True, fm['id'])

        # Tags must include 'edge'
        if 'edge' not in fm.get('tags', []):
            self.add_error("Tags must include 'edge'")
            self.add_check("Tag 'edge'", False)
            passed = False
        else:
            self.add_check("Tag 'edge'", True)

        # Required fields
        passed &= self.verify_field(fm, 'source', str)
        passed &= self.verify_field(fm, 'target', str)
        passed &= self.verify_field(fm, 'source_type', str)
        passed &= self.verify_field(fm, 'target_type', str)
        passed &= self.verify_field(fm, 'orientation', str)

        # Orientation must be directed or undirected
        orientation = fm.get('orientation')
        if orientation not in ['directed', 'undirected']:
            self.add_error(f"Orientation must be 'directed' or 'undirected', got '{orientation}'")
            self.add_check("Orientation value", False)
            passed = False
        else:
            self.add_check("Orientation value", True, orientation)

        return passed

    def verify_verification_edge(self, element: Dict[str, Any]) -> bool:
        """Verify verification edge specific requirements."""
        fm = element['frontmatter']
        body = element['body']
        passed = True

        self.log("Checking verification edge requirements")

        # Type must be edge/verification
        passed &= self.verify_field(fm, 'type', str, 'edge/verification')

        # Source type must be doc or subtype
        source_type = fm.get('source_type', '')
        if not (source_type.startswith('vertex/doc') or source_type in ['vertex/spec', 'vertex/guidance']):
            self.add_error(f"Source must be doc or subtype, got '{source_type}'")
            self.add_check("Source type (doc or subtype)", False)
            passed = False
        else:
            self.add_check("Source type (doc or subtype)", True, source_type)

        # Target type must be vertex/spec
        passed &= self.verify_field(fm, 'target_type', str, 'vertex/spec')

        # Orientation must be directed
        passed &= self.verify_field(fm, 'orientation', str, 'directed')

        # Tags must include verification
        if 'verification' not in fm.get('tags', []):
            self.add_error("Tags must include 'verification'")
            self.add_check("Tag 'verification'", False)
            passed = False
        else:
            self.add_check("Tag 'verification'", True)

        # Body must contain verification output
        if '## Verification Output' not in body:
            self.add_error("Body must contain '## Verification Output' section")
            self.add_check("Verification Output section", False)
            passed = False
        else:
            self.add_check("Verification Output section", True)

        if '## Verification Status' not in body:
            self.add_error("Body should contain '## Verification Status' section")
            self.add_check("Verification Status section", False)
            passed = False
        else:
            self.add_check("Verification Status section", True)

        return passed

    def verify_coupling_edge(self, element: Dict[str, Any]) -> bool:
        """Verify coupling edge specific requirements."""
        fm = element['frontmatter']
        passed = True

        self.log("Checking coupling edge requirements")

        # Type must be edge/coupling
        passed &= self.verify_field(fm, 'type', str, 'edge/coupling')

        # Source type must be vertex/spec
        passed &= self.verify_field(fm, 'source_type', str, 'vertex/spec')

        # Target type must be vertex/guidance
        passed &= self.verify_field(fm, 'target_type', str, 'vertex/guidance')

        # Orientation must be undirected
        passed &= self.verify_field(fm, 'orientation', str, 'undirected')

        # Tags must include coupling
        if 'coupling' not in fm.get('tags', []):
            self.add_error("Tags must include 'coupling'")
            self.add_check("Tag 'coupling'", False)
            passed = False
        else:
            self.add_check("Tag 'coupling'", True)

        return passed

    def verify_validation_edge(self, element: Dict[str, Any]) -> bool:
        """Verify validation edge specific requirements."""
        fm = element['frontmatter']
        body = element['body']
        passed = True

        self.log("Checking validation edge requirements")

        # Type must be edge/validation
        passed &= self.verify_field(fm, 'type', str, 'edge/validation')

        # Source type must be doc or subtype
        source_type = fm.get('source_type', '')
        if not (source_type.startswith('vertex/doc') or source_type in ['vertex/spec', 'vertex/guidance']):
            self.add_error(f"Source must be doc or subtype, got '{source_type}'")
            self.add_check("Source type (doc or subtype)", False)
            passed = False
        else:
            self.add_check("Source type (doc or subtype)", True, source_type)

        # Target type must be vertex/guidance
        passed &= self.verify_field(fm, 'target_type', str, 'vertex/guidance')

        # Orientation must be directed
        passed &= self.verify_field(fm, 'orientation', str, 'directed')

        # Tags must include validation
        if 'validation' not in fm.get('tags', []):
            self.add_error("Tags must include 'validation'")
            self.add_check("Tag 'validation'", False)
            passed = False
        else:
            self.add_check("Tag 'validation'", True)

        # Accountability fields
        passed &= self.verify_field(fm, 'validator', str)
        passed &= self.verify_field(fm, 'validation_method', str)

        validation_method = fm.get('validation_method', '')
        if validation_method not in ['manual', 'llm-assisted', 'automated']:
            self.add_error(f"validation_method must be 'manual', 'llm-assisted', or 'automated', got '{validation_method}'")
            self.add_check("Validation method", False)
            passed = False
        else:
            self.add_check("Validation method", True, validation_method)

        # LLM model required for llm-assisted
        if validation_method == 'llm-assisted':
            if 'llm_model' not in fm:
                self.add_error("llm_model is required when validation_method is 'llm-assisted'")
                self.add_check("LLM model (required for llm-assisted)", False, "Missing")
                passed = False
            else:
                self.add_check("LLM model (required for llm-assisted)", True, fm['llm_model'])

        # Human approver required for llm-assisted or automated
        if validation_method in ['llm-assisted', 'automated']:
            if 'human_approver' not in fm:
                self.add_error(f"human_approver is required when validation_method is '{validation_method}'")
                self.add_check("Human approver (required)", False, "Missing")
                passed = False
            else:
                self.add_check("Human approver (required)", True, fm['human_approver'])

        # Body must contain validation assessment
        if '## Validation Assessment' not in body:
            self.add_error("Body must contain '## Validation Assessment' section")
            self.add_check("Validation Assessment section", False)
            passed = False
        else:
            self.add_check("Validation Assessment section", True)

        if '## Accountability Statement' not in body:
            self.add_error("Body must contain '## Accountability Statement' section")
            self.add_check("Accountability Statement section", False)
            passed = False
        else:
            self.add_check("Accountability Statement section", True)

        return passed

    def verify_element(self, file_path: Path) -> bool:
        """Verify an element against its type template."""
        print(f"\nVerifying: {file_path}")
        print(f"{'='*70}")

        element = self.load_element(file_path)
        fm = element['frontmatter']
        element_type = fm.get('type', '')

        self.log(f"Element type: {element_type}")

        # Determine base type
        if element_type.startswith('vertex/'):
            base_passed = self.verify_vertex_base(element)
        elif element_type.startswith('edge/'):
            base_passed = self.verify_edge_base(element)
        elif element_type.startswith('face/'):
            # Face verification not yet implemented
            self.add_check("Base type", True, "face (verification not implemented)")
            base_passed = True
        elif element_type.startswith('chart/'):
            # Chart verification not yet implemented
            self.add_check("Base type", True, "chart (verification not implemented)")
            base_passed = True
        else:
            self.add_error(f"Unknown type: {element_type}")
            self.add_check("Base type", False, f"Unknown: {element_type}")
            return False

        # Type-specific verification
        type_passed = True
        if element_type == 'edge/verification':
            type_passed = self.verify_verification_edge(element)
        elif element_type == 'edge/coupling':
            type_passed = self.verify_coupling_edge(element)
        elif element_type == 'edge/validation':
            type_passed = self.verify_validation_edge(element)
        # Add more type-specific verifications as needed

        overall_passed = base_passed and type_passed and len(self.errors) == 0

        print(f"{'='*70}")
        print(f"Result: {'✓ PASS' if overall_passed else '✗ FAIL'}")
        print(f"Checks: {sum(1 for c in self.checks if c['passed'])}/{len(self.checks)} passed")

        if self.errors:
            print(f"\nErrors ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        return overall_passed


def main():
    parser = argparse.ArgumentParser(
        description='Verify element against type template requirements',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument('element', type=Path, help='Path to element file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    try:
        verifier = TypedVerifier(verbose=args.verbose)
        passed = verifier.verify_element(args.element)
        return 0 if passed else 1

    except (TypedVerificationError, ParseError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
