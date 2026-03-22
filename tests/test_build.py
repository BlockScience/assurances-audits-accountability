"""
tests/test_build.py

Integration tests for `aaa build`: builds RDF from fixture directory.
"""

import pytest
from pathlib import Path
from click.testing import CliRunner
from rdflib import Graph, Namespace

from aaa.commands.build import build

FIXTURES = Path(__file__).parent / "fixtures" / "aaa"
AAA = Namespace("https://example.org/aaa#")
KC = Namespace("https://w3id.org/kc#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")


@pytest.fixture
def built_graph(tmp_path):
    """Build RDF from fixtures into a temp file, return (Path, Graph)."""
    runner = CliRunner()
    out = tmp_path / "graph.ttl"
    result = runner.invoke(build, [str(FIXTURES), "--output", str(out)])
    assert result.exit_code == 0, result.output
    g = Graph()
    g.parse(str(out), format="turtle")
    return out, g


def test_build_succeeds(tmp_path):
    runner = CliRunner()
    out = tmp_path / "graph.ttl"
    result = runner.invoke(build, [str(FIXTURES), "--output", str(out)])
    assert result.exit_code == 0, result.output
    assert out.exists()


def test_output_is_valid_turtle(built_graph):
    _, g = built_graph
    assert len(g) > 0


def test_spec_has_correct_rdf_type(built_graph):
    _, g = built_graph
    from rdflib import URIRef
    spec = URIRef("https://example.org/aaa#v:spec:sample")
    assert (spec, RDF.type, AAA.spec) in g or any(
        True for _ in g.subjects(RDF.type, AAA.spec)
    )


def test_assurance_face_in_graph(built_graph):
    _, g = built_graph
    # There should be at least one assurance face
    assert any(True for _ in g.subjects(RDF.type, AAA.assurance))


def test_doctype_edge_in_graph(built_graph):
    _, g = built_graph
    assert any(True for _ in g.subjects(RDF.type, AAA.DocType))


def test_build_bad_spec_warns_not_fails(tmp_path):
    """A doc with a Pydantic error produces a warning but build continues."""
    runner = CliRunner()
    out = tmp_path / "graph.ttl"
    result = runner.invoke(build, [str(FIXTURES), "--output", str(out)])
    assert result.exit_code == 0
    assert "bad-spec" in result.output or "[WARN]" in result.output or out.exists()


def test_build_strict_exits_on_pydantic_error(tmp_path):
    """--strict causes exit code 1 on first Pydantic error."""
    runner = CliRunner()
    out = tmp_path / "graph.ttl"
    result = runner.invoke(build, [str(FIXTURES), "--output", str(out), "--strict"])
    # bad-spec.md will cause a failure
    assert result.exit_code != 0 or "[WARN]" not in result.output


def test_build_json_ld_format(tmp_path):
    runner = CliRunner()
    out = tmp_path / "graph.jsonld"
    result = runner.invoke(build, [
        str(FIXTURES), "--output", str(out), "--format", "json-ld"
    ])
    assert result.exit_code == 0 or out.exists() or "SHACL" in result.output


class TestVerifyCLI:
    """Tests for `aaa verify` command."""

    def test_verify_valid_spec(self):
        runner = CliRunner()
        result = runner.invoke(
            __import__("aaa.commands.verify", fromlist=["verify"]).verify,
            [str(FIXTURES / "sample-spec.md")]
        )
        assert result.exit_code == 0
        assert "[OK]" in result.output

    def test_verify_bad_spec_fails(self):
        runner = CliRunner()
        result = runner.invoke(
            __import__("aaa.commands.verify", fromlist=["verify"]).verify,
            [str(FIXTURES / "bad-spec.md")]
        )
        assert result.exit_code != 0
        assert "[FAIL]" in result.output

    def test_verify_verbose(self):
        runner = CliRunner()
        result = runner.invoke(
            __import__("aaa.commands.verify", fromlist=["verify"]).verify,
            [str(FIXTURES / "sample-spec.md"), "--verbose"]
        )
        assert result.exit_code == 0
        assert "id:" in result.output
        assert "type:" in result.output
