---
type: vertex/test
extends: vertex
id: v:test:beta
name: Test Vertex Beta
description: Second vertex of test tetrahedron
tags:
  - vertex
  - test
  - tetrahedron
version: 1.0.0
created: 2025-12-27T14:30:00Z
modified: 2025-12-27T14:30:00Z
---

# Test Vertex Beta

Second vertex in the test tetrahedron. See [alpha](alpha.md) for detailed documentation of the test fixture pattern.

## Incident Edges
- e:test:alpha:beta
- e:test:beta:gamma
- e:test:beta:delta

## Incident Faces
- f:test:alpha:beta:gamma
- f:test:alpha:beta:delta

**Note:** The face β-γ-δ containing this vertex is deliberately missing.
