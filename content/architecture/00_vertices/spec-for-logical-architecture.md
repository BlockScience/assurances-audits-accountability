---
type: vertex/spec
extends: doc
id: v:spec:logical-architecture
name: Specification for Logical Architecture Documents
description: Defines what makes a valid logical architecture document focusing on technology-agnostic components and their relationship to functions
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies:
  - v:spec:functional-architecture
---

# Specification for Logical Architecture Documents

**This specification defines the structure and requirements for logical architecture documents that establish system components, their interfaces, and the Component-Function matrix tracing components to the functions they realize.**

## Purpose

Logical architecture documents are the third of four extended architecture documents (Conceptual, Functional, Logical, Physical) that serve as prerequisites to a summary architecture. This document type focuses on HOW the system is structured: defining technology-agnostic components with clear responsibilities and interfaces. The Component-Function matrix explicitly maps which components realize which functions, creating traceable flow from system behaviors to design structure.

## Required Frontmatter Fields

All logical architecture documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:logical-architecture-<name>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, logical-architecture]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Logical Architecture-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `system_name` | string | REQUIRED | Name of the system being architected |
| `scope` | string | REQUIRED | Brief scope statement (1-2 sentences) |
| `functional_architecture_ref` | string | REQUIRED | Reference to functional architecture document (id or path) |
| `component_count` | integer | REQUIRED | Number of components defined (must be >= 3) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `physical_architecture_ref` | string | RECOMMENDED | Forward reference to physical architecture (when created) |
| `description` | string | RECOMMENDED | Brief description of document purpose |
| `dependencies` | array[string] | OPTIONAL | Related documents |

## Required Body Sections

The markdown body of a logical architecture document MUST contain:

### 1. Purpose

A clear statement of what this logical architecture establishes.

**Format:**
```markdown
## Purpose

[1-3 sentences explaining what system components and structure this document defines]
```

### 2. Overview

Context for the system and reference to the functional architecture.

**Format:**
```markdown
## Overview

[1-3 paragraphs describing:
- The system and its structural scope
- Reference to the functional architecture that established functions
- What this document contributes to the architecture chain]
```

### 3. Functional Architecture Reference

Explicit link to the prerequisite functional architecture with functions summary.

**Format:**
```markdown
## Functional Architecture Reference

[[functional-architecture-<name>]]

### Functions Summary

| ID | Name | Description |
|----|------|-------------|
| F1 | [Function from functional architecture] | [Brief description] |
| F2 | [Function from functional architecture] | [Brief description] |
```

**Requirements:**
- MUST include link to functional architecture document
- MUST include functions summary table
- Function IDs MUST match those in the referenced functional architecture

### 4. Logical Architecture

Defines system components with responsibilities and interfaces.

**Format:**
```markdown
## Logical Architecture

### Component Table

| ID | Name | Responsibility | Interfaces |
|----|------|----------------|------------|
| C1 | [Component Name] | [Single responsibility] | [Interface list] |
| C2 | [Component Name] | [Single responsibility] | [Interface list] |

### Component Definitions

#### C1: [Component Name]

**Responsibility:** [Clear, single responsibility statement]

**Interfaces:**
- [Interface 1]: [Description, direction, data exchanged]
- [Interface 2]: [Description, direction, data exchanged]

**Collaborations:** [How this component works with others]

[Repeat for each component]

### Interface Specifications

| Interface | From | To | Data Exchanged | Protocol |
|-----------|------|-----|----------------|----------|
| [I1] | C1 | C2 | [Data description] | [Logical protocol, not technology] |
```

**Requirements:**
- MUST include Component Table with at least `component_count` rows
- Each component MUST have unique ID (format: C1, C2, etc.)
- Each component MUST specify responsibility and interfaces
- MUST include Component Definitions subsection with one entry per component
- MUST include Interface Specifications subsection
- Components MUST be technology-agnostic (no implementation details)

### 5. Component-Function Matrix

The core innovation: a bipartite graph connecting components to functions.

**Format:**
```markdown
## Component-Function Matrix

### Matrix View

|      | F1  | F2  | F3  | F4  | F5  |
|------|-----|-----|-----|-----|-----|
| C1   |  X  |  X  |     |     |     |
| C2   |     |  X  |  X  |     |     |
| C3   |     |     |  X  |  X  |  X  |

### Relationship Details

| Component | Function | Realization Type | Rationale |
|-----------|----------|------------------|-----------|
| [ID] | [F#] | [Type] | [How this component realizes this function] |

### Key Allocations

[Summary of critical component-function allocations]

1. [Allocation 1: How key components realize key functions]
2. [Allocation 2]
3. [Allocation 3]
```

**Requirements:**
- MUST include Matrix View table with all components as rows and all functions as columns
- MUST include Relationship Details table with at least one entry per component
- MUST include Key Allocations with at least 3 items
- Realization types SHOULD be one of: Primary Realizer, Collaborator, Orchestrator

### 6. Integration Testing Strategy

Defines how integration testing will evaluate component interfaces.

**Format:**
```markdown
## Integration Testing Strategy

### Test Approach by Interface

| Interface | Test Type | Test Method | Success Indicator |
|-----------|-----------|-------------|-------------------|
| I1 (C1→C2) | [type] | [method] | [indicator] |
| I2 (C2→C3) | [type] | [method] | [indicator] |
```

**Requirements:**
- MUST include table with test approach for each interface
- Each interface from Interface Specifications MUST have corresponding test approach

## Optional Body Sections

### Traceability to Functional Architecture

Maps functional architecture content to this document.

**Format:**
```markdown
## Traceability to Functional Architecture

### From Functions to Components

| Function | Realized by Components |
|----------|------------------------|
| F1 | C1, C2 |
| F2 | C2, C3 |

### Coverage Analysis

[Analysis of how completely components realize functions]
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
3. **ID Format:** MUST match pattern `v:doc:logical-architecture-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `logical-architecture`

## Content Requirements

1. **Component Count:** `component_count` MUST be >= 3
2. **Component Definitions:** Number of Component Definitions subsections MUST match `component_count`
3. **Component Table Rows:** Number of Component Table rows MUST match `component_count`
4. **Matrix Coverage:** Every component MUST have at least one relationship in the Relationship Details table
5. **Function Coverage:** Every function from the functional architecture SHOULD be realized by at least one component
6. **Testing Coverage:** Every interface MUST have a corresponding entry in Integration Testing Strategy
7. **Technology Independence:** Components MUST be described without reference to specific technologies (CRITICAL)

## Bipartite Graph Properties

The Component-Function Matrix forms a bipartite graph:

- **Partition 1 (Components):** System components defined in this document
- **Partition 2 (Functions):** Functions from the functional architecture
- **Edges:** Relationships between components and functions

**Graph Requirements:**
- Every component vertex MUST have degree >= 1 (realizes at least one function)
- Every function vertex SHOULD have degree >= 1 (realized by at least one component)
- Realization types provide edge labels

## Prerequisites

Logical architecture documents MUST be preceded by a functional architecture:

| Prerequisite | Purpose | Requirement |
|--------------|---------|-------------|
| Functional Architecture | Establishes functions that components must realize | REQUIRED |

**Prerequisite Validation:**
- `functional_architecture_ref` MUST reference a valid functional architecture document
- Function IDs used MUST match those in the referenced functional architecture

## Forward References

Logical architecture documents MAY reference subsequent architecture documents:

| Forward Reference | Purpose | Requirement |
|-------------------|---------|-------------|
| Physical Architecture | Links to next layer in architecture chain | RECOMMENDED when available |

## Coupling Requirement

Every logical architecture spec SHOULD be paired with `guidance-for-logical-architecture` via a coupling edge. The guidance defines how to evaluate quality and fitness-for-purpose.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, fields, and counts are correct
- **Validation** (against guidance-for-logical-architecture): Qualitative assessment of function coverage, component cohesion, interface clarity, and technology independence

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:logical-architecture-<name>
name: <string>
tags: [vertex, doc, logical-architecture]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
system_name: <string>
scope: <string>
functional_architecture_ref: <string>
component_count: <integer>

# Recommended frontmatter
physical_architecture_ref: <string>
description: <string>

# Optional frontmatter
dependencies: [<related-documents>]

# Required body sections (markdown)
## Purpose
## Overview
## Functional Architecture Reference
  ### Functions Summary
## Logical Architecture
  ### Component Table
  ### Component Definitions
    #### C#: [Name] (one per component)
  ### Interface Specifications
## Component-Function Matrix
  ### Matrix View
  ### Relationship Details
  ### Key Allocations
## Integration Testing Strategy

# Optional body sections
## Traceability to Functional Architecture
## Constraints and Assumptions
## Risks and Mitigations
```

## Compliance

A document claiming to be a logical architecture document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. `component_count` >= 3 and matches actual component definitions
4. Component-Function Matrix covers all components and functions
5. Integration Testing Strategy covers all interfaces
6. Type constraints are satisfied
7. Functional architecture reference is present
8. Components are technology-agnostic (CRITICAL)

---

**Note:** This specification defines the third of four extended architecture documents. Logical architecture establishes system components that flow into [[spec-for-physical-architecture]].
