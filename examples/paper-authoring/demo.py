"""
demo.py — Paper Authoring with the AAA Framework

Demonstrates the complete AAA workflow through the process of writing
and assuring two conference papers on knowledge complexes.

The demo shows three core properties of the framework:

  1. Document types are KC elements, not file templates.
     A "conference paper" type is a DocType EDGE connecting a spec vertex
     (structural requirements) to a guidance vertex (quality criteria).
     DocType elements are queryable — kc.element_ids(type="DocType")
     returns the full catalogue of document types in the complex.

  2. Assurance is topological closure.
     A paper is assured when three edges form a closed triangle (face):
       - verification edge (doc ↔ spec)    — structural compliance
       - validation edge  (doc ↔ guidance) — quality approval
       - DocType edge     (spec ↔ guidance) — document type coherence
     The assurance face carries rolled-up metadata (doc_name, signed_by,
     dates, status) for efficient auditing without dereferencing documents.

  3. Composition via charts.
     A chart is a document whose identity is a SPARQL query that
     materializes a subcomplex. The paper-series chart selects the
     closure of all assurance faces — every element that participates in
     at least one assured paper — without explicitly listing them.
     Tiling completeness (every doc has assurance coverage) is the
     formal audit criterion.

Run:
    cd examples/paper-authoring
    python demo.py

    # Or build the RDF graph directly and inspect it:
    aaa build content/ --output /tmp/papers.ttl
    aaa verify content/00_vertices/spec-conference-paper.md
"""

import sys
import tempfile
from pathlib import Path

from click.testing import CliRunner
from knowledgecomplex import KnowledgeComplex
from knowledgecomplex.io import load_graph as _load_graph

from aaa.schema import build_aaa_schema
from aaa.commands.build import build
from aaa.commands.audit import _check_tiling

CONTENT_DIR = Path(__file__).parent / "content"


# ── Helpers ──────────────────────────────────────────────────────────────────

def section(title: str) -> None:
    width = 64
    print(f"\n{'─' * width}")
    print(f"  {title}")
    print('─' * width)


def _elem_line(kc: KnowledgeComplex, elem_id: str, indent: int = 2) -> str:
    pad = " " * indent
    e = kc.element(elem_id)
    name = e.attrs.get("name", "")
    label = f"{name!r}" if name else ""
    return f"{pad}{elem_id:<46} [{e.type}]  {label}"


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:

    # ── 1. Schema + Build ─────────────────────────────────────────────────────
    section("1  Schema + Build — Markdown → Codec → KnowledgeComplex → RDF")

    print("""
The AAA schema is declared using SchemaBuilder (OWL/SHACL). It defines:
  Vertex types: doc, spec, guidance, chart
  Edge types:   verification, validation, DocType
  Face types:   assurance

Pydantic Codecs parse each markdown file and validate it against its type's
model before inserting it into the KnowledgeComplex. The full complex is
then serialized to RDF (Turtle).
""")

    schema = build_aaa_schema()

    with tempfile.NamedTemporaryFile(suffix=".ttl", delete=False) as f:
        graph_path = Path(f.name)

    runner = CliRunner()
    result = runner.invoke(build, [str(CONTENT_DIR), "--output", str(graph_path)])

    if result.exit_code != 0:
        print(f"[ERROR] Build failed:\n{result.output}", file=sys.stderr)
        sys.exit(1)

    # Echo build summary (warnings and inserted count)
    for line in result.output.strip().splitlines():
        print(f"  {line}")

    kc = KnowledgeComplex(schema=schema)
    with kc.deferred_verification():
        _load_graph(kc, graph_path)

    all_ids = kc.element_ids()
    print(f"\nKnowledge complex loaded: {len(all_ids)} elements")
    for elem_id in sorted(all_ids):
        print(_elem_line(kc, elem_id))

    # ── 2. Document Type Discovery ────────────────────────────────────────────
    section("2  Document Types — DocType Edges as KC Elements")

    print("""
A document type in AAA is NOT a static template stored in a file system.
It is a DOCTYPE EDGE — a first-class element of the knowledge complex that
connects a spec vertex (structural requirements) to a guidance vertex
(quality criteria). This means document types are:
  - Queryable: kc.element_ids(type="DocType")
  - Addressable: kc.element("e:DocType:conference-paper")
  - Linkable: assurance faces reference the DocType edge in their boundary
""")

    doctype_ids = sorted(kc.element_ids(type="DocType"))
    print(f"Document types in this complex: {len(doctype_ids)}")

    for dt_id in doctype_ids:
        elem = kc.element(dt_id)
        attrs = elem.attrs
        print(f"\n  [{dt_id}]")
        print(f"    Name:          {attrs.get('name', '?')}")
        desc = attrs.get("description", "")
        print(f"    Description:   {desc[:72]}{'...' if len(desc) > 72 else ''}")
        print(f"    Used for:      {attrs.get('commonly_used_for', '?')}")

        boundary = kc.boundary(dt_id)
        spec_id = next(b for b in boundary if kc.element(b).type == "spec")
        guid_id = next(b for b in boundary if kc.element(b).type == "guidance")

        spec_desc = kc.element(spec_id).attrs.get("description", "")
        guid_desc = kc.element(guid_id).attrs.get("description", "")

        print(f"\n    Spec   ({spec_id}):")
        print(f"      {spec_desc[:72]}{'...' if len(spec_desc) > 72 else ''}")
        print(f"    Guidance ({guid_id}):")
        print(f"      {guid_desc[:72]}{'...' if len(guid_desc) > 72 else ''}")

    # ── 3. Papers ─────────────────────────────────────────────────────────────
    section("3  Papers — Doc Vertices and Their Verification Status")

    doc_ids = sorted(e for e in kc.element_ids(type="doc") if kc.element(e).type == "doc")
    print(f"Documents in the complex: {len(doc_ids)}")
    for doc_id in doc_ids:
        elem = kc.element(doc_id)
        print(f"\n  [{doc_id}]")
        print(f"    {elem.attrs.get('name', '?')}")
        desc = elem.attrs.get("description", "")
        print(f"    {desc[:80]}{'...' if len(desc) > 80 else ''}")

    print("\nVerification edges against the conference-paper spec:")
    ver_edges = sorted(kc.coboundary("v:spec:conference-paper", type="verification"))
    for v_id in ver_edges:
        attrs = kc.element(v_id).attrs
        boundary = kc.boundary(v_id)
        doc_id = next(b for b in boundary if kc.element(b).type == "doc")
        doc_name = kc.element(doc_id).attrs.get("name", "?")
        print(f"  {v_id}")
        print(f"    doc:    {doc_id}  ({doc_name[:50]}...)")
        print(f"    status: {attrs.get('status', '?')}")

    print("\nValidation edges against the conference-paper guidance:")
    val_edges = sorted(kc.coboundary("v:guidance:conference-paper", type="validation"))
    for v_id in val_edges:
        attrs = kc.element(v_id).attrs
        boundary = kc.boundary(v_id)
        doc_id = next(b for b in boundary if kc.element(b).type == "doc")
        doc_name = kc.element(doc_id).attrs.get("name", "?")
        print(f"  {v_id}")
        print(f"    doc:       {doc_id}  ({doc_name[:50]}...)")
        print(f"    status:    {attrs.get('status', '?')}")
        print(f"    signed by: {attrs.get('signed_by', '?')}")

    # ── 4. Assurance Triangles ─────────────────────────────────────────────────
    section("4  Assurance Triangles — Face Elements")

    print("""
Assurance is topological closure. A paper is assured when its
verification, validation, and DocType edges form a closed triangle.
The assurance face:
  - Is a 2-simplex whose boundary contains exactly those 3 edges
  - Carries rolled-up metadata (doc_name, signed_by, dates, status)
  - Enables auditing without dereferencing the underlying documents
  - Is an immutable attestation — adding it closes the triangle permanently

Both papers share the same DocType edge. The document type definition is
a structural invariant of the complex, not metadata duplicated per paper.
""")

    assured_ids = sorted(kc.element_ids(type="assurance"))
    print(f"Assurance faces: {len(assured_ids)}")

    for a_id in assured_ids:
        elem = kc.element(a_id)
        attrs = elem.attrs
        print(f"\n  [{a_id}]")
        print(f"    Document:          {attrs.get('doc_name', '?')}")
        print(f"    Signed by:         {attrs.get('signed_by', '?')}")
        print(f"    Status:            {attrs.get('status', '?')}")
        print(f"    Verification date: {attrs.get('verification_date', '?')}")
        print(f"    Validation date:   {attrs.get('validation_date', '?')}")
        print(f"    Boundary (3 edges):")
        for edge_id in sorted(kc.boundary(a_id)):
            edge = kc.element(edge_id)
            print(f"      {edge_id:<44} [{edge.type}]")

    # Star of paper 1 — everything reachable from it
    print("\nStar of paper 1 (all simplices containing v:doc:kc-assurance-paper):")
    star = kc.star("v:doc:kc-assurance-paper")
    for s_id in sorted(star):
        print(_elem_line(kc, s_id))

    closed = kc.closed_star("v:doc:kc-assurance-paper")
    is_sc = kc.is_subcomplex(closed)
    print(f"\nClosed star is a valid subcomplex: {is_sc}")

    # ── 5. SHACL Audit ─────────────────────────────────────────────────────────
    section("5  SHACL Audit — Graph-Level Constraints")

    print("""
SHACL constraints are enforced on the RDF graph — not on individual files.
The AAA schema declares:
  - Every spec must have at least one verification coboundary edge
  - Every guidance must have at least one validation coboundary edge
  - Every assurance face must have exactly 3 boundary edges
  - All vocabulary values (status, etc.) must be in their declared sets
  - All assurance triangles must be topologically closed (Closed Triangle SPARQL)
""")

    report = kc.audit()

    if report.conforms:
        print("Audit: CONFORMS  ✓")
        print("  All graph-level SHACL constraints satisfied:")
        print("  ✓  Every spec has ≥1 verification edge")
        print("  ✓  Every guidance has ≥1 validation edge")
        print("  ✓  All assurance faces have closed triangular boundaries")
        print("  ✓  All vocabulary values are valid")
    else:
        print(f"Audit: {len(report.violations)} VIOLATION(S)")
        for v in report.violations:
            print(f"  {v}")

    # ── 6. Paper Series Chart ──────────────────────────────────────────────────
    section("6  Paper Series Chart — Composition via SPARQL")

    print("""
A chart is a vertex/doc with a required 'query' field containing valid SPARQL.
The query materializes a subcomplex — the chart's "content" — on demand.
Chart subtypes are SHACL constraints on the resulting subcomplex.

The paper-series chart selects the closure of all assurance faces:
  face level  → every assurance face
  edge level  → every edge in the boundary of an assurance face
  vertex level → every vertex in the boundary of those edges

This means new papers appear in the chart automatically when their
assurance faces are added — no explicit enumeration needed.
""")

    chart = kc.element("v:chart:paper-series")
    chart_attrs = chart.attrs
    print(f"Chart: {chart_attrs.get('name', '?')}")
    print(f"Query:\n{chart_attrs.get('query', '').rstrip()}")

    series_ids = kc._ids_from_query(chart_attrs["query"])
    print(f"\nMaterialized subcomplex: {len(series_ids)} elements")
    for s_id in sorted(series_ids):
        print(_elem_line(kc, s_id))

    is_closed = kc.is_subcomplex(series_ids)
    print(f"\nSubcomplex is topologically closed: {is_closed}")

    uncovered = _check_tiling(kc, series_ids)
    if uncovered:
        print(f"\nTiling: INCOMPLETE — {len(uncovered)} doc(s) without assurance:")
        for doc_id in uncovered:
            print(f"  {doc_id}")
    else:
        print("Tiling: COMPLETE — every document in the series is assured  ✓")

    # ── 7. Algebraic Topology ─────────────────────────────────────────────────
    section("7  Algebraic Topology — Betti Numbers & Edge Influence")

    from knowledgecomplex import (
        betti_numbers, euler_characteristic,
        boundary_matrices, edge_pagerank, edge_influence,
    )

    vertices = kc.skeleton(0)
    edges    = kc.skeleton(1) - kc.skeleton(0)
    faces    = kc.skeleton(2) - kc.skeleton(1)
    V, E, F  = len(vertices), len(edges), len(faces)
    chi      = euler_characteristic(kc)
    betti    = betti_numbers(kc)

    print(f"Counts:  V={V}  E={E}  F={F}")
    print(f"Euler characteristic  χ = V − E + F = {V} − {E} + {F} = {chi}")
    print()
    print(f"Betti numbers:  β₀={betti[0]}  β₁={betti[1]}  β₂={betti[2]}")
    print(f"  β₀ = {betti[0]}  connected components")
    print(f"       (1 main complex with all assurance elements + 1 isolated chart vertex)")
    print(f"  β₁ = {betti[1]}  independent cycles  (both triangles filled by assurance faces)")
    print(f"  β₂ = {betti[2]}  enclosed voids")
    print(f"\nVerification: χ = β₀ − β₁ + β₂ = {betti[0]} − {betti[1]} + {betti[2]} = {betti[0]-betti[1]+betti[2]}")

    print("""
Edge Influence (PageRank-based): which edges carry the most structural weight?
The DocType edge bridges spec and guidance — every assurance triangle passes
through it, so it should rank highest.
""")

    bm = boundary_matrices(kc)
    rows = []
    for eid in sorted(bm.edge_index):
        pr    = edge_pagerank(kc, eid)
        infl  = edge_influence(eid, pr)
        rows.append((eid, infl.spread, infl.absolute_influence))

    rows.sort(key=lambda r: r[2], reverse=True)
    print(f"  {'Edge':<44}  {'spread':>7}  {'influence':>10}")
    print(f"  {'─'*44}  {'─'*7}  {'─'*10}")
    for eid, spread, influence in rows:
        etype = kc.element(eid).type
        print(f"  {eid:<44}  {spread:>7.3f}  {influence:>10.3f}  [{etype}]")

    # ── 8. Visualization ──────────────────────────────────────────────────────
    section("8  Visualization — Hasse Diagrams & Geometric Realization")

    import matplotlib.pyplot as plt
    from knowledgecomplex import (
        to_networkx, verify_networkx,
        plot_hasse, plot_hasse_star, plot_geometric,
    )

    out_dir = Path(__file__).parent / "output"
    out_dir.mkdir(exist_ok=True)

    print("""
Generating three views of the knowledge complex:

  hasse.png         — Full Hasse diagram: elements as nodes, boundary
                      as directed arrows (faces → edges → vertices).
                      Shows the complete 2-complex structure.

  hasse_star_kc_paper.png — Neighbourhood of paper 1 highlighted.
                      The star of a vertex is everything reachable
                      from it via the coboundary operator.

  geometric.png     — Geometric realization: vertices placed in 3D
                      space, edges as line segments, faces as filled
                      triangles. Shows the two shared-edge triangles.
""")

    # Export to NetworkX and verify
    G = to_networkx(kc)
    verify_networkx(G)
    print(f"NetworkX DiGraph: {G.number_of_nodes()} nodes, {G.number_of_edges()} directed edges")
    print()

    # Hasse diagram — full complex
    fig, ax = plot_hasse(kc, figsize=(13, 9))
    ax.set_title("AAA Paper Authoring — Hasse Diagram\n"
                 "arrows: boundary operator ∂ (face → edge → vertex)", fontsize=11)
    fig.tight_layout()
    path_hasse = out_dir / "hasse.png"
    fig.savefig(path_hasse, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved  {path_hasse.relative_to(Path.cwd())}")

    # Hasse star — neighbourhood of paper 1
    fig, ax = plot_hasse_star(kc, "v:doc:kc-assurance-paper", figsize=(11, 8))
    ax.set_title("Star of v:doc:kc-assurance-paper\n"
                 "highlighted: all simplices that touch this paper", fontsize=11)
    fig.tight_layout()
    path_star = out_dir / "hasse_star_kc_paper.png"
    fig.savefig(path_star, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved  {path_star.relative_to(Path.cwd())}")

    # Geometric realization
    fig, ax = plot_geometric(kc, figsize=(11, 9))
    ax.set_title("AAA Paper Authoring — Geometric Realization\n"
                 "two assurance triangles sharing the DocType edge", fontsize=11)
    fig.tight_layout()
    path_geo = out_dir / "geometric.png"
    fig.savefig(path_geo, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved  {path_geo.relative_to(Path.cwd())}")

    print(f"\nAll visualizations saved to {out_dir.relative_to(Path.cwd())}/")
    print("""
Key topological insight: the two assurance triangles share one edge
(e:DocType:conference-paper). In the geometric realization this appears
as two triangles joined at a common edge — a "book" or "butterfly" shape.
The document type definition is a shared structural element of the complex,
not metadata duplicated per paper. Topology enforces this sharing in a way
that flat document systems cannot guarantee.
""")

    # Cleanup
    graph_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
