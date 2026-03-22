#!/usr/bin/env python
"""
Tests for template parser functionality.
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from template_parser import TemplateParser, TemplateSpec


def get_templates_dir():
    """Get the templates directory - use bundled templates from src/aaa/templates."""
    repo_root = Path(__file__).parent.parent
    return repo_root / 'src' / 'aaa' / 'templates'


def test_load_all_templates():
    """Test that all templates load successfully."""
    templates_dir = get_templates_dir()
    parser = TemplateParser(templates_dir)
    parser.load_all_templates()

    assert len(parser.templates) > 0, "No templates loaded"
    print(f"✓ Loaded {len(parser.templates)} templates")


def test_validation_edge_template():
    """Test validation edge template parsing."""
    templates_dir = get_templates_dir()
    parser = TemplateParser(templates_dir)
    parser.load_all_templates()

    template = parser.get_template('edge/validation')
    assert template is not None, "Validation edge template not found"
    assert template.type == 'edge/validation'
    assert template.extends == 'edge'

    # Check frontmatter requirements
    field_names = [req.field for req in template.frontmatter_requirements]
    assert 'type' in field_names, "Missing 'type' field requirement"
    assert 'validator' in field_names, "Missing 'validator' field requirement"
    assert 'validation_method' in field_names, "Missing 'validation_method' field requirement"

    # Check conditional requirements
    llm_model_req = next((r for r in template.frontmatter_requirements if r.field == 'llm_model'), None)
    assert llm_model_req is not None, "Missing 'llm_model' field requirement"
    assert llm_model_req.conditional is not None, "llm_model should be conditional"
    assert 'validation_method' in llm_model_req.conditional, "llm_model condition should reference validation_method"

    # Check body requirements
    assert len(template.body_requirements) > 0, "No body requirements found"
    assert any('Validation Assessment' in section for section in template.body_requirements), \
        "Missing 'Validation Assessment' section requirement"

    # Check tag requirements
    assert 'edge' in template.tag_requirements, "Missing 'edge' tag requirement"
    assert 'validation' in template.tag_requirements, "Missing 'validation' tag requirement"

    print("✓ Validation edge template parsed correctly")


def test_assurance_face_template():
    """Test assurance face template parsing."""
    templates_dir = get_templates_dir()
    parser = TemplateParser(templates_dir)
    parser.load_all_templates()

    template = parser.get_template('face/assurance')
    assert template is not None, "Assurance face template not found"
    assert template.type == 'face/assurance'
    assert template.extends == 'face'

    # Check frontmatter requirements (from template frontmatter)
    field_names = [req.field for req in template.frontmatter_requirements]
    assert 'assurer' in field_names, "Missing 'assurer' field requirement"
    assert 'assurance_method' in field_names, "Missing 'assurance_method' field requirement"

    # Check conditional requirements
    llm_model_req = next((r for r in template.frontmatter_requirements if r.field == 'llm_model'), None)
    human_approver_req = next((r for r in template.frontmatter_requirements if r.field == 'human_approver'), None)

    assert llm_model_req is not None, "Missing 'llm_model' field requirement"
    assert human_approver_req is not None, "Missing 'human_approver' field requirement"

    print("✓ Assurance face template parsed correctly")


def test_conditional_evaluation():
    """Test conditional requirement evaluation."""
    templates_dir = get_templates_dir()
    parser = TemplateParser(templates_dir)
    parser.load_all_templates()

    # Test validation_method condition
    frontmatter_manual = {'validation_method': 'manual'}
    frontmatter_llm = {'validation_method': 'llm-assisted'}

    assert not parser.evaluate_conditional('validation_method==llm-assisted', frontmatter_manual), \
        "Should not match manual method"
    assert parser.evaluate_conditional('validation_method==llm-assisted', frontmatter_llm), \
        "Should match llm-assisted method"

    print("✓ Conditional evaluation works correctly")


def run_all_tests():
    """Run all tests."""
    tests = [
        test_load_all_templates,
        test_validation_edge_template,
        test_assurance_face_template,
        test_conditional_evaluation,
    ]

    print("=" * 70)
    print("Template Parser Tests")
    print("=" * 70)

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}")
            failed += 1

    print("=" * 70)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 70)

    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
