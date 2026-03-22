---
type: face/assurance
id: b2:guidance-spec
name: Boundary Face - Guidance-for-Spec Genesis Assurance
description: Genesis assurance for guidance-for-spec - foundational document exempt from signature requirements
edges:
  - e:DocType:guidance
  - e:verification:guidance-spec:spec-guidance
  - e:validation:guidance-spec:guidance-guidance
doc_name: Guidance-for-Spec
signed_by: Michael Zargham
status: assured
axiomatic: true
tags:
  - boundary
  - assurance
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Boundary Face - Guidance-for-Spec Genesis Assurance

This is a **boundary face (b2)** providing foundational assurance for guidance-for-spec (GS), one of the four genesis documents that form the core infrastructure of the knowledge complex.

## Genesis Document Status

**GS (guidance-for-spec)** is one of four foundational documents (SS, SG, GS, GG) that:

- Come into existence at genesis
- Are exempt from standard signature requirements
- Form the core infrastructure on which all other assurance depends
- Have special update rules (to be developed in future enhancements)

### Design Decision

These four documents are treated as essentially fixed for a given knowledge complex. While future enhancements may develop specific handling for versioning and signing updates to SS, SG, GS, GG, they are currently treated as foundational infrastructure exempt from the standard accountability chain.

**Rationale:** Everything else in the knowledge complex depends on these four documents. Requiring signatures on them would create circular dependencies since the signature chain itself depends on these documents being assured.

## Face Structure

**Vertices:**

1. `v:guidance:spec` (GS) - The target document
2. `v:spec:guidance` (SG) - Verification spec
3. `v:guidance:guidance` (GG) - Validation guidance

**Edges:**

1. `e:DocType:guidance` - Couples SG↔GG (standard coupling for guidance domain)
2. `e:verification:guidance-spec:spec-guidance` - GS verifies against SG
3. `e:validation:guidance-spec:guidance-guidance` - GS validates against GG

## Standard Triangle Pattern

Unlike b2:spec-spec and b2:guidance-guidance which resolve self-referential loops via b0:root, this face uses standard assurance edges:

```
        SG ----------- GG
          \           /
  verification    validation
            \       /
             \     /
               GS
```

- **Verification:** GS → SG (guidance-for-spec verifies against spec-for-guidance)
- **Validation:** GS → GG (guidance-for-spec validates against guidance-for-guidance)
- **Coupling:** SG ↔ GG (standard coupling edge)

No self-reference exists because GS is verified by SG (not itself) and validated by GG (not itself).

## Genesis Assurance

Despite having a standard triangle pattern, this face is designated b2 because:

1. **Genesis Document:** GS comes into being at system creation
2. **Signature Exempt:** No human signature required
3. **Foundation:** Part of the infrastructure that enables all other signatures

## Assurance Status

- **Status:** ASSURED
- **Method:** Genesis (instantiated at system creation)
- **Signature Required:** No (genesis document)

## Related Elements

- **Partner Boundary Faces:**
  - b2:spec-spec (SS) - self-referential, uses root
  - b2:spec-guidance (SG) - standard pattern
  - b2:guidance-guidance (GG) - self-referential, uses root

- **Coupling Edge:** e:DocType:guidance (SG↔GG)
- **Verification Edge:** e:verification:guidance-spec:spec-guidance
- **Validation Edge:** e:validation:guidance-spec:guidance-guidance

---

**Note:** This is a genesis boundary face (b2). It provides foundational assurance for guidance-for-spec without requiring the standard signature chain. Future versions may implement special rules for updating genesis documents.
