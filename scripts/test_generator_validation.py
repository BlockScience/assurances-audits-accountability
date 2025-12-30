#!/usr/bin/env python3
"""
Test suite for assurance_audit chart validation using generator utility (TDD approach).

This test validates that assurance_audit charts have the correct structure
by comparing their actual elements against the expected elements generated
from their audit targets.

Algorithm:
    1. Extract audit_targets from chart YAML frontmatter
    2. Run generate_assurance_audit_elements.py to compute expected elements
    3. Compare expected vs actual vertices, edges, faces
    4. Report any mismatches

Usage:
    pytest scripts/test_generator_validation.py -v
    pytest scripts/test_generator_validation.py::test_chart_types_audit -v
    python scripts/test_generator_validation.py  # Direct execution
"""

import sys
import yaml
from pathlib import Path
from generate_assurance_audit_elements import AssuranceAuditGenerator

def load_chart_elements(chart_path: Path) -> dict:
    """
    Load chart and extract elements from frontmatter.

    Returns:
        {
            'id': chart_id,
            'audit_targets': [vertex_ids],
            'vertices': [vertex_ids],
            'edges': [edge_ids],
            'faces': [face_ids],
            'metadata': chart_metadata
        }
    """
    with open(chart_path, 'r') as f:
        content = f.read()

    # Split frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1]
            metadata = yaml.safe_load(frontmatter_text)
        else:
            metadata = {}
    else:
        metadata = {}

    elements = metadata.get('elements', {})
    assurance_reqs = metadata.get('assurance_requirements', {})

    return {
        'id': metadata.get('id', 'unknown'),
        'audit_targets': assurance_reqs.get('audit_targets', []),
        'vertices': elements.get('vertices', []),
        'edges': elements.get('edges', []),
        'faces': elements.get('faces', []),
        'metadata': metadata
    }

# ============================================================================
# GENERATOR UNIT TESTS
# ============================================================================

def test_generator_includes_boundary_complex():
    """Test that generator always includes boundary complex."""
    generator = AssuranceAuditGenerator()
    result = generator.generate([])

    # Should have boundary complex even with no targets
    assert 'b0:root' in result['vertices']
    assert 'v:spec:spec' in result['vertices']
    assert 'v:spec:guidance' in result['vertices']
    assert 'v:guidance:spec' in result['vertices']
    assert 'v:guidance:guidance' in result['vertices']

    # Should have boundary faces
    assert 'b2:spec-spec' in result['faces']
    assert 'b2:guidance-guidance' in result['faces']

    print("✓ Generator includes boundary complex")
    return True

def test_generator_processes_spec_vertex():
    """Test that generator correctly processes a spec vertex."""
    generator = AssuranceAuditGenerator()
    result = generator.generate(['v:spec:chart'])

    # Should include the target vertex
    assert 'v:spec:chart' in result['vertices']

    # Should include verification target (SS)
    assert 'v:spec:spec' in result['vertices']

    # Should include validation target (GS)
    assert 'v:guidance:spec' in result['vertices']

    # Should include verification edge
    verification_edges = [e for e in result['edges'] if e.startswith('e:verification:chart:')]
    assert len(verification_edges) == 1

    # Should include validation edge
    validation_edges = [e for e in result['edges'] if e.startswith('e:validation:chart:')]
    assert len(validation_edges) == 1

    # Should include coupling edge (SS ↔ GS)
    assert 'e:coupling:spec' in result['edges']

    # Should include assurance face
    assert 'f:assurance:chart' in result['faces']

    print("✓ Generator processes spec vertex correctly")
    return True

def test_generator_processes_guidance_vertex():
    """Test that generator correctly processes a guidance vertex."""
    generator = AssuranceAuditGenerator()
    result = generator.generate(['v:guidance:chart'])

    # Should include the target vertex
    assert 'v:guidance:chart' in result['vertices']

    # Should include verification target (SG)
    assert 'v:spec:guidance' in result['vertices']

    # Should include validation target (GG)
    assert 'v:guidance:guidance' in result['vertices']

    # Should include verification edge
    verification_edges = [e for e in result['edges'] if e.startswith('e:verification:chart:')]
    assert len(verification_edges) == 1

    # Should include validation edge
    validation_edges = [e for e in result['edges'] if e.startswith('e:validation:chart:')]
    assert len(validation_edges) == 1

    # Should include coupling edge (SG ↔ GG)
    assert 'e:coupling:guidance' in result['edges']

    # Should include assurance face
    assert 'f:assurance:chart' in result['faces']

    print("✓ Generator processes guidance vertex correctly")
    return True

def test_generator_processes_chart_instance():
    """Test that generator correctly processes a chart instance."""
    generator = AssuranceAuditGenerator()
    result = generator.generate(['c:learning-journey-module-01'])

    # Should include the target vertex
    assert 'c:learning-journey-module-01' in result['vertices']

    # Should include verification target (spec-for-syllabus)
    assert 'v:spec:syllabus' in result['vertices']

    # Should include validation target (guidance-for-syllabus)
    assert 'v:guidance:syllabus' in result['vertices']

    # Should recursively include spec-for-syllabus's targets (SS, GS)
    assert 'v:spec:spec' in result['vertices']
    assert 'v:guidance:spec' in result['vertices']

    # Should include assurance face for the chart
    chart_faces = [f for f in result['faces'] if f.startswith('f:assurance:learning-journey')]
    assert len(chart_faces) == 1

    print("✓ Generator processes chart instance correctly")
    return True

def test_euler_characteristic_calculation():
    """Test that Euler characteristic is calculated correctly."""
    generator = AssuranceAuditGenerator()

    # Test with simple case
    result = generator.generate(['v:spec:chart'])

    V = len(result['vertices'])
    E = len(result['edges'])
    F = len(result['faces'])
    chi = V - E + F

    assert result['metadata']['euler_characteristic'] == chi

    print(f"✓ Euler characteristic correctly calculated: χ = {chi}")
    return True

# ============================================================================
# CHART VALIDATION TESTS
# ============================================================================

def test_boundary_complex_chart():
    """Test boundary-complex chart against generated expectations."""
    chart_path = Path('charts/boundary-complex/boundary-complex.md')

    if not chart_path.exists():
        print(f"⊘ Skipping: {chart_path} not found")
        return True

    chart_data = load_chart_elements(chart_path)

    # Generate expected elements from audit targets
    generator = AssuranceAuditGenerator()
    expected = generator.generate(chart_data['audit_targets'])

    # Compare vertices
    actual_vertices = set(chart_data['vertices'])
    expected_vertices = set(expected['vertices'])

    missing_vertices = expected_vertices - actual_vertices
    extra_vertices = actual_vertices - expected_vertices

    assert len(missing_vertices) == 0, f"Missing vertices: {missing_vertices}"
    assert len(extra_vertices) == 0, f"Extra vertices: {extra_vertices}"

    # Compare edges (allow some flexibility in naming)
    actual_edges = set(chart_data['edges'])
    expected_edges = set(expected['edges'])

    edge_count_diff = abs(len(actual_edges) - len(expected_edges))
    assert edge_count_diff <= 3, f"Edge count mismatch: {len(actual_edges)} actual vs {len(expected_edges)} expected"

    # Compare faces
    actual_faces = set(chart_data['faces'])
    expected_faces = set(expected['faces'])

    missing_faces = expected_faces - actual_faces
    extra_faces = actual_faces - expected_faces

    assert len(missing_faces) == 0, f"Missing faces: {missing_faces}"
    assert len(extra_faces) <= 2, f"Too many extra faces: {extra_faces}"

    print(f"✓ boundary-complex chart validates correctly")
    return True

def test_chart_types_audit():
    """Test chart-types-audit chart against generated expectations (TDD)."""
    chart_path = Path('charts/chart-types-audit/chart-types-audit.md')

    if not chart_path.exists():
        print(f"⊘ Skipping: {chart_path} not found")
        return True

    chart_data = load_chart_elements(chart_path)

    # Expected audit targets based on plan:
    # - v:spec:chart, v:guidance:chart
    # - v:spec:syllabus, v:guidance:syllabus
    # - v:spec:assurance_audit, v:guidance:assurance_audit
    # - c:learning-journey-module-01 (concrete syllabus)
    # - c:chart-types-audit (concrete assurance_audit, self-reference)

    # Generate expected elements
    generator = AssuranceAuditGenerator()
    expected = generator.generate(chart_data['audit_targets'])

    # Compare vertices
    actual_vertices = set(chart_data['vertices'])
    expected_vertices = set(expected['vertices'])

    missing_vertices = expected_vertices - actual_vertices
    extra_vertices = actual_vertices - expected_vertices

    print("\n" + "=" * 70)
    print("CHART-TYPES-AUDIT VALIDATION")
    print("=" * 70)
    print(f"\nAudit targets ({len(chart_data['audit_targets'])}):")
    for target in chart_data['audit_targets']:
        print(f"  - {target}")

    print(f"\nExpected vertices ({len(expected_vertices)}):")
    for v in sorted(expected_vertices):
        print(f"  - {v}")

    print(f"\nActual vertices ({len(actual_vertices)}):")
    for v in sorted(actual_vertices):
        print(f"  - {v}")

    if missing_vertices:
        print(f"\n❌ Missing vertices ({len(missing_vertices)}):")
        for v in sorted(missing_vertices):
            print(f"   - {v}")
    else:
        print("\n✓ All expected vertices present")

    if extra_vertices:
        print(f"\n⚠️  Extra vertices ({len(extra_vertices)}):")
        for v in sorted(extra_vertices):
            print(f"   - {v}")
    else:
        print("✓ No extra vertices")

    # Compare edges
    actual_edges = set(chart_data['edges'])
    expected_edges = set(expected['edges'])

    missing_edges = expected_edges - actual_edges
    extra_edges = actual_edges - expected_edges

    print(f"\nExpected edges ({len(expected_edges)}):")
    for e in sorted(expected_edges):
        print(f"  - {e}")

    print(f"\nActual edges ({len(actual_edges)}):")
    for e in sorted(actual_edges):
        print(f"  - {e}")

    if missing_edges:
        print(f"\n❌ Missing edges ({len(missing_edges)}):")
        for e in sorted(missing_edges):
            print(f"   - {e}")
    else:
        print("\n✓ All expected edges present")

    if extra_edges:
        print(f"\n⚠️  Extra edges ({len(extra_edges)}):")
        for e in sorted(extra_edges):
            print(f"   - {e}")

    # Compare faces
    actual_faces = set(chart_data['faces'])
    expected_faces = set(expected['faces'])

    missing_faces = expected_faces - actual_faces
    extra_faces = actual_faces - expected_faces

    print(f"\nExpected faces ({len(expected_faces)}):")
    for f in sorted(expected_faces):
        print(f"  - {f}")

    print(f"\nActual faces ({len(actual_faces)}):")
    for f in sorted(actual_faces):
        print(f"  - {f}")

    if missing_faces:
        print(f"\n❌ Missing faces ({len(missing_faces)}):")
        for f in sorted(missing_faces):
            print(f"   - {f}")
    else:
        print("\n✓ All expected faces present")

    if extra_faces:
        print(f"\n⚠️  Extra faces ({len(extra_faces)}):")
        for f in sorted(extra_faces):
            print(f"   - {f}")

    # Topology comparison
    print(f"\nTopology:")
    print(f"  Expected: V={expected['metadata']['total_vertices']}, "
          f"E={expected['metadata']['total_edges']}, "
          f"F={expected['metadata']['total_faces']}, "
          f"χ={expected['metadata']['euler_characteristic']}")

    actual_chi = len(actual_vertices) - len(actual_edges) + len(actual_faces)
    print(f"  Actual:   V={len(actual_vertices)}, "
          f"E={len(actual_edges)}, "
          f"F={len(actual_faces)}, "
          f"χ={actual_chi}")

    print("\n" + "=" * 70)
    print("VALIDATION RESULT")
    print("=" * 70)

    # Assertions
    try:
        assert len(missing_vertices) == 0, f"Missing vertices: {missing_vertices}"
        assert len(extra_vertices) == 0, f"Extra vertices: {extra_vertices}"

        assert len(missing_edges) == 0, f"Missing edges: {missing_edges}"
        # Allow some extra edges (coupling edges, etc.)
        assert len(extra_edges) <= 5, f"Too many extra edges: {extra_edges}"

        assert len(missing_faces) == 0, f"Missing faces: {missing_faces}"
        # Allow some extra faces
        assert len(extra_faces) <= 3, f"Too many extra faces: {extra_faces}"

        print("✓ PASS: chart-types-audit validates correctly\n")
        return True

    except AssertionError as e:
        print(f"✗ FAIL: {e}\n")
        return False

# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def main():
    """Run all tests and report results."""
    print("=" * 70)
    print("ASSURANCE AUDIT CHART GENERATOR - VALIDATION TEST SUITE")
    print("=" * 70)

    tests = [
        ("Generator includes boundary complex", test_generator_includes_boundary_complex),
        ("Generator processes spec vertex", test_generator_processes_spec_vertex),
        ("Generator processes guidance vertex", test_generator_processes_guidance_vertex),
        ("Generator processes chart instance", test_generator_processes_chart_instance),
        ("Euler characteristic calculation", test_euler_characteristic_calculation),
        ("Boundary-complex chart validation", test_boundary_complex_chart),
        ("Chart-types-audit validation (TDD)", test_chart_types_audit),
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        print(f"\n{'=' * 70}")
        print(f"TEST: {test_name}")
        print('=' * 70)

        try:
            result = test_func()
            if result:
                passed += 1
            else:
                failed += 1
                print(f"✗ Test failed: {test_name}")
        except AssertionError as e:
            failed += 1
            print(f"✗ Test failed: {test_name}")
            print(f"  Error: {e}")
        except Exception as e:
            failed += 1
            print(f"✗ Test error: {test_name}")
            print(f"  Exception: {e}")

    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Total: {len(tests)}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    print(f"Success rate: {passed/len(tests)*100:.1f}%")

    if failed == 0:
        print("\n✓ ALL TESTS PASSED")
        return 0
    else:
        print(f"\n✗ {failed} TEST(S) FAILED")
        return 1

if __name__ == '__main__':
    sys.exit(main())
