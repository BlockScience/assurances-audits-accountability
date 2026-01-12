---
type: template/edge/qualifies
extends: edge
id: template:edge:qualifies
name: Qualifies Edge Template
description: Connects a signer to guidance they are qualified to validate against (credential edge)
instantiable: true
tags:
  - template
  - edge
  - qualifies
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Qualifies Edge Template

**Connects a signer to the guidance document they are qualified to validate against.**

Qualifies edges represent credential relationships - they assert that a signer has the expertise, authority, or credentials to judge documents against a specific guidance's quality criteria. This edge is a prerequisite for signing.

## Type Hierarchy

```
edge (abstract)
└── qualifies (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus qualifies-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/qualifies` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:qualifies:<signer>:<guidance>` |
| `source` | string | Signer ID (format: `v:signer:<username>`) |
| `target` | string | Guidance ID (format: `v:guidance:<name>`) |
| `source_type` | string | Must be `vertex/signer` |
| `target_type` | string | Must be `vertex/guidance` |
| `orientation` | string | Must be `directed` |
| `credential_type` | string | `expertise`, `role`, `delegation`, or `certification` |
| `granted_by` | string | Who grants this qualification |
| `granted_date` | datetime | When qualification was established |
| `tags` | array | Must include `[edge, qualifies]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `expiry_date` | datetime | When qualification expires |
| `description` | string | Brief description |

## Tag Requirements

```yaml
tags:
  - edge
  - qualifies
```

## Required Body Sections

- **Qualification Description** - Signer, guidance, credential type, and rationale
- **Credential Evidence** - At least one evidence item supporting the qualification
- **Scope and Limitations** - What the qualification covers and any restrictions

## Role in Signature Pattern

Qualifies edges form the credential side of signature faces:

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

**Key property:** A qualifies edge must be valid (non-expired) at signing time. The signature face records this check.

## Credential Types

| Type | Basis | Granted By | Typical Expiry |
|------|-------|------------|----------------|
| `expertise` | Knowledge/skill | Self-declared or authority | None |
| `role` | Position/office | Organization | When role ends |
| `delegation` | Transferred authority | Delegating party | May be time-limited |
| `certification` | Formal credential | Certifying body | Certification period |

## Example Instance

```yaml
---
type: edge/qualifies
extends: edge
id: e:qualifies:mzargham:guidance-spec
name: Qualifies - mzargham qualified for guidance-for-spec
source: v:signer:mzargham
target: v:guidance:spec
source_type: vertex/signer
target_type: vertex/guidance
orientation: directed
credential_type: role
granted_by: BlockScience
granted_date: 2024-01-01T00:00:00Z
tags:
  - edge
  - qualifies
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Qualifies - mzargham qualified for guidance-for-spec

This qualifies edge establishes that mzargham is qualified to validate documents against guidance-for-spec.

## Qualification Description

**Signer:** [mzargham](../00_vertices/signer-mzargham.md)
**Guidance:** [guidance-for-spec](../00_vertices/guidance-for-spec.md)
**Credential Type:** role

Michael Zargham is qualified to validate specification documents against guidance-for-spec based on his role as Chief Engineer at BlockScience. This role carries authority over specification quality standards.

## Credential Evidence

- **Role**: Chief Engineer at BlockScience, responsible for establishing and maintaining specification standards
- **Experience**: 10+ years in systems engineering and formal specification development
- **Authorship**: Primary author of the specification framework used in this knowledge complex

## Scope and Limitations

**Scope:** This qualification covers validation of any document type against guidance-for-spec, including spec documents, guidance documents, and other typed documents.

**Limitations:** This qualification is scoped to the BlockScience knowledge complex. It does not extend to external specification frameworks or standards bodies.
```

## Validation Rules

1. **Type Format:** `type` must be `edge/qualifies`
2. **Source Type:** Source must be a signer (`vertex/signer`)
3. **Target Type:** Target must be guidance (`vertex/guidance`)
4. **Orientation:** Must be `directed`
5. **Credential Type:** Must be one of: `expertise`, `role`, `delegation`, `certification`
6. **Required Metadata:** `granted_by` and `granted_date` must be present
7. **Tag Chain:** Tags must include `[edge, qualifies]`
8. **Body Content:** Must include qualification description, evidence, and scope
9. **Signature Prerequisite:** This edge must be valid when referenced by a signature face
