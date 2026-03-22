# Quick Start

Get up and running with AAA Docware in 5 minutes.

---

## 1. Install

```bash
pip install aaa-docware
```

Or with uv:

```bash
uv add aaa-docware
```

---

## 2. Create a Project

```bash
aaa init my-project
cd my-project
```

This scaffolds the standard directory structure and copies foundation documents:

```text
my-project/
├── 00_vertices/    # Documents (doc, spec, guidance, chart)
├── 01_edges/       # Relationships (verification, validation, DocType)
├── 02_faces/       # Assurance triangles
└── charts/         # SPARQL-defined subcomplexes for audit
```

---

## 3. Add a Document

Create `00_vertices/my-doc.md`:

```yaml
---
type: vertex/doc
id: v:doc:my-doc
name: My Document
description: A short description of this document.
---

Document body content here.
```

Verify it parses correctly:

```bash
aaa verify 00_vertices/my-doc.md
```

---

## 4. Build the RDF Graph

```bash
aaa build
```

This walks all files in `00_vertices/`, `01_edges/`, and `02_faces/`, parses them via
their codec, and serialises the result to `graph.ttl`.

---

## 5. Check Topology and Accountability

```bash
aaa check topology
aaa check accountability
```

---

## Full Example

See `examples/paper-authoring/` for a complete worked example — two conference papers with
full verification, validation, assurance triangles, and a chart-based audit:

```bash
cd examples/paper-authoring
uv run python demo.py
```
