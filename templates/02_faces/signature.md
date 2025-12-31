---
type: template/face/signature
extends: face
id: template:face:signature
name: Signature Face Template
description: Accountability triangle coupling doc, guidance, and signer with shared validation edge
instantiable: true
edges:
  - validation_edge (shared with assurance face)
  - signs_edge
  - qualifies_edge
orientation: oriented
tags:
  - template
  - face
  - signature
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Signature Face Template

**Accountability triangle coupling doc, guidance, and signer.**

Signature faces complement assurance faces by making human accountability explicit. They share the validation edge with the corresponding assurance face, creating a common boundary that connects structural assurance to accountability assurance.

## Type Hierarchy

```
face (abstract)
└── signature (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `face`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `face/signature` |
| `extends` | string | Must be `face` |
| `id` | string | Format: `f:signature:<doc>:<signer>` |
| `vertices` | array | Exactly 3: [doc, guidance, signer] |
| `doc` | string | Document vertex ID |
| `guidance` | string | Guidance vertex ID |
| `signer` | string | Signer vertex ID |
| `boundary` | array | Exactly 3: [validation, signs, qualifies] |
| `validation_edge` | string | Validation edge ID (shared with assurance) |
| `signs_edge` | string | Signs edge ID |
| `qualifies_edge` | string | Qualifies edge ID |
| `signing_date` | datetime | When signature was created |
| `commit_hash` | string | Git commit recording signature |
| `tags` | array | Must include `[face, signature]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `assurance_face` | string | ID of corresponding assurance face |
| `description` | string | Brief description |

## Tag Requirements

```yaml
tags:
  - face
  - signature
```

## Required Body Sections

- **Face Description** - Type, signing date, commit, summary
- **Vertices** - Document, guidance, signer with roles
- **Edges (Boundary)** - Validation (shared), signs, qualifies
- **Triangle Coherence** - Topological and completeness checks
- **Accountability Statement** - Formal statement with signer identity

## Relationship to Assurance

```
                    doc
                   / | \
                  /  |  \
                 /   |   \
         verification | validation (SHARED)
               /     |     \
              /      |      \
           spec    signs   guidance
              \      |      /
               \     |     /
          coupling   |  qualifies
                 \   |   /
                  \  |  /
                   signer

Assurance Face: (doc, spec, guidance)
Signature Face: (doc, guidance, signer)
Common Boundary: validation edge
```

## Example Instance

```yaml
---
type: face/signature
extends: face
id: f:signature:spec-persona:mzargham
name: Signature - spec-for-persona by mzargham
description: Signature face recording mzargham's attestation to spec-for-persona
vertices:
  - v:spec:persona
  - v:guidance:spec
  - v:signer:mzargham
doc: v:spec:persona
guidance: v:guidance:spec
signer: v:signer:mzargham
boundary:
  - e:validation:spec-persona:guidance-spec
  - e:signs:mzargham:spec-persona
  - e:qualifies:mzargham:guidance-spec
validation_edge: e:validation:spec-persona:guidance-spec
signs_edge: e:signs:mzargham:spec-persona
qualifies_edge: e:qualifies:mzargham:guidance-spec
signing_date: 2025-12-30T12:00:00Z
commit_hash: abc123def456
assurance_face: f:assurance:spec-persona
tags:
  - face
  - signature
version: 1.0.0
created: 2025-12-30T12:00:00Z
modified: 2025-12-30T12:00:00Z
---

# Signature - spec-for-persona by mzargham

This signature face records mzargham's attestation to spec-for-persona based on validation against guidance-for-spec.

## Face Description

**Type:** Signature Triangle
**Signing Date:** 2025-12-30T12:00:00Z
**Commit:** abc123def456

This signature face records Michael Zargham's attestation to spec-for-persona based on validation against guidance-for-spec. It complements the assurance face by making the signer explicit.

## Vertices

1. **[spec-for-persona](../00_vertices/spec-for-persona.md)** (`v:spec:persona`)
   - The document being signed
   - Type: vertex/spec
   - Role: Target of signature

2. **[guidance-for-spec](../00_vertices/guidance-for-spec.md)** (`v:guidance:spec`)
   - Quality criteria for validation
   - Type: vertex/guidance
   - Role: Validation target

3. **[mzargham](../00_vertices/signer-mzargham.md)** (`v:signer:mzargham`)
   - The signing authority
   - Type: vertex/signer
   - GitHub: mzargham
   - Role: Accountable party

## Edges (Boundary)

1. **[validation-spec-persona:guidance-spec](../01_edges/validation-spec-persona:guidance-spec.md)** (`e:validation:spec-persona:guidance-spec`)
   - Source: spec-for-persona → Target: guidance-for-spec
   - Type: edge/validation
   - Status: Pass
   - **SHARED** with assurance face: f:assurance:spec-persona

2. **[signs-mzargham:spec-persona](../01_edges/signs-mzargham:spec-persona.md)** (`e:signs:mzargham:spec-persona`)
   - Source: mzargham → Target: spec-for-persona
   - Type: edge/signs
   - Signing Date: 2025-12-30T12:00:00Z
   - Commit: abc123def456

3. **[qualifies-mzargham:guidance-spec](../01_edges/qualifies-mzargham:guidance-spec.md)** (`e:qualifies:mzargham:guidance-spec`)
   - Source: mzargham → Target: guidance-for-spec
   - Type: edge/qualifies
   - Credential Type: role
   - Valid At: Confirmed valid at signing time

## Triangle Coherence

**Topological Properties:**
- **Closed Boundary:** All three edges form a cycle
- **Complete:** All vertices connected by edges
- **Oriented:** Validation and qualifies directed to guidance; signs directed to doc

**Signature Completeness:**
- ✓ Validation assessment exists and passed
- ✓ Signer qualification verified at signing time
- ✓ Signing event recorded with commit hash
- ✓ Shared boundary with assurance face f:assurance:spec-persona

## Accountability Statement

This signature records that Michael Zargham (mzargham) attested to spec-for-persona on 2025-12-30.

The signer's qualification was verified through e:qualifies:mzargham:guidance-spec, which establishes role authority to validate against guidance-for-spec.

This signature is recorded in commit abc123def456 and can be verified through GitHub's commit signature verification.

**Signed:** Michael Zargham
**GitHub:** mzargham
**Date:** 2025-12-30T12:00:00Z

## Related Assurance

**Assurance Face:** [f:assurance:spec-persona](assurance-spec-persona.md)
**Shared Edge:** e:validation:spec-persona:guidance-spec

This signature face complements the assurance face by making the signer explicit. Together they form a complete accountability and quality assurance record.
```

## Validation Rules

1. **Type Format:** `type` must be `face/signature`
2. **Vertex Count:** Must have exactly 3 vertices
3. **Vertex Types:** Must include one doc, one guidance, one signer
4. **Edge Count:** Must have exactly 3 boundary edges
5. **Edge Types:** Must include validation, signs, qualifies edges
6. **Triangle Formation:** Edges must form closed boundary cycle
7. **Signing Metadata:** `signing_date` and `commit_hash` required
8. **Tag Chain:** Tags must include `[face, signature]`
9. **Shared Edge:** If `assurance_face` present, `validation_edge` must be shared
10. **Body Content:** Must include all required sections with accountability statement
