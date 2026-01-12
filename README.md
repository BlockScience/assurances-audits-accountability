# Assurances, Audits & Accountability

A typed simplicial complex framework for document verification, validation, and assurance of AI-generated content with explicit human accountability.

## Quick Start

```bash
# Install
git clone https://github.com/BlockScience/assurances-audits-accountability
cd assurances-audits-accountability
uv sync

# Verify documents
uv run aaa verify 00_vertices/spec-for-spec.md

# Build the complex cache
uv run aaa build

# Audit assurance coverage
uv run aaa audit charts/boundary-complex

# Run all tests
uv run pytest tests/ -v
```

## CLI Reference

The `aaa` CLI is the primary interface for working with knowledge complexes:

```bash
aaa verify <file>              # Verify document against its template
aaa verify --all               # Verify all documents
aaa build                      # Build complex.json cache
aaa build examples/incose-paper # Build cache for an example
aaa audit <chart>              # Audit assurance coverage
aaa check accountability <file> # Check accountability statements
aaa check topology <chart>     # Check topological properties
aaa check ontology             # Verify ontology integrity
```

## Overview

This framework enables **test-driven document development** where:

- **Documents are vertices** (0-simplices) in a typed complex
- **Verification, validation, and coupling are edges** (1-simplices) connecting documents
- **Assurance triangles are faces** (2-simplices) representing complete quality attestation
- **Human accountability** is structurally required for validation judgments

## Dual Interface: VS Code + Obsidian

### VS Code + Claude Code (Construction & Verification)

**Best for:** Building, verifying, and analyzing the knowledge complex

- Run CLI commands from terminal
- Edit documents with full IDE features
- Use Claude Code for AI-assisted document development
- Git integration for version control and accountability

### Obsidian (Navigation & Exploration)

**Best for:** Exploring relationships and understanding structure

- Wiki-style `[[wikilinks]]` for seamless navigation
- Graph view visualizes document relationships
- Backlinks show what references each document
- Local-first, works offline

**To use:** Open this repository as an Obsidian vault. See [[QUICKSTART]] for a 5-minute guide.

## Repository Structure

```text
assurances-audits-accountability/
├── src/aaa/                           # Python CLI package
│   ├── cli.py                        # Main CLI entry point
│   ├── commands/                     # CLI subcommands
│   └── core/                         # Core library (re-exports from scripts)
├── design/                            # Framework design documents
│   ├── ontology-base.md              # Core type system ontology
│   ├── *-architecture-*.md           # Architecture documents
│   └── impl-plans/                   # Implementation plans
├── 00_vertices/                       # Framework specification vertices
│   ├── spec-for-*.md                 # Type specifications
│   ├── guidance-for-*.md             # Guidance documents
│   └── runbook-*.md                  # Procedural runbooks
├── 01_edges/                          # Framework relationship edges
│   ├── verification-*.md             # Verification edges
│   ├── validation-*.md               # Validation edges
│   └── coupling-*.md                 # Spec-guidance coupling
├── 02_faces/                          # Framework faces
│   ├── assurance-*.md                # Assurance triangles
│   └── signature-*.md                # Signature triangles
├── charts/                            # Composed subcomplexes
│   ├── boundary-complex/             # Foundational framework structure
│   └── test-tetrahedron/             # Test fixture
├── examples/                          # Usage examples
│   ├── incose-paper/                 # INCOSE paper self-demonstration
│   └── programs/                     # Program development examples
├── templates/                         # Type template definitions
├── scripts/                           # Verification scripts (legacy)
└── tests/                             # Test suite
```

## Navigation

**Central hub:** [[NAVIGATION]] — Start here for exploring the knowledge complex

| Directory | Obsidian | GitHub/VS Code | Contents |
|-----------|----------|----------------|----------|
| Vertices | [[00_vertices/README]] | [00_vertices/](00_vertices/) | 56 document vertices |
| Edges | [[01_edges/README]] | [01_edges/](01_edges/) | 148 relationship edges |
| Faces | [[02_faces/README]] | [02_faces/](02_faces/) | 65 triangular faces |
| Charts | [[charts/README]] | [charts/](charts/) | Composed subcomplexes |
| Docs | [[docs/README]] | [docs/](docs/) | Concepts & use cases |
| Templates | [[templates/README]] | [templates/](templates/) | Type definitions |

## Key Concepts Demonstrated

### The Assurance Triangle

Every assured document requires three edges forming a closed triangle:

1. **Verification edge** → document passes structural checks against spec
2. **Coupling edge** → spec is linked to corresponding guidance
3. **Validation edge** → document assessed against guidance (requires human approver)

### The V - F ≤ 1 Invariant

In a valid assurance complex:

- Every non-root vertex must have at least one assurance face
- Every face assures exactly one vertex
- **V - F = 1** when each document is assured exactly once
- **V - F < 1** when documents have multiple assurances (e.g., dual spec-guidance pairs)
- **V - F ≤ 1** is necessary but not sufficient for validity—useful as a quick spot-check to identify invalid complexes

### The Boundary Condition and Boundary Complex

**Boundary Condition:** The framework bootstraps through four foundational vertices—spec-for-spec (SS), spec-for-guidance (SG), guidance-for-spec (GS), guidance-for-guidance (GG)—mutually assured in a self-referential pattern. Two form valid triangles (SG, GS), while two rely on self-reference (SS via self-verification, GG via self-validation), creating degenerate faces.

**Boundary Complex:** A fifth vertex, *root* (b0), is introduced as an axiomatic element (not a document requiring assurance). The self-loops are rewired to connect through the root, eliminating degeneracy faces and providing a valid simplicial complex foundation. The root provides assurance but doesn't need it—this is what makes V - F = 1 work.

## Runbooks

Step-by-step workflows for common tasks in the knowledge complex:

| Runbook | Purpose | Steps |
|---------|---------|-------|
| [[runbook-program-development]] | Create program documentation (memo, plan, architecture, lifecycle, field survey) | 7 |
| [[runbook-assurance-audit-chart]] | Build assurance audit charts with full V&V coverage | 6 |
| [[runbook-document-type-creation]] | Create new document types (spec, guidance, coupling) | 10 |
| [[runbook-llm-specialization]] | Create specialized LLM configurations using PPP framework | 8 |

**Direct links:**
- [runbook-program-development.md](00_vertices/runbook-program-development.md)
- [runbook-assurance-audit-chart.md](00_vertices/runbook-assurance-audit-chart.md)
- [runbook-document-type-creation.md](00_vertices/runbook-document-type-creation.md)
- [runbook-llm-specialization.md](00_vertices/runbook-llm-specialization.md)

## Examples

See the [examples/](examples/) directory for complete usage demonstrations:

### INCOSE Paper Self-Demonstration

The `examples/incose-paper/` directory contains the complete assurance complex for the paper "Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability". This is a working example of the framework applied to itself.

```bash
# Build and audit the INCOSE example
uv run aaa build examples/incose-paper
uv run aaa audit examples/incose-paper/charts/incose-paper-assurance
```

### Program Development Examples

The `examples/programs/` directory contains program development examples (bus electrification, water quality monitoring, digital transformation) demonstrating how to apply the framework to real-world programs.

## Scripts (Legacy)

The `scripts/` directory contains the underlying verification tools. These are now wrapped by the `aaa` CLI and direct usage is deprecated.

| Script | CLI Equivalent |
|--------|----------------|
| `verify_template_based.py` | `aaa verify <file>` |
| `audit_assurance_chart.py` | `aaa audit <chart>` |
| `build_cache.py` | `aaa build` |
| `topology.py` | `aaa check topology <chart>` |
| `check_accountability.py` | `aaa check accountability <file>` |

## The Self-Demonstration

The INCOSE paper example in `examples/incose-paper/` IS the evidence for the paper's claims:

1. **The paper exists** as a vertex in the example complex
2. **Verification passes** against its specification
3. **Validation recorded** with human accountability
4. **Assurance faces closed** for all documents
5. **Audit passes** with 100% coverage

```bash
# Verify the self-demonstration
uv run aaa build examples/incose-paper
uv run aaa audit examples/incose-paper/charts/incose-paper-assurance
```

The existence of this repository with passing audits proves the framework works.

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## License

**Copyright (c) 2025 Michael Zargham / Block Science. All rights reserved.**

This repository is currently **proprietary** and **not open source**. No license is granted for use, modification, or distribution without explicit written permission.

We are actively researching the right balance between open source availability and commercial sustainability for this technology. If you are interested in using this framework, please reach out to us at **info@block.science**.

### AI Training Restriction

This repository and its contents may **not** be used for training machine learning models, large language models, or any AI/ML systems without explicit written permission. Automated scraping or crawling for AI training purposes is prohibited.

See [LICENSE](LICENSE) for full terms.

## AI Disclosure

This repository was developed with assistance from Claude (Opus 4.5). All framework architecture, validation methodology, and approval decisions are original author work. The author maintains full responsibility for all content and attestations.
