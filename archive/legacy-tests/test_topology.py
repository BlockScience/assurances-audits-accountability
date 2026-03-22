#!/usr/bin/env python3
"""
Tests for topology.py
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from topology import find_potential_faces, get_edge_boundary


class TestTopology:
    """Test topology functions."""

    def test_get_edge_boundary(self):
        """Test extracting edge boundaries."""
        edge = {
            'source': 'v:b',
            'target': 'v:a'
        }
        boundary = get_edge_boundary(edge)
        # Should be sorted
        assert boundary == ('v:a', 'v:b')

    def test_find_potential_faces_triangle(self):
        """Test finding potential faces in a complete triangle."""
        vertices = ['v:a', 'v:b', 'v:c']
        edges = {
            'e:a:b': {'source': 'v:a', 'target': 'v:b'},
            'e:b:c': {'source': 'v:b', 'target': 'v:c'},
            'e:a:c': {'source': 'v:a', 'target': 'v:c'},
        }

        potential = find_potential_faces(vertices, edges)

        # Should find exactly 1 potential face
        assert len(potential) == 1
        assert tuple(sorted(['v:a', 'v:b', 'v:c'])) in potential

    def test_find_potential_faces_tetrahedron(self):
        """Test finding potential faces in a complete tetrahedron."""
        vertices = ['v:a', 'v:b', 'v:c', 'v:d']
        edges = {
            'e:a:b': {'source': 'v:a', 'target': 'v:b'},
            'e:a:c': {'source': 'v:a', 'target': 'v:c'},
            'e:a:d': {'source': 'v:a', 'target': 'v:d'},
            'e:b:c': {'source': 'v:b', 'target': 'v:c'},
            'e:b:d': {'source': 'v:b', 'target': 'v:d'},
            'e:c:d': {'source': 'v:c', 'target': 'v:d'},
        }

        potential = find_potential_faces(vertices, edges)

        # Should find exactly 4 potential faces (all sides of tetrahedron)
        assert len(potential) == 4

        expected_faces = [
            tuple(sorted(['v:a', 'v:b', 'v:c'])),
            tuple(sorted(['v:a', 'v:b', 'v:d'])),
            tuple(sorted(['v:a', 'v:c', 'v:d'])),
            tuple(sorted(['v:b', 'v:c', 'v:d'])),
        ]

        for expected in expected_faces:
            assert expected in potential

    def test_find_potential_faces_incomplete(self):
        """Test that incomplete triangles are not found."""
        vertices = ['v:a', 'v:b', 'v:c']
        edges = {
            'e:a:b': {'source': 'v:a', 'target': 'v:b'},
            'e:b:c': {'source': 'v:b', 'target': 'v:c'},
            # Missing e:a:c
        }

        potential = find_potential_faces(vertices, edges)

        # Should find no potential faces (triangle incomplete)
        assert len(potential) == 0


def run_tests():
    """Run all topology tests."""
    print("=" * 70)
    print("Topology Tests")
    print("=" * 70)

    topology_tests = TestTopology()

    try:
        topology_tests.test_get_edge_boundary()
        print("✓ test_get_edge_boundary")
    except AssertionError as e:
        print(f"✗ test_get_edge_boundary: {e}")
        return False

    try:
        topology_tests.test_find_potential_faces_triangle()
        print("✓ test_find_potential_faces_triangle")
    except AssertionError as e:
        print(f"✗ test_find_potential_faces_triangle: {e}")
        return False

    try:
        topology_tests.test_find_potential_faces_tetrahedron()
        print("✓ test_find_potential_faces_tetrahedron")
    except AssertionError as e:
        print(f"✗ test_find_potential_faces_tetrahedron: {e}")
        return False

    try:
        topology_tests.test_find_potential_faces_incomplete()
        print("✓ test_find_potential_faces_incomplete")
    except AssertionError as e:
        print(f"✗ test_find_potential_faces_incomplete: {e}")
        return False

    print("\n" + "=" * 70)
    print("All topology tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
