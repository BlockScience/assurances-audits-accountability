---
type: vertex/spec
extends: doc
id: v:spec:purpose
name: Specification for Purpose Documents
description: Defines what makes a valid purpose document - the problem statement, objectives, deliverables, constraints, and success criteria
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies: []
---

# Specification for Purpose Documents

**This specification defines the structure and requirements for purpose documents in the knowledge complex.**

## Purpose

Purpose documents define **what problem the AI solves** - the user need, core objectives, specific deliverables, constraints, and success criteria. This spec establishes what fields and sections must be present in any valid purpose document.

## Required Frontmatter Fields

All purpose documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/purpose` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:purpose:<name>`) |
| `name` | string | REQUIRED | Human-readable purpose name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, purpose]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of purpose |
| `domain` | string | OPTIONAL | Primary domain (e.g., `ai_model_design`, `education`) |

## Required Body Sections

The markdown body of a purpose document MUST contain:

### 1. Purpose Statement

A clear meta-statement about this purpose document.

**Format:**
```markdown
## Purpose

This purpose document defines [what this AI helps users accomplish].
```

### 2. Problem Statement

Specific user problem being solved.

**Format:**
```markdown
## Problem Statement

Your purpose is to help users [solve specific problem].
```

**Requirements:**
- MUST focus on user need, not AI capability
- MUST be specific (not vague like "help with stuff")
- MUST use format: "help users [action]"
- SHOULD be clear and direct

### 3. Core Objectives

Specific objectives the AI accomplishes.

**Format:**
```markdown
## Core Objectives

You accomplish this by:

- [Action verb] [specific objective 1]
- [Action verb] [specific objective 2]
- [Action verb] [specific objective 3]
- [Optional: 3 more objectives, max 6 total]
```

**Requirements:**
- MUST list 3-6 objectives
- Each objective MUST use action verbs (analyzing, extracting, generating, validating)
- Objectives MUST be measurable and realistic
- Each objective MUST directly address the problem
- MUST use format: "You accomplish this by:" followed by bulleted list

### 4. Specific Deliverables

What the AI produces or provides.

**Format:**
```markdown
## Specific Deliverables

- [Concrete artifact 1] conforming to [[spec-for-type1]]
- [Concrete artifact 2] conforming to [[spec-for-type2]]
- [Concrete artifact 3]
```

**Requirements:**
- MUST name specific artifacts or outcomes
- MUST be concrete (e.g., "template.yaml specification", "compliance report")
- SHOULD specify deliverable types by referencing specs (e.g., "conforming to [[spec-for-charts]]")
- SHOULD create new spec and guidance if no existing spec covers the deliverable type
- Deliverables SHOULD align with objectives
- SHOULD include at least 2 deliverables

### 5. Constraints and Boundaries

What is OUT of scope.

**Format:**
```markdown
## Constraints and Boundaries

- [Explicit constraint 1]
- [Explicit constraint 2]
- [Explicit constraint 3]
```

**Requirements:**
- MUST define what is out of scope
- MUST set clear boundaries
- MUST prevent scope creep
- SHOULD include at least 3 constraints
- Examples: "only analyzes provided documents", "does not modify original files"

### 6. Success Criteria

What makes the AI successful.

**Format:**
```markdown
## Success Criteria

Your work is successful when:

- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]
```

**Requirements:**
- MUST use format: "Your work is successful when:" followed by bulleted list
- MUST include quality standards
- MUST include user value measures
- MUST include verifiable completion criteria
- SHOULD mix quality, completeness, usability, and outcome measures
- Criteria SHOULD be measurable, not purely subjective

## Optional Body Sections

### Use Cases

Scenarios where this purpose applies.

**Format:**
```markdown
## Use Cases

- [Use case 1]
- [Use case 2]
```

### Integration Notes

How this purpose relates to persona and protocol.

**Format:**
```markdown
## Integration Notes

**With Persona:** [How persona expertise enables this purpose]
**With Protocol:** [How protocol achieves this purpose]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/purpose`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:purpose:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, purpose]`

## Content Requirements

1. **User-Centered:** Purpose must address user needs, not just AI features
2. **Specificity:** Problem and objectives must be specific and concrete
3. **Deliverable Typing:** Deliverables should reference specs for their types; create new specs if needed
4. **Measurability:** Success criteria must be verifiable
5. **Alignment:** Objectives, deliverables, and success criteria must align
6. **Boundaries:** Constraints must be explicit to manage expectations

## Compositional Usage

Purpose documents are typically referenced as typed subsections in compositional documents:

```yaml
sections:
  - name: purpose-section
    spec: v:spec:purpose
    required: true
```

When used compositionally, the referencing document MUST include all required sections defined in this spec.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present
- **Validation** (against guidance-for-purpose): Qualitative assessment of user-centeredness, specificity, and measurability

## Schema Summary

```yaml
# Required frontmatter
type: vertex/purpose
extends: doc
id: v:purpose:<name>
name: <string>
tags: [vertex, doc, purpose]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Optional frontmatter
description: <string>
domain: <string>

# Required body sections (markdown)
## Purpose
## Problem Statement
## Core Objectives (3-6 items with action verbs)
## Specific Deliverables (≥2 items, with type specs when applicable)
## Constraints and Boundaries (≥3 items)
## Success Criteria (measurable outcomes)

# Optional body sections
## Use Cases
## Integration Notes
```

## Compliance

A document claiming `type: vertex/purpose` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Core Objectives lists 3-6 items using action verbs
4. Specific Deliverables lists at least 2 concrete artifacts
5. Constraints and Boundaries lists at least 3 explicit constraints
6. Success Criteria includes measurable outcomes
7. Type constraints are satisfied
8. Content is user-centered (not feature-focused)

---

**Note:** This specification supports the PPP (Persona-Purpose-Protocol) framework by defining the structural requirements for purpose components. Purpose is the anchor of PPP design.
