#!/usr/bin/env python
"""
Tests for template-based verification functionality.
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from verify_template_based import TemplateBasedVerifier


def get_templates_dir():
    """Get the templates directory - use bundled templates from src/aaa/templates."""
    repo_root = Path(__file__).parent.parent
    return repo_root / 'src' / 'aaa' / 'templates'


def test_validation_edges():
    """Test that all validation edges verify successfully."""
    repo_root = Path(__file__).parent.parent
    templates_dir = get_templates_dir()
    verifier = TemplateBasedVerifier(templates_dir, verbose=False)

    # Scan all content directories for validation edges
    validation_edges = list((repo_root / '01_edges').glob('validation-*.md'))
    for content_dir in (repo_root / 'content').glob('*/01_edges'):
        validation_edges.extend(content_dir.glob('validation-*.md'))
    # Also check foundation
    foundation_edges = list((repo_root / 'src' / 'aaa' / 'foundation' / '01_edges').glob('validation-*.md'))
    validation_edges.extend(foundation_edges)

    assert len(validation_edges) >= 4, f"Expected at least 4 validation edges, found {len(validation_edges)}"

    for edge_path in validation_edges:
        passed = verifier.verify_element(edge_path)
        assert passed, f"Verification failed for {edge_path.name}: {verifier.errors}"
        print(f"✓ {edge_path.name}: {verifier.checks_passed}/{verifier.checks_total} checks passed")

    print(f"✓ All {len(validation_edges)} validation edges verified")


def test_verification_edges():
    """Test that all verification edges verify successfully."""
    repo_root = Path(__file__).parent.parent
    templates_dir = get_templates_dir()
    verifier = TemplateBasedVerifier(templates_dir, verbose=False)

    # Scan all content directories for verification edges
    verification_edges = list((repo_root / '01_edges').glob('verification-*.md'))
    for content_dir in (repo_root / 'content').glob('*/01_edges'):
        verification_edges.extend(content_dir.glob('verification-*.md'))
    # Also check foundation
    foundation_edges = list((repo_root / 'src' / 'aaa' / 'foundation' / '01_edges').glob('verification-*.md'))
    verification_edges.extend(foundation_edges)

    assert len(verification_edges) >= 4, f"Expected at least 4 verification edges, found {len(verification_edges)}"

    for edge_path in verification_edges:
        passed = verifier.verify_element(edge_path)
        assert passed, f"Verification failed for {edge_path.name}: {verifier.errors}"
        print(f"✓ {edge_path.name}: {verifier.checks_passed}/{verifier.checks_total} checks passed")

    print(f"✓ All {len(verification_edges)} verification edges verified")


def test_coupling_edges():
    """Test that all boundary complex coupling edges verify successfully."""
    repo_root = Path(__file__).parent.parent
    templates_dir = get_templates_dir()
    verifier = TemplateBasedVerifier(templates_dir, verbose=False)

    # Scan all content directories for coupling edges
    coupling_edges = list((repo_root / '01_edges').glob('coupling-*.md'))
    for content_dir in (repo_root / 'content').glob('*/01_edges'):
        coupling_edges.extend(content_dir.glob('coupling-*.md'))
    # Also check foundation
    foundation_edges = list((repo_root / 'src' / 'aaa' / 'foundation' / '01_edges').glob('coupling-*.md'))
    coupling_edges.extend(foundation_edges)

    assert len(coupling_edges) >= 2, f"Expected at least 2 coupling edges, found {len(coupling_edges)}"

    for edge_path in coupling_edges:
        passed = verifier.verify_element(edge_path)
        assert passed, f"Verification failed for {edge_path.name}: {verifier.errors}"
        print(f"✓ {edge_path.name}: {verifier.checks_passed}/{verifier.checks_total} checks passed")

    print(f"✓ All {len(coupling_edges)} coupling edges verified")


def test_assurance_faces():
    """Test that all boundary complex assurance faces verify successfully."""
    repo_root = Path(__file__).parent.parent
    templates_dir = get_templates_dir()
    verifier = TemplateBasedVerifier(templates_dir, verbose=False)

    # Scan all content directories for assurance faces
    assurance_faces = list((repo_root / '02_faces').glob('assurance-*.md'))
    for content_dir in (repo_root / 'content').glob('*/02_faces'):
        assurance_faces.extend(content_dir.glob('assurance-*.md'))
    # Also check foundation
    foundation_faces = list((repo_root / 'src' / 'aaa' / 'foundation' / '02_faces').glob('assurance-*.md'))
    assurance_faces.extend(foundation_faces)

    assert len(assurance_faces) >= 4, f"Expected at least 4 assurance faces, found {len(assurance_faces)}"

    for face_path in assurance_faces:
        passed = verifier.verify_element(face_path)
        assert passed, f"Verification failed for {face_path.name}: {verifier.errors}"
        print(f"✓ {face_path.name}: {verifier.checks_passed}/{verifier.checks_total} checks passed")

    print(f"✓ All {len(assurance_faces)} assurance faces verified")


def test_foundational_vertices():
    """Test that all foundational vertices verify successfully."""
    repo_root = Path(__file__).parent.parent
    templates_dir = get_templates_dir()
    verifier = TemplateBasedVerifier(templates_dir, verbose=False)

    # Test the 4 boundary complex vertices
    vertices = [
        'spec-for-spec.md',
        'spec-for-guidance.md',
        'guidance-for-spec.md',
        'guidance-for-guidance.md',
    ]

    for vertex_name in vertices:
        vertex_path = repo_root / '00_vertices' / vertex_name
        if not vertex_path.exists():
            print(f"⚠ Skipping {vertex_name} (not found)")
            continue

        passed = verifier.verify_element(vertex_path)
        assert passed, f"Verification failed for {vertex_name}: {verifier.errors}"
        print(f"✓ {vertex_name}: {verifier.checks_passed}/{verifier.checks_total} checks passed")

    print("✓ All foundational vertices verified")


def test_conditional_requirements():
    """Test that conditional requirements work correctly."""
    repo_root = Path(__file__).parent.parent
    templates_dir = get_templates_dir()
    verifier = TemplateBasedVerifier(templates_dir, verbose=False)

    # Test llm-assisted validation edge (should require llm_model and human_approver)
    llm_edge = repo_root / '01_edges' / 'validation-spec-guidance.md'
    if llm_edge.exists():
        passed = verifier.verify_element(llm_edge)
        assert passed, f"LLM-assisted validation edge should pass: {verifier.errors}"
        print("✓ LLM-assisted validation edge conditional requirements work")

    # Test automated validation edge (should require human_approver but not llm_model)
    auto_edge = repo_root / '01_edges' / 'validation-guidance-spec.md'
    if auto_edge.exists():
        passed = verifier.verify_element(auto_edge)
        assert passed, f"Automated validation edge should pass: {verifier.errors}"
        print("✓ Automated validation edge conditional requirements work")


def run_all_tests():
    """Run all tests."""
    tests = [
        test_validation_edges,
        test_verification_edges,
        test_coupling_edges,
        test_assurance_faces,
        test_foundational_vertices,
        test_conditional_requirements,
    ]

    print("=" * 70)
    print("Template-Based Verification Tests")
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
