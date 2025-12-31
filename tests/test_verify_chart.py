#!/usr/bin/env python3
"""
Tests for verify_chart.py
"""

from pathlib import Path
import sys
import tempfile
import os

sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from verify_chart import get_edge_boundary, verify_chart_elements, find_cache_root, VerificationError


class TestVerifyChart:
    """Test chart verification functions."""

    def test_get_edge_boundary(self):
        """Test extracting edge boundary vertices."""
        edge = {'source': 'v:a', 'target': 'v:b'}
        boundary = get_edge_boundary(edge)
        assert boundary == {'v:a', 'v:b'}

    def test_verify_chart_valid(self):
        """Test verifying a valid chart."""
        chart = {
            'id': 'c:test',
            'elements': {
                'vertices': ['v:a', 'v:b'],
                'edges': ['e:a:b'],
                'faces': []
            }
        }

        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a'},
                    'v:b': {'id': 'v:b'}
                },
                'edges': {
                    'e:a:b': {
                        'id': 'e:a:b',
                        'source': 'v:a',
                        'target': 'v:b'
                    }
                },
                'faces': {}
            }
        }

        errors = verify_chart_elements(chart, cache)
        assert len(errors) == 0

    def test_verify_chart_missing_vertex(self):
        """Test that missing vertices are detected."""
        chart = {
            'id': 'c:test',
            'elements': {
                'vertices': ['v:a', 'v:missing'],
                'edges': [],
                'faces': []
            }
        }

        cache = {
            'elements': {
                'vertices': {'v:a': {'id': 'v:a'}},
                'edges': {},
                'faces': {}
            }
        }

        errors = verify_chart_elements(chart, cache)
        assert len(errors) > 0
        assert any('v:missing' in err and 'not found' in err for err in errors)

    def test_verify_chart_edge_boundary_missing(self):
        """Test that edges with boundaries outside the chart are detected."""
        chart = {
            'id': 'c:test',
            'elements': {
                'vertices': ['v:a'],
                'edges': ['e:a:b'],
                'faces': []
            }
        }

        cache = {
            'elements': {
                'vertices': {'v:a': {'id': 'v:a'}},
                'edges': {
                    'e:a:b': {
                        'id': 'e:a:b',
                        'source': 'v:a',
                        'target': 'v:b'  # v:b not in chart!
                    }
                },
                'faces': {}
            }
        }

        errors = verify_chart_elements(chart, cache)
        assert len(errors) > 0
        assert any('boundary vertices not in chart' in err for err in errors)


class TestFindCacheRoot:
    """Test cache root path resolution."""

    def test_find_cache_in_current_dir(self):
        """Test finding complex.json in current directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir).resolve()  # Resolve symlinks for comparison
            # Create complex.json in root
            (tmppath / 'complex.json').write_text('{}')
            # Search from root
            result = find_cache_root(tmppath)
            assert result == tmppath

    def test_find_cache_in_parent_dir(self):
        """Test finding complex.json in parent directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir).resolve()  # Resolve symlinks for comparison
            # Create complex.json in root
            (tmppath / 'complex.json').write_text('{}')
            # Create nested directory
            nested = tmppath / 'charts' / 'my-chart'
            nested.mkdir(parents=True)
            # Search from nested dir - should find in grandparent
            result = find_cache_root(nested)
            assert result == tmppath

    def test_find_cache_not_found(self):
        """Test error when complex.json not found."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir).resolve()
            # No complex.json anywhere
            try:
                find_cache_root(tmppath)
                assert False, "Should have raised VerificationError"
            except VerificationError as e:
                assert 'complex.json not found' in str(e)

    def test_find_cache_prefers_nearest(self):
        """Test that nearest complex.json is found first."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir).resolve()  # Resolve symlinks for comparison
            # Create complex.json in root
            (tmppath / 'complex.json').write_text('{"location": "root"}')
            # Create nested dir with its own complex.json
            nested = tmppath / 'subdir'
            nested.mkdir()
            (nested / 'complex.json').write_text('{"location": "subdir"}')
            # Search from nested - should find the nested one
            result = find_cache_root(nested)
            assert result == nested


def run_tests():
    """Run all verify_chart tests."""
    print("=" * 70)
    print("Chart Verification Tests")
    print("=" * 70)

    verify_tests = TestVerifyChart()

    try:
        verify_tests.test_get_edge_boundary()
        print("✓ test_get_edge_boundary")
    except AssertionError as e:
        print(f"✗ test_get_edge_boundary: {e}")
        return False

    try:
        verify_tests.test_verify_chart_valid()
        print("✓ test_verify_chart_valid")
    except AssertionError as e:
        print(f"✗ test_verify_chart_valid: {e}")
        return False

    try:
        verify_tests.test_verify_chart_missing_vertex()
        print("✓ test_verify_chart_missing_vertex")
    except AssertionError as e:
        print(f"✗ test_verify_chart_missing_vertex: {e}")
        return False

    try:
        verify_tests.test_verify_chart_edge_boundary_missing()
        print("✓ test_verify_chart_edge_boundary_missing")
    except AssertionError as e:
        print(f"✗ test_verify_chart_edge_boundary_missing: {e}")
        return False

    print("\n" + "=" * 70)
    print("All chart verification tests passed!")
    print("=" * 70)
    return True


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
