#!/usr/bin/env python3
"""
Compose multiple simplicial complex charts through iterative pairwise composition.

This script takes N charts and performs (N-1) pairwise compositions:
- Iteration 1: compose(chart1, chart2) -> composed1
- Iteration 2: compose(composed1, chart3) -> composed2
- ...
- Iteration N-1: compose(composedN-2, chartN) -> final

The result is a single composed chart representing the union of all input charts.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Any
from compose_charts import (
    load_chart,
    get_element_ids,
    find_shared_elements,
    union_elements_full,
)


def compose_two_charts(chart1: Dict[str, Any], chart2: Dict[str, Any],
                       step: int, total: int, verbose: bool = True) -> Dict[str, Any]:
    """Compose two charts through identification."""

    if verbose:
        print(f"\n{'='*60}")
        print(f"Composition Step {step}/{total}")
        print(f"{'='*60}")
        print(f"Chart 1: {chart1['name']}")
        print(f"  V={len(chart1['elements']['vertices'])}, "
              f"E={len(chart1['elements']['edges'])}, "
              f"F={len(chart1['elements'].get('faces', []))}")

        print(f"Chart 2: {chart2['name']}")
        print(f"  V={len(chart2['elements']['vertices'])}, "
              f"E={len(chart2['elements']['edges'])}, "
              f"F={len(chart2['elements'].get('faces', []))}")

    # Find shared elements
    shared = find_shared_elements(chart1, chart2)

    if verbose:
        print(f"\nShared elements:")
        print(f"  Vertices: {len(shared['vertices'])}")
        if shared['vertices']:
            for vid in sorted(list(shared['vertices']))[:5]:  # Show first 5
                print(f"    - {vid}")
            if len(shared['vertices']) > 5:
                print(f"    ... and {len(shared['vertices']) - 5} more")

        print(f"  Edges: {len(shared['edges'])}")
        if shared['edges']:
            for eid in sorted(list(shared['edges']))[:5]:
                print(f"    - {eid}")
            if len(shared['edges']) > 5:
                print(f"    ... and {len(shared['edges']) - 5} more")

        print(f"  Faces: {len(shared['faces'])}")
        if shared['faces']:
            for fid in sorted(list(shared['faces']))[:5]:
                print(f"    - {fid}")
            if len(shared['faces']) > 5:
                print(f"    ... and {len(shared['faces']) - 5} more")

    # Perform union
    composed_vertices_full = union_elements_full(chart1, chart2, 'vertices')
    composed_edges_full = union_elements_full(chart1, chart2, 'edges')
    composed_faces_full = union_elements_full(chart1, chart2, 'faces')

    V = len(composed_vertices_full)
    E = len(composed_edges_full)
    F = len(composed_faces_full)
    chi = V - E + F

    if verbose:
        print(f"\nResult: V={V}, E={E}, F={F}, χ={chi}")

    # Build composed chart JSON
    # Preserve composition history
    source_charts = []
    if "composition" in chart1:
        source_charts.extend(chart1["composition"].get("source_charts", []))
    else:
        source_charts.append(chart1.get("id", chart1.get("name", "unknown")))

    if "composition" in chart2:
        source_charts.extend(chart2["composition"].get("source_charts", []))
    else:
        source_charts.append(chart2.get("id", chart2.get("name", "unknown")))

    composed = {
        "type": "chart/syllabus",
        "id": f"c:composition:multi-step-{step}",
        "name": f"Composed Chart (Step {step}/{total})",
        "description": f"Iterative composition of multiple charts (step {step})",
        "composition": {
            "method": "iterative_pairwise_identification",
            "step": step,
            "total_steps": total,
            "source_charts": source_charts,
            "shared_vertices": sorted(shared['vertices']),
            "shared_edges": sorted(shared['edges']),
            "shared_faces": sorted(shared['faces'])
        },
        "elements": {
            "vertices": composed_vertices_full,
            "edges": composed_edges_full,
            "faces": composed_faces_full
        },
        "element_counts": {
            "vertices": V,
            "edges": E,
            "faces": F
        },
        "topology": {
            "V": V,
            "E": E,
            "F": F,
            "chi": chi,
            "euler_characteristic": chi
        }
    }

    return composed


def compose_charts_multi(chart_paths: List[Path], output_path: Path,
                         name: str = None, description: str = None,
                         verbose: bool = True) -> Dict[str, Any]:
    """
    Compose multiple charts through iterative pairwise composition.

    Args:
        chart_paths: List of paths to chart JSON files (in order)
        output_path: Path to write final composed chart
        name: Optional name for final chart
        description: Optional description for final chart
        verbose: Print detailed progress

    Returns:
        Final composed chart as dictionary
    """

    if len(chart_paths) < 2:
        raise ValueError("Need at least 2 charts to compose")

    if verbose:
        print(f"Multi-Chart Composition")
        print(f"{'='*60}")
        print(f"Input charts: {len(chart_paths)}")
        for i, path in enumerate(chart_paths, 1):
            print(f"  {i}. {path.name}")
        print(f"Output: {output_path.name}")
        print(f"Total composition steps: {len(chart_paths) - 1}")

    # Load first chart
    current = load_chart(chart_paths[0])

    # Iteratively compose with remaining charts
    total_steps = len(chart_paths) - 1
    for step, chart_path in enumerate(chart_paths[1:], 1):
        next_chart = load_chart(chart_path)
        current = compose_two_charts(current, next_chart, step, total_steps, verbose)

    # Update final metadata
    if name:
        current["name"] = name
    if description:
        current["description"] = description

    current["id"] = f"c:composition:learning-journey-full"
    current["composition"]["method"] = "iterative_pairwise_identification"
    current["composition"]["final"] = True

    # Write output
    if verbose:
        print(f"\n{'='*60}")
        print(f"Writing final composed chart to {output_path}...")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(current, f, indent=2)

    if verbose:
        print(f"✓ Multi-chart composition complete")
        print(f"\nFinal topology:")
        print(f"  Vertices: {current['topology']['V']}")
        print(f"  Edges: {current['topology']['E']}")
        print(f"  Faces: {current['topology']['F']}")
        print(f"  Euler characteristic: χ = {current['topology']['chi']}")

    return current


def main():
    if len(sys.argv) < 3:
        print("Usage: python compose_charts_multi.py <output.json> <chart1.json> <chart2.json> [chart3.json ...]")
        print("\nExample:")
        print("  python scripts/compose_charts_multi.py \\")
        print("    charts/learning-journey-full.json \\")
        print("    charts/learning-journey-module-01/learning-journey-module-01.json \\")
        print("    charts/learning-journey-module-02/learning-journey-module-02.json \\")
        print("    charts/learning-journey-module-03/learning-journey-module-03.json")
        print("\nNote: Charts are composed in the order provided (left to right)")
        sys.exit(1)

    output_path = Path(sys.argv[1])
    chart_paths = [Path(p) for p in sys.argv[2:]]

    # Validate inputs
    for path in chart_paths:
        if not path.exists():
            print(f"Error: {path} not found")
            sys.exit(1)

    # Compose
    compose_charts_multi(
        chart_paths,
        output_path,
        name="Learning Journey - Modules 01-07 (Complete)",
        description="Full learning journey from fundamentals through document architecture",
        verbose=True
    )


if __name__ == "__main__":
    main()
