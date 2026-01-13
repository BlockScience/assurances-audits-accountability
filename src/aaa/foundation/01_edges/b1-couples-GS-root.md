---
type: edge/b1
extends: edge
id: b1:couples-GS-root
name: Boundary Edge - Couples Guidance-for-Spec to Root
description: Boundary coupling edge connecting root to guidance-for-spec as proxy for coupling
source: b0:root
target: v:guidance:spec
source_type: vertex/b0
target_type: vertex/doc/guidance
orientation: directed
tags:
  - edge
  - boundary
  - b1
  - coupling
version: 1.0.0
created: 2025-12-27T22:15:00Z
modified: 2025-12-27T22:15:00Z
---

# Boundary Edge - Couples Guidance-for-Spec to Root

This is a **boundary edge (b1)** that couples the root vertex to guidance-for-spec, serving as a proxy for the coupling relationship in boundary assurance.

## Edge Properties

- **Type:** b1 (Boundary Edge)
- **Source:** `b0:root`
- **Target:** `v:guidance:spec` (GS)
- **Orientation:** Directed (root → GS)
- **Role:** Boundary coupling

## Semantics

This boundary edge serves as a coupling proxy in the boundary assurance triangle:

- **Standard coupling:** In regular assurance, specs couple to guidance (e.g., SS ↔ GS)
- **Boundary coupling:** In boundary assurance for SS, root couples to GS as proxy
- **Purpose:** Completes the assurance triangle without requiring SS to couple to itself

## Boundary Faces

This boundary edge participates in boundary face:

- `b2:spec-spec` (root, GS, SS) - Boundary assurance for spec-for-spec

## Edge in Context

In the boundary assurance triangle for SS:

```
         root
        /    \
   b1:self-  b1:couples-
   verification  GS-root
      /            \
    SS ----------- GS
      validation
```

The b1:couples-GS-root edge connects root to GS, serving as proxy for what would be SS coupling to GS.

## Comparison to Standard Coupling

| Property | Standard Coupling | b1:couples-GS-root |
|----------|------------------|-------------------|
| Source | Spec | b0:root |
| Target | Guidance | v:guidance:spec |
| Orientation | Undirected (↔) | Directed (→) |
| Purpose | Align spec/guidance | Proxy coupling via root |
| Face type | Standard (f:) | Boundary (b2:) |

## Related Elements

- **Source Vertex:** b0:root - The boundary anchor
- **Target Vertex:** v:guidance:spec (GS) - The guidance coupled to
- **Boundary Face:** b2:spec-spec - The complete boundary assurance triangle
- **Paired with:** b1:self-verification - Forms the boundary triangle with GS

---

**Note:** This is one of 4 boundary edges (b1) in the boundary complex. It enables root to serve as a coupling proxy in the spec-for-spec boundary assurance.
