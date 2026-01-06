#!/usr/bin/env python3
"""
Generate complete element set for an assurance audit chart from vertex list.

Uses backtracking algorithm:
1. Start with target vertices in "needs assurance" set
2. For each vertex needing assurance, create its assurance face
3. The face introduces verification target (spec) and validation target (guidance)
4. If those targets aren't assured yet, add them to "needs assurance"
5. Recurse until all unassured vertices are boundary complex members (SS, GS, SG, GG)
6. Add boundary complex (root + 4 boundary faces) to close out

Invariant: F = V - 1 (every vertex except root has exactly one assurance face)

Usage:
    python scripts/generate_assurance_audit_elements.py c:test-tetrahedron
    python scripts/generate_assurance_audit_elements.py c:test-tetrahedron c:learning-journey-module-01
"""

import sys
import json
from typing import Dict, List, Set, Tuple

# Boundary complex vertices
BOUNDARY_COMPLEX = {'v:spec:spec', 'v:spec:guidance', 'v:guidance:spec', 'v:guidance:guidance'}

# What spec does each vertex type verify against?
def get_verification_target(vertex_id: str) -> str:
    """Return the spec this vertex verifies against."""
    if vertex_id.startswith('v:spec:'):
        # All specs verify against spec-for-spec
        return 'v:spec:spec'
    elif vertex_id.startswith('v:guidance:'):
        # All guidances verify against spec-for-guidance
        return 'v:spec:guidance'
    elif vertex_id.startswith('c:'):
        # Charts verify against their type spec
        # We need to know the chart's type - infer from ID or use lookup
        chart_type = get_chart_type(vertex_id)
        return f'v:spec:{chart_type}'
    else:
        raise ValueError(f"Unknown vertex type: {vertex_id}")

# What guidance does each vertex type validate against?
def get_validation_target(vertex_id: str) -> str:
    """Return the guidance this vertex validates against."""
    if vertex_id.startswith('v:spec:'):
        # All specs validate against guidance-for-spec
        return 'v:guidance:spec'
    elif vertex_id.startswith('v:guidance:'):
        # All guidances validate against guidance-for-guidance
        return 'v:guidance:guidance'
    elif vertex_id.startswith('c:'):
        # Charts validate against their type guidance
        chart_type = get_chart_type(vertex_id)
        return f'v:guidance:{chart_type}'
    else:
        raise ValueError(f"Unknown vertex type: {vertex_id}")

# Chart type lookup - maps chart instance IDs to their document type
CHART_TYPES = {
    'c:test-tetrahedron': 'chart',
    'c:boundary-complex': 'chart',
    'c:learning-journey-module-01': 'syllabus',
    'c:learning-journey-module-02': 'syllabus',
    'c:learning-journey-module-03': 'syllabus',
    'c:learning-journey-module-04': 'syllabus',
    'c:learning-journey-module-05': 'syllabus',
    'c:learning-journey-module-06': 'syllabus',
    'c:learning-journey-module-07': 'syllabus',
    'c:learning-journey-module-08': 'syllabus',
    'c:learning-journey-module-09': 'syllabus',
    'c:learning-journey-module-10': 'syllabus',
    'c:chart-types-audit': 'assurance_audit',
}

def get_chart_type(chart_id: str) -> str:
    """Get the document type for a chart instance."""
    if chart_id in CHART_TYPES:
        return CHART_TYPES[chart_id]
    # Default to base chart type for unknown charts
    return 'chart'


class AssuranceAuditGenerator:
    """Generate complete element set for assurance audit chart using backtracking."""

    def __init__(self):
        self.vertices: Set[str] = set()
        self.edges: Set[str] = set()
        self.faces: Set[str] = set()

        # Backtracking state
        self.needs_assurance: Set[str] = set()
        self.assured: Set[str] = set()

    def generate(self, target_vertices: List[str]) -> Dict:
        """
        Generate complete element set for assurance audit chart.

        Args:
            target_vertices: List of concrete vertex IDs to be assured

        Returns:
            Dict with vertices, edges, faces lists
        """
        # Initialize: all targets need assurance
        for v in target_vertices:
            self.vertices.add(v)
            self.needs_assurance.add(v)

        # Backtrack until only boundary complex vertices remain unassured
        while self.needs_assurance - BOUNDARY_COMPLEX:
            # Pick a vertex that needs assurance and isn't in boundary complex
            vertex = next(v for v in self.needs_assurance if v not in BOUNDARY_COMPLEX)
            self._assure_vertex(vertex)

        # Now only boundary complex vertices need assurance
        # Add boundary complex to close everything out
        self._add_boundary_complex()

        return {
            'vertices': sorted(self.vertices),
            'edges': sorted(self.edges),
            'faces': sorted(self.faces),
            'metadata': {
                'total_vertices': len(self.vertices),
                'total_edges': len(self.edges),
                'total_faces': len(self.faces),
                'euler_characteristic': len(self.vertices) - len(self.edges) + len(self.faces)
            }
        }

    def _assure_vertex(self, vertex_id: str):
        """Create assurance face for a vertex, potentially introducing new vertices."""
        if vertex_id in self.assured:
            return
        if vertex_id in BOUNDARY_COMPLEX:
            return  # Boundary complex handled separately

        # Get verification and validation targets
        verification_target = get_verification_target(vertex_id)
        validation_target = get_validation_target(vertex_id)

        # Add the target vertices
        self.vertices.add(verification_target)
        self.vertices.add(validation_target)

        # Create edges
        vertex_short = self._short_name(vertex_id)
        verif_short = self._short_name(verification_target)
        valid_short = self._short_name(validation_target)

        verification_edge = f"e:verification:{vertex_short}:{verif_short}"
        validation_edge = f"e:validation:{vertex_short}:{valid_short}"
        coupling_edge = self._coupling_edge(verification_target, validation_target)

        self.edges.add(verification_edge)
        self.edges.add(validation_edge)
        self.edges.add(coupling_edge)

        # Create assurance face for this vertex
        face_id = f"f:assurance:{vertex_short}"
        self.faces.add(face_id)

        # Mark this vertex as assured
        self.assured.add(vertex_id)
        self.needs_assurance.discard(vertex_id)

        # The targets may now need assurance (if not already assured)
        if verification_target not in self.assured:
            self.needs_assurance.add(verification_target)
        if validation_target not in self.assured:
            self.needs_assurance.add(validation_target)

    def _add_boundary_complex(self):
        """Add boundary complex: root vertex and 4 boundary faces."""
        # Add root vertex
        self.vertices.add('b0:root')

        # Add boundary complex vertices (should already be there from backtracking)
        for v in BOUNDARY_COMPLEX:
            self.vertices.add(v)

        # Boundary edges (connect to root)
        self.edges.add('b1:self-verification')      # SS → root
        self.edges.add('b1:self-validation')        # GG → root
        self.edges.add('b1:couples-GS-root')        # root → GS
        self.edges.add('b1:couples-SG-root')        # root → SG

        # Internal boundary complex edges
        # SS needs: verification (to itself via root), validation (to GS), coupling (SS-GS)
        self.edges.add('e:validation:spec-spec:guidance-spec')
        self.edges.add('e:coupling:spec')  # SS ↔ GS

        # GG needs: verification (to SG), validation (to itself via root), coupling (SG-GG)
        self.edges.add('e:verification:guidance-guidance:spec-guidance')
        self.edges.add('e:coupling:guidance')  # SG ↔ GG

        # SG needs: verification (to SS), validation (to GS), coupling (cross-domain)
        self.edges.add('e:verification:spec-guidance:spec-spec')
        self.edges.add('e:validation:spec-guidance:guidance-spec')
        self.edges.add('e:coupling:spec-guidance:guidance-spec')  # SG ↔ GS cross-domain

        # GS needs: verification (to SG), validation (to GG), coupling (cross-domain, already added)
        self.edges.add('e:verification:guidance-spec:spec-guidance')
        self.edges.add('e:validation:guidance-spec:guidance-guidance')

        # Boundary faces (b2) - one for each boundary complex vertex
        self.faces.add('b2:spec-spec')           # Assures SS
        self.faces.add('b2:guidance-guidance')   # Assures GG
        self.faces.add('f:assurance:spec-guidance')   # Assures SG
        self.faces.add('f:assurance:guidance-spec')   # Assures GS

        # Mark all as assured
        self.assured.add('b0:root')  # Root doesn't need assurance (it's the anchor)
        for v in BOUNDARY_COMPLEX:
            self.assured.add(v)
            self.needs_assurance.discard(v)

    def _short_name(self, vertex_id: str) -> str:
        """Extract short name from vertex ID."""
        if vertex_id.startswith('v:spec:'):
            return vertex_id.replace('v:spec:', '') + '-spec'
        elif vertex_id.startswith('v:guidance:'):
            return vertex_id.replace('v:guidance:', '') + '-guidance'
        elif vertex_id.startswith('c:'):
            return vertex_id.replace('c:', '')
        elif vertex_id.startswith('b0:'):
            return vertex_id.replace('b0:', '')
        else:
            return vertex_id

    def _coupling_edge(self, spec_vertex: str, guidance_vertex: str) -> str:
        """Create coupling edge ID for a spec-guidance pair."""
        spec_type = spec_vertex.replace('v:spec:', '')
        guidance_type = guidance_vertex.replace('v:guidance:', '')

        if spec_type == guidance_type:
            # Same type: e:coupling:chart, e:coupling:syllabus, etc.
            return f'e:coupling:{spec_type}'
        else:
            # Cross-domain: e:coupling:spec-guidance:guidance-spec
            return f'e:coupling:{spec_type}:{guidance_type}'


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nError: No target vertices specified")
        sys.exit(1)

    # Parse arguments
    target_vertices = []
    output_file = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--output':
            if i + 1 >= len(args):
                print("Error: --output requires a filename")
                sys.exit(1)
            output_file = args[i + 1]
            i += 2
        else:
            target_vertices.append(args[i])
            i += 1

    if not target_vertices:
        print("Error: No target vertices specified")
        sys.exit(1)

    # Generate elements
    generator = AssuranceAuditGenerator()
    result = generator.generate(target_vertices)

    # Output
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)
        print(f"✓ Generated elements for {len(target_vertices)} target vertices")
        print(f"✓ Written to: {output_file}")
    else:
        print(json.dumps(result, indent=2))

    # Print summary
    print(f"\nSummary:")
    print(f"  Vertices: {result['metadata']['total_vertices']}")
    print(f"  Edges: {result['metadata']['total_edges']}")
    print(f"  Faces: {result['metadata']['total_faces']}")
    print(f"  Euler characteristic (χ): {result['metadata']['euler_characteristic']}")

    # Verify invariant
    v = result['metadata']['total_vertices']
    f = result['metadata']['total_faces']
    if f == v - 1:
        print(f"  ✓ Invariant holds: F = V - 1 ({f} = {v} - 1)")
    else:
        print(f"  ✗ Invariant VIOLATED: F = {f}, V - 1 = {v - 1}")


if __name__ == '__main__':
    main()
