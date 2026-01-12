"""
Audit an assurance_audit chart for complete assurance coverage.

This module validates that an assurance_audit chart has complete coverage
using the Assurances >= Documents invariant (every document vertex has at
least one assurance face).

Document vertices are positively identified by their type prefix:
  - v:spec:*     - specification documents
  - v:guidance:* - guidance documents
  - v:doc:*      - general documents
  - c:*          - charts (which are also documents)

Non-document vertices (do not require assurance):
  - b0:*         - boundary/root vertices
  - v:signer:*   - signer vertices (attestation identities)
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple


# Default boundary complex vertices
BOUNDARY_COMPLEX = {'v:spec:spec', 'v:spec:guidance', 'v:guidance:spec', 'v:guidance:guidance'}


def load_chart(chart_path: Path) -> dict:
    """Load chart markdown and extract frontmatter."""
    with open(chart_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1]
            body = parts[2]
            metadata = yaml.safe_load(frontmatter_text)
        else:
            metadata = {}
            body = content
    else:
        metadata = {}
        body = content

    return {
        'metadata': metadata,
        'content': body,
        'path': chart_path
    }


def load_element(element_id: str, base_dir: Path, search_dirs: List[str] = None) -> Optional[dict]:
    """Load an element (vertex, edge, or face) by ID."""
    if search_dirs is None:
        search_dirs = []

    element_path = None

    # Determine which subdirectory and patterns to use based on element type
    if element_id.startswith('v:') or element_id.startswith('b0:'):
        subdir_name = '00_vertices'
        patterns = [
            f"*{element_id.split(':')[-1]}*.md",
            f"{element_id.replace(':', '-')}.md",
            "b0-root.md" if element_id == 'b0:root' else None
        ]
    elif element_id.startswith('e:') or element_id.startswith('b1:'):
        subdir_name = '01_edges'
        patterns = [
            f"{element_id.replace('e:', '').replace(':', '-')}.md",
            f"{element_id.replace('b1:', 'b1-').replace(':', '-')}.md"
        ]
    elif element_id.startswith('f:') or element_id.startswith('b2:'):
        subdir_name = '02_faces'
        patterns = [
            f"{element_id.replace('f:assurance:', 'assurance-').replace('b2:', 'b2-').replace(':', '-')}.md",
            f"{element_id.replace('f:', '').replace('b2:', 'b2-').replace(':', '-')}.md"
        ]
    else:
        return None

    # First, search in the standard subdirectory
    subdir = base_dir / subdir_name
    for pattern in patterns:
        if pattern:
            if '*' in pattern:
                matches = list(subdir.glob(pattern))
                if matches:
                    element_path = matches[0]
                    break
            else:
                test_path = subdir / pattern
                if test_path.exists():
                    element_path = test_path
                    break

    # If not found in standard location, search in additional directories
    if not element_path:
        for search_dir in search_dirs:
            search_path = Path(search_dir)
            if not search_path.exists():
                continue
            for pattern in patterns:
                if pattern:
                    if '*' in pattern:
                        matches = list(search_path.glob(pattern))
                        if matches:
                            element_path = matches[0]
                            break
                    else:
                        test_path = search_path / pattern
                        if test_path.exists():
                            element_path = test_path
                            break
            if element_path:
                break

    if not element_path or not element_path.exists():
        return None

    with open(element_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1]
            metadata = yaml.safe_load(frontmatter_text)
        else:
            metadata = {}
    else:
        metadata = {}

    return {
        'id': element_id,
        'metadata': metadata,
        'type': metadata.get('type'),
        'path': element_path
    }


def infer_face_target(face_id: str) -> Optional[str]:
    """
    Infer which vertex a face assures based on face ID naming convention.
    """
    if face_id == 'b2:spec-spec':
        return 'v:spec:spec'
    elif face_id == 'b2:guidance-guidance':
        return 'v:guidance:guidance'
    elif face_id.startswith('f:assurance:'):
        suffix = face_id.replace('f:assurance:', '')

        if suffix.endswith('-spec'):
            doc_type = suffix[:-5]
            return f'v:spec:{doc_type}'
        elif suffix.endswith('-guidance'):
            doc_type = suffix[:-9]
            return f'v:guidance:{doc_type}'
        else:
            return f'c:{suffix}'

    return None


def get_face_target(face_id: str, base_dir: Path, search_dirs: List[str] = None) -> Optional[str]:
    """Get the target vertex for a face."""
    face_data = load_element(face_id, base_dir, search_dirs)
    if face_data and face_data.get('metadata'):
        explicit_target = face_data['metadata'].get('target')
        if explicit_target:
            return explicit_target

    return infer_face_target(face_id)


def build_assurance_network_from_frontmatter(
    chart_data: dict,
    base_dir: Path = None,
    search_dirs: List[str] = None
) -> dict:
    """Build assurance network directly from chart frontmatter."""
    if search_dirs is None:
        search_dirs = []

    elements = chart_data['metadata'].get('elements', {})
    vertices = elements.get('vertices', [])
    faces = elements.get('faces', [])

    if base_dir is None:
        chart_path = chart_data.get('path')
        if chart_path:
            base_dir = chart_path.parent.parent.parent
        else:
            base_dir = Path('.')

    assured_vertices = {}
    for face_id in faces:
        target = get_face_target(face_id, base_dir, search_dirs)
        if target:
            assured_vertices[target] = face_id

    root = 'b0:root' if 'b0:root' in vertices else None

    return {
        'faces': faces,
        'vertices': vertices,
        'assured_vertices': assured_vertices,
        'root': root
    }


def is_document_vertex(vertex_id: str) -> bool:
    """
    Determine if a vertex represents a document that requires assurance.
    """
    document_prefixes = (
        'v:spec:',
        'v:guidance:',
        'v:doc:',
        'c:',
    )
    return vertex_id.startswith(document_prefixes)


def check_invariant(network: dict, audit_targets: List[str] = None) -> Tuple[bool, str]:
    """Check the Assurances >= Documents invariant."""
    if audit_targets:
        doc_vertices = [v for v in audit_targets if is_document_vertex(v)]
    else:
        doc_vertices = [v for v in network['vertices'] if is_document_vertex(v)]
    doc_count = len(doc_vertices)

    assurance_faces = [f for f in network['faces']
                       if f.startswith('f:assurance:') or f.startswith('b2:')]
    assurance_count = len(assurance_faces)

    if assurance_count >= doc_count:
        if assurance_count == doc_count:
            return True, f"Assurances = Documents: {assurance_count} assurances for {doc_count} documents"
        else:
            extra = assurance_count - doc_count
            return True, f"Assurances >= Documents: {assurance_count} assurances for {doc_count} documents ({extra} multi-assured)"
    else:
        missing = doc_count - assurance_count
        return False, f"Assurances < Documents: {assurance_count} assurances, {doc_count} documents ({missing} unassured)"


def check_assurance_coverage(network: dict, audit_targets: List[str]) -> dict:
    """Check that all audit targets have assurance faces."""
    covered = []
    uncovered = []

    for vertex_id in audit_targets:
        if not is_document_vertex(vertex_id):
            covered.append(vertex_id)
        elif vertex_id in network['assured_vertices']:
            covered.append(vertex_id)
        else:
            uncovered.append(vertex_id)

    total = len(audit_targets)
    coverage = (len(covered) / total * 100) if total > 0 else 0

    return {
        'covered': covered,
        'uncovered': uncovered,
        'coverage': coverage
    }


def check_boundary_anchoring(network: dict) -> dict:
    """Check that boundary faces exist to anchor the assurance chain."""
    boundary_faces = ['b2:spec-spec', 'b2:guidance-guidance']
    found_faces = [f for f in boundary_faces if f in network['faces']]

    boundary_vertices = []
    if 'b2:spec-spec' in network['faces']:
        boundary_vertices.append('v:spec:spec')
    if 'b2:guidance-guidance' in network['faces']:
        boundary_vertices.append('v:guidance:guidance')

    return {
        'has_boundary': len(found_faces) > 0,
        'boundary_faces': found_faces,
        'boundary_vertices': boundary_vertices
    }


def audit_assurance_chart(chart_path: Path, search_dirs: List[str] = None) -> dict:
    """
    Audit an assurance_audit chart for complete coverage.

    Args:
        chart_path: Path to the assurance audit chart markdown file
        search_dirs: Additional directories to search for faces/edges/vertices

    Returns:
        Dictionary with audit results including status, coverage, and issues
    """
    if search_dirs is None:
        search_dirs = []

    chart_data = load_chart(chart_path)
    chart_id = chart_data['metadata'].get('id', 'unknown')

    chart_type = chart_data['metadata'].get('type')
    if chart_type != 'chart/assurance_audit':
        return {
            'status': 'FAIL',
            'chart_id': chart_id,
            'issues': [f'Chart type is {chart_type}, expected chart/assurance_audit']
        }

    network = build_assurance_network_from_frontmatter(chart_data, search_dirs=search_dirs)

    assurance_reqs = chart_data['metadata'].get('assurance_requirements', {})
    audit_targets = assurance_reqs.get('audit_targets')

    if not audit_targets:
        audit_targets = [v for v in network['vertices'] if v != 'b0:root']

    invariant_passes, invariant_msg = check_invariant(network, audit_targets)
    coverage_result = check_assurance_coverage(network, audit_targets)
    boundary_result = check_boundary_anchoring(network)

    vertex_results = {}
    for vertex_id in network['vertices']:
        if not is_document_vertex(vertex_id):
            if vertex_id.startswith('b0:'):
                note = 'Boundary vertex - provides assurance anchor, not assured itself'
            elif vertex_id.startswith('v:signer:'):
                note = 'Signer vertex - attestation identity, not a document'
            else:
                note = 'Non-document vertex - not subject to assurance'
            vertex_results[vertex_id] = {
                'assured': True,
                'face': None,
                'note': note
            }
        elif vertex_id in network['assured_vertices']:
            vertex_results[vertex_id] = {
                'assured': True,
                'face': network['assured_vertices'][vertex_id]
            }
        else:
            vertex_results[vertex_id] = {
                'assured': False,
                'face': None
            }

    issues = []

    if not invariant_passes:
        issues.append(invariant_msg)

    if coverage_result['uncovered']:
        for v in coverage_result['uncovered']:
            issues.append(f'{v}: Not assured')
            issues.append(f'{v}: No assurance faces found for {v}')

    requires_boundary = assurance_reqs.get('requires_boundary_anchoring', True)

    if not boundary_result['has_boundary'] and requires_boundary:
        issues.append('No boundary faces found - assurance chain not anchored to root')

    boundary_ok = boundary_result['has_boundary'] or not requires_boundary
    status = 'PASS' if (invariant_passes and
                        len(coverage_result['uncovered']) == 0 and
                        boundary_ok) else 'FAIL'

    return {
        'status': status,
        'chart_id': chart_id,
        'vertices_audited': len(audit_targets),
        'vertices_assured': len(coverage_result['covered']),
        'coverage': coverage_result['coverage'],
        'invariant_check': invariant_msg,
        'boundary_check': boundary_result,
        'audit_targets': audit_targets,
        'all_vertices': network['vertices'],
        'vertex_results': vertex_results,
        'summary': f"{status}: {len(coverage_result['covered'])}/{len(audit_targets)} audit targets assured ({coverage_result['coverage']:.1f}%)",
        'issues': issues
    }


def format_audit_trail(audit_result: dict) -> str:
    """Format audit trail as markdown."""
    lines = []
    lines.append(f"# Audit Trail for {audit_result['chart_id']}")
    lines.append("")
    lines.append(f"**Status:** {audit_result['status']}")
    lines.append(f"**Coverage:** {audit_result['coverage']:.1f}% ({audit_result['vertices_assured']}/{audit_result['vertices_audited']} vertices)")
    lines.append(f"**Invariant:** {audit_result['invariant_check']}")
    lines.append("")

    bc = audit_result.get('boundary_check', {})
    if bc.get('has_boundary'):
        lines.append(f"**Boundary Anchoring:** {', '.join(bc.get('boundary_faces', []))}")
    else:
        lines.append("**Boundary Anchoring:** Missing")
    lines.append("")

    lines.append("## Vertex Assurance Results")
    lines.append("")

    for vertex_id, result in sorted(audit_result['vertex_results'].items()):
        status_icon = 'PASS' if result['assured'] else 'FAIL'
        face_info = f" -> {result['face']}" if result.get('face') else ""
        note = f" ({result['note']})" if result.get('note') else ""
        lines.append(f"- [{status_icon}] `{vertex_id}`{face_info}{note}")

    lines.append("")

    if audit_result['issues']:
        lines.append("## Issues")
        lines.append("")
        for issue in audit_result['issues']:
            lines.append(f"- {issue}")
        lines.append("")

    return '\n'.join(lines)
