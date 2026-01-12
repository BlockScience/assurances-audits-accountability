---
type: template/vertex/group
extends: actor
id: template:vertex:group
name: Group Type Template
description: Collective actors composed of individuals
instantiable: true
tags:
  - template
  - vertex
  - actor
  - group
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Group Type Template

**Collective actors composed of individuals.**

Groups represent collections of actors organized for a purpose.

## Type Hierarchy

```
vertex (abstract)
└── actor (concrete)
    └── group (concrete) ← YOU ARE HERE
        └── team (concrete)
```

## Inheritance

- **Extends:** `actor`
- **Extended by:** `team`
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all actor/vertex fields:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/group` or `vertex/team` |
| `extends` | string | Must be `actor` (or `group` for team) |
| `tags` | array | Must include `[vertex, actor, group]` |

## Tag Requirements

```yaml
# For group:
tags:
  - vertex
  - actor
  - group

# For team (subtype):
tags:
  - vertex
  - actor
  - group
  - team
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `purpose` | string | Group's mission or purpose |
| `size` | number | Current member count |
| `status` | string | active, forming, disbanded |

## Body Content

Group bodies should describe:
- Purpose and mission
- Membership composition
- Required properties/roles
- Responsibilities and scope

## Role in Membership Pattern

Groups are targets of actor_in_group edges and sources of actor_requires_property edges:

```
          actor
           /\
          /  \
  in_group/    \has_property
        /        \
       /          \
   group -----> property
     requires_property
```

## Subtypes

- **team** - Formal organizational unit with defined roles

## Example Instance

```yaml
---
type: vertex/group
extends: actor
id: v:group:project-alpha
name: Project Alpha Working Group
tags:
  - vertex
  - actor
  - group
purpose: Deliver Project Alpha milestones
status: active
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Project Alpha Working Group

Cross-functional group formed to deliver Project Alpha.

## Composition

- Engineers
- Designers
- Product managers

## Required Capabilities

- Technical expertise
- Design skills
- Project management
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/group` or `vertex/team`
2. **Tag Chain:** Tags must include `[vertex, actor, group]`
3. **Membership:** Can be target of actor_in_group edges
4. **Requirements:** Can be source of actor_requires_property edges
5. **Face Participation:** Can participate in membership faces
