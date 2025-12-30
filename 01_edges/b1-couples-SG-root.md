---
type: edge/b1
extends: edge
id: b1:couples-SG-root
name: Boundary Edge - Couples Spec-for-Guidance to Root
description: Boundary coupling edge connecting root to spec-for-guidance as proxy for coupling
source: b0:root
target: v:spec:guidance
source_type: vertex/b0
target_type: vertex/doc/spec
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

# Boundary Edge - Couples Spec-for-Guidance to Root

This is a **boundary edge (b1)** that couples the root vertex to spec-for-guidance, serving as a proxy for the coupling relationship in boundary assurance.

## Edge Properties

- **Type:** b1 (Boundary Edge)
- **Source:** `b0:root`
- **Target:** `v:spec:guidance` (SG)
- **Orientation:** Directed (root → SG)
- **Role:** Boundary coupling

## Semantics

This boundary edge serves as a coupling proxy in the boundary assurance triangle:

- **Standard coupling:** In regular assurance, specs couple to guidance (e.g., SG ↔ GG)
- **Boundary coupling:** In boundary assurance for GG, root couples to SG as proxy
- **Purpose:** Completes the assurance triangle without requiring GG to couple to itself

## Boundary Faces

This boundary edge participates in boundary face:

- `b2:guidance-guidance` (root, SG, GG) - Boundary assurance for guidance-for-guidance

## Edge in Context

In the boundary assurance triangle for GG:

```
         root
        /    \
   b1:self-  b1:couples-
   validation   SG-root
      /            \
    GG ----------- SG
     verification
```

The b1:couples-SG-root edge connects root to SG, serving as proxy for what would be GG coupling to SG.

## Comparison to Standard Coupling

| Property | Standard Coupling | b1:couples-SG-root |
|----------|------------------|-------------------|
| Source | Guidance | b0:root |
| Target | Spec | v:spec:guidance |
| Orientation | Undirected (↔) | Directed (→) |
| Purpose | Align spec/guidance | Proxy coupling via root |
| Face type | Standard (f:) | Boundary (b2:) |

## Related Elements

- **Source Vertex:** b0:root - The boundary anchor
- **Target Vertex:** v:spec:guidance (SG) - The spec coupled to
- **Boundary Face:** b2:guidance-guidance - The complete boundary assurance triangle
- **Paired with:** b1:self-validation - Forms the boundary triangle with SG

---

**Note:** This is one of 4 boundary edges (b1) in the boundary complex. It enables root to serve as a coupling proxy in the guidance-for-guidance boundary assurance.
