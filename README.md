# Assurances, Audits & Accountability

Supporting material for INCOSE IS 2026 paper submission.

This repository contains the implementation and demonstration of a typed simplicial complex framework for document verification, validation, and assurance with explicit human accountability.

<!-- Hero image placeholder - will be updated when assured-signed chart is complete -->
<!-- ![Accountability Complex](images/assured-signed-complex.png) -->

**Element Counts:** 55 vertices | 104 edges | 39 faces | χ = -10

## The Paper

The paper **"Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability"** demonstrates a framework where:

- **Documents are vertices** (0-simplices) in a typed complex
- **Verification, validation, and coupling are edges** (1-simplices) connecting documents
- **Assurance triangles are faces** (2-simplices) representing complete quality attestation
- **Human accountability** is structurally required for validation judgments

**The paper is its own proof.** The file [`doc-incose-paper-2026.md`](doc-incose-paper-2026.md) exists as a vertex in an assurance complex, verified against its specification, validated against its guidance, with all checks passing.

## Quick Verification

```bash
# Setup
git clone https://github.com/BlockScience/assurances-audits-accountability
cd assurances-audits-accountability
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# Verify the paper
python scripts/verify_template_based.py doc-incose-paper-2026.md --templates templates

# Run the assurance audit
python scripts/audit_assurance_chart.py charts/incose-paper-assurance/incose-paper-assurance.md

# Run all tests
python -m pytest tests/ -v
```

**Expected output:**

```text
Result: ✓ PASS
Checks: 6/6 passed

Status: PASS
Invariant: F = V - 1: 7 = 8 - 1 ✓
Coverage: 100.0% (7/7 targets assured)
```

## Repository Structure

```text
assurances-audits-accountability/
├── doc-incose-paper-2026.md          # THE PAPER (also a vertex)
├── 00_vertices/                       # Document vertices
│   ├── spec-for-incose-paper.md      # Paper specification
│   ├── guidance-for-incose-paper.md  # Paper quality criteria
│   ├── spec-for-spec.md              # Foundational spec
│   ├── guidance-for-guidance.md      # Foundational guidance
│   └── ...
├── 01_edges/                          # Relationship edges
│   ├── verification-incose-paper-*   # Verification edges
│   ├── validation-incose-paper-*     # Validation edges (with approvers)
│   ├── coupling-incose-paper.md      # Spec-guidance coupling
│   └── ...
├── 02_faces/                          # Assurance faces
│   ├── assurance-incose-paper-*.md   # Paper assurance triangles
│   ├── b2-spec-spec.md               # Boundary face
│   └── ...
├── charts/
│   ├── incose-paper-assurance/       # THE AUDIT CHART
│   └── boundary-complex/             # Foundational structure
├── figures/                           # Paper figures
├── scripts/                           # CLI tools
├── templates/                         # Type definitions
└── tests/                             # Test suite
```

## Key Concepts Demonstrated

### The Assurance Triangle

Every assured document requires three edges forming a closed triangle:

1. **Verification edge** → document passes structural checks against spec
2. **Coupling edge** → spec is linked to corresponding guidance
3. **Validation edge** → document assessed against guidance (requires human approver)

### The V - F = 1 Invariant

In any valid assurance audit chart:

- Every vertex (except root) must have exactly one assurance face
- Every face assures exactly one vertex
- **V - F = 1** where root provides assurance but doesn't need it

### The Boundary Complex

Self-referential foundations (spec-for-spec, guidance-for-guidance) are resolved through a root vertex that anchors boundary faces, enabling computational topology methods without paradox.

## Figures

The paper references three figures generated from this repository:

| Figure | Description | Source |
|--------|-------------|--------|
| Figure 1 | Assurance Triangle | [figures/figure1-final.png](figures/figure1-final.png) |
| Figure 2 | Boundary Complex | [figures/figure3-final.png](figures/figure3-final.png) |
| Figure 3 | Audit Chart | [figures/figure2-final.png](figures/figure2-final.png) |

## Navigation

For detailed exploration of the knowledge complex:

- **[NAVIGATION.md](NAVIGATION.md)** - Central navigation hub
- **[00_vertices/README.md](00_vertices/README.md)** - All 55 vertices by type
- **[01_edges/README.md](01_edges/README.md)** - All 104 edges by type
- **[02_faces/README.md](02_faces/README.md)** - All 39 faces by type

This repository supports two workflows:

1. **VS Code + Claude Code**: Construction, verification, analysis
2. **Obsidian**: Knowledge graph navigation

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `verify_template_based.py` | Verify document against its type template |
| `audit_assurance_chart.py` | Check assurance coverage and V-F=1 invariant |
| `topology.py` | Compute Euler characteristic |
| `visualize_chart.py` | Generate interactive visualization |
| `visualize_assured_signed.py` | Enhanced 3D visualization with layered architecture |
| `build_cache.py` | Build element cache and validate all documents |

## The Self-Demonstration

This repository IS the evidence for the paper's claims:

1. **The paper exists** as [`doc-incose-paper-2026.md`](doc-incose-paper-2026.md)
2. **Verification passes** against [`spec-for-incose-paper.md`](00_vertices/spec-for-incose-paper.md)
3. **Validation recorded** in [`validation-incose-paper-content:guidance-incose-paper.md`](01_edges/validation-incose-paper-content:guidance-incose-paper.md)
4. **Assurance face closed** in [`assurance-incose-paper-content.md`](02_faces/assurance-incose-paper-content.md)
5. **Audit passes** with 100% coverage and V-F=1 verified

The existence of this repository with passing audits proves the framework works.

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## License

See [LICENSE](LICENSE) file.

## AI Disclosure

This repository was developed with assistance from Claude (Opus 4.5). All framework architecture, validation methodology, and approval decisions are original author work. The author maintains full responsibility for all content and attestations.
