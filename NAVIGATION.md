# Knowledge Complex Navigation

Central hub for navigating the Typed Simplicial Complex for Documents repository.

## Quick Start

| Link | Description |
|------|-------------|
| [[README]] | Repository overview and getting started |
| [[00_vertices/README]] | All vertices (55 documents) |
| [[01_edges/README]] | All edges (104 relationships) |
| [[02_faces/README]] | All faces (39 triangles) |

## Element Counts

| Dimension | Count | Type |
|-----------|-------|------|
| 0-cells | 55 | Vertices |
| 1-cells | 104 | Edges |
| 2-cells | 39 | Faces |

**Euler Characteristic:** χ = 55 - 104 + 39 = **-10**

## Charts

Composed simplicial complexes representing document networks:

| Chart | Description | Vertices |
|-------|-------------|----------|
| [[charts/boundary-complex/boundary-complex]] | Foundation (SS, SG, GS, GG, root) | 5 |
| [[charts/boundary-kernel/boundary-kernel]] | Foundation without root | 4 |
| [[charts/incose-paper-assurance/incose-paper-assurance]] | INCOSE paper assurance network | 8 |

**Coming soon:**
- `assured-signed-incose` - Complete accountability with signatures

## Foundation Documents

### The Four Pillars

| ID | Document | Purpose |
|----|----------|---------|
| SS | [[00_vertices/spec-for-spec]] | Spec that specs follow |
| SG | [[00_vertices/spec-for-guidance]] | Spec that guidances follow |
| GS | [[00_vertices/guidance-for-spec]] | Guidance for writing specs |
| GG | [[00_vertices/guidance-for-guidance]] | Guidance for writing guidance |

### Root Anchor

- [[00_vertices/b0-root]] - Trust chain root

## By Topic

### INCOSE Paper Submission

**Type Layer (Specs & Guidance):**
- [[00_vertices/spec-for-incose-paper]] / [[00_vertices/guidance-for-incose-paper]]
- [[00_vertices/spec-for-incose-self-demonstration]] / [[00_vertices/guidance-for-incose-self-demonstration]]

**Supporting Document Types:**
- [[00_vertices/spec-for-architecture]] / [[00_vertices/guidance-for-architecture]]
- [[00_vertices/spec-for-lifecycle]] / [[00_vertices/guidance-for-lifecycle]]
- [[00_vertices/spec-for-incose-literature-review]] / [[00_vertices/guidance-for-incose-literature-review]]
- [[00_vertices/spec-for-novel-contributions]] / [[00_vertices/guidance-for-novel-contributions]]

**Instance Layer (Content):**
- [[00_vertices/doc-incose-paper-2026]] - The paper itself
- [[00_vertices/doc-architecture-incose-paper]] - Architecture document
- [[00_vertices/doc-lifecycle-incose-paper]] - Lifecycle document
- [[00_vertices/doc-literature-review-incose-paper]] - Literature review
- [[00_vertices/doc-novel-contributions-incose-paper]] - Novel contributions

### Chart Infrastructure

- [[00_vertices/spec-for-charts]] / [[00_vertices/guidance-for-charts]]
- [[00_vertices/spec-for-assurance-audits]] / [[00_vertices/guidance-for-assurance-audits]]
- [[00_vertices/spec-for-assured-signed-chart]] / [[00_vertices/guidance-for-assured-signed-chart]]

### Signature Infrastructure

- [[00_vertices/spec-for-signer]] - Human signer vertex
- [[00_vertices/spec-for-qualifies]] - Qualification edge
- [[00_vertices/spec-for-signs]] - Signing edge
- [[00_vertices/spec-for-signature]] - Signature face

## Tools

Scripts for building, verifying, and visualizing the complex:

| Script | Purpose |
|--------|---------|
| `scripts/build_cache.py` | Validate all documents |
| `scripts/verify_template_based.py` | Verify single document |
| `scripts/export_chart_direct.py` | Export chart to JSON |
| `scripts/visualize_chart.py` | Basic 3D visualization |
| `scripts/visualize_assured_signed.py` | Enhanced accountability visualization |
| `scripts/audit_assurance_chart.py` | Audit assurance coverage |

### Quick Commands

```bash
# Validate everything
python scripts/build_cache.py

# Export and visualize a chart
python scripts/export_chart_direct.py charts/incose-paper-assurance/incose-paper-assurance.md
python scripts/visualize_assured_signed.py charts/incose-paper-assurance/incose-paper-assurance.json

# Verify a single document
python scripts/verify_template_based.py 00_vertices/spec-for-spec.md --templates templates
```

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

## Dual Workflow

This repository supports two workflows:

1. **VS Code + Claude Code**: Construction, analysis, verification
2. **Obsidian**: Navigation, knowledge graph exploration

Wiki-links (`[[...]]`) work in Obsidian. Markdown links work in both.
