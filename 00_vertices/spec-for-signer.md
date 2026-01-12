---
type: vertex/spec
extends: doc
id: v:spec:signer
name: Specification for Signer Documents
description: Defines what makes a valid signer document - actors with verified GitHub identity who can sign validation edges
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies:
  - v:spec:actor
---

# Specification for Signer Documents

**This specification defines the structure and requirements for signer documents in the knowledge complex.**

## Purpose

Signer documents define **actors with verified identity** who can attest to validation assessments through signature faces. A signer extends actor with a required GitHub username, providing identity verification through commit attribution (git blame). Signers participate in signature faces that complement assurance faces by explicitly representing the human accountability for validation.

## Inheritance

This specification **extends** `vertex/actor` (v:spec:actor).

All requirements from spec-for-actor apply, PLUS the additional requirements defined here.

## Required Frontmatter Fields

All signer documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/signer` |
| `extends` | string | REQUIRED | Must be `vertex/actor` |
| `id` | string | REQUIRED | Unique identifier (format: `v:signer:<github-username>`) |
| `name` | string | REQUIRED | Human-readable signer name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, actor, signer]` (full inheritance chain) |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Identity Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `github_username` | string | REQUIRED | GitHub username (must match id suffix) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of signer |
| `organization` | string | OPTIONAL | Organization affiliation |
| `email` | string | OPTIONAL | Contact email |

## Required Body Sections

### Inherited from spec-for-actor

The markdown body MUST contain all sections required by spec-for-actor:

1. **Purpose** - Statement of what this signer represents
2. **Actor Identity** - Identity and characteristics
3. **Capabilities** - What the signer can do (≥2 items)
4. **Properties** - What the signer can possess (≥1 item)

### Additional Required Sections for Signer

#### 5. Identity Verification

How the signer's identity is verified.

**Format:**
```markdown
## Identity Verification

**GitHub Username:** [username]
**Verification Method:** [How identity is verified - typically commit signatures]
```

**Requirements:**
- MUST include the GitHub username
- MUST describe how identity verification works
- SHOULD reference commit signing if applicable

#### 6. Signing Authority

What the signer is qualified to sign.

**Format:**
```markdown
## Signing Authority

- **[Domain/Type 1]**: [Description of what they can sign and why]
- **[Domain/Type 2]**: [Description of what they can sign and why]
```

**Requirements:**
- MUST list at least 1 signing authority domain
- Each authority SHOULD reference qualification credentials
- SHOULD align with qualifies edges the signer holds

## Optional Body Sections

### Qualifications

Credentials or expertise that establish signing authority.

**Format:**
```markdown
## Qualifications

- **[Qualification 1]**: [Description and evidence]
- **[Qualification 2]**: [Description and evidence]
```

### Signing History

Record of significant signatures made.

**Format:**
```markdown
## Signing History

- **[Date]**: [Document signed] - [Context]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/signer`
2. **Extends Field:** MUST be exactly `vertex/actor`
3. **ID Format:** MUST match pattern `v:signer:[github-username]`
4. **GitHub Username:** MUST match the username in the id field
5. **Tag Inheritance:** Tags MUST include full chain: `[vertex, actor, signer]`
6. **Dependencies:** MUST include `v:spec:actor` in dependencies array

## Content Requirements

1. **Actor Compliance:** MUST satisfy all requirements of spec-for-actor
2. **Identity:** GitHub username must be valid and match id
3. **Authority:** Must specify at least one signing authority domain
4. **Verification:** Must describe identity verification method

## Relationship Patterns

Signers participate in specific relationship patterns:

### qualifies Edges

```yaml
# Signer is qualified to validate against a guidance
type: edge/qualifies
source: v:signer:mzargham
target: v:guidance:spec
```

### signs Edges

```yaml
# Signer attests to a document (signing event)
type: edge/signs
source: v:signer:mzargham
target: v:spec:persona
```

### signature Faces

```yaml
# Complete signature pattern: doc, guidance, signer
type: face/signature
vertices:
  - v:spec:persona
  - v:guidance:spec
  - v:signer:mzargham
# shares validation edge with corresponding assurance face
```

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present, github_username matches id
- **Validation** (against guidance-for-signer): Qualitative assessment of authority appropriateness, identity clarity

## Schema Summary

```yaml
# Required frontmatter
type: vertex/signer
extends: vertex/actor
id: v:signer:<github-username>
name: <string>
github_username: <github-username>  # MUST match id suffix
tags: [vertex, actor, signer]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies:
  - v:spec:actor

# Optional frontmatter
description: <string>
organization: <string>
email: <string>

# Required body sections (markdown)
## Purpose
## Actor Identity
## Capabilities (≥2 items) [from actor]
## Properties (≥1 item) [from actor]
## Identity Verification [signer-specific]
## Signing Authority (≥1 item) [signer-specific]

# Optional body sections
## Qualifications
## Signing History
```

## Compliance

A document claiming `type: vertex/signer` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. `github_username` field matches the username portion of the id
3. All REQUIRED body sections from spec-for-actor are present
4. All REQUIRED body sections specific to signer are present
5. Signing Authority lists at least 1 authority domain
6. Type constraints are satisfied
7. Dependencies include v:spec:actor
8. The document is compliant with spec-for-actor

---

**Note:** Signer extends actor to represent humans with verified GitHub identity who can sign validation edges. The github_username requirement enables identity verification through commit attribution (git blame), creating an accountable chain of trust in the knowledge complex.
