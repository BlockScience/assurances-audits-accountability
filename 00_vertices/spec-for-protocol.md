---
type: vertex/spec
extends: doc
id: v:spec:protocol
name: Specification for Protocol Documents
description: Defines what makes a valid protocol document - the systematic workflow, phases, user collaboration, quality checks, and consistent principles
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies: []
---

# Specification for Protocol Documents

**This specification defines the structure and requirements for protocol documents in the knowledge complex.**

## Purpose

Protocol documents define **how the AI works systematically** - the workflow, phases, user collaboration points, quality assurance, and consistent principles. This spec establishes what fields and sections must be present in any valid protocol document.

## Required Frontmatter Fields

All protocol documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/protocol` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:protocol:<name>`) |
| `name` | string | REQUIRED | Human-readable protocol name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, protocol]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of protocol |
| `domain` | string | OPTIONAL | Primary domain (e.g., `ai_model_design`, `education`) |
| `num_phases` | integer | OPTIONAL | Number of phases in workflow (3-5 recommended) |

## Required Body Sections

The markdown body of a protocol document MUST contain:

### 1. Purpose Statement

A clear meta-statement about this protocol document.

**Format:**
```markdown
## Purpose

This protocol defines the systematic workflow for [accomplishing specific goal].
```

### 2. Workflow Overview

Brief overview of the complete workflow.

**Format:**
```markdown
## Workflow Overview

You work through a systematic [number]-phase process to [accomplish goal].

[1-2 sentences explaining overall approach]
```

**Requirements:**
- MUST state number of phases
- MUST explain overall approach
- SHOULD be concise (2-3 sentences maximum)

### 3. Phase Definitions

Distinct phases that make up the workflow.

**Format:**
```markdown
## Phase Definitions

### Phase 1: [Phase Name]

**When:** [Trigger or starting condition]

**Steps:**
1. [Specific action 1]
2. [Specific action 2]
3. [Specific action 3]
4. [Optional: 3 more steps, max 6 total]

**Outputs:** [What is produced]

**Next:** [Transition to next phase]

[Repeat for each phase]
```

**Requirements:**
- MUST define 3-5 phases
- Each phase MUST have:
  - Phase name
  - "When" trigger/condition
  - 3-6 specific, actionable steps
  - Outputs produced
  - Transition to next phase
- Phases MUST follow logical progression
- Steps MUST be concrete and executable (not vague)

### 4. User Collaboration Points

When and how to engage the user.

**Format:**
```markdown
## User Collaboration Points

### Validation Points
- [When to confirm findings]

### Input Gathering
- [When to ask questions]

### Approval Steps
- [When to get permission]

### Expertise Respect
- [When to defer to user knowledge]
```

**Requirements:**
- MUST specify when user is engaged
- MUST include validation points
- MUST include input gathering
- SHOULD include approval steps
- MUST balance engagement (not too frequent, not absent)

### 5. Quality Assurance

Quality checks and validation steps.

**Format:**
```markdown
## Quality Assurance

### Input Validation
- [What to check before starting]

### Process Verification
- [What to check during workflow]

### Output Quality Checks
- [What to check in deliverables]

### Completeness Verification
- [What to check for completeness]

### Error Prevention
- [How to prevent common errors]
```

**Requirements:**
- MUST define quality checks
- MUST specify WHAT to check
- MUST specify WHEN to check
- SHOULD include input validation, process verification, and output quality checks

### 6. Tools and Scripts

Explicit enumeration of tools, scripts, and commands used in the workflow.

**Format:**
```markdown
## Tools and Scripts

### Verification Tools
- **[Tool name]** (`path/to/tool`) - [When to use] - [What it does]
- Example: `python scripts/verify_template_based.py <file>` - [Usage description]

### Analysis Tools
- **[Tool name]** (`path/to/tool`) - [When to use] - [What it does]

### [Additional Tool Categories as needed]
```

**Requirements:**
- MUST list all tools and scripts referenced in workflow phases
- Each tool MUST specify:
  - Tool name or script path
  - When to use it (which phase, what trigger)
  - What it does (purpose and output)
  - Command syntax or invocation pattern
- Tools SHOULD be grouped by category (verification, analysis, generation, etc.)
- If no tools are used, section MAY be omitted OR include statement "No automated tools required"

### 7. Consistent Principles

Principles that apply throughout all phases.

**Format:**
```markdown
## Consistent Principles

Throughout all phases:

- [Cross-phase principle 1]
- [Cross-phase principle 2]
- [Cross-phase principle 3]
```

**Requirements:**
- MUST list 3-5 principles
- Principles MUST apply across all phases (not phase-specific)
- Examples: "Evidence-based reasoning", "Transparent communication", "User collaboration"
- MUST use format: "Throughout all phases:" followed by bulleted list

## Optional Body Sections

### Use Cases

Scenarios where this protocol applies.

**Format:**
```markdown
## Use Cases

- [Use case 1]
- [Use case 2]
```

### Integration Notes

How this protocol relates to persona and purpose.

**Format:**
```markdown
## Integration Notes

**With Persona:** [How protocol reflects persona's approach]
**With Purpose:** [How protocol achieves the purpose]
```

### Common Pitfalls

Anti-patterns to avoid.

**Format:**
```markdown
## Common Pitfalls

- **[Pitfall name]:** [Description and how to avoid]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/protocol`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:protocol:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, protocol]`

## Content Requirements

1. **Structure:** Protocol must have clear phases (3-5 recommended)
2. **Actionability:** Steps must be specific and executable
3. **Progression:** Phases must follow logical order
4. **Collaboration:** User engagement must be specified
5. **Quality:** Quality checks must be defined
6. **Consistency:** Cross-phase principles must be stated

## Compositional Usage

Protocol documents are typically referenced as typed subsections in compositional documents:

```yaml
sections:
  - name: protocol-section
    spec: v:spec:protocol
    required: true
```

When used compositionally, the referencing document MUST include all required sections defined in this spec.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present
- **Validation** (against guidance-for-protocol): Qualitative assessment of clarity, executability, and completeness

## Schema Summary

```yaml
# Required frontmatter
type: vertex/protocol
extends: doc
id: v:protocol:<name>
name: <string>
tags: [vertex, doc, protocol]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Optional frontmatter
description: <string>
domain: <string>
num_phases: <integer>

# Required body sections (markdown)
## Purpose
## Workflow Overview
## Phase Definitions (3-5 phases)
  ### Phase N: [Name]
    **When:** ...
    **Steps:** (3-6 items)
    **Outputs:** ...
    **Next:** ...
## User Collaboration Points
## Quality Assurance
## Tools and Scripts (if tools are used in workflow)
## Consistent Principles (3-5 items)

# Optional body sections
## Use Cases
## Integration Notes
## Common Pitfalls
```

## Compliance

A document claiming `type: vertex/protocol` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Phase Definitions includes 3-5 phases
4. Each phase has trigger, 3-6 steps, outputs, and transition
5. User Collaboration Points specifies when user is engaged
6. Quality Assurance defines what/when to check
7. Tools and Scripts section present if workflow references tools (or states no tools required)
8. Each tool listed with path, when to use, what it does, and command syntax
9. Consistent Principles lists 3-5 cross-phase behaviors
10. Type constraints are satisfied
11. Steps are concrete and executable (not vague)

---

**Note:** This specification supports the PPP (Persona-Purpose-Protocol) framework by defining the structural requirements for protocol components.
