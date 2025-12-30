---
type: template/vertex/individual
extends: actor
id: template:vertex:individual
name: Individual Type Template
description: Single actors with personal agency
instantiable: true
tags:
  - template
  - vertex
  - actor
  - individual
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Individual Type Template

**Single actors with personal agency.**

Individuals represent single people or entities as opposed to collective groups.

## Type Hierarchy

```
vertex (abstract)
└── actor (concrete)
    └── individual (concrete) ← YOU ARE HERE
        └── staff (concrete)
```

## Inheritance

- **Extends:** `actor`
- **Extended by:** `staff`
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all actor/vertex fields:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/individual` or `vertex/staff` |
| `extends` | string | Must be `actor` (or `individual` for staff) |
| `tags` | array | Must include `[vertex, actor, individual]` |

## Tag Requirements

```yaml
# For individual:
tags:
  - vertex
  - actor
  - individual

# For staff (subtype):
tags:
  - vertex
  - actor
  - individual
  - staff
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `email` | string | Email address |
| `role_title` | string | Job title or role |

## Body Content

Individual bodies should describe:
- Name and identity
- Qualifications and skills
- Team memberships
- Role assignments

## Role in Membership Pattern

Individuals are narrowed actors in the assignment face:

```
assignment face (narrows actor → individual):
  individual → team (member edge)
  individual → role (qualified edge)
  team → role (includes edge)
```

## Subtypes

- **staff** - Employees or team members in an organizational context

## Example Instance

```yaml
---
type: vertex/individual
extends: actor
id: v:individual:alice
name: Alice Johnson
tags:
  - vertex
  - actor
  - individual
email: alice@example.com
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Alice Johnson

Individual contributor in the organization.

## Qualifications

- 5 years software development experience
- Python, JavaScript expertise
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/individual` or `vertex/staff`
2. **Tag Chain:** Tags must include `[vertex, actor, individual]`
3. **Assignment:** Can be source of member and qualified edges
4. **Face Participation:** Can participate in assignment and role_assignment faces
