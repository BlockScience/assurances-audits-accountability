---
type: edge/coupling
extends: edge
id: e:coupling:novel-contributions
name: Coupling - spec-for-novel-contributions and guidance-for-novel-contributions
source: v:spec:novel-contributions
target: v:guidance:novel-contributions
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-30T18:00:00Z
modified: 2025-12-30T18:00:00Z
---

# Coupling - spec-for-novel-contributions and guidance-for-novel-contributions

This coupling edge links the specification and guidance for novel contributions documents, establishing them as a coherent "document type" within the assurance framework.

## Coupled Documents

| Role | Document | ID |
|------|----------|-----|
| Specification | [[spec-for-novel-contributions]] | v:spec:novel-contributions |
| Guidance | [[guidance-for-novel-contributions]] | v:guidance:novel-contributions |

## Type Coherence

Both documents address the same document type: **novel contributions documents** that inventory and rank research contributions.

- **Specification** defines: Required frontmatter fields, required body sections (Introduction, Contribution Entries with What/Why/Evidence/Projection, Summary Table, Key Insights), novelty level definitions, and structural constraints
- **Guidance** defines: Quality criteria (clarity, novelty calibration, evidence quality, ranking coherence, actionability, intellectual honesty), section-by-section best practices, workflow recommendations, and common issues

## Verification-Validation Alignment

| Structural Requirement (Spec) | Quality Criterion (Guidance) |
|------------------------------|------------------------------|
| At least 3 contributions enumerated | Contribution Clarity - each is self-contained |
| What/Why/Evidence/Projection format | Evidence Quality - specific and verifiable |
| Novelty levels stated | Novelty Calibration - appropriately calibrated |
| Summary table with rankings | Ranking Coherence - internally consistent |
| Key insights section | Actionability - directly usable |
| All required fields present | Intellectual Honesty - limitations acknowledged |

## Usage

When assuring a novel contributions document:

1. **Verification** checks structural compliance against `spec-for-novel-contributions`
2. **Validation** assesses quality against `guidance-for-novel-contributions`
3. **Coupling** ensures verification and validation use this matched pair

The assurance triangle closes when all three edges (verification, coupling, validation) are present.

## Document Type Summary

A well-formed novel contributions document:
- Satisfies all structural requirements from the spec (REQUIRED sections, frontmatter fields, minimum contribution count)
- Achieves "Good" or "Excellent" on guidance quality criteria
- Serves its intended purpose: guiding paper writing with accurate, actionable contribution assessments

---

**Note:** This coupling is part of the assurance infrastructure for novel contributions document type.
