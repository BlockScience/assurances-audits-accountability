---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-guidance:literature-review-guidance
name: Dependency - Self-Demonstration Guidance requires Literature Review Guidance
description: Self-demonstrating paper quality criteria reference literature review document quality criteria
source: v:guidance:incose-self-demonstration
target: v:guidance:incose-literature-review
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: quality_reference
subsection_field: quality_criteria.literature_foundation
required: true
tags:
  - edge
  - dependency
  - self-demonstration
  - guidance
version: 1.0.0
created: 2025-12-30T22:00:00Z
modified: 2025-12-30T22:00:00Z
---

# Dependency - Self-Demonstration Guidance requires Literature Review Guidance

**Self-demonstrating paper quality criteria depend on literature review document quality criteria for foundation assessment.**

## Dependency Relationship

**Dependent:** `v:guidance:incose-self-demonstration` (Guidance for Self-Demonstrating Papers)
**Dependency:** `v:guidance:incose-literature-review` (Guidance for Literature Review Documents)
**Relationship:** Self-demonstration guidance quality criteria reference literature review guidance (quality reference dependency)

**Usage:** When validating a self-demonstrating paper's literature foundation (SD4 criterion), the validator must understand what constitutes a high-quality literature review. The literature review guidance defines the quality baseline that the paper's scholarly grounding is measured against.

**Assurance Note:** This dependency edge tracks quality criteria references and is separate from the assurance DAG. For assurance, `guidance-for-incose-self-demonstration` validates against `guidance-for-guidance` (because it is a guidance document).

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Quality Criterion** | SD4: Literature Foundation in self-demonstration guidance |
| **Required** | Yes - literature review guidance defines quality expectations |
| **Purpose** | Validates paper scholarly grounding against quality literature review |
| **Validator Guidance** | Validator should be familiar with literature review guidance criteria |

### Quality Criteria Enabled

This dependency enables the following quality assessments (from guidance-for-incose-self-demonstration):

| Criterion | Description |
|-----------|-------------|
| SD4.Excellent | Background structure mirrors literature review themes, all citations from catalog |
| SD4.Good | Most citations from literature review, themes generally aligned |
| SD4.NeedsImprovement | Many citations not in literature review, background diverges from themes |
| Foundation Tips | Structure Background by theme, cite from catalog, echo the gaps, use the positioning |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers are validated for literature foundation. To assess foundation quality, the validator needs to understand:

1. **What makes a good literature review** → Defined by literature review guidance
2. **Source quality standards** → What counts as a quality source
3. **Gap identification quality** → How gaps should be articulated
4. **Synthesis expectations** → What good thematic synthesis looks like

Without referencing literature review guidance, validators cannot assess whether the paper's scholarly foundation is adequate.

### Difference from Spec Dependencies

This is a **guidance-to-guidance** dependency (quality criteria), not a spec-to-spec dependency (structural requirements):
- Spec dependencies track structural composition (what documents must exist)
- Guidance dependencies track quality references (what quality standards apply)
- Both are needed for complete self-demonstration assurance

### Difference from Assurance

This is a **reference** relationship, not an **assurance** relationship:
- Self-demonstration guidance does NOT validate against literature review guidance
- Self-demonstration guidance validates against guidance-for-guidance (because it's a guidance document)
- This dependency captures quality criteria references, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Style: consider dashed line to distinguish from spec dependencies (solid)
- Direction: arrow from self-demonstration-guidance toward literature-review-guidance

---

**Note:** This dependency is one of four guidance reference dependencies for self-demonstrating papers. The others are: architecture-guidance, lifecycle-guidance, and novel-contributions-guidance.