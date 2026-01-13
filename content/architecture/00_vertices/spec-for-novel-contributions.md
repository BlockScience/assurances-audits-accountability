---
type: vertex/spec
extends: doc
id: v:spec:novel-contributions
name: Specification for Novel Contributions Documents
description: Defines what makes a valid novel contributions document that enumerates and ranks research contributions
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T18:00:00Z
modified: 2025-12-30T18:00:00Z
dependencies: []
---

# Specification for Novel Contributions Documents

**This specification defines the structure and requirements for novel contributions documents that enumerate, characterize, and rank research contributions from a body of work.**

## Purpose

Novel contributions documents provide a structured inventory of intellectual contributions arising from research, development, or engineering work. They serve as authoritative references for paper writing, distinguishing what is genuinely new from what is incremental or implementation-focused. This spec establishes what fields, sections, and properties must be present in any valid novel contributions document.

## Required Frontmatter Fields

All novel contributions documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:novel-contributions-<context>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, novel-contributions]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Novel Contributions Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `context` | string | REQUIRED | Research context or project name |
| `contribution_count` | integer | REQUIRED | Total number of contributions enumerated |
| `novelty_levels` | array[string] | REQUIRED | Ordered list of novelty categories used |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of the research context |
| `target_venue` | string | OPTIONAL | Intended publication venue |
| `related_artifacts` | array[string] | OPTIONAL | IDs of related documents (architecture, paper, etc.) |
| `dependencies` | array[string] | OPTIONAL | Related novel contributions documents |

## Required Body Sections

The markdown body of a novel contributions document MUST contain:

### 1. Introduction

A brief overview of the research context and purpose of the contributions inventory.

**Format:**
```markdown
# [Document Title]

[1-3 paragraphs explaining:]
- What research/project generated these contributions
- Why this inventory is needed
- How contributions are organized/ranked
```

### 2. Contribution Entries

Each contribution MUST be documented as a separate section with the following structure:

**Format:**
```markdown
## [Rank]. [NOVELTY_LEVEL]: [Contribution Title]

**What:** [1-2 sentences describing the contribution]

**Why it's [novel/incremental/etc.]:**
- [Bullet points explaining novelty rationale]

**Evidence from [context]:**
- [Bullet points with concrete evidence]

**Projection to [target]:**
[How this contribution should be positioned in the target output]
```

**Requirements:**
- MUST include at least 3 contributions
- Each contribution MUST have: What, Why, Evidence, Projection sections
- Contributions MUST be numbered and ranked
- Novelty level MUST be explicitly stated in heading

### 3. Summary Table

A ranked summary of all contributions.

**Format:**
```markdown
## Summary: Contribution Hierarchy

| Rank | Contribution | Novelty | [Target] Treatment |
|------|--------------|---------|-------------------|
| 1 | [title] | [level] | [treatment] |
| 2 | [title] | [level] | [treatment] |
...
```

**Requirements:**
- MUST include all enumerated contributions
- MUST be ordered by rank
- MUST include novelty level for each
- MUST include recommended treatment for target output

### 4. Key Insights

Synthesis of patterns and recommendations for using the contributions.

**Format:**
```markdown
## Key Insights for [Target]

1. [Insight with rationale]
2. [Insight with rationale]
...
```

**Requirements:**
- MUST include at least 3 insights
- Insights SHOULD be actionable recommendations

## Novelty Level Definitions

Documents MUST use a consistent novelty classification. The following levels are RECOMMENDED:

| Level | Definition | Typical Treatment |
|-------|------------|-------------------|
| Highly Novel | First known formalization or application; significant departure from prior work | Central thesis, primary result |
| Novel | New combination, extension, or application of known concepts | Key innovation, supporting contribution |
| Moderately Novel | Adaptation of established practice to new domain | Accessible framing, background |
| Incremental | Implementation or execution of established approaches | Supporting material, mention briefly |
| Discovered | Limitations, gaps, or issues found during work | Future work, honest acknowledgment |

Custom novelty levels are permitted but MUST be defined in the document.

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:novel-contributions-[kebab-case-context]`
4. **Tag Requirement:** Tags MUST include `novel-contributions`

## Content Requirements

1. **Minimum Contributions:** Document MUST enumerate at least 3 distinct contributions
2. **Consistent Structure:** Each contribution entry MUST follow the required format
3. **Evidence-Based:** Each contribution MUST include concrete evidence
4. **Ranked:** Contributions MUST be explicitly ranked by novelty/importance
5. **Actionable:** Document MUST include guidance on how to use contributions

## Coupling Requirement

Every novel contributions document SHOULD be verified against this spec and validated against the corresponding `guidance-for-novel-contributions` document via appropriate edges. The guidance defines how to evaluate quality and fitness-for-purpose for novel contributions documents.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections and fields are present
- **Validation** (against guidance-for-novel-contributions): Qualitative assessment that the contributions are well-characterized, properly ranked, and fit-for-purpose

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:novel-contributions-<context>
name: <string>
tags: [vertex, doc, novel-contributions]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
context: <string>
contribution_count: <integer>
novelty_levels: [<string>, ...]

# Recommended frontmatter
description: <string>

# Optional frontmatter
target_venue: <string>
related_artifacts: [<vertex-ids>]
dependencies: [<related-docs>]

# Required body sections (markdown)
# Introduction (overview of context)
## [N]. [LEVEL]: [Contribution Title]
  **What:** ...
  **Why it's [level]:** ...
  **Evidence from [context]:** ...
  **Projection to [target]:** ...
## Summary: Contribution Hierarchy (table)
## Key Insights for [Target] (numbered list)
```

## Compliance

A document claiming to be a novel contributions document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. At least 3 contributions are enumerated with complete structure
4. Summary table includes all contributions with rank, novelty, and treatment
5. Key insights section includes at least 3 actionable insights
6. Type constraints are satisfied
7. Novelty levels are consistent (either standard or custom-defined)

---

**Note:** This specification enables structured documentation of research novelty, supporting systematic paper writing and contribution communication.
