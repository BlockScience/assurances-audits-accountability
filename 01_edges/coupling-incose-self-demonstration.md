---
type: edge/coupling
extends: edge
id: e:coupling:incose-self-demonstration
name: Coupling - Spec and Guidance for INCOSE Self-Demonstrating Paper
source: v:spec:incose-self-demonstration
target: v:guidance:incose-self-demonstration
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-30T21:00:00Z
modified: 2025-12-30T21:00:00Z
---

# Coupling - Spec and Guidance for INCOSE Self-Demonstrating Paper

**This coupling connects the specification and guidance for INCOSE self-demonstrating papers—papers that prove their framework by being instances of it.**

## Purpose

This coupling links the extended structural requirements for self-demonstrating papers with their quality criteria, enabling complete assurance of papers that make recursive self-proof claims. Together, these documents enable:

- **Verification:** Checking that a paper has all required supporting documents, maintains consistency across documents, and satisfies self-demonstration requirements (against [[spec-for-incose-self-demonstration]])
- **Validation:** Assessing whether the self-demonstration is coherent, credible, and compelling (against [[guidance-for-incose-self-demonstration]])

## Inheritance Relationship

This coupling extends the parent coupling `e:coupling:incose-paper`:

```
e:coupling:incose-paper
        ↑
        extends
        |
e:coupling:incose-self-demonstration (this edge)
```

A paper verified against `spec-for-incose-self-demonstration` inherits all parent spec requirements. A paper validated against `guidance-for-incose-self-demonstration` inherits all parent guidance criteria.

## Governed Document Type

Both documents govern self-demonstrating INCOSE papers—a specialized subtype of INCOSE papers characterized by:

- The paper IS an instance of the framework it describes
- Four supporting documents exist: architecture, lifecycle, literature review, novel contributions
- The paper's existence serves as proof of the framework's viability
- Recursive consistency between paper and supporting documents is required

## Role in Assurance Faces

This coupling forms the base of assurance faces where:

- Child docs are self-demonstrating papers (`type: vertex/doc` with self-demonstration claim)
- Verification edge: paper → spec-for-incose-self-demonstration
- Validation edge: paper → guidance-for-incose-self-demonstration
- Coupling edge: spec ↔ guidance (this edge)

## Assurance Triangle Structure

```
         self-demonstrating-paper
                   /\
                  /  \
     verification/    \validation
                /      \
               /        \
   spec-for-incose-    guidance-for-incose-
   self-demonstration ↔ self-demonstration
              (this coupling edge)
```

## Supporting Document Dependencies

Self-demonstrating papers require four supporting documents to exist:

| Supporting Document | Spec | Guidance |
|---------------------|------|----------|
| Architecture | `spec-for-architecture` | `guidance-for-architecture` |
| Lifecycle | `spec-for-lifecycle` | `guidance-for-lifecycle` |
| Literature Review | `spec-for-incose-literature-review` | `guidance-for-incose-literature-review` |
| Novel Contributions | `spec-for-novel-contributions` | `guidance-for-novel-contributions` |

The self-demonstrating paper assurance depends on these supporting documents being available and ideally assured themselves.

## Connection to Foundation

This coupling builds on the foundational boundary complex through inheritance:

- [[spec-for-incose-self-demonstration]] extends [[spec-for-incose-paper]] which is verified against [[spec-for-spec]]
- [[guidance-for-incose-self-demonstration]] extends [[guidance-for-incose-paper]] which is validated against [[guidance-for-guidance]]

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-incose-self-demonstration]] | v:spec:incose-self-demonstration |
| Target | [[guidance-for-incose-self-demonstration]] | v:guidance:incose-self-demonstration |
| Parent Coupling | [[coupling-incose-paper]] | e:coupling:incose-paper |

## Key Distinction

The parent type (`incose-paper`) is for any INCOSE paper submission.

This type (`incose-self-demonstration`) is for the special case where:
1. The paper describes a framework
2. The paper was produced using that framework
3. The paper's existence proves the framework works
4. Supporting documents provide the foundation the paper builds on

This coupling enables assurance of that recursive self-proof claim.

---

**Note:** This coupling enables self-demonstrating papers to be assured within the typed simplicial complex framework, supporting the meta-level claim that "the paper is its own proof" can be formally verified and validated.
