---
type: vertex/spec
extends: doc
id: v:spec:runbook
name: Specification for Runbook Documents
description: Defines structural requirements for runbook documents that guide humans through multi-step workflows producing artifacts
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-04T16:00:00Z
modified: 2025-01-04T16:00:00Z
dependencies: []
---

# Specification for Runbook Documents

**This specification defines the structure and requirements for runbook documents that guide humans through multi-step workflows, pointing them to the right tools, documents, and decision points to accomplish their goals.**

## Purpose

Runbook documents answer the question: "How do I accomplish this goal?" They provide step-by-step guidance for practitioners working through workflows that produce multiple artifacts. Unlike lifecycle documents (which describe how an engineering object gets built and assured), runbooks describe how a human walks through a workflow—making decisions, using tools, creating documents, and reaching checkpoints along the way.

Runbooks have three parts:

1. **Context (Why, What, Who):** Problem being solved, artifacts produced, roles/skills required
2. **Workflow (How):** Ordered steps with dependencies, parallelization opportunities, consistency checkpoints
3. **Maintenance (Revisions & Reassurance):** How to update documents, propagate changes, and re-assure after modifications

This document type is designed to:
- Guide practitioners through multi-step workflows
- Reference appropriate specs, guidance, and tools at each step
- Document decision points, dependencies, and parallelization opportunities
- Define clear entry and exit criteria
- Track artifacts produced throughout the workflow
- Support ongoing maintenance, change propagation, and re-assurance

## Required Frontmatter Fields

All runbook documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:runbook-<name>`) |
| `name` | string | REQUIRED | Human-readable runbook name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, runbook]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Runbook-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `workflow_name` | string | REQUIRED | Name of the workflow this runbook guides |
| `target_roles` | array[string] | REQUIRED | Roles expected to perform this workflow (e.g., `[systems engineer, program manager]`) |
| `required_skills` | array[string] | REQUIRED | Skills needed to execute this workflow |
| `step_count` | integer | REQUIRED | Number of steps in the runbook (must be ≥2) |
| `artifacts_produced` | array[string] | REQUIRED | List of artifacts produced by completing the workflow |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of runbook purpose |
| `estimated_duration` | string | RECOMMENDED | Approximate time to complete (e.g., "2-4 hours", "1-2 days") |
| `parallel_steps` | array[array[string]] | RECOMMENDED | Groups of steps that can execute in parallel |
| `prerequisites` | array[string] | RECOMMENDED | Tools or access required before starting |
| `related_runbooks` | array[string] | OPTIONAL | References to related runbooks |

## Required Body Sections

The markdown body of a runbook document MUST contain:

### 1. Context (Why, What, Who)

Establishes the purpose, scope, and audience for the workflow.

**Format:**
```markdown
## Context

### Why: Problem Statement
[What problem does this workflow solve? What value does completing it deliver?]

### What: Scope and Artifacts
[What artifacts will be produced? What is in/out of scope?]

| Artifact | Type | Description |
|----------|------|-------------|
| [Artifact 1] | [doc type] | [brief description] |

### Who: Roles and Skills
[Who should execute this workflow? What skills are required?]

| Role | Responsibilities | Required Skills |
|------|------------------|-----------------|
| [Role 1] | [What they do] | [Skills needed] |
```

**Requirements:**

- MUST include Why (problem statement and value)
- MUST include What (artifacts produced with types)
- MUST include Who (roles and required skills)
- MUST match `target_roles` and `required_skills` in frontmatter
- SHOULD include time estimate

### 2. Prerequisites

What must be in place before starting the workflow.

**Format:**
```markdown
## Prerequisites

### Required Knowledge
- [Knowledge area 1]
- [Knowledge area 2]

### Required Tools
- [Tool 1]: [brief description of how it's used]
- [Tool 2]: [brief description of how it's used]

### Required Access
- [Access requirement 1]
- [Access requirement 2]

### Entry Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

**Requirements:**
- MUST include Entry Criteria as checklist
- SHOULD include Required Knowledge, Tools, and Access subsections
- Entry Criteria MUST be verifiable before starting

### 3. Workflow Overview

A visual representation of the workflow showing dependencies and parallelization.

**Format:**
```markdown
## Workflow Overview

### Dependency Diagram

\`\`\`mermaid
flowchart TB
    subgraph Phase1[Phase 1: Foundation]
        S1[Step 1: Architecture]
    end

    subgraph Phase2[Phase 2: Process & Plan]
        S2[Step 2: Lifecycle]
        S3[Step 3: Program Plan]
    end

    S1 --> S2
    S1 --> S3
    S2 -.-> S3

    %% Parallel indicator
    note1[Steps 2 & 3 can run in parallel]
\`\`\`

### Parallelization Opportunities

| Parallel Group | Steps | Condition |
|----------------|-------|-----------|
| [Group name] | [Step X, Step Y] | [When parallel execution is valid] |

### Workflow Summary

| Step | Activity | Inputs | Output | Depends On |
|------|----------|--------|--------|------------|
| 1 | [activity] | [inputs] | [artifact] | - |
| 2 | [activity] | [inputs] | [artifact] | Step 1 |
```

**Requirements:**

- MUST include a Mermaid diagram showing step dependencies
- MUST show which steps depend on which prior outputs
- MUST document parallelization opportunities (or state "None" if purely sequential)
- MUST include a summary table with dependencies column
- Diagram SHOULD use subgraphs to group related steps
- Diagram SHOULD indicate decision points if present

### 4. Step Definitions

Detailed guidance for each step in the workflow.

**Format:**
```markdown
## Step N: [Step Name]

**Goal:** [Single sentence stating what this step accomplishes]

**Inputs:**
- [Input 1 - artifact or information needed]
- [Input 2]

**Activities:**
1. [Activity 1 with specific guidance]
2. [Activity 2 with specific guidance]
3. [Activity N]

**Tools and References:**
- [[spec-for-X]] - Use for structural requirements
- [[guidance-for-X]] - Use for quality criteria
- `command` - Use for verification

**Outputs:**
- [Output 1 - artifact produced]
- [Output 2]

**Consistency Checks:**
- [ ] [Check alignment with earlier artifact]
- [ ] [Verify references to prior documents are accurate]

**Checkpoint:** [How to verify this step is complete]
```

**Requirements:**

- MUST include at least 2 steps
- Each step MUST have: Goal, Inputs, Activities, Tools and References, Outputs, Checkpoint
- Steps that depend on earlier artifacts MUST include Consistency Checks
- Consistency Checks MUST verify alignment with referenced documents
- Activities MUST be numbered and actionable
- Tools and References MUST point to specific documents or commands
- Checkpoint MUST be verifiable

### 5. Decision Points

Documentation of choices practitioners may face.

**Format:**
```markdown
## Decision Points

### Decision: [Decision Name]

**When:** [When this decision arises]

**Options:**

| Option | When to Choose | Implications |
|--------|----------------|--------------|
| [Option A] | [Conditions] | [What happens] |
| [Option B] | [Conditions] | [What happens] |

**Default:** [Recommended default if unclear]
```

**Requirements:**
- MUST document any branching paths in the workflow
- Each decision MUST have options with conditions and implications
- SHOULD provide a default recommendation
- MAY be marked "None" if workflow is purely linear

### 6. Completion Criteria

How to know the workflow is successfully complete.

**Format:**
```markdown
## Completion Criteria

### Exit Checklist
- [ ] [Artifact 1] exists and passes verification
- [ ] [Artifact 2] exists and passes verification
- [ ] [Final validation criterion]

### Success Indicators
- [Indicator 1]
- [Indicator 2]

### Common Completion Issues
| Issue | Resolution |
|-------|------------|
| [Issue 1] | [How to resolve] |
```

**Requirements:**
- MUST include Exit Checklist as verifiable items
- MUST map back to artifacts_produced in frontmatter
- SHOULD include Success Indicators
- SHOULD include Common Completion Issues

### 7. Troubleshooting

Guidance for common problems.

**Format:**
```markdown
## Troubleshooting

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| [Problem 1] | [Cause] | [Solution] |
| [Problem 2] | [Cause] | [Solution] |
```

**Requirements:**

- MUST include at least 3 common problems with solutions
- Problems SHOULD be specific to this workflow
- Solutions SHOULD reference specific steps or tools

### 8. Maintenance (Revisions & Reassurance)

How to update documents after initial completion and maintain currency, traceability, and accountability.

**Format:**
```markdown
## Maintenance

### When to Revisit

| Trigger | Affected Artifacts | Action Required |
|---------|-------------------|-----------------|
| [Trigger event] | [Which artifacts] | [What to do] |

### Change Propagation

When earlier documents change, updates may need to propagate forward:

| If Changed | Then Review | Propagation Steps |
|------------|-------------|-------------------|
| [Artifact A] | [Artifacts B, C] | [Specific steps to update] |

### Regression Testing

After changes, verify consistency using specs and guidance:

1. [Verification step using spec]
2. [Validation step using guidance]
3. [Cross-document consistency check]

### Re-Assurance Protocol

When documents are updated, re-assurance may be required:

| Change Type | Re-Assurance Required | Process |
|-------------|----------------------|---------|
| Minor (typos, formatting) | No | Update `modified` timestamp only |
| Moderate (content changes within scope) | Verification only | Re-run verification, update edges |
| Major (scope or structure changes) | Full re-assurance | Re-verify, re-validate, update assurance faces |

### Currency Tracking

| Artifact | Current Version | Last Verified | Owner |
|----------|-----------------|---------------|-------|
| [Artifact 1] | [version] | [date] | [who] |
```

**Requirements:**

- MUST document triggers for revisiting completed workflows
- MUST describe how changes propagate between dependent artifacts
- MUST include regression testing steps using specs and guidance
- MUST define re-assurance protocol for different change types
- SHOULD include currency tracking table template

## Optional Body Sections

### Quick Reference

Condensed reference for experienced practitioners.

**Format:**
```markdown
## Quick Reference

| Step | Command/Action | Verify With |
|------|----------------|-------------|
| 1 | [action] | [verification] |
```

### Examples

Links to completed examples of this workflow.

**Format:**
```markdown
## Examples

| Example | Description | Artifacts |
|---------|-------------|-----------|
| [Example 1] | [What it demonstrates] | [Links to artifacts] |
```

### Related Workflows

Connections to other runbooks.

**Format:**
```markdown
## Related Workflows

- [[runbook-X]] - [When to use instead or in addition]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:runbook-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `runbook`

## Content Requirements

1. **Human-Centered:** Runbooks guide human practitioners, not automated processes
2. **Actionable:** Every activity must be specific enough to execute
3. **Referenced:** Each step must point to relevant specs, guidance, or tools
4. **Checkpointed:** Every step must have a verifiable completion criterion
5. **Consistent:** Steps that depend on earlier artifacts must verify alignment
6. **Complete:** All artifacts in frontmatter must be produced by steps
7. **Navigable:** Practitioners can find where they are and what's next
8. **Maintainable:** Change propagation and re-assurance protocols are documented

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:runbook-<name>
name: <string>
tags: [vertex, doc, runbook]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
workflow_name: <string>
target_roles: [<strings>]
required_skills: [<strings>]
step_count: <integer ≥2>
artifacts_produced: [<strings>]

# Optional frontmatter
description: <string>
estimated_duration: <string>
parallel_steps: [[<step-ids>]]
prerequisites: [<strings>]
related_runbooks: [<strings>]

# Required body sections
## Context
  ### Why: Problem Statement
  ### What: Scope and Artifacts
  ### Who: Roles and Skills
## Prerequisites
  ### Entry Criteria (checklist)
## Workflow Overview
  ### Dependency Diagram (Mermaid)
  ### Parallelization Opportunities
  ### Workflow Summary (table with dependencies)
## Step 1: [Name]
  - Goal, Inputs, Activities, Tools and References, Outputs
  - Consistency Checks (for dependent steps)
  - Checkpoint
## Step 2: [Name]
  - [same structure]
## [Additional Steps...]
## Decision Points
## Completion Criteria
  ### Exit Checklist
## Troubleshooting
## Maintenance
  ### When to Revisit
  ### Change Propagation
  ### Regression Testing
  ### Re-Assurance Protocol

# Optional body sections
## Quick Reference
## Examples
## Related Workflows
```

## Compliance

A document claiming to be a runbook document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed (including `target_roles` and `required_skills`)
2. Context section includes Why, What, and Who subsections
3. At least 2 steps are defined with Goal, Inputs, Activities, Tools and References, Outputs, Checkpoint
4. A Mermaid dependency diagram is present showing step dependencies
5. Parallelization opportunities are documented (or explicitly stated as "None")
6. Steps with dependencies include Consistency Checks
7. Entry Criteria and Exit Checklist are present as checklists
8. All artifacts in `artifacts_produced` are outputs of at least one step
9. At least 3 troubleshooting entries are documented
10. Maintenance section includes When to Revisit, Change Propagation, Regression Testing, and Re-Assurance Protocol
11. Type constraints are satisfied

---

**Note:** This specification establishes runbooks as human-activity guides that walk practitioners through multi-step workflows. Runbooks have three parts: Context (why, what, who), Workflow (how, with dependencies and parallelization), and Maintenance (revisions and re-assurance). They reference lifecycle documents, specs, and guidance but serve a different purpose: helping humans accomplish goals and maintain artifact currency over time.
