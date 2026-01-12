# INCOSE Paper Self-Demonstration

This example contains the complete assurance complex for the INCOSE symposium paper "Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability".

## Overview

The paper demonstrates the AAA framework by applying it to itself. Every document in this complex is verified against its specification, validated against its guidance, and assured with explicit human accountability.

## Structure

```
incose-paper/
├── 00_vertices/           # Paper documents and INCOSE-specific types
│   ├── doc-incose-paper-2026.md       # THE PAPER
│   ├── spec-for-incose-*.md           # INCOSE-specific specifications
│   └── guidance-for-incose-*.md       # INCOSE-specific guidance
├── 01_edges/              # Verification, validation, and coupling edges
├── 02_faces/              # Assurance and signature faces
├── charts/
│   └── incose-paper-assurance/        # The audit chart
└── complex.json           # Built cache (generated)
```

## Verification

```bash
# Build the cache
uv run aaa build examples/incose-paper

# Audit assurance coverage
uv run aaa audit examples/incose-paper/charts/incose-paper-assurance

# Verify a specific document
uv run aaa verify examples/incose-paper/00_vertices/doc-incose-paper-2026.md
```

## Key Documents

| Document | Purpose |
|----------|---------|
| `doc-incose-paper-2026.md` | The actual symposium paper |
| `spec-for-incose-paper.md` | Structural requirements for INCOSE papers |
| `guidance-for-incose-paper.md` | Quality criteria for INCOSE papers |
| `incose-paper-assurance.md` | The audit chart showing full coverage |

## The Self-Demonstration

This example proves the framework works by being a working instance of it:
- All documents pass verification
- All documents have validation with human accountability
- All documents have assurance faces
- The audit passes with 100% coverage
