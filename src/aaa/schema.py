"""
AAA domain schema declared using SchemaBuilder.

Declares the core assurance types in OWL/SHACL with the `aaa` namespace
(https://example.org/aaa# — will migrate to https://w3id.org/aaa# once registered).

Call build_aaa_schema() to obtain a fully configured SchemaBuilder ready for
use as the backend of a KnowledgeComplex instance.
"""

from knowledgecomplex import SchemaBuilder, text, vocab


def build_aaa_schema() -> SchemaBuilder:
    """
    Build and return the AAA domain schema.

    Core assurance types:
      Vertices: doc, spec (extends doc), guidance (extends doc),
                chart (extends doc), assurance_audit (extends chart)
      Edges:    verification, validation, DocType
      Faces:    assurance

    Topological constraints (SHACL-enforced on the RDF graph):
      - Every spec must have at least one verification edge (coboundary).
      - Every guidance must have at least one validation edge (coboundary).
      - Every doc within an assurance_audit scope must have at least one
        assurance face (coboundary).
    """
    sb = SchemaBuilder(namespace="aaa")

    # ------------------------------------------------------------------
    # Vertex types
    # ------------------------------------------------------------------

    # doc — base document type; all content artifacts extend this
    sb.add_vertex_type(
        "doc",
        attributes={
            "name": text(),
            "version": {"text": text(required=False)},
            "description": {"text": text(required=False)},
        },
    )

    # spec — structural requirements for a document type (WHAT it must have)
    sb.add_vertex_type("spec", parent="doc")

    # guidance — soft authoring guidance (HOW/WHY to write it)
    sb.add_vertex_type("guidance", parent="doc")

    # chart — a document whose identity is a SPARQL query that materialises
    # a subcomplex. The query field must contain valid SPARQL.
    sb.add_vertex_type(
        "chart",
        parent="doc",
        attributes={
            "query": text(),
        },
    )

    # assurance_audit — a chart subtype whose subcomplex must be completely
    # tiled by assurance faces (enforced via topological constraint below).
    sb.add_vertex_type("assurance_audit", parent="chart")

    # ------------------------------------------------------------------
    # Edge types
    # ------------------------------------------------------------------

    # verification — connects a doc to the spec it is verified against
    sb.add_edge_type(
        "verification",
        attributes={
            "status": vocab("passing", "failing", "pending"),
        },
    )

    # validation — connects a doc to the guidance it is validated against;
    # carries the signatory and rationale for the validation decision
    sb.add_edge_type(
        "validation",
        attributes={
            "status": vocab("approved", "rejected", "pending"),
            "rationale": {"text": text(required=False)},
            "signed_by": {"text": text(required=False)},
        },
    )

    # coupling — connects a spec to a guidance (or either to the root),
    # representing the pairing that defines a document type context
    sb.add_edge_type("coupling")

    # DocType — connects a spec to a guidance, defining a document type.
    # The spec+guidance pair is a first-class addressable element with data.
    # kc.element_ids(type="DocType") returns all defined document types.
    sb.add_edge_type(
        "DocType",
        attributes={
            "name": text(),
            "description": {"text": text(required=False)},
            "commonly_used_for": {"text": text(required=False)},
        },
    )

    # ------------------------------------------------------------------
    # Face types
    # ------------------------------------------------------------------

    # assurance — closes the triangle: verification(doc↔spec) +
    # validation(doc↔guidance) + DocType(spec↔guidance).
    # Carries rolled-up metadata for audit without dereferencing documents.
    # SHACL validates that metadata fields are consistent with boundary elements.
    sb.add_face_type(
        "assurance",
        attributes={
            "doc_name": text(),
            "signed_by": text(),
            "validation_date": {"text": text(required=False)},
            "verification_date": {"text": text(required=False)},
            "status": vocab("assured", "pending", "failed"),
        },
    )

    # ------------------------------------------------------------------
    # Topological constraints (SHACL-enforced on the RDF graph)
    # ------------------------------------------------------------------

    # Every spec must have at least one incoming verification edge.
    sb.add_topological_constraint(
        "spec",
        "coboundary",
        target_type="verification",
        predicate="min_count",
        min_count=1,
        message="Every spec must have at least one verification edge.",
    )

    # Every guidance must have at least one incoming validation edge.
    sb.add_topological_constraint(
        "guidance",
        "coboundary",
        target_type="validation",
        predicate="min_count",
        min_count=1,
        message="Every guidance must have at least one validation edge.",
    )

    # NOTE: The "every doc must have an assurance face" tiling constraint is
    # NOT added here globally — it only makes sense within the scope of an
    # assurance_audit chart subcomplex.  The `aaa audit` command enforces it
    # programmatically after materialising the chart's SPARQL query.

    return sb
