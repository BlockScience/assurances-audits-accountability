---
type: template/edge/conveys
extends: edge
id: template:edge:conveys
name: Conveys Edge Template
description: Connects a role to a permission or role it grants (Permission Assignment in NIST RBAC)
instantiable: true
tags:
  - template
  - edge
  - conveys
  - rbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Conveys Edge Template

**Connects a role to a permission or role it grants (Permission Assignment in NIST RBAC).**

Conveys edges represent permission-role assignments in the RBAC model. They define what permissions or administrative authorities a role grants to actors who hold it.

## NIST RBAC Terminology

This edge type implements **Permission Assignment (PA)** from the NIST RBAC standard - the many-to-many mapping of permissions to roles. When targeting another role, it also supports ARBAC97 administrative delegation.

## Type Hierarchy

```
edge (abstract)
└── conveys (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus conveys-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/conveys` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:conveys:<role>:<permission>` or `e:conveys:<role>:<target-role>` |
| `source` | string | Role ID (format: `v:role:<name>`) |
| `target` | string | Permission ID (`v:permission:<name>`) or Role ID (`v:role:<name>`) |
| `source_type` | string | Must be `vertex/role` |
| `target_type` | string | Must be `vertex/permission` or `vertex/role` |
| `orientation` | string | Must be `directed` |
| `tags` | array | Must include `[edge, conveys]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |
| `conditions` | array | Conditions under which the permission applies |

## Tag Requirements

```yaml
tags:
  - edge
  - conveys
```

## Required Body Sections

- **Permission Assignment** - Role, permission/target, and relationship description
- **Granted Authority** - What actions this conveys edge enables
- **Scope and Conditions** - Any limitations or conditions

## Conveys Target Types

| Target Type | Meaning | Use Case |
|-------------|---------|----------|
| `vertex/permission` | Role grants permission | Standard RBAC permission assignment |
| `vertex/role` | Role can assign another role | ARBAC97 administrative delegation |

## Role in Authorization Pattern

Conveys edges form the permission side of authorization faces:

```
     actor
      /  \
     /    \
has-role  qualifies (derived from conveys)
    /        \
   /          \
 role ------- permission (or guidance)
       conveys
```

## Example Instance (Permission Assignment)

```yaml
---
type: edge/conveys
extends: edge
id: e:conveys:admin:validate
name: Conveys - admin role conveys validate permission
source: v:role:admin
target: v:permission:validate
source_type: vertex/role
target_type: vertex/permission
orientation: directed
tags:
  - edge
  - conveys
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Conveys - admin role conveys validate permission

This edge establishes that the admin role grants the validate permission.

## Permission Assignment

**Role:** [[role-admin|v:role:admin]]
**Permission:** [[permission-validate|v:permission:validate]]

The Administrator role conveys the authority to validate any document in the knowledge complex.

## Granted Authority

Actors holding the admin role can:
- Validate documents against any guidance
- Sign validation edges
- Approve assurance faces

## Scope and Conditions

**Scope:** This permission applies to all document types in the knowledge complex.

**Conditions:** None - admin role has unrestricted validation authority.
```

## Example Instance (Role Assignment Authority)

```yaml
---
type: edge/conveys
extends: edge
id: e:conveys:admin:reviewer
name: Conveys - admin role conveys reviewer assignment authority
source: v:role:admin
target: v:role:reviewer
source_type: vertex/role
target_type: vertex/role
orientation: directed
tags:
  - edge
  - conveys
  - arbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Conveys - admin role conveys reviewer assignment authority

This edge establishes that the admin role can assign the reviewer role to other actors.

## Permission Assignment

**Admin Role:** [[role-admin|v:role:admin]]
**Target Role:** [[role-reviewer|v:role:reviewer]]

The Administrator role conveys the authority to assign the Reviewer role to other actors.

## Granted Authority

Actors holding the admin role can:
- Assign the reviewer role to other actors
- Revoke the reviewer role from actors

## Scope and Conditions

**Scope:** This conveys edge only grants authority over the reviewer role, not other roles.

**Conditions:** Assignment must be documented via an assignment-signature face.
```

## Validation Rules

1. **Type Format:** `type` must be `edge/conveys`
2. **Source Type:** Source must be a role (`vertex/role`)
3. **Target Type:** Target must be a permission (`vertex/permission`) or role (`vertex/role`)
4. **Orientation:** Must be `directed`
5. **Tag Chain:** Tags must include `[edge, conveys]`
6. **Body Content:** Must include permission assignment, granted authority, and scope
