---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-spec:literature-review-spec
name: Dependency - Self-Demonstration Spec requires Literature Review Spec
description: Self-demonstrating papers must have a literature review document conforming to spec-for-incose-literature-review
source: v:spec:incose-self-demonstration
target: v:spec:incose-literature-review
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: supporting_document
subsection_field: supporting_documents.literature_review
required: true
tags:
  - edge
  - dependency
  - self-demonstration
version: 1.0.0
created: 2025-12-30T22:00:00Z
modified: 2025-12-30T22:00:00Z
---

# Dependency - Self-Demonstration Spec requires Literature Review Spec

**Self-demonstrating INCOSE papers require a literature review document that conforms to the literature review specification.**

## Dependency Relationship

**Dependent:** `v:spec:incose-self-demonstration` (Specification for Self-Demonstrating Papers)
**Dependency:** `v:spec:incose-literature-review` (Specification for Literature Review Documents)
**Relationship:** Self-demonstration spec requires literature review spec (supporting document dependency)

**Usage:** Self-demonstrating papers must have a literature review document available at time of production. The literature review provides the scholarly foundation, citation catalog, and gap analysis that positions the paper's contribution.

**Assurance Note:** This dependency edge tracks compositional requirements and is separate from the assurance DAG. For assurance, `spec-for-incose-self-demonstration` verifies against `spec-for-spec` (because it is a spec), not against `spec-for-incose-literature-review`.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `supporting_documents.literature_review` in paper metadata |
| **Required** | Yes - literature review document MUST exist |
| **Cardinality** | One literature review document per self-demonstrating paper |
| **Assurance Status** | Literature review SHOULD be assured before paper finalization |

### Consistency Checks Enabled

This dependency enables the following consistency checks (from spec-for-incose-self-demonstration):

| Check | Description |
|-------|-------------|
| C3.1 | All citations in paper MUST appear in literature review catalog (or be explicitly new) |
| C3.2 | Gap analysis from literature review MUST align with paper's contribution claims |
| C3.3 | Thematic organization in literature review SHOULD inform Background structure |
| C3.4 | Positioning statement from literature review MUST be consistent with paper's positioning |
| C3.5 | Citation count in paper SHOULD be ≥ literature review theme count × 2 |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers must demonstrate scholarly rigor by building on existing work. The literature review document provides:

1. **Citation Catalog** → Authoritative source list the paper draws from
2. **Thematic Organization** → Structure that should inform paper's Background section
3. **Gap Analysis** → Identification of what's missing that the paper addresses
4. **Positioning** → How the contribution fits within the field

Without a literature review document, the paper's scholarly positioning would be ad-hoc and unverifiable against a systematic analysis.

### Difference from Inheritance

This is a **uses/has-a** relationship, not an **is-a** relationship:
- Self-demonstration spec is NOT a specialized kind of literature review spec
- Self-demonstration spec USES literature review spec to define what supporting document is needed
- The literature review document is a required component, not a parent type

### Difference from Assurance

This is a **compositional** relationship, not an **assurance** relationship:
- Self-demonstration spec does NOT verify against literature review spec
- Self-demonstration spec verifies against spec-for-spec (because it's a spec)
- This dependency captures requirements for supporting documents, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Direction: arrow from self-demonstration-spec toward literature-review-spec

---

**Note:** This dependency is one of four supporting document dependencies for self-demonstrating papers. The others are: architecture, lifecycle, and novel-contributions.