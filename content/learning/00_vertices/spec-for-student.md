---
type: vertex/spec
extends: doc
id: v:spec:student
name: Specification for Student Documents
description: Defines what makes a valid student document - actors engaged in learning who possess skills and study learning modules
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies:
  - v:spec:actor
---

# Specification for Student Documents

**This specification defines the structure and requirements for student documents in the knowledge complex.**

## Purpose

Student documents define **actors engaged in learning** - entities that possess skills (prerequisite knowledge), study learning modules, and acquire new skills (learning objectives). This spec extends the actor specification with learning-specific requirements.

## Inheritance

This specification **extends** `vertex/actor` (v:spec:actor).

All requirements from spec-for-actor apply, PLUS the additional requirements defined here.

## Required Frontmatter Fields

All student documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/student` |
| `extends` | string | REQUIRED | Must be `vertex/actor` |
| `id` | string | REQUIRED | Unique identifier (format: `v:student:<name>`) |
| `name` | string | REQUIRED | Human-readable student name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, actor, student]` (full inheritance chain) |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of student |
| `domain` | string | OPTIONAL | Learning domain (e.g., `knowledge_complexes`, `software_engineering`) |

## Required Body Sections

### Inherited from spec-for-actor

The markdown body MUST contain all sections required by spec-for-actor:

1. **Purpose** - Statement of what this student represents
2. **Actor Identity** - Identity and characteristics
3. **Capabilities** - What the student can do (≥2 items)
4. **Properties** - What the student can possess (≥1 item)

### Additional Required Sections for Student

#### 5. Learning Context

The context in which this student learns.

**Format:**
```markdown
## Learning Context

[Description of the learning environment, goals, or situation this student represents]
```

**Requirements:**
- MUST describe the learning situation or environment
- SHOULD explain what the student is trying to learn
- Examples: "Generic learner for knowledge complex syllabi", "Software engineering student learning testing practices"

#### 6. Prerequisite Skills

Skills the student already possesses (input state).

**Format:**
```markdown
## Prerequisite Skills

- **[Skill 1]**: [Description of skill level or proficiency]
- **[Skill 2]**: [Description of skill level or proficiency]
```

**Requirements:**
- MAY be empty list if student has no prerequisites (beginner)
- Each skill SHOULD reference a skill vertex if one exists
- Skills MUST be relevant to the learning context

#### 7. Learning Goals

Skills the student aims to acquire (output state).

**Format:**
```markdown
## Learning Goals

- **[Skill 1]**: [What the student wants to learn]
- **[Skill 2]**: [What the student wants to learn]
```

**Requirements:**
- MUST list at least 1 learning goal
- Each goal SHOULD reference a skill vertex or be describable as a skill
- Goals MUST be achievable through learning modules

## Optional Body Sections

### Current Progress

What modules the student has completed or is studying.

**Format:**
```markdown
## Current Progress

- **Completed**: [List of completed modules]
- **In Progress**: [List of modules currently studying]
- **Planned**: [List of planned modules]
```

### Learning Style

How this student prefers to learn.

**Format:**
```markdown
## Learning Style

[Description of learning preferences, pace, approach]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/student`
2. **Extends Field:** MUST be exactly `vertex/actor`
3. **ID Format:** MUST match pattern `v:student:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, actor, student]`
5. **Dependencies:** MUST include `v:spec:actor` in dependencies array

## Content Requirements

1. **Actor Compliance:** MUST satisfy all requirements of spec-for-actor
2. **Learning Context:** Must provide clear context for learning
3. **Skills:** Prerequisites and goals must be specified (goals ≥1)
4. **Coherence:** Prerequisites, goals, and context must align logically

## Relationship Patterns

Students participate in specific relationship patterns:

### has-skill Edges

```yaml
# Student possesses a skill
type: edge/has-skill
source: v:student:learner
target: v:skill:python-basics
```

### studies Edges

```yaml
# Student studies a learning module
type: edge/studies
source: v:student:learner
target: v:learning-module:core-concepts
```

### prerequisite Faces

```yaml
# Student with skill can study module requiring that skill
type: face/prerequisite
vertices:
  - v:student:learner
  - v:skill:topology-basics
  - v:learning-module:advanced-topology
```

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present, including actor requirements
- **Validation** (against guidance-for-student): Qualitative assessment of learning context appropriateness, skill coherence, and goal realism

## Schema Summary

```yaml
# Required frontmatter
type: vertex/student
extends: vertex/actor
id: v:student:<name>
name: <string>
tags: [vertex, actor, student]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies:
  - v:spec:actor

# Optional frontmatter
description: <string>
domain: <string>

# Required body sections (markdown)
## Purpose
## Actor Identity
## Capabilities (≥2 items) [from actor]
## Properties (≥1 item) [from actor]
## Learning Context [student-specific]
## Prerequisite Skills (≥0 items) [student-specific]
## Learning Goals (≥1 item) [student-specific]

# Optional body sections
## Current Progress
## Learning Style
```

## Compliance

A document claiming `type: vertex/student` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections from spec-for-actor are present
3. All REQUIRED body sections specific to student are present
4. Learning Goals lists at least 1 goal
5. Type constraints are satisfied
6. Dependencies include v:spec:actor
7. The document is compliant with spec-for-actor

---

**Note:** Student extends actor to represent learners who possess skills and engage with learning modules. This type is fundamental to educational syllabi and learning path charts.
