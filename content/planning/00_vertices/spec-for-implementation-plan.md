---
type: vertex/spec
extends: doc
id: v:spec:implementation-plan
name: Specification for Implementation Plan Documents
description: Defines structural requirements for implementation plan documents that guide human-AI collaboration through single-use development tasks
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-12T00:00:00Z
modified: 2025-01-12T00:00:00Z
dependencies: []
---

# Specification for Implementation Plan Documents

**This specification defines the structure and requirements for implementation plan documents that guide humans and AI assistants through single-use development tasks with explicit capability attribution.**

## Purpose

Implementation plan documents answer the question: "How do we execute this specific development task?" They provide step-by-step guidance for practitioners working with AI assistants (like Claude Code) on tasks such as refactors, feature implementations, bug fixes, and migrations.

Unlike runbooks (which are reusable workflows producing multiple artifacts), implementation plans are **single-use execution plans** for specific tasks. They include:

1. **Objective:** Clear goal, motivation, and measurable success criteria
2. **Prerequisites:** What must be true before starting
3. **Steps:** Ordered actions with capability hints indicating human vs. AI execution
4. **Verification:** How to confirm the plan succeeded
5. **Rollback:** How to recover if something goes wrong

This document type is designed to:

- Enable effective human-AI collaboration on development tasks
- Provide clear attribution of who/what executes each step
- Track plan status through its lifecycle
- Support verification at each step
- Enable rollback from any failure point

## Required Frontmatter Fields

All implementation plan documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:impl-plan-<name>`) |
| `name` | string | REQUIRED | Human-readable plan name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, implementation-plan]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Implementation Plan-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `status` | enum | REQUIRED | Must be `draft`, `approved`, `in-progress`, `completed`, or `abandoned` |
| `plan_type` | enum | REQUIRED | Must be `refactor`, `feature`, `bugfix`, `migration`, `documentation`, or `infrastructure` |
| `target_chart` | string | REQUIRED | Reference to chart/system being modified (id or path) |
| `estimated_effort` | string | REQUIRED | Effort estimate (e.g., "2-4 hours", "1-2 days") |
| `step_count` | integer | REQUIRED | Number of steps in the plan (must be >= 2) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of what the plan accomplishes |
| `dependencies` | array[string] | RECOMMENDED | External dependencies (other plans, PRs, etc.) |
| `assignee` | string | OPTIONAL | Who is executing this plan |
| `due_date` | date | OPTIONAL | Target completion date (ISO 8601 date) |
| `related_issues` | array[string] | OPTIONAL | References to issues, tickets, or requirements |
| `risk_level` | enum | OPTIONAL | `low`, `medium`, or `high` - overall risk assessment |

## Required Body Sections

The markdown body of an implementation plan document MUST contain:

### 1. Objective

Establishes the goal, motivation, and success criteria for the plan.

**Format:**

```markdown
## Objective

### Goal

[Single sentence stating what this plan accomplishes]

### Motivation

[Why this work is being done - problem, opportunity, or requirement]

### Success Criteria

- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]
- [ ] [Measurable criterion 3]
```

**Requirements:**

- MUST include Goal as a single sentence
- MUST include Motivation explaining the "why"
- MUST include at least 3 success criteria as checkbox items
- Success criteria MUST be objectively verifiable

### 2. Prerequisites

What must be true before execution begins.

**Format:**

```markdown
## Prerequisites

### Required Access

- [ ] [Access requirement 1]
- [ ] [Access requirement 2]

### Required Knowledge

- [Knowledge area 1]
- [Knowledge area 2]

### Entry Checklist

- [ ] [Precondition 1 - e.g., "Branch created from main"]
- [ ] [Precondition 2 - e.g., "Tests passing on main"]
- [ ] [Precondition 3 - e.g., "Dependencies identified"]
```

**Requirements:**

- MUST include Entry Checklist as verifiable checkbox items
- SHOULD include Required Access and Required Knowledge subsections
- Entry Checklist MUST be completable before Step 1

### 3. Capability Hints Taxonomy

Documents the vocabulary for human vs. AI collaboration.

**Format:**

```markdown
## Capability Hints Taxonomy

This plan uses capability hints to indicate who should perform each step.

| Hint | Executor | Claude Role | Human Role |
|------|----------|-------------|------------|
| `automatable` | Claude | Execute fully | Review output |
| `verification-only` | Claude | Run checks, report results | Interpret failures |
| `human-judgment` | Human | Provide analysis/options | Make decision |
| `human-approval` | Both | Prepare artifacts | Approve/reject |
| `pair-programming` | Both | Suggest, implement | Guide, validate |
| `human-only` | Human | Document steps | Execute |
```

**Requirements:**

- MUST include the 6 standard capability hints defined above
- MAY include additional domain-specific hints if documented in this section
- Each step in the plan MUST use exactly one capability hint from this taxonomy

### 4. Steps

Ordered, actionable steps with capability hints.

**Format:**

```markdown
## Steps

### Step N: [Step Name]

**Description:** [Clear description of what this step accomplishes]

**Capability Hint:** `[capability-hint]`

**Inputs:**

- [Input 1 - artifact, information, or prior step output]

**Actions:**

1. [ ] [Specific action 1]
2. [ ] [Specific action 2]
3. [ ] [Specific action 3]

**Outputs:**

- [Output 1 - file, artifact, or state change]

**Verification:**

- [ ] [How to verify this step succeeded]

**Dependencies:** [Step N-1] | None
```

**Requirements:**

- MUST include at least 2 steps
- Each step MUST have: Description, Capability Hint, Actions, Verification
- Actions MUST be checkbox items (trackable)
- Each action MUST be specific enough to execute without interpretation
- Capability Hint MUST use vocabulary from the Capability Hints Taxonomy section
- Dependencies MUST reference prior steps by number or "None"
- SHOULD include Inputs and Outputs for clarity

### 5. Verification Checklist

Post-execution verification that the plan succeeded.

**Format:**

```markdown
## Verification Checklist

### Automated Checks

- [ ] [Automated check 1 - e.g., "All tests pass"]
- [ ] [Automated check 2 - e.g., "No type errors"]
- [ ] [Automated check 3 - e.g., "Linting passes"]

### Manual Verification

- [ ] [Manual check 1 - e.g., "Feature works as expected"]
- [ ] [Manual check 2 - e.g., "No regressions in related areas"]

### Documentation Updates

- [ ] [Doc update 1 - e.g., "README updated if needed"]
- [ ] [Doc update 2 - e.g., "CHANGELOG entry added"]
```

**Requirements:**

- MUST include Automated Checks section
- MUST include Manual Verification section
- SHOULD include Documentation Updates section
- All items MUST be checkbox format
- MUST trace back to Success Criteria in Objective section

### 6. Rollback Plan

How to undo changes if the plan fails or causes issues.

**Format:**

```markdown
## Rollback Plan

### Rollback Trigger

[When should rollback be initiated - e.g., "Tests fail after step 3", "Production errors detected"]

### Rollback Steps

1. [ ] [Rollback action 1]
2. [ ] [Rollback action 2]
3. [ ] [Rollback action 3]

### Post-Rollback Verification

- [ ] [Verification that system is restored]
```

**Requirements:**

- MUST include Rollback Trigger criteria
- MUST include at least 2 rollback steps
- MUST include Post-Rollback Verification
- Rollback steps SHOULD enable recovery from any step in the plan

## Optional Body Sections

### Risks and Mitigations

**Format:**

```markdown
## Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [How to mitigate] |
```

### Notes

**Format:**

```markdown
## Notes

### Design Decisions

- [Decision 1 and rationale]

### Open Questions

- [ ] [Question needing resolution]

### References

- [Link or reference 1]
```

### Execution Log

**Format:**

```markdown
## Execution Log

| Step | Started | Completed | Notes |
|------|---------|-----------|-------|
| 1 | [timestamp] | [timestamp] | [any notes] |
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:impl-plan-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `implementation-plan`
5. **Status Values:** MUST be one of: `draft`, `approved`, `in-progress`, `completed`, `abandoned`
6. **Plan Type Values:** MUST be one of: `refactor`, `feature`, `bugfix`, `migration`, `documentation`, `infrastructure`

## Content Requirements

1. **Actionability:** Every action MUST be executable without interpretation
2. **Checkboxes:** All actions and verifications MUST use checkbox format `- [ ]`
3. **Capability Attribution:** Every step MUST have exactly one capability hint
4. **Traceability:** Success criteria MUST trace to verification checklist
5. **Reversibility:** Rollback plan MUST cover recovery from any step
6. **Single-Use:** Implementation plans are for specific tasks (unlike runbooks which are reusable)
7. **Progression:** Steps MUST follow logical dependency order

## Distinction from Runbooks

| Aspect | Runbook | Implementation Plan |
|--------|---------|---------------------|
| **Purpose** | Reusable workflow guide | Single-use execution plan |
| **Scope** | Multiple artifacts over time | One specific task |
| **Audience** | Any practitioner | Assignee + AI assistant |
| **Collaboration** | Roles and skills | Capability hints (human vs. AI) |
| **Maintenance** | Maintained and versioned | Archived after completion |
| **Status** | Always "active" | Progresses through lifecycle |

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:impl-plan-<name>
name: <string>
tags: [vertex, doc, implementation-plan]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
status: draft | approved | in-progress | completed | abandoned
plan_type: refactor | feature | bugfix | migration | documentation | infrastructure
target_chart: <string>
estimated_effort: <string>
step_count: <integer >= 2>

# Optional frontmatter
description: <string>
dependencies: [<strings>]
assignee: <string>
due_date: <ISO8601-date>
related_issues: [<strings>]
risk_level: low | medium | high

# Required body sections
## Objective
  ### Goal
  ### Motivation
  ### Success Criteria (checklist, >= 3 items)
## Prerequisites
  ### Entry Checklist (checklist)
## Capability Hints Taxonomy (table with 6 standard hints)
## Steps
  ### Step 1: [Name]
    - Description
    - Capability Hint
    - Actions (checklist)
    - Verification (checklist)
    - Dependencies
  ### Step 2: [Name]
    - [same structure]
  ### [Additional Steps...]
## Verification Checklist
  ### Automated Checks (checklist)
  ### Manual Verification (checklist)
## Rollback Plan
  ### Rollback Trigger
  ### Rollback Steps (checklist)
  ### Post-Rollback Verification (checklist)

# Optional body sections
## Risks and Mitigations
## Notes
## Execution Log
```

## Compliance

A document claiming to be an implementation plan is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. `status` is one of the defined enum values
3. `plan_type` is one of the defined enum values
4. Objective section includes Goal, Motivation, and at least 3 Success Criteria
5. Prerequisites section includes Entry Checklist
6. Capability Hints Taxonomy section documents all 6 standard hints
7. At least 2 steps are defined with all required fields (Description, Capability Hint, Actions, Verification, Dependencies)
8. Every step has exactly one capability hint from the taxonomy
9. All actions and verifications use checkbox format
10. Verification Checklist includes Automated Checks and Manual Verification sections
11. Rollback Plan includes Trigger, Steps, and Post-Rollback Verification
12. Type constraints are satisfied

---

**Note:** This specification establishes implementation plans as single-use execution guides for human-AI collaboration on development tasks. They differ from runbooks by focusing on specific tasks rather than reusable workflows, and by using capability hints to explicitly attribute execution to humans, AI assistants, or collaborative effort.
