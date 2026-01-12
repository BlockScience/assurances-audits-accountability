---
type: vertex/spec
extends: doc
id: v:spec:branch-review
name: Specification for Branch Review Documents
description: Defines structural requirements for branch review documents that document a reviewer's assertions about a particular branch in a particular context
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-12T00:00:00Z
modified: 2025-01-12T00:00:00Z
dependencies: []
---

# Specification for Branch Review Documents

**This specification defines the structure and requirements for branch review documents that capture a reviewer's systematic analysis and assertions about changes in a git branch relative to a base branch, within a defined review context.**

## Purpose

Branch review documents answer the question: "What can we assert about this branch?" They provide a structured framework for documenting a reviewer's analysis of changes in a branch, capturing observations, findings, assertions, and recommendations within a specific review context (e.g., architecture review, quality audit, competitive analysis).

Branch reviews are self-describing documents where each instance defines its own:
- **Review Purpose:** Why this review is being conducted
- **Review Scope:** What branch and boundaries are being examined
- **Review Context:** The lens or perspective through which changes are analyzed

This document type is designed to:
- Capture systematic analysis of branch changes
- Document reviewer assertions with supporting evidence
- Enable multiple review perspectives on the same branch
- Provide actionable recommendations
- Maintain accountability for review conclusions

## Required Frontmatter Fields

All branch review documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:branch-review-<name>`) |
| `name` | string | REQUIRED | Human-readable review name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, branch-review]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Branch-Review Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `repository` | string | REQUIRED | Repository URL or name being reviewed |
| `branch_name` | string | REQUIRED | Name of the branch being reviewed |
| `base_branch` | string | REQUIRED | Comparison base (typically `main` or `master`) |
| `review_date` | date | REQUIRED | Date when review was conducted (ISO 8601 date) |
| `reviewer` | string | REQUIRED | Who performed the review (person or entity) |
| `commit_range` | string | REQUIRED | Commit range in format `<base>..<head>` |
| `files_changed` | integer | REQUIRED | Number of files changed in the branch |
| `commits_count` | integer | REQUIRED | Number of commits in the branch |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of review purpose |
| `review_context_type` | string | RECOMMENDED | Type of review (e.g., `architecture`, `quality-audit`, `competitive-analysis`) |
| `prior_review_ref` | string | OPTIONAL | Reference to prior review of same branch |
| `related_reviews` | array[string] | OPTIONAL | References to related reviews |

## Required Body Sections

The markdown body of a branch review document MUST contain:

### 1. Review Purpose

Establishes why this review is being conducted and what questions it aims to answer.

**Format:**
```markdown
## Review Purpose

### Why This Review

[1-2 paragraphs explaining:
- What motivated this review
- What decisions or actions depend on it
- What value the review provides]

### Key Questions

This review aims to answer:

1. [Question about changes]
2. [Question about quality/architecture/etc.]
3. [Question about implications]
```

**Requirements:**
- MUST explain why the review is being conducted
- MUST list at least 3 key questions the review aims to answer
- SHOULD connect to downstream decisions or actions

### 2. Review Scope

Defines the boundaries of what is being reviewed.

**Format:**
```markdown
## Review Scope

### Branch Information

| Property | Value |
|----------|-------|
| Repository | [repo-url-or-name] |
| Branch | [branch-name] |
| Base | [base-branch] |
| Commit Range | [base-sha]..[head-sha] |
| Files Changed | [count] |
| Commits | [count] |

### In Scope

The following are explicitly within the scope of this review:

- [In-scope item 1]
- [In-scope item 2]

### Out of Scope

The following are explicitly outside the scope of this review:

- [Out-of-scope item 1]
- [Out-of-scope item 2]
```

**Requirements:**
- MUST include Branch Information table matching frontmatter
- MUST include In Scope list (at least 2 items)
- MUST include Out of Scope list (at least 1 item)

### 3. Review Context

Defines the lens or perspective through which changes are being analyzed.

**Format:**
```markdown
## Review Context

### Review Type

[Name of review type: e.g., Architecture Review, Quality Audit, Competitive Analysis]

### Perspective

[1-2 paragraphs explaining:
- What perspective or lens is being applied
- What criteria or standards are being used
- What expertise or knowledge informs this review]

### Evaluation Criteria

This review evaluates changes against:

| Criterion | Description |
|-----------|-------------|
| [Criterion 1] | [What it measures] |
| [Criterion 2] | [What it measures] |
```

**Requirements:**
- MUST identify the review type
- MUST explain the perspective being applied
- MUST list at least 2 evaluation criteria with descriptions

### 4. Branch Overview

Provides a high-level summary of what changed in the branch.

**Format:**
```markdown
## Branch Overview

### Summary

[1-3 paragraphs providing a narrative summary of:
- What the branch accomplishes
- Key themes or patterns in the changes
- Overall scope and complexity]

### Key Commits

| Commit | Message | Significance |
|--------|---------|--------------|
| [short-sha] | [message] | [why it matters] |

### Change Statistics

| Category | Count | Description |
|----------|-------|-------------|
| [Category 1] | [n] | [brief description] |
```

**Requirements:**
- MUST include a narrative summary
- MUST list at least 3 key commits with significance
- SHOULD include change statistics by category

### 5. Change Inventory

Systematic listing of changes by category.

**Format:**
```markdown
## Change Inventory

### [Category 1] (e.g., Vertices, Scripts, etc.)

| File | Change Type | Description |
|------|-------------|-------------|
| [path] | Added/Modified/Deleted | [brief description] |

### [Category 2]

| File | Change Type | Description |
|------|-------------|-------------|
| [path] | Added/Modified/Deleted | [brief description] |
```

**Requirements:**
- MUST organize changes into at least 2 categories
- MUST list each changed file with change type and description
- Categories SHOULD reflect the structure of the repository

### 6. Analysis

Observations, patterns, and implications from reviewing the changes.

**Format:**
```markdown
## Analysis

### Observations

1. [Observation about pattern or theme]
2. [Observation about quality or structure]
3. [Observation about implications]

### Patterns Identified

| Pattern | Evidence | Implication |
|---------|----------|-------------|
| [Pattern 1] | [Where observed] | [What it means] |

### Gaps and Concerns

| Gap/Concern | Description | Severity |
|-------------|-------------|----------|
| [Item 1] | [What is missing or concerning] | High/Medium/Low |
```

**Requirements:**
- MUST include at least 3 observations
- SHOULD identify patterns with evidence
- SHOULD document gaps or concerns if present (or state "None identified")

### 7. Assertions

The reviewer's claims about the branch - the core deliverable of the review.

**Format:**
```markdown
## Assertions

### Summary Assertion

[1-2 sentences stating the overall conclusion of this review]

### Specific Assertions

| ID | Assertion | Confidence | Evidence |
|----|-----------|------------|----------|
| A1 | [Claim about the branch] | High/Medium/Low | [Supporting evidence reference] |
| A2 | [Claim about the branch] | High/Medium/Low | [Supporting evidence reference] |

### Assertion Rationale

#### A1: [Assertion title]

[2-3 sentences explaining the reasoning behind this assertion]

#### A2: [Assertion title]

[2-3 sentences explaining the reasoning behind this assertion]
```

**Requirements:**
- MUST include a summary assertion (overall conclusion)
- MUST include at least 2 specific assertions with confidence levels
- MUST provide rationale for each assertion
- Confidence levels MUST be one of: `High`, `Medium`, `Low`

### 8. Recommendations

Actions suggested based on the review.

**Format:**
```markdown
## Recommendations

### Primary Recommendation

[Clear statement of the main recommended action]

### Specific Recommendations

| Priority | Recommendation | Rationale |
|----------|----------------|-----------|
| 1 | [Action to take] | [Why] |
| 2 | [Action to take] | [Why] |

### Conditional Recommendations

If [condition], then [recommendation].
```

**Requirements:**
- MUST include a primary recommendation
- MUST include at least 2 specific recommendations with rationale
- MAY include conditional recommendations

### 9. Accountability

Documents who conducted the review and under what authority.

**Format:**
```markdown
## Accountability

### Review Conducted By

| Role | Entity | Date |
|------|--------|------|
| Reviewer | [name/entity] | [date] |
| Approver | [name/entity] | [date] |

### Review Method

[Description of how the review was conducted: manual analysis, tool-assisted, LLM-assisted, etc.]

### Limitations

[Any limitations of the review that readers should be aware of]
```

**Requirements:**
- MUST identify the reviewer
- MUST describe the review method
- SHOULD document limitations

## Optional Body Sections

### Prior Reviews

If this review updates or supersedes a prior review.

**Format:**
```markdown
## Prior Reviews

| Review | Date | Relationship |
|--------|------|--------------|
| [[prior-review]] | [date] | Updates/Supersedes/Extends |
```

### Appendices

Supporting material too detailed for main sections.

**Format:**
```markdown
## Appendices

### Appendix A: [Title]

[Detailed supporting material]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:branch-review-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `branch-review`

## Content Requirements

1. **Objectivity:** Observations and assertions must be clearly distinguished
2. **Traceability:** Assertions must link to evidence in change inventory or analysis
3. **Context-Bounded:** Analysis must stay within the stated review scope and context
4. **Accountability:** Review must clearly identify who conducted it and how
5. **Actionability:** Recommendations must be specific enough to act upon
6. **Self-Describing:** Each instance defines its own purpose, scope, and context

## Coupling Requirement

Every branch review document SHOULD be:
1. Verified against this spec for structural compliance
2. Validated against `guidance-for-branch-review` for quality
3. May be referenced by subsequent reviews or decisions

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, fields, and structural elements are present
- **Validation** (against guidance-for-branch-review): Qualitative assessment of whether the review effectively answers its stated questions within its context

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:branch-review-<name>
name: <string>
tags: [vertex, doc, branch-review]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
repository: <string>
branch_name: <string>
base_branch: <string>
review_date: <date>
reviewer: <string>
commit_range: <string>
files_changed: <integer>
commits_count: <integer>

# Optional frontmatter
description: <string>
review_context_type: <string>
prior_review_ref: <string>
related_reviews: [<strings>]

# Required body sections
## Review Purpose
  ### Why This Review
  ### Key Questions (≥3)
## Review Scope
  ### Branch Information (table)
  ### In Scope (≥2 items)
  ### Out of Scope (≥1 item)
## Review Context
  ### Review Type
  ### Perspective
  ### Evaluation Criteria (≥2)
## Branch Overview
  ### Summary
  ### Key Commits (≥3)
  ### Change Statistics
## Change Inventory
  ### [Categories] (≥2 categories with file tables)
## Analysis
  ### Observations (≥3)
  ### Patterns Identified
  ### Gaps and Concerns
## Assertions
  ### Summary Assertion
  ### Specific Assertions (≥2 with confidence)
  ### Assertion Rationale
## Recommendations
  ### Primary Recommendation
  ### Specific Recommendations (≥2)
## Accountability
  ### Review Conducted By
  ### Review Method
  ### Limitations

# Optional body sections
## Prior Reviews
## Appendices
```

## Compliance

A document claiming to be a branch review document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with their subsections
3. Minimum counts are satisfied (3 key questions, 2 in-scope items, 2 criteria, 3 commits, 3 observations, 2 assertions, 2 recommendations)
4. Type constraints are satisfied
5. Assertions include confidence levels and rationale
6. Accountability section identifies reviewer and method

---

**Note:** This specification establishes branch reviews as self-describing analytical documents. Each instance defines its own review purpose, scope, and context, enabling multiple perspectives on the same branch while maintaining structural consistency for verification and validation.
