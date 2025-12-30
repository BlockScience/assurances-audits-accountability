---
type: template/vertex/role
extends: property
id: template:vertex:role
name: Role Type Template
description: Organizational roles within teams
instantiable: true
tags:
  - template
  - vertex
  - property
  - role
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Role Type Template

**Organizational roles within teams.**

Roles are properties specific to organizational structures, representing positions or functions within teams.

## Type Hierarchy

```
vertex (abstract)
└── property (concrete)
    └── role (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `property`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all property/vertex fields:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/role` |
| `extends` | string | Must be `property` |
| `tags` | array | Must include `[vertex, property, role]` |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - vertex      # base type
  - property    # parent type
  - role        # concrete type
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `level` | string | Seniority level (junior, senior, lead, etc.) |
| `responsibilities` | array | List of responsibilities |
| `required_skills` | array | Required skills or qualifications |

## Body Content

Role bodies should describe:
- Role title and purpose
- Key responsibilities
- Required qualifications
- Success criteria
- Career progression

## Role in Role Assignment Pattern

Roles participate in the most specific form of the membership pattern:

```
role_assignment face (organizational pattern):
  staff → team (member edge)
  staff → role (qualified edge)
  team → role (includes edge)
```

Roles are:
- **Included** by teams (teams require these roles via includes edges)
- **Held by** qualified staff (staff have qualifications via qualified edges)
- **Assigned** when role_assignment faces close the triangle

## Organization Charts

Roles are critical for organization chart completeness:
- Teams define required roles via includes edges
- Unfilled roles create topological holes
- Role assignments (faces) close these holes

## Example Instance

```yaml
---
type: vertex/role
extends: property
id: v:role:lead-developer
name: Lead Developer
tags:
  - vertex
  - property
  - role
level: senior
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Lead Developer

Senior technical role responsible for architecture and team leadership.

## Responsibilities

- System architecture and design
- Code review and quality standards
- Mentoring junior developers
- Technical decision-making
- Sprint planning and task breakdown

## Required Qualifications

- 5+ years software development experience
- Proven system design expertise
- Team leadership experience
- Strong communication skills

## Success Criteria

- Team velocity and quality metrics
- Architecture documentation maintained
- Knowledge sharing and mentorship
- Stakeholder satisfaction
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/role`
2. **Tag Chain:** Tags must include `[vertex, property, role]`
3. **Extends:** Must extend `property`
4. **Qualified Target:** Appropriate target for qualified edges from staff
5. **Includes Target:** Appropriate target for includes edges from teams
6. **Role Assignment:** Participates in role_assignment faces in organization charts
