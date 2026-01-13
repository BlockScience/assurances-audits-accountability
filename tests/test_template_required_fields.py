#!/usr/bin/env python3
"""
Regression tests for template required fields.

These tests prevent the bugs discovered during learning journey development:
1. Edge templates missing source_type, target_type, orientation
2. Face templates missing edges list and orientation
3. Parse errors being silently skipped without reporting
"""

from pathlib import Path
import sys
import tempfile

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from parse_chart import (
    parse_edge,
    parse_face,
    parse_directory,
    ParseError
)


class TestEdgeTemplateRequiredFields:
    """Test that edge templates have all required fields."""

    # Templates that don't need these fields (special purpose templates)
    SPECIAL_TEMPLATES = {'inherits.md', 'validation.md', 'verification.md', 'b1.md', 'coupling.md', 'dependency.md'}

    def test_edge_template_has_source_type(self):
        """Edge templates must have source_type field."""
        templates_dir = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges'

        edge_templates = list(templates_dir.glob('*.md'))
        assert len(edge_templates) > 0, "No edge templates found"

        for template_file in edge_templates:
            if template_file.name in self.SPECIAL_TEMPLATES:
                continue
            content = template_file.read_text(encoding='utf-8')
            assert 'source_type:' in content, \
                f"Edge template {template_file.name} missing source_type field"

    def test_edge_template_has_target_type(self):
        """Edge templates must have target_type field."""
        templates_dir = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges'

        edge_templates = list(templates_dir.glob('*.md'))
        assert len(edge_templates) > 0, "No edge templates found"

        for template_file in edge_templates:
            if template_file.name in self.SPECIAL_TEMPLATES:
                continue
            content = template_file.read_text(encoding='utf-8')
            assert 'target_type:' in content, \
                f"Edge template {template_file.name} missing target_type field"

    def test_edge_template_has_orientation(self):
        """Edge templates must have orientation field."""
        templates_dir = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges'

        edge_templates = list(templates_dir.glob('*.md'))
        assert len(edge_templates) > 0, "No edge templates found"

        for template_file in edge_templates:
            if template_file.name in self.SPECIAL_TEMPLATES:
                continue
            content = template_file.read_text(encoding='utf-8')
            assert 'orientation:' in content, \
                f"Edge template {template_file.name} missing orientation field"

    def test_edge_parses_with_all_fields(self, tmp_path):
        """Edge with all required fields should parse successfully."""
        edge_file = tmp_path / "test-edge.md"
        edge_file.write_text("""---
type: edge/has-skill
source: v:student:test-student
target: v:skill:test-skill
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:test-student:test-skill
name: Test edge
tags:
  - edge
  - has-skill
version: 1.0.0
---
Test edge content
""", encoding='utf-8')

        # Should parse without error
        edge = parse_edge(edge_file)
        assert edge['source_type'] == 'vertex/student'
        assert edge['target_type'] == 'vertex/skill'
        assert edge['orientation'] == 'directed'


class TestFaceTemplateRequiredFields:
    """Test that face templates have all required fields."""

    # Templates that don't need these fields (special purpose templates)
    SPECIAL_TEMPLATES = {'assurance.md', 'doc-kit.md', 'b2.md'}

    def test_face_template_has_edges_list(self):
        """Face templates must have edges list field."""
        templates_dir = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '02_faces'

        face_templates = list(templates_dir.glob('*.md'))
        assert len(face_templates) > 0, "No face templates found"

        for template_file in face_templates:
            if template_file.name in self.SPECIAL_TEMPLATES:
                continue
            content = template_file.read_text(encoding='utf-8')
            assert 'edges:' in content, \
                f"Face template {template_file.name} missing edges field"

    def test_face_template_has_orientation(self):
        """Face templates must have orientation field."""
        templates_dir = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '02_faces'

        face_templates = list(templates_dir.glob('*.md'))
        assert len(face_templates) > 0, "No face templates found"

        for template_file in face_templates:
            if template_file.name in self.SPECIAL_TEMPLATES:
                continue
            content = template_file.read_text(encoding='utf-8')
            assert 'orientation:' in content, \
                f"Face template {template_file.name} missing orientation field"

    def test_face_parses_with_all_fields(self, tmp_path):
        """Face with all required fields should parse successfully."""
        face_file = tmp_path / "test-face.md"
        face_file.write_text("""---
type: face/prerequisite
vertices:
  - v:student:test-student
  - v:skill:test-skill
  - v:learning-module:test-module
edges:
  - e:has-skill:test-student:test-skill
  - e:requires-skill:test-module:test-skill
  - e:studies:test-student:test-module
orientation: oriented
id: f:prerequisite:test-student:test-skill:test-module
name: Test face
tags:
  - face
  - prerequisite
version: 1.0.0
---
Test face content
""", encoding='utf-8')

        # Should parse without error
        face = parse_face(face_file)
        assert len(face['edges']) == 3
        assert face['orientation'] == 'oriented'


class TestParseDirectoryErrorReporting:
    """Test that parse_directory reports errors instead of silently skipping."""

    def test_parse_directory_reports_missing_fields(self, tmp_path, capsys):
        """parse_directory should report files with missing required fields."""
        # Create an edge file missing required fields
        bad_edge = tmp_path / "bad-edge.md"
        bad_edge.write_text("""---
type: edge/has-skill
source: v:student:test
target: v:skill:test
id: e:has-skill:test:test
name: Bad edge
tags:
  - edge
version: 1.0.0
---
Missing source_type, target_type, orientation
""", encoding='utf-8')

        # Create a good edge file
        good_edge = tmp_path / "good-edge.md"
        good_edge.write_text("""---
type: edge/has-skill
source: v:student:test
target: v:skill:test
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:test:test2
name: Good edge
tags:
  - edge
version: 1.0.0
---
Good edge
""", encoding='utf-8')

        # Parse directory (takes string type, not parser function)
        elements = parse_directory(tmp_path, 'edge')

        # Should have parsed the good file
        assert len(elements) == 1
        assert elements[0]['id'] == 'e:has-skill:test:test2'

        # Should have printed warning about the bad file
        captured = capsys.readouterr()
        assert "Warning:" in captured.err or "files skipped" in captured.err

    def test_parse_directory_reports_malformed_yaml(self, tmp_path, capsys):
        """parse_directory should report files with malformed YAML."""
        bad_yaml = tmp_path / "bad-yaml.md"
        bad_yaml.write_text("""---
type: edge
  malformed: yaml: structure
---
Bad YAML
""", encoding='utf-8')

        elements = parse_directory(tmp_path, 'edge')

        # Should have skipped the bad file
        assert len(elements) == 0

        # Should have printed warning
        captured = capsys.readouterr()
        assert "Warning:" in captured.err or "files skipped" in captured.err

    def test_parse_directory_success_no_warnings(self, tmp_path, capsys):
        """parse_directory should not print warnings when all files parse successfully."""
        good_edge = tmp_path / "good-edge.md"
        good_edge.write_text("""---
type: edge/has-skill
source: v:student:test
target: v:skill:test
source_type: vertex/student
target_type: vertex/skill
orientation: directed
id: e:has-skill:test:test
name: Good edge
tags:
  - edge
version: 1.0.0
---
Good edge
""", encoding='utf-8')

        elements = parse_directory(tmp_path, 'edge')

        assert len(elements) == 1

        # Should NOT have printed warnings
        captured = capsys.readouterr()
        assert "Warning:" not in captured.err
        assert "files skipped" not in captured.err


class TestLearningJourneyEdgeTemplates:
    """Test learning journey specific edge templates have required fields."""

    def test_has_skill_template(self):
        """has-skill template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges' / 'has-skill.md'
        assert template.exists(), "has-skill template not found"

        content = template.read_text(encoding='utf-8')
        assert 'source_type: vertex/student' in content
        assert 'target_type: vertex/skill' in content
        assert 'orientation: directed' in content

    def test_requires_skill_template(self):
        """requires-skill template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges' / 'requires-skill.md'
        assert template.exists(), "requires-skill template not found"

        content = template.read_text(encoding='utf-8')
        assert 'source_type: vertex/learning-module' in content
        assert 'target_type: vertex/skill' in content
        assert 'orientation: directed' in content

    def test_develops_skill_template(self):
        """develops-skill template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges' / 'develops-skill.md'
        assert template.exists(), "develops-skill template not found"

        content = template.read_text(encoding='utf-8')
        assert 'source_type: vertex/learning-module' in content
        assert 'target_type: vertex/skill' in content
        assert 'orientation: directed' in content

    def test_studies_template(self):
        """studies template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges' / 'studies.md'
        assert template.exists(), "studies template not found"

        content = template.read_text(encoding='utf-8')
        assert 'source_type: vertex/student' in content
        assert 'target_type: vertex/learning-module' in content
        assert 'orientation: directed' in content

    def test_transitions_to_template(self):
        """transitions-to template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges' / 'transitions-to.md'
        assert template.exists(), "transitions-to template not found"

        content = template.read_text(encoding='utf-8')
        assert 'source_type: vertex/student' in content
        assert 'target_type: vertex/student' in content
        assert 'orientation: directed' in content

    def test_advances_template(self):
        """advances template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '01_edges' / 'advances.md'
        assert template.exists(), "advances template not found"

        content = template.read_text(encoding='utf-8')
        assert 'source_type: vertex/learning-module' in content
        assert 'target_type: vertex/student' in content
        assert 'orientation: directed' in content


class TestLearningJourneyFaceTemplates:
    """Test learning journey specific face templates have required fields."""

    def test_prerequisite_template(self):
        """prerequisite template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '02_faces' / 'prerequisite.md'
        assert template.exists(), "prerequisite template not found"

        content = template.read_text(encoding='utf-8')
        assert 'edges:' in content
        assert 'orientation: oriented' in content
        # Should have 3 edges in boundary
        assert 'e:has-skill' in content
        assert 'e:requires-skill' in content
        assert 'e:studies' in content

    def test_completion_template(self):
        """completion template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '02_faces' / 'completion.md'
        assert template.exists(), "completion template not found"

        content = template.read_text(encoding='utf-8')
        assert 'edges:' in content
        assert 'orientation: oriented' in content
        # Should have 3 edges in boundary (studies, transitions-to, advances)
        assert 'e:studies' in content
        assert 'e:transitions-to' in content
        assert 'e:advances' in content

    def test_skill_gain_template(self):
        """skill-gain template has all required fields."""
        template = Path(__file__).parent.parent / 'src' / 'aaa' / 'templates' / '02_faces' / 'skill-gain.md'
        assert template.exists(), "skill-gain template not found"

        content = template.read_text(encoding='utf-8')
        assert 'edges:' in content
        assert 'orientation: oriented' in content
        # Should have 3 edges in boundary (advances, has-skill, develops-skill)
        assert 'e:advances' in content
        assert 'e:has-skill' in content
        assert 'e:develops-skill' in content


def run_tests():
    """Run all template required fields tests."""
    print("=" * 70)
    print("Template Required Fields Regression Tests")
    print("=" * 70)

    import pytest

    # Run pytest on this file
    exit_code = pytest.main([__file__, '-v'])

    return exit_code == 0


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
