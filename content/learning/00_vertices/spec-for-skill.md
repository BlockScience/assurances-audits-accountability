---
type: vertex/spec
extends: doc
id: v:spec:skill
name: Specification for Skill Documents
description: Defines what makes a valid skill document - learnable capabilities or knowledge that can be possessed by students and required by learning modules
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies:
  - v:spec:property
---

# Specification for Skill Documents

**This specification defines the structure and requirements for skill documents in the knowledge complex.**

## Purpose

Skill documents define **learnable capabilities or knowledge** that can be possessed by students (as prerequisites) and acquired through learning modules (as learning objectives). Skills are the currency of educational progression. This spec extends the property specification with learning-specific requirements.

## Inheritance

This specification **extends** `vertex/property` (v:spec:property).

All requirements from spec-for-property apply, PLUS the additional requirements defined here.

## Required Frontmatter Fields

All skill documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/skill` |
| `extends` | string | REQUIRED | Must be `vertex/property` |
| `id` | string | REQUIRED | Unique identifier (format: `v:skill:<name>`) |
| `name` | string | REQUIRED | Human-readable skill name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, property, skill]` (full inheritance chain) |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of skill |
| `domain` | string | OPTIONAL | Knowledge domain (e.g., `programming`, `mathematics`, `topology`) |
| `level` | string | OPTIONAL | Skill level (e.g., `beginner`, `intermediate`, `advanced`) |

## Required Body Sections

### Inherited from spec-for-property

The markdown body MUST contain all sections required by spec-for-property:

1. **Purpose** - Statement of what this skill represents
2. **Property Definition** - Definition and meaning of the skill
3. **Acquisition** - How the skill is learned
4. **Applicable Actors** - What actors can possess this skill (≥1 item)

### Additional Required Sections for Skill

#### 5. Learning Outcomes

Observable indicators that demonstrate skill possession.

**Format:**
```markdown
## Learning Outcomes

After acquiring this skill, a learner can:

- [Observable outcome 1]
- [Observable outcome 2]
- [Observable outcome 3]
```

**Requirements:**
- MUST list at least 2 observable outcomes
- Each outcome MUST be measurable or demonstrable
- Outcomes MUST use action verbs (explain, implement, analyze, create, etc.)
- SHOULD follow Bloom's taxonomy or similar framework

#### 6. Prerequisite Skills

Skills that should be possessed before learning this skill.

**Format:**
```markdown
## Prerequisite Skills

- **[Skill 1]**: [Why this prerequisite is needed]
- **[Skill 2]**: [Why this prerequisite is needed]
```

**Requirements:**
- MAY be empty if this is a foundational skill
- Each prerequisite SHOULD reference another skill vertex
- MUST NOT create circular dependencies (skill A requires skill A)

#### 7. Enables

What this skill enables a learner to do or learn.

**Format:**
```markdown
## Enables

- **[Activity/Skill 1]**: [How this skill enables it]
- **[Activity/Skill 2]**: [How this skill enables it]
```

**Requirements:**
- MUST list at least 1 thing this skill enables
- MAY reference learning modules, advanced skills, or capabilities
- SHOULD explain the progression path

## Optional Body Sections

### Assessment Methods

How possession of this skill can be assessed.

**Format:**
```markdown
## Assessment Methods

- **[Method 1]**: [Description of assessment approach]
- **[Method 2]**: [Description of assessment approach]
```

**Examples:** "Problem-solving exercises", "Code review", "Written explanation", "Practical demonstration"

### Related Skills

Other skills related to this one.

**Format:**
```markdown
## Related Skills

- **[Skill 1]**: [Relationship - e.g., prerequisite for, similar to, complements]
- **[Skill 2]**: [Relationship]
```

### Resources

Materials for learning this skill.

**Format:**
```markdown
## Resources

- [Resource 1]: [Description]
- [Resource 2]: [Description]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/skill`
2. **Extends Field:** MUST be exactly `vertex/property`
3. **ID Format:** MUST match pattern `v:skill:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, property, skill]`
5. **Dependencies:** MUST include `v:spec:property` in dependencies array
6. **Prerequisite Acyclicity:** MUST NOT create circular prerequisite chains

## Content Requirements

1. **Property Compliance:** MUST satisfy all requirements of spec-for-property
2. **Observability:** Learning outcomes must be observable/measurable
3. **Progression:** Enables section must show how skill connects to advancement
4. **Prerequisites:** Must define prerequisite chain (or explicitly state none)
5. **Domain Clarity:** Skill must be clearly scoped to a knowledge domain

## Relationship Patterns

Skills participate in specific relationship patterns:

### has-skill Edges

```yaml
# Student possesses this skill
type: edge/has-skill
source: v:student:learner
target: v:skill:python-basics
```

### requires-skill Edges

```yaml
# Learning module requires this skill as prerequisite
type: edge/requires-skill
source: v:learning-module:advanced-programming
target: v:skill:python-basics
```

### prerequisite Faces

```yaml
# Student with skill can study module requiring that skill
type: face/prerequisite
vertices:
  - v:student:learner
  - v:skill:python-basics
  - v:learning-module:data-structures
```

## Skill Granularity Guidance

Skills can range from broad to narrow:

- **Broad:** "Python programming", "Data analysis"
- **Moderate:** "Object-oriented design", "Statistical testing"
- **Narrow:** "List comprehensions", "T-tests"

Choose granularity appropriate to:
- The learning context
- The modules that require the skill
- The assessment capability

For educational syllabi, moderate granularity is typically most useful.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present, including property requirements
- **Validation** (against guidance-for-skill): Qualitative assessment of learning outcome quality, prerequisite appropriateness, and domain fit

## Schema Summary

```yaml
# Required frontmatter
type: vertex/skill
extends: vertex/property
id: v:skill:<name>
name: <string>
tags: [vertex, property, skill]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies:
  - v:spec:property

# Optional frontmatter
description: <string>
domain: <string>
level: <string>

# Required body sections (markdown)
## Purpose
## Property Definition [from property]
## Acquisition [from property]
## Applicable Actors (≥1 item) [from property]
## Learning Outcomes (≥2 items) [skill-specific]
## Prerequisite Skills (≥0 items) [skill-specific]
## Enables (≥1 item) [skill-specific]

# Optional body sections
## Assessment Methods
## Related Skills
## Resources
```

## Compliance

A document claiming `type: vertex/skill` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections from spec-for-property are present
3. All REQUIRED body sections specific to skill are present
4. Learning Outcomes lists at least 2 observable outcomes
5. Enables lists at least 1 progression path
6. Type constraints are satisfied
7. Dependencies include v:spec:property
8. The document is compliant with spec-for-property
9. No circular prerequisite dependencies exist

---

**Note:** Skill extends property to represent learnable knowledge and capabilities. Skills form the prerequisite and learning objective chains that structure educational syllabi and learning paths.
