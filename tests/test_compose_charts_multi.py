#!/usr/bin/env python3
"""
Tests for multi-chart composition script.
"""

import json
import pytest
from pathlib import Path
import sys

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from compose_charts_multi import compose_charts_multi, compose_two_charts


@pytest.fixture
def chart_dir():
    """Get charts directory."""
    return Path(__file__).parent.parent / "charts"


@pytest.fixture
def module_charts(chart_dir):
    """Get paths to all module learning journey charts."""
    charts = []
    for i in range(1, 8):
        chart_path = chart_dir / f"learning-journey-module-0{i}" / f"learning-journey-module-0{i}.json"
        if chart_path.exists():
            charts.append(chart_path)
    return charts


def test_compose_two_modules(chart_dir, tmp_path):
    """Test composing just two modules."""
    chart1 = chart_dir / "learning-journey-module-01" / "learning-journey-module-01.json"
    chart2 = chart_dir / "learning-journey-module-02" / "learning-journey-module-02.json"
    output = tmp_path / "composed-01-02.json"

    if not chart1.exists() or not chart2.exists():
        pytest.skip("Module charts not found")

    result = compose_charts_multi([chart1, chart2], output, verbose=False)

    # Verify output file exists
    assert output.exists()

    # Verify structure
    assert "elements" in result
    assert "topology" in result
    assert result["topology"]["chi"] == 1  # Should remain topologically complete

    # Verify it has more elements than either individual chart
    with open(chart1) as f:
        c1 = json.load(f)
    assert result["topology"]["V"] > c1["topology"]["V"]


def test_compose_three_modules(chart_dir, tmp_path):
    """Test composing three modules."""
    charts = [
        chart_dir / "learning-journey-module-01" / "learning-journey-module-01.json",
        chart_dir / "learning-journey-module-02" / "learning-journey-module-02.json",
        chart_dir / "learning-journey-module-03" / "learning-journey-module-03.json",
    ]

    # Skip if any chart missing
    if not all(c.exists() for c in charts):
        pytest.skip("Module charts not found")

    output = tmp_path / "composed-01-03.json"
    result = compose_charts_multi(charts, output, verbose=False)

    # Verify structure
    assert result["composition"]["total_steps"] == 2
    assert result["composition"]["final"] is True
    assert result["topology"]["chi"] == 1


def test_compose_fork_merge_pattern(chart_dir, tmp_path):
    """Test composing modules 05, 06, 07 (fork-merge pattern)."""
    charts = [
        chart_dir / "learning-journey-module-05" / "learning-journey-module-05.json",
        chart_dir / "learning-journey-module-06" / "learning-journey-module-06.json",
        chart_dir / "learning-journey-module-07" / "learning-journey-module-07.json",
    ]

    if not all(c.exists() for c in charts):
        pytest.skip("Module charts not found")

    output = tmp_path / "composed-05-07.json"
    result = compose_charts_multi(charts, output, verbose=False)

    # Should have shared convergence point (document-architect)
    assert "v:student:document-architect" in [v["id"] for v in result["elements"]["vertices"]]

    # Should have shared fork point (assurance-learner)
    assert "v:student:assurance-learner" in [v["id"] for v in result["elements"]["vertices"]]

    # Topology should still be complete
    assert result["topology"]["chi"] == 1


def test_compose_all_seven_modules(module_charts, tmp_path):
    """Test composing all seven modules."""
    if len(module_charts) < 7:
        pytest.skip(f"Only found {len(module_charts)} module charts, need 7")

    output = tmp_path / "learning-journey-full.json"
    result = compose_charts_multi(
        module_charts,
        output,
        name="Learning Journey - Modules 01-07 (Complete)",
        description="Full learning journey test",
        verbose=False
    )

    # Verify final metadata
    assert result["name"] == "Learning Journey - Modules 01-07 (Complete)"
    assert result["composition"]["final"] is True
    assert result["composition"]["total_steps"] == 6  # 7 charts = 6 composition steps

    # Verify topology
    assert "topology" in result
    assert result["topology"]["V"] > 0
    assert result["topology"]["E"] > 0
    assert result["topology"]["F"] > 0

    # Verify key student states exist
    vertex_ids = [v["id"] for v in result["elements"]["vertices"]]
    assert "v:student:foundational-learner" in vertex_ids
    assert "v:student:document-architect" in vertex_ids

    # Verify all 7 learning modules exist
    module_count = sum(1 for v in result["elements"]["vertices"]
                      if v["id"].startswith("v:learning-module:"))
    assert module_count == 7

    print(f"\nFinal composition statistics:")
    print(f"  Total vertices: {result['topology']['V']}")
    print(f"  Total edges: {result['topology']['E']}")
    print(f"  Total faces: {result['topology']['F']}")
    print(f"  Euler characteristic: χ = {result['topology']['chi']}")


def test_composition_preserves_elements(chart_dir, tmp_path):
    """Test that composition doesn't lose elements."""
    chart1 = chart_dir / "learning-journey-module-01" / "learning-journey-module-01.json"
    chart2 = chart_dir / "learning-journey-module-02" / "learning-journey-module-02.json"

    if not chart1.exists() or not chart2.exists():
        pytest.skip("Module charts not found")

    output = tmp_path / "test-preservation.json"
    result = compose_charts_multi([chart1, chart2], output, verbose=False)

    # Load original charts
    with open(chart1) as f:
        c1 = json.load(f)
    with open(chart2) as f:
        c2 = json.load(f)

    # All elements from chart1 should be in result
    c1_vertices = {v["id"] if isinstance(v, dict) else v for v in c1["elements"]["vertices"]}
    result_vertices = {v["id"] for v in result["elements"]["vertices"]}
    assert c1_vertices.issubset(result_vertices)

    # All elements from chart2 should be in result
    c2_vertices = {v["id"] if isinstance(v, dict) else v for v in c2["elements"]["vertices"]}
    assert c2_vertices.issubset(result_vertices)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
