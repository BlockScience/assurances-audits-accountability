---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-spec:novel-contributions-spec
name: Dependency - Self-Demonstration Spec requires Novel Contributions Spec
description: Self-demonstrating papers must have a novel contributions document conforming to spec-for-novel-contributions
source: v:spec:incose-self-demonstration
target: v:spec:novel-contributions
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: supporting_document
subsection_field: supporting_documents.novel_contributions
required: true
tags:
  - edge
  - dependency
  - self-demonstration
version: 1.0.0
created: 2025-12-30T22:00:00Z
modified: 2025-12-30T22:00:00Z
---

# Dependency - Self-Demonstration Spec requires Novel Contributions Spec

**Self-demonstrating INCOSE papers require a novel contributions document that conforms to the novel contributions specification.**

## Dependency Relationship

**Dependent:** `v:spec:incose-self-demonstration` (Specification for Self-Demonstrating Papers)
**Dependency:** `v:spec:novel-contributions` (Specification for Novel Contributions Documents)
**Relationship:** Self-demonstration spec requires novel contributions spec (supporting document dependency)

**Usage:** Self-demonstrating papers must have a novel contributions document available at time of production. This document articulates what is new, differentiating, and valuable about the work—providing the authoritative source for contribution claims in the paper.

**Assurance Note:** This dependency edge tracks compositional requirements and is separate from the assurance DAG. For assurance, `spec-for-incose-self-demonstration` verifies against `spec-for-spec` (because it is a spec), not against `spec-for-novel-contributions`.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `supporting_documents.novel_contributions` in paper metadata |
| **Required** | Yes - novel contributions document MUST exist |
| **Cardinality** | One novel contributions document per self-demonstrating paper |
| **Assurance Status** | Novel contributions SHOULD be assured before paper finalization |

### Consistency Checks Enabled

This dependency enables the following consistency checks (from spec-for-incose-self-demonstration):

| Check | Description |
|-------|-------------|
| C4.1 | All claimed contributions in paper MUST appear in novel contributions document |
| C4.2 | Novelty claims MUST NOT exceed those in novel contributions document |
| C4.3 | Differentiation from prior work MUST match novel contributions analysis |
| C4.4 | Evidence cited for novelty MUST match novel contributions document |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers must make clear, defensible contribution claims. The novel contributions document provides:

1. **Contribution Statements** → Precise articulation of what is new
2. **Differentiation Analysis** → How contributions differ from prior work
3. **Evidence Mapping** → What evidence supports each contribution claim
4. **Novelty Justification** → Why these contributions matter

Without a novel contributions document, contribution claims in the paper would be informal and potentially inconsistent. The document serves as the "single source of truth" for what the paper claims to contribute.

### Difference from Inheritance

This is a **uses/has-a** relationship, not an **is-a** relationship:
- Self-demonstration spec is NOT a specialized kind of novel contributions spec
- Self-demonstration spec USES novel contributions spec to define what supporting document is needed
- The novel contributions document is a required component, not a parent type

### Difference from Assurance

This is a **compositional** relationship, not an **assurance** relationship:
- Self-demonstration spec does NOT verify against novel contributions spec
- Self-demonstration spec verifies against spec-for-spec (because it's a spec)
- This dependency captures requirements for supporting documents, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Direction: arrow from self-demonstration-spec toward novel-contributions-spec

---

**Note:** This dependency is one of four supporting document dependencies for self-demonstrating papers. The others are: architecture, lifecycle, and literature-review.