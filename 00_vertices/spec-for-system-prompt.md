---
type: vertex/spec
extends: doc
id: v:spec:system_prompt
name: Specification for System Prompt Documents
description: Defines what makes a valid system prompt document composed of typed subsections (persona, purpose, protocol) following the PPP framework
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies:
  - v:spec:persona
  - v:spec:purpose
  - v:spec:protocol
---

# Specification for System Prompt Documents

**This specification defines the structure and requirements for system prompt documents - compositional documents built from typed subsections.**

## Purpose

System prompt documents define **complete AI model configurations** using the PPP (Persona-Purpose-Protocol) framework. This spec establishes that system prompts are compositional documents where each major section conforms to a specific document type (persona, purpose, protocol).

**Key Innovation:** This spec demonstrates the **typed subsection pattern** - subsections that must conform to other spec documents, analogous to typing fields with schema types (like context in JSON-LD).

## Required Frontmatter Fields

All system prompt documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/system_prompt` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:system_prompt:<name>`) |
| `name` | string | REQUIRED | Human-readable system prompt name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, system_prompt]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Compositional Structure

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `dependencies` | array[string] | REQUIRED | Must list: `[v:spec:persona, v:spec:purpose, v:spec:protocol]` |

**Critical:** The `dependencies` field declares which specs govern the typed subsections. This enables automated verification that subsections conform to their declared types.

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of system prompt |
| `domain` | string | OPTIONAL | Primary domain (e.g., `ai_model_design`, `education`) |
| `model_target` | string | OPTIONAL | Target AI model (e.g., `claude-opus-4`, `gpt-4`) |
| `intended_use` | string | OPTIONAL | Primary use case for this system prompt |

## Required Body Sections

The markdown body of a system prompt document MUST contain:

### 1. Purpose Statement

A clear meta-statement about this system prompt document.

**Format:**
```markdown
## Purpose

This system prompt defines a complete AI model configuration for [intended use] using the PPP (Persona-Purpose-Protocol) framework.
```

### 2. Persona Section (Typed Subsection)

**MUST conform to:** `v:spec:persona`

**Format:**
```markdown
## Persona

[All required sections from v:spec:persona:]

### Role and Identity
...

### Domain Expertise
...

### Approach and Methodology
...

### Communication Tone
...

### Boundaries and Limitations
...
```

**Requirements:**
- This section MUST contain ALL required sections from [v:spec:persona](v:spec:persona)
- This section MUST verify against the persona specification
- Subsection headers MUST be level 3 (###) under the level 2 (##) Persona header

### 3. Purpose Section (Typed Subsection)

**MUST conform to:** `v:spec:purpose`

**Format:**
```markdown
## Purpose

[All required sections from v:spec:purpose:]

### Problem Statement
...

### Core Objectives
...

### Specific Deliverables
...

### Constraints and Boundaries
...

### Success Criteria
...
```

**Requirements:**
- This section MUST contain ALL required sections from [v:spec:purpose](v:spec:purpose)
- This section MUST verify against the purpose specification
- Subsection headers MUST be level 3 (###) under the level 2 (##) Purpose header

**Note on Header Collision:** The top-level document has a `## Purpose` meta-statement AND a `## Purpose` typed section. The meta-statement describes the system prompt document itself, while the typed section defines the AI's purpose. These are distinct.

### 4. Protocol Section (Typed Subsection)

**MUST conform to:** `v:spec:protocol`

**Format:**
```markdown
## Protocol

[All required sections from v:spec:protocol:]

### Workflow Overview
...

### Phase Definitions
...

### User Collaboration Points
...

### Quality Assurance
...

### Consistent Principles
...
```

**Requirements:**
- This section MUST contain ALL required sections from [v:spec:protocol](v:spec:protocol)
- This section MUST verify against the protocol specification
- Subsection headers MUST be level 3 (###) under the level 2 (##) Protocol header

## Required Body Sections (continued)

### 5. Integration Validation

Confirmation that the three components work together coherently.

**Format:**
```markdown
## Integration Validation

### Component Alignment

**Persona ↔ Purpose:** [How persona expertise enables purpose objectives]

**Purpose ↔ Protocol:** [How protocol achieves purpose deliverables]

**Persona ↔ Protocol:** [How protocol reflects persona's approach]

### Consistency Checks

- ✅ Tone is consistent across all components
- ✅ No contradictions between boundaries and constraints
- ✅ Expertise supports objectives
- ✅ Protocol phases achieve deliverables
```

**Requirements:**
- MUST explicitly validate alignment between components
- MUST check for contradictions
- MUST confirm tone consistency
- SHOULD use checklist format

## Optional Body Sections

### Use Cases

Scenarios where this system prompt is appropriate.

**Format:**
```markdown
## Use Cases

- [Use case 1]
- [Use case 2]
```

### Deployment Notes

Practical considerations for using this system prompt.

**Format:**
```markdown
## Deployment Notes

### Model Compatibility
[Which models this works with]

### Known Limitations
[Practical constraints]

### Performance Characteristics
[Expected behavior]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/system_prompt`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:system_prompt:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, system_prompt]`
5. **Dependencies Field:** MUST list `[v:spec:persona, v:spec:purpose, v:spec:protocol]`

## Compositional Requirements

**Critical Pattern:** System prompts demonstrate **typed subsections** - sections that must conform to other specifications.

### Verification Strategy

1. **Document-level verification:** Check system_prompt structure (this spec)
2. **Subsection-level verification:**
   - Extract Persona section → verify against v:spec:persona
   - Extract Purpose section → verify against v:spec:purpose
   - Extract Protocol section → verify against v:spec:protocol
3. **Integration validation:** Check component alignment (no contradictions)

### Analogies

This pattern is analogous to:
- **JSON-LD context:** Typing fields with schemas
- **Type systems:** Declaring field types
- **Schema composition:** Combining schemas with constraints

## Content Requirements

1. **Complete PPP Structure:** All three components (Persona, Purpose, Protocol) must be present
2. **Component Conformance:** Each component must satisfy its spec
3. **Integration:** Components must align and not contradict
4. **Tone Consistency:** Tone in Persona must be maintained throughout
5. **Purpose-Driven:** Purpose is the anchor - Persona and Protocol serve Purpose

## Verification vs. Validation

- **Verification** (against this spec):
  - Check all required sections present
  - Verify each typed subsection against its spec
  - Confirm dependencies declared
  - Validate integration checks present

- **Validation** (against guidance-for-system-prompt):
  - Qualitative assessment of component integration
  - Evaluation of coherence and usability
  - Assessment of tone consistency

## Schema Summary

```yaml
# Required frontmatter
type: vertex/system_prompt
extends: doc
id: v:system_prompt:<name>
name: <string>
tags: [vertex, doc, system_prompt]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies:
  - v:spec:persona
  - v:spec:purpose
  - v:spec:protocol

# Optional frontmatter
description: <string>
domain: <string>
model_target: <string>
intended_use: <string>

# Required body sections (markdown)
## Purpose (meta-statement about this document)

## Persona (typed subsection: conforms to v:spec:persona)
  ### Role and Identity
  ### Domain Expertise
  ### Approach and Methodology
  ### Communication Tone
  ### Boundaries and Limitations

## Purpose (typed subsection: conforms to v:spec:purpose)
  ### Problem Statement
  ### Core Objectives
  ### Specific Deliverables
  ### Constraints and Boundaries
  ### Success Criteria

## Protocol (typed subsection: conforms to v:spec:protocol)
  ### Workflow Overview
  ### Phase Definitions
  ### User Collaboration Points
  ### Quality Assurance
  ### Consistent Principles

## Integration Validation
  ### Component Alignment
  ### Consistency Checks

# Optional body sections
## Use Cases
## Deployment Notes
```

## Compliance

A document claiming `type: vertex/system_prompt` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. Dependencies field lists all three specs: persona, purpose, protocol
3. Persona section conforms to v:spec:persona
4. Purpose section conforms to v:spec:purpose
5. Protocol section conforms to v:spec:protocol
6. Integration Validation section present with alignment checks
7. Type constraints are satisfied
8. No contradictions between components

## Pattern Significance

**This spec establishes the compositional document pattern:**

- Documents can have **typed subsections** that must conform to other specs
- Subsection types are declared via `dependencies` field
- Verification requires checking both document structure AND subsection conformance
- This enables modular, reusable document components
- Analogous to typing fields in schemas or contexts in JSON-LD

**This pattern can be extended to other compositional document types.**

---

**Note:** This specification demonstrates advanced compositional structure where subsections are typed with references to other specifications. System prompts are composed of three typed sections (Persona, Purpose, Protocol), making them schema-like documents that combine multiple spec types.
