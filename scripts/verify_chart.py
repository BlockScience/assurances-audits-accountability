"""
Verify that a chart is a valid simplicial complex.

Checks that:
1. All referenced vertices, edges, and faces exist
2. Every edge's boundary vertices are in the chart
3. Every face's boundary edges are in the chart
4. Every face's boundary vertices match its edges' endpoints
"""

import argparse
import json
from pathlib import Path
from typing import Dict, Any, List, Set

from parse_chart import parse_chart, ParseError


class VerificationError(Exception):
    """Raised when chart verification fails."""
    pass


def load_cache(root_path: Path) -> Dict[str, Any]:
    """
    Load complex.json cache.

    Args:
        root_path: Root directory containing complex.json

    Returns:
        Cache dictionary

    Raises:
        VerificationError: If cache doesn't exist or is invalid
    """
    cache_path = root_path / 'complex.json'

    if not cache_path.exists():
        raise VerificationError(
            f"Cache not found: {cache_path}\n"
            f"Run 'python scripts/build_cache.py --path {root_path}' first"
        )

    try:
        return json.loads(cache_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        raise VerificationError(f"Invalid JSON in cache: {e}")


def get_edge_boundary(edge: Dict[str, Any]) -> Set[str]:
    """
    Get the boundary vertices of an edge.

    Args:
        edge: Edge element dictionary

    Returns:
        Set of vertex IDs (source and target)
    """
    return {edge['source'], edge['target']}


def verify_chart_elements(chart: Dict[str, Any], cache: Dict[str, Any]) -> List[str]:
    """
    Verify that all chart elements exist and form a valid simplicial complex.

    Args:
        chart: Parsed chart element
        cache: complex.json cache

    Returns:
        List of error messages (empty if valid)
    """
    errors = []
    elements = chart['elements']

    # Extract element indices from cache
    cached_vertices = cache['elements']['vertices']
    cached_edges = cache['elements']['edges']
    cached_faces = cache['elements']['faces']

    # Verify all vertices exist
    for vertex_id in elements['vertices']:
        if vertex_id not in cached_vertices:
            errors.append(f"Vertex {vertex_id} not found in cache")

    # Verify all edges exist and their boundaries are in the chart
    chart_vertices = set(elements['vertices'])

    for edge_id in elements['edges']:
        if edge_id not in cached_edges:
            errors.append(f"Edge {edge_id} not found in cache")
            continue

        edge = cached_edges[edge_id]
        boundary = get_edge_boundary(edge)

        # Check if boundary vertices are in chart
        missing = boundary - chart_vertices
        if missing:
            errors.append(
                f"Edge {edge_id} has boundary vertices not in chart: {missing}"
            )

    # Verify all faces exist and their boundaries are in the chart
    chart_edges = set(elements['edges'])

    for face_id in elements['faces']:
        if face_id not in cached_faces:
            errors.append(f"Face {face_id} not found in cache")
            continue

        face = cached_faces[face_id]

        # Check if boundary edges are in chart
        face_edges = set(face['edges'])
        missing_edges = face_edges - chart_edges
        if missing_edges:
            errors.append(
                f"Face {face_id} has boundary edges not in chart: {missing_edges}"
            )

        # Check if face vertices are in chart
        face_vertices = set(face['vertices'])
        missing_vertices = face_vertices - chart_vertices
        if missing_vertices:
            errors.append(
                f"Face {face_id} has vertices not in chart: {missing_vertices}"
            )

        # Verify face is a valid 2-simplex:
        # The vertices must be exactly the boundary of the edges
        edge_endpoints = set()
        for edge_id in face['edges']:
            if edge_id in cached_edges:
                edge_endpoints.update(get_edge_boundary(cached_edges[edge_id]))

        if edge_endpoints != face_vertices:
            errors.append(
                f"Face {face_id} vertices {face_vertices} don't match "
                f"edge boundaries {edge_endpoints}"
            )

    return errors


def find_cache_root(start_path: Path) -> Path:
    """
    Search upward from start_path to find directory containing complex.json.

    Args:
        start_path: Starting directory to search from

    Returns:
        Path to directory containing complex.json

    Raises:
        VerificationError: If complex.json not found in any parent directory
    """
    current = start_path.resolve()

    # Search upward through parent directories
    while current != current.parent:  # Stop at filesystem root
        cache_path = current / 'complex.json'
        if cache_path.exists():
            return current
        current = current.parent

    # Check filesystem root
    if (current / 'complex.json').exists():
        return current

    raise VerificationError(
        f"complex.json not found in any parent directory of {start_path}\n"
        f"Run 'python scripts/build_cache.py' from the repository root first"
    )


def verify_chart_file(chart_path: Path, root_path: Path = None) -> List[str]:
    """
    Verify a chart file.

    Args:
        chart_path: Path to chart markdown file
        root_path: Root directory (defaults to searching upward for complex.json)

    Returns:
        List of error messages (empty if valid)
    """
    errors = []

    # Parse chart
    try:
        chart = parse_chart(chart_path)
    except ParseError as e:
        return [f"Parse error: {e}"]

    # Determine root path by searching upward for complex.json
    if root_path is None:
        try:
            root_path = find_cache_root(chart_path.parent)
        except VerificationError as e:
            return [str(e)]

    # Load cache
    try:
        cache = load_cache(root_path)
    except VerificationError as e:
        return [str(e)]

    # Verify chart structure
    errors.extend(verify_chart_elements(chart, cache))

    return errors


def main():
    """Command-line interface for verify_chart."""
    parser = argparse.ArgumentParser(
        description='Verify that a chart is a valid simplicial complex'
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

    args = parser.parse_args()

    errors = verify_chart_file(args.chart, args.root)

    if errors:
        print(f"✗ Chart verification failed for {args.chart}:")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print(f"✓ Chart {args.chart} is a valid simplicial complex")
        return 0


if __name__ == '__main__':
    exit(main())
