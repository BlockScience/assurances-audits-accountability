---
type: face/face
extends: null
id: f:test:alpha:beta:gamma
name: Test Face Alpha-Beta-Gamma

# Topological structure
vertices:
  - v:test:alpha
  - v:test:beta
  - v:test:gamma
edges:
  - e:test:alpha:beta
  - e:test:beta:gamma
  - e:test:alpha:gamma
orientation: unoriented

tags:
  - face
version: 1.0.0
created: 2025-12-27T14:50:00Z
modified: 2025-12-27T14:50:00Z
---

# Test Face Alpha-Beta-Gamma

Generic test face forming one triangular face of the tetrahedron.

Part of the tetrahedron test chart demonstrating basic simplicial complex structure.

## Structure

This face closes the triangle formed by:
- Vertices: [alpha](../00_vertices/test-alpha.md), [beta](../00_vertices/test-beta.md), [gamma](../00_vertices/test-gamma.md)
- Edges: [alpha-beta](../01_edges/test-alpha-beta.md), [beta-gamma](../01_edges/test-beta-gamma.md), [alpha-gamma](../01_edges/test-alpha-gamma.md)
