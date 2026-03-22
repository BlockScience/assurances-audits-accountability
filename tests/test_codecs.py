"""
tests/test_codecs.py

Tests for AAA Pydantic models and Codecs using fixture markdown files.
"""

from pathlib import Path

import pytest
from pydantic import ValidationError

from aaa.codecs import (
    AssuranceCodec,
    ChartCodec,
    DocCodec,
    DocTypeCodec,
    GuidanceCodec,
    SpecCodec,
    ValidationCodec,
    VerificationCodec,
    codec_for_type,
    dimension_for_type,
    short_type,
)

FIXTURES = Path(__file__).parent / "fixtures" / "aaa"


def uri(filename: str) -> str:
    return (FIXTURES / filename).as_uri()


# --- codec_for_type registry ---


def test_codec_for_spec():
    assert isinstance(codec_for_type("vertex/spec"), SpecCodec)


def test_codec_for_doctype():
    assert isinstance(codec_for_type("DocType"), DocTypeCodec)


def test_codec_for_assurance():
    assert isinstance(codec_for_type("face/assurance"), AssuranceCodec)


def test_codec_for_unknown_falls_back_to_doc():
    assert isinstance(codec_for_type("vertex/some_future_type"), DocCodec)


# --- dimension_for_type ---


def test_dimension_vertex():
    assert dimension_for_type("vertex/spec") == "vertex"


def test_dimension_edge():
    assert dimension_for_type("edge/verification") == "edge"


def test_dimension_face():
    assert dimension_for_type("face/assurance") == "face"


def test_dimension_short_name_vertex():
    assert dimension_for_type("doc") == "vertex"


def test_dimension_short_name_edge():
    assert dimension_for_type("DocType") == "edge"


# --- short_type ---


def test_short_type_strips_prefix():
    assert short_type("vertex/spec") == "spec"
    assert short_type("edge/verification") == "verification"
    assert short_type("face/assurance") == "assurance"


def test_short_type_passthrough():
    assert short_type("spec") == "spec"


# --- SpecCodec ---


class TestSpecCodec:
    def test_decompile_valid(self):
        attrs = SpecCodec().decompile(uri("sample-spec.md"))
        assert attrs["id"] == "v:spec:sample"
        assert attrs["name"] == "Sample Spec"
        assert attrs["type"] == "vertex/spec"

    def test_decompile_missing_name_raises(self):
        with pytest.raises(ValidationError):
            SpecCodec().decompile(uri("bad-spec.md"))

    def test_decompile_returns_all_frontmatter(self):
        attrs = SpecCodec().decompile(uri("sample-spec.md"))
        assert "version" in attrs
        assert "description" in attrs


# --- GuidanceCodec ---


class TestGuidanceCodec:
    def test_decompile_valid(self):
        attrs = GuidanceCodec().decompile(uri("sample-guidance.md"))
        assert attrs["id"] == "v:guidance:sample"


# --- DocCodec ---


class TestDocCodec:
    def test_decompile_valid(self):
        attrs = DocCodec().decompile(uri("sample-doc.md"))
        assert attrs["name"] == "Sample Document"


# --- ChartCodec ---


class TestChartCodec:
    def test_decompile_valid(self):
        attrs = ChartCodec().decompile(uri("sample-chart.md"))
        assert "query" in attrs
        assert "SELECT" in attrs["query"].upper()

    def test_invalid_sparql_raises(self, tmp_path):
        bad = tmp_path / "bad-chart.md"
        bad.write_text(
            "---\ntype: vertex/chart\nid: v:chart:bad\nname: Bad\nquery: not sparql\n---\n"
        )
        with pytest.raises(ValidationError, match="SPARQL"):
            ChartCodec().decompile(bad.as_uri())


# --- VerificationCodec ---


class TestVerificationCodec:
    def test_decompile_valid(self):
        attrs = VerificationCodec().decompile(uri("sample-verification.md"))
        assert attrs["status"] == "passing"
        assert attrs["source"] == "v:doc:sample"
        assert attrs["target"] == "v:spec:sample"

    def test_invalid_status_raises(self, tmp_path):
        bad = tmp_path / "bad-ver.md"
        bad.write_text(
            "---\ntype: edge/verification\nid: e:v:bad\nname: Bad\n"
            "source: a\ntarget: b\nstatus: unknown\n---\n"
        )
        with pytest.raises(ValidationError):
            VerificationCodec().decompile(bad.as_uri())

    def test_same_source_target_raises(self, tmp_path):
        bad = tmp_path / "loop-ver.md"
        bad.write_text(
            "---\ntype: edge/verification\nid: e:v:loop\nname: Loop\n"
            "source: x\ntarget: x\nstatus: passing\n---\n"
        )
        with pytest.raises(ValidationError, match="differ"):
            VerificationCodec().decompile(bad.as_uri())


# --- ValidationCodec ---


class TestValidationCodec:
    def test_decompile_valid(self):
        attrs = ValidationCodec().decompile(uri("sample-validation.md"))
        assert attrs["status"] == "approved"
        assert attrs["signed_by"] == "Alice"


# --- DocTypeCodec ---


class TestDocTypeCodec:
    def test_decompile_valid(self):
        attrs = DocTypeCodec().decompile(uri("sample-doctype.md"))
        assert attrs["source"] == "v:spec:sample"
        assert attrs["target"] == "v:guidance:sample"
        assert attrs["name"] == "Sample DocType"


# --- AssuranceCodec ---


class TestAssuranceCodec:
    def test_decompile_valid(self):
        attrs = AssuranceCodec().decompile(uri("sample-assurance.md"))
        assert attrs["doc_name"] == "Sample Document"
        assert attrs["signed_by"] == "Alice"
        assert attrs["status"] == "assured"
        assert len(attrs["edges"]) == 3

    def test_wrong_edge_count_raises(self, tmp_path):
        bad = tmp_path / "bad-assurance.md"
        bad.write_text(
            "---\ntype: face/assurance\nid: f:a:bad\nname: Bad\n"
            "edges: [e1, e2]\ndoc_name: X\nsigned_by: Y\nstatus: assured\n---\n"
        )
        with pytest.raises(ValidationError):
            AssuranceCodec().decompile(bad.as_uri())

    def test_invalid_status_raises(self, tmp_path):
        bad = tmp_path / "bad-status.md"
        bad.write_text(
            "---\ntype: face/assurance\nid: f:a:bad\nname: Bad\n"
            "edges: [e1, e2, e3]\ndoc_name: X\nsigned_by: Y\nstatus: unknown\n---\n"
        )
        with pytest.raises(ValidationError):
            AssuranceCodec().decompile(bad.as_uri())


# --- compile round-trip ---


class TestCompileRoundTrip:
    def test_roundtrip_spec(self, tmp_path):
        src = FIXTURES / "sample-spec.md"
        dst = tmp_path / "spec.md"
        dst.write_text(src.read_text())
        codec = SpecCodec()
        attrs = codec.decompile(dst.as_uri())
        attrs["uri"] = dst.as_uri()
        codec.compile(attrs)
        attrs2 = codec.decompile(dst.as_uri())
        assert attrs2["id"] == attrs["id"]
        assert attrs2["name"] == attrs["name"]
