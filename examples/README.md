# Examples

This directory contains complete usage demonstrations of the AAA framework.

## paper-authoring

A self-contained example showing the full AAA workflow applied to writing and assuring
two conference papers on knowledge complexes.

**What it demonstrates:**

- Document types as KC elements (spec + guidance + DocType edge — not file templates)
- Assurance triangles: verification + validation + DocType close a 2-simplex
- Shared DocType edge reused across both papers
- Chart-based composition: a SPARQL query materialises the paper series as a subcomplex
- Tiling completeness audit: every doc in the subcomplex is covered by an assurance face
- Algebraic topology: Betti numbers, Euler characteristic, edge influence

**Run the demo:**

```bash
cd examples/paper-authoring
uv run python demo.py
```

**Or build and audit directly with the CLI:**

```bash
aaa build examples/paper-authoring/content/ --output /tmp/demo.ttl
aaa verify examples/paper-authoring/content/00_vertices/spec-conference-paper.md
```
