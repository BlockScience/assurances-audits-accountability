"""
Ontology rule enforcement engine.

This module enforces the local rules defined in the ontology. Local rules are
type constraints layered on top of topological structure. They cannot weaken
topological rules (e.g., faces must have 3 edges) but can add type-specific
constraints (e.g., verification edges must go from doc to spec).

TOPOLOGY vs ONTOLOGY:
- Topology: Structural rules of simplicial complexes. A face has 3 edges,
  edges have 2 vertices, charts form valid simplicial complexes.
- Ontology: Type system with local rules. Types define what edges can connect
  to what vertices, what faces must be adjacent, degree constraints, etc.

LOCAL + UNIVERSAL PATTERN:
Each ontology rule is:
1. LOCAL: It only inspects an element and its boundary/coboundary
2. UNIVERSAL: It applies to all elements of a particular type

This makes rules compositional - checking locally guarantees global coherence.

This module implements ontology verification (deterministic type checking),
NOT validation (human judgment of fitness for purpose).
"""

from typing import Dict, Any, List, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum

from .complex import SimplicialComplex, ComplexGraph, build_simplicial_complex, build_complex_graph


class RuleType(Enum):
    """Types of ontology rules."""
    DEGREE = "degree"           # Vertex degree constraints
    EDGE_ENDPOINT = "edge-endpoint"  # Edge source/target type constraints
    FACE_BOUNDARY = "face-boundary"  # Face must have valid boundary
    FACE_ADJACENCY = "face-adjacency"  # Faces must share specific edges
    STAR = "star"               # Constraints on vertex neighborhood


class Severity(Enum):
    """Rule violation severity."""
    ERROR = "error"      # Must be fixed
    WARNING = "warning"  # Should be reviewed


@dataclass
class RuleViolation:
    """A single rule violation."""
    rule_name: str
    rule_type: RuleType
    severity: Severity
    element_id: str
    element_type: str  # 'vertex', 'edge', 'face'
    message: str
    details: Optional[Dict[str, Any]] = None

    def __str__(self) -> str:
        return f"[{self.severity.value.upper()}] {self.rule_name}: {self.message} ({self.element_id})"


# ========== Local Rule Functions ==========
#
# Each rule function follows the LOCAL pattern:
# - Takes (complex, element_id) as arguments
# - Only inspects the element and its boundary/coboundary
# - Returns Optional[RuleViolation] (None if passes)
#
# Rules are applied UNIVERSALLY to all elements of matching types.

def check_edge_endpoint_types(
    complex: SimplicialComplex,
    edge_id: str,
    source_types: List[str],
    target_types: List[str],
    rule_name: str = "edge_endpoint_type"
) -> Optional[RuleViolation]:
    """
    Check that an edge's endpoints match allowed types.

    This is a LOCAL rule - it only inspects the edge's boundary vertices.

    Args:
        complex: The simplicial complex
        edge_id: Edge to check
        source_types: Allowed vertex type prefixes for source
        target_types: Allowed vertex type prefixes for target
        rule_name: Name for violation reporting

    Returns:
        RuleViolation if endpoints don't match, None otherwise
    """
    edge = complex.get_edge(edge_id)
    if edge is None:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.EDGE_ENDPOINT,
            severity=Severity.ERROR,
            element_id=edge_id,
            element_type="edge",
            message=f"Edge {edge_id} not found",
            details={'edge_id': edge_id}
        )

    # Get edge type for error messages
    edge_type = edge.type.replace('edge/', '') if edge.type.startswith('edge/') else edge.type

    endpoint_types = complex.get_edge_endpoint_types(edge_id)
    if endpoint_types is None:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.EDGE_ENDPOINT,
            severity=Severity.ERROR,
            element_id=edge_id,
            element_type="edge",
            message=f"Edge {edge_id} has no endpoint types",
            details={'edge_id': edge_id, 'edge_type': edge_type}
        )

    source_type, target_type = endpoint_types

    # Check source type matches any allowed prefix
    source_matches = any(
        source_type == allowed or source_type.startswith(f"{allowed}/")
        for allowed in source_types
    )
    if not source_matches:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.EDGE_ENDPOINT,
            severity=Severity.ERROR,
            element_id=edge_id,
            element_type="edge",
            message=f"Source vertex type '{source_type}' not allowed for {edge_type} edge",
            details={
                'edge_type': edge_type,
                'source_type': source_type,
                'allowed_source_types': source_types
            }
        )

    # Check target type matches any allowed prefix
    target_matches = any(
        target_type == allowed or target_type.startswith(f"{allowed}/")
        for allowed in target_types
    )
    if not target_matches:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.EDGE_ENDPOINT,
            severity=Severity.ERROR,
            element_id=edge_id,
            element_type="edge",
            message=f"Target vertex type '{target_type}' not allowed for {edge_type} edge",
            details={
                'edge_type': edge_type,
                'target_type': target_type,
                'allowed_target_types': target_types
            }
        )

    return None


def check_vertex_degree(
    complex: SimplicialComplex,
    vertex_id: str,
    edge_type: str,
    direction: str,  # 'in', 'out', 'any'
    min_degree: int,
    max_degree: Optional[int],
    rule_name: str = "vertex_degree"
) -> Optional[RuleViolation]:
    """
    Check that a vertex has the required degree for edges of a type.

    This is a LOCAL rule - it only inspects the vertex's coboundary edges.

    Args:
        complex: The simplicial complex
        vertex_id: Vertex to check
        edge_type: Edge type to count
        direction: 'in', 'out', or 'any'
        min_degree: Minimum required degree
        max_degree: Maximum allowed degree (None = unlimited)
        rule_name: Name for violation reporting

    Returns:
        RuleViolation if degree constraint violated, None otherwise
    """
    if direction == 'out':
        count = complex.out_degree(vertex_id, edge_type)
    elif direction == 'in':
        count = complex.in_degree(vertex_id, edge_type)
    else:  # 'any'
        count = complex.degree(vertex_id, edge_type)

    if count < min_degree:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.DEGREE,
            severity=Severity.ERROR,
            element_id=vertex_id,
            element_type="vertex",
            message=f"Has {count} {edge_type} edges ({direction}), minimum is {min_degree}",
            details={
                'edge_type': edge_type,
                'direction': direction,
                'actual': count,
                'min': min_degree,
                'max': max_degree
            }
        )

    if max_degree is not None and count > max_degree:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.DEGREE,
            severity=Severity.ERROR,
            element_id=vertex_id,
            element_type="vertex",
            message=f"Has {count} {edge_type} edges ({direction}), maximum is {max_degree}",
            details={
                'edge_type': edge_type,
                'direction': direction,
                'actual': count,
                'min': min_degree,
                'max': max_degree
            }
        )

    return None


def check_face_boundary_types(
    complex: SimplicialComplex,
    face_id: str,
    required_edge_types: List[str],
    rule_name: str = "face_boundary_types"
) -> Optional[RuleViolation]:
    """
    Check that a face's boundary contains edges of required types.

    This is a LOCAL rule - it only inspects the face's boundary edges.

    Args:
        complex: The simplicial complex
        face_id: Face to check
        required_edge_types: Edge types that must be in the boundary
        rule_name: Name for violation reporting

    Returns:
        RuleViolation if required types missing, None otherwise
    """
    boundary_types = complex.get_face_boundary_types(face_id)
    if boundary_types is None:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.FACE_BOUNDARY,
            severity=Severity.ERROR,
            element_id=face_id,
            element_type="face",
            message=f"Face {face_id} has no boundary",
            details={'face_id': face_id}
        )

    # Normalize required types (handle edge/ prefix)
    normalized_required = set()
    for t in required_edge_types:
        if t.startswith('edge/'):
            normalized_required.add(t)
        else:
            normalized_required.add(f"edge/{t}")

    # Check each required type is present
    missing = normalized_required - boundary_types
    if missing:
        return RuleViolation(
            rule_name=rule_name,
            rule_type=RuleType.FACE_BOUNDARY,
            severity=Severity.ERROR,
            element_id=face_id,
            element_type="face",
            message=f"Missing required edge types: {missing}",
            details={
                'required': list(normalized_required),
                'actual': list(boundary_types),
                'missing': list(missing)
            }
        )

    return None


@dataclass
class OntologyRule:
    """
    A local ontology rule applied universally to elements of a type.

    Each rule:
    - Targets elements of a specific type
    - Uses a local check function that only inspects boundary/coboundary
    - Is applied to all matching elements universally
    """
    name: str
    element_type: str  # e.g., 'edge/verification', 'face/assurance', 'vertex/doc'
    dimension: int  # 0=vertex, 1=edge, 2=face
    check: Callable[[SimplicialComplex, str], Optional[RuleViolation]]
    strict: bool = False  # If True, only exact type match; else includes subtypes
    description: str = ""


class OntologyRuleEngine:
    """
    Enforces ontology local rules on a knowledge complex.

    Rules are from ontology-base.md:
    1. Vertex degree constraints
    2. Module qualification cascade
    3. Signature face requires guidance qualification
    4. Module-signature shares edge with signature
    5. Signature shares edge with assurance
    6. Assurance requires b2 anchor
    7. Output satisfaction requires output type
    8. Input satisfaction requires input type
    9. Edge endpoint type compliance
    10. Face boundary closure
    11. Authorization chain validity
    12. Runbook module ordering (DAG)
    13. Runbook I/O chaining
    14. Execution trace DAG requirement
    15. Execution causal chain
    """

    # Edge endpoint type constraints from ontology
    # Format: edge_type -> (source_types, target_types)
    # source_types/target_types are lists of allowed vertex type prefixes
    EDGE_ENDPOINT_CONSTRAINTS = {
        'verification': (['vertex/doc', 'vertex/spec', 'vertex/guidance', 'vertex/module', 'vertex/ontology'],
                        ['vertex/spec']),
        'validation': (['vertex/doc', 'vertex/spec', 'vertex/guidance', 'vertex/ontology'],
                      ['vertex/guidance']),
        'coupling': (['vertex/spec'], ['vertex/guidance']),
        # signs/qualifies: only actual signers can sign/qualify (b0 cannot sign)
        'signs': (['vertex/signer'], ['vertex/doc', 'vertex/spec', 'vertex/guidance', 'vertex/ontology']),
        'qualifies': (['vertex/signer'], ['vertex/guidance', 'vertex/module']),
        # has-role: actor or signer (signer extends actor) holds a role
        'has-role': (['vertex/actor', 'vertex/signer'], ['vertex/role']),
        # conveys: role grants permission to sign validations against a guidance,
        # or grants authority to assign another role (ARBAC97 can_assign)
        # Target types:
        # - guidance: authority to validate against this guidance
        # - role: authority to assign this role (ARBAC97)
        # - permission: generic permission (NIST RBAC PA)
        # (NIST RBAC: Permission Assignment)
        'conveys': (['vertex/role'], ['vertex/guidance', 'vertex/role', 'vertex/permission']),
        'requires-permission': (['vertex/action'], ['vertex/permission']),
        # ARBAC97 role assignment edges (signer extends actor)
        'can-assign': (['vertex/actor', 'vertex/signer'], ['vertex/role']),
        'signs-assignment': (['vertex/signer'], ['vertex/actor']),
        'precedes': (['vertex/module'], ['vertex/module']),
        'feeds': (['vertex/doc'], ['vertex/module']),
        'yields': (['vertex/module'], ['vertex/doc']),
        'consumes': (['vertex/execution'], ['vertex/doc']),
        'produces': (['vertex/execution'], ['vertex/doc']),
        'executes': (['vertex/execution'], ['vertex/module']),
        'follows': (['vertex/execution'], ['vertex/execution']),
        # Type hierarchy edges
        'inherits': (['vertex/spec'], ['vertex/spec']),
        'instantiates': (['vertex/doc'], ['vertex/spec']),
    }

    # Degree constraints from ontology
    # Format: (vertex_type_prefix, edge_type, direction) -> (min, max)
    # direction: 'out', 'in', 'any'
    # max=None means unlimited
    #
    # NOTE: doc verification/validation degree constraints are NOT enforced here because:
    # - Documents can have multiple types through inheritance
    # - Each inherited type allows ONE verification edge and ONE validation edge
    # - E.g., vertex/doc/persona inherits from 'persona' AND 'doc', so it can have:
    #   - verification → spec/persona AND verification → spec/doc
    #   - validation → guidance/persona AND validation → guidance/doc
    # - The constraint is "0..n where n = number of inherited types", not a fixed max
    DEGREE_CONSTRAINTS = {
        ('vertex/spec', 'coupling', 'any'): (1, 1),
        ('vertex/guidance', 'coupling', 'any'): (1, 1),
        ('vertex/module', 'input', 'in'): (1, None),
        ('vertex/module', 'output', 'out'): (1, None),
    }

    def __init__(self, graph: ComplexGraph):
        """
        Initialize rule engine with a typed graph.

        Args:
            graph: ComplexGraph built from cache
        """
        self.graph = graph
        self.violations: List[RuleViolation] = []

    @classmethod
    def from_cache(cls, cache: Dict[str, Any]) -> 'OntologyRuleEngine':
        """Create rule engine from cache data."""
        graph = build_complex_graph(cache)
        return cls(graph)

    def check_all(self) -> List[RuleViolation]:
        """
        Run all ontology rule checks.

        Returns:
            List of all rule violations found
        """
        self.violations = []

        # Core type constraints
        self._check_edge_endpoint_constraints()
        self._check_degree_constraints()
        self._check_face_boundary_closure()

        # Authorization rules (authorization → signature → assurance chain)
        self._check_authorization_boundary_types()
        self._check_signature_requires_authorization()

        # Role assignment rules (role-assignment → assignment-signature chain)
        self._check_role_assignment_boundary_types()
        self._check_assignment_signature_boundary_types()
        self._check_assignment_signature_requires_role_assignment()

        # Signature and assurance rules
        self._check_signature_requires_qualification()
        self._check_signature_shares_edge_with_assurance()
        self._check_documents_have_assurance()

        # Module rules
        self._check_module_qualification_cascade()
        self._check_module_signature_shares_edge()

        # Satisfaction rules
        self._check_input_satisfaction_requires_input_type()
        self._check_output_satisfaction_requires_output_type()

        # DAG requirements
        self._check_execution_trace_dag()
        self._check_runbook_module_ordering()

        # Chaining rules
        self._check_runbook_io_chaining()
        self._check_execution_causal_chain()

        return self.violations

    def _add_violation(
        self,
        rule_name: str,
        rule_type: RuleType,
        severity: Severity,
        element_id: str,
        element_type: str,
        message: str,
        details: Optional[Dict[str, Any]] = None
    ):
        """Add a rule violation."""
        self.violations.append(RuleViolation(
            rule_name=rule_name,
            rule_type=rule_type,
            severity=severity,
            element_id=element_id,
            element_type=element_type,
            message=message,
            details=details
        ))

    # ========== Edge Endpoint Type Compliance (Rule 9) ==========

    def _check_edge_endpoint_constraints(self):
        """
        Check that edge endpoints match type constraints.

        Rule: Edge source and target must match type constraints defined
        for that edge type in the ontology.

        Uses LOCAL pattern: For each edge, only inspects its boundary vertices.
        """
        for edge_id, edge in self.graph.edges.items():
            # Extract base edge type
            edge_type = edge.type.replace('edge/', '') if edge.type.startswith('edge/') else edge.type

            if edge_type not in self.EDGE_ENDPOINT_CONSTRAINTS:
                continue  # Unknown edge type - skip (might be app-specific)

            source_types, target_types = self.EDGE_ENDPOINT_CONSTRAINTS[edge_type]

            # Use the local rule function
            violation = check_edge_endpoint_types(
                self.graph,
                edge_id,
                source_types,
                target_types,
                rule_name="edge_endpoint_type_compliance"
            )
            if violation:
                self.violations.append(violation)

    def _type_matches_any(self, actual_type: str, allowed_types: List[str]) -> bool:
        """Check if actual type matches any of the allowed type prefixes."""
        for allowed in allowed_types:
            if actual_type == allowed or actual_type.startswith(f"{allowed}/"):
                return True
        return False

    # ========== Degree Constraints (Rules 1-7) ==========

    def _check_degree_constraints(self):
        """
        Check vertex degree constraints.

        Rule: Vertices of certain types have min/max constraints on
        incident edges of specific types.

        Uses LOCAL pattern: For each vertex, only inspects its coboundary edges.
        """
        for vid, vertex in self.graph.vertices.items():
            for (vertex_type_prefix, edge_type, direction), (min_deg, max_deg) in self.DEGREE_CONSTRAINTS.items():
                # Check if this vertex matches the constraint's vertex type
                if not (vertex.type == vertex_type_prefix or vertex.type.startswith(f"{vertex_type_prefix}/")):
                    continue

                # Use the local rule function
                violation = check_vertex_degree(
                    self.graph,
                    vid,
                    edge_type,
                    direction,
                    min_deg,
                    max_deg,
                    rule_name="degree_constraint"
                )
                if violation:
                    self.violations.append(violation)

    # ========== Face Boundary Closure (Rule 10) ==========

    def _check_face_boundary_closure(self):
        """
        Check that face boundaries form closed triangles.

        Rule: Face boundary edges must form a closed triangle
        connecting exactly three vertices.

        Note: This is technically a topological rule, but we check it
        here for completeness since the ontology specifies it.
        """
        for fid, face in self.graph.faces.items():
            # Must have exactly 3 vertices
            if len(face.vertices) != 3:
                self._add_violation(
                    rule_name="face_boundary_closure",
                    rule_type=RuleType.FACE_BOUNDARY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"Face has {len(face.vertices)} vertices, must have exactly 3",
                    details={'vertices': face.vertices}
                )
                continue

            # Must have exactly 3 edges
            if len(face.edges) != 3:
                self._add_violation(
                    rule_name="face_boundary_closure",
                    rule_type=RuleType.FACE_BOUNDARY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"Face has {len(face.edges)} boundary edges, must have exactly 3",
                    details={'edges': face.edges}
                )
                continue

            # Check that edges connect the vertices
            edge_vertices = set()
            for eid in face.edges:
                edge = self.graph.get_edge(eid)
                if edge:
                    edge_vertices.add(edge.source)
                    edge_vertices.add(edge.target)

            face_vertex_set = set(face.vertices)
            if edge_vertices != face_vertex_set:
                self._add_violation(
                    rule_name="face_boundary_closure",
                    rule_type=RuleType.FACE_BOUNDARY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Face boundary edges don't connect the face's vertices",
                    details={
                        'face_vertices': list(face_vertex_set),
                        'edge_vertices': list(edge_vertices)
                    }
                )

    # ========== Signature Requires Qualification (Rule 3) ==========

    def _check_signature_requires_qualification(self):
        """
        Check that signature faces have required qualifies edge.

        Rule: f:signature:(doc, guidance, signer) requires
        qualifies(signer, guidance) in signer's star.
        """
        for fid in self.graph.get_faces_by_type('signature'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Extract signer and guidance from face data
            signer_id = face.data.get('signer')
            guidance_id = face.data.get('guidance')

            if not signer_id or not guidance_id:
                self._add_violation(
                    rule_name="signature_requires_qualification",
                    rule_type=RuleType.STAR,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Signature face missing signer or guidance field",
                    details={'signer': signer_id, 'guidance': guidance_id}
                )
                continue

            # Check for qualifies edge from signer to guidance
            has_qualifies = self.graph.edge_exists(signer_id, guidance_id, 'qualifies')

            if not has_qualifies:
                self._add_violation(
                    rule_name="signature_requires_qualification",
                    rule_type=RuleType.STAR,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"Signer '{signer_id}' lacks qualifies edge to guidance '{guidance_id}'",
                    details={'signer': signer_id, 'guidance': guidance_id}
                )

    # ========== Assurance Requires Signature (Rule 5) ==========

    def _check_assurance_requires_signature(self):
        """
        Check that assurance faces have a signature face sharing their validation edge.

        Rule: f:assurance: must have f:signature: sharing e:validation: edge.

        Key insight: Signature faces CAN exist without assurance faces (they represent
        a signer's approval of a validation, which may pre-exist the assurance).
        But assurance faces CANNOT exist without a corresponding signature - every
        assurance requires human accountability via a signed validation.
        """
        for fid in self.graph.get_faces_by_type('assurance'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            validation_edge_id = face.data.get('validation_edge')
            if not validation_edge_id:
                # Try to find validation edge in boundary
                for eid in face.edges:
                    if self.graph._edge_matches_type(eid, 'validation'):
                        validation_edge_id = eid
                        break

            if not validation_edge_id:
                self._add_violation(
                    rule_name="assurance_requires_signature",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Assurance face has no validation edge in boundary",
                    details={'edges': face.edges}
                )
                continue

            # Check if any signature face shares this validation edge
            signature_faces = self.graph.get_faces_containing_edge(validation_edge_id, 'signature')

            if not signature_faces:
                self._add_violation(
                    rule_name="assurance_requires_signature",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"No signature face shares validation edge '{validation_edge_id}' - assurance requires human sign-off",
                    details={'validation_edge': validation_edge_id}
                )

    # Legacy alias for backward compatibility
    def _check_signature_shares_edge_with_assurance(self):
        """Backward compatibility alias - calls _check_assurance_requires_signature."""
        self._check_assurance_requires_signature()

    # ========== Documents Have Assurance ==========

    def _check_documents_have_assurance(self):
        """
        Check that all document vertices have assurance faces.

        Rule: Every document vertex (spec, guidance, ontology, doc, module) must
        have an assurance face (f:assurance: or f:b2:) where it is the target.

        Note: Actor vertices (signer, role, etc.) are governed by RBAC rules,
        not V&V assurance. The b0:root vertex is also exempt.
        """
        # Document types that require assurance
        doc_types = {'vertex/doc', 'vertex/spec', 'vertex/guidance',
                     'vertex/ontology', 'vertex/module'}

        # Get all assurance and b2 faces
        assurance_faces = set(self.graph.get_faces_by_type('assurance'))
        b2_faces = set(self.graph.get_faces_by_type('b2'))
        all_assurance_faces = assurance_faces | b2_faces

        # Build set of assured document IDs (targets of assurance faces)
        assured_docs = set()
        for fid in all_assurance_faces:
            face = self.graph.get_face(fid)
            if face:
                target = face.data.get('target')
                if target:
                    assured_docs.add(target)

        # Check each document vertex
        for vid in self.graph.get_all_vertices():
            vertex = self.graph.get_vertex(vid)
            if not vertex:
                continue

            # Check if this is a document type
            vtype = vertex.type
            is_doc = any(vtype == dt or vtype.startswith(dt + '/') for dt in doc_types)

            if is_doc and vid not in assured_docs:
                self._add_violation(
                    rule_name="documents_have_assurance",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.WARNING,
                    element_id=vid,
                    element_type="vertex",
                    message=f"Document vertex has no assurance face (assurance or b2)",
                    details={'vertex_type': vtype, 'assured_docs': list(assured_docs)}
                )

    # ========== Authorization Face Boundary Types ==========

    def _check_authorization_boundary_types(self):
        """
        Check that authorization faces have required edge types in boundary.

        Rule: f:authorization:(signer, role, guidance) must have:
        - e:has-role: (signer → role)
        - e:conveys: (role → guidance)
        - e:qualifies: (signer → guidance) - SHARED with signature face

        The authorization face proves WHY a signer is qualified: they hold a role
        that conveys authority to validate against the guidance.
        """
        for fid in self.graph.get_faces_by_type('authorization'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Check for required edge types in boundary
            edge_types_found = set()
            for eid in face.edges:
                edge = self.graph.get_edge(eid)
                if edge:
                    edge_type = edge.type.replace('edge/', '') if edge.type.startswith('edge/') else edge.type
                    edge_types_found.add(edge_type)

            required_types = {'has-role', 'conveys', 'qualifies'}
            missing = required_types - edge_types_found

            if missing:
                self._add_violation(
                    rule_name="authorization_boundary_types",
                    rule_type=RuleType.FACE_BOUNDARY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"Authorization face missing required edge types: {missing}",
                    details={
                        'required': list(required_types),
                        'found': list(edge_types_found),
                        'missing': list(missing)
                    }
                )

    # ========== Signature Requires Authorization (Face Adjacency) ==========

    def _check_signature_requires_authorization(self):
        """
        Check that signature faces have an authorization face sharing their qualifies edge.

        Rule: f:signature: must have f:authorization: sharing e:qualifies: edge.

        This establishes the chain: authorization → signature → assurance

        Key insight: Authorization faces CAN exist without signature faces (role
        assignments pre-exist any signing activity). But signature faces CANNOT
        exist without authorization faces - you can't sign unless you have proper
        authority via your role.

        The shared edge is 'qualifies' (signer → guidance), which appears in both:
        - Authorization face: proves the signer has authority via their role
        - Signature face: uses that authority to sign a validation
        """
        for fid in self.graph.get_faces_by_type('signature'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Find qualifies edge in boundary
            qualifies_edge_id = face.data.get('qualifies_edge')
            if not qualifies_edge_id:
                # Try to find qualifies edge in boundary
                for eid in face.edges:
                    if self.graph._edge_matches_type(eid, 'qualifies'):
                        qualifies_edge_id = eid
                        break

            if not qualifies_edge_id:
                self._add_violation(
                    rule_name="signature_requires_authorization",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Signature face has no qualifies edge in boundary",
                    details={'edges': face.edges}
                )
                continue

            # Check if any authorization face shares this qualifies edge
            authorization_faces = self.graph.get_faces_containing_edge(qualifies_edge_id, 'authorization')

            if not authorization_faces:
                self._add_violation(
                    rule_name="signature_requires_authorization",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"No authorization face shares qualifies edge '{qualifies_edge_id}' - signer must have role-based authority",
                    details={'qualifies_edge': qualifies_edge_id}
                )

    # ========== Role Assignment Boundary Types (ARBAC97) ==========

    def _check_role_assignment_boundary_types(self):
        """
        Check that role-assignment faces have required edge types in boundary.

        Rule: f:role-assignment:(actor, admin-role, target-role) must have:
        - e:has-role: (actor → admin-role)
        - e:conveys: (admin-role → target-role)
        - e:can-assign: (actor → target-role)

        The role-assignment face proves WHY an actor can assign a role: they hold
        an admin-role that conveys authority to assign the target role.
        """
        for fid in self.graph.get_faces_by_type('role-assignment'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Check for required edge types in boundary
            edge_types_found = set()
            for eid in face.edges:
                edge = self.graph.get_edge(eid)
                if edge:
                    edge_type = edge.type.replace('edge/', '') if edge.type.startswith('edge/') else edge.type
                    edge_types_found.add(edge_type)

            required_types = {'has-role', 'conveys', 'can-assign'}
            missing = required_types - edge_types_found

            if missing:
                self._add_violation(
                    rule_name="role_assignment_boundary_types",
                    rule_type=RuleType.FACE_BOUNDARY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"Role-assignment face missing required edge types: {missing}",
                    details={
                        'required': list(required_types),
                        'found': list(edge_types_found),
                        'missing': list(missing)
                    }
                )

    # ========== Assignment Signature Boundary Types (ARBAC97) ==========

    def _check_assignment_signature_boundary_types(self):
        """
        Check that assignment-signature faces have required edge types in boundary.

        Rule: f:assignment-signature:(admin-signer, target-actor, role) must have:
        - e:signs-assignment: (admin-signer → target-actor)
        - e:has-role: (target-actor → role)
        - e:can-assign: (admin-signer → role)

        The assignment-signature face proves the admin signed the role assignment.
        """
        for fid in self.graph.get_faces_by_type('assignment-signature'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Check for required edge types in boundary
            edge_types_found = set()
            for eid in face.edges:
                edge = self.graph.get_edge(eid)
                if edge:
                    edge_type = edge.type.replace('edge/', '') if edge.type.startswith('edge/') else edge.type
                    edge_types_found.add(edge_type)

            required_types = {'signs-assignment', 'has-role', 'can-assign'}
            missing = required_types - edge_types_found

            if missing:
                self._add_violation(
                    rule_name="assignment_signature_boundary_types",
                    rule_type=RuleType.FACE_BOUNDARY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"Assignment-signature face missing required edge types: {missing}",
                    details={
                        'required': list(required_types),
                        'found': list(edge_types_found),
                        'missing': list(missing)
                    }
                )

    # ========== Assignment Signature Requires Role Assignment (Face Adjacency) ==========

    def _check_assignment_signature_requires_role_assignment(self):
        """
        Check that assignment-signature faces have a role-assignment face sharing their can-assign edge.

        Rule: f:assignment-signature: must have f:role-assignment: sharing e:can-assign: edge.

        This establishes the chain: role-assignment → assignment-signature → has-role (result)

        Parallel to: authorization → signature → assurance
        """
        for fid in self.graph.get_faces_by_type('assignment-signature'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Find can-assign edge in boundary
            can_assign_edge_id = face.data.get('can_assign_edge')
            if not can_assign_edge_id:
                # Try to find can-assign edge in boundary
                for eid in face.edges:
                    if self.graph._edge_matches_type(eid, 'can-assign'):
                        can_assign_edge_id = eid
                        break

            if not can_assign_edge_id:
                self._add_violation(
                    rule_name="assignment_signature_requires_role_assignment",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Assignment-signature face has no can-assign edge in boundary",
                    details={'edges': face.edges}
                )
                continue

            # Check if any role-assignment face shares this can-assign edge
            role_assignment_faces = self.graph.get_faces_containing_edge(can_assign_edge_id, 'role-assignment')

            if not role_assignment_faces:
                self._add_violation(
                    rule_name="assignment_signature_requires_role_assignment",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"No role-assignment face shares can-assign edge '{can_assign_edge_id}' - admin must have assignment authority",
                    details={'can_assign_edge': can_assign_edge_id}
                )

    # ========== Module Qualification Cascade (Rule 2) ==========

    def _check_module_qualification_cascade(self):
        """
        Check module qualification cascade rule.

        Rule: qualifies(signer, module) requires qualifies(signer, g)
        for every guidance g in module's output faces.
        """
        # Find all qualifies edges to modules
        for eid in self.graph.get_edges_by_type('qualifies'):
            edge = self.graph.get_edge(eid)
            if not edge:
                continue

            target_vertex = self.graph.get_vertex(edge.target)
            if not target_vertex:
                continue

            # Check if target is a module
            if not (target_vertex.type == 'vertex/module' or target_vertex.type.startswith('vertex/module/')):
                continue

            signer_id = edge.source
            module_id = edge.target

            # Find output faces for this module
            output_faces = self.graph.get_faces_containing_vertex(module_id, 'output')

            for output_fid in output_faces:
                output_face = self.graph.get_face(output_fid)
                if not output_face:
                    continue

                # Get guidance from output face
                guidance_id = output_face.data.get('guidance')
                if not guidance_id:
                    continue

                # Check signer has qualifies edge to this guidance
                has_guidance_qual = self.graph.edge_exists(signer_id, guidance_id, 'qualifies')

                if not has_guidance_qual:
                    self._add_violation(
                        rule_name="module_qualification_cascade",
                        rule_type=RuleType.STAR,
                        severity=Severity.ERROR,
                        element_id=eid,
                        element_type="edge",
                        message=f"Signer '{signer_id}' qualified for module '{module_id}' but lacks qualification for output guidance '{guidance_id}'",
                        details={
                            'signer': signer_id,
                            'module': module_id,
                            'missing_guidance': guidance_id,
                            'output_face': output_fid
                        }
                    )

    # ========== Module-Signature Shares Edge (Rule 4) ==========

    def _check_module_signature_shares_edge(self):
        """
        Check that module-signature faces share signs edge with signature face.

        Rule: f:module-signature: must share e:signs: edge with f:signature: face.
        """
        for fid in self.graph.get_faces_by_type('module-signature'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            # Find signs edge in boundary
            signs_edge_id = None
            for eid in face.edges:
                if self.graph._edge_matches_type(eid, 'signs'):
                    signs_edge_id = eid
                    break

            if not signs_edge_id:
                self._add_violation(
                    rule_name="module_signature_shares_signs_edge",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Module-signature face has no signs edge in boundary",
                    details={'edges': face.edges}
                )
                continue

            # Check if any signature face shares this edge
            signature_faces = self.graph.get_faces_containing_edge(signs_edge_id, 'signature')

            if not signature_faces:
                self._add_violation(
                    rule_name="module_signature_shares_signs_edge",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"No signature face shares signs edge '{signs_edge_id}'",
                    details={'signs_edge': signs_edge_id}
                )

    # ========== Input/Output Satisfaction Rules (Rules 7-8) ==========

    def _check_input_satisfaction_requires_input_type(self):
        """
        Check that input-satisfaction faces share edges with input faces.

        Rule: f:input-satisfaction: must share edges with f:input: in module chart.
        """
        for fid in self.graph.get_faces_by_type('input-satisfaction'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            module_id = face.data.get('module')
            if not module_id:
                continue

            # Find input faces for this module
            input_faces = self.graph.get_faces_containing_vertex(module_id, 'input')

            if not input_faces:
                self._add_violation(
                    rule_name="input_satisfaction_requires_input_type",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"No input face found for module '{module_id}'",
                    details={'module': module_id}
                )
                continue

            # Check for shared edges with any input face
            has_shared_edge = False
            for input_fid in input_faces:
                shared = self.graph.faces_share_edge(fid, input_fid)
                if shared:
                    has_shared_edge = True
                    break

            if not has_shared_edge:
                self._add_violation(
                    rule_name="input_satisfaction_requires_input_type",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Input-satisfaction face shares no edges with module's input faces",
                    details={'module': module_id, 'input_faces': input_faces}
                )

    def _check_output_satisfaction_requires_output_type(self):
        """
        Check that output-satisfaction faces share edges with output faces.

        Rule: f:output-satisfaction: must share edges with f:output: in module chart.
        """
        for fid in self.graph.get_faces_by_type('output-satisfaction'):
            face = self.graph.get_face(fid)
            if not face:
                continue

            module_id = face.data.get('module')
            if not module_id:
                continue

            # Find output faces for this module
            output_faces = self.graph.get_faces_containing_vertex(module_id, 'output')

            if not output_faces:
                self._add_violation(
                    rule_name="output_satisfaction_requires_output_type",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message=f"No output face found for module '{module_id}'",
                    details={'module': module_id}
                )
                continue

            # Check for shared edges with any output face
            has_shared_edge = False
            for output_fid in output_faces:
                shared = self.graph.faces_share_edge(fid, output_fid)
                if shared:
                    has_shared_edge = True
                    break

            if not has_shared_edge:
                self._add_violation(
                    rule_name="output_satisfaction_requires_output_type",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=fid,
                    element_type="face",
                    message="Output-satisfaction face shares no edges with module's output faces",
                    details={'module': module_id, 'output_faces': output_faces}
                )

    # ========== Execution Trace DAG (Rule 14) ==========

    def _check_execution_trace_dag(self):
        """
        Check that follows edges form a DAG.

        Rule: Follows edges MUST form a directed acyclic graph (causality).
        """
        is_dag, cycle = self.graph.check_dag('follows')

        if not is_dag:
            self._add_violation(
                rule_name="execution_trace_dag",
                rule_type=RuleType.EDGE_ENDPOINT,
                severity=Severity.ERROR,
                element_id="follows_edges",
                element_type="edge",
                message="Follows edges contain a cycle (violates causality)",
                details={'cycle_vertices': cycle}
            )

    # ========== Runbook Module Ordering (Rule 12) ==========

    def _check_runbook_module_ordering(self):
        """
        Check that precedes edges form a valid partial order.

        Rule: Precedes edges define a partial order on modules.
        Note: Same module MAY appear multiple times if I/O types are compatible.
        """
        # Note: Unlike follows edges, precedes edges need not be a strict DAG
        # because a module can refine its own output (iterative refinement).
        # We only check for type-incompatible cycles.

        # For now, just verify precedes edges connect modules
        for eid in self.graph.get_edges_by_type('precedes'):
            edge = self.graph.get_edge(eid)
            if not edge:
                continue

            source = self.graph.get_vertex(edge.source)
            target = self.graph.get_vertex(edge.target)

            if source and not self._type_matches_any(source.type, ['vertex/module']):
                self._add_violation(
                    rule_name="runbook_module_ordering",
                    rule_type=RuleType.EDGE_ENDPOINT,
                    severity=Severity.ERROR,
                    element_id=eid,
                    element_type="edge",
                    message=f"Precedes edge source '{edge.source}' is not a module",
                    details={'source_type': source.type if source else None}
                )

            if target and not self._type_matches_any(target.type, ['vertex/module']):
                self._add_violation(
                    rule_name="runbook_module_ordering",
                    rule_type=RuleType.EDGE_ENDPOINT,
                    severity=Severity.ERROR,
                    element_id=eid,
                    element_type="edge",
                    message=f"Precedes edge target '{edge.target}' is not a module",
                    details={'target_type': target.type if target else None}
                )

    # ========== Runbook I/O Chaining (Rule 13) ==========

    def _check_runbook_io_chaining(self):
        """
        Check runbook I/O type chaining.

        Rule: Prior module's output type must match subsequent module's input type.
        """
        for eid in self.graph.get_edges_by_type('precedes'):
            edge = self.graph.get_edge(eid)
            if not edge:
                continue

            prior_module = edge.source
            next_module = edge.target

            # Get output faces of prior module
            prior_outputs = self.graph.get_faces_containing_vertex(prior_module, 'output')

            # Get input faces of next module
            next_inputs = self.graph.get_faces_containing_vertex(next_module, 'input')

            if not prior_outputs or not next_inputs:
                continue  # Can't check without both

            # Collect output specs from prior
            prior_output_specs = set()
            for fid in prior_outputs:
                face = self.graph.get_face(fid)
                if face and face.data.get('spec'):
                    prior_output_specs.add(face.data['spec'])

            # Collect input specs from next
            next_input_specs = set()
            for fid in next_inputs:
                face = self.graph.get_face(fid)
                if face and face.data.get('spec'):
                    next_input_specs.add(face.data['spec'])

            # Check for overlap
            matching_specs = prior_output_specs & next_input_specs

            if not matching_specs and prior_output_specs and next_input_specs:
                self._add_violation(
                    rule_name="runbook_io_chaining",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=eid,
                    element_type="edge",
                    message=f"No matching I/O type between modules",
                    details={
                        'prior_module': prior_module,
                        'next_module': next_module,
                        'prior_output_specs': list(prior_output_specs),
                        'next_input_specs': list(next_input_specs)
                    }
                )

    # ========== Execution Causal Chain (Rule 15) ==========

    def _check_execution_causal_chain(self):
        """
        Check execution causal chain.

        Rule: If execution B follows execution A, then B must consume
        at least one document that A produced.
        """
        for eid in self.graph.get_edges_by_type('follows'):
            edge = self.graph.get_edge(eid)
            if not edge:
                continue

            # B follows A means: A -> B (A precedes B)
            exec_a = edge.source
            exec_b = edge.target

            # Get documents produced by A
            docs_produced_by_a = set()
            for prod_eid in self.graph.get_edges_from(exec_a, 'produces'):
                prod_edge = self.graph.get_edge(prod_eid)
                if prod_edge:
                    docs_produced_by_a.add(prod_edge.target)

            # Get documents consumed by B
            docs_consumed_by_b = set()
            for cons_eid in self.graph.get_edges_from(exec_b, 'consumes'):
                cons_edge = self.graph.get_edge(cons_eid)
                if cons_edge:
                    docs_consumed_by_b.add(cons_edge.target)

            # Check overlap
            shared_docs = docs_produced_by_a & docs_consumed_by_b

            if not shared_docs and docs_produced_by_a:
                self._add_violation(
                    rule_name="execution_causal_chain",
                    rule_type=RuleType.FACE_ADJACENCY,
                    severity=Severity.ERROR,
                    element_id=eid,
                    element_type="edge",
                    message=f"Execution '{exec_b}' follows '{exec_a}' but consumes none of A's outputs",
                    details={
                        'exec_a': exec_a,
                        'exec_b': exec_b,
                        'a_produces': list(docs_produced_by_a),
                        'b_consumes': list(docs_consumed_by_b)
                    }
                )


def check_ontology_rules(cache: Dict[str, Any]) -> List[RuleViolation]:
    """
    Convenience function to check all ontology rules.

    Args:
        cache: Parsed complex.json data

    Returns:
        List of rule violations
    """
    engine = OntologyRuleEngine.from_cache(cache)
    return engine.check_all()
