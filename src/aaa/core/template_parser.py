"""
Template Parser for Knowledge Complex

Extracts verification requirements from template files.
Templates become the single source of truth for what fields/sections are required.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any

from .parse import extract_frontmatter


class TemplateRequirement:
    """Represents a single requirement extracted from a template."""

    def __init__(
        self,
        field: str,
        required: bool = True,
        expected_value: Optional[Any] = None,
        conditional: Optional[str] = None,
        field_type: Optional[type] = None
    ):
        self.field = field
        self.required = required
        self.expected_value = expected_value
        self.conditional = conditional  # e.g., "validation_method == 'llm-assisted'"
        self.field_type = field_type


class TemplateSpec:
    """Specification extracted from a template file."""

    def __init__(self, template_path: Path):
        self.template_path = template_path
        self.type = None
        self.extends = None
        self.frontmatter_requirements: List[TemplateRequirement] = []
        self.body_requirements: List[str] = []  # Required section headers
        self.tag_requirements: List[str] = []

    def add_frontmatter_requirement(self, req: TemplateRequirement):
        """Add a frontmatter field requirement."""
        self.frontmatter_requirements.append(req)

    def add_body_requirement(self, section_header: str):
        """Add a required body section."""
        self.body_requirements.append(section_header)

    def add_tag_requirement(self, tag: str):
        """Add a required tag."""
        self.tag_requirements.append(tag)


class TemplateParser:
    """Parses template files to extract verification requirements."""

    def __init__(self, templates_dir: Path):
        self.templates_dir = Path(templates_dir)
        self.templates: Dict[str, TemplateSpec] = {}

    def load_all_templates(self):
        """Load all templates from the templates directory."""
        for template_file in self.templates_dir.rglob("*.md"):
            if template_file.name.startswith('.'):
                continue
            try:
                spec = self.parse_template(template_file)
                if spec.type:
                    self.templates[spec.type] = spec
            except Exception as e:
                print(f"Warning: Could not parse template {template_file}: {e}")

    def parse_template(self, template_path: Path) -> TemplateSpec:
        """Parse a single template file."""
        spec = TemplateSpec(template_path)

        content = template_path.read_text(encoding='utf-8')
        frontmatter, body = extract_frontmatter(content)

        if not frontmatter:
            return spec

        # Extract type from frontmatter
        spec.type = frontmatter.get('type', '')
        # Remove 'template/' prefix if present
        if spec.type.startswith('template/'):
            spec.type = spec.type.replace('template/', '', 1)

        spec.extends = frontmatter.get('extends')

        # Parse frontmatter requirements from template's own frontmatter
        self._parse_frontmatter_from_template(frontmatter, spec)

        # Parse frontmatter requirements from body tables
        self._parse_frontmatter_table(body, spec)

        # Parse body section requirements
        self._parse_body_requirements(body, spec)

        # Parse tag requirements
        self._parse_tag_requirements(body, spec)

        return spec

    def _parse_frontmatter_from_template(self, frontmatter: Dict[str, Any], spec: TemplateSpec):
        """
        Parse frontmatter requirements from the template's own frontmatter.

        For templates without a requirements table in the body, we can extract
        requirements from the template frontmatter itself, reading inline comments.
        """
        # Get the raw template content to read comments
        content = spec.template_path.read_text(encoding='utf-8')

        # Extract frontmatter section (between ---markers)
        fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            return

        fm_text = fm_match.group(1)

        # Parse each line for field definitions and comments
        for line in fm_text.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Look for field: value # comment patterns
            match = re.match(r'(\w+):\s*(.+?)(?:\s*#\s*(.+))?$', line)
            if not match:
                continue

            field_name = match.group(1)
            field_value = match.group(2).strip()
            comment = match.group(3).strip() if match.group(3) else ''

            # Skip template-specific fields
            if field_name in ['type', 'extends', 'id', 'name', 'description', 'instantiable', 'version', 'created', 'modified']:
                continue

            # Check if comment indicates conditional requirement
            conditional = None
            if 'REQUIRED for' in comment or 'REQUIRED when' in comment or 'REQUIRED if' in comment:
                # Extract condition
                cond_match = re.search(r'REQUIRED (?:for|when|if) (\w+)', comment)
                if cond_match:
                    cond_value = cond_match.group(1)
                    # Assume the condition is method-based (validation_method, assurance_method, etc.)
                    # Find the method field
                    method_field = None
                    if 'validation_method' in fm_text:
                        method_field = 'validation_method'
                    elif 'assurance_method' in fm_text:
                        method_field = 'assurance_method'

                    if method_field:
                        conditional = f"{method_field}=={cond_value}"

            # Determine if required (has no default placeholder)
            required = '<' not in field_value and not field_value.startswith('"<')

            # For array fields, check if it's required
            if field_value.startswith('-'):
                required = True

            # Create requirement
            req = TemplateRequirement(
                field=field_name,
                required=required,
                conditional=conditional
            )
            spec.add_frontmatter_requirement(req)

    def _parse_frontmatter_table(self, body: str, spec: TemplateSpec):
        """
        Parse the 'Required Frontmatter Fields' table to extract requirements.

        Looks for patterns like:
        | `type` | string | Must be `edge/validation` |
        | `llm_model` | string | REQUIRED if `validation_method` is `llm-assisted` |
        """
        # Find the frontmatter table
        table_pattern = r'\|\s*Field\s*\|\s*Type\s*\|\s*Description\s*\|.*?\n((?:\|.*?\n)+)'
        match = re.search(table_pattern, body, re.DOTALL | re.IGNORECASE)

        if not match:
            return

        table_content = match.group(1)

        # Parse each row
        for line in table_content.split('\n'):
            if not line.strip() or line.strip().startswith('|---'):
                continue

            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 4:
                continue

            field_name = parts[1].strip('`').strip()
            field_type_str = parts[2].strip().lower()
            description = parts[3].strip()

            if not field_name:
                continue

            # Map type strings to Python types
            field_type = {
                'string': str,
                'array': list,
                'datetime': str,
                'boolean': bool,
                'number': (int, float),
            }.get(field_type_str, str)

            # Check if it's a conditional requirement
            conditional = None
            if 'REQUIRED if' in description or 'REQUIRED when' in description:
                # Extract the condition
                cond_match = re.search(r'REQUIRED (?:if|when) `?([^`]+)`? (?:is|==) `?([^`\s]+)`?', description)
                if cond_match:
                    cond_field = cond_match.group(1)
                    cond_value = cond_match.group(2)
                    conditional = f"{cond_field}=={cond_value}"

            # Check if there's an expected value
            expected_value = None
            if 'Must be' in description:
                value_match = re.search(r'Must be `([^`]+)`', description)
                if value_match:
                    expected_value = value_match.group(1)

            # Check if it's marked as deprecated or optional
            required = 'DEPRECATED' not in description and 'optional' not in description.lower()

            # For conditional fields, they're required when condition is met
            if conditional:
                required = True

            req = TemplateRequirement(
                field=field_name,
                required=required,
                expected_value=expected_value,
                conditional=conditional,
                field_type=field_type
            )
            spec.add_frontmatter_requirement(req)

    def _parse_body_requirements(self, body: str, spec: TemplateSpec):
        """
        Parse required body sections.

        Looks for patterns like:
        ### Required Section: Validation Assessment
        ## Body Content Requirements
        The markdown body MUST contain...
        """
        # Look for "Required Section:" patterns
        required_sections = re.findall(r'###\s*Required Section:\s*(.+)', body)
        for section in required_sections:
            section_header = f"## {section.strip()}"
            spec.add_body_requirement(section_header)

        # Look for "MUST contain '## Section Name'" patterns
        must_contain = re.findall(r"MUST contain ['\"]## ([^'\"]+)['\"]", body)
        for section in must_contain:
            section_header = f"## {section.strip()}"
            if section_header not in spec.body_requirements:
                spec.add_body_requirement(section_header)

    def _parse_tag_requirements(self, body: str, spec: TemplateSpec):
        """
        Parse required tags.

        Looks for patterns like:
        tags:
          - edge         # base type
          - validation   # concrete type
        """
        # Find tag requirements section
        tag_pattern = r'```yaml\s*tags:\s*((?:\s*-\s*\w+(?:\s*#[^\n]*)?\s*\n?)+)\s*```'
        matches = re.findall(tag_pattern, body)

        for match in matches:
            # Extract tag names (ignore comments)
            tags = re.findall(r'-\s*(\w+)', match)
            for tag in tags:
                if tag not in spec.tag_requirements:
                    spec.add_tag_requirement(tag)

        # Also look for "Must include [tag1, tag2]" patterns
        must_include = re.findall(r'Must include `?\[([^\]]+)\]`?', body)
        for tag_list in must_include:
            tags = [t.strip().strip('`').strip("'").strip('"') for t in tag_list.split(',')]
            for tag in tags:
                if tag and tag not in spec.tag_requirements:
                    spec.add_tag_requirement(tag)

    def get_template(self, element_type: str) -> Optional[TemplateSpec]:
        """Get the template spec for a given element type."""
        return self.templates.get(element_type)

    def evaluate_conditional(self, conditional: str, frontmatter: Dict[str, Any]) -> bool:
        """
        Evaluate a conditional requirement.

        Args:
            conditional: String like "validation_method==llm-assisted"
            frontmatter: The document's frontmatter

        Returns:
            True if the condition is met, False otherwise
        """
        if not conditional:
            return False

        # Parse simple equality conditions
        match = re.match(r'(\w+)==(.+)', conditional)
        if match:
            field = match.group(1)
            expected = match.group(2).strip("'\"")
            actual = frontmatter.get(field, '')
            return str(actual) == expected

        return False
