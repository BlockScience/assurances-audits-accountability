---
type: edge/b1
extends: edge
id: b1:self-verification
name: Boundary Edge - Self-Verification of Spec-for-Spec
description: Anchors self-verification of spec-for-spec through root vertex
source: v:spec:spec
target: b0:root
source_type: vertex/doc/spec
target_type: vertex/b0
orientation: directed
tags:
  - edge
  - boundary
  - b1
  - verification
version: 1.0.0
created: 2025-12-27T22:15:00Z
modified: 2025-12-27T22:15:00Z
---

# Boundary Edge - Self-Verification of Spec-for-Spec

This is a **boundary edge (b1)** that enables self-verification of the spec-for-spec foundational document by anchoring it through the b0:root vertex.

## Edge Properties

- **Type:** b1 (Boundary Edge)
- **Source:** `v:spec:spec` (SS)
- **Target:** `b0:root`
- **Orientation:** Directed (SS → root)
- **Role:** Self-verification anchor

## Semantics

This boundary edge resolves the self-referential paradox for spec-for-spec:

- **Problem:** SS would need to verify against itself (SS → SS), creating a degenerate self-loop
- **Solution:** The b1:self-verification edge (SS → root) anchors this self-verification through the boundary vertex
- **Result:** Creates a valid assurance triangle without circular dependency

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

The b1:self-verification edge connects SS to root, replacing what would be a degenerate SS→SS self-loop.

## Comparison to Standard Verification

| Property | Standard Verification | b1:self-verification |
|----------|---------------------|---------------------|
| Source | Document | v:spec:spec |
| Target | Spec (distinct) | b0:root |
| Purpose | Verify structure | Anchor self-verification |
| Face type | Standard (f:) | Boundary (b2:) |
| Self-referential | No | Yes (resolved via root) |

## Related Elements

- **Source Vertex:** v:spec:spec (SS) - The foundational spec being assured
- **Target Vertex:** b0:root - The boundary anchor
- **Boundary Face:** b2:spec-spec - The complete boundary assurance triangle
- **Coupled with:** b1:couples-GS-root - Forms the other boundary edge in the triangle

---

**Note:** This is one of 4 boundary edges (b1) in the boundary complex. It enables the spec-for-spec foundational document to achieve valid assurance without circular self-reference.
