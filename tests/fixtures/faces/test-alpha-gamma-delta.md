---
type: face/face
extends: null
id: f:test:alpha:gamma:delta
name: Test Face Alpha-Gamma-Delta

# Topological structure
vertices:
  - v:test:alpha
  - v:test:gamma
  - v:test:delta
edges:
  - e:test:alpha:gamma
  - e:test:gamma:delta
  - e:test:alpha:delta
orientation: unoriented

tags:
  - face
version: 1.0.0
created: 2025-12-27T14:50:00Z
modified: 2025-12-27T14:50:00Z
---

# Test Face Alpha-Gamma-Delta

Generic test face forming one triangular face of the tetrahedron.

Part of the tetrahedron test chart demonstrating basic simplicial complex structure.

## Structure

This face closes the triangle formed by:
- Vertices: [alpha](../00_vertices/test-alpha.md), [gamma](../00_vertices/test-gamma.md), [delta](../00_vertices/test-delta.md)
- Edges: [alpha-gamma](../01_edges/test-alpha-gamma.md), [gamma-delta](../01_edges/test-gamma-delta.md), [alpha-delta](../01_edges/test-alpha-delta.md)

## Note on Missing Face

The tetrahedron would have 4 faces in total. The face **Beta-Gamma-Delta** is deliberately omitted to create a topological hole for testing hole detection algorithms.
