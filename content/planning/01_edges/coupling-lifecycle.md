---
type: edge/coupling
extends: edge
id: e:coupling:lifecycle
name: Coupling - Spec-for-Lifecycle and Guidance-for-Lifecycle
source: v:spec:lifecycle
target: v:guidance:lifecycle
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-30T18:00:00Z
modified: 2025-12-30T18:00:00Z
---

# Coupling - Spec-for-Lifecycle and Guidance-for-Lifecycle

**This coupling connects the specification for lifecycle documents with the guidance for lifecycle document quality.**

## Purpose

This coupling links the structural requirements for lifecycle documents with their quality criteria, enabling complete assurance of engineering process documentation. Together, these documents enable:

- **Verification:** Checking that a lifecycle document has required phases, flowchart, narrative (against [[spec-for-lifecycle]])
- **Validation:** Assessing whether a lifecycle is clear, complete, actionable, and fit-for-purpose (against [[guidance-for-lifecycle]])

## Governed Document Type

Both documents govern all lifecycle documents in the knowledge complex, including:
- lifecycle-incose-paper (the concrete instance documenting INCOSE paper development)
- Any future lifecycle documents for other artifact types

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are lifecycle documents (`type: vertex/doc` with `lifecycle` tag)
- Verification edge: lifecycle → spec-for-lifecycle
- Validation edge: lifecycle → guidance-for-lifecycle
- Coupling edge: spec-for-lifecycle ↔ guidance-for-lifecycle (this edge)

## Assurance Triangle Structure

```
                lifecycle-doc
                     /\
                    /  \
       verification/    \validation
                  /      \
                 /        \
    spec-for-lifecycle ←→ guidance-for-lifecycle
              (this coupling edge)
```

## Connection to Foundation

This coupling builds on the foundational boundary complex:

- [[spec-for-lifecycle]] verified against [[spec-for-spec]]
- [[spec-for-lifecycle]] validated against [[guidance-for-spec]]
- [[guidance-for-lifecycle]] verified against [[spec-for-guidance]]
- [[guidance-for-lifecycle]] validated against [[guidance-for-guidance]]

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-lifecycle]] | v:spec:lifecycle |
| Target | [[guidance-for-lifecycle]] | v:guidance:lifecycle |

---

**Note:** This coupling enables lifecycle documents to be assured within the typed simplicial complex framework, supporting the meta-documentation of engineering processes.
