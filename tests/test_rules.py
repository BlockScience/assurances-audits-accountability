"""
Tests for ontology rule enforcement.

These tests verify that the OntologyRuleEngine correctly enforces
the local rules defined in the ontology. Rules are type constraints
layered on top of topological structure.

TOPOLOGY vs ONTOLOGY:
- Topology: Structural rules of simplicial complexes
- Ontology: Type system with local rules that add constraints

This module tests ontology verification (deterministic type checking).
"""

import pytest
from aaa.core.complex import (
    SimplicialComplex,
    ComplexGraph,
    build_simplicial_complex,
    TopologyViolation,
    check_edge_valid_boundary,
    check_face_valid_boundary,
    check_face_closure,
    check_topology,
)
from aaa.core.rules import (
    OntologyRuleEngine,
    OntologyRule,
    RuleViolation,
    RuleType,
    Severity,
    check_ontology_rules,
    # Local rule functions
    check_edge_endpoint_types,
    check_vertex_degree,
    check_face_boundary_types,
)


# ========== Fixtures ==========

@pytest.fixture
def empty_cache():
    """Empty knowledge complex cache."""
    return {
        'elements': {
            'vertices': {},
            'edges': {},
            'faces': {},
        },
        'statistics': {
            'vertices': 0,
            'edges': 0,
            'faces': 0,
        }
    }


@pytest.fixture
def minimal_assurance_cache():
    """Minimal valid assurance triangle."""
    return {
        'elements': {
            'vertices': {
                'v:doc:test': {
                    'id': 'v:doc:test',
                    'type': 'vertex/doc',
                    'name': 'Test Document',
                },
                'v:spec:test': {
                    'id': 'v:spec:test',
                    'type': 'vertex/spec',
                    'name': 'Test Spec',
                },
                'v:guidance:test': {
                    'id': 'v:guidance:test',
                    'type': 'vertex/guidance',
                    'name': 'Test Guidance',
                },
            },
            'edges': {
                'e:verification:doc-spec': {
                    'id': 'e:verification:doc-spec',
                    'type': 'edge/verification',
                    'source': 'v:doc:test',
                    'target': 'v:spec:test',
                    'orientation': 'directed',
                },
                'e:validation:doc-guidance': {
                    'id': 'e:validation:doc-guidance',
                    'type': 'edge/validation',
                    'source': 'v:doc:test',
                    'target': 'v:guidance:test',
                    'orientation': 'directed',
                },
                'e:coupling:spec-guidance': {
                    'id': 'e:coupling:spec-guidance',
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
                    'edges': ['e:verification:doc-spec', 'e:validation:doc-guidance', 'e:coupling:spec-guidance'],
                    'orientation': 'oriented',
                    'target': 'v:doc:test',
                    'spec': 'v:spec:test',
                    'guidance': 'v:guidance:test',
                },
            },
        },
        'statistics': {
            'vertices': 3,
            'edges': 3,
            'faces': 1,
        }
    }


# ========== Graph Module Tests ==========

class TestComplexGraph:
    """Tests for ComplexGraph construction and queries."""

    def test_from_cache_empty(self, empty_cache):
        """Test building graph from empty cache."""
        graph = ComplexGraph.from_cache(empty_cache)
        assert len(graph.vertices) == 0
        assert len(graph.edges) == 0
        assert len(graph.faces) == 0

    def test_from_cache_minimal(self, minimal_assurance_cache):
        """Test building graph from minimal cache."""
        graph = ComplexGraph.from_cache(minimal_assurance_cache)
        assert len(graph.vertices) == 3
        assert len(graph.edges) == 3
        assert len(graph.faces) == 1

    def test_get_vertex(self, minimal_assurance_cache):
        """Test vertex retrieval."""
        graph = ComplexGraph.from_cache(minimal_assurance_cache)
        vertex = graph.get_vertex('v:doc:test')
        assert vertex is not None
        assert vertex.type == 'vertex/doc'

    def test_get_edges_from(self, minimal_assurance_cache):
        """Test getting outgoing edges."""
        graph = ComplexGraph.from_cache(minimal_assurance_cache)
        edges = graph.get_edges_from('v:doc:test')
        assert len(edges) == 2  # verification and validation

    def test_get_edges_from_by_type(self, minimal_assurance_cache):
        """Test getting outgoing edges filtered by type."""
        graph = ComplexGraph.from_cache(minimal_assurance_cache)
        edges = graph.get_edges_from('v:doc:test', 'verification')
        assert len(edges) == 1

    def test_edge_exists(self, minimal_assurance_cache):
        """Test edge existence check."""
        graph = ComplexGraph.from_cache(minimal_assurance_cache)
        assert graph.edge_exists('v:doc:test', 'v:spec:test', 'verification')
        assert not graph.edge_exists('v:doc:test', 'v:spec:test', 'coupling')

    def test_degree(self, minimal_assurance_cache):
        """Test degree calculation."""
        graph = ComplexGraph.from_cache(minimal_assurance_cache)
        # Doc has 2 outgoing edges
        assert graph.out_degree('v:doc:test') == 2
        # Spec has 1 coupling edge (undirected, so counted in both directions)
        assert graph.degree('v:spec:test', 'coupling') == 1

    def test_faces_share_edge(self, minimal_assurance_cache):
        """Test finding shared edges between faces."""
        # Add a second face that shares an edge
        cache = minimal_assurance_cache.copy()
        cache['elements'] = minimal_assurance_cache['elements'].copy()
        cache['elements']['faces'] = minimal_assurance_cache['elements']['faces'].copy()

        # Add a b2 face sharing coupling edge
        cache['elements']['faces']['f:b2:test'] = {
            'id': 'f:b2:test',
            'type': 'face/b2',
            'vertices': ['v:spec:test', 'v:guidance:test', 'v:spec:meta'],
            'edges': ['e:coupling:spec-guidance', 'e:meta1', 'e:meta2'],
            'orientation': 'oriented',
        }

        graph = ComplexGraph.from_cache(cache)
        shared = graph.faces_share_edge('f:assurance:test', 'f:b2:test')
        assert 'e:coupling:spec-guidance' in shared


class TestGraphDagCheck:
    """Tests for DAG verification."""

    def test_dag_empty(self, empty_cache):
        """Empty graph is a DAG."""
        graph = ComplexGraph.from_cache(empty_cache)
        is_dag, cycle = graph.check_dag('follows')
        assert is_dag
        assert cycle is None

    def test_dag_no_cycle(self):
        """Linear chain is a DAG."""
        cache = {
            'elements': {
                'vertices': {
                    'v:execution:a': {'id': 'v:execution:a', 'type': 'vertex/execution'},
                    'v:execution:b': {'id': 'v:execution:b', 'type': 'vertex/execution'},
                    'v:execution:c': {'id': 'v:execution:c', 'type': 'vertex/execution'},
                },
                'edges': {
                    'e:follows:a-b': {
                        'id': 'e:follows:a-b',
                        'type': 'edge/follows',
                        'source': 'v:execution:a',
                        'target': 'v:execution:b',
                        'orientation': 'directed',
                    },
                    'e:follows:b-c': {
                        'id': 'e:follows:b-c',
                        'type': 'edge/follows',
                        'source': 'v:execution:b',
                        'target': 'v:execution:c',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            }
        }
        graph = ComplexGraph.from_cache(cache)
        is_dag, cycle = graph.check_dag('follows')
        assert is_dag
        assert cycle is None

    def test_dag_with_cycle(self):
        """Cycle is detected."""
        cache = {
            'elements': {
                'vertices': {
                    'v:execution:a': {'id': 'v:execution:a', 'type': 'vertex/execution'},
                    'v:execution:b': {'id': 'v:execution:b', 'type': 'vertex/execution'},
                },
                'edges': {
                    'e:follows:a-b': {
                        'id': 'e:follows:a-b',
                        'type': 'edge/follows',
                        'source': 'v:execution:a',
                        'target': 'v:execution:b',
                        'orientation': 'directed',
                    },
                    'e:follows:b-a': {
                        'id': 'e:follows:b-a',
                        'type': 'edge/follows',
                        'source': 'v:execution:b',
                        'target': 'v:execution:a',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            }
        }
        graph = ComplexGraph.from_cache(cache)
        is_dag, cycle = graph.check_dag('follows')
        assert not is_dag
        assert cycle is not None


# ========== Rule Engine Tests ==========

class TestOntologyRuleEngine:
    """Tests for the ontology rule engine."""

    def test_empty_cache_no_violations(self, empty_cache):
        """Empty cache has no violations."""
        violations = check_ontology_rules(empty_cache)
        assert len(violations) == 0

    def test_valid_assurance_minimal(self, minimal_assurance_cache):
        """Minimal valid assurance triangle should have few violations."""
        violations = check_ontology_rules(minimal_assurance_cache)
        # The minimal cache is valid except for b2 anchoring
        error_violations = [v for v in violations if v.severity == Severity.ERROR]
        # Should only have warnings about b2 anchoring
        for v in violations:
            if v.severity == Severity.ERROR:
                # Should not have endpoint or face boundary errors
                assert v.rule_name not in ['edge_endpoint_type_compliance', 'face_boundary_closure']


class TestEdgeEndpointRules:
    """Tests for edge endpoint type constraints."""

    def test_valid_verification_edge(self):
        """Verification edge from doc to spec is valid."""
        cache = {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec'},
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
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_edge_endpoint_constraints()

        endpoint_violations = [v for v in engine.violations
                              if v.rule_name == 'edge_endpoint_type_compliance']
        assert len(endpoint_violations) == 0

    def test_invalid_verification_edge_wrong_source(self):
        """Verification edge from guidance to spec is invalid."""
        cache = {
            'elements': {
                'vertices': {
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec'},
                },
                'edges': {
                    'e:verification:test': {
                        'id': 'e:verification:test',
                        'type': 'edge/verification',
                        'source': 'v:guidance:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_edge_endpoint_constraints()

        endpoint_violations = [v for v in engine.violations
                              if v.rule_name == 'edge_endpoint_type_compliance']
        # Guidance is allowed for verification source per ontology
        # so this should NOT be a violation
        assert len(endpoint_violations) == 0

    def test_invalid_signs_edge_wrong_source(self):
        """Signs edge from doc to doc is invalid (should be from signer)."""
        cache = {
            'elements': {
                'vertices': {
                    'v:doc:a': {'id': 'v:doc:a', 'type': 'vertex/doc'},
                    'v:doc:b': {'id': 'v:doc:b', 'type': 'vertex/doc'},
                },
                'edges': {
                    'e:signs:test': {
                        'id': 'e:signs:test',
                        'type': 'edge/signs',
                        'source': 'v:doc:a',
                        'target': 'v:doc:b',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_edge_endpoint_constraints()

        endpoint_violations = [v for v in engine.violations
                              if v.rule_name == 'edge_endpoint_type_compliance']
        assert len(endpoint_violations) == 1
        assert 'signs' in endpoint_violations[0].message


class TestDegreeConstraintRules:
    """Tests for vertex degree constraints."""

    def test_doc_multiple_verifications_allowed(self):
        """Doc can have multiple verification edges (for multi-type documents).

        Documents can verify against multiple specs when they have multiple types.
        For example, a persona document can verify against both spec/persona AND
        spec/doc simultaneously. This was previously restricted to at most 1, but
        that constraint was incorrect.
        """
        cache = {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc'},
                    'v:spec:a': {'id': 'v:spec:a', 'type': 'vertex/spec'},
                    'v:spec:b': {'id': 'v:spec:b', 'type': 'vertex/spec'},
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
                },
                'faces': {},
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_degree_constraints()

        # No violations - documents can have multiple verification edges
        degree_violations = [v for v in engine.violations
                           if v.rule_name == 'degree_constraint'
                           and v.element_id == 'v:doc:test']
        assert len(degree_violations) == 0

    def test_spec_must_have_coupling(self):
        """Spec must have exactly one coupling edge."""
        cache = {
            'elements': {
                'vertices': {
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec'},
                },
                'edges': {},
                'faces': {},
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_degree_constraints()

        degree_violations = [v for v in engine.violations
                           if v.rule_name == 'degree_constraint'
                           and v.element_id == 'v:spec:test']
        assert len(degree_violations) == 1
        assert 'minimum is 1' in degree_violations[0].message


class TestFaceBoundaryRules:
    """Tests for face boundary closure."""

    def test_valid_face_boundary(self, minimal_assurance_cache):
        """Valid face with 3 vertices and 3 edges passes."""
        engine = OntologyRuleEngine.from_cache(minimal_assurance_cache)
        engine._check_face_boundary_closure()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'face_boundary_closure']
        assert len(boundary_violations) == 0

    def test_face_wrong_vertex_count(self):
        """Face with wrong vertex count fails."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a', 'type': 'vertex/doc'},
                    'v:b': {'id': 'v:b', 'type': 'vertex/spec'},
                },
                'edges': {},
                'faces': {
                    'f:test': {
                        'id': 'f:test',
                        'type': 'face/assurance',
                        'vertices': ['v:a', 'v:b'],  # Only 2 vertices
                        'edges': ['e:1', 'e:2', 'e:3'],
                        'orientation': 'oriented',
                    },
                },
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_face_boundary_closure()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'face_boundary_closure']
        assert len(boundary_violations) == 1
        assert 'must have exactly 3' in boundary_violations[0].message


class TestSignatureRules:
    """Tests for signature face rules."""

    def test_signature_requires_qualifies(self):
        """Signature face requires qualifies edge from signer to guidance."""
        cache = {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance'},
                    'v:signer:test': {'id': 'v:signer:test', 'type': 'vertex/signer'},
                },
                'edges': {
                    'e:validation:test': {
                        'id': 'e:validation:test',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:signs:test': {
                        'id': 'e:signs:test',
                        'type': 'edge/signs',
                        'source': 'v:signer:test',
                        'target': 'v:doc:test',
                        'orientation': 'directed',
                    },
                    # Missing: e:qualifies:test from signer to guidance
                },
                'faces': {
                    'f:signature:test': {
                        'id': 'f:signature:test',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:test'],
                        'edges': ['e:validation:test', 'e:signs:test', 'e:qualifies:missing'],
                        'orientation': 'oriented',
                        'doc': 'v:doc:test',
                        'guidance': 'v:guidance:test',
                        'signer': 'v:signer:test',
                    },
                },
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_signature_requires_qualification()

        sig_violations = [v for v in engine.violations
                        if v.rule_name == 'signature_requires_qualification']
        assert len(sig_violations) == 1
        assert 'lacks qualifies edge' in sig_violations[0].message


class TestAssuranceRequiresSignature:
    """Tests for assurance face must have signature face sharing validation edge.

    This is a critical local rule: an assurance face (doc, spec, guidance) must
    have a signature face (doc, guidance, signer) sharing its validation edge.

    Key insight on directionality:
    - Signature faces CAN exist without assurance faces (they represent a signer's
      approval of a validation, which may pre-exist the assurance)
    - Assurance faces CANNOT exist without a corresponding signature - every
      assurance requires human accountability via a signed validation

    The shared validation edge ensures:
    - Every assurance has human accountability via a signed validation
    - The signer is accountable for the same validation in the assurance triangle
    """

    @pytest.fixture
    def valid_assurance_with_signature_cache(self):
        """Complete valid setup with assurance and signature faces sharing validation edge.

        Structure:
        - Assurance face: doc -- spec -- guidance (verification, validation, coupling)
        - Signature face: doc -- guidance -- signer (validation, qualifies, signs)
        - Both faces SHARE the validation edge (doc -> guidance)
        """
        return {
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
                    # Signature edges
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
                    'f:assurance:test': {
                        'id': 'f:assurance:test',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:test', 'e:validation:test', 'e:coupling:test'],
                        'orientation': 'oriented',
                        'target': 'v:doc:test',
                        'spec': 'v:spec:test',
                        'guidance': 'v:guidance:test',
                        'validation_edge': 'e:validation:test',
                        'verification_edge': 'e:verification:test',
                        'coupling_edge': 'e:coupling:test',
                    },
                    'f:signature:test': {
                        'id': 'f:signature:test',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        # SHARES e:validation:test with assurance face
                        'edges': ['e:validation:test', 'e:qualifies:alice-guidance', 'e:signs:alice-doc'],
                        'orientation': 'oriented',
                        'doc': 'v:doc:test',
                        'guidance': 'v:guidance:test',
                        'signer': 'v:signer:alice',
                        'validation_edge': 'e:validation:test',
                    },
                },
            },
            'statistics': {'vertices': 4, 'edges': 5, 'faces': 2}
        }

    @pytest.fixture
    def invalid_assurance_no_shared_validation_cache(self):
        """Invalid setup: assurance face has validation edge not shared with signature.

        The assurance face has its own validation edge that is NOT the same as
        the signature face's validation edge. This violates the rule.
        """
        return {
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
                    'e:validation:assurance': {
                        'id': 'e:validation:assurance',
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
                    # Signature edges - DIFFERENT validation edge!
                    'e:validation:signature': {
                        'id': 'e:validation:signature',
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
                    'f:assurance:test': {
                        'id': 'f:assurance:test',
                        'type': 'face/assurance',
                        'vertices': ['v:doc:test', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:test', 'e:validation:assurance', 'e:coupling:test'],
                        'orientation': 'oriented',
                        'target': 'v:doc:test',
                        'spec': 'v:spec:test',
                        'guidance': 'v:guidance:test',
                        'validation_edge': 'e:validation:assurance',
                    },
                    'f:signature:test': {
                        'id': 'f:signature:test',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        # Uses DIFFERENT validation edge - NOT shared!
                        'edges': ['e:validation:signature', 'e:qualifies:alice-guidance', 'e:signs:alice-doc'],
                        'orientation': 'oriented',
                        'doc': 'v:doc:test',
                        'guidance': 'v:guidance:test',
                        'signer': 'v:signer:alice',
                        'validation_edge': 'e:validation:signature',
                    },
                },
            },
            'statistics': {'vertices': 4, 'edges': 6, 'faces': 2}
        }

    @pytest.fixture
    def valid_signature_without_assurance_cache(self):
        """Valid setup: signature face exists alone - this is OK!

        Signature faces CAN exist without assurance faces. They represent a signer's
        approval of a validation, which may pre-exist the assurance.
        """
        return {
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
                    # Signature face alone - this is VALID
                    'f:signature:standalone': {
                        'id': 'f:signature:standalone',
                        'type': 'face/signature',
                        'vertices': ['v:doc:test', 'v:guidance:test', 'v:signer:alice'],
                        'edges': ['e:validation:test', 'e:qualifies:alice-guidance', 'e:signs:alice-doc'],
                        'orientation': 'oriented',
                        'doc': 'v:doc:test',
                        'guidance': 'v:guidance:test',
                        'signer': 'v:signer:alice',
                        'validation_edge': 'e:validation:test',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    @pytest.fixture
    def invalid_assurance_without_signature_cache(self):
        """Invalid setup: assurance face exists without signature - NOT allowed!

        Assurance faces CANNOT exist without a corresponding signature face.
        Every assurance requires human accountability via a signed validation.
        """
        return {
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
                        'target': 'v:doc:test',
                        'spec': 'v:spec:test',
                        'guidance': 'v:guidance:test',
                        'validation_edge': 'e:validation:test',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_valid_assurance_with_signature(self, valid_assurance_with_signature_cache):
        """Assurance face with signature face sharing validation edge should pass."""
        engine = OntologyRuleEngine.from_cache(valid_assurance_with_signature_cache)
        engine._check_assurance_requires_signature()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assurance_requires_signature']
        assert len(adjacency_violations) == 0

    def test_invalid_assurance_different_validation_edge(self, invalid_assurance_no_shared_validation_cache):
        """Assurance face with different validation edge than signature face should fail."""
        engine = OntologyRuleEngine.from_cache(invalid_assurance_no_shared_validation_cache)
        engine._check_assurance_requires_signature()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assurance_requires_signature']
        assert len(adjacency_violations) == 1
        assert 'No signature face shares validation edge' in adjacency_violations[0].message

    def test_valid_signature_without_assurance(self, valid_signature_without_assurance_cache):
        """Signature face without assurance face is VALID - signatures can pre-exist assurance."""
        engine = OntologyRuleEngine.from_cache(valid_signature_without_assurance_cache)
        engine._check_assurance_requires_signature()

        # No violations - signature faces can exist alone
        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assurance_requires_signature']
        assert len(adjacency_violations) == 0

    def test_invalid_assurance_without_signature(self, invalid_assurance_without_signature_cache):
        """Assurance face without signature face is INVALID - assurance requires human sign-off."""
        engine = OntologyRuleEngine.from_cache(invalid_assurance_without_signature_cache)
        engine._check_assurance_requires_signature()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assurance_requires_signature']
        assert len(adjacency_violations) == 1
        assert 'No signature face shares validation edge' in adjacency_violations[0].message
        assert 'assurance requires human sign-off' in adjacency_violations[0].message

    def test_assurance_no_validation_edge_in_boundary(self):
        """Assurance face without validation edge in boundary should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance'},
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
                        'type': 'edge/other',  # Wrong type - not validation!
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
                        # Has verification, coupling, and 'other' - NO validation!
                        'edges': ['e:verification:test', 'e:other:test', 'e:coupling:test'],
                        'orientation': 'oriented',
                        'target': 'v:doc:test',
                        'spec': 'v:spec:test',
                        'guidance': 'v:guidance:test',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_assurance_requires_signature()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assurance_requires_signature']
        assert len(adjacency_violations) == 1
        assert 'no validation edge in boundary' in adjacency_violations[0].message

    def test_full_ontology_check_includes_assurance_signature_rule(self, valid_assurance_with_signature_cache):
        """Full check_all should include assurance-requires-signature check."""
        engine = OntologyRuleEngine.from_cache(valid_assurance_with_signature_cache)
        all_violations = engine.check_all()

        # Filter to only adjacency violations
        adjacency_violations = [v for v in all_violations
                               if v.rule_name == 'assurance_requires_signature']

        # Should have no adjacency violations for valid cache
        assert len(adjacency_violations) == 0


class TestExecutionDagRules:
    """Tests for execution trace DAG requirements."""

    def test_execution_dag_valid(self):
        """Valid execution trace DAG passes."""
        cache = {
            'elements': {
                'vertices': {
                    'v:execution:a': {'id': 'v:execution:a', 'type': 'vertex/execution'},
                    'v:execution:b': {'id': 'v:execution:b', 'type': 'vertex/execution'},
                },
                'edges': {
                    'e:follows:a-b': {
                        'id': 'e:follows:a-b',
                        'type': 'edge/follows',
                        'source': 'v:execution:a',
                        'target': 'v:execution:b',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_execution_trace_dag()

        dag_violations = [v for v in engine.violations
                        if v.rule_name == 'execution_trace_dag']
        assert len(dag_violations) == 0

    def test_execution_dag_with_cycle(self):
        """Execution trace with cycle fails."""
        cache = {
            'elements': {
                'vertices': {
                    'v:execution:a': {'id': 'v:execution:a', 'type': 'vertex/execution'},
                    'v:execution:b': {'id': 'v:execution:b', 'type': 'vertex/execution'},
                },
                'edges': {
                    'e:follows:a-b': {
                        'id': 'e:follows:a-b',
                        'type': 'edge/follows',
                        'source': 'v:execution:a',
                        'target': 'v:execution:b',
                        'orientation': 'directed',
                    },
                    'e:follows:b-a': {
                        'id': 'e:follows:b-a',
                        'type': 'edge/follows',
                        'source': 'v:execution:b',
                        'target': 'v:execution:a',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            }
        }
        engine = OntologyRuleEngine.from_cache(cache)
        engine._check_execution_trace_dag()

        dag_violations = [v for v in engine.violations
                        if v.rule_name == 'execution_trace_dag']
        assert len(dag_violations) == 1
        assert 'cycle' in dag_violations[0].message


# ========== Integration Tests ==========

class TestRuleEngineIntegration:
    """Integration tests for rule engine with check_ontology_rules function."""

    def test_check_ontology_rules_returns_list(self, empty_cache):
        """check_ontology_rules returns a list."""
        violations = check_ontology_rules(empty_cache)
        assert isinstance(violations, list)

    def test_violation_has_required_fields(self, minimal_assurance_cache):
        """RuleViolation has all required fields."""
        # Add an invalid edge to ensure we get a violation
        cache = minimal_assurance_cache.copy()
        cache['elements'] = minimal_assurance_cache['elements'].copy()
        cache['elements']['edges'] = minimal_assurance_cache['elements']['edges'].copy()
        cache['elements']['edges']['e:signs:invalid'] = {
            'id': 'e:signs:invalid',
            'type': 'edge/signs',
            'source': 'v:doc:test',  # Invalid: should be signer
            'target': 'v:spec:test',
            'orientation': 'directed',
        }

        violations = check_ontology_rules(cache)

        # Find our expected violation
        signs_violations = [v for v in violations
                          if v.element_id == 'e:signs:invalid']
        assert len(signs_violations) > 0

        v = signs_violations[0]
        assert hasattr(v, 'rule_name')
        assert hasattr(v, 'rule_type')
        assert hasattr(v, 'severity')
        assert hasattr(v, 'element_id')
        assert hasattr(v, 'element_type')
        assert hasattr(v, 'message')


# ========== Graph Utility Method Tests ==========

class TestGraphUtilities:
    """Tests for graph utility methods including type filtering with strict mode."""

    @pytest.fixture
    def type_inheritance_cache(self):
        """Cache with type inheritance hierarchy (spec inherits from doc)."""
        return {
            'elements': {
                'vertices': {
                    'v:doc:plain': {'id': 'v:doc:plain', 'type': 'vertex/doc', 'name': 'Plain Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:spec:other': {'id': 'v:spec:other', 'type': 'vertex/spec', 'name': 'Other Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:a': {
                        'id': 'e:verification:a',
                        'type': 'edge/verification',
                        'source': 'v:doc:plain',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:a': {
                        'id': 'e:coupling:a',
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
                        'vertices': ['v:doc:plain', 'v:spec:test', 'v:guidance:test'],
                        'edges': ['e:verification:a', 'e:coupling:a', 'e:validation:a'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 4, 'edges': 2, 'faces': 1}
        }

    def test_get_all_vertices(self, type_inheritance_cache):
        """Test get_all_vertices returns all vertex IDs."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        vertices = graph.get_all_vertices()
        assert len(vertices) == 4
        assert 'v:doc:plain' in vertices
        assert 'v:spec:test' in vertices

    def test_get_all_edges(self, type_inheritance_cache):
        """Test get_all_edges returns all edge IDs."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        edges = graph.get_all_edges()
        assert len(edges) == 2
        assert 'e:verification:a' in edges
        assert 'e:coupling:a' in edges

    def test_get_all_faces(self, type_inheritance_cache):
        """Test get_all_faces returns all face IDs."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        faces = graph.get_all_faces()
        assert len(faces) == 1
        assert 'f:assurance:test' in faces

    def test_get_vertices_by_type_non_strict(self, type_inheritance_cache):
        """Test get_vertices_by_type with strict=False includes path-based subtypes.

        Note: Current implementation uses path-prefix inheritance ('vertex/doc/subtype').
        Ontology semantic inheritance (spec inherits from doc) requires explicit
        type hierarchy which is not yet implemented.
        """
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        # Non-strict uses path prefix matching (e.g., 'vertex/doc/subtype')
        # NOT semantic inheritance (spec doesn't inherit from doc via path)
        docs = graph.get_vertices_by_type('vertex/doc', strict=False)
        # Only includes exact type and path subtypes, not semantic subtypes
        assert 'v:doc:plain' in docs
        # Note: v:spec:test is NOT included because 'vertex/spec' doesn't
        # start with 'vertex/doc/' - semantic inheritance not yet supported

    def test_get_vertices_by_type_strict(self, type_inheritance_cache):
        """Test get_vertices_by_type with strict=True excludes subtypes."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        # strict=True should only return exact type matches
        docs = graph.get_vertices_by_type('vertex/doc', strict=True)
        assert 'v:doc:plain' in docs
        assert 'v:spec:test' not in docs
        assert 'v:spec:other' not in docs
        assert len(docs) == 1

    def test_get_vertices_by_type_strict_spec(self, type_inheritance_cache):
        """Test strict mode returns only exact spec matches."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        specs = graph.get_vertices_by_type('vertex/spec', strict=True)
        assert len(specs) == 2
        assert 'v:spec:test' in specs
        assert 'v:spec:other' in specs

    def test_get_edges_by_type_non_strict(self, type_inheritance_cache):
        """Test get_edges_by_type with strict=False."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        edges = graph.get_edges_by_type('edge/verification', strict=False)
        assert len(edges) == 1
        assert 'e:verification:a' in edges

    def test_get_edges_by_type_strict(self, type_inheritance_cache):
        """Test get_edges_by_type with strict=True."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        edges = graph.get_edges_by_type('edge/verification', strict=True)
        assert len(edges) == 1
        assert 'e:verification:a' in edges

    def test_get_faces_by_type(self, type_inheritance_cache):
        """Test get_faces_by_type."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        faces = graph.get_faces_by_type('face/assurance', strict=False)
        assert len(faces) == 1
        assert 'f:assurance:test' in faces

    def test_get_elements_all(self, type_inheritance_cache):
        """Test get_elements with no filters returns all."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        elements = graph.get_elements()
        assert len(elements['vertices']) == 4
        assert len(elements['edges']) == 2
        assert len(elements['faces']) == 1

    def test_get_elements_by_dimension(self, type_inheritance_cache):
        """Test get_elements filtered by dimension."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        # Dimension 0 = vertices
        elements = graph.get_elements(dimension=0)
        assert len(elements['vertices']) == 4
        assert len(elements['edges']) == 0
        assert len(elements['faces']) == 0

        # Dimension 1 = edges
        elements = graph.get_elements(dimension=1)
        assert len(elements['vertices']) == 0
        assert len(elements['edges']) == 2
        assert len(elements['faces']) == 0

        # Dimension 2 = faces
        elements = graph.get_elements(dimension=2)
        assert len(elements['vertices']) == 0
        assert len(elements['edges']) == 0
        assert len(elements['faces']) == 1

    def test_get_elements_by_type_non_strict(self, type_inheritance_cache):
        """Test get_elements filtered by type with inheritance."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        elements = graph.get_elements(element_type='vertex/doc', strict=False)
        # Should include doc + specs
        assert len(elements['vertices']) >= 1
        assert 'v:doc:plain' in elements['vertices']

    def test_get_elements_by_type_strict(self, type_inheritance_cache):
        """Test get_elements filtered by type strict mode."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        elements = graph.get_elements(element_type='vertex/doc', strict=True)
        assert len(elements['vertices']) == 1
        assert 'v:doc:plain' in elements['vertices']

    def test_get_element_data(self, type_inheritance_cache):
        """Test get_element_data returns correct data."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        data = graph.get_element_data('v:doc:plain')
        assert data is not None
        assert data['id'] == 'v:doc:plain'
        assert data['type'] == 'vertex/doc'
        assert data['name'] == 'Plain Doc'

        # Edge data
        data = graph.get_element_data('e:verification:a')
        assert data is not None
        assert data['type'] == 'edge/verification'

        # Face data
        data = graph.get_element_data('f:assurance:test')
        assert data is not None
        assert data['type'] == 'face/assurance'

    def test_get_element_data_not_found(self, type_inheritance_cache):
        """Test get_element_data returns None for unknown element."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        data = graph.get_element_data('v:nonexistent:id')
        assert data is None

    def test_get_element_type(self, type_inheritance_cache):
        """Test get_element_type returns correct type."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        assert graph.get_element_type('v:doc:plain') == 'vertex/doc'
        assert graph.get_element_type('v:spec:test') == 'vertex/spec'
        assert graph.get_element_type('e:verification:a') == 'edge/verification'
        assert graph.get_element_type('f:assurance:test') == 'face/assurance'

    def test_get_element_type_not_found(self, type_inheritance_cache):
        """Test get_element_type returns None for unknown element."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        assert graph.get_element_type('v:nonexistent:id') is None

    def test_list_types_all(self, type_inheritance_cache):
        """Test list_types returns all types."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)
        types = graph.list_types()
        assert 'vertex/doc' in types['vertex_types']
        assert 'vertex/spec' in types['vertex_types']
        assert 'vertex/guidance' in types['vertex_types']
        assert 'edge/verification' in types['edge_types']
        assert 'edge/coupling' in types['edge_types']
        assert 'face/assurance' in types['face_types']

    def test_list_types_by_dimension(self, type_inheritance_cache):
        """Test list_types filtered by dimension."""
        graph = ComplexGraph.from_cache(type_inheritance_cache)

        # Vertices only
        types = graph.list_types(dimension=0)
        assert len(types['vertex_types']) > 0
        assert len(types['edge_types']) == 0
        assert len(types['face_types']) == 0

        # Edges only
        types = graph.list_types(dimension=1)
        assert len(types['vertex_types']) == 0
        assert len(types['edge_types']) > 0
        assert len(types['face_types']) == 0


class TestBoundaryOperations:
    """Tests for simplicial complex boundary operations."""

    @pytest.fixture
    def full_complex_cache(self):
        """Cache with a complete assurance triangle for boundary tests."""
        return {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:a': {
                        'id': 'e:verification:a',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:validation:a': {
                        'id': 'e:validation:a',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:a': {
                        'id': 'e:coupling:a',
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
                        'edges': ['e:verification:a', 'e:validation:a', 'e:coupling:a'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_get_boundary_vertex(self, full_complex_cache):
        """Vertex boundary is empty."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        boundary = graph.get_boundary('v:doc:test')
        assert boundary == []

    def test_get_boundary_edge(self, full_complex_cache):
        """Edge boundary is its two vertices."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        boundary = graph.get_boundary('e:verification:a')
        assert len(boundary) == 2
        assert 'v:doc:test' in boundary
        assert 'v:spec:test' in boundary

    def test_get_boundary_face(self, full_complex_cache):
        """Face boundary is its three edges."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        boundary = graph.get_boundary('f:assurance:test')
        assert len(boundary) == 3
        assert 'e:verification:a' in boundary
        assert 'e:validation:a' in boundary
        assert 'e:coupling:a' in boundary

    def test_get_boundary_not_found(self, full_complex_cache):
        """Boundary of non-existent element is None."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        boundary = graph.get_boundary('v:nonexistent')
        assert boundary is None

    def test_get_edge_boundary(self, full_complex_cache):
        """Get edge boundary as tuple."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        boundary = graph.get_edge_boundary('e:verification:a')
        assert boundary == ('v:doc:test', 'v:spec:test')

    def test_get_face_boundary(self, full_complex_cache):
        """Get face boundary as list of edges."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        boundary = graph.get_face_boundary('f:assurance:test')
        assert len(boundary) == 3
        assert set(boundary) == {'e:verification:a', 'e:validation:a', 'e:coupling:a'}

    def test_get_face_vertices(self, full_complex_cache):
        """Get face vertices."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        vertices = graph.get_face_vertices('f:assurance:test')
        assert len(vertices) == 3
        assert set(vertices) == {'v:doc:test', 'v:spec:test', 'v:guidance:test'}

    def test_get_coboundary_vertex(self, full_complex_cache):
        """Coboundary of vertex is incident edges."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        coboundary = graph.get_coboundary('v:doc:test')
        # Doc is source of verification and validation edges
        assert 'e:verification:a' in coboundary
        assert 'e:validation:a' in coboundary

    def test_get_coboundary_edge(self, full_complex_cache):
        """Coboundary of edge is faces containing it."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        coboundary = graph.get_coboundary('e:verification:a')
        assert 'f:assurance:test' in coboundary

    def test_get_coboundary_face(self, full_complex_cache):
        """Coboundary of face is empty (no 3-simplices)."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        coboundary = graph.get_coboundary('f:assurance:test')
        assert coboundary == []

    def test_get_dimension(self, full_complex_cache):
        """Get dimension of elements."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        assert graph.get_dimension('v:doc:test') == 0
        assert graph.get_dimension('e:verification:a') == 1
        assert graph.get_dimension('f:assurance:test') == 2
        assert graph.get_dimension('nonexistent') is None

    def test_is_in_boundary(self, full_complex_cache):
        """Check boundary membership."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        # Vertex in edge boundary
        assert graph.is_in_boundary('v:doc:test', 'e:verification:a')
        assert not graph.is_in_boundary('v:guidance:test', 'e:verification:a')
        # Edge in face boundary
        assert graph.is_in_boundary('e:verification:a', 'f:assurance:test')
        assert not graph.is_in_boundary('v:doc:test', 'f:assurance:test')

    def test_closure_single_face(self, full_complex_cache):
        """Closure of face includes all edges and vertices."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        closure = graph.closure(['f:assurance:test'])
        assert len(closure['faces']) == 1
        assert len(closure['edges']) == 3
        assert len(closure['vertices']) == 3

    def test_closure_single_edge(self, full_complex_cache):
        """Closure of edge includes its vertices."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        closure = graph.closure(['e:verification:a'])
        assert len(closure['faces']) == 0
        assert len(closure['edges']) == 1
        assert len(closure['vertices']) == 2

    def test_star_vertex(self, full_complex_cache):
        """Star of vertex includes vertex, incident edges, and containing faces."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        star = graph.star('v:doc:test')
        assert 'v:doc:test' in star['vertices']
        # Doc is source of verification and validation
        assert 'e:verification:a' in star['edges']
        assert 'e:validation:a' in star['edges']
        # Doc is in the assurance face
        assert 'f:assurance:test' in star['faces']

    def test_link_vertex(self, full_complex_cache):
        """Link of vertex is opposite vertices/edges in containing faces."""
        graph = ComplexGraph.from_cache(full_complex_cache)
        link = graph.link('v:doc:test')
        # Link vertices are the other vertices in faces containing doc
        assert 'v:spec:test' in link['vertices']
        assert 'v:guidance:test' in link['vertices']
        assert 'v:doc:test' not in link['vertices']
        # Link edges are edges in faces that don't contain doc
        assert 'e:coupling:a' in link['edges']
        assert 'e:verification:a' not in link['edges']  # Contains doc


# ========== Orientation Tests ==========

class TestOrientationOperations:
    """Tests for orientation-aware boundary operations."""

    @pytest.fixture
    def oriented_complex_cache(self):
        """Cache with mixed directed/undirected edges and oriented face."""
        return {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:a': {
                        'id': 'e:verification:a',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:validation:a': {
                        'id': 'e:validation:a',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:a': {
                        'id': 'e:coupling:a',
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
                        'edges': ['e:verification:a', 'e:validation:a', 'e:coupling:a'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    # Edge orientation tests

    def test_is_edge_directed_true(self, oriented_complex_cache):
        """Directed edge returns True."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.is_edge_directed('e:verification:a') is True

    def test_is_edge_directed_false(self, oriented_complex_cache):
        """Undirected edge returns False."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.is_edge_directed('e:coupling:a') is False

    def test_is_edge_directed_not_found(self, oriented_complex_cache):
        """Non-existent edge returns None."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.is_edge_directed('e:nonexistent') is None

    def test_get_edge_boundary_ordered(self, oriented_complex_cache):
        """Edge boundary returns ordered tuple (source, target)."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        boundary = graph.get_edge_boundary('e:verification:a')
        # Order matters for directed edges
        assert boundary == ('v:doc:test', 'v:spec:test')
        assert boundary[0] == 'v:doc:test'  # Source
        assert boundary[1] == 'v:spec:test'  # Target

    def test_get_edge_boundary_set(self, oriented_complex_cache):
        """Edge boundary set is unordered."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        boundary_set = graph.get_edge_boundary_set('e:verification:a')
        assert boundary_set == {'v:doc:test', 'v:spec:test'}

    def test_get_edge_boundary_set_not_found(self, oriented_complex_cache):
        """Non-existent edge returns None for boundary set."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.get_edge_boundary_set('e:nonexistent') is None

    def test_get_edge_boundary_with_types(self, oriented_complex_cache):
        """Get edge boundary with vertex types."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        boundary_types = graph.get_edge_boundary_with_types('e:verification:a')
        assert boundary_types is not None
        (src, tgt) = boundary_types
        assert src == ('v:doc:test', 'vertex/doc')
        assert tgt == ('v:spec:test', 'vertex/spec')

    def test_get_edge_endpoint_types(self, oriented_complex_cache):
        """Get just the types of edge endpoints."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        types = graph.get_edge_endpoint_types('e:verification:a')
        assert types == ('vertex/doc', 'vertex/spec')

    def test_get_edge_endpoint_types_not_found(self, oriented_complex_cache):
        """Non-existent edge returns None for endpoint types."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.get_edge_endpoint_types('e:nonexistent') is None

    # Face orientation tests

    def test_is_face_oriented_true(self, oriented_complex_cache):
        """Oriented face returns True."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.is_face_oriented('f:assurance:test') is True

    def test_is_face_oriented_not_found(self, oriented_complex_cache):
        """Non-existent face returns None."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.is_face_oriented('f:nonexistent') is None

    def test_get_face_boundary_ordered(self, oriented_complex_cache):
        """Face boundary returns ordered list of edges."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        boundary = graph.get_face_boundary('f:assurance:test')
        # Order is preserved from definition
        assert boundary == ['e:verification:a', 'e:validation:a', 'e:coupling:a']

    def test_get_face_boundary_set(self, oriented_complex_cache):
        """Face boundary set is unordered."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        boundary_set = graph.get_face_boundary_set('f:assurance:test')
        assert boundary_set == {'e:verification:a', 'e:validation:a', 'e:coupling:a'}

    def test_get_face_boundary_set_not_found(self, oriented_complex_cache):
        """Non-existent face returns None for boundary set."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.get_face_boundary_set('f:nonexistent') is None

    def test_get_face_vertices_ordered(self, oriented_complex_cache):
        """Face vertices returns ordered list."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        vertices = graph.get_face_vertices('f:assurance:test')
        # Order is preserved from definition
        assert vertices == ['v:doc:test', 'v:spec:test', 'v:guidance:test']

    def test_get_face_vertices_set(self, oriented_complex_cache):
        """Face vertices set is unordered."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        vertices_set = graph.get_face_vertices_set('f:assurance:test')
        assert vertices_set == {'v:doc:test', 'v:spec:test', 'v:guidance:test'}

    def test_get_face_vertices_set_not_found(self, oriented_complex_cache):
        """Non-existent face returns None for vertices set."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.get_face_vertices_set('f:nonexistent') is None

    def test_get_face_boundary_with_types(self, oriented_complex_cache):
        """Get face boundary edges with their types."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        boundary_types = graph.get_face_boundary_with_types('f:assurance:test')
        assert boundary_types is not None
        assert len(boundary_types) == 3
        # Order preserved with types
        assert boundary_types[0] == ('e:verification:a', 'edge/verification')
        assert boundary_types[1] == ('e:validation:a', 'edge/validation')
        assert boundary_types[2] == ('e:coupling:a', 'edge/coupling')

    def test_get_face_boundary_with_types_not_found(self, oriented_complex_cache):
        """Non-existent face returns None for boundary with types."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.get_face_boundary_with_types('f:nonexistent') is None

    def test_get_face_boundary_types(self, oriented_complex_cache):
        """Get set of edge types in face boundary."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        types = graph.get_face_boundary_types('f:assurance:test')
        assert types == {'edge/verification', 'edge/validation', 'edge/coupling'}

    def test_get_face_boundary_types_not_found(self, oriented_complex_cache):
        """Non-existent face returns None for boundary types."""
        graph = ComplexGraph.from_cache(oriented_complex_cache)
        assert graph.get_face_boundary_types('f:nonexistent') is None


# ========== Topology Rule Tests ==========

class TestTopologyRules:
    """Tests for topology rules (structural simplicial complex rules)."""

    @pytest.fixture
    def valid_complex_cache(self):
        """A valid simplicial complex with proper topology."""
        return {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc', 'name': 'Test Doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec', 'name': 'Test Spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance', 'name': 'Test Guidance'},
                },
                'edges': {
                    'e:verification:a': {
                        'id': 'e:verification:a',
                        'type': 'edge/verification',
                        'source': 'v:doc:test',
                        'target': 'v:spec:test',
                        'orientation': 'directed',
                    },
                    'e:validation:a': {
                        'id': 'e:validation:a',
                        'type': 'edge/validation',
                        'source': 'v:doc:test',
                        'target': 'v:guidance:test',
                        'orientation': 'directed',
                    },
                    'e:coupling:a': {
                        'id': 'e:coupling:a',
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
                        'edges': ['e:verification:a', 'e:validation:a', 'e:coupling:a'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_check_topology_valid_complex(self, valid_complex_cache):
        """Valid complex should have no topology violations."""
        complex = ComplexGraph.from_cache(valid_complex_cache)
        violations = check_topology(complex)
        assert len(violations) == 0

    def test_check_edge_valid_boundary_success(self, valid_complex_cache):
        """Edge with valid boundary should pass."""
        complex = ComplexGraph.from_cache(valid_complex_cache)
        violation = check_edge_valid_boundary(complex, 'e:verification:a')
        assert violation is None

    def test_check_edge_missing_source_vertex(self):
        """Edge with missing source vertex should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:target': {'id': 'v:target', 'type': 'vertex/doc', 'name': 'Target'},
                },
                'edges': {
                    'e:bad': {
                        'id': 'e:bad',
                        'type': 'edge/verification',
                        'source': 'v:missing',
                        'target': 'v:target',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violation = check_edge_valid_boundary(complex, 'e:bad')
        assert violation is not None
        assert violation.rule_name == 'edge_valid_boundary'
        assert 'v:missing' in violation.message
        assert 'does not exist' in violation.message

    def test_check_edge_missing_target_vertex(self):
        """Edge with missing target vertex should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:source': {'id': 'v:source', 'type': 'vertex/doc', 'name': 'Source'},
                },
                'edges': {
                    'e:bad': {
                        'id': 'e:bad',
                        'type': 'edge/verification',
                        'source': 'v:source',
                        'target': 'v:missing',
                        'orientation': 'directed',
                    },
                },
                'faces': {},
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violation = check_edge_valid_boundary(complex, 'e:bad')
        assert violation is not None
        assert 'v:missing' in violation.message

    def test_check_face_valid_boundary_success(self, valid_complex_cache):
        """Face with valid boundary should pass."""
        complex = ComplexGraph.from_cache(valid_complex_cache)
        violation = check_face_valid_boundary(complex, 'f:assurance:test')
        assert violation is None

    def test_check_face_wrong_edge_count(self):
        """Face with wrong number of edges should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a', 'type': 'vertex/doc'},
                    'v:b': {'id': 'v:b', 'type': 'vertex/spec'},
                },
                'edges': {
                    'e:1': {'id': 'e:1', 'type': 'edge/test', 'source': 'v:a', 'target': 'v:b'},
                    'e:2': {'id': 'e:2', 'type': 'edge/test', 'source': 'v:b', 'target': 'v:a'},
                },
                'faces': {
                    'f:bad': {
                        'id': 'f:bad',
                        'type': 'face/test',
                        'vertices': ['v:a', 'v:b'],
                        'edges': ['e:1', 'e:2'],  # Only 2 edges!
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violation = check_face_valid_boundary(complex, 'f:bad')
        assert violation is not None
        assert violation.rule_name == 'face_valid_boundary'
        assert 'exactly 3' in violation.message

    def test_check_face_missing_edge(self):
        """Face with missing boundary edge should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a', 'type': 'vertex/doc'},
                    'v:b': {'id': 'v:b', 'type': 'vertex/spec'},
                    'v:c': {'id': 'v:c', 'type': 'vertex/guidance'},
                },
                'edges': {
                    'e:1': {'id': 'e:1', 'type': 'edge/test', 'source': 'v:a', 'target': 'v:b'},
                    'e:2': {'id': 'e:2', 'type': 'edge/test', 'source': 'v:b', 'target': 'v:c'},
                    # e:3 is missing!
                },
                'faces': {
                    'f:bad': {
                        'id': 'f:bad',
                        'type': 'face/test',
                        'vertices': ['v:a', 'v:b', 'v:c'],
                        'edges': ['e:1', 'e:2', 'e:missing'],  # e:missing doesn't exist
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violation = check_face_valid_boundary(complex, 'f:bad')
        assert violation is not None
        assert 'e:missing' in violation.message
        assert 'does not exist' in violation.message

    def test_check_face_closure_success(self, valid_complex_cache):
        """Face with properly closed boundary should pass."""
        complex = ComplexGraph.from_cache(valid_complex_cache)
        violation = check_face_closure(complex, 'f:assurance:test')
        assert violation is None

    def test_check_face_closure_wrong_vertex_count(self):
        """Face with wrong number of vertices should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a', 'type': 'vertex/doc'},
                    'v:b': {'id': 'v:b', 'type': 'vertex/spec'},
                },
                'edges': {
                    'e:1': {'id': 'e:1', 'type': 'edge/test', 'source': 'v:a', 'target': 'v:b'},
                    'e:2': {'id': 'e:2', 'type': 'edge/test', 'source': 'v:b', 'target': 'v:a'},
                    'e:3': {'id': 'e:3', 'type': 'edge/test', 'source': 'v:a', 'target': 'v:b'},
                },
                'faces': {
                    'f:bad': {
                        'id': 'f:bad',
                        'type': 'face/test',
                        'vertices': ['v:a', 'v:b'],  # Only 2 vertices!
                        'edges': ['e:1', 'e:2', 'e:3'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violation = check_face_closure(complex, 'f:bad')
        assert violation is not None
        assert violation.rule_name == 'face_closure'
        assert 'exactly 3 vertices' in violation.message

    def test_check_face_closure_edges_dont_match_vertices(self):
        """Face where edges don't connect to declared vertices should fail."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a', 'type': 'vertex/doc'},
                    'v:b': {'id': 'v:b', 'type': 'vertex/spec'},
                    'v:c': {'id': 'v:c', 'type': 'vertex/guidance'},
                    'v:d': {'id': 'v:d', 'type': 'vertex/other'},  # Extra vertex
                },
                'edges': {
                    'e:1': {'id': 'e:1', 'type': 'edge/test', 'source': 'v:a', 'target': 'v:b'},
                    'e:2': {'id': 'e:2', 'type': 'edge/test', 'source': 'v:b', 'target': 'v:d'},  # Points to v:d!
                    'e:3': {'id': 'e:3', 'type': 'edge/test', 'source': 'v:d', 'target': 'v:a'},  # Points to v:d!
                },
                'faces': {
                    'f:bad': {
                        'id': 'f:bad',
                        'type': 'face/test',
                        'vertices': ['v:a', 'v:b', 'v:c'],  # Says v:c but edges use v:d
                        'edges': ['e:1', 'e:2', 'e:3'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violation = check_face_closure(complex, 'f:bad')
        assert violation is not None
        assert "don't connect to face vertices" in violation.message

    def test_check_topology_catches_all_violations(self):
        """check_topology should find multiple violations."""
        cache = {
            'elements': {
                'vertices': {
                    'v:a': {'id': 'v:a', 'type': 'vertex/doc'},
                },
                'edges': {
                    'e:bad': {
                        'id': 'e:bad',
                        'type': 'edge/test',
                        'source': 'v:a',
                        'target': 'v:missing',  # Missing target
                    },
                },
                'faces': {
                    'f:bad': {
                        'id': 'f:bad',
                        'type': 'face/test',
                        'vertices': ['v:a'],
                        'edges': ['e:bad', 'e:also-missing'],  # Wrong count AND missing edge
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {}
        }
        complex = ComplexGraph.from_cache(cache)
        violations = check_topology(complex)
        # Should catch: edge missing target, face wrong edge count
        assert len(violations) >= 2
        rule_names = {v.rule_name for v in violations}
        assert 'edge_valid_boundary' in rule_names
        assert 'face_valid_boundary' in rule_names


# ========== Local Rule Functions Tests ==========


class TestLocalRuleFunctions:
    """Tests for the local rule functions that implement the LOCAL + UNIVERSAL pattern."""

    @pytest.fixture
    def simple_cache(self):
        """A simple cache with one of each element."""
        return {
            'elements': {
                'vertices': {
                    'v:doc:test': {'id': 'v:doc:test', 'type': 'vertex/doc'},
                    'v:spec:test': {'id': 'v:spec:test', 'type': 'vertex/spec'},
                    'v:guidance:test': {'id': 'v:guidance:test', 'type': 'vertex/guidance'},
                    'v:signer:alice': {'id': 'v:signer:alice', 'type': 'vertex/signer'},
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
            'statistics': {'vertices': 4, 'edges': 3, 'faces': 1}
        }

    # ========== check_edge_endpoint_types tests ==========

    def test_check_edge_endpoint_types_valid(self, simple_cache):
        """Valid edge endpoints should pass."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # Verification edge: doc -> spec
        result = check_edge_endpoint_types(
            complex,
            'e:verification:test',
            source_types=['vertex/doc'],
            target_types=['vertex/spec']
        )
        assert result is None

    def test_check_edge_endpoint_types_wrong_source(self, simple_cache):
        """Wrong source type should fail."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # Verification edge source should be doc, not signer
        result = check_edge_endpoint_types(
            complex,
            'e:verification:test',
            source_types=['vertex/signer'],  # Wrong - should be doc
            target_types=['vertex/spec']
        )
        assert result is not None
        assert result.rule_type == RuleType.EDGE_ENDPOINT
        assert 'Source' in result.message

    def test_check_edge_endpoint_types_wrong_target(self, simple_cache):
        """Wrong target type should fail."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # Verification edge target should be spec, not guidance
        result = check_edge_endpoint_types(
            complex,
            'e:verification:test',
            source_types=['vertex/doc'],
            target_types=['vertex/guidance']  # Wrong - should be spec
        )
        assert result is not None
        assert result.rule_type == RuleType.EDGE_ENDPOINT
        assert 'Target' in result.message

    def test_check_edge_endpoint_types_subtype_match(self, simple_cache):
        """Subtype matching should work (spec is a doc subtype)."""
        # Add a spec with a more specific subtype
        simple_cache['elements']['vertices']['v:spec:sub'] = {
            'id': 'v:spec:sub',
            'type': 'vertex/spec/custom'  # Subtype of spec
        }
        simple_cache['elements']['edges']['e:ver:sub'] = {
            'id': 'e:ver:sub',
            'type': 'edge/verification',
            'source': 'v:doc:test',
            'target': 'v:spec:sub',
            'orientation': 'directed',
        }
        complex = SimplicialComplex.from_cache(simple_cache)

        # Should pass because vertex/spec/custom is a subtype of vertex/spec
        result = check_edge_endpoint_types(
            complex,
            'e:ver:sub',
            source_types=['vertex/doc'],
            target_types=['vertex/spec']  # Should match vertex/spec/custom
        )
        assert result is None

    def test_check_edge_endpoint_types_edge_not_found(self, simple_cache):
        """Non-existent edge should return violation."""
        complex = SimplicialComplex.from_cache(simple_cache)

        result = check_edge_endpoint_types(
            complex,
            'e:nonexistent',
            source_types=['vertex/doc'],
            target_types=['vertex/spec']
        )
        assert result is not None
        assert 'not found' in result.message

    # ========== check_vertex_degree tests ==========

    def test_check_vertex_degree_in_range(self, simple_cache):
        """Degree within range should pass."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # doc has 1 verification edge (out), which is within 0-1
        result = check_vertex_degree(
            complex,
            'v:doc:test',
            edge_type='verification',
            direction='out',
            min_degree=0,
            max_degree=1
        )
        assert result is None

    def test_check_vertex_degree_exceeds_max(self, simple_cache):
        """Degree exceeding max should fail."""
        # Add a second verification edge from same doc
        simple_cache['elements']['vertices']['v:spec:second'] = {
            'id': 'v:spec:second',
            'type': 'vertex/spec'
        }
        simple_cache['elements']['edges']['e:verification:second'] = {
            'id': 'e:verification:second',
            'type': 'edge/verification',
            'source': 'v:doc:test',
            'target': 'v:spec:second',
            'orientation': 'directed',
        }
        complex = SimplicialComplex.from_cache(simple_cache)

        # doc now has 2 verification edges, max is 1
        result = check_vertex_degree(
            complex,
            'v:doc:test',
            edge_type='verification',
            direction='out',
            min_degree=0,
            max_degree=1
        )
        assert result is not None
        assert result.rule_type == RuleType.DEGREE
        assert 'maximum is 1' in result.message

    def test_check_vertex_degree_below_min(self, simple_cache):
        """Degree below min should fail."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # doc has 0 qualifies edges, but we require at least 1
        result = check_vertex_degree(
            complex,
            'v:doc:test',
            edge_type='qualifies',
            direction='any',
            min_degree=1,
            max_degree=None
        )
        assert result is not None
        assert result.rule_type == RuleType.DEGREE
        assert 'minimum is 1' in result.message

    def test_check_vertex_degree_unlimited_max(self, simple_cache):
        """Unlimited max (None) should allow any count."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # doc has 1 verification edge, no max
        result = check_vertex_degree(
            complex,
            'v:doc:test',
            edge_type='verification',
            direction='out',
            min_degree=0,
            max_degree=None  # Unlimited
        )
        assert result is None

    def test_check_vertex_degree_direction_in(self, simple_cache):
        """Incoming edge direction should be counted correctly."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # spec has 1 incoming verification edge
        result = check_vertex_degree(
            complex,
            'v:spec:test',
            edge_type='verification',
            direction='in',
            min_degree=1,
            max_degree=1
        )
        assert result is None

    def test_check_vertex_degree_direction_any(self, simple_cache):
        """Any direction should count both in and out."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # spec has 1 coupling edge (undirected, so counted in 'any')
        result = check_vertex_degree(
            complex,
            'v:spec:test',
            edge_type='coupling',
            direction='any',
            min_degree=1,
            max_degree=1
        )
        assert result is None

    # ========== check_face_boundary_types tests ==========

    def test_check_face_boundary_types_all_present(self, simple_cache):
        """Face with all required edge types should pass."""
        complex = SimplicialComplex.from_cache(simple_cache)

        result = check_face_boundary_types(
            complex,
            'f:assurance:test',
            required_edge_types=['verification', 'validation', 'coupling']
        )
        assert result is None

    def test_check_face_boundary_types_missing_type(self, simple_cache):
        """Face missing a required edge type should fail."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # Assurance face doesn't have 'signs' edge
        result = check_face_boundary_types(
            complex,
            'f:assurance:test',
            required_edge_types=['verification', 'signs']  # 'signs' is missing
        )
        assert result is not None
        assert result.rule_type == RuleType.FACE_BOUNDARY
        assert 'Missing' in result.message
        assert 'edge/signs' in str(result.details['missing'])

    def test_check_face_boundary_types_with_prefix(self, simple_cache):
        """Edge types with edge/ prefix should work."""
        complex = SimplicialComplex.from_cache(simple_cache)

        result = check_face_boundary_types(
            complex,
            'f:assurance:test',
            required_edge_types=['edge/verification', 'edge/validation', 'edge/coupling']
        )
        assert result is None

    def test_check_face_boundary_types_face_not_found(self, simple_cache):
        """Non-existent face should return violation."""
        complex = SimplicialComplex.from_cache(simple_cache)

        result = check_face_boundary_types(
            complex,
            'f:nonexistent',
            required_edge_types=['verification']
        )
        assert result is not None
        assert 'no boundary' in result.message

    # ========== OntologyRule dataclass tests ==========

    def test_ontology_rule_creation(self):
        """OntologyRule dataclass should be properly created."""
        def dummy_check(complex, element_id):
            return None

        rule = OntologyRule(
            name="test_rule",
            element_type="edge/verification",
            dimension=1,
            check=dummy_check,
            strict=False,
            description="A test rule"
        )
        assert rule.name == "test_rule"
        assert rule.element_type == "edge/verification"
        assert rule.dimension == 1
        assert rule.strict is False

    def test_ontology_rule_invocation(self, simple_cache):
        """OntologyRule check function should be invokable."""
        complex = SimplicialComplex.from_cache(simple_cache)

        # Create a rule that uses check_edge_endpoint_types
        def verification_check(c, eid):
            return check_edge_endpoint_types(
                c, eid,
                source_types=['vertex/doc'],
                target_types=['vertex/spec']
            )

        rule = OntologyRule(
            name="verification_endpoints",
            element_type="edge/verification",
            dimension=1,
            check=verification_check,
            description="Verification edge must go from doc to spec"
        )

        # Apply the rule
        result = rule.check(complex, 'e:verification:test')
        assert result is None  # Should pass


# ========== Authorization Face Tests ==========

class TestAuthorizationBoundaryTypes:
    """Tests for authorization face boundary type constraints.

    Authorization face represents role-based access control:
    - Vertices: signer, role, guidance
    - Edges: has-role (signer → role), conveys (role → guidance), qualifies (signer → guidance)

    The qualifies edge is SHARED with signature faces, creating the chain:
    authorization → signature → assurance
    """

    @pytest.fixture
    def valid_authorization_cache(self):
        """Complete valid authorization face.

        Structure:
        - signer has role via has-role edge
        - role conveys authority to validate guidance via conveys edge
        - signer is qualified for guidance via qualifies edge (shared with signature)
        """
        return {
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
                        'signer': 'v:signer:alice',
                        'role': 'v:role:reviewer',
                        'guidance': 'v:guidance:test',
                        'qualifies_edge': 'e:qualifies:alice-guidance',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    @pytest.fixture
    def invalid_authorization_missing_conveys(self):
        """Authorization face missing conveys edge - INVALID."""
        return {
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
                    # Missing conveys edge!
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
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_valid_authorization_boundary(self, valid_authorization_cache):
        """Valid authorization face with all required edge types should pass."""
        engine = OntologyRuleEngine.from_cache(valid_authorization_cache)
        engine._check_authorization_boundary_types()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'authorization_boundary_types']
        assert len(boundary_violations) == 0

    def test_invalid_authorization_missing_conveys(self, invalid_authorization_missing_conveys):
        """Authorization face missing conveys edge should fail."""
        engine = OntologyRuleEngine.from_cache(invalid_authorization_missing_conveys)
        engine._check_authorization_boundary_types()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'authorization_boundary_types']
        assert len(boundary_violations) == 1
        assert 'conveys' in str(boundary_violations[0].details.get('missing', []))

    def test_authorization_alone_is_valid(self, valid_authorization_cache):
        """Authorization face can exist without signature face - role assignments pre-exist signing."""
        engine = OntologyRuleEngine.from_cache(valid_authorization_cache)
        violations = engine.check_all()

        # Should have no authorization-specific violations
        auth_violations = [v for v in violations
                          if 'authorization' in v.rule_name.lower()]
        assert len(auth_violations) == 0


class TestSignatureRequiresAuthorization:
    """Tests for signature face must have authorization face sharing qualifies edge.

    This establishes the chain: authorization → signature → assurance

    Key insight on directionality:
    - Authorization faces CAN exist without signature faces (role assignments pre-exist signing)
    - Signature faces CANNOT exist without authorization faces (you can't sign without authority)

    The shared qualifies edge ensures:
    - Every signature has role-based authority backing
    - The signer's qualification comes from their role in the authorization face
    """

    @pytest.fixture
    def valid_signature_with_authorization_cache(self):
        """Complete valid setup with authorization and signature faces sharing qualifies edge.

        Structure:
        - Authorization face: signer -- role -- guidance (has-role, conveys, qualifies)
        - Signature face: doc -- guidance -- signer (validation, qualifies, signs)
        - Both faces SHARE the qualifies edge (signer → guidance)
        """
        return {
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
            'statistics': {'vertices': 4, 'edges': 5, 'faces': 2}
        }

    @pytest.fixture
    def invalid_signature_no_authorization_cache(self):
        """Invalid setup: signature face exists but has no authorization face sharing qualifies edge.

        The signature face has a qualifies edge, but there's no authorization face
        that shares that same qualifies edge.
        """
        return {
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
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    @pytest.fixture
    def valid_authorization_without_signature_cache(self):
        """Valid setup: authorization face exists alone, no signature yet.

        This is VALID because authorization (role assignment) can pre-exist
        any signing activity.
        """
        return {
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
                    # Authorization face ALONE - no signature yet
                    'f:authorization:alice-reviewer': {
                        'id': 'f:authorization:alice-reviewer',
                        'type': 'face/authorization',
                        'vertices': ['v:signer:alice', 'v:role:reviewer', 'v:guidance:test'],
                        'edges': ['e:has-role:alice-reviewer', 'e:conveys:reviewer-guidance', 'e:qualifies:alice-guidance'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_valid_signature_with_authorization(self, valid_signature_with_authorization_cache):
        """Signature face with authorization face sharing qualifies edge should pass."""
        engine = OntologyRuleEngine.from_cache(valid_signature_with_authorization_cache)
        engine._check_signature_requires_authorization()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'signature_requires_authorization']
        assert len(adjacency_violations) == 0

    def test_invalid_signature_without_authorization(self, invalid_signature_no_authorization_cache):
        """Signature face without authorization face should fail."""
        engine = OntologyRuleEngine.from_cache(invalid_signature_no_authorization_cache)
        engine._check_signature_requires_authorization()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'signature_requires_authorization']
        assert len(adjacency_violations) == 1
        assert 'No authorization face shares qualifies edge' in adjacency_violations[0].message

    def test_valid_authorization_without_signature(self, valid_authorization_without_signature_cache):
        """Authorization face without signature face is VALID - role assignments can pre-exist signing."""
        engine = OntologyRuleEngine.from_cache(valid_authorization_without_signature_cache)
        engine._check_signature_requires_authorization()

        # No violations for signature-requires-authorization because there are no signature faces
        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'signature_requires_authorization']
        assert len(adjacency_violations) == 0

    def test_full_chain_authorization_signature_assurance(self):
        """Complete chain: authorization → signature → assurance should all pass."""
        cache = {
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
            'statistics': {'vertices': 5, 'edges': 7, 'faces': 3}
        }

        engine = OntologyRuleEngine.from_cache(cache)

        # Check authorization rules
        engine._check_authorization_boundary_types()
        auth_violations = [v for v in engine.violations if 'authorization' in v.rule_name]
        assert len(auth_violations) == 0, f"Authorization violations: {auth_violations}"

        # Check signature-requires-authorization
        engine._check_signature_requires_authorization()
        sig_auth_violations = [v for v in engine.violations if v.rule_name == 'signature_requires_authorization']
        assert len(sig_auth_violations) == 0, f"Signature-auth violations: {sig_auth_violations}"

        # Check assurance-requires-signature
        engine._check_assurance_requires_signature()
        assurance_violations = [v for v in engine.violations if v.rule_name == 'assurance_requires_signature']
        assert len(assurance_violations) == 0, f"Assurance-sig violations: {assurance_violations}"

    def test_full_ontology_check_includes_authorization_rules(self, valid_signature_with_authorization_cache):
        """Full ontology check should include authorization rule enforcement."""
        violations = check_ontology_rules(valid_signature_with_authorization_cache)

        # Should not have authorization or signature-requires-authorization violations
        auth_violations = [v for v in violations
                          if 'authorization' in v.rule_name.lower()]
        assert len(auth_violations) == 0


# ============================================================
# ARBAC97 ROLE ASSIGNMENT CHAIN TESTS
# (role-assignment → assignment-signature)
# ============================================================

class TestRoleAssignmentBoundaryTypes:
    """Test that role-assignment faces have correct edge types in their boundary.

    Role-assignment face: (actor, admin-role, target-role)
    Required edges: has-role, conveys, can-assign
    """

    @pytest.fixture
    def valid_role_assignment_cache(self):
        """Valid role-assignment face with correct boundary types."""
        return {
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
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    @pytest.fixture
    def invalid_role_assignment_missing_conveys_cache(self):
        """Invalid role-assignment face missing conveys edge."""
        return {
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
                    # Missing conveys, using 'other' instead
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
                        'edges': ['e:has-role:admin', 'e:other:placeholder', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_valid_role_assignment_boundary(self, valid_role_assignment_cache):
        """Valid role-assignment face should pass boundary type check."""
        engine = OntologyRuleEngine.from_cache(valid_role_assignment_cache)
        engine._check_role_assignment_boundary_types()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'role_assignment_boundary_types']
        assert len(boundary_violations) == 0

    def test_invalid_role_assignment_missing_conveys(self, invalid_role_assignment_missing_conveys_cache):
        """Role-assignment face missing conveys edge should fail."""
        engine = OntologyRuleEngine.from_cache(invalid_role_assignment_missing_conveys_cache)
        engine._check_role_assignment_boundary_types()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'role_assignment_boundary_types']
        assert len(boundary_violations) == 1
        assert 'conveys' in boundary_violations[0].message


class TestAssignmentSignatureBoundaryTypes:
    """Test that assignment-signature faces have correct edge types in their boundary.

    Assignment-signature face: (admin-signer, target-actor, target-role)
    Required edges: signs-assignment, has-role, can-assign
    """

    @pytest.fixture
    def valid_assignment_signature_cache(self):
        """Valid assignment-signature face with correct boundary types."""
        return {
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
                    'f:assignment-signature:bob': {
                        'id': 'f:assignment-signature:bob',
                        'type': 'face/assignment-signature',
                        'vertices': ['v:signer:admin', 'v:actor:bob', 'v:role:target-role'],
                        'edges': ['e:signs-assignment:admin-bob', 'e:has-role:bob-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                        'can_assign_edge': 'e:can-assign:admin-target',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    @pytest.fixture
    def invalid_assignment_signature_missing_signs_assignment_cache(self):
        """Invalid assignment-signature face missing signs-assignment edge."""
        return {
            'elements': {
                'vertices': {
                    'v:signer:admin': {'id': 'v:signer:admin', 'type': 'vertex/signer', 'name': 'Admin Signer'},
                    'v:actor:bob': {'id': 'v:actor:bob', 'type': 'vertex/actor', 'name': 'Bob'},
                    'v:role:target-role': {'id': 'v:role:target-role', 'type': 'vertex/role', 'name': 'Target Role'},
                },
                'edges': {
                    # Missing signs-assignment, using 'other' instead
                    'e:other:placeholder': {
                        'id': 'e:other:placeholder',
                        'type': 'edge/other',
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
                    'f:assignment-signature:bad': {
                        'id': 'f:assignment-signature:bad',
                        'type': 'face/assignment-signature',
                        'vertices': ['v:signer:admin', 'v:actor:bob', 'v:role:target-role'],
                        'edges': ['e:other:placeholder', 'e:has-role:bob-target', 'e:can-assign:admin-target'],
                        'orientation': 'oriented',
                    },
                },
            },
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_valid_assignment_signature_boundary(self, valid_assignment_signature_cache):
        """Valid assignment-signature face should pass boundary type check."""
        engine = OntologyRuleEngine.from_cache(valid_assignment_signature_cache)
        engine._check_assignment_signature_boundary_types()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'assignment_signature_boundary_types']
        assert len(boundary_violations) == 0

    def test_invalid_assignment_signature_missing_signs_assignment(self, invalid_assignment_signature_missing_signs_assignment_cache):
        """Assignment-signature face missing signs-assignment edge should fail."""
        engine = OntologyRuleEngine.from_cache(invalid_assignment_signature_missing_signs_assignment_cache)
        engine._check_assignment_signature_boundary_types()

        boundary_violations = [v for v in engine.violations
                              if v.rule_name == 'assignment_signature_boundary_types']
        assert len(boundary_violations) == 1
        assert 'signs-assignment' in boundary_violations[0].message


class TestAssignmentSignatureRequiresRoleAssignment:
    """Test that assignment-signature faces require role-assignment faces sharing can-assign edge.

    This is the ARBAC97 pattern: role-assignment → assignment-signature
    """

    @pytest.fixture
    def valid_assignment_signature_with_role_assignment_cache(self):
        """Assignment-signature face with role-assignment face sharing can-assign edge."""
        return {
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
                    # SHARED can-assign edge
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
            'statistics': {'vertices': 4, 'edges': 5, 'faces': 2}
        }

    @pytest.fixture
    def invalid_assignment_signature_no_role_assignment_cache(self):
        """Assignment-signature face without role-assignment face - invalid."""
        return {
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
                    # Assignment-signature WITHOUT role-assignment
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
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    @pytest.fixture
    def valid_role_assignment_without_assignment_signature_cache(self):
        """Role-assignment face without assignment-signature - valid (authority pre-exists)."""
        return {
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
                    # Role-assignment alone - this is VALID
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
            'statistics': {'vertices': 3, 'edges': 3, 'faces': 1}
        }

    def test_valid_assignment_signature_with_role_assignment(self, valid_assignment_signature_with_role_assignment_cache):
        """Assignment-signature with role-assignment sharing can-assign edge should pass."""
        engine = OntologyRuleEngine.from_cache(valid_assignment_signature_with_role_assignment_cache)
        engine._check_assignment_signature_requires_role_assignment()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assignment_signature_requires_role_assignment']
        assert len(adjacency_violations) == 0

    def test_invalid_assignment_signature_without_role_assignment(self, invalid_assignment_signature_no_role_assignment_cache):
        """Assignment-signature without role-assignment should fail."""
        engine = OntologyRuleEngine.from_cache(invalid_assignment_signature_no_role_assignment_cache)
        engine._check_assignment_signature_requires_role_assignment()

        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assignment_signature_requires_role_assignment']
        assert len(adjacency_violations) == 1
        assert 'No role-assignment face shares can-assign edge' in adjacency_violations[0].message

    def test_valid_role_assignment_without_assignment_signature(self, valid_role_assignment_without_assignment_signature_cache):
        """Role-assignment without assignment-signature is VALID - authority can pre-exist assignments."""
        engine = OntologyRuleEngine.from_cache(valid_role_assignment_without_assignment_signature_cache)
        engine._check_assignment_signature_requires_role_assignment()

        # No violations because there are no assignment-signature faces
        adjacency_violations = [v for v in engine.violations
                               if v.rule_name == 'assignment_signature_requires_role_assignment']
        assert len(adjacency_violations) == 0

    def test_full_ontology_check_includes_role_assignment_rules(self, valid_assignment_signature_with_role_assignment_cache):
        """Full ontology check should include role assignment rule enforcement."""
        violations = check_ontology_rules(valid_assignment_signature_with_role_assignment_cache)

        # Should not have role-assignment or assignment-signature violations
        role_assign_violations = [v for v in violations
                                 if 'role_assignment' in v.rule_name.lower() or 'assignment_signature' in v.rule_name.lower()]
        assert len(role_assign_violations) == 0
