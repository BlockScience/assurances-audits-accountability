---
type: vertex/test
extends: vertex
id: v:test:alpha
name: Test Vertex Alpha
description: First vertex of test tetrahedron demonstrating simplicial complex structure
tags:
  - vertex
  - test
  - tetrahedron
version: 1.0.0
created: 2025-12-27T14:30:00Z
modified: 2025-12-27T14:30:00Z
---

# Test Vertex Alpha

This is a minimal test vertex used in the [test-tetrahedron chart](../../charts/test-tetrahedron/test-tetrahedron.md) to demonstrate simplicial complex structure.

## Purpose

Alpha serves as the first vertex in a 4-vertex tetrahedron (K4 complete graph) that teaches:
- How vertices form the 0-cells of a simplicial complex
- How edges connect pairs of vertices (1-cells)
- How faces are bounded by triples of edges (2-cells)
- How deliberate holes create non-trivial topology

## Role in Tetrahedron

**Vertex:** Alpha (one of 4 vertices)

**Incident Edges:**
- e:test:alpha:beta (α → β)
- e:test:alpha:gamma (α → γ)
- e:test:alpha:delta (α → δ)

**Incident Faces:**
- f:test:alpha:beta:gamma (α-β-γ triangle)
- f:test:alpha:beta:delta (α-β-δ triangle)
- f:test:alpha:gamma:delta (α-γ-δ triangle)

**Missing Face:**
- The face β-γ-δ (not containing α) is deliberately missing, creating a topological hole

## Educational Value

This test vertex demonstrates:
- **Minimal structure**: Just enough metadata to be a valid vertex
- **Clear naming**: Greek letter makes it obviously a test element
- **Well-documented role**: Explains its purpose in the teaching example
- **Traceability**: Links to the chart that uses it

---

**Note:** This is a test fixture element. It has no semantic meaning beyond demonstrating topological structure.
