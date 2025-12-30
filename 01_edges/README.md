# Edges (1-Cells)

Relationships connecting vertices in the knowledge complex. Edges represent typed connections between documents.

## Summary

| Type | Count | Description |
|------|-------|-------------|
| **Coupling** | 16 | Spec-guidance alignment |
| **Verification** | 37 | Doc-spec conformance |
| **Validation** | 37 | Doc-guidance assessment |
| **Dependency** | 8 | Requirement relationships |
| **Boundary** | 4 | Connections to root |

**Total:** 104 edges (2 untracked additions pending)

## Edge Types

### Coupling Edges (coupling-*)

Link paired spec and guidance documents. These edges assert that a spec and its corresponding guidance are designed to work together.

**Pattern:** spec ↔ guidance

**Examples:**
- [[coupling-spec]] - Links spec-for-spec with guidance-for-spec
- [[coupling-guidance]] - Links spec-for-guidance with guidance-for-guidance
- [[coupling-charts]] - Links spec-for-charts with guidance-for-charts
- [[coupling-incose-paper]] - Links spec/guidance for INCOSE papers

### Verification Edges (verification-*)

Assert that a document conforms to its specification. These are deterministic, automatable checks.

**Pattern:** doc → spec

**Format:** `verification-<target>:<spec>.md`

**Examples:**
- [[verification-incose-paper-spec:spec-spec]] - INCOSE paper spec verifies against spec-for-spec
- [[verification-architecture-spec:spec-spec]] - Architecture spec verifies against spec-for-spec
- [[verification-guidance-spec:spec-guidance]] - guidance-for-spec verifies against spec-for-guidance

### Validation Edges (validation-*)

Assert that a document meets quality criteria. These are qualitative, human-assessed checks.

**Pattern:** doc → guidance

**Format:** `validation-<target>:<guidance>.md`

**Examples:**
- [[validation-incose-paper-spec:guidance-spec]] - INCOSE paper spec validates against guidance-for-spec
- [[validation-architecture-spec:guidance-spec]] - Architecture spec validates against guidance-for-spec
- [[validation-novel-contributions-spec:guidance-spec]] - Novel contributions spec validates

### Dependency Edges (dependency-*)

Express that one document depends on another. Used for tracking requirements flow.

**Pattern:** dependent → dependency

**Examples:**
- [[dependency-incose-self-demonstration-spec:incose-paper-spec]] - Self-demo extends INCOSE paper spec
- [[dependency-incose-self-demonstration-spec:architecture-spec]] - Self-demo requires architecture

### Boundary Edges (b1-*)

Connect to the root anchor for trust chain grounding.

- [[b1-self-verification]] - Foundation self-verification
- [[b1-self-validation]] - Foundation self-validation
- [[b1-couples-GS-root]] - GS coupled to root
- [[b1-couples-SG-root]] - SG coupled to root

### Future: Signature Edges

When signature infrastructure is complete:

- **qualifies-*** - Signer qualified for guidance
- **signs-*** - Signer attests to document

## Key Patterns

### The Assurance Triangle

Every assured document has three edges forming a triangle:

```
        doc
       /   \
verification  validation
     /         \
   spec ←——→ guidance
      coupling
```

### The Signature Triangle (Future)

Every signed document will have three edges:

```
       doc
      /   \
   signs   validation
    /         \
signer ←——→ guidance
     qualifies
```

### Common Boundary

Assurance and signature faces share the **validation edge** as their common boundary, connecting accountability to quality.

## Naming Convention

- `coupling-<type>.md` - Couples spec and guidance for a type
- `verification-<target>:<spec>.md` - Target verifies against spec
- `validation-<target>:<guidance>.md` - Target validates against guidance
- `dependency-<source>:<target>.md` - Source depends on target
- `b1-<name>.md` - Boundary edge

## Related Directories

- [[../00_vertices/README|Vertices]] - The nodes edges connect
- [[../02_faces/README|Faces]] - Triangular patterns using edges
- [[../charts/README|Charts]] - Composed simplicial complexes
