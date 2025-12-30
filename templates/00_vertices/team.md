---
type: template/vertex/team
extends: group
id: template:vertex:team
name: Team Type Template
description: Formal organizational unit with defined roles
instantiable: true
tags:
  - template
  - vertex
  - actor
  - group
  - team
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Team Type Template

**Formal organizational unit with defined roles.**

Teams are groups with explicit role definitions and staff assignments.

## Type Hierarchy

```
vertex (abstract)
└── actor (concrete)
    └── group (concrete)
        └── team (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `group`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all group/actor/vertex fields:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/team` |
| `extends` | string | Must be `group` |
| `tags` | array | Must include `[vertex, actor, group, team]` |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - vertex      # base type
  - actor       # grandparent type
  - group       # parent type
  - team        # concrete type
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `department` | string | Organizational department |
| `manager` | string | Team lead/manager ID |
| `charter` | string | Team charter or mandate |

## Body Content

Team bodies should describe:
- Team mission and responsibilities
- Required roles
- Current staff assignments
- Deliverables and scope

## Role in Role Assignment Pattern

Teams participate in the most specific form of the membership pattern:

```
role_assignment face (organizational pattern):
  staff → team (member edge)
  staff → role (qualified edge)
  team → role (includes edge)
```

Teams:
- Have staff members assigned to them (member edges)
- Require specific roles to be filled (includes edges)
- Are completed when all role requirements have assignments

## Organizational Charts

Teams are key elements in organization charts:
- **all_requirements_filled constraint:** Every includes edge (team → role) must be closed by a role_assignment face
- Topological holes indicate unfilled positions

## Example Instance

```yaml
---
type: vertex/team
extends: group
id: v:team:frontend
name: Frontend Engineering Team
tags:
  - vertex
  - actor
  - group
  - team
department: Engineering
charter: Build and maintain user-facing web applications
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Frontend Engineering Team

Responsible for all frontend web application development.

## Required Roles

- Lead Developer (1)
- Senior Developer (2)
- Developer (3)

## Current Members

- Alice Johnson (Lead Developer)
- Carol Smith (Developer)

## Responsibilities

- React application development
- UI/UX implementation
- Frontend infrastructure
- Code review and mentoring
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/team`
2. **Tag Chain:** Tags must include `[vertex, actor, group, team]`
3. **Extends:** Must extend `group`
4. **Member Target:** Appropriate target for member edges from staff
5. **Includes Source:** Appropriate source for includes edges to roles
6. **Organization Chart:** Must participate in organization charts
7. **Role Fulfillment:** All includes edges should ideally be closed by role_assignment faces
