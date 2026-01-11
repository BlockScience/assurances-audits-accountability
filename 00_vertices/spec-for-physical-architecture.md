---
type: vertex/spec
extends: doc
id: v:spec:physical-architecture
name: Specification for Physical Architecture Documents
description: Defines what makes a valid physical architecture document focusing on concrete technology choices and their relationship to logical components
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies:
  - v:spec:logical-architecture
---

# Specification for Physical Architecture Documents

**This specification defines the structure and requirements for physical architecture documents that establish concrete technology choices, their configurations, and the Element-Component matrix tracing elements to the logical components they implement.**

## Purpose

Physical architecture documents are the fourth of four extended architecture documents (Conceptual, Functional, Logical, Physical) that serve as prerequisites to a summary architecture. This document type focuses on WHAT specific technologies implement the design: naming concrete tools, frameworks, and services with versions. The Element-Component matrix explicitly maps which physical elements implement which logical components, completing the traceability chain from stakeholder needs to implementation.

## Required Frontmatter Fields

All physical architecture documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:physical-architecture-<name>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, physical-architecture]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Physical Architecture-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `system_name` | string | REQUIRED | Name of the system being architected |
| `scope` | string | REQUIRED | Brief scope statement (1-2 sentences) |
| `logical_architecture_ref` | string | REQUIRED | Reference to logical architecture document (id or path) |
| `element_count` | integer | REQUIRED | Number of physical elements defined (must be >= 3) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of document purpose |
| `dependencies` | array[string] | OPTIONAL | Related documents |

## Required Body Sections

The markdown body of a physical architecture document MUST contain:

### 1. Purpose

A clear statement of what this physical architecture establishes.

**Format:**
```markdown
## Purpose

[1-3 sentences explaining what technology choices and implementation elements this document defines]
```

### 2. Overview

Context for the system and reference to the logical architecture.

**Format:**
```markdown
## Overview

[1-3 paragraphs describing:
- The system and its implementation scope
- Reference to the logical architecture that established components
- What this document contributes to the architecture chain]
```

### 3. Logical Architecture Reference

Explicit link to the prerequisite logical architecture with components summary.

**Format:**
```markdown
## Logical Architecture Reference

[[logical-architecture-<name>]]

### Components Summary

| ID | Name | Responsibility |
|----|------|----------------|
| C1 | [Component from logical architecture] | [Brief responsibility] |
| C2 | [Component from logical architecture] | [Brief responsibility] |
```

**Requirements:**
- MUST include link to logical architecture document
- MUST include components summary table
- Component IDs MUST match those in the referenced logical architecture

### 4. Physical Architecture

Defines physical elements with technology choices and rationale.

**Format:**
```markdown
## Physical Architecture

### Element Table

| ID | Name | Technology/Tool | Version | Purpose |
|----|------|-----------------|---------|---------|
| E1 | [Element Name] | [Specific technology] | [Version] | [Purpose] |
| E2 | [Element Name] | [Specific technology] | [Version] | [Purpose] |

### Element Definitions

#### E1: [Element Name]

**Technology:** [Specific tool/framework/service name]
**Version:** [Specific version or version constraint]

**Purpose:** [What this element accomplishes]

**Rationale:** [Why this technology was chosen]

**Configuration:** [Key configuration aspects]

[Repeat for each element]

### Deployment View

[Description of how elements are deployed and configured together]

#### Deployment Diagram

[Optional: ASCII or linked diagram showing deployment topology]

#### Environment Configuration

| Environment | Configuration Notes |
|-------------|---------------------|
| Development | [Dev-specific config] |
| Production | [Prod-specific config] |
```

**Requirements:**
- MUST include Element Table with at least `element_count` rows
- Each element MUST have unique ID (format: E1, E2, etc.)
- Each element MUST specify concrete technology and version
- MUST include Element Definitions subsection with one entry per element
- Each definition MUST include rationale for technology choice
- MUST include Deployment View subsection
- Elements MUST be technology-specific (concrete tools, versions, services)

### 5. Element-Component Matrix

The core innovation: a bipartite graph connecting physical elements to logical components.

**Format:**
```markdown
## Element-Component Matrix

### Matrix View

|      | C1  | C2  | C3  | C4  |
|------|-----|-----|-----|-----|
| E1   |  X  |     |     |     |
| E2   |  X  |  X  |     |     |
| E3   |     |     |  X  |  X  |

### Relationship Details

| Element | Component | Implementation Type | Rationale |
|---------|-----------|---------------------|-----------|
| [ID] | [C#] | [Type] | [How this element implements this component] |

### Key Implementations

[Summary of critical element-component implementations]

1. [Implementation 1: How key elements implement key components]
2. [Implementation 2]
3. [Implementation 3]
```

**Requirements:**
- MUST include Matrix View table with all elements as rows and all components as columns
- MUST include Relationship Details table with at least one entry per element
- MUST include Key Implementations with at least 3 items
- Implementation types SHOULD be one of: Full Implementation, Partial Implementation, Shared Implementation

### 6. Unit Testing Strategy

Defines how unit testing will evaluate individual elements.

**Format:**
```markdown
## Unit Testing Strategy

### Test Approach by Element

| Element | Test Framework | Test Method | Success Indicator |
|---------|----------------|-------------|-------------------|
| E1 | [framework] | [method] | [indicator] |
| E2 | [framework] | [method] | [indicator] |
```

**Requirements:**
- MUST include table with test approach for each element
- Each element from Element Table MUST have corresponding test approach
- Test frameworks MAY be technology-specific (this is the physical layer)

## Optional Body Sections

### Traceability to Logical Architecture

Maps logical architecture content to this document.

**Format:**
```markdown
## Traceability to Logical Architecture

### From Components to Elements

| Component | Implemented by Elements |
|-----------|------------------------|
| C1 | E1, E2 |
| C2 | E2, E3 |

### Coverage Analysis

[Analysis of how completely elements implement components]
```

### Technology Selection Rationale

**Format:**
```markdown
## Technology Selection Rationale

### Selection Criteria

[What criteria guided technology choices]

### Alternatives Considered

| Element | Technology Chosen | Alternatives | Why Chosen |
|---------|-------------------|--------------|------------|
| E1 | [chosen] | [alt1, alt2] | [rationale] |
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
3. **ID Format:** MUST match pattern `v:doc:physical-architecture-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `physical-architecture`

## Content Requirements

1. **Element Count:** `element_count` MUST be >= 3
2. **Element Definitions:** Number of Element Definitions subsections MUST match `element_count`
3. **Element Table Rows:** Number of Element Table rows MUST match `element_count`
4. **Matrix Coverage:** Every element MUST have at least one relationship in the Relationship Details table
5. **Component Coverage:** Every component from the logical architecture SHOULD be implemented by at least one element
6. **Testing Coverage:** Every element MUST have a corresponding entry in Unit Testing Strategy
7. **Technology Specificity:** Elements MUST specify concrete technologies with versions (REQUIRED)
8. **Rationale:** Every element definition MUST include rationale for technology choice

## Bipartite Graph Properties

The Element-Component Matrix forms a bipartite graph:

- **Partition 1 (Elements):** Physical elements defined in this document
- **Partition 2 (Components):** Logical components from the logical architecture
- **Edges:** Implementation relationships between elements and components

**Graph Requirements:**
- Every element vertex MUST have degree >= 1 (implements at least one component)
- Every component vertex SHOULD have degree >= 1 (implemented by at least one element)
- Implementation types provide edge labels

## Prerequisites

Physical architecture documents MUST be preceded by a logical architecture:

| Prerequisite | Purpose | Requirement |
|--------------|---------|-------------|
| Logical Architecture | Establishes components that elements must implement | REQUIRED |

**Prerequisite Validation:**
- `logical_architecture_ref` MUST reference a valid logical architecture document
- Component IDs used MUST match those in the referenced logical architecture

## Coupling Requirement

Every physical architecture spec SHOULD be paired with `guidance-for-physical-architecture` via a coupling edge. The guidance defines how to evaluate quality and fitness-for-purpose.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, fields, and counts are correct
- **Validation** (against guidance-for-physical-architecture): Qualitative assessment of component coverage, technology specificity, rationale clarity, and deployment clarity

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:physical-architecture-<name>
name: <string>
tags: [vertex, doc, physical-architecture]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
system_name: <string>
scope: <string>
logical_architecture_ref: <string>
element_count: <integer>

# Recommended frontmatter
description: <string>

# Optional frontmatter
dependencies: [<related-documents>]

# Required body sections (markdown)
## Purpose
## Overview
## Logical Architecture Reference
  ### Components Summary
## Physical Architecture
  ### Element Table
  ### Element Definitions
    #### E#: [Name] (one per element)
  ### Deployment View
## Element-Component Matrix
  ### Matrix View
  ### Relationship Details
  ### Key Implementations
## Unit Testing Strategy

# Optional body sections
## Traceability to Logical Architecture
## Technology Selection Rationale
## Constraints and Assumptions
## Risks and Mitigations
```

## Compliance

A document claiming to be a physical architecture document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. `element_count` >= 3 and matches actual element definitions
4. Element-Component Matrix covers all elements and components
5. Unit Testing Strategy covers all elements
6. Type constraints are satisfied
7. Logical architecture reference is present
8. Elements specify concrete technologies with versions
9. Element definitions include rationale for technology choices

---

**Note:** This specification defines the fourth and final extended architecture document. Physical architecture completes the chain that flows into the summary [[spec-for-architecture]].
