"""
aaa audit - Audit a chart for assurance completeness.

A chart is a document with a required 'query' field containing valid SPARQL.
Running `aaa audit` on a chart:
  1. Loads the global KC from the RDF graph (built by `aaa build`).
  2. Executes the chart's SPARQL query to materialise the subcomplex.
  3. Validates topological closure (kc.is_subcomplex).
  4. Runs SHACL on the subcomplex (AuditReport).
  5. Checks complete tiling: every doc-type element must have an assurance face.

Examples:
    aaa audit charts/my-chart/my-chart.md
    aaa audit charts/my-chart/my-chart.md --graph graph.ttl
"""

import click
import sys
from pathlib import Path

from knowledgecomplex import KnowledgeComplex, load_graph
from knowledgecomplex.io import load_graph as _load_graph

from aaa.schema import build_aaa_schema
from aaa.codecs import codec_for_type


def _load_kc(graph_path: Path) -> KnowledgeComplex:
    """Load a KnowledgeComplex from a serialised RDF graph."""
    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    with kc.deferred_verification():
        _load_graph(kc, graph_path)
    return kc


def _read_chart_query(chart_path: Path) -> tuple[str, str]:
    """Return (chart_id, query) from a chart markdown file."""
    codec = codec_for_type("vertex/chart")
    attrs = codec.decompile(chart_path.as_uri())
    return attrs.get("id", chart_path.stem), attrs["query"]


def _check_tiling(kc: KnowledgeComplex, element_ids: set[str]) -> list[str]:
    """
    Check complete tiling: every doc-type element in the subcomplex must have
    at least one assurance face whose boundary includes that element.

    Returns a list of doc IDs that are missing assurance coverage.
    """
    uncovered = []
    for elem_id in element_ids:
        try:
            elem = kc.element(elem_id)
        except (ValueError, KeyError):
            continue
        # Only check doc-type vertices (not edges or faces, and not spec/guidance/chart
        # which are meta-documents rather than work products being assured)
        elem_type = elem.type
        if elem_type not in ("doc",):
            continue
        # Check star (transitive coboundary) for assurance faces.
        # A doc vertex is covered if any assurance face is reachable via
        # the boundary chain: doc → edge → face (star traverses transitively).
        assurance_faces = kc.star(elem_id, type="assurance")
        if not assurance_faces:
            uncovered.append(elem_id)

    return uncovered


@click.command()
@click.argument("chart", type=click.Path(exists=True))
@click.option("--graph", "-g", default="graph.ttl", show_default=True,
              type=click.Path(),
              help="Path to the RDF graph built by `aaa build`.")
@click.option("--no-tiling", is_flag=True,
              help="Skip the assurance tiling completeness check.")
def audit(chart, graph, no_tiling):
    """Audit CHART for assurance completeness against the RDF graph."""
    chart_path = Path(chart)
    graph_path = Path(graph)

    if not graph_path.exists():
        click.echo(
            f"[ERROR] Graph not found: {graph_path}\n"
            f"        Run `aaa build` first to generate the RDF graph.",
            err=True,
        )
        sys.exit(1)

    # 1. Load KC from graph
    try:
        kc = _load_kc(graph_path)
    except Exception as exc:
        click.echo(f"[ERROR] Failed to load graph {graph_path}: {exc}", err=True)
        sys.exit(1)

    # 2. Read chart SPARQL query
    try:
        chart_id, query = _read_chart_query(chart_path)
    except Exception as exc:
        click.echo(f"[ERROR] Failed to read chart {chart_path}: {exc}", err=True)
        sys.exit(1)

    click.echo(f"Auditing chart: {chart_id}")

    # 3. Execute query to materialise subcomplex element IDs
    try:
        element_ids: set[str] = kc._ids_from_query(query)
    except Exception as exc:
        click.echo(f"[ERROR] Chart SPARQL query failed: {exc}", err=True)
        sys.exit(1)

    click.echo(f"  Subcomplex: {len(element_ids)} elements")

    # 4. Validate topological closure
    if not kc.is_subcomplex(element_ids):
        click.echo("[FAIL]  Subcomplex is not topologically closed (boundary violation).")
        sys.exit(1)
    click.echo("  Topology:   closed ✓")

    # 5. SHACL audit on subcomplex
    report = kc.audit()
    if not report.conforms:
        click.echo(f"[FAIL]  SHACL violations ({len(report.violations)}):")
        for v in report.violations:
            click.echo(f"        {v.element_id}: {v.message}")
        # Continue to tiling check even if SHACL fails
    else:
        click.echo("  SHACL:      conforms ✓")

    # 6. Tiling completeness
    if not no_tiling:
        uncovered = _check_tiling(kc, element_ids)
        if uncovered:
            click.echo(f"[FAIL]  Tiling incomplete — {len(uncovered)} doc(s) without assurance:")
            for doc_id in uncovered:
                click.echo(f"        {doc_id}")
            sys.exit(1)
        else:
            click.echo("  Tiling:     complete ✓")

    if report.conforms:
        click.echo(f"[OK]    Audit passed: {chart_id}")
    else:
        sys.exit(1)
