---
type: vertex/spec
extends: doc
id: v:spec:persona
name: Specification for Persona Documents
description: Defines what makes a valid persona document - the identity, expertise, approach, tone, and boundaries of an AI model
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies: []
---

# Specification for Persona Documents

**This specification defines the structure and requirements for persona documents in the knowledge complex.**

## Purpose

Persona documents define **who the AI is** - its role, identity, expertise, approach, communication style, and boundaries. This spec establishes what fields and sections must be present in any valid persona document.

## Required Frontmatter Fields

All persona documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/persona` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:persona:<name>`) |
| `name` | string | REQUIRED | Human-readable persona name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, persona]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of persona |
| `domain` | string | OPTIONAL | Primary domain (e.g., `ai_model_design`, `education`) |

## Required Body Sections

The markdown body of a persona document MUST contain:

### 1. Purpose Statement

A clear statement of what this persona defines.

**Format:**
```markdown
## Purpose

This persona defines [role/identity description].
```

### 2. Role and Identity

Specific role and professional identity of the AI.

**Format:**
```markdown
## Role and Identity

[1-2 paragraphs defining who the AI is - specific role, professional identity, character]
```

**Requirements:**
- MUST be specific (not vague like "helpful assistant")
- MUST define professional identity
- SHOULD use active voice

### 3. Domain Expertise

Specific areas of knowledge and skill.

**Format:**
```markdown
## Domain Expertise

- [Specific expertise area 1]
- [Specific expertise area 2]
- [Specific expertise area 3]
- [Optional: Specific expertise area 4]
```

**Requirements:**
- MUST list 2-4 expertise areas
- Each area MUST be relevant and specific
- MUST use domain-appropriate terminology
- MUST NOT claim impossible breadth

### 4. Approach and Methodology

How the AI thinks and works.

**Format:**
```markdown
## Approach and Methodology

[Description of thinking style, analytical approach, working method]
```

**Requirements:**
- MUST describe HOW the AI thinks and works
- SHOULD use behavioral terms
- Examples: "systematic and evidence-based", "collaborative and iterative"

### 5. Communication Tone

How the AI communicates.

**Format:**
```markdown
## Communication Tone

[Description of tone, formality level, relationship with user]
```

**Requirements:**
- MUST specify tone (e.g., analytical, patient, professional, encouraging)
- MUST describe formality level
- MUST be appropriate for use case
- MUST be consistent with approach

### 6. Boundaries and Limitations

What the AI does NOT do or claim.

**Format:**
```markdown
## Boundaries and Limitations

- [Explicit limitation 1]
- [Explicit limitation 2]
- [Explicit limitation 3]
```

**Requirements:**
- MUST explicitly state limitations
- MUST define scope limits
- MUST acknowledge constraints
- SHOULD include at least 3 boundaries
- Examples: "does not provide legal advice", "acknowledges uncertainty when appropriate"

## Optional Body Sections

### Use Cases

Scenarios where this persona applies.

**Format:**
```markdown
## Use Cases

- [Use case 1]
- [Use case 2]
```

### Integration Notes

How this persona integrates with purpose and protocol.

**Format:**
```markdown
## Integration Notes

**With Purpose:** [How expertise enables purpose]
**With Protocol:** [How approach informs workflow]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/persona`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:persona:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, persona]`

## Content Requirements

1. **Specificity:** Persona must be specific and credible, not generic
2. **Coherence:** All elements (identity, expertise, approach, tone) must align
3. **Honesty:** Boundaries must be explicit and realistic
4. **Actionability:** Approach and tone must be clear enough to follow

## Compositional Usage

Persona documents are typically referenced as typed subsections in compositional documents:

```yaml
sections:
  - name: persona-section
    spec: v:spec:persona
    required: true
```

When used compositionally, the referencing document MUST include all required sections defined in this spec.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections are present
- **Validation** (against guidance-for-persona): Qualitative assessment of specificity, coherence, and credibility

## Schema Summary

```yaml
# Required frontmatter
type: vertex/persona
extends: doc
id: v:persona:<name>
name: <string>
tags: [vertex, doc, persona]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Optional frontmatter
description: <string>
domain: <string>

# Required body sections (markdown)
## Purpose
## Role and Identity
## Domain Expertise (2-4 items)
## Approach and Methodology
## Communication Tone
## Boundaries and Limitations (≥3 items)

# Optional body sections
## Use Cases
## Integration Notes
```

## Compliance

A document claiming `type: vertex/persona` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Domain Expertise lists 2-4 specific areas
4. Boundaries and Limitations lists at least 3 explicit limitations
5. Type constraints are satisfied
6. Role is specific and credible (not vague)

---

**Note:** This specification supports the PPP (Persona-Purpose-Protocol) framework by defining the structural requirements for persona components.
