---
type: vertex/spec
extends: doc
id: v:spec:actor
name: Specification for Actor Documents
description: Defines what makes a valid actor document - entities that can perform actions, possess properties, and participate in relationships
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies: []
---

# Specification for Actor Documents

**This specification defines the structure and requirements for actor documents in the knowledge complex.**

## Purpose

Actor documents define **entities that can act** - they can possess properties (skills, roles, attributes), perform actions, and participate in relationships with other entities. This spec establishes what fields and sections must be present in any valid actor document.

## Required Frontmatter Fields

All actor documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/actor` or extend it (e.g., `vertex/student`) |
| `extends` | string | REQUIRED | Must be `vertex` or another vertex type |
| `id` | string | REQUIRED | Unique identifier (format: `v:actor:<name>`) |
| `name` | string | REQUIRED | Human-readable actor name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, actor]` at minimum |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of actor |
| `domain` | string | OPTIONAL | Primary domain (e.g., `organization`, `education`, `system`) |

## Required Body Sections

The markdown body of an actor document MUST contain:

### 1. Purpose Statement

A clear statement of what this actor represents.

**Format:**
```markdown
## Purpose

This actor represents [entity description and role in the system].
```

### 2. Actor Identity

Specific identity and characteristics of the actor.

**Format:**
```markdown
## Actor Identity

[1-2 paragraphs defining what/who this actor is - type, characteristics, role in domain]
```

**Requirements:**
- MUST be specific about what kind of entity this is
- MUST define the actor's primary function or role
- SHOULD explain why this actor exists in the system

### 3. Capabilities

What the actor can do.

**Format:**
```markdown
## Capabilities

- [Capability 1]: [Description]
- [Capability 2]: [Description]
- [Capability 3]: [Description]
```

**Requirements:**
- MUST list at least 2 capabilities
- Each capability MUST be actionable
- SHOULD distinguish this actor from other actor types

### 4. Properties

What the actor can possess or be characterized by.

**Format:**
```markdown
## Properties

- [Property type 1]: [What kind of properties of this type can the actor have]
- [Property type 2]: [What kind of properties of this type can the actor have]
```

**Requirements:**
- MUST list at least 1 property type the actor can possess
- SHOULD reference property specs if they exist (e.g., `vertex/skill`, `vertex/role`)
- Examples: "Skills: Can possess learnable capabilities", "Roles: Can hold organizational positions"

## Optional Body Sections

### Relationships

Types of relationships this actor can participate in.

**Format:**
```markdown
## Relationships

- [Relationship type 1]: [Description of relationship with other entities]
- [Relationship type 2]: [Description of relationship with other entities]
```

### Examples

Concrete instances of this actor type.

**Format:**
```markdown
## Examples

- **[Actor name 1]**: [Brief description]
- **[Actor name 2]**: [Brief description]
```

### Constraints

Limitations or constraints on this actor type.

**Format:**
```markdown
## Constraints

- [Constraint 1]
- [Constraint 2]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/actor` (or a type that extends it)
2. **Extends Field:** MUST be `vertex` or another vertex type
3. **ID Format:** MUST match pattern `v:actor:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include at minimum: `[vertex, actor]`

## Content Requirements

1. **Specificity:** Actor identity must be clearly defined, not vague
2. **Actionability:** Capabilities must describe what the actor can DO
3. **Properties:** Must define what characteristics/attributes the actor can possess
4. **Domain Relevance:** Actor must serve a clear purpose in its domain

## Extension Pattern

Actor is a **base type** intended to be extended:

```yaml
# Example: Student extends Actor
type: vertex/student
extends: vertex/actor
id: v:student:learner
tags: [vertex, actor, student]
```

When extending actor, child types:
- MUST inherit all required sections from this spec
- MAY add additional required sections
- MUST include parent type in extends field
- MUST include full tag inheritance chain

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present
- **Validation** (against guidance-for-actor): Qualitative assessment of clarity, actionability, and domain fit

## Schema Summary

```yaml
# Required frontmatter
type: vertex/actor  # or extends it
extends: vertex
id: v:actor:<name>
name: <string>
tags: [vertex, actor]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Optional frontmatter
description: <string>
domain: <string>

# Required body sections (markdown)
## Purpose
## Actor Identity
## Capabilities (≥2 items)
## Properties (≥1 item)

# Optional body sections
## Relationships
## Examples
## Constraints
```

## Compliance

A document claiming `type: vertex/actor` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Capabilities lists at least 2 actionable capabilities
4. Properties lists at least 1 property type
5. Type constraints are satisfied
6. Actor identity is clear and specific

---

**Note:** Actor is a foundational type for entities that can act, possess properties, and participate in relationships. It is intended to be extended for domain-specific actor types (students, staff, teams, etc.).
