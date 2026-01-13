---
type: template/edge/has-role
extends: edge
id: template:edge:has-role
name: Has Role Edge Template
description: Connects an actor to a role they hold (User Assignment in NIST RBAC)
instantiable: true
tags:
  - template
  - edge
  - has-role
  - rbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Has Role Edge Template

**Connects an actor to a role they hold (User Assignment in NIST RBAC).**

Has-role edges represent user-role assignments in the RBAC model. They assert that an actor (human signer or automated agent) holds a particular organizational role, which grants them the permissions conveyed by that role.

## NIST RBAC Terminology

This edge type implements **User Assignment (UA)** from the NIST RBAC standard - the many-to-many mapping of users to roles.

## Type Hierarchy

```
edge (abstract)
└── has-role (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus has-role-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/has-role` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:has-role:<actor>:<role>` |
| `source` | string | Actor ID (format: `v:signer:<username>` or `v:actor:<name>`) |
| `target` | string | Role ID (format: `v:role:<name>`) |
| `source_type` | string | Must be `vertex/actor` or `vertex/signer` |
| `target_type` | string | Must be `vertex/role` |
| `orientation` | string | Must be `directed` |
| `granted_by` | string | Who granted this role assignment |
| `granted_date` | datetime | When role was assigned |
| `tags` | array | Must include `[edge, has-role]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `expiry_date` | datetime | When role assignment expires |
| `description` | string | Brief description |

## Tag Requirements

```yaml
tags:
  - edge
  - has-role
```

## Required Body Sections

- **Role Assignment** - Actor, role, granted by, and date
- **Authority Chain** - How this assignment was authorized
- **Scope** - What permissions this role grants

## Role in Authorization Pattern

Has-role edges form one side of authorization faces:

```
     actor
      /  \
     /    \
has-role  can-assign (if admin role)
    /        \
   /          \
 role ------ target-role
       conveys
```

## Example Instance

```yaml
---
type: edge/has-role
extends: edge
id: e:has-role:mzargham:admin
name: Has Role - mzargham has admin role
source: v:signer:mzargham
target: v:role:admin
source_type: vertex/signer
target_type: vertex/role
orientation: directed
granted_by: system
granted_date: 2026-01-13T00:00:00Z
tags:
  - edge
  - has-role
  - bootstrap
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Has Role - mzargham has admin role

This edge establishes that mzargham holds the Administrator role.

## Role Assignment

**Actor:** [[signer-mzargham|v:signer:mzargham]]
**Role:** [[role-admin|v:role:admin]]
**Granted By:** System (bootstrap during repository initialization)
**Granted Date:** 2026-01-13T00:00:00Z

## Authority Chain

This role assignment was created during repository initialization. The founding user automatically receives the admin role, establishing the root of the RBAC authority chain.

## Scope

This role assignment grants mzargham full administrative authority over this knowledge complex, including:
- Assigning roles to other actors
- Establishing qualification credentials
- Managing framework structure
```

## Validation Rules

1. **Type Format:** `type` must be `edge/has-role`
2. **Source Type:** Source must be an actor (`vertex/actor`) or signer (`vertex/signer`)
3. **Target Type:** Target must be a role (`vertex/role`)
4. **Orientation:** Must be `directed`
5. **Required Metadata:** `granted_by` and `granted_date` must be present
6. **Tag Chain:** Tags must include `[edge, has-role]`
7. **Body Content:** Must include role assignment, authority chain, and scope
