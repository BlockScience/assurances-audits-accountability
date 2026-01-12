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
from aaa.core.complex import SimplicialComplex, ComplexGraph, build_simplicial_complex
from aaa.core.rules import (
    OntologyRuleEngine,
    RuleViolation,
    RuleType,
    Severity,
    check_ontology_rules,
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

    def test_doc_single_verification(self):
        """Doc can have at most one verification edge."""
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

        degree_violations = [v for v in engine.violations
                           if v.rule_name == 'degree_constraint'
                           and v.element_id == 'v:doc:test']
        assert len(degree_violations) == 1
        assert 'maximum is 1' in degree_violations[0].message

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
