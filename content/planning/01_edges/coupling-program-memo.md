---
type: edge/coupling
extends: edge
id: e:coupling:program-memo
name: Coupling - Spec-for-Program-Memo and Guidance-for-Program-Memo
source: v:spec:program-memo
target: v:guidance:program-memo
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-01-04T15:00:00Z
modified: 2025-01-04T15:00:00Z
---

# Coupling - Spec-for-Program-Memo and Guidance-for-Program-Memo

**This coupling connects the specification for program memo documents with the guidance for program memo quality.**

## Purpose

This coupling links the structural requirements for program memo documents with their quality criteria, enabling complete assurance of executive summary documentation. Together, these documents enable:

- **Verification:** Checking that a program memo has required sections, source references, and navigation elements (against [[spec-for-program-memo]])
- **Validation:** Assessing whether a program memo effectively synthesizes source documents and serves executive audiences (against [[guidance-for-program-memo]])

## Governed Document Type

Both documents govern all program memo documents in the knowledge complex. Program memos serve as executive primers for documentation packages consisting of:
- Architecture document (what we're building)
- Lifecycle document (how we're building it)
- Program plan document (execution details)

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are program memo documents (`type: vertex/doc` with `program-memo` tag)
- Verification edge: program-memo → spec-for-program-memo
- Validation edge: program-memo → guidance-for-program-memo
- Coupling edge: spec-for-program-memo ↔ guidance-for-program-memo (this edge)

## Assurance Triangle Structure

```
               program-memo-doc
                     /\
                    /  \
       verification/    \validation
                  /      \
                 /        \
    spec-for-program-memo ↔ guidance-for-program-memo
              (this coupling edge)
```

## Connection to Foundation

This coupling builds on the foundational boundary complex:

- [[spec-for-program-memo]] verified against [[spec-for-spec]]
- [[spec-for-program-memo]] validated against [[guidance-for-spec]]
- [[guidance-for-program-memo]] verified against [[spec-for-guidance]]
- [[guidance-for-program-memo]] validated against [[guidance-for-guidance]]

## Document Package Integration

Program memo documents synthesize content from three source documents:

| Source Document | Memo Section | Content Drawn |
|-----------------|--------------|---------------|
| Architecture | What We're Building | Conceptual layer, logical layer (summary), acceptance criteria |
| Lifecycle | How We're Building It | Phase overview, V&V approach |
| Program Plan | Execution Summary | Milestones, resources, top risks |

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-program-memo]] | v:spec:program-memo |
| Target | [[guidance-for-program-memo]] | v:guidance:program-memo |

---

**Note:** This coupling enables program memo documents to be assured within the typed simplicial complex framework, supporting executive communication of documentation packages.
