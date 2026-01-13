---
type: edge/coupling
extends: edge
id: e:coupling:guidance
name: Coupling - Spec-for-Guidance and Guidance-for-Guidance
source: v:spec:guidance
target: v:guidance:guidance
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

# Coupling - Spec-for-Guidance and Guidance-for-Guidance

**This coupling connects the specification that defines all guidance documents with the guidance that defines guidance document quality criteria.**

## Purpose

This coupling is foundational to the knowledge complex's boundary complex. Together, these documents enable:

- **Verification:** Checking that a guidance document has required fields and structure (against [spec-for-guidance](../00_vertices/spec-for-guidance.md))
- **Validation:** Assessing whether a guidance document is empathetic, actionable, comprehensive, and usable (against [guidance-for-guidance](../00_vertices/guidance-for-guidance.md))

## Governed Document Type

Both documents govern all guidance documents in the knowledge complex, including:
- guidance-for-guidance itself (self-referential)
- guidance-for-spec
- All other guidance documents

## Self-Referential Property

This coupling is part of the boundary complex's self-referential foundation:

```
        SS ←→ GS
         ↕     ↕
        SG ←→ GG (this edge)
```

Where:
- **SS** = spec-for-spec
- **GS** = guidance-for-spec
- **SG** = spec-for-guidance ([source](../00_vertices/spec-for-guidance.md))
- **GG** = guidance-for-guidance ([target](../00_vertices/guidance-for-guidance.md))

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are guidance documents
- Verification edge: guidance → spec-for-guidance
- Validation edge: guidance → guidance-for-guidance
- Coupling edge: spec-for-guidance ↔ guidance-for-guidance (this edge)

Example: The guidance-for-spec document can form an assurance face with this coupling as its base.

## Semantic Alignment

The structural requirements in spec-for-guidance align with the quality criteria in guidance-for-guidance:

| Spec-for-Guidance Requires | Guidance-for-Guidance Assesses |
|----------------------------|-------------------------------|
| Purpose section | Clarity and empathy of purpose |
| Quality Criteria (≥3) | Comprehensiveness of criteria |
| Leveled assessment | Meaningfulness of quality levels |
| Section-by-Section Guidance | Actionability of advice |
| Workflow Guidance | Usability of workflow |
| Best Practices (≥5 if present) | Specificity of practices |

Together, they provide comprehensive coverage of what makes a guidance document both **valid** (structurally) and **excellent** (qualitatively).

## Bootstrap Significance

This coupling is created before any assurance faces exist, establishing the foundation upon which all future assurance relationships will be built. It completes the boundary complex's coupling structure, demonstrating the knowledge complex's self-describing property.

## Symmetry with Coupling-Spec

This coupling mirrors the structure of coupling-spec:
- Both connect a spec with its corresponding guidance
- Both are part of the boundary complex
- Both enable verification and validation of foundational document types
- Together, they establish the complete self-referential framework
