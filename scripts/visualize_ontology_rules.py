#!/usr/bin/env python3
"""
Visualize ontology rule demonstrations.

This script creates visual demonstrations of each ontology rule,
showing both valid and invalid cases for human inspection.

Usage:
    python scripts/visualize_ontology_rules.py

Output:
    tests/fixtures/ontology-rules-demo/
        - rule_edge_endpoints.html       # Edge endpoint type rules
        - rule_vertex_degree.html        # Vertex degree constraints
        - rule_face_boundary_types.html  # Face boundary type rules
        - rule_summary.html              # Summary of all rules
"""

import json
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Any, Optional

# Try plotly, fall back to text output if not available
try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False
    print("Note: plotly not installed. Text-only output will be generated.")

from aaa.core.complex import SimplicialComplex, check_topology
from aaa.core.rules import (
    OntologyRuleEngine,
    check_edge_endpoint_types,
    check_vertex_degree,
    check_face_boundary_types,
    RuleType,
)


OUTPUT_DIR = Path("tests/fixtures/ontology-rules-demo")


@dataclass
class RuleDemo:
    """A demonstration case for an ontology rule."""
    name: str
    description: str
    cache: Dict[str, Any]
    expected_violations: int
    rule_type: str
    explanation: str


# ============================================================
# EDGE ENDPOINT TYPE RULES
# ============================================================

EDGE_ENDPOINT_DEMOS = [
    RuleDemo(
        name="Valid Verification Edge",
        description="doc → spec (CORRECT)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Document'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                },
                'edges': {
                    'e:verification:test': {
                        'id': 'e:verification:test',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="edge_endpoint",
        explanation="Verification edges go from a document/spec/guidance/module to a spec. Here doc → spec is valid."
    ),
    RuleDemo(
        name="Invalid Verification Edge - Wrong Source",
        description="signer → spec (WRONG: signer not allowed as verification source)",
        cache={
            'elements': {
                'vertices': {
                    'v:signer:test': {'id': 'v:signer:test', 'type': 'vertex/signer', 'name': 'Test Signer'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                },
                'edges': {
                    'e:verification:bad': {
                        'id': 'e:verification:bad',
                        'type': 'edge/verification',
                        'source': 'v:signer:test',  # WRONG! Signer can't be verification source
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="edge_endpoint",
        explanation="Verification edges must originate from doc/spec/guidance/module. A SIGNER cannot be a verification source."
    ),
    RuleDemo(
        name="Invalid Verification Edge - Wrong Target",
        description="doc → guidance (WRONG: target should be spec)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:bad': {
                        'id': 'e:verification:bad',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',  # WRONG! Should be vertex/spec
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="edge_endpoint",
        explanation="This verification edge targets GUIDANCE, but verification must target a SPECIFICATION."
    ),
    RuleDemo(
        name="Valid Validation Edge",
        description="doc → guidance (CORRECT)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="edge_endpoint",
        explanation="Validation edges go from document to guidance - human assessment of fitness for purpose."
    ),
    RuleDemo(
        name="Valid Coupling Edge",
        description="spec ↔ guidance (CORRECT - undirected)",
        cache={
            'elements': {
                'vertices': {
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:coupling:test': {
                        'id': 'e:coupling:test',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:test',
                        'orientation': 'undirected',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="edge_endpoint",
        explanation="Coupling edges connect a spec to its corresponding guidance (1:1 relationship)."
    ),
    RuleDemo(
        name="Invalid Signs Edge - Wrong Source",
        description="doc → doc (WRONG: source should be signer)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:a': {'id': 'v:doc:a', 'type': 'vertex/doc', 'name': 'Doc A'},
                    'v:doc:b': {'id': 'v:doc:b', 'type': 'vertex/doc', 'name': 'Doc B'},
                },
                'edges': {
                    'e:signs:bad': {
                        'id': 'e:signs:bad',
                        'type': 'edge/signs',
                        'source': 'v:doc:a',  # WRONG! Should be vertex/signer
                        'target': 'v:doc:b',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="edge_endpoint",
        explanation="Signs edges must originate from a SIGNER (human accountable party), not a document."
    ),
]


# ============================================================
# VERTEX DEGREE RULES
# ============================================================

VERTEX_DEGREE_DEMOS = [
    RuleDemo(
        name="Valid: Doc with One Verification",
        description="Doc → Spec ↔ Guidance (doc has 1 verification edge)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:test': {
                        'id': 'e:verification:test',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:test': {
                        'id': 'e:coupling:test',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:test',
                        'orientation': 'undirected',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="degree",
        explanation="A document can have at most 1 verification edge (verified against one spec). Spec is properly coupled."
    ),
    RuleDemo(
        name="Invalid: Doc with Multiple Verifications",
        description="Doc → Spec1 ↔ G1, Doc → Spec2 ↔ G2 (VIOLATION: doc has 2 verification edges)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:a': {'id': 'v:spec:a', 'type': 'vertex/spec', 'name': 'Spec A'},
                    'v:spec:b': {'id': 'v:spec:b', 'type': 'vertex/spec', 'name': 'Spec B'},
                    'v:guidance:a': {'id': 'v:guidance:a', 'type': 'vertex/guidance', 'name': 'Guidance A'},
                    'v:guidance:b': {'id': 'v:guidance:b', 'type': 'vertex/guidance', 'name': 'Guidance B'},
                },
                'edges': {
                    'e:verification:a': {
                        'id': 'e:verification:a',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:a',
                        'orientation': 'directed',
                    },
                    'e:verification:b': {
                        'id': 'e:verification:b',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:b',
                        'orientation': 'directed',
                    },
                    'e:coupling:a': {
                        'id': 'e:coupling:a',
                        'type': 'edge/coupling',
                        'source': 'v:spec:a',
                        'target': 'v:guidance:a',
                        'orientation': 'undirected',
                    },
                    'e:coupling:b': {
                        'id': 'e:coupling:b',
                        'type': 'edge/coupling',
                        'source': 'v:spec:b',
                        'target': 'v:guidance:b',
                        'orientation': 'undirected',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="degree",
        explanation="A document cannot be verified against multiple specs - max degree is 1. Both specs are properly coupled."
    ),
    RuleDemo(
        name="Valid: Spec with Exactly One Coupling",
        description="Spec ↔ Guidance (exactly 1 coupling)",
        cache={
            'elements': {
                'vertices': {
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:coupling:test': {
                        'id': 'e:coupling:test',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:test',
                        'orientation': 'undirected',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="degree",
        explanation="Each spec couples to exactly one guidance (1:1 relationship)."
    ),
    RuleDemo(
        name="Invalid: Spec with No Coupling",
        description="Spec alone (VIOLATION: must have exactly 1 coupling)",
        cache={
            'elements': {
                'vertices': {
                    'v:spec:orphan': {'id': 'v:spec:orphan', 'type': 'vertex/spec', 'name': 'Orphan Spec'},
                },
                'edges': {},
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="degree",
        explanation="A spec without a coupling edge is incomplete - it needs corresponding guidance."
    ),
    RuleDemo(
        name="Invalid: Spec with Multiple Couplings",
        description="Spec ↔ Guidance1, Spec ↔ Guidance2 (VIOLATION)",
        cache={
            'elements': {
                'vertices': {
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:a': {'id': 'v:guidance:a', 'type': 'vertex/guidance', 'name': 'Guidance A'},
                    'v:guidance:b': {'id': 'v:guidance:b', 'type': 'vertex/guidance', 'name': 'Guidance B'},
                },
                'edges': {
                    'e:coupling:a': {
                        'id': 'e:coupling:a',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:a',
                        'orientation': 'undirected',
                    },
                    'e:coupling:b': {
                        'id': 'e:coupling:b',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:b',
                        'orientation': 'undirected',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="degree",
        explanation="A spec cannot couple to multiple guidances - this creates ambiguity in validation."
    ),
]


# ============================================================
# FACE BOUNDARY TYPE RULES
# ============================================================

FACE_BOUNDARY_DEMOS = [
    RuleDemo(
        name="Valid Assurance Face",
        description="Triangle with verification + validation + coupling",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:test': {
                        'id': 'e:verification:test',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:test': {
                        'id': 'e:coupling:test',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:test',
                        'orientation': 'undirected',
                    },
                },
                'faces': {
                    'f:assurance:test': {
                        'id': 'f:assurance:test',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:test', 'e:validation:test', 'e:coupling:test'],
                        'orientation': 'oriented',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="face_boundary",
        explanation="An assurance face must have all three edge types: verification, validation, and coupling."
    ),
    RuleDemo(
        name="Invalid: Face Missing Validation Edge",
        description="Triangle with verification + coupling (MISSING validation)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:test': {
                        'id': 'e:verification:test',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:test': {
                        'id': 'e:coupling:test',
                        'type': 'edge/coupling',
                        'source': 'v:spec:test',
                        'target': 'v:guidance:test',
                        'orientation': 'undirected',
                    },
                    'e:other:test': {
                        'id': 'e:other:test',
                        'type': 'edge/other',  # Not a validation edge!
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:assurance:bad': {
                        'id': 'f:assurance:bad',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:test', 'e:other:test', 'e:coupling:test'],  # No validation!
                        'orientation': 'oriented',
                    },
                },
            },
        },
        expected_violations=1,
        rule_type="face_boundary",
        explanation="This assurance face is missing a validation edge - human sign-off is required."
    ),
]


def run_demo(demo: RuleDemo) -> Dict[str, Any]:
    """Run a single demonstration and collect results."""
    complex = SimplicialComplex.from_cache(demo.cache)
    engine = OntologyRuleEngine.from_cache(demo.cache)

    # Run specific checks based on rule type
    if demo.rule_type == "edge_endpoint":
        engine._check_edge_endpoint_constraints()
    elif demo.rule_type == "degree":
        engine._check_degree_constraints()
    elif demo.rule_type == "face_boundary":
        # Face boundary type checking - use the local rule function directly
        # Check each assurance face for required edge types
        for face_id, face in complex.faces.items():
            if face.type and 'assurance' in face.type:
                violation = check_face_boundary_types(
                    complex,
                    face_id,
                    required_edge_types=['edge/verification', 'edge/validation', 'edge/coupling'],
                    rule_name="assurance_boundary_types"
                )
                if violation:
                    engine.violations.append(violation)

    violations = engine.violations

    return {
        'name': demo.name,
        'description': demo.description,
        'expected_violations': demo.expected_violations,
        'actual_violations': len(violations),
        'passed': len(violations) == demo.expected_violations,
        'explanation': demo.explanation,
        'violation_messages': [str(v) for v in violations],
        'cache': demo.cache,
    }


def generate_text_report(results: List[Dict[str, Any]], rule_category: str) -> str:
    """Generate a text report for a rule category."""
    lines = []
    lines.append("=" * 70)
    lines.append(f"ONTOLOGY RULE DEMONSTRATION: {rule_category}")
    lines.append("=" * 70)
    lines.append("")

    passed = sum(1 for r in results if r['passed'])
    lines.append(f"Results: {passed}/{len(results)} demonstrations passed")
    lines.append("")

    for i, result in enumerate(results, 1):
        status = "✓ PASS" if result['passed'] else "✗ FAIL"
        lines.append(f"Demo {i}: {result['name']}")
        lines.append(f"  Status: {status}")
        lines.append(f"  Description: {result['description']}")
        lines.append(f"  Expected violations: {result['expected_violations']}")
        lines.append(f"  Actual violations: {result['actual_violations']}")
        lines.append(f"  Explanation: {result['explanation']}")

        if result['violation_messages']:
            lines.append("  Violations found:")
            for msg in result['violation_messages']:
                lines.append(f"    - {msg}")
        lines.append("")

    return "\n".join(lines)


def generate_html_report(results: List[Dict[str, Any]], rule_category: str, output_path: Path):
    """Generate an HTML report with visualizations."""
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Ontology Rule Demo: {rule_category}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; background: #f5f5f5; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        .demo {{ background: white; margin: 20px 0; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .pass {{ border-left: 4px solid #27ae60; }}
        .fail {{ border-left: 4px solid #e74c3c; }}
        .status {{ font-weight: bold; font-size: 1.2em; }}
        .status.pass {{ color: #27ae60; }}
        .status.fail {{ color: #e74c3c; }}
        .description {{ color: #7f8c8d; font-style: italic; margin: 10px 0; }}
        .explanation {{ background: #ecf0f1; padding: 15px; border-radius: 4px; margin: 15px 0; }}
        .violations {{ background: #fdedec; padding: 15px; border-radius: 4px; margin: 15px 0; }}
        .violations h4 {{ color: #c0392b; margin-top: 0; }}
        .graph {{ margin: 20px 0; padding: 20px; background: #fff; border: 1px solid #ddd; border-radius: 4px; }}
        .vertex {{ fill: #3498db; stroke: white; stroke-width: 2; }}
        .vertex.spec {{ fill: #27ae60; }}
        .vertex.guidance {{ fill: #f39c12; }}
        .vertex.signer {{ fill: #9b59b6; }}
        .edge {{ stroke: #95a5a6; stroke-width: 2; }}
        .edge.verification {{ stroke: #3498db; }}
        .edge.validation {{ stroke: #e74c3c; }}
        .edge.coupling {{ stroke: #9b59b6; stroke-dasharray: 5,5; }}
        .edge.invalid {{ stroke: #e74c3c; stroke-width: 3; }}
        .label {{ font-size: 12px; fill: #2c3e50; }}
        code {{ background: #ecf0f1; padding: 2px 6px; border-radius: 3px; font-family: 'Fira Code', monospace; }}
        .summary {{ background: #d5dbdb; padding: 20px; border-radius: 8px; margin-bottom: 30px; }}
    </style>
</head>
<body>
    <h1>Ontology Rule Demonstration: {rule_category}</h1>

    <div class="summary">
        <strong>Summary:</strong> {sum(1 for r in results if r['passed'])}/{len(results)} demonstrations passed
    </div>
"""

    for i, result in enumerate(results, 1):
        status_class = "pass" if result['passed'] else "fail"
        status_text = "✓ PASS" if result['passed'] else "✗ FAIL"

        html += f"""
    <div class="demo {status_class}">
        <h2>Demo {i}: {result['name']}</h2>
        <p class="status {status_class}">{status_text}</p>
        <p class="description">{result['description']}</p>

        <div class="graph">
            {generate_svg_graph(result['cache'])}
        </div>

        <div class="explanation">
            <strong>Rule:</strong> {result['explanation']}
        </div>

        <p>
            <strong>Expected violations:</strong> {result['expected_violations']}<br>
            <strong>Actual violations:</strong> {result['actual_violations']}
        </p>
"""

        if result['violation_messages']:
            html += """
        <div class="violations">
            <h4>Violations Found:</h4>
            <ul>
"""
            for msg in result['violation_messages']:
                html += f"                <li><code>{msg}</code></li>\n"
            html += """
            </ul>
        </div>
"""

        html += "    </div>\n"

    html += """
</body>
</html>
"""

    output_path.write_text(html)
    print(f"Generated: {output_path}")


def generate_svg_graph(cache: Dict[str, Any]) -> str:
    """Generate an SVG visualization of the graph."""
    vertices = cache['elements']['vertices']
    edges = cache['elements']['edges']

    # Simple layout - arrange vertices in a circle or line
    n = len(vertices)
    if n == 0:
        return "<p>No vertices</p>"

    # Calculate positions
    positions = {}
    if n <= 2:
        # Horizontal line
        for i, vid in enumerate(vertices.keys()):
            positions[vid] = (100 + i * 200, 100)
    else:
        # Triangle or circle
        import math
        for i, vid in enumerate(vertices.keys()):
            angle = (2 * math.pi * i / n) - math.pi / 2
            x = 200 + 100 * math.cos(angle)
            y = 150 + 100 * math.sin(angle)
            positions[vid] = (x, y)

    svg_parts = ['<svg width="400" height="300" viewBox="0 0 400 300">']

    # Draw edges
    for eid, edge in edges.items():
        source = edge['source']
        target = edge['target']
        if source in positions and target in positions:
            x1, y1 = positions[source]
            x2, y2 = positions[target]

            # Determine edge class
            edge_type = edge.get('type', '')
            edge_class = 'edge'
            if 'verification' in edge_type:
                edge_class += ' verification'
            elif 'validation' in edge_type:
                edge_class += ' validation'
            elif 'coupling' in edge_type:
                edge_class += ' coupling'

            # Add arrow marker for directed edges
            if edge.get('orientation', 'directed') == 'directed':
                # Calculate arrow direction
                dx, dy = x2 - x1, y2 - y1
                length = (dx**2 + dy**2)**0.5
                if length > 0:
                    ux, uy = dx/length, dy/length
                    # Shorten line to make room for arrowhead
                    x2 -= ux * 15
                    y2 -= uy * 15
                    # Draw arrowhead
                    ax1 = x2 - ux*10 - uy*5
                    ay1 = y2 - uy*10 + ux*5
                    ax2 = x2 - ux*10 + uy*5
                    ay2 = y2 - uy*10 - ux*5
                    svg_parts.append(f'<polygon points="{x2},{y2} {ax1},{ay1} {ax2},{ay2}" fill="#666"/>')

            svg_parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{edge_class}"/>')

            # Edge label
            mx, my = (x1+x2)/2, (y1+y2)/2 - 10
            edge_label = edge_type.replace('edge/', '')
            svg_parts.append(f'<text x="{mx}" y="{my}" class="label" text-anchor="middle" font-size="10">{edge_label}</text>')

    # Draw vertices
    for vid, vertex in vertices.items():
        if vid in positions:
            x, y = positions[vid]

            # Determine vertex class
            vtype = vertex.get('type', '')
            vertex_class = 'vertex'
            if 'spec' in vtype:
                vertex_class += ' spec'
            elif 'guidance' in vtype:
                vertex_class += ' guidance'
            elif 'signer' in vtype:
                vertex_class += ' signer'

            svg_parts.append(f'<circle cx="{x}" cy="{y}" r="20" class="{vertex_class}"/>')

            # Vertex label
            label = vtype.replace('vertex/', '')
            svg_parts.append(f'<text x="{x}" y="{y+5}" class="label" text-anchor="middle">{label}</text>')

    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def main():
    """Run all demonstrations and generate reports."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Run edge endpoint demos
    print("\n=== Edge Endpoint Type Rules ===")
    edge_results = [run_demo(demo) for demo in EDGE_ENDPOINT_DEMOS]
    print(generate_text_report(edge_results, "Edge Endpoint Types"))
    generate_html_report(edge_results, "Edge Endpoint Types", OUTPUT_DIR / "rule_edge_endpoints.html")

    # Run vertex degree demos
    print("\n=== Vertex Degree Rules ===")
    degree_results = [run_demo(demo) for demo in VERTEX_DEGREE_DEMOS]
    print(generate_text_report(degree_results, "Vertex Degree Constraints"))
    generate_html_report(degree_results, "Vertex Degree Constraints", OUTPUT_DIR / "rule_vertex_degree.html")

    # Run face boundary demos
    print("\n=== Face Boundary Type Rules ===")
    face_results = [run_demo(demo) for demo in FACE_BOUNDARY_DEMOS]
    print(generate_text_report(face_results, "Face Boundary Types"))
    generate_html_report(face_results, "Face Boundary Types", OUTPUT_DIR / "rule_face_boundary_types.html")

    # Generate summary
    all_results = edge_results + degree_results + face_results
    total_passed = sum(1 for r in all_results if r['passed'])

    summary_html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Ontology Rules Summary</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; background: #f5f5f5; }}
        h1 {{ color: #2c3e50; }}
        .card {{ background: white; padding: 20px; margin: 20px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .pass {{ color: #27ae60; }}
        .fail {{ color: #e74c3c; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #3498db; color: white; }}
    </style>
</head>
<body>
    <h1>Ontology Rules Demonstration Summary</h1>

    <div class="card">
        <h2>Overall Results: <span class="{'pass' if total_passed == len(all_results) else 'fail'}">{total_passed}/{len(all_results)} passed</span></h2>
    </div>

    <div class="card">
        <h2>Rule Categories</h2>
        <table>
            <tr>
                <th>Category</th>
                <th>Demos</th>
                <th>Passed</th>
                <th>Link</th>
            </tr>
            <tr>
                <td>Edge Endpoint Types</td>
                <td>{len(edge_results)}</td>
                <td class="{'pass' if all(r['passed'] for r in edge_results) else 'fail'}">{sum(1 for r in edge_results if r['passed'])}/{len(edge_results)}</td>
                <td><a href="rule_edge_endpoints.html">View Details</a></td>
            </tr>
            <tr>
                <td>Vertex Degree Constraints</td>
                <td>{len(degree_results)}</td>
                <td class="{'pass' if all(r['passed'] for r in degree_results) else 'fail'}">{sum(1 for r in degree_results if r['passed'])}/{len(degree_results)}</td>
                <td><a href="rule_vertex_degree.html">View Details</a></td>
            </tr>
            <tr>
                <td>Face Boundary Types</td>
                <td>{len(face_results)}</td>
                <td class="{'pass' if all(r['passed'] for r in face_results) else 'fail'}">{sum(1 for r in face_results if r['passed'])}/{len(face_results)}</td>
                <td><a href="rule_face_boundary_types.html">View Details</a></td>
            </tr>
        </table>
    </div>

    <div class="card">
        <h2>Rule Summary</h2>
        <h3>Edge Endpoint Type Rules</h3>
        <p>These rules ensure edges connect the correct types of vertices:</p>
        <ul>
            <li><strong>verification:</strong> doc → spec (machine-checkable structural compliance)</li>
            <li><strong>validation:</strong> doc → guidance (human assessment of fitness for purpose)</li>
            <li><strong>coupling:</strong> spec ↔ guidance (1:1 pairing of spec with its guidance)</li>
            <li><strong>signs:</strong> signer → doc (human accountability for validation)</li>
            <li><strong>qualifies:</strong> signer → guidance/module (human qualified to validate)</li>
        </ul>

        <h3>Vertex Degree Constraints</h3>
        <p>These rules constrain how many edges of each type can connect to a vertex:</p>
        <ul>
            <li><strong>doc → verification:</strong> 0..1 (at most one verification per document)</li>
            <li><strong>spec ↔ coupling:</strong> exactly 1 (each spec pairs with exactly one guidance)</li>
            <li><strong>guidance ↔ coupling:</strong> exactly 1 (each guidance pairs with exactly one spec)</li>
        </ul>

        <h3>Face Boundary Type Rules</h3>
        <p>These rules ensure faces have the correct edge types in their boundary:</p>
        <ul>
            <li><strong>assurance:</strong> must have verification + validation + coupling edges</li>
            <li><strong>signature:</strong> must have validation + qualifies + signs edges</li>
        </ul>
    </div>
</body>
</html>
"""

    (OUTPUT_DIR / "rule_summary.html").write_text(summary_html)
    print(f"\nGenerated: {OUTPUT_DIR / 'rule_summary.html'}")

    print(f"\n{'='*70}")
    print(f"TOTAL: {total_passed}/{len(all_results)} demonstrations passed")
    print(f"{'='*70}")
    print(f"\nOpen {OUTPUT_DIR / 'rule_summary.html'} in a browser to view all demonstrations.")


if __name__ == '__main__':
    main()
