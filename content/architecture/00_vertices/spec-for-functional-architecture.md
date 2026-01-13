---
type: vertex/spec
extends: doc
id: v:spec:functional-architecture
name: Specification for Functional Architecture Documents
description: Defines what makes a valid functional architecture document focusing on system functions and their relationship to acceptance criteria
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies:
  - v:spec:conceptual-architecture
---

# Specification for Functional Architecture Documents

**This specification defines the structure and requirements for functional architecture documents that establish system functions, their inputs and outputs, and the Function-Criterion matrix tracing functions to acceptance criteria.**

## Purpose

Functional architecture documents are the second of four extended architecture documents (Conceptual, Functional, Logical, Physical) that serve as prerequisites to a summary architecture. This document type focuses on what the system must DO: defining technology-agnostic functions with clear inputs and outputs. The Function-Criterion matrix explicitly maps which functions address which acceptance criteria, creating traceable flow from stakeholder needs to system behaviors.

## Required Frontmatter Fields

All functional architecture documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:functional-architecture-<name>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, functional-architecture]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Functional Architecture-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `system_name` | string | REQUIRED | Name of the system being architected |
| `scope` | string | REQUIRED | Brief scope statement (1-2 sentences) |
| `conceptual_architecture_ref` | string | REQUIRED | Reference to conceptual architecture document (id or path) |
| `function_count` | integer | REQUIRED | Number of functions defined (must be >= 3) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `logical_architecture_ref` | string | RECOMMENDED | Forward reference to logical architecture (when created) |
| `description` | string | RECOMMENDED | Brief description of document purpose |
| `dependencies` | array[string] | OPTIONAL | Related documents |

## Required Body Sections

The markdown body of a functional architecture document MUST contain:

### 1. Purpose

A clear statement of what this functional architecture establishes.

**Format:**
```markdown
## Purpose

[1-3 sentences explaining what system functions and behaviors this document defines]
```

### 2. Overview

Context for the system and reference to the conceptual architecture.

**Format:**
```markdown
## Overview

[1-3 paragraphs describing:
- The system and its functional scope
- Reference to the conceptual architecture that established acceptance criteria
- What this document contributes to the architecture chain]
```

### 3. Conceptual Architecture Reference

Explicit link to the prerequisite conceptual architecture with acceptance criteria summary.

**Format:**
```markdown
## Conceptual Architecture Reference

[[conceptual-architecture-<name>]]

### Acceptance Criteria Summary

| ID | Criterion | Target |
|----|-----------|--------|
| AC1 | [Criterion from conceptual architecture] | [Target] |
| AC2 | [Criterion from conceptual architecture] | [Target] |
```

**Requirements:**
- MUST include link to conceptual architecture document
- MUST include acceptance criteria summary table
- Criteria IDs MUST match those in the referenced conceptual architecture

### 4. Functional Architecture

Defines system functions with inputs and outputs.

**Format:**
```markdown
## Functional Architecture

### Function Table

| ID | Name | Inputs | Outputs | Description |
|----|------|--------|---------|-------------|
| F1 | [Function Name] | [Input list] | [Output list] | [Brief description] |
| F2 | [Function Name] | [Input list] | [Output list] | [Brief description] |

### Function Definitions

#### F1: [Function Name]

**Purpose:** [What this function accomplishes]

**Inputs:**
- [Input 1]: [Description]
- [Input 2]: [Description]

**Outputs:**
- [Output 1]: [Description]

**Behavior:** [Description of function behavior, constraints, and edge cases]

[Repeat for each function]
```

**Requirements:**
- MUST include Function Table with at least `function_count` rows
- Each function MUST have unique ID (format: F1, F2, etc.)
- Each function MUST specify inputs and outputs
- MUST include Function Definitions subsection with one entry per function
- Functions MUST be technology-agnostic (no implementation details)

### 5. Function-Criterion Matrix

The core innovation: a bipartite graph connecting functions to acceptance criteria.

**Format:**
```markdown
## Function-Criterion Matrix

### Matrix View

|      | AC1 | AC2 | AC3 | AC4 | AC5 |
|------|-----|-----|-----|-----|-----|
| F1   |  X  |  X  |     |     |     |
| F2   |     |  X  |  X  |     |     |
| F3   |     |     |  X  |  X  |  X  |

### Relationship Details

| Function | Criterion | Contribution Type | Rationale |
|----------|-----------|-------------------|-----------|
| [ID] | [AC#] | [Type] | [How this function contributes to this criterion] |

### Key Traces

[Summary of critical function-criterion relationships]

1. [Trace 1: How key functions address key criteria]
2. [Trace 2]
3. [Trace 3]
```

**Requirements:**
- MUST include Matrix View table with all functions as rows and all criteria as columns
- MUST include Relationship Details table with at least one entry per function
- MUST include Key Traces with at least 3 items
- Contribution types SHOULD be one of: Primary Contributor, Supporting, Partial

### 6. System Testing Strategy

Defines how system-level testing will evaluate functions.

**Format:**
```markdown
## System Testing Strategy

### Test Approach by Function

| Function | Test Type | Test Method | Success Indicator |
|----------|-----------|-------------|-------------------|
| F1 | [type] | [method] | [indicator] |
| F2 | [type] | [method] | [indicator] |
```

**Requirements:**
- MUST include table with test approach for each function
- Each function from Function Table MUST have corresponding test approach

## Optional Body Sections

### Traceability to Conceptual Architecture

Maps conceptual architecture content to this document.

**Format:**
```markdown
## Traceability to Conceptual Architecture

### From Criteria to Functions

| Acceptance Criterion | Addressed by Functions |
|---------------------|------------------------|
| AC1 | F1, F3 |
| AC2 | F1, F2 |

### Coverage Analysis

[Analysis of how completely functions address acceptance criteria]
```

### Constraints and Assumptions

**Format:**
```markdown
## Constraints and Assumptions

### Constraints

- [Constraint 1]
- [Constraint 2]

### Assumptions

- [Assumption 1]
- [Assumption 2]
```

### Risks and Mitigations

**Format:**
```markdown
## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [R1] | [impact] | [likelihood] | [mitigation] |
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:functional-architecture-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `functional-architecture`

## Content Requirements

1. **Function Count:** `function_count` MUST be >= 3
2. **Function Definitions:** Number of Function Definitions subsections MUST match `function_count`
3. **Function Table Rows:** Number of Function Table rows MUST match `function_count`
4. **Matrix Coverage:** Every function MUST have at least one relationship in the Relationship Details table
5. **Criterion Coverage:** Every acceptance criterion from the conceptual architecture SHOULD be addressed by at least one function
6. **Testing Coverage:** Every function MUST have a corresponding entry in System Testing Strategy
7. **Technology Independence:** Functions MUST be described without reference to specific technologies

## Bipartite Graph Properties

The Function-Criterion Matrix forms a bipartite graph:

- **Partition 1 (Functions):** System functions defined in this document
- **Partition 2 (Criteria):** Acceptance criteria from the conceptual architecture
- **Edges:** Relationships between functions and criteria

**Graph Requirements:**
- Every function vertex MUST have degree >= 1 (contributes to at least one criterion)
- Every criterion vertex SHOULD have degree >= 1 (addressed by at least one function)
- Contribution types provide edge labels

## Prerequisites

Functional architecture documents MUST be preceded by a conceptual architecture:

| Prerequisite | Purpose | Requirement |
|--------------|---------|-------------|
| Conceptual Architecture | Establishes acceptance criteria that functions must address | REQUIRED |

**Prerequisite Validation:**
- `conceptual_architecture_ref` MUST reference a valid conceptual architecture document
- Acceptance criteria IDs used MUST match those in the referenced conceptual architecture

## Forward References

Functional architecture documents MAY reference subsequent architecture documents:

| Forward Reference | Purpose | Requirement |
|-------------------|---------|-------------|
| Logical Architecture | Links to next layer in architecture chain | RECOMMENDED when available |

## Coupling Requirement

Every functional architecture spec SHOULD be paired with `guidance-for-functional-architecture` via a coupling edge. The guidance defines how to evaluate quality and fitness-for-purpose.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, fields, and counts are correct
- **Validation** (against guidance-for-functional-architecture): Qualitative assessment of criterion coverage, function completeness, and I/O clarity

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:functional-architecture-<name>
name: <string>
tags: [vertex, doc, functional-architecture]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
system_name: <string>
scope: <string>
conceptual_architecture_ref: <string>
function_count: <integer>

# Recommended frontmatter
logical_architecture_ref: <string>
description: <string>

# Optional frontmatter
dependencies: [<related-documents>]

# Required body sections (markdown)
## Purpose
## Overview
## Conceptual Architecture Reference
  ### Acceptance Criteria Summary
## Functional Architecture
  ### Function Table
  ### Function Definitions
    #### F#: [Name] (one per function)
## Function-Criterion Matrix
  ### Matrix View
  ### Relationship Details
  ### Key Traces
## System Testing Strategy

# Optional body sections
## Traceability to Conceptual Architecture
## Constraints and Assumptions
## Risks and Mitigations
```

## Compliance

A document claiming to be a functional architecture document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. `function_count` >= 3 and matches actual function definitions
4. Function-Criterion Matrix covers all functions and criteria
5. System Testing Strategy covers all functions
6. Type constraints are satisfied
7. Conceptual architecture reference is present
8. Functions are technology-agnostic

---

**Note:** This specification defines the second of four extended architecture documents. Functional architecture establishes system functions that flow into [[spec-for-logical-architecture]].
