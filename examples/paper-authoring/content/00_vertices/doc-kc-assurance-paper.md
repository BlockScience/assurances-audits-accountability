---
type: vertex/doc
id: v:doc:kc-assurance-paper
name: Knowledge Complexes for Structured Document Assurance
version: "1.0"
description: >
  We present a simplicial complex approach to document type definition
  and assurance. Document types are edges (DocType) in a knowledge complex
  connecting structural specifications to quality guidance. Assurance is
  represented as a closed triangle (face) proving structural compliance,
  quality validation, and type coherence simultaneously. We demonstrate
  the framework on a corpus of engineering program documents and show
  that topological tiling completeness is equivalent to audit completeness.
tags:
  - doc
  - paper
  - knowledge-complex
  - assurance
---

# Knowledge Complexes for Structured Document Assurance

## Abstract

We present a framework in which document types, structural requirements,
quality guidance, and assurance attestations are all first-class elements
of a simplicial complex. A document type is an edge (DocType) connecting a
specification vertex to a guidance vertex. A document is assured when its
verification edge, validation edge, and DocType edge form a closed triangle
— an assurance face. This topological structure enables compositional
auditing: completeness of assurance over a corpus reduces to a tiling check
on a subcomplex materialized by a SPARQL query.

## Introduction

Document quality assurance in engineering programs typically relies on
ad-hoc checklists and manual review processes. The core problem is the
lack of a formal structure that connects structural requirements (what a
document must contain) to quality criteria (how well it must be written)
to attestation (proof that both were satisfied).

We claim: (1) document types are most naturally represented as edges in
a knowledge graph connecting specs to guidance; (2) assurance is a
topological closure property, not a binary flag; (3) audit completeness
over a corpus is equivalent to tiling completeness of a simplicial complex.

## Approach

We define the AAA (Assurances, Audits, Accountability) framework using the
knowledgecomplex library as a backend. The framework declares three simplex
types: Vertex (documents, specs, guidance), Edge (verification, validation,
DocType), and Face (assurance). SHACL constraints enforce topological
invariants at the graph level; Pydantic validates individual documents.

## Results

We demonstrate the framework on two conference papers about knowledge
complexes. Both papers achieve full assurance through the triangle pattern.
The paper-series chart materializes the complete subcomplex via SPARQL
and confirms tiling completeness. Euler characteristic χ = 2 (two
components: main complex + chart vertex).

## Conclusion

The simplicial complex representation of document assurance provides a
mathematically rigorous foundation for audit completeness. Limitations:
the current framework does not handle time-ordered revisions or partial
assurance. Future work includes filtration-based audit trails.

## References

- Zargham et al., "Knowledge Complexes," arXiv 2025
- OWL 2 Web Ontology Language, W3C Recommendation, 2012
- SHACL, W3C Recommendation, 2017
