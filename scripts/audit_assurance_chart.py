#!/usr/bin/env python3
"""
Audit an assurance_audit chart for complete assurance coverage.

This tool validates that an assurance_audit chart has complete coverage
using the Assurances ≥ Documents invariant (every document vertex has at
least one assurance face).

The invariant is: number of assurance faces ≥ number of document vertices.
Some documents may have multiple assurance faces (e.g., a paper assured
against both a base spec and an extended self-demonstration spec).

Document vertices are positively identified by their type prefix:
  - v:spec:*     - specification documents
  - v:guidance:* - guidance documents
  - v:doc:*      - general documents
  - c:*          - charts (which are also documents)

Non-document vertices (do not require assurance):
  - b0:*         - boundary/root vertices
  - v:signer:*   - signer vertices (attestation identities)

This positive identification approach preserves compositionality:
when valid complexes are composed, the invariant holds because we
identify what IS a document rather than excluding what ISN'T.

The tool works directly with chart frontmatter - it does NOT require
separate face files. Face definitions come from the chart's elements.faces
list along with the generator's understanding of face structure.

Usage:
    python scripts/audit_assurance_chart.py charts/chart-types-audit/chart-types-audit.md
    python scripts/audit_assurance_chart.py chart.md --search-dir /path/to/assurance/dir

Options:
    --search-dir DIR    Additional directory to search for faces/edges/vertices.
                        Can be specified multiple times. These directories are
                        searched in addition to the standard 00_vertices/,
                        01_edges/, 02_faces/ locations.

Output:
    - PASS/FAIL status
    - Coverage report
    - Diagnostics for any failures
"""

import sys
import json
import yaml
import argparse
from pathlib import Path
from collections import defaultdict

# Import the generator to understand face structure
try:
    from generate_assurance_audit_elements import (
        get_verification_target,
        get_validation_target,
        get_chart_type,
        BOUNDARY_COMPLEX
    )
    GENERATOR_AVAILABLE = True
except ImportError:
    GENERATOR_AVAILABLE = False
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


def load_element(element_id: str, base_dir: Path, search_dirs: list = None) -> dict:
    """Load an element (vertex, edge, or face) by ID.

    Args:
        element_id: The element ID (e.g., 'v:spec:chart', 'f:assurance:field-survey-wqm')
        base_dir: Base directory containing 00_vertices/, 01_edges/, 02_faces/
        search_dirs: Additional directories to search for elements (flat search)
    """
    if search_dirs is None:
        search_dirs = []

    # Try to find the file by globbing since naming conventions vary
    element_path = None

    # Determine which subdirectory and patterns to use based on element type
    if element_id.startswith('v:') or element_id.startswith('b0:'):
        subdir_name = '00_vertices'
        # Try different patterns
        patterns = [
            f"*{element_id.split(':')[-1]}*.md",
            f"{element_id.replace(':', '-')}.md",
            "b0-root.md" if element_id == 'b0:root' else None
        ]
    elif element_id.startswith('e:') or element_id.startswith('b1:'):
        subdir_name = '01_edges'
        # For edges, the filename usually drops the prefix
        patterns = [
            f"{element_id.replace('e:', '').replace(':', '-')}.md",
            f"{element_id.replace('b1:', 'b1-').replace(':', '-')}.md"
        ]
    elif element_id.startswith('f:') or element_id.startswith('b2:'):
        subdir_name = '02_faces'
        # For faces, pattern is usually assurance-{type}.md or b2-{type}.md
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

    # If not found in standard location, search in additional directories (flat search)
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


def infer_face_target(face_id: str) -> str:
    """
    Infer which vertex a face assures based on face ID naming convention.

    The face ID uses the vertex's "short name" which is:
    - v:spec:X -> X-spec
    - v:guidance:X -> X-guidance
    - c:X -> X

    So the face f:assurance:{short_name} assures the vertex with that short name:
    - f:assurance:chart-spec -> v:spec:chart
    - f:assurance:chart-guidance -> v:guidance:chart
    - f:assurance:guidance-spec -> v:spec:guidance (note: spec for guidance docs)
    - f:assurance:spec-guidance -> v:guidance:spec (note: guidance for spec docs)
    - f:assurance:test-tetrahedron -> c:test-tetrahedron
    - b2:spec-spec -> v:spec:spec
    - b2:guidance-guidance -> v:guidance:guidance
    """
    if face_id == 'b2:spec-spec':
        return 'v:spec:spec'
    elif face_id == 'b2:guidance-guidance':
        return 'v:guidance:guidance'
    elif face_id.startswith('f:assurance:'):
        suffix = face_id.replace('f:assurance:', '')

        if suffix.endswith('-spec'):
            # f:assurance:chart-spec -> v:spec:chart
            # f:assurance:guidance-spec -> v:spec:guidance
            doc_type = suffix[:-5]  # Remove '-spec'
            return f'v:spec:{doc_type}'
        elif suffix.endswith('-guidance'):
            # f:assurance:chart-guidance -> v:guidance:chart
            # f:assurance:spec-guidance -> v:guidance:spec
            doc_type = suffix[:-9]  # Remove '-guidance'
            return f'v:guidance:{doc_type}'
        else:
            # f:assurance:test-tetrahedron -> c:test-tetrahedron
            return f'c:{suffix}'

    return None


def get_face_target(face_id: str, base_dir: Path, search_dirs: list = None) -> str:
    """
    Get the target vertex for a face, preferring explicit metadata over inference.

    First tries to load the face file and read its 'target' field.
    Falls back to infer_face_target() if file not found or no target field.

    Args:
        face_id: The face ID (e.g., 'f:assurance:field-survey-wqm')
        base_dir: Base directory containing 00_vertices/, 01_edges/, 02_faces/
        search_dirs: Additional directories to search for face files
    """
    # Try to load face file and read explicit target
    face_data = load_element(face_id, base_dir, search_dirs)
    if face_data and face_data.get('metadata'):
        explicit_target = face_data['metadata'].get('target')
        if explicit_target:
            return explicit_target

    # Fall back to inference from naming convention
    return infer_face_target(face_id)


def build_assurance_network_from_frontmatter(chart_data: dict, base_dir: Path = None, search_dirs: list = None) -> dict:
    """
    Build assurance network directly from chart frontmatter.

    Uses the F = V - 1 invariant: every vertex except root has exactly
    one face that assures it. Face-to-vertex mapping is read from face
    metadata (preferred) or inferred from face ID naming convention (fallback).

    Args:
        chart_data: Parsed chart data with metadata
        base_dir: Base directory containing 00_vertices/, 01_edges/, 02_faces/
        search_dirs: Additional directories to search for face files

    Returns:
        {
            'faces': [face_ids],
            'vertices': [vertex_ids],
            'assured_vertices': {vertex_id: face_id},  # 1:1 mapping
            'root': 'b0:root' or None
        }
    """
    if search_dirs is None:
        search_dirs = []

    elements = chart_data['metadata'].get('elements', {})

    vertices = elements.get('vertices', [])
    faces = elements.get('faces', [])

    # Determine base directory for loading face files
    if base_dir is None:
        chart_path = chart_data.get('path')
        if chart_path:
            # Go up from charts/<name>/<name>.md to repo root
            base_dir = chart_path.parent.parent.parent
        else:
            base_dir = Path('.')

    # Build vertex -> face mapping
    assured_vertices = {}

    for face_id in faces:
        target = get_face_target(face_id, base_dir, search_dirs)
        if target:
            assured_vertices[target] = face_id

    # Find root
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

    Document vertices are positively identified by their type prefix:
      - v:spec:*     - specification documents
      - v:guidance:* - guidance documents
      - v:doc:*      - general documents
      - c:*          - charts (which are also documents)

    This positive identification preserves compositionality: when valid
    complexes are composed, the invariant holds because we identify what
    IS a document rather than excluding what ISN'T.

    Non-document vertices (b0:*, v:signer:*) are implicitly excluded by
    not matching any document pattern.
    """
    # Positive identification of document vertex types
    document_prefixes = (
        'v:spec:',      # specification documents
        'v:guidance:',  # guidance documents
        'v:doc:',       # general documents
        'c:',           # charts
    )
    return vertex_id.startswith(document_prefixes)


def check_invariant(network: dict, audit_targets: list = None) -> tuple:
    """
    Check the Assurances ≥ Documents invariant.

    Every document vertex should have at least one assurance face.
    Some documents may have multiple assurance faces (e.g., a paper
    assured against both a base spec and an extended self-demonstration spec).

    Document vertices are positively identified (v:spec:*, v:guidance:*,
    v:doc:*, c:*) rather than negatively excluded, which preserves
    compositionality under complex composition.

    Args:
        network: The assurance network dict
        audit_targets: If provided, only count these vertices for the invariant.
                      This is useful for instance-level audits where referenced
                      type vertices are assured elsewhere.

    Returns (passes, message)
    """
    # Count document vertices using positive identification
    if audit_targets:
        # Only consider audit targets for the invariant
        doc_vertices = [v for v in audit_targets if is_document_vertex(v)]
    else:
        doc_vertices = [v for v in network['vertices'] if is_document_vertex(v)]
    doc_count = len(doc_vertices)

    # Count assurance faces (f:assurance:* and b2:*)
    assurance_faces = [f for f in network['faces']
                       if f.startswith('f:assurance:') or f.startswith('b2:')]
    assurance_count = len(assurance_faces)

    if assurance_count >= doc_count:
        if assurance_count == doc_count:
            return True, f"Assurances = Documents: {assurance_count} assurances for {doc_count} documents ✓"
        else:
            extra = assurance_count - doc_count
            return True, f"Assurances ≥ Documents: {assurance_count} assurances for {doc_count} documents ({extra} multi-assured) ✓"
    else:
        missing = doc_count - assurance_count
        return False, f"Assurances < Documents: {assurance_count} assurances, {doc_count} documents ({missing} unassured)"


def check_assurance_coverage(network: dict, audit_targets: list) -> dict:
    """
    Check that all audit targets have assurance faces.

    Returns:
        {
            'covered': [vertex_ids that have faces],
            'uncovered': [vertex_ids missing faces],
            'coverage': float (0-100)
        }
    """
    covered = []
    uncovered = []

    for vertex_id in audit_targets:
        if not is_document_vertex(vertex_id):
            # Non-document vertices (b0:*, v:signer:*) don't need assurance
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
    """
    Check that boundary faces exist to anchor the assurance chain.

    Returns:
        {
            'has_boundary': bool,
            'boundary_faces': [face_ids],
            'boundary_vertices': [vertex_ids that are boundary-assured]
        }
    """
    boundary_faces = ['b2:spec-spec', 'b2:guidance-guidance']
    found_faces = [f for f in boundary_faces if f in network['faces']]

    # Check which boundary vertices are assured
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


def audit_assurance_chart(chart_path: Path, search_dirs: list = None) -> dict:
    """
    Audit an assurance_audit chart for complete coverage.

    Args:
        chart_path: Path to the assurance audit chart markdown file
        search_dirs: Additional directories to search for faces/edges/vertices

    Returns:
        {
            'status': 'PASS' | 'FAIL',
            'chart_id': str,
            'vertices_audited': int,
            'vertices_assured': int,
            'coverage': float,
            'invariant_check': str,
            'boundary_check': dict,
            'vertex_results': {vertex_id: {'assured': bool, 'face': str}},
            'issues': [diagnostic messages]
        }
    """
    if search_dirs is None:
        search_dirs = []

    # Load chart
    chart_data = load_chart(chart_path)
    chart_id = chart_data['metadata'].get('id', 'unknown')

    # Verify this is an assurance_audit chart
    chart_type = chart_data['metadata'].get('type')
    if chart_type != 'chart/assurance_audit':
        return {
            'status': 'FAIL',
            'chart_id': chart_id,
            'issues': [f'Chart type is {chart_type}, expected chart/assurance_audit']
        }

    # Build assurance network from frontmatter
    network = build_assurance_network_from_frontmatter(chart_data, search_dirs=search_dirs)

    # Determine audit targets
    assurance_reqs = chart_data['metadata'].get('assurance_requirements', {})
    audit_targets = assurance_reqs.get('audit_targets')

    if not audit_targets:
        # Audit all vertices except root
        audit_targets = [v for v in network['vertices'] if v != 'b0:root']

    # Check invariant (using audit_targets if specified to scope the check)
    invariant_passes, invariant_msg = check_invariant(network, audit_targets)

    # Check coverage
    coverage_result = check_assurance_coverage(network, audit_targets)

    # Check boundary anchoring
    boundary_result = check_boundary_anchoring(network)

    # Build vertex results
    vertex_results = {}
    for vertex_id in network['vertices']:
        if not is_document_vertex(vertex_id):
            # Non-document vertices (b0:*, v:signer:*) don't require assurance
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

    # Collect issues
    issues = []

    if not invariant_passes:
        issues.append(invariant_msg)

    if coverage_result['uncovered']:
        for v in coverage_result['uncovered']:
            issues.append(f'{v}: Not assured')
            issues.append(f'{v}: No assurance faces found for {v}')

    # Check if boundary anchoring is required (default: True for full audits)
    # Instance-level audits that rely on type-level assurance can set this to false
    requires_boundary = assurance_reqs.get('requires_boundary_anchoring', True)

    if not boundary_result['has_boundary'] and requires_boundary:
        issues.append('No boundary faces found - assurance chain not anchored to root')

    # Determine status
    # PASS requires:
    # 1. Invariant holds (Assurances >= Documents)
    # 2. All audit targets are covered
    # 3. Boundary faces exist (unless requires_boundary_anchoring is false)
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

    # Boundary check
    bc = audit_result.get('boundary_check', {})
    if bc.get('has_boundary'):
        lines.append(f"**Boundary Anchoring:** ✅ {', '.join(bc.get('boundary_faces', []))}")
    else:
        lines.append("**Boundary Anchoring:** ❌ Missing")
    lines.append("")

    lines.append("## Vertex Assurance Results")
    lines.append("")

    for vertex_id, result in sorted(audit_result['vertex_results'].items()):
        status_icon = '✅' if result['assured'] else '❌'
        face_info = f" → {result['face']}" if result.get('face') else ""
        note = f" ({result['note']})" if result.get('note') else ""
        lines.append(f"- {status_icon} `{vertex_id}`{face_info}{note}")

    lines.append("")

    if audit_result['issues']:
        lines.append("## Issues")
        lines.append("")
        for issue in audit_result['issues']:
            lines.append(f"- ❌ {issue}")
        lines.append("")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Audit an assurance_audit chart for complete assurance coverage.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python scripts/audit_assurance_chart.py charts/chart-types-audit/chart-types-audit.md
    python scripts/audit_assurance_chart.py chart.md --search-dir /path/to/assurance/dir
    python scripts/audit_assurance_chart.py chart.md --search-dir dir1 --search-dir dir2
        '''
    )
    parser.add_argument('chart', type=Path, help='Path to the assurance audit chart markdown file')
    parser.add_argument(
        '--search-dir', '-s',
        action='append',
        dest='search_dirs',
        metavar='DIR',
        help='Additional directory to search for faces/edges/vertices. Can be specified multiple times.'
    )

    args = parser.parse_args()

    chart_path = args.chart
    search_dirs = args.search_dirs or []

    if not chart_path.exists():
        print(f"Error: Chart file not found: {chart_path}")
        sys.exit(1)

    print(f"Auditing: {chart_path.name}")
    if search_dirs:
        print(f"Search dirs: {', '.join(search_dirs)}")
    print("")

    # Run audit
    result = audit_assurance_chart(chart_path, search_dirs=search_dirs)

    # Print summary
    print(f"Status: {result['status']}")
    print(f"Invariant: {result['invariant_check']}")
    print(f"Coverage: {result['coverage']:.1f}% ({result['vertices_assured']}/{result['vertices_audited']} targets assured)")
    print("")

    # Boundary check
    bc = result.get('boundary_check', {})
    if bc.get('has_boundary'):
        print(f"Boundary: ✅ {', '.join(bc.get('boundary_faces', []))}")
    else:
        print("Boundary: ❌ Missing")
    print("")

    # Print vertex results
    print("=== Vertex Assurance ===")
    for vertex_id, vresult in sorted(result['vertex_results'].items()):
        status_icon = '✅' if vresult['assured'] else '❌'
        is_target = ' [TARGET]' if vertex_id in result.get('audit_targets', []) else ''
        face_info = f" → {vresult['face']}" if vresult.get('face') else ""
        print(f"{status_icon} {vertex_id}{is_target}{face_info}")

    print("")

    if result['issues']:
        print("Issues:")
        for issue in result['issues']:
            print(f"  - {issue}")
        print("")

    # Generate audit trail markdown
    trail = format_audit_trail(result)
    trail_path = chart_path.parent / f"{chart_path.stem}-audit-trail.md"
    with open(trail_path, 'w', encoding='utf-8') as f:
        f.write(trail)

    print(f"✓ Audit trail written to: {trail_path.name}")

    sys.exit(0 if result['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
