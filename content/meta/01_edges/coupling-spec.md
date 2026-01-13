---
type: edge/coupling
extends: edge
id: e:coupling:spec
name: Coupling - Spec-for-Spec and Guidance-for-Spec
source: v:spec:spec
target: v:guidance:spec
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-27T16:30:00Z
modified: 2025-12-27T16:30:00Z
---

# Coupling - Spec-for-Spec and Guidance-for-Spec

**This coupling connects the specification that defines all specifications with the guidance that defines specification quality criteria.**

## Purpose

This coupling is foundational to the knowledge complex's boundary complex. Together, these documents enable:

- **Verification:** Checking that a spec document has required fields and structure (against [spec-for-spec](../00_vertices/spec-for-spec.md))
- **Validation:** Assessing whether a spec document is clear, complete, testable, and maintainable (against [guidance-for-spec](../00_vertices/guidance-for-spec.md))

## Governed Document Type

Both documents govern all specification documents in the knowledge complex, including:
- spec-for-spec itself (self-referential)
- spec-for-guidance
- All other spec documents

## Self-Referential Property

This coupling is part of the boundary complex's self-referential foundation:

```
        SS ←→ GS (this edge)
         ↕     ↕
        SG ←→ GG
```

Where:
- **SS** = spec-for-spec ([source](../00_vertices/spec-for-spec.md))
- **GS** = guidance-for-spec ([target](../00_vertices/guidance-for-spec.md))
- **SG** = spec-for-guidance
- **GG** = guidance-for-guidance

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are specifications
- Verification edge: spec → spec-for-spec
- Validation edge: spec → guidance-for-spec
- Coupling edge: spec-for-spec ↔ guidance-for-spec (this edge)

Example: The spec-for-guidance document can form an assurance face with this coupling as its base.

## Semantic Alignment

The structural requirements in spec-for-spec align with the quality criteria in guidance-for-spec:

| Spec-for-Spec Requires | Guidance-for-Spec Assesses |
|-------------------------|----------------------------|
| Purpose section | Clarity of purpose statement |
| Required fields table | Completeness of requirements |
| Schema definition | Testability of schema |
| Validation rules | Consistency of rules |
| Examples | Quality of examples |

Together, they provide comprehensive coverage of what makes a specification both **valid** (structurally) and **excellent** (qualitatively).

## Bootstrap Significance

This coupling is created before any assurance faces exist, establishing the foundation upon which all future assurance relationships will be built. It demonstrates the knowledge complex's self-describing property.
