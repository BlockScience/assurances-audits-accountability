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
    RuleDemo(
        name="Valid Inherits Edge",
        description="spec → spec (CORRECT - type hierarchy)",
        cache={
            'elements': {
                'vertices': {
                    'v:spec:parent': {'id': 'v:spec:parent', 'type': 'vertex/spec', 'name': 'Parent Spec'},
                    'v:spec:child': {'id': 'v:spec:child', 'type': 'vertex/spec', 'name': 'Child Spec'},
                },
                'edges': {
                    'e:inherits:test': {
                        'id': 'e:inherits:test',
                        'type': 'edge/inherits',
                        'source': 'v:spec:child',
                        'target': 'v:spec:parent',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="edge_endpoint",
        explanation="Inherits edges connect a child spec to its parent spec, establishing type hierarchy."
    ),
    RuleDemo(
        name="Invalid Inherits Edge - Wrong Target",
        description="spec → guidance (WRONG: target should be spec)",
        cache={
            'elements': {
                'vertices': {
                    'v:spec:child': {'id': 'v:spec:child', 'type': 'vertex/spec', 'name': 'Child Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:inherits:bad': {
                        'id': 'e:inherits:bad',
                        'type': 'edge/inherits',
                        'source': 'v:spec:child',
                        'target': 'v:guidance:test',  # WRONG! Should be vertex/spec
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=1,
        rule_type="edge_endpoint",
        explanation="Inherits edges must connect specs to other specs - a spec cannot inherit from guidance."
    ),
    RuleDemo(
        name="Valid Instantiates Edge",
        description="doc → spec (CORRECT - type instantiation)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:persona:test': {'id': 'v:doc:persona:test', 'type': 'vertex/doc/persona', 'name': 'Test Persona'},
                    'v:spec:persona': {'id': 'v:spec:persona', 'type': 'vertex/spec', 'name': 'Persona Spec'},
                },
                'edges': {
                    'e:instantiates:test': {
                        'id': 'e:instantiates:test',
                        'type': 'edge/instantiates',
                        'source': 'v:doc:persona:test',
                        'target': 'v:spec:persona',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
        },
        expected_violations=0,
        rule_type="edge_endpoint",
        explanation="Instantiates edges connect a document to the spec that defines its type."
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
        explanation="A document with a single verification edge. Spec is properly coupled to guidance."
    ),
    RuleDemo(
        name="Valid: Doc with Multiple Type Verifications",
        description="Doc → Spec1 ↔ G1, Doc → Spec2 ↔ G2 (VALID: doc has multiple types)",
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
        expected_violations=0,
        rule_type="degree",
        explanation="Documents can have one verification edge PER TYPE they inherit. A persona doc inherits from both 'persona' and 'doc', so it can verify against spec/persona AND spec/doc (one verification per inherited type)."
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


# ============================================================
# FACE ADJACENCY RULES (Assurance Requires Signature)
# ============================================================

FACE_ADJACENCY_DEMOS = [
    RuleDemo(
        name="Valid: Assurance Face Has Signature Sharing Validation Edge",
        description="Assurance face has corresponding signature face sharing validation edge",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                },
                'edges': {
                    # Assurance edges
                    'e:verification:test': {
                        'id': 'e:verification:test',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:validation:test': {  # SHARED EDGE
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
                    # Signature edges
                    'e:qualifies:alice': {
                        'id': 'e:qualifies:alice',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:signs:alice': {
                        'id': 'e:signs:alice',
                        'type': 'edge/signs',
                        'source': 'v:signer:alice',
                        'target': 'v:doc:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:assurance:test': {
                        'id': 'f:assurance:test',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:test', 'e:validation:test', 'e:coupling:test'],
                        'orientation': 'oriented',
                        'validation_edge': 'e:validation:test',
                    },
                    'f:signature:test': {
                        'id': 'f:signature:test',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        # SHARES e:validation:test with assurance face
                        'edges': ['e:validation:test', 'e:qualifies:alice', 'e:signs:alice'],
                        'orientation': 'oriented',
                        'signer': 'v:signer:alice',
                        'guidance': 'v:guidance:test',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="face_adjacency",
        explanation="Assurance face has a signature face sharing the same validation edge - human accountability is established."
    ),
    RuleDemo(
        name="Valid: Signature Face Without Assurance (Pre-existing Approval)",
        description="Signature face exists alone - this is VALID (approvals can pre-exist assurance)",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                },
                'edges': {
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:qualifies:alice': {
                        'id': 'e:qualifies:alice',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:signs:alice': {
                        'id': 'e:signs:alice',
                        'type': 'edge/signs',
                        'source': 'v:signer:alice',
                        'target': 'v:doc:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    # Signature face alone - this is VALID!
                    'f:signature:standalone': {
                        'id': 'f:signature:standalone',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        'edges': ['e:validation:test', 'e:qualifies:alice', 'e:signs:alice'],
                        'orientation': 'oriented',
                        'signer': 'v:signer:alice',
                        'guidance': 'v:guidance:test',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="face_adjacency",
        explanation="Signature faces CAN exist without assurance faces. They represent a signer's approval of a validation, which may pre-exist the assurance."
    ),
    RuleDemo(
        name="Invalid: Assurance Face Without Signature (No Human Sign-off)",
        description="Assurance face exists alone without any signature - NOT allowed!",
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
                    # Assurance face alone - NO signature! This is INVALID
                    'f:assurance:orphan': {
                        'id': 'f:assurance:orphan',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:test', 'e:validation:test', 'e:coupling:test'],
                        'orientation': 'oriented',
                        'validation_edge': 'e:validation:test',
                    },
                },
            },
        },
        expected_violations=1,
        rule_type="face_adjacency",
        explanation="VIOLATION: Assurance face exists without a corresponding signature face. Every assurance requires human accountability via a signed validation."
    ),
]


# ============================================================
# AUTHORIZATION CHAIN DEMOS (authorization → signature → assurance)
# ============================================================

AUTHORIZATION_CHAIN_DEMOS = [
    RuleDemo(
        name="Valid: Authorization Face Alone (Role Assignment Pre-exists Signing)",
        description="Authorization face exists alone - this is VALID (role assignments can pre-exist signing activity)",
        cache={
            'elements': {
                'vertices': {
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                    'v:role:reviewer': {'id': 'v:role:reviewer', 'type': 'vertex/role', 'name': 'Reviewer'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:has-role:alice-reviewer': {
                        'id': 'e:has-role:alice-reviewer',
                        'type': 'edge/has-role',
                        'source': 'v:signer:alice',
                        'target': 'v:role:reviewer',
                        'orientation': 'directed',
                    },
                    'e:conveys:reviewer-guidance': {
                        'id': 'e:conveys:reviewer-guidance',
                        'type': 'edge/conveys',
                        'source': 'v:role:reviewer',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:qualifies:alice-guidance': {
                        'id': 'e:qualifies:alice-guidance',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:authorization:alice-reviewer': {
                        'id': 'f:authorization:alice-reviewer',
                        'type': 'face/authorization',
                        'vertices': ['v:signer:alice', 'v:role:reviewer', 'v:guidance:test'],
                        'edges': ['e:has-role:alice-reviewer', 'e:conveys:reviewer-guidance', 'e:qualifies:alice-guidance'],
                        'orientation': 'oriented',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="authorization_chain",
        explanation="Authorization faces CAN exist without signature faces. They represent role-based authority that pre-exists any signing activity."
    ),
    RuleDemo(
        name="Valid: Authorization + Signature (Role Backs Signing Authority)",
        description="Authorization face with signature face sharing qualifies edge - signer has role-based authority",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                    'v:role:reviewer': {'id': 'v:role:reviewer', 'type': 'vertex/role', 'name': 'Reviewer'},
                },
                'edges': {
                    # Authorization edges
                    'e:has-role:alice-reviewer': {
                        'id': 'e:has-role:alice-reviewer',
                        'type': 'edge/has-role',
                        'source': 'v:signer:alice',
                        'target': 'v:role:reviewer',
                        'orientation': 'directed',
                    },
                    'e:conveys:reviewer-guidance': {
                        'id': 'e:conveys:reviewer-guidance',
                        'type': 'edge/conveys',
                        'source': 'v:role:reviewer',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    # SHARED qualifies edge
                    'e:qualifies:alice-guidance': {
                        'id': 'e:qualifies:alice-guidance',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    # Signature edges
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:signs:alice-doc': {
                        'id': 'e:signs:alice-doc',
                        'type': 'edge/signs',
                        'source': 'v:signer:alice',
                        'target': 'v:doc:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:authorization:alice-reviewer': {
                        'id': 'f:authorization:alice-reviewer',
                        'type': 'face/authorization',
                        'vertices': ['v:signer:alice', 'v:role:reviewer', 'v:guidance:test'],
                        # INCLUDES the shared qualifies edge
                        'edges': ['e:has-role:alice-reviewer', 'e:conveys:reviewer-guidance', 'e:qualifies:alice-guidance'],
                        'orientation': 'oriented',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                    'f:signature:test': {
                        'id': 'f:signature:test',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        # SHARES qualifies edge with authorization face
                        'edges': ['e:validation:test', 'e:qualifies:alice-guidance', 'e:signs:alice-doc'],
                        'orientation': 'oriented',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="authorization_chain",
        explanation="Authorization face shares qualifies edge with signature face. The signer's authority to sign comes from their role."
    ),
    RuleDemo(
        name="Valid: Complete Chain - Authorization → Signature → Assurance",
        description="Full chain with all three faces sharing appropriate edges",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                    'v:role:reviewer': {'id': 'v:role:reviewer', 'type': 'vertex/role', 'name': 'Reviewer'},
                },
                'edges': {
                    # Authorization edges
                    'e:has-role:alice-reviewer': {
                        'id': 'e:has-role:alice-reviewer',
                        'type': 'edge/has-role',
                        'source': 'v:signer:alice',
                        'target': 'v:role:reviewer',
                        'orientation': 'directed',
                    },
                    'e:conveys:reviewer-guidance': {
                        'id': 'e:conveys:reviewer-guidance',
                        'type': 'edge/conveys',
                        'source': 'v:role:reviewer',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    # SHARED qualifies edge (authorization ↔ signature)
                    'e:qualifies:alice-guidance': {
                        'id': 'e:qualifies:alice-guidance',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    # Signature edges
                    'e:signs:alice-doc': {
                        'id': 'e:signs:alice-doc',
                        'type': 'edge/signs',
                        'source': 'v:signer:alice',
                        'target': 'v:doc:test',
                        'orientation': 'directed',
                    },
                    # SHARED validation edge (signature ↔ assurance)
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    # Assurance edges
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
                'faces': {
                    'f:authorization:alice-reviewer': {
                        'id': 'f:authorization:alice-reviewer',
                        'type': 'face/authorization',
                        'vertices': ['v:signer:alice', 'v:role:reviewer', 'v:guidance:test'],
                        'edges': ['e:has-role:alice-reviewer', 'e:conveys:reviewer-guidance', 'e:qualifies:alice-guidance'],
                        'orientation': 'oriented',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                    'f:signature:test': {
                        'id': 'f:signature:test',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        # SHARES qualifies with authorization, validation with assurance
                        'edges': ['e:validation:test', 'e:qualifies:alice-guidance', 'e:signs:alice-doc'],
                        'orientation': 'oriented',
                        'validation_edge': 'e:validation:test',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                    'f:assurance:test': {
                        'id': 'f:assurance:test',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        # SHARES validation with signature
                        'edges': ['e:verification:test', 'e:validation:test', 'e:coupling:test'],
                        'orientation': 'oriented',
                        'validation_edge': 'e:validation:test',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="authorization_chain",
        explanation="Complete chain: authorization → signature → assurance. The signer's role gives authority (authorization), which backs their signature, which backs the assurance."
    ),
    RuleDemo(
        name="Invalid: Signature Without Authorization (No Role-Based Authority)",
        description="Signature face exists but has no authorization face sharing qualifies edge - NOT allowed!",
        cache={
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                },
                'edges': {
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:qualifies:alice-guidance': {
                        'id': 'e:qualifies:alice-guidance',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:signs:alice-doc': {
                        'id': 'e:signs:alice-doc',
                        'type': 'edge/signs',
                        'source': 'v:signer:alice',
                        'target': 'v:doc:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    # Signature face WITHOUT corresponding authorization face
                    'f:signature:orphan': {
                        'id': 'f:signature:orphan',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        'edges': ['e:validation:test', 'e:qualifies:alice-guidance', 'e:signs:alice-doc'],
                        'orientation': 'oriented',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                },
            },
        },
        expected_violations=1,
        rule_type="authorization_chain",
        explanation="VIOLATION: Signature face exists without a corresponding authorization face sharing the qualifies edge. You can't sign without role-based authority."
    ),
    RuleDemo(
        name="Invalid: Authorization Missing Conveys Edge",
        description="Authorization face missing conveys edge - required edge type missing",
        cache={
            'elements': {
                'vertices': {
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer', 'name': 'Alice'},
                    'v:role:reviewer': {'id': 'v:role:reviewer', 'type': 'vertex/role', 'name': 'Reviewer'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:has-role:alice-reviewer': {
                        'id': 'e:has-role:alice-reviewer',
                        'type': 'edge/has-role',
                        'source': 'v:signer:alice',
                        'target': 'v:role:reviewer',
                        'orientation': 'directed',
                    },
                    # Missing conveys edge! Using 'other' instead
                    'e:other:placeholder': {
                        'id': 'e:other:placeholder',
                        'type': 'edge/other',
                        'source': 'v:role:reviewer',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:qualifies:alice-guidance': {
                        'id': 'e:qualifies:alice-guidance',
                        'type': 'edge/qualifies',
                        'source': 'v:signer:alice',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:authorization:bad': {
                        'id': 'f:authorization:bad',
                        'type': 'face/authorization',
                        'vertices': ['v:signer:alice', 'v:role:reviewer', 'v:guidance:test'],
                        # Missing conveys, has 'other' instead
                        'edges': ['e:has-role:alice-reviewer', 'e:other:placeholder', 'e:qualifies:alice-guidance'],
                        'orientation': 'oriented',
                    },
                },
            },
        },
        expected_violations=1,
        rule_type="authorization_chain",
        explanation="VIOLATION: Authorization face is missing the 'conveys' edge. It must have has-role, conveys, and qualifies edges."
    ),
]


# ============================================================
# ROLE ASSIGNMENT CHAIN DEMOS (ARBAC97: role-assignment → assignment-signature)
# ============================================================

ROLE_ASSIGNMENT_DEMOS = [
    RuleDemo(
        name="Valid: Role-Assignment Face (Admin Can Assign Target Role)",
        description="Role-assignment face with has-role, conveys, can-assign edges - admin has authority to assign a role",
        cache={
            'elements': {
                'vertices': {
                    'v:actor:admin': {'id': 'v:actor:admin', 'type': 'vertex/actor', 'name': 'Admin User'},
                    'v:role:admin-role': {'id': 'v:role:admin-role', 'type': 'vertex/role', 'name': 'Admin Role'},
                    'v:role:target-role': {'id': 'v:role:target-role', 'type': 'vertex/role', 'name': 'Target Role'},
                },
                'edges': {
                    'e:has-role:admin': {
                        'id': 'e:has-role:admin',
                        'type': 'edge/has-role',
                        'source': 'v:actor:admin',
                        'target': 'v:role:admin-role',
                        'orientation': 'directed',
                    },
                    'e:conveys:admin-to-target': {
                        'id': 'e:conveys:admin-to-target',
                        'type': 'edge/conveys',
                        'source': 'v:role:admin-role',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                    'e:can-assign:admin-target': {
                        'id': 'e:can-assign:admin-target',
                        'type': 'edge/can-assign',
                        'source': 'v:actor:admin',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:role-assignment:admin-target': {
                        'id': 'f:role-assignment:admin-target',
                        'type': 'face/role-assignment',
                        'vertices': ['v:actor:admin', 'v:role:admin-role', 'v:role:target-role'],
                        'edges': ['e:has-role:admin', 'e:conveys:admin-to-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                        'can_assign_edge': 'e:can-assign:admin-target',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="role_assignment_chain",
        explanation="Role-assignment face proves that admin-role conveys authority to assign target-role. The admin holds admin-role (has-role), which conveys assignment authority (conveys → role), giving the admin can-assign authority."
    ),
    RuleDemo(
        name="Valid: Role-Assignment + Assignment-Signature (Complete Chain)",
        description="Role-assignment face with assignment-signature sharing can-assign edge",
        cache={
            'elements': {
                'vertices': {
                    'v:signer:admin': {'id': 'v:signer:admin', 'type': 'vertex/signer', 'name': 'Admin Signer'},
                    'v:role:admin-role': {'id': 'v:role:admin-role', 'type': 'vertex/role', 'name': 'Admin Role'},
                    'v:role:target-role': {'id': 'v:role:target-role', 'type': 'vertex/role', 'name': 'Target Role'},
                    'v:actor:bob': {'id': 'v:actor:bob', 'type': 'vertex/actor', 'name': 'Bob'},
                },
                'edges': {
                    # Role-assignment edges
                    'e:has-role:admin': {
                        'id': 'e:has-role:admin',
                        'type': 'edge/has-role',
                        'source': 'v:signer:admin',
                        'target': 'v:role:admin-role',
                        'orientation': 'directed',
                    },
                    'e:conveys:admin-to-target': {
                        'id': 'e:conveys:admin-to-target',
                        'type': 'edge/conveys',
                        'source': 'v:role:admin-role',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                    # SHARED can-assign edge (role-assignment ↔ assignment-signature)
                    'e:can-assign:admin-target': {
                        'id': 'e:can-assign:admin-target',
                        'type': 'edge/can-assign',
                        'source': 'v:signer:admin',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                    # Assignment-signature edges
                    'e:signs-assignment:admin-bob': {
                        'id': 'e:signs-assignment:admin-bob',
                        'type': 'edge/signs-assignment',
                        'source': 'v:signer:admin',
                        'target': 'v:actor:bob',
                        'orientation': 'directed',
                    },
                    'e:has-role:bob-target': {
                        'id': 'e:has-role:bob-target',
                        'type': 'edge/has-role',
                        'source': 'v:actor:bob',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:role-assignment:admin-target': {
                        'id': 'f:role-assignment:admin-target',
                        'type': 'face/role-assignment',
                        'vertices': ['v:signer:admin', 'v:role:admin-role', 'v:role:target-role'],
                        'edges': ['e:has-role:admin', 'e:conveys:admin-to-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                        'can_assign_edge': 'e:can-assign:admin-target',
                    },
                    'f:assignment-signature:bob': {
                        'id': 'f:assignment-signature:bob',
                        'type': 'face/assignment-signature',
                        'vertices': ['v:signer:admin', 'v:actor:bob', 'v:role:target-role'],
                        # SHARES can-assign edge with role-assignment face
                        'edges': ['e:signs-assignment:admin-bob', 'e:has-role:bob-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                        'can_assign_edge': 'e:can-assign:admin-target',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="role_assignment_chain",
        explanation="Complete ARBAC97 chain: role-assignment → assignment-signature. The admin's role gives can-assign authority (role-assignment), which backs their signature on Bob's role assignment (assignment-signature)."
    ),
    RuleDemo(
        name="Invalid: Assignment-Signature Without Role-Assignment",
        description="Assignment-signature face exists without role-assignment face sharing can-assign edge - NOT allowed!",
        cache={
            'elements': {
                'vertices': {
                    'v:signer:admin': {'id': 'v:signer:admin', 'type': 'vertex/signer', 'name': 'Admin Signer'},
                    'v:actor:bob': {'id': 'v:actor:bob', 'type': 'vertex/actor', 'name': 'Bob'},
                    'v:role:target-role': {'id': 'v:role:target-role', 'type': 'vertex/role', 'name': 'Target Role'},
                },
                'edges': {
                    'e:signs-assignment:admin-bob': {
                        'id': 'e:signs-assignment:admin-bob',
                        'type': 'edge/signs-assignment',
                        'source': 'v:signer:admin',
                        'target': 'v:actor:bob',
                        'orientation': 'directed',
                    },
                    'e:has-role:bob-target': {
                        'id': 'e:has-role:bob-target',
                        'type': 'edge/has-role',
                        'source': 'v:actor:bob',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                    'e:can-assign:admin-target': {
                        'id': 'e:can-assign:admin-target',
                        'type': 'edge/can-assign',
                        'source': 'v:signer:admin',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    # Assignment-signature WITHOUT corresponding role-assignment face
                    'f:assignment-signature:orphan': {
                        'id': 'f:assignment-signature:orphan',
                        'type': 'face/assignment-signature',
                        'vertices': ['v:signer:admin', 'v:actor:bob', 'v:role:target-role'],
                        'edges': ['e:signs-assignment:admin-bob', 'e:has-role:bob-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                        'can_assign_edge': 'e:can-assign:admin-target',
                    },
                },
            },
        },
        expected_violations=1,
        rule_type="role_assignment_chain",
        explanation="VIOLATION: Assignment-signature face exists without a corresponding role-assignment face sharing the can-assign edge. You can't sign a role assignment without role-based authority."
    ),
    RuleDemo(
        name="Invalid: Role-Assignment Missing Conveys Edge",
        description="Role-assignment face missing conveys edge - required edge type missing",
        cache={
            'elements': {
                'vertices': {
                    'v:actor:admin': {'id': 'v:actor:admin', 'type': 'vertex/actor', 'name': 'Admin User'},
                    'v:role:admin-role': {'id': 'v:role:admin-role', 'type': 'vertex/role', 'name': 'Admin Role'},
                    'v:role:target-role': {'id': 'v:role:target-role', 'type': 'vertex/role', 'name': 'Target Role'},
                },
                'edges': {
                    'e:has-role:admin': {
                        'id': 'e:has-role:admin',
                        'type': 'edge/has-role',
                        'source': 'v:actor:admin',
                        'target': 'v:role:admin-role',
                        'orientation': 'directed',
                    },
                    # Missing conveys edge! Using 'other' instead
                    'e:other:placeholder': {
                        'id': 'e:other:placeholder',
                        'type': 'edge/other',
                        'source': 'v:role:admin-role',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                    'e:can-assign:admin-target': {
                        'id': 'e:can-assign:admin-target',
                        'type': 'edge/can-assign',
                        'source': 'v:actor:admin',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    'f:role-assignment:bad': {
                        'id': 'f:role-assignment:bad',
                        'type': 'face/role-assignment',
                        'vertices': ['v:actor:admin', 'v:role:admin-role', 'v:role:target-role'],
                        # Missing conveys, has 'other' instead
                        'edges': ['e:has-role:admin', 'e:other:placeholder', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                    },
                },
            },
        },
        expected_violations=1,
        rule_type="role_assignment_chain",
        explanation="VIOLATION: Role-assignment face is missing the 'conveys' edge. It must have has-role, conveys, and can-assign edges."
    ),
    RuleDemo(
        name="Valid: Role-Assignment Alone (Authority Pre-exists Assignment)",
        description="Role-assignment face exists alone - VALID (authority can pre-exist actual assignment)",
        cache={
            'elements': {
                'vertices': {
                    'v:actor:admin': {'id': 'v:actor:admin', 'type': 'vertex/actor', 'name': 'Admin User'},
                    'v:role:admin-role': {'id': 'v:role:admin-role', 'type': 'vertex/role', 'name': 'Admin Role'},
                    'v:role:target-role': {'id': 'v:role:target-role', 'type': 'vertex/role', 'name': 'Target Role'},
                },
                'edges': {
                    'e:has-role:admin': {
                        'id': 'e:has-role:admin',
                        'type': 'edge/has-role',
                        'source': 'v:actor:admin',
                        'target': 'v:role:admin-role',
                        'orientation': 'directed',
                    },
                    'e:conveys:admin-to-target': {
                        'id': 'e:conveys:admin-to-target',
                        'type': 'edge/conveys',
                        'source': 'v:role:admin-role',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                    'e:can-assign:admin-target': {
                        'id': 'e:can-assign:admin-target',
                        'type': 'edge/can-assign',
                        'source': 'v:actor:admin',
                        'target': 'v:role:target-role',
                        'orientation': 'directed',
                    },
                },
                'faces': {
                    # Role-assignment face alone - this is VALID!
                    'f:role-assignment:standalone': {
                        'id': 'f:role-assignment:standalone',
                        'type': 'face/role-assignment',
                        'vertices': ['v:actor:admin', 'v:role:admin-role', 'v:role:target-role'],
                        'edges': ['e:has-role:admin', 'e:conveys:admin-to-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                        'can_assign_edge': 'e:can-assign:admin-target',
                    },
                },
            },
        },
        expected_violations=0,
        rule_type="role_assignment_chain",
        explanation="Role-assignment faces CAN exist without assignment-signature faces. They represent can-assign authority that pre-exists any actual role assignment signatures."
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
    elif demo.rule_type == "face_adjacency":
        # Face adjacency rule: signature face must share validation edge with assurance face
        # This is a critical accountability rule - signature faces are created when users
        # approve validation edges, often pre-existing assurance faces
        engine._check_signature_shares_edge_with_assurance()
    elif demo.rule_type == "authorization_chain":
        # Authorization chain rules: authorization → signature → assurance
        # This checks both authorization boundary types and signature-requires-authorization
        engine._check_authorization_boundary_types()
        engine._check_signature_requires_authorization()
    elif demo.rule_type == "role_assignment_chain":
        # Role assignment chain rules (ARBAC97): role-assignment → assignment-signature
        # This checks role-assignment boundary types and assignment-signature-requires-role-assignment
        engine._check_role_assignment_boundary_types()
        engine._check_assignment_signature_boundary_types()
        engine._check_assignment_signature_requires_role_assignment()

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

    # Run face adjacency demos (signature-assurance coupling)
    print("\n=== Face Adjacency Rules (Signature-Assurance) ===")
    adjacency_results = [run_demo(demo) for demo in FACE_ADJACENCY_DEMOS]
    print(generate_text_report(adjacency_results, "Face Adjacency (Signature-Assurance)"))
    generate_html_report(adjacency_results, "Face Adjacency (Signature-Assurance)", OUTPUT_DIR / "rule_face_adjacency.html")

    # Run authorization chain demos (authorization → signature → assurance)
    print("\n=== Authorization Chain Rules ===")
    auth_results = [run_demo(demo) for demo in AUTHORIZATION_CHAIN_DEMOS]
    print(generate_text_report(auth_results, "Authorization Chain (authorization → signature → assurance)"))
    generate_html_report(auth_results, "Authorization Chain (authorization → signature → assurance)", OUTPUT_DIR / "rule_authorization_chain.html")

    # Run role assignment chain demos (ARBAC97: role-assignment → assignment-signature)
    print("\n=== Role Assignment Chain Rules (ARBAC97) ===")
    role_assign_results = [run_demo(demo) for demo in ROLE_ASSIGNMENT_DEMOS]
    print(generate_text_report(role_assign_results, "Role Assignment Chain (ARBAC97: role-assignment → assignment-signature)"))
    generate_html_report(role_assign_results, "Role Assignment Chain (ARBAC97: role-assignment → assignment-signature)", OUTPUT_DIR / "rule_role_assignment.html")

    # Generate summary
    all_results = edge_results + degree_results + face_results + adjacency_results + auth_results + role_assign_results
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
            <tr>
                <td>Face Adjacency (Signature-Assurance)</td>
                <td>{len(adjacency_results)}</td>
                <td class="{'pass' if all(r['passed'] for r in adjacency_results) else 'fail'}">{sum(1 for r in adjacency_results if r['passed'])}/{len(adjacency_results)}</td>
                <td><a href="rule_face_adjacency.html">View Details</a></td>
            </tr>
            <tr>
                <td>Authorization Chain (authorization → signature → assurance)</td>
                <td>{len(auth_results)}</td>
                <td class="{'pass' if all(r['passed'] for r in auth_results) else 'fail'}">{sum(1 for r in auth_results if r['passed'])}/{len(auth_results)}</td>
                <td><a href="rule_authorization_chain.html">View Details</a></td>
            </tr>
            <tr>
                <td>Role Assignment Chain (ARBAC97: role-assignment → assignment-signature)</td>
                <td>{len(role_assign_results)}</td>
                <td class="{'pass' if all(r['passed'] for r in role_assign_results) else 'fail'}">{sum(1 for r in role_assign_results if r['passed'])}/{len(role_assign_results)}</td>
                <td><a href="rule_role_assignment.html">View Details</a></td>
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
            <li><strong>inherits:</strong> spec → spec (child spec extends parent spec)</li>
            <li><strong>instantiates:</strong> doc → spec (document is instance of spec type)</li>
        </ul>

        <h3>Vertex Degree Constraints</h3>
        <p>These rules constrain how many edges of each type can connect to a vertex:</p>
        <ul>
            <li><strong>doc → verification:</strong> 0..n where n = number of inherited types (one verification per type)</li>
            <li><strong>spec ↔ coupling:</strong> exactly 1 (each spec pairs with exactly one guidance)</li>
            <li><strong>guidance ↔ coupling:</strong> exactly 1 (each guidance pairs with exactly one spec)</li>
        </ul>

        <h3>Face Boundary Type Rules</h3>
        <p>These rules ensure faces have the correct edge types in their boundary:</p>
        <ul>
            <li><strong>assurance:</strong> must have verification + validation + coupling edges</li>
            <li><strong>signature:</strong> must have validation + qualifies + signs edges</li>
        </ul>

        <h3>Face Adjacency Rules (Assurance Requires Signature)</h3>
        <p>These rules ensure assurance faces have human accountability via signature faces:</p>
        <ul>
            <li><strong>assurance-requires-signature:</strong> assurance face (doc, spec, guidance) must have a signature face (doc, guidance, signer) sharing its validation edge</li>
            <li><strong>signature-can-pre-exist:</strong> signature faces CAN exist without assurance faces (they represent pre-existing approvals)</li>
        </ul>
        <p><em>Key insight: Signature faces are created when a user approves a validation edge. They often PRE-EXIST assurance faces. Assurance faces CANNOT exist without a corresponding signature.</em></p>

        <h3>Authorization Chain Rules (authorization → signature → assurance)</h3>
        <p>These rules establish the complete chain of accountability via role-based access control:</p>
        <ul>
            <li><strong>authorization:</strong> face with signer, role, guidance connected by has-role, conveys, qualifies edges</li>
            <li><strong>signature-requires-authorization:</strong> signature face must have authorization face sharing the qualifies edge</li>
            <li><strong>authorization-can-pre-exist:</strong> authorization faces CAN exist without signature faces (role assignments pre-exist signing)</li>
        </ul>
        <p><em>Key insight: The chain authorization → signature → assurance establishes complete accountability. A signer's authority comes from their role (authorization), which backs their signature, which backs the assurance.</em></p>

        <h3>Role Assignment Chain Rules (ARBAC97: role-assignment → assignment-signature)</h3>
        <p>These rules implement ARBAC97 administrative role-based access control for role assignment authority:</p>
        <ul>
            <li><strong>role-assignment:</strong> face with actor, admin-role, target-role connected by has-role, conveys, can-assign edges</li>
            <li><strong>assignment-signature:</strong> face with admin-signer, target-actor, target-role connected by signs-assignment, has-role, can-assign edges</li>
            <li><strong>assignment-signature-requires-role-assignment:</strong> assignment-signature face must have role-assignment face sharing the can-assign edge</li>
            <li><strong>role-assignment-can-pre-exist:</strong> role-assignment faces CAN exist without assignment-signature faces (authority pre-exists assignments)</li>
        </ul>
        <p><em>Key insight: This implements ARBAC97's can_assign relation. An admin's role conveys authority to assign other roles. The chain role-assignment → assignment-signature establishes who has authority to assign roles and tracks role assignments with human sign-off.</em></p>
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
