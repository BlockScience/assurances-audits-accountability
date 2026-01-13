---
type: template/face/role-assignment
extends: face
id: template:face:role-assignment
name: Role Assignment Face Template
description: ARBAC97 role assignment authority - proves admin can assign a specific role
instantiable: true
edges:
  - has_role_edge
  - conveys_edge
  - can_assign_edge
orientation: oriented
tags:
  - template
  - face
  - role-assignment
  - arbac
  - rbac
version: 1.0.0
created: 2026-01-12T00:00:00Z
modified: 2026-01-12T00:00:00Z
---

# Role Assignment Face Template

**ARBAC97 role assignment authority triangle.**

Role assignment faces prove that an admin actor has authority to assign a specific role to other actors. This implements the ARBAC97 `can_assign` relation through role membership.

## Type Hierarchy

```
face (abstract)
└── role-assignment (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `face`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `face/role-assignment` |
| `extends` | string | Must be `face` |
| `id` | string | Format: `f:role-assignment:<admin>:<admin-role>:<target-role>` |
| `vertices` | array | Exactly 3: [admin-actor, admin-role, target-role] |
| `admin` | string | Admin actor or signer vertex ID |
| `admin_role` | string | Admin role vertex ID |
| `target_role` | string | Target role vertex ID (role that can be assigned) |
| `edges` | array | Exactly 3: [has-role, conveys, can-assign] |
| `orientation` | string | Must be `oriented` |
| `has_role_edge` | string | Has-role edge ID (admin has admin-role) |
| `conveys_edge` | string | Conveys edge ID (admin-role conveys assignment authority) |
| `can_assign_edge` | string | Can-assign edge ID (admin can assign target-role) |
| `tags` | array | Must include `[face, role-assignment]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |

## Tag Requirements

```yaml
tags:
  - face
  - role-assignment
```

## Required Body Sections

- **Face Description** - Type, purpose, ARBAC97 context
- **Vertices** - Admin, admin-role, target-role with types
- **Edges (Boundary)** - Has-role, conveys, can-assign
- **Triangle Coherence** - ARBAC chain verification
- **Assignment Authority** - What assignments this enables

## ARBAC97 Pattern

```
       target-role
           /\
          /  \
 conveys /    \ can-assign
   (PA) /      \ (ARBAC97)
       /        \
      /          \
 admin-role ---- admin
          has-role
            (UA)

UA: admin has-role admin-role
PA: admin-role conveys assignment-authority for target-role
ARBAC97: admin can-assign target-role (to other actors)
```

The admin-role sits **opposite** the can-assign edge, following the pattern where the role opposite an edge type conveys authority to create that edge type.

## Example Instance

```yaml
---
type: face/role-assignment
extends: face
id: f:role-assignment:mzargham:admin:reviewer
name: Role Assignment - mzargham as Admin can assign Reviewer
description: Proves mzargham can assign Reviewer role through Admin role
vertices:
  - v:signer:mzargham
  - v:role:admin
  - v:role:reviewer
admin: v:signer:mzargham
admin_role: v:role:admin
target_role: v:role:reviewer
edges:
  - e:has-role:mzargham:admin
  - e:conveys:admin:reviewer
  - e:can-assign:mzargham:reviewer
orientation: oriented
has_role_edge: e:has-role:mzargham:admin
conveys_edge: e:conveys:admin:reviewer
can_assign_edge: e:can-assign:mzargham:reviewer
tags:
  - face
  - role-assignment
version: 1.0.0
created: 2026-01-12T12:00:00Z
modified: 2026-01-12T12:00:00Z
---

# Role Assignment - mzargham as Admin can assign Reviewer

This role assignment face proves that mzargham has authority to assign the Reviewer role to other actors through their Admin role.

## Face Description

**Type:** Role Assignment Triangle (ARBAC97)
**Purpose:** Administrative role assignment authority

This face implements the ARBAC97 pattern where:
- User Assignment (UA): mzargham has-role Admin
- Permission Assignment (PA): Admin conveys assignment-authority for Reviewer
- ARBAC97 can_assign: mzargham can-assign Reviewer

## Vertices

1. **[mzargham](../00_vertices/signer-mzargham.md)** (`v:signer:mzargham`)
   - The admin actor with assignment authority
   - Type: vertex/signer
   - Role in face: Assignment authority holder

2. **[Admin](../00_vertices/role-admin.md)** (`v:role:admin`)
   - The administrative role granting assignment authority
   - Type: vertex/role
   - Role in face: Authority source

3. **[Reviewer](../00_vertices/role-reviewer.md)** (`v:role:reviewer`)
   - The role that can be assigned
   - Type: vertex/role
   - Role in face: Assignment target

## Edges (Boundary)

1. **[has-role-mzargham:admin](../01_edges/has-role-mzargham-admin.md)** (`e:has-role:mzargham:admin`)
   - Source: mzargham → Target: Admin
   - Type: edge/has-role
   - NIST: User Assignment (UA)
   - Grants admin role membership

2. **[conveys-admin:reviewer](../01_edges/conveys-admin-reviewer.md)** (`e:conveys:admin:reviewer`)
   - Source: Admin → Target: Reviewer
   - Type: edge/conveys
   - NIST: Permission Assignment (PA)
   - Admin role grants authority to assign Reviewer

3. **[can-assign-mzargham:reviewer](../01_edges/can-assign-mzargham-reviewer.md)** (`e:can-assign:mzargham:reviewer`)
   - Source: mzargham → Target: Reviewer
   - Type: edge/can-assign
   - ARBAC97: can_assign relation
   - Actor can assign this role to others

## Triangle Coherence

**Topological Properties:**
- **Closed Boundary:** All three edges form a cycle
- **Complete:** All vertices connected by edges
- **Oriented:** Edges follow ARBAC permission flow

**ARBAC Chain Verification:**
- ✓ Admin has admin-role assignment (UA exists)
- ✓ Admin-role conveys assignment authority (PA exists)
- ✓ Can-assign relation recorded (can-assign edge exists)
- ✓ Assignment authority chain is complete

## Assignment Authority

**ARBAC97 Logic:**
```
has-role(mzargham, Admin) ∧ conveys(Admin, Reviewer)
  ⟹ can-assign(mzargham, Reviewer)
```

This role assignment face authorizes mzargham to:
- Assign the Reviewer role to other actors
- Create has-role edges: `e:has-role:<actor>:reviewer`

**Scope:** mzargham can assign Reviewer to any actor, subject to other policy constraints.

## Accountability Statement

This role assignment face establishes that mzargham has administrative authority to assign the Reviewer role through their Admin role membership.

**Admin:** mzargham
**Admin Role:** Admin
**Assignable Role:** Reviewer
```

## Validation Rules

1. **Type Format:** `type` must be `face/role-assignment`
2. **Vertex Count:** Must have exactly 3 vertices
3. **Vertex Types:** Must include one actor/signer, two roles (admin-role, target-role)
4. **Edge Count:** Must have exactly 3 boundary edges
5. **Edge Types:** Must include has-role, conveys, can-assign edges
6. **Triangle Formation:** Edges must form closed boundary cycle
7. **ARBAC Chain:** has-role connects admin to admin-role, conveys connects admin-role to target-role
8. **Tag Chain:** Tags must include `[face, role-assignment]`
9. **Body Content:** Must include all required sections

## Relationship to Assignment-Signature Face

Role assignment faces and assignment-signature faces share the `can-assign` edge:
- Role assignment face: Proves admin has authority to assign role
- Assignment-signature face: Records actual assignment with accountability

```
Role Assignment Face: (admin, admin-role, target-role)
Assignment-Signature Face: (admin, target-actor, target-role)
Shared Edge: can-assign (admin → target-role)
```

This shared edge creates face adjacency that enforces: you cannot sign a role assignment without first having role assignment authority.
