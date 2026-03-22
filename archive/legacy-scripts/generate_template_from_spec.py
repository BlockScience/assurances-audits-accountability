#!/usr/bin/env python3
"""
Generate Obsidian template from specification document.

Phase 1 POC: Demonstrates auto-generation for persona document type.

Usage:
    python scripts/generate_template_from_spec.py 00_vertices/spec-for-persona.md
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import yaml

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))
from parse_chart import extract_frontmatter


class SpecParser:
    """Parse specification documents to extract template requirements."""

    def __init__(self, spec_path: Path):
        self.spec_path = spec_path
        self.content = spec_path.read_text(encoding='utf-8')
        self.frontmatter, self.body = extract_frontmatter(self.content)

    def extract_frontmatter_requirements(self) -> List[Dict[str, Any]]:
        """
        Extract frontmatter requirements from the spec's requirement tables.

        Looks for markdown tables with headers like:
        | Field | Type | Requirement | Description |

        Also handles nested objects (elements.vertices) and array of objects (visualizations).
        """
        requirements = []

        # Find all tables in the document
        # Make trailing newline optional to handle tables at end of file
        table_pattern = r'\|[^\n]+\|\n\|[-:\s|]+\|\n((?:\|[^\n]+\|(?:\n|$))+)'
        tables = re.finditer(table_pattern, self.body)

        for table_match in tables:
            table_text = table_match.group(0)

            # Check if this is a frontmatter requirements table
            if '| Field |' not in table_text or '| Type |' not in table_text:
                continue

            # Parse table rows
            rows = table_text.strip().split('\n')[2:]  # Skip header and separator
            for row in rows:
                if not row.strip():
                    continue

                cells = [cell.strip() for cell in row.split('|')[1:-1]]  # Remove empty first/last
                if len(cells) < 4:
                    continue

                field = cells[0].strip('`')
                field_type = cells[1]
                requirement = cells[2]
                description = cells[3]

                requirements.append({
                    'field': field,
                    'type': field_type,
                    'requirement': requirement,
                    'description': description
                })

        return requirements

    def extract_object_array_structure(self, parent_field: str) -> Optional[List[Dict[str, Any]]]:
        """
        Extract structure for array of objects (e.g., visualizations array).

        Looks for sections like "#### Visualization Object Structure" that define
        the fields within objects in an array.
        """
        # Try with plural removed (visualizations → visualization)
        singular = parent_field.rstrip('s')

        # Pattern: look for section about object structure, then find the table
        # Try both singular and plural forms
        patterns = [
            rf'####\s+{singular.title()}.*?Object Structure.*?(\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|(?:\n|$))+)',
            rf'####\s+{parent_field.title()}.*?Object Structure.*?(\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|(?:\n|$))+)'
        ]

        match = None
        for pattern in patterns:
            match = re.search(pattern, self.body, re.IGNORECASE | re.DOTALL)
            if match:
                break

        if not match:
            return None

        table_text = match.group(1)
        rows = table_text.strip().split('\n')[2:]  # Skip header and separator

        fields = []
        for row in rows:
            if not row.strip():
                continue

            cells = [cell.strip() for cell in row.split('|')[1:-1]]
            if len(cells) < 4:
                continue

            field = cells[0].strip('`')
            field_type = cells[1]
            requirement = cells[2]
            description = cells[3]

            fields.append({
                'field': field,
                'type': field_type,
                'requirement': requirement,
                'description': description
            })

        return fields if fields else None

    def extract_body_sections(self) -> List[Dict[str, str]]:
        """
        Extract required body sections from the spec.

        Looks for sections like:
        ### 1. Purpose Statement
        ### 2. Role and Identity
        """
        sections = []

        # Find numbered sections under "Required Body Sections"
        section_pattern = r'### (\d+)\. (.+?)\n\n(.*?)(?=\n###|\n##|\Z)'
        matches = re.finditer(section_pattern, self.body, re.DOTALL)

        for match in matches:
            number = match.group(1)
            name = match.group(2)
            content = match.group(3)

            # Extract format example if present
            format_example = None
            format_match = re.search(r'\*\*Format:\*\*\n```markdown\n(.*?)\n```', content, re.DOTALL)
            if format_match:
                format_example = format_match.group(1).strip()

            # Extract requirements
            requirements = []
            req_pattern = r'- (MUST|SHOULD|MAY) (.+)'
            for req_match in re.finditer(req_pattern, content):
                requirements.append(f"{req_match.group(1)} {req_match.group(2)}")

            sections.append({
                'number': number,
                'name': name,
                'format': format_example,
                'requirements': requirements
            })

        return sections


class TemplateGenerator:
    """Generate Obsidian template from parsed spec requirements."""

    def __init__(self, spec_parser: SpecParser):
        self.spec = spec_parser

    def generate_template(self) -> str:
        """Generate complete template content."""
        frontmatter = self.generate_frontmatter()
        body = self.generate_body()

        return f"---\n{frontmatter}---\n\n{body}"

    def generate_frontmatter(self) -> str:
        """Generate template frontmatter from spec requirements."""
        requirements = self.spec.extract_frontmatter_requirements()

        fm_dict = {}
        nested_objects = {}  # Track parent fields for nested objects
        array_object_fields = set()  # Track fields that are part of array[object] structures

        # First pass: identify array[object] fields and their sub-fields
        for req in requirements:
            if req['type'] == 'array[object]':
                object_fields = self.spec.extract_object_array_structure(req['field'])
                if object_fields:
                    # Mark all sub-fields as part of this array structure
                    for obj_field in object_fields:
                        array_object_fields.add(obj_field['field'])

        # Second pass: generate frontmatter
        for req in requirements:
            field = req['field']
            description = req['description']
            field_type = req['type']
            requirement = req['requirement']

            # Skip fields that are part of array[object] structures (they're in the object definition)
            if field in array_object_fields:
                continue

            # Handle nested object fields (e.g., elements.vertices)
            if '.' in field:
                parent, child = field.split('.', 1)
                if parent not in nested_objects:
                    nested_objects[parent] = {}
                # Will be processed later
                nested_objects[parent][child] = {
                    'type': field_type,
                    'requirement': requirement,
                    'description': description
                }
                continue

            # Handle array of objects (e.g., visualizations)
            if field_type == 'array[object]':
                # Extract object structure
                object_fields = self.spec.extract_object_array_structure(field)
                if object_fields:
                    fm_dict[field] = self.generate_object_array_placeholder(field, object_fields, requirement == 'OPTIONAL')
                else:
                    fm_dict[field] = []
                continue

            # Handle parent object that has nested children
            if field_type == 'object' and field in [req2['field'].split('.')[0] for req2 in requirements if '.' in req2['field']]:
                # This is a parent object, will be filled in when processing nested fields
                continue

            # Determine field value
            if 'Must be' in description and '`' in description:
                # Fixed value - extract literal
                match = re.search(r'Must be `([^`]+)`', description)
                if match:
                    value = match.group(1)
                    fm_dict[field] = value
                    continue

            if 'format:' in description.lower() or 'Format:' in description:
                # Format specified - extract pattern
                match = re.search(r'[Ff]ormat: `([^`]+)`', description)
                if match:
                    pattern = match.group(1)
                    # Convert pattern to placeholder
                    value = self.pattern_to_placeholder(pattern)
                    fm_dict[field] = value
                    continue

            # Default placeholder based on field name and type
            if field_type == 'array[string]':
                if 'Must include' in description:
                    # Extract required array values
                    match = re.search(r'Must include `\[([^\]]+)\]`', description)
                    if match:
                        items = [item.strip() for item in match.group(1).split(',')]
                        fm_dict[field] = items
                        continue
                # Generic array placeholder - empty for optional fields
                if requirement == 'OPTIONAL':
                    fm_dict[field] = []
                else:
                    fm_dict[field] = [f'<{field}_item>']
            elif field_type == 'string':
                # Check for recommended defaults
                if requirement == 'RECOMMENDED':
                    if field == 'description':
                        fm_dict[field] = f'<Brief description of this {self.get_doc_type()}>'
                    elif field == 'version':
                        fm_dict[field] = '1.0.0'
                    else:
                        fm_dict[field] = f'<{field.replace("_", " ").title()}>'
                elif requirement == 'OPTIONAL':
                    fm_dict[field] = f'<optional {field}>'
                else:
                    fm_dict[field] = f'<{field.replace("_", " ").title()}>'
            elif field_type == 'datetime':
                fm_dict[field] = 'YYYY-MM-DDTHH:MM:SSZ'
            else:
                fm_dict[field] = f'<{field}>'

        # Add nested objects to fm_dict
        for parent, children in nested_objects.items():
            fm_dict[parent] = {}
            for child, child_spec in children.items():
                child_type = child_spec['type']
                child_req = child_spec['requirement']

                if child_type == 'array[string]':
                    if child_req == 'OPTIONAL':
                        fm_dict[parent][child] = []
                    else:
                        fm_dict[parent][child] = [f'<{child}_id>']
                elif child_type == 'string':
                    fm_dict[parent][child] = f'<{child}>'
                else:
                    fm_dict[parent][child] = f'<{child}>'

        # Convert to YAML with proper formatting
        lines = []
        for key, value in fm_dict.items():
            if isinstance(value, dict):
                # Nested object
                lines.append(f"{key}:")
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, list):
                        lines.append(f"  {sub_key}:")
                        if sub_value:  # Non-empty array
                            for item in sub_value:
                                lines.append(f"    - {item}")
                        else:  # Empty array (OPTIONAL field)
                            lines.append(f"    []")
                    else:
                        lines.append(f"  {sub_key}: {sub_value}")
            elif isinstance(value, str) and '\n' in value:
                # This is a pre-formatted multi-line string (object array placeholder)
                lines.append(value)
            elif isinstance(value, list):
                lines.append(f"{key}:")
                for item in value:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{key}: {value}")

        # If no frontmatter fields were generated, return empty YAML object
        if not lines:
            return "{}\n"

        return "\n".join(lines) + "\n"

    def generate_field_placeholder(self, field: str, field_type: str) -> str:
        """Generate a placeholder value for a field based on its type."""
        if field_type == 'datetime':
            return 'YYYY-MM-DDTHH:MM:SSZ'
        elif field_type == 'string':
            # Special cases for common fields
            if field == 'file':
                return '<path>'
            elif field == 'format':
                return '<format>'
            else:
                return f'<{field}>'
        else:
            return f'<{field}>'

    def generate_object_array_placeholder(self, field_name: str, object_fields: List[Dict], is_optional: bool) -> str:
        """Generate placeholder for array of objects with proper YAML structure."""
        if is_optional:
            # Optional array - show commented example
            lines = [f"{field_name}:  # OPTIONAL"]
            # Add first array item marker
            lines.append("  -")
            # Add all object fields
            for obj_field in object_fields:
                field = obj_field['field']
                field_type = obj_field['type']
                if field_type == 'datetime':
                    lines.append(f"    {field}: YYYY-MM-DDTHH:MM:SSZ")
                else:
                    placeholder = self.generate_field_placeholder(field, field_type)
                    lines.append(f"    {field}: {placeholder}")
        else:
            # Required array
            lines = [f"{field_name}:"]
            # Add first array item marker
            lines.append("  -")
            # Add all object fields
            for obj_field in object_fields:
                field = obj_field['field']
                field_type = obj_field['type']
                if field_type == 'datetime':
                    lines.append(f"    {field}: YYYY-MM-DDTHH:MM:SSZ")
                else:
                    placeholder = self.generate_field_placeholder(field, field_type)
                    lines.append(f"    {field}: {placeholder}")

        return "\n".join(lines)

    def get_doc_type(self) -> str:
        """Extract document type name from spec."""
        name = self.spec.frontmatter.get('name', '')
        doc_type = name.replace('Specification for ', '').replace(' Documents', '')
        return doc_type.lower()

    def generate_body(self) -> str:
        """Generate template body from spec requirements."""
        sections = self.spec.extract_body_sections()

        body_parts = []

        # Add title
        doc_type = self.spec.frontmatter.get('name', 'Document').replace('Specification for ', '').replace(' Documents', '')
        body_parts.append(f"# {doc_type} - <Name>\n")

        # Add sections
        for section in sections:
            name = section['name']
            format_example = section['format']
            requirements = section.get('requirements', [])

            body_parts.append(f"## {name}\n")

            if format_example:
                # Clean up format example (remove ## if present, it's already added)
                example = format_example
                if example.startswith('## '):
                    example = example.split('\n', 1)[1] if '\n' in example else ''

                body_parts.append(f"{example}\n")
            else:
                # Generate placeholder from requirements if available
                if requirements:
                    # Use first requirement as hint
                    hint = requirements[0].replace('MUST ', '').replace('SHOULD ', '')
                    body_parts.append(f"[{hint}]\n")
                else:
                    body_parts.append(f"[{name} content]\n")

        # Add footer note
        body_parts.append("---\n")
        body_parts.append("\n**Note:** This document is part of the PPP (Persona-Purpose-Protocol) framework.\n")

        return "\n".join(body_parts)

    def pattern_to_placeholder(self, pattern: str) -> str:
        """Convert a format pattern to a template placeholder."""
        # Replace patterns like v:persona:<name> with v:persona:<name>
        # Keep literal parts, preserve <placeholders>
        return pattern

    def format_to_placeholder(self, format_text: str) -> str:
        """Convert format example to template placeholder."""
        # Replace content in brackets with placeholders
        result = format_text
        result = re.sub(r'\[([^\]]+)\]', r'[\1]', result)
        return result


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate Obsidian template from specification document'
    )
    parser.add_argument(
        'spec_path',
        type=Path,
        help='Path to specification document (e.g., 00_vertices/spec-for-persona.md)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output path for generated template (default: auto-determined)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Print detailed generation info'
    )

    args = parser.parse_args()

    # Validate input
    if not args.spec_path.exists():
        print(f"Error: Spec file not found: {args.spec_path}")
        return 1

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        # Auto-determine from spec name
        # spec-for-persona.md → templates/00_vertices/persona.md
        spec_name = args.spec_path.stem  # spec-for-persona
        if spec_name.startswith('spec-for-'):
            doc_type = spec_name.replace('spec-for-', '')
            output_path = Path('templates') / '00_vertices' / f'{doc_type}.md'
        else:
            print(f"Error: Could not determine output path for {spec_name}")
            return 1

    # Parse spec
    if args.verbose:
        print(f"Parsing spec: {args.spec_path}")

    spec_parser = SpecParser(args.spec_path)

    if args.verbose:
        fm_reqs = spec_parser.extract_frontmatter_requirements()
        print(f"  Found {len(fm_reqs)} frontmatter requirements")

        body_sections = spec_parser.extract_body_sections()
        print(f"  Found {len(body_sections)} body sections")

    # Generate template
    if args.verbose:
        print(f"\nGenerating template...")

    generator = TemplateGenerator(spec_parser)
    template_content = generator.generate_template()

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(template_content, encoding='utf-8')

    print(f"✓ Generated template: {output_path}")
    print(f"  Lines: {len(template_content.splitlines())}")
    print(f"  Size: {len(template_content)} bytes")

    return 0


if __name__ == '__main__':
    sys.exit(main())
