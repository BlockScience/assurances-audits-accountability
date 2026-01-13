---
type: edge/coupling
extends: edge
id: e:coupling:spec-guidance:guidance-spec
name: Coupling - Spec-for-Guidance and Guidance-for-Spec Cross-Domain Alignment
description: Ensures spec-for-guidance and guidance-for-spec are mutually consistent (foundational boundary complex coupling)
source: v:spec:guidance
target: v:guidance:spec
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
  - boundary-complex
version: 1.0.0
created: 2025-12-27T16:00:00Z
modified: 2025-12-27T16:00:00Z
---

# Coupling - Spec-for-Guidance and Guidance-for-Spec Cross-Domain Alignment

This coupling edge establishes that spec-for-guidance and guidance-for-spec are mutually consistent and aligned, forming a critical cross-domain coupling in the boundary complex.

## Coupling Relationship

**Source:** `v:spec:guidance` (Specification for Guidance Documents)
**Target:** `v:guidance:spec` (Guidance for Specifications)
**Relationship:** spec-for-guidance COUPLES_WITH guidance-for-spec (cross-domain consistency)

## Cross-Domain Alignment

### Structural-Quality Consistency ✅

The spec and guidance align on foundational document types:

- ✅ SG defines structure for guidances
- ✅ GS defines quality criteria for specs
- ✅ No contradictions between domains
- ✅ Together they enable assurance triangles

### Coverage Alignment ✅

Both documents are foundational:

- ✅ SG enables all guidance documents (structural foundation)
- ✅ GS enables all spec validation (quality foundation)
- ✅ Together they form the meta-level of the knowledge complex
- ✅ Cross-domain coupling ensures coherence

### Terminology Consistency ✅

Shared foundational terminology:

- ✅ Both use same document type concepts
- ✅ Definitions align across domains
- ✅ Meta-level consistency maintained
- ✅ Cross-references work correctly

## Coherence Assessment

**Coupling Strength:** Strong (Boundary Complex)

**Rationale:** This coupling is foundational to the knowledge complex. SG defines how to write guidances (including GS itself), while GS defines how to assess specs (including SG itself). This cross-domain coupling enables the self-referential assurance property of the boundary complex.

## Role in Boundary Complex

This coupling edge is part of the boundary complex foundation:

```
Boundary Complex Couplings:
- SS ↔ GS (spec:spec couples with guidance:spec)
- SG ↔ GS (spec:guidance couples with guidance:spec) ← THIS EDGE
- SG ↔ GG (spec:guidance couples with guidance:guidance)
- SS ↔ GG (spec:spec couples with guidance:guidance)
```

Together, these couplings ensure the boundary complex is coherent and self-consistent.

## Examples of Alignment

### Example 1: Document Type Hierarchy

**SG says:** Guidance documents extend doc, must have quality_criteria section
**GS says:** Specs should be assessed for completeness, coverage of domain

**Alignment:** ✅ SG structures guidances, GS assesses specs - complementary roles

### Example 2: Assurance Pattern

**SG says:** Guidances have specific structural requirements
**GS says:** Specs should be validated for quality against guidance

**Alignment:** ✅ Enables the assurance triangle pattern (spec→spec, spec→guidance, coupling)

### Example 3: Self-Reference

**SG says:** (defines structure for all guidances, including GS)
**GS says:** (defines quality criteria for all specs, including SG)

**Alignment:** ✅ Cross-domain coupling enables mutual assurance

## Notes

This edge is critical for the self-referential property of the boundary complex. Without it, the meta-level documents (SG and GS) could not assure each other across domains.

---

**Version:** 1.0.0
**Status:** Coupled
**Strength:** Strong (Boundary)
**Last Modified:** 2025-12-27
