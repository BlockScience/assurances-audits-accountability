---
type: edge/coupling
extends: edge
id: e:coupling:incose-paper
name: Coupling - INCOSE Paper Spec and Guidance
source: v:spec:incose-paper
target: v:guidance:incose-paper
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-12-30T11:00:00Z
modified: 2025-12-30T11:00:00Z
---

# Coupling - INCOSE Paper Spec and Guidance

This coupling edge connects the specification for INCOSE IS 2026 research papers with the guidance for writing excellent INCOSE papers.

## Purpose

Together, these documents enable complete assurance for INCOSE paper submissions:

- **Verification:** Checking that a paper has required structural elements (against spec-for-incose-paper)
  - Word count under 7,000
  - All required sections present
  - AI disclosure included
  - INCOSE template format used

- **Validation:** Assessing whether a paper is high quality and likely to be accepted (against guidance-for-incose-paper)
  - Relevance to SE community
  - Accessibility and clarity
  - Rigor and validity
  - Novelty and contribution
  - Theme alignment
  - Engagement and impact

## Governed Document Type

Both documents govern INCOSE International Symposium research paper submissions. Specifically:

- Research papers (full methodology, results, validation)
- Practice papers (problem space, approach, lessons learned)
- Papers targeting IS 2026 "Seeking Wa in SE" theme

## Relationship to Boundary Complex

This coupling edge extends the boundary complex for a new document type. It follows the same pattern as:

- `e:coupling:spec` (spec-for-spec ↔ guidance-for-spec)
- `e:coupling:guidance` (spec-for-guidance ↔ guidance-for-guidance)

The INCOSE paper spec and guidance are child documents of the foundational spec/guidance types, and this coupling enables their assurance triangles.

## Assurance Triangle Usage

This edge forms the base of assurance triangles for:

1. **spec-for-incose-paper** - verified against spec-for-spec, validated against guidance-for-spec
2. **guidance-for-incose-paper** - verified against spec-for-guidance, validated against guidance-for-guidance
3. **Any INCOSE paper document** - verified against spec-for-incose-paper, validated against guidance-for-incose-paper

---

**Note:** This coupling is part of the INCOSE paper assurance infrastructure.
