---
type: template/vertex/staff
extends: individual
id: template:vertex:staff
name: Staff Type Template
description: Employees or team members in organizational context
instantiable: true
tags:
  - template
  - vertex
  - actor
  - individual
  - staff
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Staff Type Template

**Employees or team members in organizational context.**

Staff are individuals who are members of the organization's workforce.

## Type Hierarchy

```
vertex (abstract)
└── actor (concrete)
    └── individual (concrete)
        └── staff (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `individual`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all individual/actor/vertex fields:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/staff` |
| `extends` | string | Must be `individual` |
| `tags` | array | Must include `[vertex, actor, individual, staff]` |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - vertex      # base type
  - actor       # grandparent type
  - individual  # parent type
  - staff       # concrete type
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `employee_id` | string | Employee identifier |
| `department` | string | Department assignment |
| `start_date` | date | Employment start date |
| `status` | string | active, on_leave, terminated |

## Body Content

Staff bodies should describe:
- Employee information
- Current assignments
- Qualifications and certifications
- Team memberships and roles

## Role in Role Assignment Pattern

Staff participate in the most specific form of the membership pattern:

```
role_assignment face (most specific):
  staff → team (member edge)
  staff → role (qualified edge)
  team → role (includes edge)
```

This is the organizational coordination pattern where:
- Staff members are assigned to teams
- Staff have specific role qualifications
- Teams require those roles to be filled

## Example Instance

```yaml
---
type: vertex/staff
extends: individual
id: v:staff:alice
name: Alice Johnson
tags:
  - vertex
  - actor
  - individual
  - staff
employee_id: EMP-001
department: Engineering
status: active
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Alice Johnson

Software engineer on the frontend team.

## Current Assignments

- Team: Frontend
- Role: Lead Developer

## Qualifications

- Senior Engineer certification
- 5 years React experience
- Team leadership training completed
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/staff`
2. **Tag Chain:** Tags must include `[vertex, actor, individual, staff]`
3. **Extends:** Must extend `individual`
4. **Role Assignment:** Appropriate source for member and qualified edges in role_assignment faces
5. **Organization Context:** Typically exists within an organization chart
