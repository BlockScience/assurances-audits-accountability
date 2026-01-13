---
type: vertex/spec
extends: doc
id: v:spec:property
name: Specification for Property Documents
description: Defines what makes a valid property document - attributes, characteristics, or capabilities that can be possessed by actors
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies: []
---

# Specification for Property Documents

**This specification defines the structure and requirements for property documents in the knowledge complex.**

## Purpose

Property documents define **attributes or characteristics that can be possessed** by actors. Properties include skills, roles, qualifications, statuses, and other characteristics that describe or modify actors. This spec establishes what fields and sections must be present in any valid property document.

## Required Frontmatter Fields

All property documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/property` or extend it (e.g., `vertex/skill`) |
| `extends` | string | REQUIRED | Must be `vertex` or another vertex type |
| `id` | string | REQUIRED | Unique identifier (format: `v:property:<name>`) |
| `name` | string | REQUIRED | Human-readable property name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, property]` at minimum |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of property |
| `domain` | string | OPTIONAL | Primary domain (e.g., `education`, `organization`, `technical`) |

## Required Body Sections

The markdown body of a property document MUST contain:

### 1. Purpose Statement

A clear statement of what this property represents.

**Format:**
```markdown
## Purpose

This property represents [attribute/characteristic description and what it signifies].
```

### 2. Property Definition

Specific definition and meaning of the property.

**Format:**
```markdown
## Property Definition

[1-2 paragraphs defining what this property is, what it means when an actor possesses it]
```

**Requirements:**
- MUST clearly define what the property is
- MUST explain the significance of possessing this property
- SHOULD distinguish this property from similar properties

### 3. Acquisition

How this property is acquired or assigned.

**Format:**
```markdown
## Acquisition

[Description of how actors gain this property]
```

**Requirements:**
- MUST explain the process or criteria for acquisition
- SHOULD indicate whether property is earned, assigned, inherent, or learned
- Examples: "Learned through study and practice", "Assigned by authority", "Inherent to entity type"

### 4. Applicable Actors

What types of actors can possess this property.

**Format:**
```markdown
## Applicable Actors

- [Actor type 1]: [Why/how this actor type can possess this property]
- [Actor type 2]: [Why/how this actor type can possess this property]
```

**Requirements:**
- MUST list at least 1 actor type that can possess this property
- SHOULD reference actor specs if they exist (e.g., `vertex/student`, `vertex/staff`)
- MAY specify constraints (e.g., "Only students who have completed Module A")

## Optional Body Sections

### Verification

How possession of this property can be verified.

**Format:**
```markdown
## Verification

[Description of how to verify an actor possesses this property]
```

**Examples:** "Assessment results", "Certificate", "Attestation", "Observable behavior"

### Related Properties

Other properties related to this one.

**Format:**
```markdown
## Related Properties

- **[Property name 1]**: [Relationship description]
- **[Property name 2]**: [Relationship description]
```

**Examples:** "Prerequisite for", "Implies possession of", "Mutually exclusive with"

### Examples

Concrete instances of this property.

**Format:**
```markdown
## Examples

- **[Property instance 1]**: [Brief description]
- **[Property instance 2]**: [Brief description]
```

### Constraints

Limitations or constraints on this property.

**Format:**
```markdown
## Constraints

- [Constraint 1]
- [Constraint 2]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/property` (or a type that extends it)
2. **Extends Field:** MUST be `vertex` or another vertex type
3. **ID Format:** MUST match pattern `v:property:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include at minimum: `[vertex, property]`

## Content Requirements

1. **Clarity:** Property definition must be unambiguous
2. **Acquisition:** Must explain how property is obtained
3. **Applicability:** Must specify which actors can possess this property
4. **Domain Relevance:** Property must serve a clear purpose in its domain

## Extension Pattern

Property is a **base type** intended to be extended:

```yaml
# Example: Skill extends Property
type: vertex/skill
extends: vertex/property
id: v:skill:python-programming
tags: [vertex, property, skill]
```

When extending property, child types:
- MUST inherit all required sections from this spec
- MAY add additional required sections
- MUST include parent type in extends field
- MUST include full tag inheritance chain

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present
- **Validation** (against guidance-for-property): Qualitative assessment of clarity, applicability, and domain fit

## Schema Summary

```yaml
# Required frontmatter
type: vertex/property  # or extends it
extends: vertex
id: v:property:<name>
name: <string>
tags: [vertex, property]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Optional frontmatter
description: <string>
domain: <string>

# Required body sections (markdown)
## Purpose
## Property Definition
## Acquisition
## Applicable Actors (≥1 item)

# Optional body sections
## Verification
## Related Properties
## Examples
## Constraints
```

## Compliance

A document claiming `type: vertex/property` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Applicable Actors lists at least 1 actor type
4. Type constraints are satisfied
5. Property definition is clear and unambiguous
6. Acquisition process is explained

---

**Note:** Property is a foundational type for attributes that can be possessed by actors. It is intended to be extended for domain-specific property types (skills, roles, qualifications, etc.).
