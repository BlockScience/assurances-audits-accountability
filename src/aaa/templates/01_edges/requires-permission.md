---
type: template/edge/requires-permission
extends: edge
id: template:edge:requires-permission
name: Requires Permission Edge Template
description: Connects an action to a permission required to perform it (NIST RBAC permission requirement)
instantiable: true
tags:
  - template
  - edge
  - requires-permission
  - rbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Requires Permission Edge Template

**Connects an action to a permission required to perform it.**

Requires-permission edges define the access control requirements for actions in the system. They specify which permission an actor must have (through their role assignments) to perform a particular action.

## NIST RBAC Terminology

This edge type implements permission requirements in the NIST RBAC model - the link between operations/objects and the permissions that authorize them.

## Type Hierarchy

```
edge (abstract)
└── requires-permission (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus requires-permission-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/requires-permission` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:requires-permission:<action>:<permission>` |
| `source` | string | Action ID (format: `v:action:<name>`) |
| `target` | string | Permission ID (format: `v:permission:<name>`) |
| `source_type` | string | Must be `vertex/action` |
| `target_type` | string | Must be `vertex/permission` |
| `orientation` | string | Must be `directed` |
| `tags` | array | Must include `[edge, requires-permission]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |
| `enforcement` | string | How requirement is enforced: `strict`, `advisory` |

## Tag Requirements

```yaml
tags:
  - edge
  - requires-permission
```

## Required Body Sections

- **Permission Requirement** - Action, permission, and relationship description
- **Enforcement** - How and when this requirement is checked
- **Access Path** - How actors obtain the required permission

## Role in Access Control

Requires-permission edges complete the access control chain:

```
actor --has-role--> role --conveys--> permission
                                          ^
                                          |
                              requires-permission
                                          |
                                       action
```

An actor can perform an action if:
1. Actor has-role R
2. R conveys permission P
3. Action requires-permission P

## Example Instance

```yaml
---
type: edge/requires-permission
extends: edge
id: e:requires-permission:validate:validate-authority
name: Requires Permission - validate action requires validate authority
source: v:action:validate
target: v:permission:validate
source_type: vertex/action
target_type: vertex/permission
orientation: directed
enforcement: strict
tags:
  - edge
  - requires-permission
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Requires Permission - validate action requires validate authority

This edge establishes that the validate action requires the validate permission.

## Permission Requirement

**Action:** [[action-validate|v:action:validate]]
**Permission:** [[permission-validate|v:permission:validate]]

To perform document validation (creating validation edges and signing them), an actor must have the validate permission.

## Enforcement

**Level:** Strict - the system will reject validation attempts from actors lacking this permission.

**Check Points:**
- When creating a validation edge (source signer must have permission)
- When creating a signature face (signer must be qualified)

## Access Path

Actors obtain the validate permission through:
1. Holding the `admin` role (conveys all permissions)
2. Holding a role that specifically conveys `validate` permission
3. Being explicitly qualified for specific guidance documents
```

## Validation Rules

1. **Type Format:** `type` must be `edge/requires-permission`
2. **Source Type:** Source must be an action (`vertex/action`)
3. **Target Type:** Target must be a permission (`vertex/permission`)
4. **Orientation:** Must be `directed`
5. **Tag Chain:** Tags must include `[edge, requires-permission]`
6. **Body Content:** Must include permission requirement, enforcement, and access path
