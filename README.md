# AAA Docware

[![PyPI version](https://img.shields.io/pypi/v/aaa-docware.svg)](https://pypi.org/project/aaa-docware/)
[![Python](https://img.shields.io/pypi/pyversions/aaa-docware.svg)](https://pypi.org/project/aaa-docware/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Tests](https://github.com/BlockScience/assurances-audits-accountability/actions/workflows/test.yml/badge.svg)](https://github.com/BlockScience/assurances-audits-accountability/actions/workflows/test.yml)

A typed simplicial complex framework for document verification, validation, and assurance.

## Installation

```bash
pip install aaa-docware
```

## Quick Start

```bash
# Create a new knowledge complex project
aaa init my-project
cd my-project

# Verify a document against its type schema
aaa verify 00_vertices/my-doc.md

# Build the RDF graph from all documents
aaa build

# Audit assurance coverage
aaa audit charts/my-chart
```

## What is a Knowledge Complex?

A knowledge complex treats collections of documents as a **typed simplicial complex** — a mathematical structure where documents, their relationships, and quality attestations form vertices, edges, and faces:

- **Vertices** (0-simplices): Documents — specs, guidances, ontologies, charts
- **Edges** (1-simplices): Relationships — verification, validation, coupling
- **Faces** (2-simplices): Assurance triangles — complete quality attestation requiring both automated checks and human judgment

The framework enforces that every assured document has:

1. A **verification edge** — automated structural checks against a spec
2. A **coupling edge** — linking the spec to its corresponding guidance
3. A **validation edge** — human assessment against guidance (requires accountability)

## CLI Reference

| Command | Description |
|---------|-------------|
| `aaa init <name>` | Scaffold a new knowledge complex project |
| `aaa verify <file>` | Verify document against its type schema |
| `aaa build [path]` | Build RDF graph from markdown documents |
| `aaa audit <chart>` | Audit assurance coverage of a chart |
| `aaa check topology <chart>` | Check Euler characteristic and topology |
| `aaa check types` | List all registered document types |

See the [full CLI reference](https://blockscience.github.io/assurances-audits-accountability/cli-reference/) for details.

## For Contributors

```bash
git clone https://github.com/BlockScience/assurances-audits-accountability
cd assurances-audits-accountability
uv sync

make test    # Run tests
make lint    # Check linting
make format  # Auto-format
make docs    # Serve docs locally
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Documentation

Full documentation: [blockscience.github.io/assurances-audits-accountability](https://blockscience.github.io/assurances-audits-accountability/)

## License

[Apache License 2.0](LICENSE) — Copyright 2025 Michael Zargham / Block Science
