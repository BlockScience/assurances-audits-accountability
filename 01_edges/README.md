# Edges (1-Cells)

Relationships connecting vertices in the knowledge complex. Edges are typed connections between documents.

**Navigation:** [[../README|Home]] | [[../NAVIGATION|Navigation Hub]] | [[../00_vertices/README|Vertices]] | [[../02_faces/README|Faces]]

---

## Summary

| Type | Count | Description |
|------|-------|-------------|
| Coupling | 16 | Spec ↔ guidance alignment |
| Verification | 37 | Doc → spec conformance |
| Validation | 37 | Doc → guidance assessment |
| Signs | 18 | Signer → document attestation |
| Qualifies | 10 | Signer → guidance qualification |
| Cites | 4 | Document → document reference |
| Dependency | 8 | Requirement relationships |
| Inherits | 2 | Type inheritance |
| Boundary | 4 | Connections to root |
| **Total** | **148** | |

---

## INCOSE Paper Edges

### Paper Verification & Validation

| Edge | Description |
|------|-------------|
| [[verification-incose-paper-2026:spec-incose-paper]] | Paper verifies against base spec |
| [[verification-incose-paper-2026:spec-incose-self-demonstration]] | Paper verifies against self-demo spec |
| [[validation-incose-paper-2026:guidance-incose-paper]] | Paper validates against base guidance |
| [[validation-incose-paper-2026:guidance-incose-self-demonstration]] | Paper validates against self-demo guidance |

### Paper Signatures

| Edge | Description |
|------|-------------|
| [[signs-mzargham:incose-paper-2026]] | Author signs base assurance |
| [[signs-mzargham:incose-paper-2026-self-demo]] | Author signs self-demo assurance |
| [[qualifies-mzargham:guidance-incose-paper]] | Author qualified for paper guidance |
| [[qualifies-mzargham:guidance-incose-self-demonstration]] | Author qualified for self-demo guidance |

### Paper Citations

| Edge | Description |
|------|-------------|
| [[cites-incose-paper-2026:architecture-incose]] | Paper cites architecture doc |
| [[cites-incose-paper-2026:lifecycle-incose]] | Paper cites lifecycle doc |
| [[cites-incose-paper-2026:literature-review-incose]] | Paper cites literature review |
| [[cites-incose-paper-2026:novel-contributions-incose]] | Paper cites novel contributions |

---

## Coupling Edges

Link paired spec ↔ guidance documents. Assert that a spec and its corresponding guidance are designed to work together.

### Foundation Coupling

| Edge | Description |
|------|-------------|
| [[coupling-spec]] | Links spec-for-spec ↔ guidance-for-spec |
| [[coupling-guidance]] | Links spec-for-guidance ↔ guidance-for-guidance |
| [[coupling-spec-guidance-guidance-spec]] | Cross-coupling between spec and guidance foundations |

### INCOSE Paper Type Coupling

| Edge | Description |
|------|-------------|
| [[coupling-incose-paper]] | Links spec/guidance for INCOSE papers |
| [[coupling-incose-self-demonstration]] | Links spec/guidance for self-demo papers |
| [[coupling-architecture]] | Links spec/guidance for architecture docs |
| [[coupling-lifecycle]] | Links spec/guidance for lifecycle docs |
| [[coupling-incose-literature-review]] | Links spec/guidance for literature reviews |
| [[coupling-novel-contributions]] | Links spec/guidance for novel contributions |

### Chart Infrastructure Coupling

| Edge | Description |
|------|-------------|
| [[coupling-chart]] | Links spec/guidance for charts |
| [[coupling-assurance_audit]] | Links spec/guidance for assurance audits |
| [[coupling-chart-assurance_audit]] | Chart-assurance_audit coupling |

### PPP Framework Coupling

| Edge | Description |
|------|-------------|
| [[coupling-persona]] | Links spec/guidance for personas |
| [[coupling-purpose]] | Links spec/guidance for purposes |
| [[coupling-protocol]] | Links spec/guidance for protocols |
| [[coupling-system_prompt]] | Links spec/guidance for system prompts |

---

## Verification Edges

Assert that a document conforms to its specification. Deterministic, automatable checks.

**Pattern:** document → spec

### Foundation Verification

| Edge | Description |
|------|-------------|
| [[verification-spec-spec]] | spec-for-spec verifies against itself |
| [[verification-spec-guidance]] | spec-for-guidance verifies against spec-for-spec |
| [[verification-guidance-spec]] | guidance-for-spec verifies against spec-for-guidance |
| [[verification-guidance-guidance]] | guidance-for-guidance verifies against spec-for-guidance |

### INCOSE Paper Type Verification

| Edge | Description |
|------|-------------|
| [[verification-incose-paper-spec:spec-spec]] | INCOSE paper spec verifies |
| [[verification-incose-paper-guidance:spec-guidance]] | INCOSE paper guidance verifies |
| [[verification-incose-self-demonstration-spec:spec-spec]] | Self-demo spec verifies |
| [[verification-incose-self-demonstration-guidance:spec-guidance]] | Self-demo guidance verifies |

### Supporting Document Type Verification

| Edge | Description |
|------|-------------|
| [[verification-architecture-spec:spec-spec]] | Architecture spec verifies |
| [[verification-architecture-guidance:spec-guidance]] | Architecture guidance verifies |
| [[verification-lifecycle-spec:spec-spec]] | Lifecycle spec verifies |
| [[verification-lifecycle-guidance:spec-guidance]] | Lifecycle guidance verifies |
| [[verification-literature-review-spec:spec-spec]] | Literature review spec verifies |
| [[verification-literature-review-guidance:spec-guidance]] | Literature review guidance verifies |
| [[verification-novel-contributions-spec:spec-spec]] | Novel contributions spec verifies |
| [[verification-novel-contributions-guidance:spec-guidance]] | Novel contributions guidance verifies |

### Supporting Document Instance Verification

| Edge | Description |
|------|-------------|
| [[verification-architecture-incose:spec-architecture]] | Architecture doc verifies |
| [[verification-lifecycle-incose:spec-lifecycle]] | Lifecycle doc verifies |
| [[verification-literature-review-incose:spec-incose-literature-review]] | Literature review verifies |
| [[verification-novel-contributions-incose:spec-novel-contributions]] | Novel contributions verifies |

---

## Validation Edges

Assert that a document meets quality criteria. Qualitative, human-assessed checks.

**Pattern:** document → guidance

**Key property:** All validation edges require a `human_approver` field for accountability.

### Foundation Validation

| Edge | Description |
|------|-------------|
| [[validation-spec-spec]] | spec-for-spec validates against guidance-for-spec |
| [[validation-spec-guidance]] | spec-for-guidance validates against guidance-for-spec |
| [[validation-guidance-spec]] | guidance-for-spec validates against guidance-for-guidance |
| [[validation-guidance-guidance]] | guidance-for-guidance validates against itself |

### INCOSE Paper Type Validation

| Edge | Description |
|------|-------------|
| [[validation-incose-paper-spec:guidance-spec]] | INCOSE paper spec validates |
| [[validation-incose-paper-guidance:guidance-guidance]] | INCOSE paper guidance validates |
| [[validation-incose-self-demonstration-spec:guidance-spec]] | Self-demo spec validates |
| [[validation-incose-self-demonstration-guidance:guidance-guidance]] | Self-demo guidance validates |

### Supporting Document Instance Validation

| Edge | Description |
|------|-------------|
| [[validation-architecture-incose:guidance-architecture]] | Architecture doc validates |
| [[validation-lifecycle-incose:guidance-lifecycle]] | Lifecycle doc validates |
| [[validation-literature-review-incose:guidance-incose-literature-review]] | Literature review validates |
| [[validation-novel-contributions-incose:guidance-novel-contributions]] | Novel contributions validates |

---

## Signature Edges

### Signs Edges

Assert that a signer attests to a document's quality.

**Pattern:** signer → document

| Edge | Description |
|------|-------------|
| [[signs-mzargham:incose-paper-2026]] | Author signs paper (base) |
| [[signs-mzargham:incose-paper-2026-self-demo]] | Author signs paper (self-demo) |
| [[signs-mzargham:architecture-incose]] | Author signs architecture doc |
| [[signs-mzargham:lifecycle-incose]] | Author signs lifecycle doc |
| [[signs-mzargham:literature-review-incose]] | Author signs literature review |
| [[signs-mzargham:novel-contributions-incose]] | Author signs novel contributions |
| [[signs-root:spec-spec]] | Root signs SS |
| [[signs-root:spec-guidance]] | Root signs SG |
| [[signs-root:guidance-spec]] | Root signs GS |
| [[signs-root:guidance-guidance]] | Root signs GG |

### Qualifies Edges

Assert that a signer is qualified to validate against a guidance.

**Pattern:** signer → guidance

| Edge | Description |
|------|-------------|
| [[qualifies-mzargham:guidance-incose-paper]] | Author qualified for paper guidance |
| [[qualifies-mzargham:guidance-incose-self-demonstration]] | Author qualified for self-demo guidance |
| [[qualifies-mzargham:guidance-architecture]] | Author qualified for architecture guidance |
| [[qualifies-mzargham:guidance-lifecycle]] | Author qualified for lifecycle guidance |
| [[qualifies-mzargham:guidance-incose-literature-review]] | Author qualified for lit review guidance |
| [[qualifies-mzargham:guidance-novel-contributions]] | Author qualified for novel contributions guidance |
| [[qualifies-mzargham:guidance-spec]] | Author qualified for spec guidance |
| [[qualifies-mzargham:guidance-guidance]] | Author qualified for guidance guidance |
| [[qualifies-root:guidance-spec]] | Root qualified for spec guidance |
| [[qualifies-root:guidance-guidance]] | Root qualified for guidance guidance |

---

## Dependency & Inheritance Edges

### Dependency Edges

Express that one document depends on another.

| Edge | Description |
|------|-------------|
| [[dependency-incose-self-demonstration-spec:architecture-spec]] | Self-demo depends on architecture |
| [[dependency-incose-self-demonstration-spec:lifecycle-spec]] | Self-demo depends on lifecycle |
| [[dependency-incose-self-demonstration-spec:literature-review-spec]] | Self-demo depends on lit review |
| [[dependency-incose-self-demonstration-spec:novel-contributions-spec]] | Self-demo depends on novel contributions |

### Inheritance Edges

Express type inheritance relationships.

| Edge | Description |
|------|-------------|
| [[inherits-incose-self-demonstration:incose-paper]] | Self-demo extends INCOSE paper type |
| [[inherits-incose-self-demonstration-guidance:incose-paper-guidance]] | Self-demo guidance extends paper guidance |

---

## Boundary Edges

Connect to the root anchor for trust chain grounding.

| Edge | Description |
|------|-------------|
| [[b1-self-verification]] | Foundation self-verification |
| [[b1-self-validation]] | Foundation self-validation |
| [[b1-couples-GS-root]] | GS coupled to root |
| [[b1-couples-SG-root]] | SG coupled to root |

---

## Key Patterns

### The Assurance Triangle

Every assured document has three edges forming a triangle:

```text
        doc
       /   \
verification  validation
     /         \
   spec ←——→ guidance
      coupling
```

### The Signature Triangle

Every signed document has three edges:

```text
       doc
      /   \
   signs   validation
    /         \
signer ←——→ guidance
     qualifies
```

### Common Boundary

Assurance and signature faces share the **validation edge** as their common boundary.

---

## Naming Conventions

- `coupling-<type>.md` — Couples spec and guidance for a type
- `verification-<target>:<spec>.md` — Target verifies against spec
- `validation-<target>:<guidance>.md` — Target validates against guidance
- `signs-<signer>:<document>.md` — Signer attests to document
- `qualifies-<signer>:<guidance>.md` — Signer qualified for guidance
- `cites-<source>:<target>.md` — Source cites target
- `dependency-<source>:<target>.md` — Source depends on target
- `inherits-<child>:<parent>.md` — Child inherits from parent
- `b1-<name>.md` — Boundary edge

---

## Related Directories

| Directory | Description |
|-----------|-------------|
| [[../00_vertices/README]] | The nodes edges connect |
| [[../02_faces/README]] | Triangular patterns using edges |
| [[../charts/README]] | Composed simplicial complexes |
| [[../templates/README]] | Type definitions for creating edges |
