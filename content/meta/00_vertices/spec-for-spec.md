---
type: vertex/spec
extends: doc
id: v:spec:spec
name: Specification for Specifications
description: Defines what makes a valid specification document in the knowledge complex
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T16:00:00Z
modified: 2025-12-27T16:00:00Z
dependencies: []
---

# Specification for Specifications

**This specification defines the structure and requirements for all specification documents in the knowledge complex.**

## Purpose

Specifications (specs) define **structural requirements** and **schema constraints** - the "what" of documentation. This spec-for-spec establishes what fields, sections, and properties must be present in any valid spec document.

## Required Frontmatter Fields

All spec documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/spec` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:spec:<name>`) |
| `name` | string | REQUIRED | Human-readable specification name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, spec]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of spec purpose |
| `sections` | array[object] | OPTIONAL | Compositional spec structure |
| `schema_type` | string | OPTIONAL | Schema format (json-schema, yaml, markdown, etc.) |
| `strictness` | enum | OPTIONAL | Enforcement level: `required`, `recommended`, `optional` |

## Required Body Sections

The markdown body of a spec document MUST contain:

### 1. Purpose Statement

A clear statement of what the spec defines and why it exists.

**Format:**
```markdown
## Purpose

[1-3 sentences explaining what this spec defines]
```

### 2. Structural Requirements

Explicit definition of what fields, sections, or elements must be present.

**Format:**
```markdown
## Required [Elements/Fields/Sections]

[Table or list defining required structural elements]
```

### 3. Format Constraints

Data types, patterns, validations, or format requirements.

**Format:**
```markdown
## Format Constraints

[Specific format rules, patterns, data types]
```

### 4. Schema Definition

Explicit schema in appropriate format (table, YAML, JSON Schema, etc.).

**May be structured as:**
- Markdown tables with column definitions
- YAML structure examples
- JSON Schema blocks
- Compositional references to other specs

## Optional Body Sections

### Examples

Concrete instances that satisfy the spec. RECOMMENDED for clarity.

**Format:**
```markdown
## Example Instance

\`\`\`yaml
---
[Valid example frontmatter]
---

# Valid Example Body
\`\`\`
```

### Validation Rules

Explicit rules for programmatic validation. RECOMMENDED for automation.

**Format:**
```markdown
## Validation Rules

1. [Rule description]
2. [Rule description]
```

### Compositional Sections

For modular specs that reference other specs.

**Format:**
```yaml
sections:
  - name: [section-name]
    spec: v:spec:[referenced-spec-id]
    required: true
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/spec`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:spec:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, spec]`

## Content Requirements

1. **Prescriptive Language:** Specs use imperative language (MUST, SHALL, REQUIRED)
2. **Structural Focus:** Specs define structure, not quality or best practices
3. **Deterministic:** Requirements must be objectively checkable
4. **Complete:** All required elements defined unambiguously

## Coupling Requirement

Every spec SHOULD be paired with a corresponding guidance document via a `coupling` edge. The guidance defines how to evaluate quality and fitness-for-purpose for documents that satisfy this spec's structural requirements.

## Self-Reference

This specification is itself an instance of type `vertex/spec` and satisfies its own requirements (self-describing property).

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that structural requirements are met
- **Validation** (against guidance-for-spec): Qualitative assessment of fitness-for-purpose

## Schema Summary

```yaml
# Required frontmatter
type: vertex/spec
extends: doc
id: v:spec:<name>
name: <string>
tags: [vertex, doc, spec]
version: <semver>
created: <ISO8601>
modified: <ISO8601>

# Optional frontmatter
description: <string>
sections: [...]
schema_type: <string>
strictness: required|recommended|optional

# Required body sections (markdown)
## Purpose
## Required [Elements]
## Format Constraints
## Schema Definition

# Optional body sections
## Example Instance
## Validation Rules
```

## Compliance

A document claiming `type: vertex/spec` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Type constraints are satisfied
4. Content uses prescriptive language focused on structure

---

**Note:** This specification verifies itself - it contains all required fields and sections it mandates, demonstrating self-referential coherence.
