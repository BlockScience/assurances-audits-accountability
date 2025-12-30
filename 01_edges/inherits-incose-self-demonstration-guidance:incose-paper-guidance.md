---
type: edge/inherits
extends: edge
id: e:inherits:incose-self-demonstration-guidance:incose-paper-guidance
name: Inherits - INCOSE Self-Demonstration Guidance extends INCOSE Paper Guidance
description: Self-demonstrating paper guidance is a specialization of standard INCOSE paper guidance with additional quality criteria
source: v:guidance:incose-self-demonstration
target: v:guidance:incose-paper
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
inheritance_type: domain_specialization
inherited_fields:
  - relevance_criteria
  - accessibility_criteria
  - rigor_criteria
  - novelty_criteria
  - theme_alignment_criteria
  - engagement_criteria
  - section_guidance
  - self_assessment_rubric
added_fields:
  - document_coherence_criteria
  - architecture_alignment_criteria
  - lifecycle_enactment_criteria
  - literature_foundation_criteria
  - contribution_integrity_criteria
  - self_demonstration_credibility_criteria
  - traceability_criteria
  - extended_rubric
tags:
  - edge
  - inherits
  - incose-paper
  - self-demonstration
  - guidance
version: 1.0.0
created: 2025-12-30T22:30:00Z
modified: 2025-12-30T22:30:00Z
---

# Inherits - INCOSE Self-Demonstration Guidance extends INCOSE Paper Guidance

**Self-demonstrating paper guidance extends the standard INCOSE paper guidance with additional quality criteria for document coherence, supporting document alignment, and self-referential credibility.**

## Inheritance Relationship

**Child:** `v:guidance:incose-self-demonstration` (Guidance for Self-Demonstrating Papers)
**Parent:** `v:guidance:incose-paper` (Guidance for INCOSE Papers)
**Relationship:** incose-self-demonstration-guidance extends incose-paper-guidance (domain specialization)

**Assurance Note:** This inheritance edge tracks domain specialization and is separate from the assurance DAG. For assurance, both guidance documents validate against `v:guidance:guidance` (because they are guidance documents), not against each other.

## Inherited Structure

### Inherited from Parent (guidance-for-incose-paper)

| Criterion | Description |
|-----------|-------------|
| Relevance to SE Community | Is the topic relevant to systems engineering? |
| Accessibility and Clarity | Can readers understand the content? |
| Rigor and Validity | Is the methodology sound and defensible? |
| Novelty and Contribution | Does it advance the field? |
| Theme Alignment | Does it connect to IS 2026 theme? |
| Engagement and Impact | Will it generate discussion and adoption? |
| Section-Specific Guidance | Quality expectations for each section |
| Self-Assessment Rubric | 24-point parent rubric |

### Added by Child (guidance-for-incose-self-demonstration)

| Criterion | Description |
|-----------|-------------|
| SD1: Document Coherence | Consistency across paper and supporting documents |
| SD2: Architecture Alignment | Paper reflects architecture document faithfully |
| SD3: Lifecycle Enactment | Paper visibly enacts the lifecycle it describes |
| SD4: Literature Foundation | Paper demonstrably builds on literature review |
| SD5: Contribution Integrity | Paper accurately represents novel contributions document |
| SD6: Self-Demonstration Credibility | Recursive "paper proves itself" claim is believable |
| SD7: Traceability Experience | Reader can trace claims across documents |
| Extended Rubric | 28-point additional scoring (52 total with parent) |

### Extended Section Guidance

The child extends these parent section criteria:

| Section | Extension |
|---------|-----------|
| Abstract | SHOULD explicitly mention self-demonstration |
| Background | Structure SHOULD mirror literature review themes |
| Methodology | SHOULD reference architecture and lifecycle documents |
| Results | MUST include audit results, assurance status |
| Discussion | SHOULD address what paper cannot self-demonstrate |

## Semantic Justification

### Why Self-Demonstration Guidance Extends Standard Guidance

Self-demonstrating paper quality criteria are a **specialized superset** of standard INCOSE paper criteria:

1. **Base Quality:** All standard quality criteria apply
2. **Additional Assessment:** Self-demonstrating papers require coherence assessment across documents
3. **Same Validators:** Conference reviewers assess both using similar processes
4. **Cumulative Scoring:** Extended rubric adds to parent rubric

A self-demonstrating paper must first be a good INCOSE paper, then additionally demonstrate coherence and credibility.

### Why Not Separate Criteria

Creating completely independent criteria would:
- Force validators to assess papers twice (once for structure, once for self-demo)
- Miss the cumulative nature (bad INCOSE paper can't be good self-demo)
- Lose the inheritance relationship that makes scoring efficient

### Difference from Assurance

This inheritance relationship is **definitional**, not **assurance**:

| Aspect | Inheritance (this edge) | Assurance (validation edge) |
|--------|------------------------|-------------------------------|
| **Question** | "What quality criteria apply?" | "Does this document meet criteria?" |
| **Purpose** | Define quality expectations | Prove fitness-for-purpose |
| **Target** | Parent guidance definition | Guidance for guidance validation |
| **Example** | Self-demo extends paper guidance | Self-demo guidance validates against guidance-for-guidance |

## Visualization Notes

In 3D visualization:
- Render as inherits edge (distinct from assurance and dependency edges)
- Color: suggest using purple/violet to indicate inheritance relationship
- Style: consider double-line or bold to distinguish from dependency edges
- Direction: arrow from child (self-demonstration-guidance) TO parent (incose-paper-guidance)
- Group with parallel spec inherits edge

## Parallel Structure

This guidance inheritance has a parallel spec inheritance:
- `e:inherits:incose-self-demonstration-guidance:incose-paper-guidance` (this edge - guidance)
- `e:inherits:incose-self-demonstration:incose-paper` (parallel - spec)

Both should be visualized together to show the coupled type extension.

## Quality Scoring Summary

| Rubric | Max Points | Focus |
|--------|------------|-------|
| Parent (inherited) | 24 | Standard paper quality |
| Extended (added) | 28 | Self-demonstration quality |
| **Combined** | **52** | **Total quality assessment** |

Target for excellent self-demonstrating paper: ≥40/52

---

**Note:** This edge documents that self-demonstrating paper quality criteria extend standard INCOSE paper criteria. The child guidance adds coherence, alignment, and credibility criteria while inheriting all base quality expectations.