---
type: template/vertex/signer
extends: actor
id: template:vertex:signer
name: Signer Type Template
description: Actors with verified GitHub identity who can sign validation edges
instantiable: true
tags:
  - template
  - vertex
  - actor
  - signer
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Signer Type Template

**Actors with verified GitHub identity who can sign validation edges.**

Signers represent humans with cryptographically verifiable identity (via GitHub username and commit signatures) who can attest to validation assessments. They participate in signature faces that complement assurance faces.

## Type Hierarchy

```
vertex (abstract)
└── actor (concrete)
    └── signer (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `actor`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all actor/vertex fields, plus signer-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/signer` |
| `extends` | string | Must be `actor` |
| `id` | string | Format: `v:signer:<github-username>` |
| `github_username` | string | **REQUIRED** - GitHub username (must match id suffix) |
| `tags` | array | Must include `[vertex, actor, signer]` |

## Tag Requirements

```yaml
tags:
  - vertex
  - actor
  - signer
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description of signer |
| `organization` | string | Organization affiliation |
| `email` | string | Contact email |

## Required Body Sections

### From Actor

- **Purpose** - Statement of what this signer represents
- **Actor Identity** - Identity and characteristics
- **Capabilities** - What the signer can do (≥2 items)
- **Properties** - What the signer can possess (≥1 item)

### Signer-Specific

- **Identity Verification** - GitHub username and verification method
- **Signing Authority** - What domains/types the signer is qualified to sign (≥1 item)

## Role in Signature Pattern

Signers are the accountability vertex in signature faces:

```
signature face (doc, guidance, signer):
  doc → guidance (validation edge - SHARED with assurance)
  signer → doc (signs edge - attestation event)
  signer → guidance (qualifies edge - credential)
```

## Relationship to Assurance

Signature faces **complement** assurance faces by:
1. Sharing the validation edge (common boundary)
2. Making the signer explicit (vs. just metadata in validation edge)
3. Recording the qualifies credential at signing time

## Example Instance

```yaml
---
type: vertex/signer
extends: actor
id: v:signer:mzargham
name: Michael Zargham
github_username: mzargham
description: Chief Engineer and primary signer for knowledge complex documents
organization: BlockScience
tags:
  - vertex
  - actor
  - signer
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies:
  - v:spec:actor
---

# Michael Zargham

## Purpose

This signer represents Michael Zargham, Chief Engineer responsible for signing validation assessments and assurance attestations in the knowledge complex.

## Actor Identity

Michael Zargham is the Chief Engineer at BlockScience, with expertise in systems engineering, mathematical modeling, and knowledge management frameworks. As a signer, he provides human accountability for validation assessments generated with LLM assistance.

## Capabilities

- **Sign Validations**: Can attest to validation assessments against guidance documents
- **Approve Assurances**: Can approve assurance faces as the human approver
- **Review Technical Content**: Can evaluate technical documentation quality

## Properties

- **Signing Authority**: Holds qualification credentials for signing in multiple domains
- **GitHub Identity**: Verified through commit signatures

## Identity Verification

**GitHub Username:** mzargham
**Verification Method:** Commits to this repository are signed with verified GPG key associated with this GitHub account. The signing identity is verified through GitHub's commit signature verification.

## Signing Authority

- **Specification Documents**: Qualified to sign validation assessments for spec documents based on expertise in systems engineering methodology
- **Guidance Documents**: Qualified to sign validation assessments for guidance documents based on experience establishing quality criteria
- **Framework Architecture**: Qualified to sign architectural decisions based on role as Chief Engineer
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/signer`
2. **Extends:** `extends` must be `actor`
3. **ID Format:** `id` must match `v:signer:<github-username>`
4. **GitHub Username:** `github_username` REQUIRED and must match id suffix
5. **Tag Chain:** Tags must include `[vertex, actor, signer]`
6. **Actor Compliance:** Must satisfy all actor requirements
7. **Body Sections:** Must include Identity Verification and Signing Authority sections