# Faces (2-Cells)

Triangular patterns establishing trust in the knowledge complex. Faces are 2-dimensional simplices formed by three vertices and three edges.

**Navigation:** [[../README|Home]] | [[../NAVIGATION|Navigation Hub]] | [[../00_vertices/README|Vertices]] | [[../01_edges/README|Edges]]

---

## Summary

| Type | Count | Description |
|------|-------|-------------|
| Assurance | 42 | (doc, spec, guidance) triangles |
| Signature | 21 | (doc, guidance, signer) triangles |
| Boundary | 2 | Self-referential foundations |
| **Total** | **65** | |

---

## INCOSE Paper Faces

### Paper Dual Assurance

The paper is assured against TWO spec/guidance pairs:

| Face | Description |
|------|-------------|
| [[assurance-incose-paper-2026-base]] | Paper assured against base INCOSE paper type |
| [[assurance-incose-paper-2026-self-demo]] | Paper assured against self-demonstration type |

### Paper Signatures

| Face | Description |
|------|-------------|
| [[signature-incose-paper-2026-base]] | Author signs base assurance |
| [[signature-incose-paper-2026-self-demo]] | Author signs self-demo assurance |

### Supporting Document Assurance

| Face | Target Document |
|------|-----------------|
| [[assurance-architecture-incose]] | Architecture document |
| [[assurance-lifecycle-incose]] | Lifecycle document |
| [[assurance-literature-review-incose]] | Literature review |
| [[assurance-novel-contributions-incose]] | Novel contributions |

### Supporting Document Signatures

| Face | Target Document |
|------|-----------------|
| [[signature-architecture-incose]] | Architecture document |
| [[signature-lifecycle-incose]] | Lifecycle document |
| [[signature-literature-review-incose]] | Literature review |
| [[signature-novel-contributions-incose]] | Novel contributions |

---

## Assurance Faces

Assert that a document is **assured** — both structurally correct (verified) and of sufficient quality (validated).

**Pattern:** (doc, spec, guidance) triangle with three edges:

- verification: doc → spec
- validation: doc → guidance
- coupling: spec ↔ guidance

### Foundation Assurance

| Face | Target | Description |
|------|--------|-------------|
| [[b2-spec-spec]] | spec-for-spec | SS assures itself (boundary) |
| [[b2-guidance-guidance]] | guidance-for-guidance | GG assures itself (boundary) |
| [[assurance-spec-guidance]] | spec-for-guidance | SG assured |
| [[assurance-guidance-spec]] | guidance-for-spec | GS assured |

### INCOSE Paper Type Assurance

| Face | Target |
|------|--------|
| [[assurance-incose-paper-spec]] | spec-for-incose-paper |
| [[assurance-incose-paper-guidance]] | guidance-for-incose-paper |
| [[assurance-incose-self-demonstration-spec]] | spec-for-incose-self-demonstration |
| [[assurance-incose-self-demonstration-guidance]] | guidance-for-incose-self-demonstration |

### Supporting Document Type Assurance

| Face | Target |
|------|--------|
| [[assurance-architecture-spec]] | spec-for-architecture |
| [[assurance-architecture-guidance]] | guidance-for-architecture |
| [[assurance-lifecycle-spec]] | spec-for-lifecycle |
| [[assurance-lifecycle-guidance]] | guidance-for-lifecycle |
| [[assurance-literature-review-spec]] | spec-for-incose-literature-review |
| [[assurance-literature-review-guidance]] | guidance-for-incose-literature-review |
| [[assurance-novel-contributions-spec]] | spec-for-novel-contributions |
| [[assurance-novel-contributions-guidance]] | guidance-for-novel-contributions |

### Chart Infrastructure Assurance

| Face | Target |
|------|--------|
| [[assurance-chart]] | chart type |
| [[assurance-chart-guidance]] | chart guidance |
| [[assurance-assurance_audit]] | assurance_audit type |
| [[assurance-assurance_audit-guidance]] | assurance_audit guidance |

### PPP Framework Assurance

| Face | Target |
|------|--------|
| [[assurance-persona-claude]] | Claude persona |
| [[assurance-purpose-claude]] | Claude purpose |
| [[assurance-protocol-claude]] | Claude protocol |
| [[assurance-system_prompt-compiled]] | Compiled system prompt |

---

## Signature Faces

Assert that a document is **signed** — explicitly attested by a qualified human.

**Pattern:** (doc, guidance, signer) triangle with three edges:

- validation: doc → guidance (SHARED with assurance face)
- signs: signer → doc
- qualifies: signer → guidance

### Foundation Signatures

| Face | Target |
|------|--------|
| [[signature-spec-spec]] | spec-for-spec |
| [[signature-spec-guidance]] | spec-for-guidance |
| [[signature-guidance-spec]] | guidance-for-spec |
| [[signature-guidance-guidance]] | guidance-for-guidance |

### INCOSE Paper Type Signatures

| Face | Target |
|------|--------|
| [[signature-incose-paper-spec]] | spec-for-incose-paper |
| [[signature-incose-paper-guidance]] | guidance-for-incose-paper |
| [[signature-incose-self-demonstration-spec]] | spec-for-incose-self-demonstration |
| [[signature-incose-self-demonstration-guidance]] | guidance-for-incose-self-demonstration |

### Supporting Document Type Signatures

| Face | Target |
|------|--------|
| [[signature-architecture-spec]] | spec-for-architecture |
| [[signature-architecture-guidance]] | guidance-for-architecture |
| [[signature-lifecycle-spec]] | spec-for-lifecycle |
| [[signature-lifecycle-guidance]] | guidance-for-lifecycle |
| [[signature-literature-review-spec]] | spec-for-incose-literature-review |
| [[signature-literature-review-guidance]] | guidance-for-incose-literature-review |
| [[signature-novel-contributions-spec]] | spec-for-novel-contributions |
| [[signature-novel-contributions-guidance]] | guidance-for-novel-contributions |

---

## Boundary Faces

Self-referential foundation triangles that ground the entire system.

| Face | Target | Description |
|------|--------|-------------|
| [[b2-spec-spec]] | spec-for-spec | SS assures itself |
| [[b2-guidance-guidance]] | guidance-for-guidance | GG assures itself |

These are special because they close the recursive loop: they verify and validate against themselves.

---

## The Common Boundary Property

**Key Insight:** Assurance and signature faces share exactly one edge — the **validation edge**.

```text
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

---

## Assurance Coverage by Layer

### Layer 0: Foundation

| Face | Target | Status |
|------|--------|--------|
| b2:spec-spec | v:spec:spec | ✅ ASSURED |
| b2:guidance-guidance | v:guidance:guidance | ✅ ASSURED |
| f:assurance:spec-guidance | v:spec:guidance | ✅ ASSURED |
| f:assurance:guidance-spec | v:guidance:spec | ✅ ASSURED |

### Layer 1: Document Types

| Face | Target | Status |
|------|--------|--------|
| f:assurance:incose-paper-spec | v:spec:incose-paper | ✅ ASSURED |
| f:assurance:incose-paper-guidance | v:guidance:incose-paper | ✅ ASSURED |
| f:assurance:incose-self-demonstration-spec | v:spec:incose-self-demonstration | ✅ ASSURED |
| f:assurance:incose-self-demonstration-guidance | v:guidance:incose-self-demonstration | ✅ ASSURED |

### Layer 2: Document Instances

| Face | Target | Status |
|------|--------|--------|
| f:assurance:incose-paper-2026-base | v:doc:incose-paper-2026 | ✅ ASSURED |
| f:assurance:incose-paper-2026-self-demo | v:doc:incose-paper-2026 | ✅ ASSURED |
| f:assurance:architecture-incose | v:doc:architecture-incose-paper | ✅ ASSURED |
| f:assurance:lifecycle-incose | v:doc:lifecycle-incose-paper | ✅ ASSURED |

---

## Trust Chain Visualization

All assurance chains trace back to the boundary complex:

```text
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

---

## Naming Conventions

- `assurance-<target>.md` — Assures a document vertex
- `signature-<target>.md` — Signer attests to document
- `b2-<name>.md` — Boundary (self-referential) face

---

## Related Directories

| Directory | Description |
|-----------|-------------|
| [[../00_vertices/README]] | The nodes that form face corners |
| [[../01_edges/README]] | The relationships that form face boundaries |
| [[../charts/README]] | Composed simplicial complexes |
| [[../templates/README]] | Type definitions for creating faces |
