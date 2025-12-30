---
type: vertex/test
extends: vertex
id: v:test:gamma
name: Test Vertex Gamma
description: Third vertex of test tetrahedron
tags:
  - vertex
  - test
  - tetrahedron
version: 1.0.0
created: 2025-12-27T14:30:00Z
modified: 2025-12-27T14:30:00Z
---

# Test Vertex Gamma

Third vertex in the test tetrahedron. See [alpha](alpha.md) for detailed documentation.

## Incident Edges
- e:test:alpha:gamma
- e:test:beta:gamma
- e:test:gamma:delta

## Incident Faces
- f:test:alpha:beta:gamma
- f:test:alpha:gamma:delta

**Note:** The face β-γ-δ containing this vertex is deliberately missing.
