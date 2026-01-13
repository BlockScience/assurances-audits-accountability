---
type: template/face/assignment-signature
extends: face
id: template:face:assignment-signature
name: Assignment Signature Face Template
description: ARBAC97 assignment attestation - records human sign-off on role assignment
instantiable: true
edges:
  - signs_assignment_edge
  - has_role_edge
  - can_assign_edge
orientation: oriented
tags:
  - template
  - face
  - assignment-signature
  - arbac
  - rbac
version: 1.0.0
created: 2026-01-12T00:00:00Z
modified: 2026-01-12T00:00:00Z
---

# Assignment Signature Face Template

**ARBAC97 assignment attestation triangle.**

Assignment signature faces record human sign-off on a role assignment action. They prove that an admin with can-assign authority actually assigned a role to a target actor.

## Type Hierarchy

```
face (abstract)
└── assignment-signature (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `face`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `face/assignment-signature` |
| `extends` | string | Must be `face` |
| `id` | string | Format: `f:assignment-signature:<admin>:<target>:<role>` |
| `vertices` | array | Exactly 3: [admin-signer, target-actor, target-role] |
| `admin` | string | Admin signer vertex ID (who assigns) |
| `target` | string | Target actor vertex ID (who receives role) |
| `role` | string | Target role vertex ID (role being assigned) |
| `edges` | array | Exactly 3: [signs-assignment, has-role, can-assign] |
| `orientation` | string | Must be `oriented` |
| `signs_assignment_edge` | string | Signs-assignment edge ID |
| `has_role_edge` | string | Has-role edge ID (result of assignment) |
| `can_assign_edge` | string | Can-assign edge ID (shared with role-assignment face) |
| `assignment_date` | datetime | When assignment was made |
| `commit_hash` | string | Git commit recording assignment |
| `tags` | array | Must include `[face, assignment-signature]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |
| `role_assignment_face` | string | ID of corresponding role-assignment face |

## Tag Requirements

```yaml
tags:
  - face
  - assignment-signature
```

## Required Body Sections

- **Face Description** - Type, assignment date, commit, summary
- **Vertices** - Admin, target actor, role with types
- **Edges (Boundary)** - Signs-assignment, has-role, can-assign
- **Triangle Coherence** - Assignment chain verification
- **Accountability Statement** - Formal attestation with admin identity

## ARBAC97 Assignment Pattern

```
        target-role
           /\
          /  \
has-role /    \ can-assign
(result)/      \ (authority)
       /        \
      /          \
  target ------- admin
      signs-assignment
       (attestation)

signs-assignment: admin attests to assigning role to target
has-role: target now has the role (result)
can-assign: admin has authority to assign this role (from role-assignment face)
```

## Example Instance

```yaml
---
type: face/assignment-signature
extends: face
id: f:assignment-signature:mzargham:alice:reviewer
name: Assignment Signature - mzargham assigns Reviewer to alice
description: Records mzargham's assignment of Reviewer role to alice
vertices:
  - v:signer:mzargham
  - v:actor:alice
  - v:role:reviewer
admin: v:signer:mzargham
target: v:actor:alice
role: v:role:reviewer
edges:
  - e:signs-assignment:mzargham:alice
  - e:has-role:alice:reviewer
  - e:can-assign:mzargham:reviewer
orientation: oriented
signs_assignment_edge: e:signs-assignment:mzargham:alice
has_role_edge: e:has-role:alice:reviewer
can_assign_edge: e:can-assign:mzargham:reviewer
assignment_date: 2026-01-12T12:00:00Z
commit_hash: abc123def456
role_assignment_face: f:role-assignment:mzargham:admin:reviewer
tags:
  - face
  - assignment-signature
version: 1.0.0
created: 2026-01-12T12:00:00Z
modified: 2026-01-12T12:00:00Z
---

# Assignment Signature - mzargham assigns Reviewer to alice

This assignment signature face records mzargham's assignment of the Reviewer role to alice.

## Face Description

**Type:** Assignment Signature Triangle (ARBAC97)
**Assignment Date:** 2026-01-12T12:00:00Z
**Commit:** abc123def456

This face records that mzargham, with can-assign authority for Reviewer role, assigned that role to alice. The has-role edge is the result of this assignment action.

## Vertices

1. **[mzargham](../00_vertices/signer-mzargham.md)** (`v:signer:mzargham`)
   - The admin performing the assignment
   - Type: vertex/signer
   - Role in face: Assignment authority

2. **[alice](../00_vertices/actor-alice.md)** (`v:actor:alice`)
   - The actor receiving the role
   - Type: vertex/actor
   - Role in face: Assignment recipient

3. **[Reviewer](../00_vertices/role-reviewer.md)** (`v:role:reviewer`)
   - The role being assigned
   - Type: vertex/role
   - Role in face: Assignment target

## Edges (Boundary)

1. **[signs-assignment-mzargham:alice](../01_edges/signs-assignment-mzargham-alice.md)** (`e:signs-assignment:mzargham:alice`)
   - Source: mzargham → Target: alice
   - Type: edge/signs-assignment
   - Records the assignment action
   - Commit: abc123def456

2. **[has-role-alice:reviewer](../01_edges/has-role-alice-reviewer.md)** (`e:has-role:alice:reviewer`)
   - Source: alice → Target: Reviewer
   - Type: edge/has-role
   - Result of the assignment
   - alice now has Reviewer role

3. **[can-assign-mzargham:reviewer](../01_edges/can-assign-mzargham-reviewer.md)** (`e:can-assign:mzargham:reviewer`)
   - Source: mzargham → Target: Reviewer
   - Type: edge/can-assign
   - **SHARED** with role-assignment face
   - Proves admin has assignment authority

## Triangle Coherence

**Topological Properties:**
- **Closed Boundary:** All three edges form a cycle
- **Complete:** All vertices connected by edges
- **Oriented:** Edges follow assignment flow

**Assignment Chain Verification:**
- ✓ Admin has can-assign authority (can-assign edge exists)
- ✓ Assignment action recorded (signs-assignment edge exists)
- ✓ Role granted to target (has-role edge exists)
- ✓ Shared boundary with role-assignment face

## Accountability Statement

This assignment signature records that mzargham assigned the Reviewer role to alice on 2026-01-12.

The admin's can-assign authority was verified through the shared can-assign edge with role-assignment face f:role-assignment:mzargham:admin:reviewer.

This assignment is recorded in commit abc123def456.

**Admin:** mzargham
**Target:** alice
**Role Assigned:** Reviewer
**Date:** 2026-01-12T12:00:00Z
```

## Validation Rules

1. **Type Format:** `type` must be `face/assignment-signature`
2. **Vertex Count:** Must have exactly 3 vertices
3. **Vertex Types:** Must include one signer (admin), one actor (target), one role
4. **Edge Count:** Must have exactly 3 boundary edges
5. **Edge Types:** Must include signs-assignment, has-role, can-assign edges
6. **Triangle Formation:** Edges must form closed boundary cycle
7. **Assignment Metadata:** `assignment_date` and `commit_hash` required
8. **Tag Chain:** Tags must include `[face, assignment-signature]`
9. **Shared Edge:** `can_assign_edge` must be shared with role-assignment face
10. **Body Content:** Must include all required sections with accountability statement

## Relationship to Role Assignment Face

Assignment signature faces and role assignment faces share the `can-assign` edge:
- Role assignment face: Proves admin has authority to assign role
- Assignment signature face: Records actual assignment with accountability

```
Role Assignment Face: (admin, admin-role, target-role)
Assignment-Signature Face: (admin, target-actor, target-role)
Shared Edge: can-assign (admin → target-role)
```

This shared edge creates face adjacency that enforces: you cannot sign a role assignment (create assignment-signature face) without first having role assignment authority (role-assignment face must exist sharing the can-assign edge).

## Assignment Chain

```
role-assignment → assignment-signature → has-role (result)
       ↓                   ↓                   ↓
  (defines authority)  (proves sign-off)  (actor has role)
```

This parallels the document assurance chain:
```
authorization → signature → assurance
       ↓            ↓           ↓
  (defines auth)  (sign-off)  (assured doc)
```
