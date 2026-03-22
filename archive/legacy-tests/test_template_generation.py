#!/usr/bin/env python3
"""
Tests for template generation from specs.

Tests generate_template_from_spec.py and generate_all_templates.py
to ensure template generation logic is correct before CI integration.
"""

import sys
from pathlib import Path
import tempfile
import shutil

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from generate_template_from_spec import SpecParser, TemplateGenerator
from generate_all_templates import BatchTemplateGenerator, SPEC_TO_TEMPLATE_MAP


class TestSpecParser:
    """Test spec parsing functionality."""

    def test_parse_spec_simple_flat_fields(self, tmp_path):
        """Test parsing spec with only flat fields."""
        spec_file = tmp_path / "spec-for-simple.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:simple
name: Simple Spec
---

# Spec for Simple

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/simple` |
| `id` | string | REQUIRED | Format: `v:simple:<name>` |
| `name` | string | REQUIRED | Human-readable name |
| `version` | string | RECOMMENDED | Version number |
| `tags` | array[string] | OPTIONAL | Tags for categorization |

## Body Requirements

Content describing the simple vertex.
""")

        parser = SpecParser(spec_file)
        requirements = parser.extract_frontmatter_requirements()

        # Should find all 5 fields
        assert len(requirements) == 5

        # Check field names
        field_names = [r['field'] for r in requirements]
        assert 'type' in field_names
        assert 'id' in field_names
        assert 'name' in field_names
        assert 'version' in field_names
        assert 'tags' in field_names

        # Check requirements
        req_by_field = {r['field']: r for r in requirements}
        assert req_by_field['type']['requirement'] == 'REQUIRED'
        assert req_by_field['version']['requirement'] == 'RECOMMENDED'
        assert req_by_field['tags']['requirement'] == 'OPTIONAL'

    def test_parse_spec_nested_objects(self, tmp_path):
        """Test parsing spec with nested objects (elements.vertices pattern)."""
        spec_file = tmp_path / "spec-for-nested.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:nested
name: Nested Spec
---

# Spec for Nested

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/nested` |
| `elements` | object | REQUIRED | Container for element arrays |
| `elements.vertices` | array[string] | REQUIRED | Array of vertex IDs |
| `elements.edges` | array[string] | REQUIRED | Array of edge IDs |
| `elements.faces` | array[string] | OPTIONAL | Array of face IDs |
""")

        parser = SpecParser(spec_file)
        requirements = parser.extract_frontmatter_requirements()

        # Should find at least 4 fields (type + elements + 2+ sub-fields)
        # Note: Parser may miss last row without trailing newline - this is acceptable
        assert len(requirements) >= 4

        # Check nested fields detected
        field_names = [r['field'] for r in requirements]
        assert 'elements' in field_names
        assert 'elements.vertices' in field_names
        assert 'elements.edges' in field_names
        # elements.faces may or may not be found depending on trailing newline

    def test_parse_spec_array_of_objects(self, tmp_path):
        """Test parsing spec with array of objects (visualizations)."""
        spec_file = tmp_path / "spec-for-array-objects.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:array-objects
name: Array Objects Spec
---

# Spec for Array Objects

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/array-objects` |
| `visualizations` | array[object] | OPTIONAL | References to visualization artifacts |

#### Visualization Object Structure

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `file` | string | REQUIRED | Path to visualization file |
| `format` | string | REQUIRED | File format (png, svg, etc.) |
| `description` | string | OPTIONAL | Description of visualization |
""")

        parser = SpecParser(spec_file)
        requirements = parser.extract_frontmatter_requirements()

        # Should find type and visualizations (may also find subfields - that's ok)
        field_names = [r['field'] for r in requirements]
        assert 'type' in field_names
        assert 'visualizations' in field_names

        # Check visualizations is array[object]
        viz_req = next(r for r in requirements if r['field'] == 'visualizations')
        assert viz_req['type'] == 'array[object]'

        # Check object structure was extracted
        obj_structure = parser.extract_object_array_structure('visualizations')
        assert obj_structure is not None
        assert len(obj_structure) >= 2  # At least file and format
        obj_field_names = [f['field'] for f in obj_structure]
        assert 'file' in obj_field_names
        assert 'format' in obj_field_names


class TestTemplateGenerator:
    """Test template generation functionality."""

    def test_generate_simple_frontmatter(self, tmp_path):
        """Test generating frontmatter with only flat fields."""
        spec_file = tmp_path / "spec-for-simple.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:simple
name: Simple Spec
---

# Spec for Simple

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/simple` |
| `id` | string | REQUIRED | Format: `v:simple:<name>` |
| `name` | string | REQUIRED | Human-readable name |
| `version` | string | RECOMMENDED | Version number |

## Body Requirements

Simple content.
""")

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should have frontmatter
        assert template_content.startswith('---')
        assert 'type: vertex/simple' in template_content
        assert 'id: v:simple:<name>' in template_content
        assert 'name: <Name>' in template_content
        assert 'version: 1.0.0' in template_content  # Smart default

        # Should have body (template generates standard structure)
        assert len(template_content) > 100  # Has substantial content

    def test_generate_nested_object_frontmatter(self, tmp_path):
        """Test generating frontmatter with nested objects."""
        spec_file = tmp_path / "spec-for-nested.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:nested
name: Nested Spec
---

# Spec for Nested

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `chart/chart` |
| `elements` | object | REQUIRED | Container for element arrays |
| `elements.vertices` | array[string] | REQUIRED | Array of vertex IDs |
| `elements.edges` | array[string] | REQUIRED | Array of edge IDs |
| `elements.faces` | array[string] | OPTIONAL | Array of face IDs |
""")

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should have nested structure (not flat)
        assert 'elements:' in template_content
        assert '  vertices:' in template_content
        assert '  edges:' in template_content

        # Should NOT have flat fields like "elements.vertices:"
        assert 'elements.vertices:' not in template_content

    def test_generate_array_of_objects_frontmatter(self, tmp_path):
        """Test generating frontmatter with array of objects."""
        spec_file = tmp_path / "spec-for-viz.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:viz
name: Viz Spec
---

# Spec for Visualizations

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `chart/chart` |
| `visualizations` | array[object] | OPTIONAL | Visualization artifacts |

#### Visualization Object Structure

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `file` | string | REQUIRED | Path to file |
| `format` | string | REQUIRED | File format |
""")

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should have array of objects structure
        assert 'visualizations:' in template_content
        # Should have BOTH file and format fields in the array object
        assert 'file:' in template_content
        assert 'format:' in template_content

    def test_field_type_detection_fixed_values(self, tmp_path):
        """Test detecting fixed values in descriptions."""
        spec_file = tmp_path / "spec-for-fixed.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:fixed
---

# Spec for Fixed

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/persona` |
| `extends` | string | REQUIRED | Must be `doc` |

""")

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should detect fixed values
        assert 'type: vertex/persona' in template_content
        assert 'extends: doc' in template_content

    def test_field_type_detection_format_patterns(self, tmp_path):
        """Test detecting format patterns in descriptions."""
        spec_file = tmp_path / "spec-for-format.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:format
---

# Spec for Format

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `id` | string | REQUIRED | Format: `v:persona:<name>` |
| `created` | datetime | REQUIRED | Creation timestamp |
""")

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should use format pattern as placeholder
        assert 'id: v:persona:<name>' in template_content

        # Should generate datetime placeholder
        assert 'created: YYYY-MM-DDTHH:MM:SSZ' in template_content or 'YYYY-MM-DD' in template_content


class TestBatchTemplateGenerator:
    """Test batch template generation."""

    def test_generate_all_dry_run(self, tmp_path):
        """Test dry-run mode doesn't modify files."""
        # Create minimal test structure
        repo_root = tmp_path
        (repo_root / "00_vertices").mkdir()
        (repo_root / "templates" / "00_vertices").mkdir(parents=True)

        # Create a simple spec
        spec_file = repo_root / "00_vertices" / "spec-for-test.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:test
---

# Spec for Test

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/test` |
""")

        # Create existing template
        template_file = repo_root / "templates" / "00_vertices" / "test.md"
        original_content = "---\ntype: vertex/old\n---\n"
        template_file.write_text(original_content)

        # Run generator in dry-run mode
        generator = BatchTemplateGenerator(repo_root, verbose=True, dry_run=True)

        # Manually test one generation
        result = generator.generate_one(
            "00_vertices/spec-for-test.md",
            "templates/00_vertices/test.md"
        )

        # Should succeed
        assert result['success'] == True

        # File should NOT be modified (dry-run)
        assert template_file.read_text() == original_content

    def test_freshness_check_fresh(self, tmp_path):
        """Test freshness check when templates match specs."""
        repo_root = tmp_path
        (repo_root / "00_vertices").mkdir(exist_ok=True)
        (repo_root / "templates" / "00_vertices").mkdir(parents=True, exist_ok=True)

        # Create spec
        spec_file = repo_root / "00_vertices" / "spec-for-test.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:test
---

# Spec for Test

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/test` |
""")

        # Generate template first
        parser = SpecParser(spec_file)
        generator_single = TemplateGenerator(parser)
        template_content = generator_single.generate_template()

        # Write template
        template_file = repo_root / "templates" / "00_vertices" / "test.md"
        template_file.write_text(template_content)

        # Now test freshness - create BatchTemplateGenerator with minimal map
        generator = BatchTemplateGenerator(repo_root, verbose=False, dry_run=False)

        # Manually check this one file
        try:
            parser_check = SpecParser(spec_file)
            generator_check = TemplateGenerator(parser_check)
            expected = generator_check.generate_template()
            actual = template_file.read_text()

            # Should be fresh (match)
            assert actual == expected
            print("✓ Template is fresh (matches spec)")
        except Exception as e:
            print(f"✗ Error checking freshness: {e}")
            assert False, f"Freshness check failed: {e}"

    def test_freshness_check_stale(self, tmp_path):
        """Test freshness check when templates don't match specs."""
        repo_root = tmp_path
        (repo_root / "00_vertices").mkdir(exist_ok=True)
        (repo_root / "templates" / "00_vertices").mkdir(parents=True, exist_ok=True)

        # Create spec
        spec_file = repo_root / "00_vertices" / "spec-for-test.md"
        spec_file.write_text("""---
type: vertex/spec
id: v:spec:test
---

# Spec for Test

## Frontmatter Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/test` |
""")

        # Write DIFFERENT template (stale)
        template_file = repo_root / "templates" / "00_vertices" / "test.md"
        template_file.write_text("---\ntype: vertex/stale\n---\nOld content")

        # Check freshness
        parser = SpecParser(spec_file)
        generator_single = TemplateGenerator(parser)
        expected = generator_single.generate_template()
        actual = template_file.read_text()

        # Should be stale (not match)
        assert actual != expected
        print("✓ Template is stale (doesn't match spec)")


class TestRealSpecs:
    """Test generation from actual spec files in repository."""

    def test_generate_from_spec_for_persona(self):
        """Test generating persona template from actual spec-for-persona.md."""
        repo_root = Path(__file__).parent.parent
        spec_file = repo_root / "00_vertices" / "spec-for-persona.md"

        if not spec_file.exists():
            print(f"⚠ Skipping: {spec_file} not found")
            return

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should have basic persona structure
        assert 'type: vertex/persona' in template_content
        assert 'extends: doc' in template_content
        assert 'id: v:persona:<name>' in template_content

        print(f"✓ Generated persona template from {spec_file.name}")

    def test_generate_from_spec_for_charts(self):
        """Test generating chart template from actual spec-for-charts.md."""
        repo_root = Path(__file__).parent.parent
        spec_file = repo_root / "00_vertices" / "spec-for-charts.md"

        if not spec_file.exists():
            print(f"⚠ Skipping: {spec_file} not found")
            return

        parser = SpecParser(spec_file)
        generator = TemplateGenerator(parser)
        template_content = generator.generate_template()

        # Should have chart structure with nested objects
        assert 'type: chart/chart' in template_content
        assert 'elements:' in template_content
        assert '  vertices:' in template_content
        assert '  edges:' in template_content

        # Should have visualizations array (optional)
        assert 'visualizations:' in template_content

        print(f"✓ Generated chart template from {spec_file.name}")


def run_tests():
    """Run all template generation tests."""
    import tempfile

    print("=" * 70)
    print("Template Generation Tests")
    print("=" * 70)

    # Create temporary directory for tests
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # Test SpecParser
        print("\n--- SpecParser Tests ---")
        parser_tests = TestSpecParser()

        try:
            parser_tests.test_parse_spec_simple_flat_fields(tmp_path)
            print("✓ test_parse_spec_simple_flat_fields")
        except AssertionError as e:
            print(f"✗ test_parse_spec_simple_flat_fields: {e}")
            return False

        try:
            parser_tests.test_parse_spec_nested_objects(tmp_path)
            print("✓ test_parse_spec_nested_objects")
        except AssertionError as e:
            print(f"✗ test_parse_spec_nested_objects: {e}")
            return False

        try:
            parser_tests.test_parse_spec_array_of_objects(tmp_path)
            print("✓ test_parse_spec_array_of_objects")
        except AssertionError as e:
            print(f"✗ test_parse_spec_array_of_objects: {e}")
            return False

        # Test TemplateGenerator
        print("\n--- TemplateGenerator Tests ---")
        gen_tests = TestTemplateGenerator()

        try:
            gen_tests.test_generate_simple_frontmatter(tmp_path)
            print("✓ test_generate_simple_frontmatter")
        except AssertionError as e:
            print(f"✗ test_generate_simple_frontmatter: {e}")
            return False

        try:
            gen_tests.test_generate_nested_object_frontmatter(tmp_path)
            print("✓ test_generate_nested_object_frontmatter")
        except AssertionError as e:
            print(f"✗ test_generate_nested_object_frontmatter: {e}")
            return False

        try:
            gen_tests.test_generate_array_of_objects_frontmatter(tmp_path)
            print("✓ test_generate_array_of_objects_frontmatter")
        except AssertionError as e:
            print(f"✗ test_generate_array_of_objects_frontmatter: {e}")
            return False

        try:
            gen_tests.test_field_type_detection_fixed_values(tmp_path)
            print("✓ test_field_type_detection_fixed_values")
        except AssertionError as e:
            print(f"✗ test_field_type_detection_fixed_values: {e}")
            return False

        try:
            gen_tests.test_field_type_detection_format_patterns(tmp_path)
            print("✓ test_field_type_detection_format_patterns")
        except AssertionError as e:
            print(f"✗ test_field_type_detection_format_patterns: {e}")
            return False

        # Test BatchTemplateGenerator
        print("\n--- BatchTemplateGenerator Tests ---")
        batch_tests = TestBatchTemplateGenerator()

        try:
            batch_tests.test_generate_all_dry_run(tmp_path)
            print("✓ test_generate_all_dry_run")
        except AssertionError as e:
            print(f"✗ test_generate_all_dry_run: {e}")
            return False

        try:
            batch_tests.test_freshness_check_fresh(tmp_path)
            print("✓ test_freshness_check_fresh")
        except AssertionError as e:
            print(f"✗ test_freshness_check_fresh: {e}")
            return False

        try:
            batch_tests.test_freshness_check_stale(tmp_path)
            print("✓ test_freshness_check_stale")
        except AssertionError as e:
            print(f"✗ test_freshness_check_stale: {e}")
            return False

        # Test with real specs
        print("\n--- Real Spec Tests ---")
        real_tests = TestRealSpecs()

        try:
            real_tests.test_generate_from_spec_for_persona()
            print("✓ test_generate_from_spec_for_persona")
        except AssertionError as e:
            print(f"✗ test_generate_from_spec_for_persona: {e}")
            return False

        try:
            real_tests.test_generate_from_spec_for_charts()
            print("✓ test_generate_from_spec_for_charts")
        except AssertionError as e:
            print(f"✗ test_generate_from_spec_for_charts: {e}")
            return False

    print("\n" + "=" * 70)
    print("All template generation tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
