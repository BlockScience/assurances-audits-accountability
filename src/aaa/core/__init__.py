"""
AAA Core Module

This module provides the core functionality for the AAA (Assurances, Audits, Accountability)
framework. It provides parsing, verification, caching, auditing, and topology analysis
for knowledge complex documents.

All functionality is self-contained within the package - no external dependencies
on repository structure.
"""

# Re-export key classes and functions from submodules
from .parse import (
    ParseError,
    extract_frontmatter,
    parse_element,
    parse_vertex,
    parse_edge,
    parse_face,
    parse_chart,
    parse_directory,
)

from .template_parser import (
    TemplateParser,
    TemplateSpec,
    TemplateRequirement,
)

from .verifier import (
    TemplateBasedVerifier,
)

from .cache import (
    build_cache,
    calculate_euler_characteristic,
    sanitize_for_json,
)

from .audit import (
    audit_assurance_chart,
    format_audit_trail,
    is_document_vertex,
    check_invariant,
    check_assurance_coverage,
    BOUNDARY_COMPLEX,
)

from .topology import (
    find_holes,
    find_potential_faces,
    load_cache,
)

from .accountability import (
    AccountabilityError,
    check_validation_edge_accountability,
    check_shared_validation_edge_consistency,
    check_all_signature_accountability,
    get_accountable_party_from_edge,
    usernames_match,
)

from .resources import (
    get_bundled_templates_path,
    get_bundled_foundation_path,
    get_templates_path,
)

from .complex import (
    SimplicialComplex,
    ComplexGraph,  # backwards compatibility alias
    TypedVertex,
    TypedEdge,
    TypedFace,
    build_simplicial_complex,
    build_complex_graph,  # backwards compatibility alias
    # Topology rules
    TopologyViolation,
    check_edge_valid_boundary,
    check_face_valid_boundary,
    check_face_closure,
    check_topology,
)

from .rules import (
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

# Backwards compatibility alias
audit_chart = audit_assurance_chart

__all__ = [
    # Parse
    'ParseError',
    'extract_frontmatter',
    'parse_element',
    'parse_vertex',
    'parse_edge',
    'parse_face',
    'parse_chart',
    'parse_directory',
    # Template Parser
    'TemplateParser',
    'TemplateSpec',
    'TemplateRequirement',
    # Verifier
    'TemplateBasedVerifier',
    # Cache
    'build_cache',
    'calculate_euler_characteristic',
    'sanitize_for_json',
    # Audit
    'audit_assurance_chart',
    'audit_chart',  # backwards compatibility
    'format_audit_trail',
    'is_document_vertex',
    'check_invariant',
    'check_assurance_coverage',
    'BOUNDARY_COMPLEX',
    # Topology
    'find_holes',
    'find_potential_faces',
    'load_cache',
    # Accountability
    'AccountabilityError',
    'check_validation_edge_accountability',
    'check_shared_validation_edge_consistency',
    'check_all_signature_accountability',
    'get_accountable_party_from_edge',
    'usernames_match',
    # Resources
    'get_bundled_templates_path',
    'get_bundled_foundation_path',
    'get_templates_path',
    # Simplicial Complex
    'SimplicialComplex',
    'ComplexGraph',  # backwards compatibility alias
    'TypedVertex',
    'TypedEdge',
    'TypedFace',
    'build_simplicial_complex',
    'build_complex_graph',  # backwards compatibility alias
    # Topology Rules
    'TopologyViolation',
    'check_edge_valid_boundary',
    'check_face_valid_boundary',
    'check_face_closure',
    'check_topology',
    # Ontology Rules (Type Verification)
    'OntologyRuleEngine',
    'OntologyRule',
    'RuleViolation',
    'RuleType',
    'Severity',
    'check_ontology_rules',
    # Local Rule Functions
    'check_edge_endpoint_types',
    'check_vertex_degree',
    'check_face_boundary_types',
]
