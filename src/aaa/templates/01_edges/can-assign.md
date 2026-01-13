---
type: template/edge/can-assign
extends: edge
id: template:edge:can-assign
name: Can Assign Edge Template
description: Connects an actor to a role they can assign to others (ARBAC97 administrative authority)
instantiable: true
tags:
  - template
  - edge
  - can-assign
  - rbac
  - arbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Can Assign Edge Template

**Connects an actor to a role they can assign to others (ARBAC97 administrative authority).**

Can-assign edges represent administrative role assignment authority in the ARBAC97 model. They define which actors have the authority to assign specific roles to other actors.

## NIST/ARBAC97 Terminology

This edge type implements **`can_assign`** from ARBAC97 (Administrative RBAC) - the relation that specifies which administrative roles can assign users to which regular roles.

In formal ARBAC97 notation: `can_assign(admin_role, target_role)` means actors holding `admin_role` can assign other actors to `target_role`.

## Type Hierarchy

```
edge (abstract)
└── can-assign (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus can-assign-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/can-assign` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:can-assign:<actor>:<role>` |
| `source` | string | Actor ID (format: `v:signer:<username>` or `v:actor:<name>`) |
| `target` | string | Role ID (format: `v:role:<name>`) |
| `source_type` | string | Must be `vertex/actor` or `vertex/signer` |
| `target_type` | string | Must be `vertex/role` |
| `orientation` | string | Must be `directed` |
| `tags` | array | Must include `[edge, can-assign]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |
| `derived_from` | string | Role that conveys this authority |

## Tag Requirements

```yaml
tags:
  - edge
  - can-assign
```

## Required Body Sections

- **Assignment Authority** - Actor, target role, and authority source
- **Authority Chain** - How this can-assign authority was derived
- **Scope and Limitations** - What the assignment authority covers

## Role in Role-Assignment Face

Can-assign edges form one side of role-assignment faces:

```
     actor
      /  \
     /    \
has-role  can-assign
    /        \
   /          \
admin-role -- target-role
       conveys
```

**Key property:** The actor must hold a role that conveys authority over the target role.

## Example Instance

```yaml
---
type: edge/can-assign
extends: edge
id: e:can-assign:mzargham:reviewer
name: Can Assign - mzargham can assign reviewer role
source: v:signer:mzargham
target: v:role:reviewer
source_type: vertex/signer
target_type: vertex/role
orientation: directed
derived_from: v:role:admin
tags:
  - edge
  - can-assign
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Can Assign - mzargham can assign reviewer role

This edge establishes that mzargham has authority to assign the reviewer role to other actors.

## Assignment Authority

**Actor:** [[signer-mzargham|v:signer:mzargham]]
**Target Role:** [[role-reviewer|v:role:reviewer]]
**Derived From:** admin role (via conveys edge)

## Authority Chain

1. mzargham has-role admin
2. admin role conveys reviewer (assignment authority)
3. Therefore, mzargham can-assign reviewer

This chain forms a role-assignment face that proves the authority is properly derived.

## Scope and Limitations

**Scope:** mzargham can assign the reviewer role to any actor in this knowledge complex.

**Limitations:**
- Cannot assign the admin role (would require higher authority)
- Assignment must be documented via assignment-signature face
```

## Validation Rules

1. **Type Format:** `type` must be `edge/can-assign`
2. **Source Type:** Source must be an actor (`vertex/actor`) or signer (`vertex/signer`)
3. **Target Type:** Target must be a role (`vertex/role`)
4. **Orientation:** Must be `directed`
5. **Tag Chain:** Tags must include `[edge, can-assign]`
6. **Body Content:** Must include assignment authority, authority chain, and scope
7. **Face Requirement:** Should be part of a role-assignment face proving authority derivation
