---
type: vertex/spec
extends: doc
id: v:spec:guidance
name: Specification for Guidance Documents
description: Defines what makes a valid guidance document in the knowledge complex
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T16:00:00Z
modified: 2025-12-27T16:00:00Z
dependencies: []
---

# Specification for Guidance Documents

**This specification defines the structure and requirements for all guidance documents in the knowledge complex.**

## Purpose

Guidance documents define **quality criteria** and **best practices** - the "how well" of documentation. This spec-for-guidance establishes what fields, sections, and properties must be present in any valid guidance document.

## Required Frontmatter Fields

All guidance documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/guidance` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:guidance:<name>`) |
| `name` | string | REQUIRED | Human-readable guidance name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, guidance]` in full inheritance chain |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of guidance purpose |
| `criteria` | array[string] | OPTIONAL | Enumerated quality criteria names |
| `rubric` | object | OPTIONAL | Structured scoring rubric |

## Required Body Sections

The markdown body of a guidance document MUST contain:

### 1. Purpose Statement

A clear statement of what the guidance helps evaluate and why it exists.

**Format:**
```markdown
## Purpose

[1-3 sentences explaining what this guidance helps assess]
```

### 2. Document Overview

Context about what template or document type this guidance supports.

**Format:**
```markdown
## Document Overview

### What This Guidance Covers

[Description of supported document type]

### Best Use Cases

[List of 3-5 scenarios where this guidance applies]
```

### 3. Quality Criteria

Leveled assessment criteria for evaluating document quality.

**Format:**
```markdown
## Quality Criteria

### [Criterion Name]

**Excellent:** [Description of excellent quality]
**Good:** [Description of good quality]
**Needs Improvement:** [Description of inadequate quality]
```

**Requirements:**
- MUST have at least 3 distinct criteria
- Each criterion MUST have at least 2 quality levels defined
- Criteria SHOULD use consistent level names (e.g., Excellent/Good/Needs Improvement)

### 4. Section-by-Section Guidance

Practical advice for completing each section of the supported document type.

**Format:**
```markdown
## Section-by-Section Guidance

### [Section Name]

**Purpose:** [Why this section exists]

**Tips:**
- [Specific actionable tip]
- [Another tip]

**Anti-patterns:**
- ❌ [What not to do]
- ✅ [What to do instead]
```

**Requirements:**
- MUST provide guidance for each major section of the supported document type
- Tips MUST be specific and actionable (not vague advice)

## Required or Recommended Body Sections

### 5. Workflow Guidance

Recommended order for completing the supported document type.

**Format:**
```markdown
## Workflow Guidance

### Recommended Authoring Sequence

1. **[Step Name]** ([time estimate])
   - [Description]
   - [What to accomplish]

### Quality Checkpoints

- **After step N:** [Checkpoint question]
```

**Requirement:** RECOMMENDED (strongly encouraged)

### 6. Common Issues and Solutions

Anti-patterns and their remedies.

**Format:**
```markdown
## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| [Issue name] | [What goes wrong] | [How to fix it] |
```

**Requirement:** RECOMMENDED

### 7. Best Practices

Actionable practices for creating excellent instances.

**Format:**
```markdown
## Best Practices

1. [Practice 1]
2. [Practice 2]
...
```

**Requirements:**
- RECOMMENDED
- If present, MUST include at least 5 practices
- Practices MUST be actionable (not abstract principles)

## Optional Body Sections

### Examples

References to excellent example documents.

**Format:**
```markdown
## Examples

| Document Name | Purpose | Key Features |
|---------------|---------|--------------|
| [Name] | [What it does] | [Why it's exemplary] |
```

### Validation vs. Verification

Distinction between qualitative assessment (validation) and structural checking (verification).

**Format:**
```markdown
## Validation vs. Verification

**Verification** (deterministic):
- [Structural checks]

**Validation** (qualitative):
- [Quality assessments]
```

### Tooling Support

Available tools for working with this guidance.

**Format:**
```markdown
## Tooling Support

### Verification Commands

\`\`\`bash
# Example commands
\`\`\`

### Validation Support

[Description of validation tools or processes]
```

### Self-Consistency Check

For meta-guidances: demonstrate self-validation.

**Format:**
```markdown
## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

✓ [Criterion met]
✓ [Another criterion met]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/guidance`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:guidance:[kebab-case-name]`
4. **Tag Inheritance:** Tags MUST include full chain: `[vertex, doc, guidance]`

## Content Requirements

1. **Descriptive Language:** Guidances use descriptive/evaluative language (should, excellent, poor)
2. **Quality Focus:** Guidances define assessment criteria, not structure
3. **Leveled Criteria:** Quality should be assessed on spectrum (not just pass/fail)
4. **Actionable:** Advice must be specific enough to follow

## Coupling Requirement

Every guidance SHOULD be paired with a corresponding spec document via a `coupling` edge. The spec defines structural requirements while this guidance defines quality assessment.

## Self-Reference

This specification is itself an instance of type `vertex/spec` and defines the structure for documents of type `vertex/guidance`.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that structural requirements are met
- **Validation** (against guidance-for-guidance): Qualitative assessment of guidance document quality

## Schema Summary

```yaml
# Required frontmatter
type: vertex/guidance
extends: doc
id: v:guidance:<name>
name: <string>
tags: [vertex, doc, guidance]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Optional frontmatter
description: <string>
criteria: [<criterion-names>]
rubric: {...}

# Required body sections (markdown)
## Purpose
## Document Overview
  ### What This Guidance Covers
  ### Best Use Cases
## Quality Criteria (≥3 criteria, ≥2 levels each)
  ### [Criterion Name]
    **Excellent:** ...
    **Good:** ...
    **Needs Improvement:** ...
## Section-by-Section Guidance

# Recommended body sections
## Workflow Guidance
## Common Issues and Solutions
## Best Practices (≥5 if present)

# Optional body sections
## Examples
## Validation vs. Verification
## Tooling Support
## Self-Consistency
```

## Compliance

A document claiming `type: vertex/guidance` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Quality Criteria section has ≥3 criteria with ≥2 levels each
4. Section-by-Section Guidance provides specific, actionable advice
5. Type constraints are satisfied
6. Content uses descriptive/evaluative language focused on quality

---

**Note:** This specification defines the structure for guidance documents, including guidance-for-guidance, demonstrating the spec/guidance symmetry in the knowledge complex.
