---
type: vertex/test
extends: vertex
id: v:test:delta
name: Test Vertex Delta
description: Fourth vertex of test tetrahedron
tags:
  - vertex
  - test
  - tetrahedron
version: 1.0.0
created: 2025-12-27T14:30:00Z
modified: 2025-12-27T14:30:00Z
---

# Test Vertex Delta

Fourth vertex in the test tetrahedron. See [alpha](alpha.md) for detailed documentation.

## Incident Edges
- e:test:alpha:delta
- e:test:beta:delta
- e:test:gamma:delta

## Incident Faces
- f:test:alpha:beta:delta
- f:test:alpha:gamma:delta

**Note:** The face β-γ-δ containing this vertex is deliberately missing, creating χ=1.
