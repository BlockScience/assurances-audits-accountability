---
type: vertex/spec
extends: doc
id: v:spec:signs
name: Specification for Signs Edge Documents
description: Defines what makes a valid signs edge - attestation event where signer attests to a document
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies: []
---

# Specification for Signs Edge Documents

**This specification defines the structure and requirements for signs edge documents in the knowledge complex.**

## Purpose

Signs edges represent **attestation events** where a signer formally attests to a document. Unlike validation edges which record quality assessments, signs edges record the specific moment when a qualified signer puts their name to a document. The signs edge captures the signing event metadata: who signed, when, and the commit hash that records the signature.

## Semantic Meaning

A signs edge from signer S to document D means:
- "S attested to D at a specific point in time"
- "S's identity is verified through the commit signature"
- "S was qualified to sign at the time of signing"

## Required Frontmatter Fields

All signs edge documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `edge/signs` |
| `extends` | string | REQUIRED | Must be `edge` |
| `id` | string | REQUIRED | Unique identifier (format: `e:signs:<signer>:<doc>`) |
| `name` | string | REQUIRED | Human-readable edge name |
| `tags` | array[string] | REQUIRED | Must include `[edge, signs]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Endpoint Fields

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `source` | string | REQUIRED | Signer vertex ID (format: `v:signer:<username>`) |
| `target` | string | REQUIRED | Document vertex ID being signed |
| `source_type` | string | REQUIRED | Must be `vertex/signer` |
| `target_type` | string | REQUIRED | Document type (e.g., `vertex/spec`, `vertex/guidance`) |
| `orientation` | string | REQUIRED | Must be `directed` |

### Signing Event Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `signing_date` | datetime | REQUIRED | ISO 8601 timestamp of signing event |
| `commit_hash` | string | REQUIRED | Git commit hash recording the signature |
| `qualifies_edge` | string | REQUIRED | ID of the qualifies edge that was valid at signing |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

## Required Body Sections

### 1. Signing Event

**Format:**
```markdown
## Signing Event

**Signer:** [Link to signer vertex]
**Document:** [Link to document being signed]
**Date:** [ISO 8601 timestamp]
**Commit:** [commit hash]

[Brief description of what is being attested]
```

### 2. Qualification at Signing

**Format:**
```markdown
## Qualification at Signing

**Qualifies Edge:** [Link to qualifies edge]
**Credential Type:** [type from qualifies edge]
**Valid At:** [confirmation that qualifies edge was valid at signing_date]

[Statement confirming qualification was checked]
```

**Requirements:**
- MUST reference the qualifies edge that was checked
- MUST confirm the qualifies edge was valid (not expired) at signing time
- Serves as evidence that signing prerequisites were met

### 3. Attestation Statement

**Format:**
```markdown
## Attestation Statement

I, [signer name], attest to [document name] on [date].

This attestation is recorded in commit [hash] and can be verified through the Git signature.

**Signed:** [GitHub username]
**Date:** [signing_date]
```

## Optional Body Sections

### Context

Additional context about why this signature was made:

```markdown
## Context

[Why this document is being signed, what it represents]
```

### Supersedes

If this signature replaces a previous one:

```markdown
## Supersedes

**Previous Signature:** [link to previous signs edge]
**Reason:** [why re-signing was necessary]
```

## Type Constraints

1. **Type Field:** MUST be exactly `edge/signs`
2. **Extends Field:** MUST be exactly `edge`
3. **ID Format:** MUST match pattern `e:signs:[signer-username]:[doc-name]`
4. **Source Type:** Source MUST be `vertex/signer`
5. **Target Type:** Target MUST be a document type (`vertex/doc` or subtype)
6. **Orientation:** MUST be `directed`
7. **Tag Inheritance:** Tags MUST include: `[edge, signs]`

## Signing Prerequisites

Before a signs edge can be created:

1. **Signer Exists:** The source signer vertex must exist
2. **Document Exists:** The target document must exist
3. **Qualifies Valid:** A qualifies edge from signer to relevant guidance must be valid (non-expired)
4. **Commit Signature:** The commit creating this edge must be signed by the signer's GitHub account

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

The signs edge:
- Connects signer to document (attestation event)
- Records the moment of signing (timestamp, commit)
- Requires valid qualifies edge (credential check)

## Verification vs. Validation

- **Verification** (against this spec): Check required fields, commit_hash format, qualifies_edge reference
- **Validation** (against guidance-for-signs): Assess whether attestation is appropriate, context clear

## Schema Summary

```yaml
# Required frontmatter
type: edge/signs
extends: edge
id: e:signs:<signer>:<doc>
name: <string>
source: v:signer:<username>
target: <document-vertex-id>
source_type: vertex/signer
target_type: <document-type>
orientation: directed
signing_date: <ISO8601>
commit_hash: <git-commit-hash>
qualifies_edge: <qualifies-edge-id>
tags: [edge, signs]
version: <semver>
created: <ISO8601>
modified: <ISO8601>

# Optional frontmatter
description: <string>

# Required body sections (markdown)
## Signing Event
## Qualification at Signing
## Attestation Statement

# Optional body sections
## Context
## Supersedes
```

## Compliance

A document claiming `type: edge/signs` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. Source is a valid signer vertex ID
3. Target is a valid document vertex ID
4. commit_hash is a valid Git commit hash format
5. qualifies_edge references an existing qualifies edge
6. All REQUIRED body sections are present
7. Attestation statement includes signer identity and date
8. Type constraints are satisfied

---

**Note:** Signs edges record attestation events - the specific moment when a qualified signer puts their name to a document. They differ from validation edges in that they capture the event itself (who, when, commit) rather than the quality assessment. Together with qualifies and validation edges, they form signature faces that complement assurance faces.
