---
type: template/edge/signs
extends: edge
id: template:edge:signs
name: Signs Edge Template
description: Connects a signer to a document they attest to (signing event)
instantiable: true
tags:
  - template
  - edge
  - signs
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Signs Edge Template

**Connects a signer to a document they formally attest to.**

Signs edges represent attestation events - the specific moment when a qualified signer puts their name to a document. They record who signed, when, and the commit hash that captures the signature.

## Type Hierarchy

```
edge (abstract)
└── signs (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus signs-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/signs` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:signs:<signer>:<doc>` |
| `source` | string | Signer ID (format: `v:signer:<username>`) |
| `target` | string | Document ID being signed |
| `source_type` | string | Must be `vertex/signer` |
| `target_type` | string | Document type (e.g., `vertex/spec`) |
| `orientation` | string | Must be `directed` |
| `signing_date` | datetime | When the signing occurred |
| `commit_hash` | string | Git commit hash recording signature |
| `qualifies_edge` | string | ID of qualifies edge valid at signing |
| `tags` | array | Must include `[edge, signs]` |

## Tag Requirements

```yaml
tags:
  - edge
  - signs
```

## Required Body Sections

- **Signing Event** - Signer, document, date, commit, and description
- **Qualification at Signing** - Reference to qualifies edge with validity confirmation
- **Attestation Statement** - Formal attestation with signer identity and date

## Role in Signature Pattern

Signs edges form the attestation side of signature faces:

```
          doc
         /    \
        /      \
   signs      validation (shared with assurance)
      /          \
     /            \
 signer -------- guidance
         qualifies
```

**Key property:** The signs edge records a specific event. The commit_hash provides cryptographic evidence of the signing through Git commit signatures.

## Signing Prerequisites

Before creating a signs edge:

1. **Signer Exists:** Source signer vertex must exist
2. **Document Exists:** Target document must exist
3. **Qualifies Valid:** qualifies edge from signer to relevant guidance must be non-expired
4. **Commit Signed:** The commit must be signed by signer's GitHub account

## Example Instance

```yaml
---
type: edge/signs
extends: edge
id: e:signs:mzargham:spec-persona
name: Signs - mzargham signs spec-for-persona
source: v:signer:mzargham
target: v:spec:persona
source_type: vertex/signer
target_type: vertex/spec
orientation: directed
signing_date: 2025-12-30T12:00:00Z
commit_hash: abc123def456
qualifies_edge: e:qualifies:mzargham:guidance-spec
tags:
  - edge
  - signs
version: 1.0.0
created: 2025-12-30T12:00:00Z
modified: 2025-12-30T12:00:00Z
---

# Signs - mzargham signs spec-for-persona

This signs edge records Michael Zargham's attestation to spec-for-persona.

## Signing Event

**Signer:** [mzargham](../00_vertices/signer-mzargham.md)
**Document:** [spec-for-persona](../00_vertices/spec-for-persona.md)
**Date:** 2025-12-30T12:00:00Z
**Commit:** abc123def456

Michael Zargham attests to the quality and correctness of spec-for-persona as Chief Engineer.

## Qualification at Signing

**Qualifies Edge:** [e:qualifies:mzargham:guidance-spec](qualifies-mzargham:guidance-spec.md)
**Credential Type:** role
**Valid At:** Confirmed - qualifies edge has no expiry date and was valid at 2025-12-30T12:00:00Z

The signer's qualification to validate against guidance-for-spec was verified prior to signing.

## Attestation Statement

I, Michael Zargham (mzargham), attest to spec-for-persona on 2025-12-30.

This attestation is recorded in commit abc123def456 and can be verified through the Git signature associated with my GitHub account.

**Signed:** mzargham
**Date:** 2025-12-30T12:00:00Z
```

## Validation Rules

1. **Type Format:** `type` must be `edge/signs`
2. **Source Type:** Source must be a signer (`vertex/signer`)
3. **Target Type:** Target must be a document (`vertex/doc` or subtype)
4. **Orientation:** Must be `directed`
5. **Required Metadata:** `signing_date`, `commit_hash`, `qualifies_edge` must be present
6. **Commit Hash:** Must be valid Git commit hash format
7. **Qualifies Reference:** `qualifies_edge` must reference existing qualifies edge
8. **Tag Chain:** Tags must include `[edge, signs]`
9. **Body Content:** Must include signing event, qualification check, and attestation statement
