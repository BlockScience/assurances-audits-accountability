"""
Build complex.json cache from markdown files.

Scans directories for vertices, edges, faces, and charts, parses them,
and generates a JSON cache file with all element metadata.
"""

import json
import yaml
from pathlib import Path
from datetime import datetime, date, timezone
from typing import Dict, Any, List, Optional

from .parse import parse_directory, ParseError


def load_registry(root_path: Path) -> Optional[Dict[str, Any]]:
    """
    Load content registry from content/registry.yaml if it exists.

    Args:
        root_path: Root directory of the repository

    Returns:
        Registry dictionary or None if not found
    """
    registry_path = root_path / 'content' / 'registry.yaml'
    if registry_path.exists():
        return yaml.safe_load(registry_path.read_text(encoding='utf-8'))
    return None


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
    elif isinstance(obj, date):
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


def build_cache(root_path: Path, output_path: Path = None, include_foundation: bool = True) -> Dict[str, Any]:
    """
    Build complex.json cache from directory structure.

    Scans directories from registry.yaml if present, otherwise uses defaults:
    - Root directories: 00_vertices/, 01_edges/, 02_faces/, charts/
    - Content directories: content/*/00_vertices/, content/*/01_edges/, etc.
    - Foundation directory (if include_foundation=True): src/aaa/foundation/

    Args:
        root_path: Root directory containing element directories
        output_path: Optional path for complex.json (defaults to root_path/complex.json)
        include_foundation: Whether to include bundled foundation elements (default True)

    Returns:
        Cache dictionary

    Raises:
        ParseError: If any element fails to parse
    """
    if output_path is None:
        output_path = root_path / 'complex.json'

    # Parse all directories
    print(f"Building cache for: {root_path}")

    vertices = []
    edges = []
    faces = []

    # Load registry if present
    registry = load_registry(root_path)

    if registry:
        print("  Using content registry")

        # Parse root directories (boundary elements)
        if 'root' in registry:
            root_paths = registry['root'].get('paths', {})
            if 'vertices' in root_paths:
                vertices.extend(parse_directory(root_path / root_paths['vertices'], 'vertex'))
            if 'edges' in root_paths:
                edges.extend(parse_directory(root_path / root_paths['edges'], 'edge'))
            if 'faces' in root_paths:
                faces.extend(parse_directory(root_path / root_paths['faces'], 'face'))

        # Parse content domain directories
        for domain_name, domain_config in registry.get('domains', {}).items():
            paths = domain_config.get('paths', {})
            if 'vertices' in paths:
                domain_vertices = parse_directory(root_path / paths['vertices'], 'vertex')
                vertices.extend(domain_vertices)
            if 'edges' in paths:
                domain_edges = parse_directory(root_path / paths['edges'], 'edge')
                edges.extend(domain_edges)
            if 'faces' in paths:
                domain_faces = parse_directory(root_path / paths['faces'], 'face')
                faces.extend(domain_faces)
            # Also parse doc directories for design documents
            if 'docs' in paths:
                doc_vertices = parse_directory(root_path / paths['docs'], 'vertex')
                vertices.extend(doc_vertices)

        # Parse foundation if specified and requested
        if include_foundation and 'foundation' in registry:
            foundation_paths = registry['foundation'].get('paths', {})
            if 'vertices' in foundation_paths:
                vertices.extend(parse_directory(root_path / foundation_paths['vertices'], 'vertex'))
            if 'edges' in foundation_paths:
                edges.extend(parse_directory(root_path / foundation_paths['edges'], 'edge'))
            if 'faces' in foundation_paths:
                faces.extend(parse_directory(root_path / foundation_paths['faces'], 'face'))
    else:
        # Fallback to hardcoded directories for backwards compatibility
        print("  No registry found, using default directories")

        # Root directories
        vertices_dir = root_path / '00_vertices'
        edges_dir = root_path / '01_edges'
        faces_dir = root_path / '02_faces'

        # Foundation directories (bundled with package)
        foundation_dir = root_path / 'src' / 'aaa' / 'foundation'
        foundation_vertices_dir = foundation_dir / '00_vertices'
        foundation_edges_dir = foundation_dir / '01_edges'
        foundation_faces_dir = foundation_dir / '02_faces'

        # Parse vertices from root and optionally foundation
        vertices = parse_directory(vertices_dir, 'vertex')
        if include_foundation and foundation_vertices_dir.exists():
            vertices.extend(parse_directory(foundation_vertices_dir, 'vertex'))

        # Parse edges from root and optionally foundation
        edges = parse_directory(edges_dir, 'edge')
        if include_foundation and foundation_edges_dir.exists():
            edges.extend(parse_directory(foundation_edges_dir, 'edge'))

        # Parse faces from root and optionally foundation
        faces = parse_directory(faces_dir, 'face')
        if include_foundation and foundation_faces_dir.exists():
            faces.extend(parse_directory(foundation_faces_dir, 'face'))

    # Always parse charts directory
    charts_dir = root_path / 'charts'
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
