---
type: vertex/spec
extends: doc
id: v:spec:lifecycle
name: Specification for Lifecycle Documents
description: Defines structural requirements for engineering lifecycle process documents describing assured document development workflows
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T18:00:00Z
modified: 2025-12-30T18:00:00Z
dependencies:
  - v:spec:architecture
---

# Specification for Lifecycle Documents

**This specification defines the structure and requirements for engineering lifecycle documents that describe workflows for developing assured documents within the typed simplicial complex framework.**

## Purpose

Lifecycle documents describe the systematic process—the "algorithm"—for developing documents that achieve assurance. They capture the phases, inputs, outputs, decision points, and verification/validation gates that transform requirements into assured artifacts. This spec establishes what fields, sections, and properties must be present in any valid lifecycle document.

## Required Frontmatter Fields

All lifecycle documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:lifecycle-<name>`) |
| `name` | string | REQUIRED | Human-readable lifecycle document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, lifecycle]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Lifecycle-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `lifecycle_name` | string | REQUIRED | Name of the lifecycle being documented |
| `target_artifact` | string | REQUIRED | What artifact type this lifecycle produces |
| `phase_count` | integer | REQUIRED | Number of phases in the lifecycle (must be ≥2) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of lifecycle purpose |
| `foundation_requirements` | array[string] | RECOMMENDED | Pre-existing assured documents required |
| `parallel_phases` | array[array[string]] | OPTIONAL | Groups of phases that can execute in parallel |

## Required Body Sections

The markdown body of a lifecycle document MUST contain:

### 1. Introduction

A clear statement of what lifecycle this document describes and what it produces.

**Format:**
```markdown
## Introduction

[1-3 paragraphs explaining:
- What this lifecycle produces
- Why this lifecycle exists (what problem it solves)
- How it relates to the assurance framework]
```

**Requirements:**
- MUST state the target artifact type
- MUST explain the lifecycle's purpose
- MUST reference the assurance framework context

### 2. Foundation/Prerequisites

Explicit documentation of assumed pre-existing elements.

**Format:**
```markdown
## Foundation / Prerequisites

[Description of what must exist before this lifecycle begins]

| Element | Type | Purpose |
|---------|------|---------|
| [element-1] | [type] | [why it's needed] |
| [element-2] | [type] | [why it's needed] |
```

**Requirements:**
- MUST list all required pre-existing documents
- MUST specify the assurance status of prerequisites (e.g., "assumed assured")
- MUST explain why each prerequisite is necessary

### 3. Phase Definitions

Detailed description of each phase in the lifecycle.

**Format:**
```markdown
## Phase N: [Phase Name]

**Goal:** [Single sentence stating what this phase accomplishes]

**Inputs:**
- [Input 1]
- [Input 2]

**Process:**
1. [Step 1]
2. [Step 2]
3. [Step N]

**Outputs:**
- [Output 1]
- [Output 2]

**Verification/Validation Gates:**
- [Gate description with pass/fail criteria]
```

**Requirements:**
- MUST include at least 2 phases
- Each phase MUST have: Goal, Inputs, Process (numbered steps), Outputs
- Phases involving assurance MUST include Verification/Validation Gates
- MUST clearly distinguish verification (automated) from validation (human)

### 4. Flowchart Visualization

A visual representation of the lifecycle flow.

**Format:**
```markdown
## Lifecycle Flowchart

\`\`\`mermaid
flowchart TB
    [Mermaid diagram content]
\`\`\`
```

**Requirements:**
- MUST use Mermaid syntax
- MUST show all phases
- MUST show decision points (verify/validate gates)
- MUST show pass/fail paths
- SHOULD use subgraphs to group related elements
- SHOULD use color coding for different phase types

### 5. Narrative Walkthrough

Prose description of the lifecycle flow.

**Format:**
```markdown
## Narrative Walkthrough

### Step 1: [Step Name]
[Prose description of the first major step]

### Step 2: [Step Name]
[Prose description of the second major step]

[Continue for all major steps...]
```

**Requirements:**
- MUST cover all phases in prose form
- MUST explain the "why" behind key decisions
- MUST describe iteration patterns if applicable
- SHOULD connect phases to assurance concepts

### 6. Key Properties

Summary of important characteristics of the lifecycle.

**Format:**
```markdown
## Key Properties

### [Property 1 Name]
[Description of property and why it matters]

### [Property 2 Name]
[Description of property and why it matters]
```

**Requirements:**
- MUST include at least 3 key properties
- Properties SHOULD address: trust relationships, parallelism, iteration, human involvement, traceability

## Optional Body Sections

### V-Model Relationship

Maps the lifecycle to the engineering V-model.

**Format:**
```markdown
## Relationship to V-Model

| V-Model Phase | Lifecycle Phase | Activity |
|---------------|-----------------|----------|
| [V-phase] | [Lifecycle phase] | [Activity] |
```

### Accountability Statement

Documents who is responsible for the lifecycle documentation.

**Format:**
```markdown
## Accountability Statement

[Statement about authorship, LLM assistance if any, and human responsibility]
```

### Examples

Concrete instances that follow this lifecycle.

**Format:**
```markdown
## Examples

| Instance | Target Artifact | Phases Used |
|----------|-----------------|-------------|
| [name] | [artifact type] | [phases] |
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:lifecycle-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `lifecycle`

## Content Requirements

1. **Process-Focused:** Lifecycle documents describe workflows, not static structures
2. **Gate-Aware:** Verification and validation gates must be explicit
3. **Traceable:** Inputs and outputs must be traceable across phases
4. **Human-Aware:** Validation steps requiring human judgment must be identified
5. **Complete:** All phases from start to deliverable must be documented

## Coupling Requirement

Every lifecycle document SHOULD be verified against this spec and validated against the corresponding `guidance-for-lifecycle` document via appropriate edges. The guidance defines how to evaluate quality and fitness-for-purpose for lifecycle documents.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, phases, and elements are present
- **Validation** (against guidance-for-lifecycle): Qualitative assessment that the lifecycle is clear, complete, and fit-for-purpose

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:lifecycle-<name>
name: <string>
tags: [vertex, doc, lifecycle]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
lifecycle_name: <string>
target_artifact: <string>
phase_count: <integer ≥2>

# Optional frontmatter
description: <string>
foundation_requirements: [<document-ids>]
parallel_phases: [[<phase-names>]]

# Required body sections (markdown)
## Introduction
## Foundation / Prerequisites
## Phase 1: [Name]
  - Goal, Inputs, Process, Outputs, Gates
## Phase 2: [Name]
  - Goal, Inputs, Process, Outputs, Gates
## [Additional Phases...]
## Lifecycle Flowchart (mermaid)
## Narrative Walkthrough
## Key Properties

# Optional body sections
## Relationship to V-Model
## Accountability Statement
## Examples
```

## Compliance

A document claiming to be a lifecycle document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. At least 2 phases are defined with Goal, Inputs, Process, Outputs
4. A mermaid flowchart is present showing the lifecycle
5. Verification/validation gates are documented for assurance-related phases
6. Type constraints are satisfied

---

**Note:** This specification follows the pattern established by spec-for-spec and is designed to support the documentation of engineering processes within the assurance framework.
