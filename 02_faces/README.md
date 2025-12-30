# Faces (2-Cells)

Triangular patterns establishing trust in the knowledge complex. Faces are 2-dimensional simplices formed by three vertices and three edges.

## Summary

| Type | Count | Description |
|------|-------|-------------|
| **Assurance** | 37 | (doc, spec, guidance) triangles |
| **Boundary** | 2 | Self-referential foundations |

**Total:** 39 faces

**Future (pending signature infrastructure):**
- **Signature** - (doc, guidance, signer) triangles

## Face Types

### Assurance Faces (assurance-*)

Assert that a document is **assured** - both structurally correct and of sufficient quality.

**Vertices:** (doc, spec, guidance)

**Edges:**
- verification: doc → spec
- validation: doc → guidance
- coupling: spec ↔ guidance

**Examples:**
- [[assurance-spec-guidance]] - v:spec:guidance is assured
- [[assurance-guidance-spec]] - v:guidance:spec is assured
- [[assurance-incose-paper-spec]] - INCOSE paper spec is assured
- [[assurance-architecture-spec]] - Architecture spec is assured

### Boundary Faces (b2-*)

Self-referential foundation triangles that ground the entire system.

- [[b2-spec-spec]] - spec-for-spec assures itself
- [[b2-guidance-guidance]] - guidance-for-guidance assures itself

These are special because they close the recursive loop: they verify and validate against themselves.

### Future: Signature Faces (signature-*)

Will assert that a document is **signed** - explicitly attested by a qualified human.

**Vertices:** (doc, guidance, signer)

**Edges:**
- validation: doc → guidance (SHARED with assurance face)
- signs: signer → doc
- qualifies: signer → guidance

## The Common Boundary Property

**Key Insight:** Assurance and signature faces share exactly one edge - the **validation edge**.

```
                    doc
                   / | \
                  /  |  \
         verification | validation (SHARED)
               /     |     \
           spec    signs   guidance
              \      |      /
          coupling   |  qualifies
                 \   |   /
                  signer
```

This topological coupling ensures that:
1. Quality assessment (validation) connects to accountability (signature)
2. You cannot sign a document without validating it
3. Human accountability is linked to quality, not just structure

## Assurance Coverage

### Foundation Layer

| Face | Target | Status |
|------|--------|--------|
| b2:spec-spec | v:spec:spec | ASSURED |
| b2:guidance-guidance | v:guidance:guidance | ASSURED |
| f:assurance:spec-guidance | v:spec:guidance | ASSURED |
| f:assurance:guidance-spec | v:guidance:spec | ASSURED |

### Type Layer (INCOSE)

| Face | Target | Status |
|------|--------|--------|
| f:assurance:incose-paper-spec | v:spec:incose-paper | ASSURED |
| f:assurance:incose-paper-guidance | v:guidance:incose-paper | ASSURED |
| f:assurance:architecture-spec | v:spec:architecture | ASSURED |
| f:assurance:architecture-guidance | v:guidance:architecture | ASSURED |
| f:assurance:lifecycle-spec | v:spec:lifecycle | ASSURED |
| f:assurance:lifecycle-guidance | v:guidance:lifecycle | ASSURED |

### Instance Layer

| Face | Target | Status |
|------|--------|--------|
| f:assurance:incose-paper-content | v:doc:incose-paper-2026 | ASSURED |
| f:assurance:architecture-content | v:doc:architecture-incose-paper | ASSURED |
| f:assurance:lifecycle-content | v:doc:lifecycle-incose-paper | ASSURED |

## Naming Convention

- `assurance-<target>.md` - Assures a document vertex
- `b2-<name>.md` - Boundary (self-referential) face
- `signature-<doc>:<signer>.md` - (Future) Signer attests to document

## Trust Chain Visualization

All assurance chains trace back to the boundary complex:

```
Instance docs ────────────────────────────────┐
    │                                         │
    ↓ (assurance faces)                       │
Type specs/guidances ─────────────────────────┤
    │                                         │
    ↓ (assurance faces)                       │
Foundation (SS, SG, GS, GG) ──────────────────┤
    │                                         │
    ↓ (boundary faces)                        │
b0:root ←─────────────────────────────────────┘
```

## Related Directories

- [[../00_vertices/README|Vertices]] - The nodes that form face corners
- [[../01_edges/README|Edges]] - The relationships that form face boundaries
- [[../charts/README|Charts]] - Composed simplicial complexes
