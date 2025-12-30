---
type: vertex/spec
extends: doc
id: v:spec:qualifies
name: Specification for Qualifies Edge Documents
description: Defines what makes a valid qualifies edge - credential linking signer to guidance they can validate against
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies: []
---

# Specification for Qualifies Edge Documents

**This specification defines the structure and requirements for qualifies edge documents in the knowledge complex.**

## Purpose

Qualifies edges represent **credential relationships** between signers and guidance documents. They assert that a signer possesses the expertise, authority, or credentials necessary to validate documents against a specific guidance. This edge is a prerequisite for signing - a signer cannot sign a validation without holding a valid qualifies edge to the relevant guidance.

## Semantic Meaning

A qualifies edge from signer S to guidance G means:
- "S is qualified to validate documents against G"
- "S has the credentials/expertise to judge quality per G's criteria"
- "S's signature on validations against G carries authority"

## Required Frontmatter Fields

All qualifies edge documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `edge/qualifies` |
| `extends` | string | REQUIRED | Must be `edge` |
| `id` | string | REQUIRED | Unique identifier (format: `e:qualifies:<signer>:<guidance>`) |
| `name` | string | REQUIRED | Human-readable edge name |
| `tags` | array[string] | REQUIRED | Must include `[edge, qualifies]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Endpoint Fields

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `source` | string | REQUIRED | Signer vertex ID (format: `v:signer:<username>`) |
| `target` | string | REQUIRED | Guidance vertex ID (format: `v:guidance:<name>`) |
| `source_type` | string | REQUIRED | Must be `vertex/signer` |
| `target_type` | string | REQUIRED | Must be `vertex/guidance` |
| `orientation` | string | REQUIRED | Must be `directed` |

### Credential Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `credential_type` | string | REQUIRED | Type of qualification: `expertise`, `role`, `delegation`, `certification` |
| `granted_by` | string | REQUIRED | Who/what grants this qualification |
| `granted_date` | datetime | REQUIRED | When qualification was established |
| `expiry_date` | datetime | OPTIONAL | When qualification expires (if applicable) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

## Required Body Sections

### 1. Qualification Description

**Format:**
```markdown
## Qualification Description

**Signer:** [Link to signer vertex]
**Guidance:** [Link to guidance vertex]
**Credential Type:** [expertise | role | delegation | certification]

[Description of why this signer is qualified to validate against this guidance]
```

### 2. Credential Evidence

**Format:**
```markdown
## Credential Evidence

[Evidence supporting the qualification claim]

- **[Evidence type 1]**: [Description]
- **[Evidence type 2]**: [Description]
```

**Requirements:**
- MUST provide at least one form of evidence
- Evidence SHOULD be verifiable
- For role-based credentials, reference the authority granting the role

### 3. Scope and Limitations

**Format:**
```markdown
## Scope and Limitations

**Scope:** [What this qualification covers]
**Limitations:** [Any restrictions on the qualification]
```

## Optional Body Sections

### Delegation Chain

If credential_type is `delegation`, document the chain:

```markdown
## Delegation Chain

1. [Original authority]
2. [Intermediate delegator] (if any)
3. [This signer]
```

### Renewal History

```markdown
## Renewal History

- **[Date]**: [Renewal event]
```

## Type Constraints

1. **Type Field:** MUST be exactly `edge/qualifies`
2. **Extends Field:** MUST be exactly `edge`
3. **ID Format:** MUST match pattern `e:qualifies:[signer-username]:[guidance-name]`
4. **Source Type:** Source MUST be `vertex/signer`
5. **Target Type:** Target MUST be `vertex/guidance`
6. **Orientation:** MUST be `directed`
7. **Tag Inheritance:** Tags MUST include: `[edge, qualifies]`

## Credential Types

### expertise

Qualification based on demonstrated knowledge or skill:
- Evidence: publications, experience, education
- Granted by: self-declared with evidence, or recognized by authority
- Typical expiry: none (expertise persists)

### role

Qualification based on organizational position:
- Evidence: employment, appointment, charter
- Granted by: organization or authority
- Typical expiry: when role ends

### delegation

Qualification delegated from another qualified party:
- Evidence: delegation document or authorization
- Granted by: the delegating party
- Typical expiry: may be time-limited

### certification

Qualification based on formal certification:
- Evidence: certificate, credential record
- Granted by: certifying body
- Typical expiry: certification period

## Role in Signature Pattern

Qualifies edges form one side of the signature triangle:

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

The qualifies edge:
- Connects signer to guidance (credential relationship)
- Is a **prerequisite** for the signs edge
- Must be **valid at signing time** (checked during signature)

## Verification vs. Validation

- **Verification** (against this spec): Check all required fields present, types match, evidence exists
- **Validation** (against guidance-for-qualifies): Assess whether evidence is sufficient, scope appropriate

## Schema Summary

```yaml
# Required frontmatter
type: edge/qualifies
extends: edge
id: e:qualifies:<signer>:<guidance>
name: <string>
source: v:signer:<username>
target: v:guidance:<name>
source_type: vertex/signer
target_type: vertex/guidance
orientation: directed
credential_type: expertise | role | delegation | certification
granted_by: <string>
granted_date: <ISO8601>
tags: [edge, qualifies]
version: <semver>
created: <ISO8601>
modified: <ISO8601>

# Optional frontmatter
expiry_date: <ISO8601>
description: <string>

# Required body sections (markdown)
## Qualification Description
## Credential Evidence (≥1 evidence item)
## Scope and Limitations

# Optional body sections
## Delegation Chain
## Renewal History
```

## Compliance

A document claiming `type: edge/qualifies` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. Source is a valid signer vertex ID
3. Target is a valid guidance vertex ID
4. credential_type is one of the valid types
5. granted_by and granted_date are specified
6. All REQUIRED body sections are present
7. At least one evidence item is provided
8. Type constraints are satisfied

---

**Note:** Qualifies edges establish the credential basis for signing authority. They are prerequisites for signature faces - a signer cannot sign a validation unless they hold a valid (non-expired) qualifies edge to the relevant guidance at signing time.