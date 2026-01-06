---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-guidance:novel-contributions-guidance
name: Dependency - Self-Demonstration Guidance requires Novel Contributions Guidance
description: Self-demonstrating paper quality criteria reference novel contributions document quality criteria
source: v:guidance:incose-self-demonstration
target: v:guidance:novel-contributions
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: quality_reference
subsection_field: quality_criteria.contribution_integrity
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

# Dependency - Self-Demonstration Guidance requires Novel Contributions Guidance

**Self-demonstrating paper quality criteria depend on novel contributions document quality criteria for contribution integrity assessment.**

## Dependency Relationship

**Dependent:** `v:guidance:incose-self-demonstration` (Guidance for Self-Demonstrating Papers)
**Dependency:** `v:guidance:novel-contributions` (Guidance for Novel Contributions Documents)
**Relationship:** Self-demonstration guidance quality criteria reference novel contributions guidance (quality reference dependency)

**Usage:** When validating a self-demonstrating paper's contribution integrity (SD5 criterion), the validator must understand what constitutes a high-quality novel contributions document. The novel contributions guidance defines the quality baseline that integrity is measured against.

**Assurance Note:** This dependency edge tracks quality criteria references and is separate from the assurance DAG. For assurance, `guidance-for-incose-self-demonstration` validates against `guidance-for-guidance` (because it is a guidance document).

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Quality Criterion** | SD5: Contribution Integrity in self-demonstration guidance |
| **Required** | Yes - novel contributions guidance defines quality expectations |
| **Purpose** | Validates paper contribution claims against quality novel contributions document |
| **Validator Guidance** | Validator should be familiar with novel contributions guidance criteria |

### Quality Criteria Enabled

This dependency enables the following quality assessments (from guidance-for-incose-self-demonstration):

| Criterion | Description |
|-----------|-------------|
| SD5.Excellent | All contributions match exactly, no overclaiming, evidence consistent |
| SD5.Good | Contributions largely match, minor language variation |
| SD5.NeedsImprovement | Contributions differ, paper overclaims, evidence inconsistencies |
| Integrity Tips | Copy contribution statements, don't improvise claims, match evidence, preserve differentiation |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers are validated for contribution integrity. To assess integrity quality, the validator needs to understand:

1. **What makes a good novel contributions document** → Defined by novel contributions guidance
2. **Claim quality standards** → What well-articulated contributions look like
3. **Evidence requirements** → What evidence should support claims
4. **Differentiation quality** → How to assess "different from prior work" claims

Without referencing novel contributions guidance, validators cannot assess whether the paper's contribution claims have integrity.

### Difference from Spec Dependencies

This is a **guidance-to-guidance** dependency (quality criteria), not a spec-to-spec dependency (structural requirements):
- Spec dependencies track structural composition (what documents must exist)
- Guidance dependencies track quality references (what quality standards apply)
- Both are needed for complete self-demonstration assurance

### Difference from Assurance

This is a **reference** relationship, not an **assurance** relationship:
- Self-demonstration guidance does NOT validate against novel contributions guidance
- Self-demonstration guidance validates against guidance-for-guidance (because it's a guidance document)
- This dependency captures quality criteria references, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Style: consider dashed line to distinguish from spec dependencies (solid)
- Direction: arrow from self-demonstration-guidance toward novel-contributions-guidance

---

**Note:** This dependency is one of four guidance reference dependencies for self-demonstrating papers. The others are: architecture-guidance, lifecycle-guidance, and literature-review-guidance.