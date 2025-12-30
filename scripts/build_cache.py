"""
Build complex.json cache from markdown files.

Scans directories for vertices, edges, faces, and charts, parses them,
and generates a JSON cache file with all element metadata.
"""

import json
import argparse
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, List

from parse_chart import parse_directory, ParseError


def sanitize_for_json(obj: Any) -> Any:
    """
    Recursively convert non-JSON-serializable objects to JSON-safe types.

    Args:
        obj: Object to sanitize

    Returns:
        JSON-serializable version of obj
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: sanitize_for_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize_for_json(item) for item in obj]
    else:
        return obj


def calculate_euler_characteristic(vertices: List, edges: List, faces: List) -> int:
    """
    Calculate Euler characteristic: χ = V - E + F

    Args:
        vertices: List of vertex elements
        edges: List of edge elements
        faces: List of face elements

    Returns:
        Euler characteristic (integer)
    """
    return len(vertices) - len(edges) + len(faces)


def build_cache(root_path: Path, output_path: Path = None) -> Dict[str, Any]:
    """
    Build complex.json cache from directory structure.

    Args:
        root_path: Root directory containing element directories
        output_path: Optional path for complex.json (defaults to root_path/complex.json)

    Returns:
        Cache dictionary

    Raises:
        ParseError: If any element fails to parse
    """
    if output_path is None:
        output_path = root_path / 'complex.json'

    # Parse all directories
    print(f"Building cache for: {root_path}")

    vertices_dir = root_path / '00_vertices'
    edges_dir = root_path / '01_edges'
    faces_dir = root_path / '02_faces'
    charts_dir = root_path / 'charts'

    vertices = parse_directory(vertices_dir, 'vertex')
    edges = parse_directory(edges_dir, 'edge')
    faces = parse_directory(faces_dir, 'face')
    charts = parse_directory(charts_dir, 'chart')

    print(f"  Parsed {len(vertices)} vertices")
    print(f"  Parsed {len(edges)} edges")
    print(f"  Parsed {len(faces)} faces")
    print(f"  Parsed {len(charts)} charts")

    # Build cache structure
    cache = {
        'version': '1.0.0',
        'generated': datetime.now(timezone.utc).isoformat(),
        'root_path': '.',
        'elements': {
            'vertices': {},
            'edges': {},
            'faces': {},
            'charts': {}
        },
        'statistics': {
            'vertex_count': len(vertices),
            'edge_count': len(edges),
            'face_count': len(faces),
            'chart_count': len(charts),
            'euler_characteristic': calculate_euler_characteristic(vertices, edges, faces)
        }
    }

    # Index elements by ID
    for vertex in vertices:
        # Make file path relative to root
        vertex_copy = vertex.copy()
        vertex_copy['file'] = str(Path(vertex['file']).relative_to(root_path))
        # Remove body from cache (keep only metadata)
        vertex_copy.pop('body', None)
        # Sanitize for JSON serialization
        cache['elements']['vertices'][vertex['id']] = sanitize_for_json(vertex_copy)

    for edge in edges:
        edge_copy = edge.copy()
        edge_copy['file'] = str(Path(edge['file']).relative_to(root_path))
        edge_copy.pop('body', None)
        cache['elements']['edges'][edge['id']] = sanitize_for_json(edge_copy)

    for face in faces:
        face_copy = face.copy()
        face_copy['file'] = str(Path(face['file']).relative_to(root_path))
        face_copy.pop('body', None)
        cache['elements']['faces'][face['id']] = sanitize_for_json(face_copy)

    for chart in charts:
        chart_copy = chart.copy()
        chart_copy['file'] = str(Path(chart['file']).relative_to(root_path))
        chart_copy.pop('body', None)
        cache['elements']['charts'][chart['id']] = sanitize_for_json(chart_copy)

    # Write cache file
    output_path.write_text(json.dumps(cache, indent=2), encoding='utf-8')
    print(f"\nCache written to: {output_path}")
    print(f"Euler characteristic: χ = {cache['statistics']['euler_characteristic']}")

    return cache


def main():
    """Command-line interface for build_cache."""
    parser = argparse.ArgumentParser(
        description='Build complex.json cache from markdown files'
    )
    parser.add_argument(
        '--path',
        type=Path,
        default=Path.cwd(),
        help='Root directory to scan (default: current directory)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output path for complex.json (default: <path>/complex.json)'
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help='Build and verify all elements (runs verification after build)'
    )

    args = parser.parse_args()

    try:
        cache = build_cache(args.path, args.output)

        if args.verify:
            print("\n=== Running verification ===")
            # Import here to avoid circular dependency
            from verify_structure import verify_all
            errors = verify_all(args.path)
            if errors:
                print(f"\nVerification failed with {len(errors)} errors:")
                for error in errors:
                    print(f"  - {error}")
                return 1
            else:
                print("Verification passed!")

        return 0

    except ParseError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
