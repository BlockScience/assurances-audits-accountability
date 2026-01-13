---
type: face/b2
extends: face
id: b2:spec-guidance
name: Boundary Face - Spec-for-Guidance Genesis Assurance
description: Genesis assurance for spec-for-guidance - foundational document exempt from signature requirements
vertices:
  - v:spec:guidance
  - v:spec:spec
  - v:guidance:spec
edges:
  - e:coupling:spec
  - e:verification:spec-guidance:spec-spec
  - e:validation:spec-guidance:guidance-spec
orientation: oriented
target: v:spec:guidance
spec: v:spec:spec
guidance: v:guidance:spec
coupling_edge: e:coupling:spec
verification_edge: e:verification:spec-guidance:spec-spec
validation_edge: e:validation:spec-guidance:guidance-spec
status: ASSURED
tags:
  - face
  - boundary
  - b2
  - assurance
  - genesis
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Boundary Face - Spec-for-Guidance Genesis Assurance

This is a **boundary face (b2)** providing foundational assurance for spec-for-guidance (SG), one of the four genesis documents that form the core infrastructure of the knowledge complex.

## Genesis Document Status

**SG (spec-for-guidance)** is one of four foundational documents (SS, SG, GS, GG) that:

- Come into existence at genesis
- Are exempt from standard signature requirements
- Form the core infrastructure on which all other assurance depends
- Have special update rules (to be developed in future enhancements)

### Design Decision

These four documents are treated as essentially fixed for a given knowledge complex. While future enhancements may develop specific handling for versioning and signing updates to SS, SG, GS, GG, they are currently treated as foundational infrastructure exempt from the standard accountability chain.

**Rationale:** Everything else in the knowledge complex depends on these four documents. Requiring signatures on them would create circular dependencies since the signature chain itself depends on these documents being assured.

## Face Structure

**Vertices:**

1. `v:spec:guidance` (SG) - The target document
2. `v:spec:spec` (SS) - Verification spec
3. `v:guidance:spec` (GS) - Validation guidance

**Edges:**

1. `e:coupling:spec` - Couples SS↔GS (standard coupling for spec domain)
2. `e:verification:spec-guidance:spec-spec` - SG verifies against SS
3. `e:validation:spec-guidance:guidance-spec` - SG validates against GS

## Standard Triangle Pattern

Unlike b2:spec-spec and b2:guidance-guidance which resolve self-referential loops via b0:root, this face uses standard assurance edges:

```
        SS ----------- GS
          \           /
  verification    validation
            \       /
             \     /
               SG
```

- **Verification:** SG → SS (spec-for-guidance verifies against spec-for-spec)
- **Validation:** SG → GS (spec-for-guidance validates against guidance-for-spec)
- **Coupling:** SS ↔ GS (standard coupling edge)

No self-reference exists because SG is verified by SS (not itself) and validated by GS (not itself).

## Genesis Assurance

Despite having a standard triangle pattern, this face is designated b2 because:

1. **Genesis Document:** SG comes into being at system creation
2. **Signature Exempt:** No human signature required
3. **Foundation:** Part of the infrastructure that enables all other signatures

## Assurance Status

- **Status:** ASSURED
- **Method:** Genesis (instantiated at system creation)
- **Signature Required:** No (genesis document)

## Related Elements

- **Partner Boundary Faces:**
  - b2:spec-spec (SS) - self-referential, uses root
  - b2:guidance-spec (GS) - standard pattern
  - b2:guidance-guidance (GG) - self-referential, uses root

- **Coupling Edge:** e:coupling:spec (SS↔GS)
- **Verification Edge:** e:verification:spec-guidance:spec-spec
- **Validation Edge:** e:validation:spec-guidance:guidance-spec

---

**Note:** This is a genesis boundary face (b2). It provides foundational assurance for spec-for-guidance without requiring the standard signature chain. Future versions may implement special rules for updating genesis documents.
