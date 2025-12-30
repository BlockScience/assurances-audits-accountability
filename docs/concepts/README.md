# Core Concepts

This directory contains reference documentation explaining the fundamental concepts of knowledge complexes.

## Available Concepts

### [Charts vs Documents](charts-vs-documents.md)
Understanding the distinction between charts (knowledge complex artifacts) and chart documents (markdown files describing charts). Explains:
- What charts are in the context of simplicial complexes
- Chart types and chart instances
- The role of chart documents as specifications
- Relationship between charts and their visualizations

### [Validation & Accountability](validation-accountability.md)
Governance and review processes for knowledge complex elements. Covers:
- Verification (automated tool-based checks)
- Validation (human expert review)
- Assurance (attestation of quality)
- Accountability patterns and attribution
- The verification → validation → assurance triangle pattern

### [Audit Trails](audit-trails.md)

Understanding audit trail methodology for knowledge complexes. Covers:

- Audit trail structure and purpose
- Tracing verification and validation history
- Assurance network completeness

### [Hodge Decomposition & Edge PageRank](hodge-decomposition.md)

Algebraic topology tools for analyzing charts at scale. Covers:

- Edge Laplacian construction (L₁ = down + up Laplacian)
- Personalized edge PageRank computation
- Hodge decomposition into gradient, circular, and harmonic components
- Influence measures (penetration, spread, absolute/relative influence)
- Interpreting structural bridges, confluence zones, and topological cycles
- Practical usage of `hodge_analysis.py`

## Using This Documentation

These concept documents serve as **reference material** for understanding knowledge complex fundamentals. They are designed to be consulted when:
- You need clarification on terminology
- You're designing new chart types
- You're implementing verification or validation processes
- You need to understand the theoretical foundation

For a **progressive learning experience**, start with the [Learning Path](../learning/README.md) instead.

## Related Documentation

- **Learning Path**: [docs/learning/](../learning/) - Guided journey through knowledge complexes
- **Use Cases**: [docs/use-cases/](../use-cases/) - Real-world examples and applications
- **Development**: [docs/development/](../development/) - Technical implementation details

---

**Tip**: These concepts build on simplicial complex theory. If terms like "vertex," "edge," and "face" are unfamiliar, start with [Module 01](../../charts/learning-journey-module-01/) in the learning path.
