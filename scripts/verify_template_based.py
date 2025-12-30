#!/usr/bin/env python
"""
Template-Based Verification for Knowledge Complex

Uses templates as the single source of truth for verification requirements.
Replaces hardcoded type-specific verification logic with template-driven checks.
"""

import sys
from pathlib import Path
from typing import Dict, List, Any

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parse_chart import extract_frontmatter, ParseError
from template_parser import TemplateParser, TemplateSpec, TemplateRequirement


class TemplateBasedVerifier:
    """Verifies knowledge complex elements against their templates."""

    def __init__(self, templates_dir: Path, verbose: bool = False):
        self.verbose = verbose
        self.errors: List[str] = []
        self.checks_passed = 0
        self.checks_total = 0

        # Load all templates
        self.parser = TemplateParser(templates_dir)
        self.parser.load_all_templates()

        if self.verbose:
            print(f"Loaded {len(self.parser.templates)} templates")

    def verify_element(self, element_path: Path) -> bool:
        """
        Verify an element against its template.

        Returns:
            True if all checks pass, False otherwise
        """
        self.errors = []
        self.checks_passed = 0
        self.checks_total = 0

        try:
            content = element_path.read_text(encoding='utf-8')
            frontmatter, body = extract_frontmatter(content)

            if not frontmatter:
                self.add_error("No frontmatter found")
                return False

            # Get element type
            element_type = frontmatter.get('type', '')
            if not element_type:
                self.add_error("No 'type' field in frontmatter")
                return False

            # Get template for this type
            template = self.parser.get_template(element_type)
            if not template:
                self.add_error(f"No template found for type '{element_type}'")
                return False

            if self.verbose:
                print(f"Using template: {template.template_path.name}")

            # Verify frontmatter fields
            passed = self.verify_frontmatter(frontmatter, template)

            # Verify body sections
            passed &= self.verify_body(body, template)

            # Verify tags
            passed &= self.verify_tags(frontmatter, template)

            return passed

        except Exception as e:
            self.add_error(f"Verification error: {e}")
            return False

    def verify_frontmatter(self, frontmatter: Dict[str, Any], template: TemplateSpec) -> bool:
        """Verify frontmatter fields against template requirements."""
        passed = True

        for req in template.frontmatter_requirements:
            # Check if field is conditionally required
            if req.conditional:
                condition_met = self.parser.evaluate_conditional(req.conditional, frontmatter)
                if not condition_met:
                    # Condition not met, field not required
                    continue

            # Check if field exists
            if req.field not in frontmatter:
                if req.required:
                    self.add_error(f"Missing required field '{req.field}'")
                    passed = False
                continue

            self.check(f"Field '{req.field}'", frontmatter[req.field])

            # Check expected value if specified
            if req.expected_value:
                actual = frontmatter[req.field]
                # Handle "Must be X or subtype" patterns
                if '/' in str(req.expected_value) and '/' in str(actual):
                    # Type check - allow subtypes
                    expected_parts = req.expected_value.split('/')
                    actual_parts = str(actual).split('/')
                    # For "vertex/doc", allow "vertex/spec" (extends doc)
                    # This is simplified - full type checking would need inheritance chain
                    if actual_parts[0] != expected_parts[0]:
                        self.add_error(f"Field '{req.field}': expected base '{expected_parts[0]}', got '{actual_parts[0]}'")
                        passed = False
                elif str(actual) != str(req.expected_value):
                    self.add_error(f"Field '{req.field}': expected '{req.expected_value}', got '{actual}'")
                    passed = False
                else:
                    self.check(f"Field '{req.field}' value", req.expected_value)

            # Check field type if specified
            if req.field_type:
                # Skip type check for datetime fields - YAML parser converts them
                import datetime
                if isinstance(frontmatter[req.field], (datetime.datetime, datetime.date)):
                    # Datetime fields are fine - YAML parser handles them
                    continue

                if not isinstance(frontmatter[req.field], req.field_type):
                    # Handle tuples of types (for union types)
                    if isinstance(req.field_type, tuple):
                        if not isinstance(frontmatter[req.field], req.field_type):
                            self.add_error(f"Field '{req.field}': expected {req.field_type}, got {type(frontmatter[req.field])}")
                            passed = False
                    else:
                        self.add_error(f"Field '{req.field}': expected {req.field_type}, got {type(frontmatter[req.field])}")
                        passed = False

        return passed

    def verify_body(self, body: str, template: TemplateSpec) -> bool:
        """Verify required body sections are present."""
        passed = True

        for required_section in template.body_requirements:
            if required_section in body:
                self.check(f"Body section '{required_section}'")
            else:
                self.add_error(f"Missing required body section '{required_section}'")
                passed = False

        return passed

    def verify_tags(self, frontmatter: Dict[str, Any], template: TemplateSpec) -> bool:
        """Verify required tags are present."""
        passed = True

        tags = frontmatter.get('tags', [])
        if not isinstance(tags, list):
            self.add_error("'tags' field must be an array")
            return False

        for required_tag in template.tag_requirements:
            if required_tag in tags:
                self.check(f"Tag '{required_tag}'")
            else:
                self.add_error(f"Missing required tag '{required_tag}'")
                passed = False

        return passed

    def check(self, description: str, value: Any = None):
        """Record a successful check."""
        self.checks_passed += 1
        self.checks_total += 1
        if self.verbose:
            value_str = f": {value}" if value is not None else ""
            print(f"  ✓ {description}{value_str}")

    def add_error(self, message: str):
        """Record an error."""
        self.checks_total += 1
        self.errors.append(message)
        if self.verbose:
            print(f"  ✗ {message}")

    def print_report(self, element_path: Path, passed: bool):
        """Print verification report."""
        print(f"Verifying: {element_path}")
        print("=" * 70)

        if not self.verbose:
            # Print errors
            for error in self.errors:
                print(f"  ✗ {error}")

        print("=" * 70)
        if passed:
            print(f"Result: ✓ PASS")
            print(f"Checks: {self.checks_passed}/{self.checks_total} passed")
        else:
            print(f"Result: ✗ FAIL")
            print(f"Checks: {self.checks_passed}/{self.checks_total} passed")
            print(f"Errors: {len(self.errors)}")


def main():
    """Main verification function."""
    import argparse

    parser = argparse.ArgumentParser(description='Verify knowledge complex elements against templates')
    parser.add_argument('element', help='Path to element file to verify')
    parser.add_argument('--verbose', action='store_true', help='Show all checks, not just errors')
    parser.add_argument('--templates', default=None, help='Path to templates directory')

    args = parser.parse_args()

    element_path = Path(args.element)
    if not element_path.exists():
        print(f"Error: File not found: {element_path}")
        return 1

    # Default templates directory
    if args.templates:
        templates_dir = Path(args.templates)
    else:
        templates_dir = Path(__file__).parent.parent / 'templates'

    if not templates_dir.exists():
        print(f"Error: Templates directory not found: {templates_dir}")
        return 1

    # Create verifier
    verifier = TemplateBasedVerifier(templates_dir, verbose=args.verbose)

    # Verify element
    passed = verifier.verify_element(element_path)

    # Print report
    verifier.print_report(element_path, passed)

    return 0 if passed else 1


if __name__ == '__main__':
    sys.exit(main())
