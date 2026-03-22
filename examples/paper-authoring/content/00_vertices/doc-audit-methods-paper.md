---
type: vertex/doc
id: v:doc:audit-methods-paper
name: Topological Audit Methods for Large Document Corpora
version: "1.0"
description: >
  We address the problem of audit completeness verification for large
  corpora of engineering documents. Our approach uses simplicial complex
  tiling: a corpus is completely audited when every document vertex is
  covered by at least one assurance face. We give an algorithm based on
  SPARQL-materialized subcomplexes and prove that tiling completeness
  is decidable in linear time in the number of assurance faces.
tags:
  - doc
  - paper
  - audit
  - topology
---

# Topological Audit Methods for Large Document Corpora

## Abstract

Verifying that every document in a large corpus has been properly assured
is a significant operational challenge. We show that this audit completeness
problem is equivalent to checking whether a simplicial complex is completely
tiled by its maximal faces. We present a SPARQL-based algorithm that
materializes the relevant subcomplex and checks tiling in O(|F|) time,
where F is the number of assurance faces. The approach is implemented in
the AAA framework and validated on engineering program corpora.

## Introduction

In engineering programs managing hundreds of documents across multiple
lifecycle phases, tracking audit completeness manually is error-prone.
The core question — "has every document been assured?" — is deceptively
simple but requires checking a complex web of dependencies.

We claim: (1) audit completeness is a tiling problem on a simplicial
complex; (2) SPARQL queries can materialize the relevant subcomplex
without loading individual documents; (3) tiling completeness checking
is efficient and formally verifiable.

## Approach

We define the tiling completeness problem formally: a subcomplex S is
completely tiled if every doc-type vertex in S is in the star of at least
one assurance face. We implement this check using the KC star operator
and demonstrate it on the paper-authoring example.

## Results

The tiling algorithm correctly identifies covered and uncovered documents.
When all assurance faces are present, the algorithm reports complete tiling.
When an assurance face is missing, the algorithm identifies the specific
uncovered document, enabling targeted remediation.

## Conclusion

Topological tiling completeness provides a formal criterion for audit
completeness that is both computationally efficient and semantically clear.
Limitations: the approach assumes all assurance faces are in the same KC;
distributed corpora require KC federation. Future work includes streaming
audit updates as new documents are added.

## References

- Hatcher & Topology, "Algebraic Topology," Cambridge 2002
- Zargham et al., "Knowledge Complexes," arXiv 2025
- SPARQL 1.1 Query Language, W3C Recommendation, 2013
