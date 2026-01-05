---
type: edge/coupling
extends: edge
id: e:coupling:program-plan
name: Coupling - Spec-for-Program-Plan and Guidance-for-Program-Plan
source: v:spec:program-plan
target: v:guidance:program-plan
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2026-01-04T22:00:00Z
modified: 2026-01-04T22:00:00Z
---

# Coupling - Spec-for-Program-Plan and Guidance-for-Program-Plan

**This coupling connects the specification for program plan documents with the guidance for program plan quality.**

## Purpose

This coupling links the structural requirements for program plan documents with their quality criteria, enabling complete assurance of execution planning documentation. Together, these documents enable:

- **Verification:** Checking that a program plan has required sections (Executive Summary, Scope and Objectives, WBS, Schedule, Resources, Risks, Stakeholders, QA, Communication, Governance) and proper references to architecture and lifecycle documents (against [[spec-for-program-plan]])
- **Validation:** Assessing whether a program plan is realistic, actionable, properly traces to architecture/lifecycle, and has appropriate governance (against [[guidance-for-program-plan]])

## Governed Document Type

Both documents govern all program plan documents in the knowledge complex. Program plans define how to execute the delivery of a system defined by:
- Field survey document (operational context)
- Architecture document (what we're building)
- Lifecycle document (how we're building it)

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are program plan documents (`type: vertex/doc` with `program-plan` tag)
- Verification edge: program-plan → spec-for-program-plan
- Validation edge: program-plan → guidance-for-program-plan
- Coupling edge: spec-for-program-plan ↔ guidance-for-program-plan (this edge)

## Assurance Triangle Structure

```
               program-plan-doc
                     /\
                    /  \
       verification/    \validation
                  /      \
                 /        \
    spec-for-program-plan ↔ guidance-for-program-plan
              (this coupling edge)
```

## Connection to Foundation

This coupling builds on the foundational boundary complex:

- [[spec-for-program-plan]] verified against [[spec-for-spec]]
- [[spec-for-program-plan]] validated against [[guidance-for-spec]]
- [[guidance-for-program-plan]] verified against [[spec-for-guidance]]
- [[guidance-for-program-plan]] validated against [[guidance-for-guidance]]

## V-Model Alignment

Program plan documents align with the V-model approach:

| Program Plan Element | V-Model Connection |
|---------------------|-------------------|
| Objectives | Trace to architecture acceptance criteria |
| Milestones | Align with lifecycle phase gates |
| QA section | References V-model verification approach |
| Governance | Oversight for V&V activities |

## Document References

| Role | Document | ID |
|------|----------|-----|
| Source | [[spec-for-program-plan]] | v:spec:program-plan |
| Target | [[guidance-for-program-plan]] | v:guidance:program-plan |

---

**Note:** This coupling enables program plan documents to be assured within the typed simplicial complex framework, supporting execution planning that traces to architecture and lifecycle.
