# Knowledge Complex Navigation

Central hub for navigating the Typed Simplicial Complex for Documents repository.

**Dual Interface:** This repository works in both VS Code (for construction/verification) and Obsidian (for navigation/exploration). Wiki-links like `[[spec-for-spec]]` work in Obsidian; markdown links work everywhere.

---

## Quick Start

| Link | Description |
|------|-------------|
| [[README]] | Repository overview and getting started |
| [[00_vertices/README]] | All 56 vertices (documents) |
| [[01_edges/README]] | All 148 edges (relationships) |
| [[02_faces/README]] | All 65 faces (triangles) |

---

## The INCOSE Paper

The paper and its complete assurance network:

### The Paper Itself

- [[doc-incose-paper-2026]] — The INCOSE IS 2026 paper content
- [[spec-for-incose-paper]] — What the paper must contain
- [[guidance-for-incose-paper]] — Quality criteria for papers

### Supporting Documents

| Document | Spec | Guidance |
|----------|------|----------|
| [[doc-architecture-incose-paper]] | [[spec-for-architecture]] | [[guidance-for-architecture]] |
| [[doc-lifecycle-incose-paper]] | [[spec-for-lifecycle]] | [[guidance-for-lifecycle]] |
| [[doc-literature-review-incose-paper]] | [[spec-for-incose-literature-review]] | [[guidance-for-incose-literature-review]] |
| [[doc-novel-contributions-incose-paper]] | [[spec-for-novel-contributions]] | [[guidance-for-novel-contributions]] |

### Dual Assurance

The paper is assured against TWO spec/guidance pairs:

1. **Base assurance:** [[assurance-incose-paper-2026-base]]
2. **Self-demonstration assurance:** [[assurance-incose-paper-2026-self-demo]]

---

## Foundation Documents

### The Four Pillars

The self-referential foundation that grounds all assurance:

| ID | Document | Purpose |
|----|----------|---------|
| SS | [[spec-for-spec]] | Spec that specs follow |
| SG | [[spec-for-guidance]] | Spec that guidances follow |
| GS | [[guidance-for-spec]] | Guidance for writing specs |
| GG | [[guidance-for-guidance]] | Guidance for writing guidance |

### Root Anchor

- [[b0-root]] — Trust chain root (provides assurance but doesn't need it)

### Boundary Faces

- [[b2-spec-spec]] — SS assures itself
- [[b2-guidance-guidance]] — GG assures itself

---

## Charts

Composed simplicial complexes representing document networks:

| Chart | Description | Vertices |
|-------|-------------|----------|
| [[charts/incose-paper-assurance/incose-paper-assurance]] | INCOSE paper dual assurance network | 24 |
| [[charts/boundary-complex/boundary-complex]] | Foundation (SS, SG, GS, GG, root) | 5 |
| [[charts/test-tetrahedron/test-tetrahedron]] | Minimal test fixture | 4 |

---

## By Element Type

### Vertices (0-Simplices)

**Specifications** define structural requirements:
- [[spec-for-spec]], [[spec-for-guidance]] — Meta-specifications
- [[spec-for-charts]], [[spec-for-assurance-audits]] — Chart infrastructure
- [[spec-for-incose-paper]], [[spec-for-incose-self-demonstration]] — Paper types
- [[spec-for-architecture]], [[spec-for-lifecycle]] — Supporting doc types
- [[spec-for-signer]], [[spec-for-qualifies]], [[spec-for-signs]] — Signature infrastructure

**Guidance** defines quality criteria:
- [[guidance-for-spec]], [[guidance-for-guidance]] — Meta-guidance
- [[guidance-for-charts]], [[guidance-for-assurance-audits]] — Chart infrastructure
- [[guidance-for-incose-paper]], [[guidance-for-incose-self-demonstration]] — Paper types
- [[guidance-for-architecture]], [[guidance-for-lifecycle]] — Supporting doc types

**Content Documents** are actual work products:
- [[doc-incose-paper-2026]] — The paper
- [[doc-architecture-incose-paper]], [[doc-lifecycle-incose-paper]]
- [[doc-literature-review-incose-paper]], [[doc-novel-contributions-incose-paper]]

### Edges (1-Simplices)

**Coupling** links spec ↔ guidance pairs:
- [[coupling-spec]], [[coupling-guidance]] — Foundation
- [[coupling-incose-paper]], [[coupling-incose-self-demonstration]] — Paper types
- [[coupling-architecture]], [[coupling-lifecycle]] — Supporting types

**Verification** asserts document → spec conformance:
- [[verification-incose-paper-2026:spec-incose-paper]]
- [[verification-incose-paper-2026:spec-incose-self-demonstration]]

**Validation** asserts document → guidance quality:
- [[validation-incose-paper-2026:guidance-incose-paper]]
- [[validation-incose-paper-2026:guidance-incose-self-demonstration]]

**Signature Infrastructure:**
- [[qualifies-mzargham:guidance-incose-paper]] — Signer qualified for guidance
- [[signs-mzargham:incose-paper-2026]] — Signer attests to document

### Faces (2-Simplices)

**Assurance Faces** close quality triangles:
- [[assurance-incose-paper-2026-base]], [[assurance-incose-paper-2026-self-demo]]
- [[assurance-architecture-incose]], [[assurance-lifecycle-incose]]
- [[assurance-literature-review-incose]], [[assurance-novel-contributions-incose]]

**Signature Faces** close accountability triangles:
- [[signature-incose-paper-2026-base]], [[signature-incose-paper-2026-self-demo]]

**Boundary Faces** ground the foundation:
- [[b2-spec-spec]], [[b2-guidance-guidance]]

---

## Tools

Scripts for building, verifying, and visualizing the complex:

| Script | Purpose |
|--------|---------|
| `scripts/build_cache.py` | Validate all documents, build cache |
| `scripts/verify_template_based.py` | Verify single document |
| `scripts/audit_assurance_chart.py` | Audit assurance coverage |
| `scripts/export_chart_direct.py` | Export chart to JSON |
| `scripts/visualize_chart.py` | Basic 3D visualization |
| `scripts/visualize_assured_signed.py` | Enhanced layered visualization |
| `scripts/topology.py` | Compute Euler characteristic |

### Quick Commands

```bash
# Validate everything
python scripts/build_cache.py

# Verify the paper
python scripts/verify_template_based.py 00_vertices/doc-incose-paper-2026.md --templates templates

# Run assurance audit
python scripts/audit_assurance_chart.py charts/incose-paper-assurance/incose-paper-assurance.md

# Generate visualization
python scripts/export_chart_direct.py charts/incose-paper-assurance/incose-paper-assurance.md
python scripts/visualize_assured_signed.py charts/incose-paper-assurance/incose-paper-assurance.json
```

---

## Templates

Document templates in `templates/`:

| Template | Location |
|----------|----------|
| Spec | `templates/00_vertices/spec.md` |
| Guidance | `templates/00_vertices/guidance.md` |
| Signer | `templates/00_vertices/signer.md` |
| Coupling | `templates/01_edges/coupling.md` |
| Verification | `templates/01_edges/verification.md` |
| Validation | `templates/01_edges/validation.md` |
| Qualifies | `templates/01_edges/qualifies.md` |
| Signs | `templates/01_edges/signs.md` |
| Assurance | `templates/02_faces/assurance.md` |
| Signature | `templates/02_faces/signature.md` |
| Chart | `templates/charts/chart.md` |

---

## Key Concepts

### Assurance = Verification + Validation

- **Verification**: Does it conform to spec? (deterministic)
- **Validation**: Does it meet quality criteria? (qualitative)
- **Assurance**: Both verification AND validation pass

### The Assurance Triangle

```
        doc
       /   \
verification  validation
     /         \
   spec ←——→ guidance
      coupling
```

### Common Boundary Property

Assurance and signature faces share the **validation edge**:

```
        doc
       / | \
      /  |  \
 verif.  |  validation (SHARED)
    /    |      \
 spec  signs   guidance
    \    |      /
coupling |  qualifies
      \  |  /
      signer
```

---

## Concepts & Use Cases

For deeper understanding:

- [[docs/concepts/validation-accountability]] — Why humans must approve validation
- [[docs/concepts/audit-trails]] — How audit trails work
- [[docs/concepts/charts-vs-documents]] — Charts vs standalone documents
- [[docs/concepts/hodge-decomposition]] — Advanced topological analysis

Use cases:

- [[docs/use-cases/assurance-audit/README]] — Practical assurance auditing
- [[docs/use-cases/organization-design-and-analysis/README]] — Org modeling

---

## Dual Workflow

This repository supports two workflows:

1. **VS Code + Claude Code**: Construction, analysis, verification
2. **Obsidian**: Navigation, knowledge graph exploration

Wiki-links (`[[...]]`) work in Obsidian. Markdown links work in both.

---

**Start exploring:** [[00_vertices/README]] | [[01_edges/README]] | [[02_faces/README]]
