---
type: vertex/spec
extends: doc
id: v:spec:conceptual-architecture
name: Specification for Conceptual Architecture Documents
description: Defines what makes a valid conceptual architecture document focusing on stakeholder needs and acceptance criteria with a stakeholder-criterion matrix
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies:
  - v:spec:field-survey
---

# Specification for Conceptual Architecture Documents

**This specification defines the structure and requirements for conceptual architecture documents that establish stakeholder needs, acceptance criteria, and the relationships between them through a stakeholder-criterion matrix.**

## Purpose

Conceptual architecture documents are the first of four extended architecture documents (Conceptual, Functional, Logical, Physical) that serve as prerequisites to a summary architecture. This document type focuses on the ConOps layer: establishing who the stakeholders are, what they need, and how acceptance will be evaluated. The stakeholder-criterion matrix explicitly maps which acceptance criteria matter to which stakeholders, creating a traceable foundation for all subsequent architecture layers.

## Required Frontmatter Fields

All conceptual architecture documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:conceptual-architecture-<name>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, conceptual-architecture]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Conceptual Architecture-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `system_name` | string | REQUIRED | Name of the system being architected |
| `scope` | string | REQUIRED | Brief scope statement (1-2 sentences) |
| `field_survey_ref` | string | REQUIRED | Reference to field survey document (id or path) |
| `stakeholder_count` | integer | REQUIRED | Number of stakeholders in the matrix (must be >= 2) |
| `criterion_count` | integer | REQUIRED | Number of acceptance criteria defined (must be >= 3) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `functional_architecture_ref` | string | RECOMMENDED | Forward reference to functional architecture (when created) |
| `description` | string | RECOMMENDED | Brief description of document purpose |
| `stakeholders` | array[string] | RECOMMENDED | List of stakeholder IDs from field survey (e.g., A1, A2) |
| `dependencies` | array[string] | OPTIONAL | Related documents |

## Required Body Sections

The markdown body of a conceptual architecture document MUST contain:

### 1. Purpose

A clear statement of what this conceptual architecture establishes.

**Format:**
```markdown
## Purpose

[1-3 sentences explaining what stakeholder needs and acceptance criteria this document defines]
```

### 2. Overview

Context for the system and reference to the field survey.

**Format:**
```markdown
## Overview

[1-3 paragraphs describing:
- The system and its context
- Reference to the field survey that established stakeholders
- What this document contributes to the architecture chain]
```

### 3. Field Survey Reference

Explicit link to the prerequisite field survey with stakeholder summary.

**Format:**
```markdown
## Field Survey Reference

[[field-survey-<name>]]

### Stakeholders Used

| ID | Name | Type | Role in This Architecture |
|----|------|------|---------------------------|
| [ID] | [Name from field survey] | [Type] | [How they relate to this system] |
```

**Requirements:**
- MUST include link to field survey document
- MUST include stakeholders table with at least `stakeholder_count` rows
- Stakeholder IDs SHOULD match those in the referenced field survey

### 4. Problem Statement (ConOps)

Describes stakeholder needs and operational context.

**Format:**
```markdown
## Problem Statement (ConOps)

### Operational Context

[Description of how the system operates day-to-day:
- When and where does the system operate?
- Who interacts with it and how?
- What are the key operational scenarios?]

### Stakeholder Needs

#### [ID]: [Stakeholder Name] Needs

- [Need 1]
- [Need 2]
- [Need 3]

[Repeat subsection for each stakeholder]
```

**Requirements:**
- MUST include Operational Context subsection
- MUST include Stakeholder Needs subsection with one sub-subsection per stakeholder
- Number of stakeholder subsections MUST match `stakeholder_count`
- Each stakeholder MUST have at least 2 needs listed

### 5. Acceptance Criteria

Defines measurable criteria for system acceptance.

**Format:**
```markdown
## Acceptance Criteria

| ID | Criterion | Measurement | Target |
|----|-----------|-------------|--------|
| AC1 | [Description] | [How measured] | [What constitutes success] |
| AC2 | [Description] | [How measured] | [What constitutes success] |

### Criterion Definitions

#### AC1: [Criterion Name]

[2-3 sentences providing additional context, rationale, or measurement details]

[Repeat for each criterion]
```

**Requirements:**
- MUST include criteria table with at least `criterion_count` rows
- Each criterion MUST have unique ID (format: AC1, AC2, etc.)
- Each criterion MUST specify measurement approach and success target
- MUST include Criterion Definitions subsection with one entry per criterion

### 6. Stakeholder-Criterion Matrix

The core innovation: a bipartite graph connecting stakeholders to acceptance criteria.

**Format:**
```markdown
## Stakeholder-Criterion Matrix

### Matrix View

|        | AC1 | AC2 | AC3 | AC4 | AC5 |
|--------|-----|-----|-----|-----|-----|
| A1     |  X  |     |  X  |     |     |
| A2     |     |  X  |  X  |  X  |     |
| A3     |  X  |  X  |     |     |  X  |

### Relationship Details

| Stakeholder | Criterion | Role | Rationale |
|-------------|-----------|------|-----------|
| [ID] | [AC#] | [Role Type] | [Why this stakeholder cares about this criterion] |

### Key Dependencies

[Summary of critical stakeholder-criterion relationships that drive the architecture]

1. [Dependency 1]
2. [Dependency 2]
3. [Dependency 3]
```

**Requirements:**
- MUST include Matrix View table with all stakeholders as rows and all criteria as columns
- MUST include Relationship Details table with at least one entry per stakeholder
- MUST include Key Dependencies with at least 3 items
- Role types SHOULD be one of: Primary Beneficiary, Primary User, Accountable, Affected Party, Validator

### 7. Acceptance Testing Strategy

Defines how acceptance will be evaluated.

**Format:**
```markdown
## Acceptance Testing Strategy

### Test Approach by Criterion

| Criterion | Test Type | Test Method | Success Indicator |
|-----------|-----------|-------------|-------------------|
| AC1 | [type] | [method] | [indicator] |
| AC2 | [type] | [method] | [indicator] |
```

**Requirements:**
- MUST include table with test approach for each criterion
- Each criterion from Acceptance Criteria section MUST have corresponding test approach

## Optional Body Sections

### Traceability to Field Survey

Maps field survey content to this document.

**Format:**
```markdown
## Traceability to Field Survey

### From Actors to Stakeholder Needs

| Field Survey Actor | Conceptual Architecture Stakeholder Needs |
|--------------------|--------------------------------------------|
| [Actor ID] | [Need references] |

### Key Findings Addressed

- **Gap/Tension from Field Survey**: [Gap] -> **Addressed by**: [How addressed]
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
3. **ID Format:** MUST match pattern `v:doc:conceptual-architecture-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `conceptual-architecture`

## Content Requirements

1. **Stakeholder Count:** `stakeholder_count` MUST be >= 2
2. **Criterion Count:** `criterion_count` MUST be >= 3
3. **Stakeholder Subsections:** Number of Stakeholder Needs subsections MUST match `stakeholder_count`
4. **Criterion Rows:** Number of Acceptance Criteria table rows MUST match `criterion_count`
5. **Matrix Coverage:** Every stakeholder MUST have at least one relationship in the Relationship Details table
6. **Testing Coverage:** Every criterion MUST have a corresponding entry in Acceptance Testing Strategy

## Bipartite Graph Properties

The Stakeholder-Criterion Matrix forms a bipartite graph:

- **Partition 1 (Stakeholders):** Subset of actors from the field survey
- **Partition 2 (Criteria):** Acceptance criteria defined in this document
- **Edges:** Relationships between stakeholders and criteria

**Graph Requirements:**
- Every stakeholder vertex MUST have degree >= 1 (connected to at least one criterion)
- The graph need not be fully connected
- Relationship types provide edge labels

## Prerequisites

Conceptual architecture documents MUST be preceded by a field survey:

| Prerequisite | Purpose | Requirement |
|--------------|---------|-------------|
| Field Survey | Establishes actors and resources that inform stakeholder selection | REQUIRED |

**Prerequisite Validation:**
- `field_survey_ref` MUST reference a valid field survey document
- Stakeholder IDs used SHOULD match actor IDs from the referenced field survey

## Forward References

Conceptual architecture documents MAY reference subsequent architecture documents:

| Forward Reference | Purpose | Requirement |
|-------------------|---------|-------------|
| Functional Architecture | Links to next layer in architecture chain | RECOMMENDED when available |

## Coupling Requirement

Every conceptual architecture spec SHOULD be paired with `guidance-for-conceptual-architecture` via a coupling edge. The guidance defines how to evaluate quality and fitness-for-purpose.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, fields, and counts are correct
- **Validation** (against guidance-for-conceptual-architecture): Qualitative assessment of stakeholder completeness, criterion quality, and matrix accuracy

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:conceptual-architecture-<name>
name: <string>
tags: [vertex, doc, conceptual-architecture]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
system_name: <string>
scope: <string>
field_survey_ref: <string>
stakeholder_count: <integer>
criterion_count: <integer>

# Recommended frontmatter
functional_architecture_ref: <string>
description: <string>
stakeholders: [<actor-ids>]

# Optional frontmatter
dependencies: [<related-documents>]

# Required body sections (markdown)
## Purpose
## Overview
## Field Survey Reference
  ### Stakeholders Used
## Problem Statement (ConOps)
  ### Operational Context
  ### Stakeholder Needs
    #### [ID]: [Name] Needs (one per stakeholder)
## Acceptance Criteria
  ### Criterion Definitions
    #### AC#: [Name] (one per criterion)
## Stakeholder-Criterion Matrix
  ### Matrix View
  ### Relationship Details
  ### Key Dependencies
## Acceptance Testing Strategy

# Optional body sections
## Traceability to Field Survey
## Constraints and Assumptions
## Risks and Mitigations
```

## Compliance

A document claiming to be a conceptual architecture document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. `stakeholder_count` >= 2 and matches actual stakeholder subsections
4. `criterion_count` >= 3 and matches actual criteria table rows
5. Stakeholder-Criterion Matrix covers all stakeholders and criteria
6. Acceptance Testing Strategy covers all criteria
7. Type constraints are satisfied
8. Field survey reference is present

---

**Note:** This specification defines the first of four extended architecture documents. Conceptual architecture establishes stakeholder needs and acceptance criteria that flow into [[spec-for-functional-architecture]] (future).
