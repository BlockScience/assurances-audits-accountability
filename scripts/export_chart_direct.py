#!/usr/bin/env python3
"""
Export chart to JSON by directly reading element files (no cache dependency).

Usage:
    python scripts/export_chart_direct.py charts/test-tetrahedron.md
"""

import sys
import json
import yaml
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        raise ValueError("No frontmatter found")
    return yaml.safe_load(match.group(1))


def build_element_index(base_path: Path) -> Dict[str, Path]:
    """Build a mapping of element ID to file path by scanning directories."""
    index = {}

    # Scan vertices
    vertices_dir = base_path / '00_vertices'
    if vertices_dir.exists():
        for md_file in vertices_dir.glob('*.md'):
            try:
                content = md_file.read_text()
                fm = parse_frontmatter(content)
                if 'id' in fm:
                    index[fm['id']] = md_file
            except:
                pass

    # Scan edges
    edges_dir = base_path / '01_edges'
    if edges_dir.exists():
        for md_file in edges_dir.glob('*.md'):
            try:
                content = md_file.read_text()
                fm = parse_frontmatter(content)
                if 'id' in fm:
                    index[fm['id']] = md_file
            except:
                pass

    # Scan faces
    faces_dir = base_path / '02_faces'
    if faces_dir.exists():
        for md_file in faces_dir.glob('*.md'):
            try:
                content = md_file.read_text()
                fm = parse_frontmatter(content)
                if 'id' in fm:
                    index[fm['id']] = md_file
            except:
                pass

    return index


def read_element(element_id: str, element_index: Dict[str, Path]) -> Dict[str, Any]:
    """Read element file and extract key info using element index."""
    # Look up element path in index
    element_path = element_index.get(element_id)
    if not element_path:
        return None

    with open(element_path, 'r') as f:
        content = f.read()

    fm = parse_frontmatter(content)

    # Build element dict based on type
    element = {
        'id': fm['id'],
        'name': fm['name'],
        'type': fm['type']
    }

    # Add type-specific fields
    if element_id.startswith('e:') or element_id.startswith('b1:'):
        element['source'] = fm.get('source')
        element['target'] = fm.get('target')
        element['element_type'] = 'edge'
    elif element_id.startswith('f:') or element_id.startswith('b2:'):
        element['boundary'] = fm.get('boundary', [])
        element['vertices'] = fm.get('vertices', [])
        element['element_type'] = 'face'
    else:
        element['element_type'] = 'vertex'

    return element


def export_chart(chart_path: Path) -> Dict[str, Any]:
    """Export chart to JSON structure."""
    # Find repo root by looking for 00_vertices directory
    base_path = chart_path.parent
    while base_path != base_path.parent:
        if (base_path / '00_vertices').exists():
            break
        base_path = base_path.parent

    if not (base_path / '00_vertices').exists():
        raise ValueError(f"Cannot find repo root from {chart_path}")

    # Build element index
    element_index = build_element_index(base_path)

    # Read chart
    with open(chart_path, 'r') as f:
        content = f.read()

    fm = parse_frontmatter(content)

    # Get element IDs
    elements = fm.get('elements', {})
    vertex_ids = elements.get('vertices', [])
    edge_ids = elements.get('edges', [])
    face_ids = elements.get('faces', [])

    # Read element details
    vertices = []
    for v_id in vertex_ids:
        elem = read_element(v_id, element_index)
        if elem:
            vertices.append(elem)

    edges = []
    for e_id in edge_ids:
        elem = read_element(e_id, element_index)
        if elem:
            edges.append(elem)

    faces = []
    for f_id in face_ids:
        elem = read_element(f_id, element_index)
        if elem:
            faces.append(elem)

    # Helper to convert datetime objects to ISO strings
    def serialize_value(val):
        if isinstance(val, datetime):
            return val.isoformat()
        elif isinstance(val, dict):
            return {k: serialize_value(v) for k, v in val.items()}
        elif isinstance(val, list):
            return [serialize_value(v) for v in val]
        else:
            return val

    # Build chart JSON
    # Make source_file path relative to base_path
    try:
        relative_source = chart_path.relative_to(base_path)
    except ValueError:
        # If chart_path is not under base_path, use name only
        relative_source = chart_path.name

    chart_json = {
        'chart_id': fm['id'],
        'name': fm['name'],
        'description': fm.get('description', ''),
        'type': fm['type'],
        'constructed_by': fm.get('constructed_by', ''),
        'construction_method': fm.get('construction_method', ''),
        'purpose': fm.get('purpose', ''),
        'scope': fm.get('scope', ''),
        'element_counts': {
            'vertices': len(vertices),
            'edges': len(edges),
            'faces': len(faces)
        },
        'topology': {
            'euler_characteristic': len(vertices) - len(edges) + len(faces),
            'dimension': 2 if faces else (1 if edges else 0)
        },
        'elements': {
            'vertices': vertices,
            'edges': edges,
            'faces': faces
        },
        'metadata': {
            'exported': datetime.now().isoformat(),
            'source_file': str(relative_source)
        }
    }

    # Add assurance_requirements if this is an assurance_audit chart
    if fm['type'] == 'chart/assurance_audit':
        assurance_reqs = fm.get('assurance_requirements', {})
        chart_json['assurance_requirements'] = serialize_value(assurance_reqs)
        # Also add audit-specific fields at root level for convenience
        chart_json['audit_targets'] = assurance_reqs.get('audit_targets', [])
        chart_json['audit_date'] = serialize_value(fm.get('audit_date', ''))
        chart_json['auditor'] = fm.get('auditor', '')
        chart_json['audit_status'] = fm.get('audit_status', '')

    return chart_json


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/export_chart_direct.py charts/test-tetrahedron.md")
        sys.exit(1)

    chart_path = Path(sys.argv[1])
    if not chart_path.exists():
        print(f"Error: Chart not found: {chart_path}")
        sys.exit(1)

    # Export
    print(f"Exporting: {chart_path.name}")
    data = export_chart(chart_path)

    # Write JSON
    output_path = chart_path.with_suffix('.json')
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ Exported to: {output_path.name}")
    print(f"  V={data['element_counts']['vertices']}, "
          f"E={data['element_counts']['edges']}, "
          f"F={data['element_counts']['faces']}, "
          f"χ={data['topology']['euler_characteristic']}")


if __name__ == '__main__':
    main()
