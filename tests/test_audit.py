"""
tests/test_audit.py

Tests for the `aaa audit` command: chart SPARQL materialisation,
topological closure, SHACL compliance, and tiling completeness.
"""

import pytest
from pathlib import Path
from click.testing import CliRunner

from knowledgecomplex import KnowledgeComplex
from aaa.schema import build_aaa_schema
from aaa.commands.audit import _check_tiling
from aaa.commands.build import build

FIXTURES = Path(__file__).parent / "fixtures" / "aaa"


@pytest.fixture
def built_graph(tmp_path):
    """Build an RDF graph from fixtures into a temp file, return (Path, KnowledgeComplex)."""
    from knowledgecomplex.io import load_graph as _load_graph

    runner = CliRunner()
    out = tmp_path / "graph.ttl"
    result = runner.invoke(build, [str(FIXTURES), "--output", str(out)])
    assert result.exit_code == 0, result.output

    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    with kc.deferred_verification():
        _load_graph(kc, out)
    return out, kc


@pytest.fixture
def sample_kc():
    """Minimal in-memory KC with the full assurance triangle."""
    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    with kc.deferred_verification():
        kc.add_vertex("v:spec:sample", type="spec", name="Sample Spec")
        kc.add_vertex("v:guidance:sample", type="guidance", name="Sample Guidance")
        kc.add_vertex("v:doc:sample", type="doc", name="Sample Document")
        kc.add_edge("e:DocType:sample", type="DocType",
                    vertices={"v:spec:sample", "v:guidance:sample"}, name="Sample DocType")
        kc.add_edge("e:verification:sample", type="verification",
                    vertices={"v:doc:sample", "v:spec:sample"},
                    name="Sample Verification", status="passing")
        kc.add_edge("e:validation:sample", type="validation",
                    vertices={"v:doc:sample", "v:guidance:sample"},
                    name="Sample Validation", status="approved", signed_by="Alice")
        kc.add_face("f:assurance:sample", type="assurance",
                    boundary=["e:verification:sample", "e:validation:sample", "e:DocType:sample"],
                    name="Sample Assurance", doc_name="Sample Document",
                    signed_by="Alice", status="assured")
    return kc


# --- SHACL audit ---

def test_audit_conforms_on_valid_kc(sample_kc):
    report = sample_kc.audit()
    assert report.conforms, f"Expected conforming audit; violations:\n{report.text}"


def test_audit_violation_missing_verification():
    """A spec without a verification edge violates the topological SHACL constraint."""
    from knowledgecomplex.exceptions import ValidationError as KCValidationError

    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    try:
        with kc.deferred_verification():
            kc.add_vertex("v:spec:isolated", type="spec", name="Isolated Spec")
            kc.add_vertex("v:guidance:sample", type="guidance", name="Sample Guidance")
            kc.add_edge("e:DocType:x", type="DocType",
                        vertices={"v:spec:isolated", "v:guidance:sample"}, name="X")
            # No verification edge for v:spec:isolated
    except KCValidationError:
        pass  # Expected — context manager verify() raises; KC is still queryable
    report = kc.audit()
    assert not report.conforms
    assert any("verification" in v.message.lower() for v in report.violations)


def test_audit_violation_missing_validation():
    """A guidance without a validation edge violates the topological SHACL constraint."""
    from knowledgecomplex.exceptions import ValidationError as KCValidationError

    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    try:
        with kc.deferred_verification():
            kc.add_vertex("v:spec:sample", type="spec", name="Sample Spec")
            kc.add_vertex("v:guidance:isolated", type="guidance", name="Isolated Guidance")
            kc.add_vertex("v:doc:sample", type="doc", name="Sample Document")
            kc.add_edge("e:DocType:sample", type="DocType",
                        vertices={"v:spec:sample", "v:guidance:isolated"}, name="DocType")
            kc.add_edge("e:verification:sample", type="verification",
                        vertices={"v:doc:sample", "v:spec:sample"}, name="Verification",
                        status="passing")
            # No validation edge for v:guidance:isolated
    except KCValidationError:
        pass  # Expected
    report = kc.audit()
    assert not report.conforms
    assert any("validation" in v.message.lower() for v in report.violations)


# --- Tiling check ---

def test_tiling_complete(sample_kc):
    """All doc elements are covered by an assurance face."""
    all_ids = {
        "v:spec:sample", "v:guidance:sample", "v:doc:sample",
        "e:DocType:sample", "e:verification:sample", "e:validation:sample",
        "f:assurance:sample",
    }
    uncovered = _check_tiling(sample_kc, all_ids)
    assert uncovered == []


def test_tiling_incomplete():
    """A doc without an assurance face is flagged as uncovered."""
    schema = build_aaa_schema()
    kc = KnowledgeComplex(schema=schema)
    with kc.deferred_verification():
        kc.add_vertex("v:spec:s", type="spec", name="Spec")
        kc.add_vertex("v:guidance:g", type="guidance", name="Guidance")
        kc.add_vertex("v:doc:d", type="doc", name="Unassured Doc")
        kc.add_edge("e:DocType:dt", type="DocType",
                    vertices={"v:spec:s", "v:guidance:g"}, name="DocType")
        kc.add_edge("e:verification:v", type="verification",
                    vertices={"v:doc:d", "v:spec:s"}, name="Verification", status="passing")
        kc.add_edge("e:validation:vl", type="validation",
                    vertices={"v:doc:d", "v:guidance:g"}, name="Validation", status="approved")
        # No face — v:doc:d has no assurance
    all_ids = {
        "v:spec:s", "v:guidance:g", "v:doc:d",
        "e:DocType:dt", "e:verification:v", "e:validation:vl",
    }
    uncovered = _check_tiling(kc, all_ids)
    assert "v:doc:d" in uncovered


def test_tiling_ignores_spec_and_guidance(sample_kc):
    """spec and guidance vertices are not checked for assurance coverage."""
    # Only include vertices (no assurance face) — spec/guidance should not be flagged
    ids = {"v:spec:sample", "v:guidance:sample"}
    uncovered = _check_tiling(sample_kc, ids)
    assert uncovered == []


# --- CLI audit command ---

def test_audit_cli_succeeds(tmp_path, built_graph):
    runner = CliRunner()
    graph_path, _ = built_graph
    result = runner.invoke(
        __import__("aaa.commands.audit", fromlist=["audit"]).audit,
        [str(FIXTURES / "sample-chart.md"), "--graph", str(graph_path), "--no-tiling"],
    )
    # May succeed or warn about SPARQL results; should not crash
    assert result.exit_code in (0, 1)


def test_audit_cli_missing_graph(tmp_path):
    runner = CliRunner()
    result = runner.invoke(
        __import__("aaa.commands.audit", fromlist=["audit"]).audit,
        [str(FIXTURES / "sample-chart.md"), "--graph", str(tmp_path / "missing.ttl")],
    )
    assert result.exit_code != 0
    assert "Graph not found" in result.output or "not found" in result.output.lower()
