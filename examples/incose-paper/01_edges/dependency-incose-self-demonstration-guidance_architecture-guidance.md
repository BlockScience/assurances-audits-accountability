---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-guidance:architecture-guidance
name: Dependency - Self-Demonstration Guidance requires Architecture Guidance
description: Self-demonstrating paper quality criteria reference architecture document quality criteria
source: v:guidance:incose-self-demonstration
target: v:guidance:architecture
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: quality_reference
subsection_field: quality_criteria.architecture_alignment
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

# Dependency - Self-Demonstration Guidance requires Architecture Guidance

**Self-demonstrating paper quality criteria depend on architecture document quality criteria for alignment assessment.**

## Dependency Relationship

**Dependent:** `v:guidance:incose-self-demonstration` (Guidance for Self-Demonstrating Papers)
**Dependency:** `v:guidance:architecture` (Guidance for Architecture Documents)
**Relationship:** Self-demonstration guidance quality criteria reference architecture guidance (quality reference dependency)

**Usage:** When validating a self-demonstrating paper's architecture alignment (SD2 criterion), the validator must understand what constitutes a high-quality architecture document. The architecture guidance defines the quality baseline that the paper's alignment is measured against.

**Assurance Note:** This dependency edge tracks quality criteria references and is separate from the assurance DAG. For assurance, `guidance-for-incose-self-demonstration` validates against `guidance-for-guidance` (because it is a guidance document).

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Quality Criterion** | SD2: Architecture Alignment in self-demonstration guidance |
| **Required** | Yes - architecture guidance defines quality expectations |
| **Purpose** | Validates paper alignment against a quality architecture document |
| **Validator Guidance** | Validator should be familiar with architecture guidance criteria |

### Quality Criteria Enabled

This dependency enables the following quality assessments (from guidance-for-incose-self-demonstration):

| Criterion | Description |
|-----------|-------------|
| SD2.Excellent | All four layers clearly represented, V-model mapping informs V&V discussion |
| SD2.Good | Most layers represented, V-model connection present |
| SD2.NeedsImprovement | Layers missing or misrepresented |
| Architecture Tips | Quote the architecture, reference layers explicitly, match physical details |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers are validated for architecture alignment. To assess alignment quality, the validator needs to understand:

1. **What makes a good architecture document** → Defined by architecture guidance
2. **Quality baseline** → If the architecture document is low quality, alignment checking is compromised
3. **Layer expectations** → Architecture guidance defines what each layer should contain
4. **V-model mapping quality** → Architecture guidance specifies V-model requirements

Without referencing architecture guidance, validators would have no standard for what "excellent architecture alignment" means.

### Difference from Spec Dependencies

This is a **guidance-to-guidance** dependency (quality criteria), not a spec-to-spec dependency (structural requirements):
- Spec dependencies track structural composition (what documents must exist)
- Guidance dependencies track quality references (what quality standards apply)
- Both are needed for complete self-demonstration assurance

### Difference from Assurance

This is a **reference** relationship, not an **assurance** relationship:
- Self-demonstration guidance does NOT validate against architecture guidance
- Self-demonstration guidance validates against guidance-for-guidance (because it's a guidance document)
- This dependency captures quality criteria references, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Style: consider dashed line to distinguish from spec dependencies (solid)
- Direction: arrow from self-demonstration-guidance toward architecture-guidance

---

**Note:** This dependency is one of four guidance reference dependencies for self-demonstrating papers. The others are: lifecycle-guidance, literature-review-guidance, and novel-contributions-guidance.
