#!/usr/bin/env python3
"""
Tests for chart composition script.

Tests verify:
1. Correct identification of shared elements
2. Proper set union with deduplication
3. Topology calculation (V, E, F, χ)
4. Type consistency validation
5. Preservation of element data for visualization
"""

import pytest
import json
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from compose_charts import (
    load_chart,
    get_element_ids,
    find_shared_elements,
    union_elements,
    compose_charts
)


# Test fixtures
@pytest.fixture
def simple_chart_a():
    """Simple chart with 3 vertices, 2 edges, 0 faces."""
    return {
        "name": "Chart A",
        "elements": {
            "vertices": [
                {"id": "v:a", "type": "vertex/test"},
                {"id": "v:b", "type": "vertex/test"},
                {"id": "v:c", "type": "vertex/test"}
            ],
            "edges": [
                {"id": "e:a:b", "source": "v:a", "target": "v:b"},
                {"id": "e:b:c", "source": "v:b", "target": "v:c"}
            ],
            "faces": []
        }
    }


@pytest.fixture
def simple_chart_b():
    """Simple chart sharing vertex c with chart A."""
    return {
        "name": "Chart B",
        "elements": {
            "vertices": [
                {"id": "v:c", "type": "vertex/test"},
                {"id": "v:d", "type": "vertex/test"}
            ],
            "edges": [
                {"id": "e:c:d", "source": "v:c", "target": "v:d"}
            ],
            "faces": []
        }
    }


@pytest.fixture
def module1_chart(tmp_path):
    """Load actual Module 1 chart."""
    module1_path = Path("charts/learning-journey-module-01/learning-journey-module-01.json")
    if module1_path.exists():
        return load_chart(module1_path)
    pytest.skip("Module 1 chart not found")


@pytest.fixture
def module2_chart(tmp_path):
    """Load actual Module 2 chart."""
    module2_path = Path("charts/learning-journey-module-02/learning-journey-module-02.json")
    if module2_path.exists():
        return load_chart(module2_path)
    pytest.skip("Module 2 chart not found")


# Unit tests
class TestGetElementIds:
    """Test element ID extraction."""

    def test_extract_vertex_ids_from_objects(self, simple_chart_a):
        """Should extract vertex IDs from object format."""
        ids = get_element_ids(simple_chart_a, 'vertices')
        assert ids == {'v:a', 'v:b', 'v:c'}

    def test_extract_edge_ids_from_objects(self, simple_chart_a):
        """Should extract edge IDs from object format."""
        ids = get_element_ids(simple_chart_a, 'edges')
        assert ids == {'e:a:b', 'e:b:c'}

    def test_extract_from_string_list(self):
        """Should handle string list format (IDs only)."""
        chart = {
            "elements": {
                "vertices": ["v:a", "v:b", "v:c"]
            }
        }
        ids = get_element_ids(chart, 'vertices')
        assert ids == {'v:a', 'v:b', 'v:c'}

    def test_empty_elements(self):
        """Should handle missing element types."""
        chart = {"elements": {}}
        ids = get_element_ids(chart, 'vertices')
        assert ids == set()


class TestFindSharedElements:
    """Test shared element identification."""

    def test_identify_shared_vertex(self, simple_chart_a, simple_chart_b):
        """Should identify vertex c as shared."""
        shared = find_shared_elements(simple_chart_a, simple_chart_b)
        assert shared['vertices'] == {'v:c'}
        assert shared['edges'] == set()
        assert shared['faces'] == set()

    def test_no_shared_elements(self):
        """Should handle disjoint charts."""
        chart_a = {
            "elements": {
                "vertices": ["v:a", "v:b"],
                "edges": [],
                "faces": []
            }
        }
        chart_b = {
            "elements": {
                "vertices": ["v:c", "v:d"],
                "edges": [],
                "faces": []
            }
        }
        shared = find_shared_elements(chart_a, chart_b)
        assert shared['vertices'] == set()
        assert shared['edges'] == set()
        assert shared['faces'] == set()

    def test_module1_module2_shared(self, module1_chart, module2_chart):
        """Should identify correct shared elements between Module 1 and 2."""
        shared = find_shared_elements(module1_chart, module2_chart)

        # Expected shared elements
        assert 'v:student:foundational-learner' in shared['vertices']
        assert 'v:skill:simplicial-complex-fundamentals' in shared['vertices']
        assert len(shared['vertices']) == 2

        assert 'e:has-skill:foundational-learner:simplicial-complex-fundamentals' in shared['edges']
        assert len(shared['edges']) == 1

        assert len(shared['faces']) == 0


class TestUnionElements:
    """Test set union operations."""

    def test_union_with_shared_vertex(self, simple_chart_a, simple_chart_b):
        """Should union vertices counting shared once."""
        union = union_elements(simple_chart_a, simple_chart_b, 'vertices')
        # Chart A: {a, b, c}, Chart B: {c, d} -> Union: {a, b, c, d}
        assert set(union) == {'v:a', 'v:b', 'v:c', 'v:d'}
        assert len(union) == 4  # c counted once

    def test_union_disjoint_sets(self):
        """Should union disjoint sets correctly."""
        chart_a = {"elements": {"vertices": ["v:a", "v:b"]}}
        chart_b = {"elements": {"vertices": ["v:c", "v:d"]}}
        union = union_elements(chart_a, chart_b, 'vertices')
        assert set(union) == {'v:a', 'v:b', 'v:c', 'v:d'}
        assert len(union) == 4

    def test_union_identical_sets(self):
        """Should handle identical element sets."""
        chart_a = {"elements": {"vertices": ["v:a", "v:b"]}}
        chart_b = {"elements": {"vertices": ["v:a", "v:b"]}}
        union = union_elements(chart_a, chart_b, 'vertices')
        assert set(union) == {'v:a', 'v:b'}
        assert len(union) == 2  # All elements shared, counted once

    def test_module1_module2_union(self, module1_chart, module2_chart):
        """Should compute correct union for Module 1 and 2."""
        v_union = union_elements(module1_chart, module2_chart, 'vertices')
        e_union = union_elements(module1_chart, module2_chart, 'edges')
        f_union = union_elements(module1_chart, module2_chart, 'faces')

        # Module 1: V=5, Module 2: V=5, Shared=2 -> Union=8
        assert len(v_union) == 8

        # Module 1: E=7, Module 2: E=7, Shared=1 -> Union=13
        assert len(e_union) == 13

        # Module 1: F=3, Module 2: F=3, Shared=0 -> Union=6
        assert len(f_union) == 6


class TestTopologyCalculation:
    """Test Euler characteristic calculation."""

    def test_simple_composition_topology(self, simple_chart_a, simple_chart_b):
        """Should calculate χ correctly for simple composition."""
        v_union = union_elements(simple_chart_a, simple_chart_b, 'vertices')
        e_union = union_elements(simple_chart_a, simple_chart_b, 'edges')
        f_union = union_elements(simple_chart_a, simple_chart_b, 'faces')

        V = len(v_union)  # 4 vertices
        E = len(e_union)  # 3 edges
        F = len(f_union)  # 0 faces
        chi = V - E + F

        assert V == 4
        assert E == 3
        assert F == 0
        assert chi == 1

    def test_module_composition_topology(self, module1_chart, module2_chart):
        """Should calculate correct topology for Module 1+2 composition."""
        v_union = union_elements(module1_chart, module2_chart, 'vertices')
        e_union = union_elements(module1_chart, module2_chart, 'edges')
        f_union = union_elements(module1_chart, module2_chart, 'faces')

        V = len(v_union)
        E = len(e_union)
        F = len(f_union)
        chi = V - E + F

        assert V == 8
        assert E == 13
        assert F == 6
        assert chi == 1


class TestComposeCharts:
    """Integration tests for full composition."""

    def test_compose_simple_charts(self, simple_chart_a, simple_chart_b, tmp_path):
        """Should compose two simple charts correctly."""
        # Write charts to temp files
        chart_a_path = tmp_path / "chart_a.json"
        chart_b_path = tmp_path / "chart_b.json"
        output_path = tmp_path / "composed.json"

        with open(chart_a_path, 'w') as f:
            json.dump(simple_chart_a, f)
        with open(chart_b_path, 'w') as f:
            json.dump(simple_chart_b, f)

        # Compose
        result = compose_charts(
            chart_a_path,
            chart_b_path,
            Path("complex.json"),
            output_path
        )

        # Verify result
        assert result['topology']['V'] == 4
        assert result['topology']['E'] == 3
        assert result['topology']['F'] == 0
        assert result['topology']['chi'] == 1

        assert set(result['composition']['shared_vertices']) == {'v:c'}
        assert result['composition']['shared_edges'] == []
        assert result['composition']['shared_faces'] == []

    def test_compose_modules(self, tmp_path):
        """Should compose Module 1 and Module 2 correctly."""
        module1_path = Path("charts/learning-journey-module-01/learning-journey-module-01.json")
        module2_path = Path("charts/learning-journey-module-02/learning-journey-module-02.json")

        if not (module1_path.exists() and module2_path.exists()):
            pytest.skip("Module charts not found")

        output_path = tmp_path / "composed-modules.json"

        result = compose_charts(
            module1_path,
            module2_path,
            Path("complex.json"),
            output_path
        )

        # Verify topology
        assert result['topology']['V'] == 8
        assert result['topology']['E'] == 13
        assert result['topology']['F'] == 6
        assert result['topology']['chi'] == 1

        # Verify shared elements
        assert len(result['composition']['shared_vertices']) == 2
        assert 'v:student:foundational-learner' in result['composition']['shared_vertices']
        assert 'v:skill:simplicial-complex-fundamentals' in result['composition']['shared_vertices']

        assert len(result['composition']['shared_edges']) == 1
        assert 'e:has-skill:foundational-learner:simplicial-complex-fundamentals' in result['composition']['shared_edges']

        assert len(result['composition']['shared_faces']) == 0

        # Verify output file was created
        assert output_path.exists()

        # Verify JSON is valid
        with open(output_path) as f:
            loaded = json.load(f)
            assert loaded['topology']['chi'] == 1


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_chart_composition(self):
        """Should handle empty charts."""
        empty_chart = {"elements": {"vertices": [], "edges": [], "faces": []}}
        shared = find_shared_elements(empty_chart, empty_chart)
        assert shared['vertices'] == set()
        assert shared['edges'] == set()
        assert shared['faces'] == set()

    def test_self_composition(self, simple_chart_a):
        """Should handle composing chart with itself (all elements shared)."""
        shared = find_shared_elements(simple_chart_a, simple_chart_a)
        # All elements are shared
        assert len(shared['vertices']) == 3
        assert len(shared['edges']) == 2

    def test_union_preserves_order(self):
        """Should return sorted union results."""
        chart_a = {"elements": {"vertices": ["v:c", "v:a", "v:b"]}}
        chart_b = {"elements": {"vertices": ["v:d", "v:a"]}}
        union = union_elements(chart_a, chart_b, 'vertices')
        # Should be sorted
        assert union == ['v:a', 'v:b', 'v:c', 'v:d']


# Property-based tests
class TestCompositionProperties:
    """Test mathematical properties of composition."""

    def test_composition_associative(self, tmp_path):
        """Test: (A ∪ B) ∪ C = A ∪ (B ∪ C)."""
        # Create three simple charts
        chart_a = {"elements": {"vertices": ["v:a", "v:b"], "edges": [], "faces": []}}
        chart_b = {"elements": {"vertices": ["v:b", "v:c"], "edges": [], "faces": []}}
        chart_c = {"elements": {"vertices": ["v:c", "v:d"], "edges": [], "faces": []}}

        # Compose (A ∪ B) first
        ab_union = union_elements(chart_a, chart_b, 'vertices')
        chart_ab = {"elements": {"vertices": ab_union, "edges": [], "faces": []}}
        abc_left = union_elements(chart_ab, chart_c, 'vertices')

        # Compose (B ∪ C) first
        bc_union = union_elements(chart_b, chart_c, 'vertices')
        chart_bc = {"elements": {"vertices": bc_union, "edges": [], "faces": []}}
        abc_right = union_elements(chart_a, chart_bc, 'vertices')

        # Should be equal
        assert set(abc_left) == set(abc_right)

    def test_composition_commutative(self, simple_chart_a, simple_chart_b):
        """Test: A ∪ B = B ∪ A."""
        ab = union_elements(simple_chart_a, simple_chart_b, 'vertices')
        ba = union_elements(simple_chart_b, simple_chart_a, 'vertices')
        assert set(ab) == set(ba)

    def test_shared_count_formula(self, module1_chart, module2_chart):
        """Test: |A ∪ B| = |A| + |B| - |A ∩ B|."""
        # Get sizes
        v1 = get_element_ids(module1_chart, 'vertices')
        v2 = get_element_ids(module2_chart, 'vertices')
        shared = find_shared_elements(module1_chart, module2_chart)
        union = union_elements(module1_chart, module2_chart, 'vertices')

        # Verify formula
        assert len(union) == len(v1) + len(v2) - len(shared['vertices'])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
