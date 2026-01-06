---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-guidance:lifecycle-guidance
name: Dependency - Self-Demonstration Guidance requires Lifecycle Guidance
description: Self-demonstrating paper quality criteria reference lifecycle document quality criteria
source: v:guidance:incose-self-demonstration
target: v:guidance:lifecycle
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: quality_reference
subsection_field: quality_criteria.lifecycle_enactment
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

# Dependency - Self-Demonstration Guidance requires Lifecycle Guidance

**Self-demonstrating paper quality criteria depend on lifecycle document quality criteria for enactment assessment.**

## Dependency Relationship

**Dependent:** `v:guidance:incose-self-demonstration` (Guidance for Self-Demonstrating Papers)
**Dependency:** `v:guidance:lifecycle` (Guidance for Lifecycle Documents)
**Relationship:** Self-demonstration guidance quality criteria reference lifecycle guidance (quality reference dependency)

**Usage:** When validating a self-demonstrating paper's lifecycle enactment (SD3 criterion), the validator must understand what constitutes a high-quality lifecycle document. The lifecycle guidance defines the quality baseline that enactment is measured against.

**Assurance Note:** This dependency edge tracks quality criteria references and is separate from the assurance DAG. For assurance, `guidance-for-incose-self-demonstration` validates against `guidance-for-guidance` (because it is a guidance document).

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Quality Criterion** | SD3: Lifecycle Enactment in self-demonstration guidance |
| **Required** | Yes - lifecycle guidance defines quality expectations |
| **Purpose** | Validates paper enactment against a quality lifecycle document |
| **Validator Guidance** | Validator should be familiar with lifecycle guidance criteria |

### Quality Criteria Enabled

This dependency enables the following quality assessments (from guidance-for-incose-self-demonstration):

| Criterion | Description |
|-----------|-------------|
| SD3.Excellent | Lifecycle phases visibly enacted, reader can see lifecycle in paper's story |
| SD3.Good | Lifecycle phases recognizable, most phases referenced |
| SD3.NeedsImprovement | Paper seems produced differently than lifecycle describes |
| Enactment Tips | Narrate your process, show artifacts, acknowledge iteration, name the humans |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers are validated for lifecycle enactment. To assess enactment quality, the validator needs to understand:

1. **What makes a good lifecycle document** → Defined by lifecycle guidance
2. **Phase clarity** → Lifecycle guidance defines what clear phase descriptions look like
3. **Assurance integration** → How lifecycle should connect to V&V
4. **Traceability** → How lifecycle phases should map to actual work

Without referencing lifecycle guidance, validators cannot assess whether the paper genuinely enacted its lifecycle or merely claimed to.

### Difference from Spec Dependencies

This is a **guidance-to-guidance** dependency (quality criteria), not a spec-to-spec dependency (structural requirements):
- Spec dependencies track structural composition (what documents must exist)
- Guidance dependencies track quality references (what quality standards apply)
- Both are needed for complete self-demonstration assurance

### Difference from Assurance

This is a **reference** relationship, not an **assurance** relationship:
- Self-demonstration guidance does NOT validate against lifecycle guidance
- Self-demonstration guidance validates against guidance-for-guidance (because it's a guidance document)
- This dependency captures quality criteria references, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Style: consider dashed line to distinguish from spec dependencies (solid)
- Direction: arrow from self-demonstration-guidance toward lifecycle-guidance

---

**Note:** This dependency is one of four guidance reference dependencies for self-demonstrating papers. The others are: architecture-guidance, literature-review-guidance, and novel-contributions-guidance.