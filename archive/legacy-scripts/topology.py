"""
Topological analysis of simplicial complexes.

Detects holes (missing faces) in a simplicial complex by finding all potential
faces (triangles of edges) and checking which ones are actually present.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, Any, List, Set, Tuple
from itertools import combinations

from parse_chart import parse_chart, ParseError


def load_cache(root_path: Path) -> Dict[str, Any]:
    """Load complex.json cache."""
    cache_path = root_path / 'complex.json'
    if not cache_path.exists():
        raise FileNotFoundError(f"Cache not found: {cache_path}")
    return json.loads(cache_path.read_text(encoding='utf-8'))


def get_edge_boundary(edge: Dict[str, Any]) -> Tuple[str, str]:
    """Get the boundary vertices of an edge as a sorted tuple."""
    return tuple(sorted([edge['source'], edge['target']]))


def find_potential_faces(
    vertices: List[str],
    edges: Dict[str, Dict[str, Any]]
) -> List[Tuple[str, str, str]]:
    """
    Find all potential 2-faces (triangles) in the complex.

    A potential face is a triple of vertices (A, B, C) where all three edges
    (A-B, B-C, A-C) exist in the complex.

    Args:
        vertices: List of vertex IDs in the chart
        edges: Dictionary of edge_id -> edge_data

    Returns:
        List of potential face tuples (vertex1, vertex2, vertex3)
    """
    # Build adjacency list from edges
    adjacency: Dict[str, Set[str]] = {v: set() for v in vertices}

    for edge in edges.values():
        v1, v2 = edge['source'], edge['target']
        if v1 in adjacency and v2 in adjacency:
            adjacency[v1].add(v2)
            adjacency[v2].add(v1)

    # Find all triangles
    potential_faces = []

    for v1, v2, v3 in combinations(vertices, 3):
        # Check if all three edges exist
        has_v1_v2 = v2 in adjacency[v1]
        has_v2_v3 = v3 in adjacency[v2]
        has_v1_v3 = v3 in adjacency[v1]

        if has_v1_v2 and has_v2_v3 and has_v1_v3:
            # All edges present - this is a potential face
            potential_faces.append(tuple(sorted([v1, v2, v3])))

    return potential_faces


def find_holes(chart_path: Path, root_path: Path = None) -> Dict[str, Any]:
    """
    Analyze a chart for topological holes.

    Args:
        chart_path: Path to chart markdown file
        root_path: Root directory (defaults to chart_path's grandparent)

    Returns:
        Dictionary with:
            - chart_id: Chart ID
            - potential_faces: List of potential face triples
            - actual_faces: List of actual face IDs with their vertices
            - holes: List of missing face triples
            - euler_characteristic: χ = V - E + F
    """
    # Parse chart
    try:
        chart = parse_chart(chart_path)
    except ParseError as e:
        raise ValueError(f"Parse error: {e}")

    # Determine root path
    if root_path is None:
        root_path = chart_path.parent.parent

    # Load cache
    cache = load_cache(root_path)

    # Get chart elements
    chart_vertices = chart['elements']['vertices']
    chart_edge_ids = chart['elements']['edges']
    chart_face_ids = chart['elements']['faces']

    # Filter cache to only chart elements
    chart_edges = {
        eid: cache['elements']['edges'][eid]
        for eid in chart_edge_ids
        if eid in cache['elements']['edges']
    }

    chart_faces = {
        fid: cache['elements']['faces'][fid]
        for fid in chart_face_ids
        if fid in cache['elements']['faces']
    }

    # Find all potential faces
    potential_faces = find_potential_faces(chart_vertices, chart_edges)

    # Find which potential faces actually exist
    actual_face_vertices = [
        tuple(sorted(face['vertices']))
        for face in chart_faces.values()
    ]

    # Holes are potential faces that don't exist
    holes = [
        face for face in potential_faces
        if face not in actual_face_vertices
    ]

    # Calculate Euler characteristic
    V = len(chart_vertices)
    E = len(chart_edges)
    F = len(chart_faces)
    euler_char = V - E + F

    return {
        'chart_id': chart['id'],
        'chart_name': chart['name'],
        'statistics': {
            'vertices': V,
            'edges': E,
            'faces': F,
            'potential_faces': len(potential_faces),
            'holes': len(holes),
            'euler_characteristic': euler_char
        },
        'potential_faces': [list(pf) for pf in potential_faces],
        'actual_faces': [
            {'id': fid, 'vertices': list(face['vertices'])}
            for fid, face in chart_faces.items()
        ],
        'holes': [list(hole) for hole in holes]
    }


def main():
    """Command-line interface for topology analysis."""
    parser = argparse.ArgumentParser(
        description='Analyze topological properties and detect holes in a chart'
    )
    parser.add_argument(
        'chart',
        type=Path,
        help='Path to chart markdown file'
    )
    parser.add_argument(
        '--root',
        type=Path,
        help='Root directory (default: infer from chart path)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON instead of human-readable format'
    )

    args = parser.parse_args()

    try:
        analysis = find_holes(args.chart, args.root)

        if args.json:
            print(json.dumps(analysis, indent=2))
        else:
            # Human-readable output
            print(f"\n=== Topological Analysis: {analysis['chart_name']} ===\n")

            stats = analysis['statistics']
            print(f"Vertices (V): {stats['vertices']}")
            print(f"Edges (E):    {stats['edges']}")
            print(f"Faces (F):    {stats['faces']}")
            print(f"\nEuler characteristic: χ = V - E + F = {stats['euler_characteristic']}")

            print(f"\nPotential faces (triangles of edges): {stats['potential_faces']}")
            print(f"Actual faces:                         {stats['faces']}")
            print(f"Holes (missing faces):                {stats['holes']}")

            if analysis['holes']:
                print(f"\n⚠️  Detected {len(analysis['holes'])} topological hole(s):")
                for i, hole in enumerate(analysis['holes'], 1):
                    print(f"  {i}. Missing face: {hole}")
            else:
                print("\n✓ No holes detected - chart is a complete simplicial complex")

        return 0

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
