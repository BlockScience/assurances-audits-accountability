---
type: template/edge/signs-assignment
extends: edge
id: template:edge:signs-assignment
name: Signs Assignment Edge Template
description: Connects a signer to an actor they are assigning a role to (attestation of role assignment)
instantiable: true
tags:
  - template
  - edge
  - signs-assignment
  - rbac
  - arbac
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Signs Assignment Edge Template

**Connects a signer to an actor they are assigning a role to (attestation of role assignment).**

Signs-assignment edges represent the human accountability for role assignments. They document that a qualified admin has signed off on granting a role to another actor, providing the audit trail required for RBAC governance.

## Purpose

This edge type is distinct from `signs` (which is for document validation). Signs-assignment specifically attests to role assignments, linking the admin performing the assignment to the actor receiving the role.

## Type Hierarchy

```
edge (abstract)
└── signs-assignment (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus signs-assignment-specific:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/signs-assignment` |
| `extends` | string | Must be `edge` |
| `id` | string | Format: `e:signs-assignment:<admin>:<target-actor>` |
| `source` | string | Admin signer ID (format: `v:signer:<username>`) |
| `target` | string | Target actor ID (format: `v:signer:<username>` or `v:actor:<name>`) |
| `source_type` | string | Must be `vertex/signer` |
| `target_type` | string | Must be `vertex/actor` or `vertex/signer` |
| `orientation` | string | Must be `directed` |
| `assignment_date` | datetime | When the assignment was made |
| `role_assigned` | string | The role being assigned (reference) |
| `tags` | array | Must include `[edge, signs-assignment]` |

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description |
| `commit_hash` | string | Git commit hash for verification |
| `justification` | string | Reason for the assignment |

## Tag Requirements

```yaml
tags:
  - edge
  - signs-assignment
```

## Required Body Sections

- **Assignment Attestation** - Admin, target actor, role, and date
- **Authority Verification** - Proof that admin has can-assign authority
- **Assignment Justification** - Why this role was assigned

## Role in Assignment-Signature Face

Signs-assignment edges form the accountability side of assignment-signature faces:

```
         admin-signer
           /      \
          /        \
signs-assignment  can-assign
        /            \
       /              \
 target-actor ------- target-role
              has-role
```

**Key property:** The admin-signer must have can-assign authority for the target-role.

## Example Instance

```yaml
---
type: edge/signs-assignment
extends: edge
id: e:signs-assignment:mzargham:alice
name: Signs Assignment - mzargham assigns role to alice
source: v:signer:mzargham
target: v:signer:alice
source_type: vertex/signer
target_type: vertex/signer
orientation: directed
assignment_date: 2026-01-13T12:00:00Z
role_assigned: v:role:reviewer
tags:
  - edge
  - signs-assignment
version: 1.0.0
created: 2026-01-13T12:00:00Z
modified: 2026-01-13T12:00:00Z
---

# Signs Assignment - mzargham assigns role to alice

This edge attests that mzargham has assigned the reviewer role to alice.

## Assignment Attestation

**Admin:** [[signer-mzargham|v:signer:mzargham]]
**Target Actor:** [[signer-alice|v:signer:alice]]
**Role Assigned:** [[role-reviewer|v:role:reviewer]]
**Assignment Date:** 2026-01-13T12:00:00Z

## Authority Verification

mzargham has authority to make this assignment:
1. mzargham has-role admin
2. admin role conveys reviewer (via conveys edge)
3. mzargham can-assign reviewer (derived authority)

This forms a complete role-assignment face proving the authority chain.

## Assignment Justification

alice has demonstrated competency in document review through:
- Participation in previous review cycles
- Completion of reviewer onboarding
- Recommendation from existing reviewers

This assignment enables alice to perform document validation within their qualified domains.
```

## Validation Rules

1. **Type Format:** `type` must be `edge/signs-assignment`
2. **Source Type:** Source must be a signer (`vertex/signer`)
3. **Target Type:** Target must be an actor (`vertex/actor`) or signer (`vertex/signer`)
4. **Orientation:** Must be `directed`
5. **Required Metadata:** `assignment_date` and `role_assigned` must be present
6. **Tag Chain:** Tags must include `[edge, signs-assignment]`
7. **Body Content:** Must include attestation, authority verification, and justification
8. **Face Requirement:** Should be part of an assignment-signature face
