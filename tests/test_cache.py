#!/usr/bin/env python3
"""
Tests for build_cache.py
"""

import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from build_cache import build_cache, calculate_euler_characteristic


class TestEulerCharacteristic:
    """Test Euler characteristic calculation."""

    def test_empty_complex(self):
        """Test empty complex has χ = 0."""
        assert calculate_euler_characteristic([], [], []) == 0

    def test_single_vertex(self):
        """Test single vertex has χ = 1."""
        assert calculate_euler_characteristic(['v1'], [], []) == 1

    def test_edge(self):
        """Test edge (2 vertices, 1 edge) has χ = 1."""
        assert calculate_euler_characteristic(['v1', 'v2'], ['e1'], []) == 1

    def test_triangle(self):
        """Test triangle (3 vertices, 3 edges, 1 face) has χ = 1."""
        assert calculate_euler_characteristic(
            ['v1', 'v2', 'v3'],
            ['e1', 'e2', 'e3'],
            ['f1']
        ) == 1

    def test_tetrahedron_with_hole(self):
        """Test tetrahedron with hole (4 vertices, 6 edges, 3 faces) has χ = 1."""
        assert calculate_euler_characteristic(
            ['v1', 'v2', 'v3', 'v4'],
            ['e1', 'e2', 'e3', 'e4', 'e5', 'e6'],
            ['f1', 'f2', 'f3']
        ) == 1


class TestBuildCache:
    """Test cache building."""

    def test_build_cache_simple(self, tmp_path):
        """Test building a cache from simple structure."""
        # Create simple structure
        vertices_dir = tmp_path / "00_vertices"
        vertices_dir.mkdir()

        (vertices_dir / "test.md").write_text("""---
type: vertex/vertex
extends: null
id: v:test
name: Test Vertex
tags:
  - vertex
version: 1.0.0
---
""")

        # Build cache
        cache = build_cache(tmp_path, tmp_path / "complex.json")

        assert cache['version'] == '1.0.0'
        assert 'v:test' in cache['elements']['vertices']
        assert cache['statistics']['vertex_count'] == 1
        assert cache['statistics']['edge_count'] == 0

        # Verify cache file was written
        cache_file = tmp_path / "complex.json"
        assert cache_file.exists()

        # Verify it can be loaded
        loaded = json.loads(cache_file.read_text())
        assert loaded['statistics']['vertex_count'] == 1


def run_tests():
    """Run all cache tests."""
    print("=" * 70)
    print("Cache Building Tests")
    print("=" * 70)

    # TestEulerCharacteristic
    print("\n--- Euler Characteristic Tests ---")
    euler_tests = TestEulerCharacteristic()

    try:
        euler_tests.test_empty_complex()
        print("✓ test_empty_complex")
    except AssertionError as e:
        print(f"✗ test_empty_complex: {e}")
        return False

    try:
        euler_tests.test_single_vertex()
        print("✓ test_single_vertex")
    except AssertionError as e:
        print(f"✗ test_single_vertex: {e}")
        return False

    try:
        euler_tests.test_edge()
        print("✓ test_edge")
    except AssertionError as e:
        print(f"✗ test_edge: {e}")
        return False

    try:
        euler_tests.test_triangle()
        print("✓ test_triangle")
    except AssertionError as e:
        print(f"✗ test_triangle: {e}")
        return False

    try:
        euler_tests.test_tetrahedron_with_hole()
        print("✓ test_tetrahedron_with_hole")
    except AssertionError as e:
        print(f"✗ test_tetrahedron_with_hole: {e}")
        return False

    # TestBuildCache
    print("\n--- Build Cache Tests ---")
    build_tests = TestBuildCache()

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        try:
            build_tests.test_build_cache_simple(tmp_path)
            print("✓ test_build_cache_simple")
        except AssertionError as e:
            print(f"✗ test_build_cache_simple: {e}")
            return False

    print("\n" + "=" * 70)
    print("All cache tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
