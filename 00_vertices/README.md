# Vertices (0-Cells)

Foundational elements of the knowledge complex. Vertices represent standalone documents that define or describe something.

## Summary

| Type | Count | Description |
|------|-------|-------------|
| **Specifications** | 27 | Define structural requirements |
| **Guidance** | 22 | Define quality criteria |
| **Documents** | 5 | Content documents |
| **Boundary** | 1 | Root anchor (b0:root) |

**Total:** 55 vertices

## By Type

### Specifications (spec-for-*)

Specs define **what** a document must contain to be valid.

**Foundation:**
- [[spec-for-spec]] - The meta-specification
- [[spec-for-guidance]] - Requirements for guidance documents

**Document Types:**
- [[spec-for-charts]] - Chart document structure
- [[spec-for-assurance-audits]] - Assurance audit requirements
- [[spec-for-assured-signed-chart]] - Combined assurance + signature charts

**INCOSE Paper:**
- [[spec-for-incose-paper]] - Conference paper requirements
- [[spec-for-incose-self-demonstration]] - Self-demonstrating paper requirements
- [[spec-for-architecture]] - Architecture document requirements
- [[spec-for-lifecycle]] - Lifecycle document requirements
- [[spec-for-incose-literature-review]] - Literature review requirements
- [[spec-for-novel-contributions]] - Novel contributions requirements

**Signature Infrastructure:**
- [[spec-for-signer]] - Human signer vertex requirements
- [[spec-for-qualifies]] - Qualification edge requirements
- [[spec-for-signs]] - Signing edge requirements
- [[spec-for-signature]] - Signature face requirements

### Guidance Documents (guidance-for-*)

Guidance defines **how well** a document achieves quality.

**Foundation:**
- [[guidance-for-guidance]] - The meta-guidance
- [[guidance-for-spec]] - Quality criteria for specs

**Document Types:**
- [[guidance-for-charts]] - Quality criteria for charts
- [[guidance-for-assurance-audits]] - Quality criteria for assurance audits
- [[guidance-for-assured-signed-chart]] - Quality criteria for assured-signed charts

**INCOSE Paper:**
- [[guidance-for-incose-paper]] - Quality criteria for conference papers
- [[guidance-for-incose-self-demonstration]] - Quality criteria for self-demonstrating papers
- [[guidance-for-architecture]] - Quality criteria for architecture documents
- [[guidance-for-lifecycle]] - Quality criteria for lifecycle documents
- [[guidance-for-incose-literature-review]] - Quality criteria for literature reviews
- [[guidance-for-novel-contributions]] - Quality criteria for novel contributions

### Content Documents (doc-*)

Actual content produced following specs and guidance.

- [[doc-incose-paper-2026]] - INCOSE IS 2026 paper content
- [[doc-architecture-incose-paper]] - Architecture document
- [[doc-lifecycle-incose-paper]] - Lifecycle document
- [[doc-literature-review-incose-paper]] - Literature review
- [[doc-novel-contributions-incose-paper]] - Novel contributions

### Boundary Elements (b0-*)

- [[b0-root]] - Root anchor for all trust chains

## Quick Reference

### The Meta-Documents

The knowledge complex is grounded in four self-referential foundation vertices:

| ID | Short Name | Purpose |
|----|------------|---------|
| v:spec:spec | SS | Spec that specs follow |
| v:spec:guidance | SG | Spec that guidances follow |
| v:guidance:spec | GS | Guidance for writing specs |
| v:guidance:guidance | GG | Guidance for writing guidance |

### Naming Convention

- `spec-for-<type>.md` - Structural requirements for a document type
- `guidance-for-<type>.md` - Quality criteria for a document type
- `doc-<name>.md` - Actual content document
- `b0-<name>.md` - Boundary element

## Related Directories

- [[../01_edges/README|Edges]] - Relationships between vertices
- [[../02_faces/README|Faces]] - Triangular trust patterns
- [[../charts/README|Charts]] - Composed simplicial complexes
