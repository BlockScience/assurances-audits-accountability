---
type: template/face/authorization
extends: face
id: template:face:authorization
name: Authorization Face Template
description: NIST RBAC permission derivation - proves actor has permission through role
instantiable: true
edges:
  - has_role_edge
  - conveys_edge
  - (derived permission edge)
orientation: oriented
tags:
  - template
  - face
  - authorization
  - rbac
version: 1.0.0
created: 2026-01-12T00:00:00Z
modified: 2026-01-12T00:00:00Z
---

# Authorization Face Template

**NIST RBAC permission derivation triangle.**

Authorization faces prove that an actor has a specific permission through their role assignment. This implements the core NIST RBAC pattern: User Assignment (UA) + Permission Assignment (PA) = derived permission.

## Type Hierarchy

```
face (abstract)
└── authorization (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `face`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `face/authorization` |
| `extends` | string | Must be `face` |
| `id` | string | Format: `f:authorization:<actor>:<role>:<permission>` |
| `vertices` | array | Exactly 3: [actor, role, permission] |
| `actor` | string | Actor or signer vertex ID |
| `role` | string | Role vertex ID |
| `permission` | string | Permission or guidance vertex ID |
| `edges` | array | Exactly 3: [has-role, conveys, qualifies] |
| `orientation` | string | Must be `oriented` |
| `has_role_edge` | string | Has-role edge ID (UA) |
| `conveys_edge` | string | Conveys edge ID (PA) |
| `qualifies_edge` | string | Qualifies edge ID (derived permission) |
| `tags` | array | Must include `[face, authorization]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |
| `granted_date` | datetime | When authorization was established |

## Tag Requirements

```yaml
tags:
  - face
  - authorization
```

## Required Body Sections

- **Face Description** - Type, purpose, NIST RBAC context
- **Vertices** - Actor, role, permission with types
- **Edges (Boundary)** - Has-role (UA), conveys (PA), qualifies (derived)
- **Triangle Coherence** - RBAC chain verification
- **Permission Derivation** - How permission is derived through role

## NIST RBAC Pattern

```
         permission/guidance
              /\
             /  \
    conveys /    \ qualifies
      (PA) /      \ (derived)
          /        \
         /          \
      role -------- actor
           has-role
             (UA)

UA (User Assignment): actor has-role role
PA (Permission Assignment): role conveys permission
Derived: actor qualifies-for permission (through role)
```

## Example Instance

```yaml
---
type: face/authorization
extends: face
id: f:authorization:mzargham:reviewer:validate-guidance-spec
name: Authorization - mzargham as Reviewer for guidance-for-spec
description: Proves mzargham can validate against guidance-for-spec through Reviewer role
vertices:
  - v:signer:mzargham
  - v:role:reviewer
  - v:guidance:spec
actor: v:signer:mzargham
role: v:role:reviewer
permission: v:guidance:spec
edges:
  - e:has-role:mzargham:reviewer
  - e:conveys:reviewer:guidance-spec
  - e:qualifies:mzargham:spec
orientation: oriented
has_role_edge: e:has-role:mzargham:reviewer
conveys_edge: e:conveys:reviewer:guidance-spec
qualifies_edge: e:qualifies:mzargham:spec
tags:
  - face
  - authorization
version: 1.0.0
created: 2026-01-12T12:00:00Z
modified: 2026-01-12T12:00:00Z
---

# Authorization - mzargham as Reviewer for guidance-for-spec

This authorization face proves that mzargham has permission to validate documents against guidance-for-spec through their Reviewer role assignment.

## Face Description

**Type:** Authorization Triangle (NIST RBAC)
**Purpose:** Permission derivation through role assignment

This face implements the NIST RBAC pattern where:
- User Assignment (UA): mzargham has-role Reviewer
- Permission Assignment (PA): Reviewer conveys validate-permission for guidance-for-spec
- Derived: mzargham qualifies-for guidance-for-spec

## Vertices

1. **[mzargham](../00_vertices/signer-mzargham.md)** (`v:signer:mzargham`)
   - The actor seeking permission
   - Type: vertex/signer
   - Role in face: Permission holder

2. **[Reviewer](../00_vertices/role-reviewer.md)** (`v:role:reviewer`)
   - The role granting permission
   - Type: vertex/role
   - Role in face: Permission mediator

3. **[guidance-for-spec](../00_vertices/guidance-for-spec.md)** (`v:guidance:spec`)
   - The permission target (validation authority)
   - Type: vertex/guidance
   - Role in face: Permission scope

## Edges (Boundary)

1. **[has-role-mzargham:reviewer](../01_edges/has-role-mzargham-reviewer.md)** (`e:has-role:mzargham:reviewer`)
   - Source: mzargham → Target: Reviewer
   - Type: edge/has-role
   - NIST: User Assignment (UA)
   - Grants role membership

2. **[conveys-reviewer:guidance-spec](../01_edges/conveys-reviewer-guidance-spec.md)** (`e:conveys:reviewer:guidance-spec`)
   - Source: Reviewer → Target: guidance-for-spec
   - Type: edge/conveys
   - NIST: Permission Assignment (PA)
   - Role grants validation authority

3. **[qualifies-mzargham:spec](../01_edges/qualifies-mzargham-spec.md)** (`e:qualifies:mzargham:spec`)
   - Source: mzargham → Target: guidance-for-spec
   - Type: edge/qualifies
   - NIST: Derived permission
   - Actor has permission through role

## Triangle Coherence

**Topological Properties:**
- **Closed Boundary:** All three edges form a cycle
- **Complete:** All vertices connected by edges
- **Oriented:** Edges follow RBAC permission flow

**RBAC Chain Verification:**
- ✓ Actor has role assignment (UA exists)
- ✓ Role conveys permission (PA exists)
- ✓ Derived permission recorded (qualifies edge exists)
- ✓ Permission chain is complete and valid

## Permission Derivation

**NIST RBAC Logic:**
```
has-role(mzargham, Reviewer) ∧ conveys(Reviewer, guidance-for-spec)
  ⟹ qualifies(mzargham, guidance-for-spec)
```

The qualifies edge is the derived permission that results from the RBAC chain. This authorization face proves the derivation is valid.

## Accountability Statement

This authorization establishes that mzargham has permission to validate documents against guidance-for-spec through their Reviewer role.

**Actor:** mzargham
**Role:** Reviewer
**Permission:** Validate against guidance-for-spec
```

## Validation Rules

1. **Type Format:** `type` must be `face/authorization`
2. **Vertex Count:** Must have exactly 3 vertices
3. **Vertex Types:** Must include one actor/signer, one role, one permission/guidance
4. **Edge Count:** Must have exactly 3 boundary edges
5. **Edge Types:** Must include has-role, conveys, qualifies edges
6. **Triangle Formation:** Edges must form closed boundary cycle
7. **RBAC Chain:** has-role source must be actor, conveys source must be role
8. **Tag Chain:** Tags must include `[face, authorization]`
9. **Body Content:** Must include all required sections

## Relationship to Signature Face

Authorization faces and signature faces share the `qualifies` edge:
- Authorization face: Proves actor has permission (via role)
- Signature face: Uses that permission to sign a validation

```
Authorization Face: (actor, role, guidance)
Signature Face: (doc, guidance, signer)
Shared Edge: qualifies (signer → guidance)
```

This shared edge creates face adjacency that enforces the rule: you cannot sign (create signature face) without first having authorization (authorization face must exist).
