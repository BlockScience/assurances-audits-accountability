---
type: edge/coupling
extends: edge
id: e:coupling:incose-literature-review
name: Coupling - Spec and Guidance for INCOSE Literature Reviews
source: v:spec:incose-literature-review
target: v:guidance:incose-literature-review
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-30T19:00:00Z
modified: 2025-12-30T19:00:00Z
---

# Coupling - Spec and Guidance for INCOSE Literature Reviews

**This coupling connects the specification for INCOSE literature review documents with the guidance for literature review quality.**

## Purpose

This coupling links the structural requirements for literature reviews with their quality criteria, enabling complete assurance of research support artifacts. Together, these documents enable:

- **Verification:** Checking that a literature review has required themes, citation catalog, gap analysis (against [[spec-for-incose-literature-review]])
- **Validation:** Assessing whether sources are appropriate, synthesis is insightful, and gaps are meaningful (against [[guidance-for-incose-literature-review]])

## Governed Document Type

Both documents govern all INCOSE literature review documents in the knowledge complex, including:
- Literature reviews supporting INCOSE paper submissions
- Background research artifacts for systems engineering papers

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are literature review documents (`type: vertex/doc` with `literature-review` tag)
- Verification edge: literature-review → spec-for-incose-literature-review
- Validation edge: literature-review → guidance-for-incose-literature-review
- Coupling edge: spec ↔ guidance (this edge)

## Assurance Triangle Structure

```
              literature-review-doc
                     /\
                    /  \
       verification/    \validation
                  /      \
                 /        \
    spec-for-incose-    guidance-for-incose-
    literature-review ↔ literature-review
              (this coupling edge)
```

## Connection to Foundation

This coupling builds on the foundational boundary complex:

- [[spec-for-incose-literature-review]] verified against [[spec-for-spec]]
- [[spec-for-incose-literature-review]] validated against [[guidance-for-spec]]
- [[guidance-for-incose-literature-review]] verified against [[spec-for-guidance]]
- [[guidance-for-incose-literature-review]] validated against [[guidance-for-guidance]]

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-incose-literature-review]] | v:spec:incose-literature-review |
| Target | [[guidance-for-incose-literature-review]] | v:guidance:incose-literature-review |

---

**Note:** This coupling enables literature review documents to be assured within the typed simplicial complex framework, supporting traceable scholarly foundations for INCOSE papers.
