---
type: face/face
extends: null
id: f:test:alpha:beta:delta
name: Test Face Alpha-Beta-Delta

# Topological structure
vertices:
  - v:test:alpha
  - v:test:beta
  - v:test:delta
edges:
  - e:test:alpha:beta
  - e:test:beta:delta
  - e:test:alpha:delta
orientation: unoriented

tags:
  - face
version: 1.0.0
created: 2025-12-27T14:50:00Z
modified: 2025-12-27T14:50:00Z
---

# Test Face Alpha-Beta-Delta

Generic test face forming one triangular face of the tetrahedron.

Part of the tetrahedron test chart demonstrating basic simplicial complex structure.

## Structure

This face closes the triangle formed by:
- Vertices: [alpha](../00_vertices/test-alpha.md), [beta](../00_vertices/test-beta.md), [delta](../00_vertices/test-delta.md)
- Edges: [alpha-beta](../01_edges/test-alpha-beta.md), [beta-delta](../01_edges/test-beta-delta.md), [alpha-delta](../01_edges/test-alpha-delta.md)
