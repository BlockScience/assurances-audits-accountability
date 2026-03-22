"""
tests/test_schema.py

Tests for build_aaa_schema(): OWL/SHACL output, type hierarchy, topological constraints.
"""

import pytest
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDFS

from aaa.schema import build_aaa_schema

AAA = Namespace("https://example.org/aaa#")
KC = Namespace("https://w3id.org/kc#")


@pytest.fixture(scope="module")
def schema():
    return build_aaa_schema()


# --- OWL output ---

def test_dump_owl_is_valid_turtle(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert len(g) > 0


def test_doc_is_subclass_of_kc_vertex(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.doc, RDFS.subClassOf, KC.Vertex) in g


def test_spec_is_subclass_of_doc(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.spec, RDFS.subClassOf, AAA.doc) in g


def test_guidance_is_subclass_of_doc(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.guidance, RDFS.subClassOf, AAA.doc) in g


def test_chart_is_subclass_of_doc(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.chart, RDFS.subClassOf, AAA.doc) in g


def test_assurance_audit_is_subclass_of_chart(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.assurance_audit, RDFS.subClassOf, AAA.chart) in g


def test_verification_is_subclass_of_kc_edge(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.verification, RDFS.subClassOf, KC.Edge) in g


def test_assurance_is_subclass_of_kc_face(schema):
    g = Graph()
    g.parse(data=schema.dump_owl(), format="turtle")
    assert (AAA.assurance, RDFS.subClassOf, KC.Face) in g


def test_doctype_edge_declared(schema):
    owl = schema.dump_owl()
    assert "DocType" in owl


# --- SHACL output ---

def test_dump_shacl_is_valid_turtle(schema):
    g = Graph()
    g.parse(data=schema.dump_shacl(), format="turtle")
    assert len(g) > 0


def test_verification_status_vocab_in_shacl(schema):
    shacl = schema.dump_shacl()
    assert "passing" in shacl
    assert "failing" in shacl
    assert "pending" in shacl


def test_validation_status_vocab_in_shacl(schema):
    shacl = schema.dump_shacl()
    assert "approved" in shacl
    assert "rejected" in shacl


def test_assurance_status_vocab_in_shacl(schema):
    shacl = schema.dump_shacl()
    assert "assured" in shacl
    assert "failed" in shacl


def test_topological_constraints_in_shacl(schema):
    shacl = schema.dump_shacl()
    # spec→verification and guidance→validation constraints are global
    assert "verification" in shacl
    assert "validation" in shacl
    # NOTE: doc→assurance tiling is NOT a global SHACL constraint;
    # it is enforced by `aaa audit` within chart scope only.


def test_chart_query_attribute_in_shacl(schema):
    shacl = schema.dump_shacl()
    assert "query" in shacl


def test_doctype_name_required_in_shacl(schema):
    shacl = schema.dump_shacl()
    assert "DocType" in shacl


# --- Round-trip: SchemaBuilder → KC constructor ---

def test_schema_powers_knowledge_complex(schema):
    from knowledgecomplex import KnowledgeComplex
    kc = KnowledgeComplex(schema=schema)
    # Use deferred_verification so SHACL runs once after the full triangle is built,
    # not eagerly after each individual element insertion.
    with kc.deferred_verification():
        kc.add_vertex("s1", type="spec", name="Spec One")
        kc.add_vertex("g1", type="guidance", name="Guidance One")
        kc.add_vertex("d1", type="doc", name="Doc One")
        kc.add_edge("dt1", type="DocType", vertices={"s1", "g1"}, name="Doc One Type")
        kc.add_edge("ver1", type="verification", vertices={"d1", "s1"}, status="passing")
        kc.add_edge("val1", type="validation", vertices={"d1", "g1"}, status="approved")
        kc.add_face(
            "a1", type="assurance",
            boundary=["ver1", "val1", "dt1"],
            doc_name="Doc One", signed_by="Alice", status="assured",
        )
    # No ValidationError expected — all constraints satisfied at exit
    assert "s1" in kc.element_ids(type="spec")
    assert "dt1" in kc.element_ids(type="DocType")
    assert "a1" in kc.element_ids(type="assurance")
