---
type: edge/inherits
extends: edge
id: e:inherits:incose-self-demonstration:incose-paper
name: Inherits - INCOSE Self-Demonstration extends INCOSE Paper
description: Self-demonstrating paper spec is a specialization of standard INCOSE paper spec with additional requirements
source: v:spec:incose-self-demonstration
target: v:spec:incose-paper
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
inheritance_type: domain_specialization
inherited_fields:
  - word_limit
  - required_sections
  - ai_disclosure_requirements
  - anonymization_requirements
  - template_format
  - structural_constraints
added_fields:
  - self_demonstrating
  - supporting_documents
  - consistency_requirements
  - completeness_requirements
  - self_demonstration_requirements
  - assurance_status
tags:
  - edge
  - inherits
  - incose-paper
  - self-demonstration
version: 1.0.0
created: 2025-12-30T22:30:00Z
modified: 2025-12-30T22:30:00Z
---

# Inherits - INCOSE Self-Demonstration extends INCOSE Paper

**Self-demonstrating paper specification extends the standard INCOSE paper specification with additional requirements for consistency, completeness, and self-referential proof.**

## Inheritance Relationship

**Child:** `v:spec:incose-self-demonstration` (Specification for Self-Demonstrating Papers)
**Parent:** `v:spec:incose-paper` (Specification for INCOSE Papers)
**Relationship:** incose-self-demonstration extends incose-paper (domain specialization)

**Assurance Note:** This inheritance edge tracks domain specialization and is separate from the assurance DAG. For assurance, both specs verify against `v:spec:spec` (because they are specs), not against each other.

## Inherited Structure

### Inherited from Parent (spec-for-incose-paper)

| Field/Section | Description |
|---------------|-------------|
| `word_limit` | ≤7,000 words requirement |
| `required_sections` | Abstract, Introduction, Background, Methodology, Results, Discussion, Conclusion, Acknowledgments, References |
| `ai_disclosure_requirements` | INCOSE AI disclosure statement requirements |
| `anonymization_requirements` | Initial submission anonymization rules |
| `template_format` | Two-column INCOSE proceedings format |
| `structural_constraints` | Section ordering, citation format, etc. |

### Added by Child (spec-for-incose-self-demonstration)

| Field/Section | Description |
|---------------|-------------|
| `self_demonstrating` | Boolean flag (always `true` for this type) |
| `supporting_documents` | Required architecture, lifecycle, literature review, novel contributions |
| `consistency_requirements` | C1-C4 checks for cross-document consistency |
| `completeness_requirements` | CP1-CP4 checks for cross-document completeness |
| `self_demonstration_requirements` | SD1-SD3 checks for self-referential proof |
| `assurance_status` | Metadata tracking paper's position in assurance chart |

### Extended Sections

The child extends these parent sections with additional content:

| Section | Extension |
|---------|-----------|
| Methodology | SHOULD reference architecture document |
| Results | MUST include audit results showing assurance status |
| Discussion | SHOULD address what paper cannot self-demonstrate |

## Semantic Justification

### Why Self-Demonstration Extends Standard Paper

Self-demonstrating papers are a **specialized subset** of INCOSE papers:

1. **Structural Identity:** All structural requirements of standard papers apply
2. **Additional Constraints:** Self-demonstrating papers add consistency/completeness requirements
3. **Same Audience:** Both target INCOSE symposium reviewers
4. **Submission Identical:** Both use same template, format, submission process

The specialization adds requirements without changing the base structure—a classic "is-a" relationship.

### Why Not a Separate Type

Creating a completely separate spec would:
- Duplicate all standard INCOSE paper requirements
- Create maintenance burden (changes need propagation)
- Miss the conceptual relationship (self-demonstrating IS an INCOSE paper)

Inheritance captures the real-world relationship accurately.

### Difference from Assurance

This inheritance relationship is **definitional**, not **assurance**:

| Aspect | Inheritance (this edge) | Assurance (verification edge) |
|--------|------------------------|-------------------------------|
| **Question** | "What is this type?" | "Is this instance valid?" |
| **Purpose** | Define type structure | Prove conformance |
| **Target** | Parent type definition | Spec for spec validation |
| **Example** | Self-demo extends paper | Self-demo spec verifies against spec-for-spec |

## Visualization Notes

In 3D visualization:
- Render as inherits edge (distinct from assurance and dependency edges)
- Color: suggest using purple/violet to indicate inheritance relationship
- Style: consider double-line or bold to distinguish from dependency edges
- Direction: arrow from child (self-demonstration) TO parent (incose-paper)
- Group with parallel guidance inherits edge

## Parallel Structure

This spec inheritance has a parallel guidance inheritance:
- `e:inherits:incose-self-demonstration:incose-paper` (this edge - spec)
- `e:inherits:incose-self-demonstration-guidance:incose-paper-guidance` (parallel - guidance)

Both should be visualized together to show the coupled type extension.

---

**Note:** This edge documents that self-demonstrating papers are a specialized form of INCOSE papers. The child type adds requirements for supporting documents and cross-document consistency while inheriting all base structural requirements.