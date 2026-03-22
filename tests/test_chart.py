"""
tests/test_chart.py

Tests for chart materialization: ChartCodec decompile, SPARQL query execution,
and subcomplex validation via KnowledgeComplex.
"""

from pathlib import Path

import pytest
from knowledgecomplex import KnowledgeComplex

from aaa.codecs.chart import ChartCodec
from aaa.schema import build_aaa_schema

FIXTURES = Path(__file__).parent / "fixtures" / "aaa"


def _build_sample_kc():
    """Build the minimal sample KC used in several tests."""
    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    with kc.deferred_verification():
        kc.add_vertex("v:spec:sample", type="spec", name="Sample Spec")
        kc.add_vertex("v:guidance:sample", type="guidance", name="Sample Guidance")
        kc.add_vertex("v:doc:sample", type="doc", name="Sample Document")
        kc.add_vertex(
            "v:chart:sample",
            type="chart",
            name="Sample Chart",
            query="SELECT ?x WHERE { ?x a <https://example.org/aaa#doc> . }",
        )
        kc.add_edge(
            "e:DocType:sample",
            type="DocType",
            vertices={"v:spec:sample", "v:guidance:sample"},
            name="Sample DocType",
        )
        kc.add_edge(
            "e:verification:sample",
            type="verification",
            vertices={"v:doc:sample", "v:spec:sample"},
            name="Sample Verification",
            status="passing",
        )
        kc.add_edge(
            "e:validation:sample",
            type="validation",
            vertices={"v:doc:sample", "v:guidance:sample"},
            name="Sample Validation",
            status="approved",
            signed_by="Alice",
        )
        kc.add_face(
            "f:assurance:sample",
            type="assurance",
            boundary=["e:verification:sample", "e:validation:sample", "e:DocType:sample"],
            name="Sample Assurance",
            doc_name="Sample Document",
            signed_by="Alice",
            status="assured",
        )
    return kc


# --- ChartCodec decompile ---


def test_chart_decompile_valid():
    attrs = ChartCodec().decompile((FIXTURES / "sample-chart.md").as_uri())
    assert "query" in attrs
    assert "SELECT" in attrs["query"].upper()


def test_chart_decompile_invalid_sparql(tmp_path):
    bad = tmp_path / "bad.md"
    bad.write_text(
        "---\ntype: vertex/chart\nid: v:chart:bad\nname: Bad\nquery: not valid sparql at all\n---\n"
    )
    from pydantic import ValidationError

    with pytest.raises(ValidationError, match="SPARQL"):
        ChartCodec().decompile(bad.as_uri())


# --- SPARQL query materialization ---


def test_chart_query_returns_doc_elements():
    kc = _build_sample_kc()
    query = """
    PREFIX aaa: <https://example.org/aaa#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?element WHERE {
        ?element a aaa:doc .
    }
    """
    result_ids = kc._ids_from_query(query)
    assert "v:doc:sample" in result_ids


def test_chart_query_returns_all_elements():
    kc = _build_sample_kc()
    query = """
    PREFIX kc: <https://example.org/kc#>
    SELECT ?element WHERE {
        ?complex kc:hasElement ?element .
    }
    """
    result_ids = kc._ids_from_query(query)
    assert len(result_ids) >= 7  # 4 vertices + 3 edges (face not counted separately by query)


# --- Subcomplex validation ---


def test_valid_subcomplex_passes():
    kc = _build_sample_kc()
    # The full set of elements should be a valid subcomplex (closed under boundary)
    all_ids = {
        "v:spec:sample",
        "v:guidance:sample",
        "v:doc:sample",
        "e:DocType:sample",
        "e:verification:sample",
        "e:validation:sample",
        "f:assurance:sample",
    }
    assert kc.is_subcomplex(all_ids)


def test_incomplete_subcomplex_fails():
    kc = _build_sample_kc()
    # Include the face but omit one boundary edge → not closed
    incomplete = {
        "v:spec:sample",
        "v:guidance:sample",
        "v:doc:sample",
        "e:DocType:sample",
        "e:verification:sample",
        # Missing e:validation:sample
        "f:assurance:sample",
    }
    assert not kc.is_subcomplex(incomplete)


def test_vertex_only_subcomplex_passes():
    kc = _build_sample_kc()
    # Vertices alone are always closed (empty boundary)
    assert kc.is_subcomplex({"v:spec:sample", "v:doc:sample"})
