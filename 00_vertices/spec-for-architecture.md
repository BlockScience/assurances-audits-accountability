---
type: vertex/spec
extends: doc
id: v:spec:architecture
name: Specification for Architecture Documents
description: Defines what makes a valid architecture document using the 4-layer SE framework (Conceptual, Functional, Logical, Physical)
tags:
  - vertex
  - doc
  - spec
version: 1.3.0
created: 2025-12-30T12:00:00Z
modified: 2026-01-12T00:00:00Z
dependencies:
  - v:spec:field-survey
---

# Specification for Architecture Documents

**This specification defines the structure and requirements for architecture documents that describe systems using the four-layer SE framework aligned with the INCOSE SE Handbook and V-model lifecycle.**

## Purpose

Architecture documents describe systems across four abstraction layers: Conceptual, Functional, Logical, and Physical. Each layer maps to a corresponding evaluation level in the V-model (Acceptance, System, Integration, and Unit testing respectively). This spec establishes what fields, sections, and properties must be present in any valid architecture document.

## Required Frontmatter Fields

All architecture documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:architecture-<name>`) |
| `name` | string | REQUIRED | Human-readable architecture document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, architecture]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Architecture-Specific Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `system_name` | string | REQUIRED | Name of the system being architected |
| `scope` | string | REQUIRED | Brief scope statement (1-2 sentences) |
| `field_survey_ref` | string | REQUIRED | Reference to field survey document (id or path) |
| `stakeholders` | array[string] | RECOMMENDED | List of stakeholder categories |

### Extended Architecture References (Optional)

When using extended mode (see Architecture Modes below), these fields reference the detailed extended architecture documents:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `conceptual_architecture_ref` | string | OPTIONAL | Reference to conceptual-architecture document |
| `functional_architecture_ref` | string | OPTIONAL | Reference to functional-architecture document |
| `logical_architecture_ref` | string | OPTIONAL | Reference to logical-architecture document |
| `physical_architecture_ref` | string | OPTIONAL | Reference to physical-architecture document |
| `requirements_trace_ref` | string | OPTIONAL | Reference to requirements traceability report |

**Note:** In extended mode, all four architecture layer references MUST be present. The `requirements_trace_ref` is RECOMMENDED for extended mode to provide formal bidirectional traceability evidence. In standard mode, these fields are omitted.

### Optional Metadata

| Field          | Type          | Requirement | Description                               |
|----------------|---------------|-------------|-------------------------------------------|
| `description`  | string        | RECOMMENDED | Brief description of architecture purpose |
| `dependencies` | array[string] | OPTIONAL    | Related architecture documents            |

## Required Body Sections

The markdown body of an architecture document MUST contain:

### 1. Overview

A brief introduction to the system and architecture document.

**Format:**
```markdown
## Overview

[1-3 paragraphs describing the system, its purpose, and the scope of this architecture document]
```

### 2. V-Model Summary Table

A table mapping the four layers to their evaluation counterparts, showing both design document status and implementation status.

**Format:**
```markdown
## V-Model Summary

| Layer | Left Side (Idealized) | Design Status | Right Side (Realized) | Implementation Status |
|-------|----------------------|---------------|----------------------|----------------------|
| **Conceptual** | ConOps: [description] | [design status] | Acceptance Testing: [description] | [impl status] |
| **Functional** | Functional Architecture: [description] | [design status] | System Testing: [description] | [impl status] |
| **Logical** | Logical Architecture: [description] | [design status] | Integration Testing: [description] | [impl status] |
| **Physical** | Physical Architecture: [description] | [design status] | Unit Testing: [description] | [impl status] |
```

**Column Definitions:**

| Column | Purpose | Valid Values |
|--------|---------|--------------|
| Left Side (Idealized) | Describes the design/requirements for this layer | Descriptive text |
| Design Status | Status of the design document(s) for this layer | Draft, Review, Assured |
| Right Side (Realized) | Describes the testing/verification approach | Descriptive text |
| Implementation Status | Status of actual implementation and testing | Not Started, In Progress, Partial, Complete |

**Requirements:**
- MUST include all four layers
- MUST include both left side (idealized/design) and right side (realized/testing)
- Design Status column MUST indicate current design document lifecycle position
- Implementation Status column MUST indicate realization/testing progress

### 3. Conceptual Layer

Describes stakeholder needs and operational context (ConOps).

**Format:**
```markdown
## Conceptual Layer

### Problem Statement (ConOps)

[Description of stakeholder needs and operational context]

- [Need 1]
- [Need 2]
- [Need 3]

### Acceptance Criteria

[How stakeholder acceptance will be evaluated]

- [Criterion 1]
- [Criterion 2]
```

**Requirements:**
- MUST include at least 3 stakeholder needs
- MUST include at least 2 acceptance criteria
- MUST describe operational context

### 4. Functional Layer

Describes what functions the system must perform.

**Format:**
```markdown
## Functional Layer

### Functional Architecture

[Description of system functions and their relationships]

| Function | Inputs | Outputs | Description |
|----------|--------|---------|-------------|
| [F1] | [inputs] | [outputs] | [description] |
| [F2] | [inputs] | [outputs] | [description] |

### System Testing Criteria

[How functional correctness will be evaluated]

- [Test criterion 1]
- [Test criterion 2]
```

**Requirements:**
- MUST include at least 3 functions
- MUST specify inputs and outputs for each function
- MUST include system testing criteria

### 5. Logical Layer

Describes design-independent component structure.

**Format:**
```markdown
## Logical Layer

### Logical Architecture

[Description of components and their interactions, independent of implementation technology]

| Component | Responsibility | Interfaces |
|-----------|---------------|------------|
| [C1] | [responsibility] | [interfaces] |
| [C2] | [responsibility] | [interfaces] |

### Integration Testing Criteria

[How component integration will be evaluated]

- [Integration test 1]
- [Integration test 2]
```

**Requirements:**
- MUST include at least 3 components
- MUST describe component interfaces
- MUST include integration testing criteria
- MUST be technology-agnostic (design-independent)

### 6. Physical Layer

Describes specific implementation choices.

**Format:**
```markdown
## Physical Layer

### Physical Architecture

[Description of specific technologies, tools, and implementation choices]

| Element | Technology/Tool | Purpose |
|---------|----------------|---------|
| [E1] | [technology] | [purpose] |
| [E2] | [technology] | [purpose] |

### Unit Testing Criteria

[How individual units will be evaluated]

- [Unit test 1]
- [Unit test 2]
```

**Requirements:**
- MUST include at least 3 implementation elements
- MUST specify concrete technologies or tools
- MUST include unit testing criteria

## Architecture Modes

Architecture documents can be authored in two modes:

### Standard Mode (Inline Layers)

All four layers are fully documented inline within the architecture document. Each layer section contains:
- Detailed content (needs, functions, components, elements)
- Corresponding testing criteria
- Minimum element counts (3+ per layer)

This mode is appropriate for:
- Smaller systems
- Rapid prototyping
- When detailed traceability matrices are not required

**Requirements:** All layer sections MUST be substantive with minimum required elements as specified above.

### Extended Mode (Reference Synthesis)

The four layers are documented in separate extended architecture documents, and the summary architecture references them. The architecture document contains:
- V-Model Summary table (required)
- Layer sections with references to extended documents
- Synthesis of key content (not duplication)
- Optional requirements traceability report reference

Extended mode requires all four frontmatter references:
- `conceptual_architecture_ref` pointing to a valid conceptual-architecture document
- `functional_architecture_ref` pointing to a valid functional-architecture document
- `logical_architecture_ref` pointing to a valid logical-architecture document
- `physical_architecture_ref` pointing to a valid physical-architecture document

Extended mode RECOMMENDS:

- `requirements_trace_ref` pointing to a valid requirements traceability report that demonstrates bidirectional coverage from stakeholder needs through implementation elements

**Requirements:** Layer sections in extended mode MUST reference their extended documents and MAY contain abbreviated synthesis content rather than full inline detail. The minimum element counts (3+ per layer) are satisfied by the referenced extended documents, not the summary architecture.

This mode is appropriate for:
- Complex systems requiring detailed traceability
- Programs needing stakeholder-criterion, function-criterion, component-function, and element-component matrices
- Formal assurance requirements
- Multi-team projects where each architecture layer may be owned separately
- Compliance-critical work requiring evidence of complete requirements coverage

### Mode Detection

The mode is determined by presence of extended architecture references:
- If `conceptual_architecture_ref`, `functional_architecture_ref`, `logical_architecture_ref`, and `physical_architecture_ref` are ALL present → Extended Mode
- Otherwise → Standard Mode

## Optional Body Sections

### Traceability Matrix

Maps requirements across layers.

**Format:**
```markdown
## Traceability Matrix

| Conceptual Need | Functional Requirement | Logical Component | Physical Element |
|-----------------|----------------------|-------------------|------------------|
| [CN1] | [FR1] | [LC1] | [PE1] |
```

### Constraints and Assumptions

Documents constraints and assumptions affecting the architecture.

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

Identifies architectural risks.

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
3. **ID Format:** MUST match pattern `v:doc:architecture-[kebab-case-name]`
4. **Tag Requirement:** Tags MUST include `architecture`

## Content Requirements

1. **Layer Completeness:** All four layers MUST be present. In standard mode, layers MUST be substantive with minimum required elements. In extended mode, layers MUST reference their extended documents and MAY contain abbreviated synthesis content.
2. **V-Model Alignment:** Each layer MUST have both idealized (left) and realized (right) aspects
3. **Testability:** Each layer MUST include testability criteria (in standard mode) or reference to testing strategy (in extended mode)
4. **Traceability:** Content SHOULD be traceable across layers (needs → functions → components → implementations)
5. **Technology Independence:** Logical layer MUST be describable without reference to specific technologies
6. **Extended Mode Consistency:** In extended mode, all four extended architecture references MUST be present and MUST reference valid documents
7. **Extended Mode References:** In extended mode, layer sections MUST include explicit references to their corresponding extended documents

## Prerequisites

Architecture documents MUST be preceded by a field survey document that establishes context:

| Prerequisite | Purpose                                                          | Requirement |
|--------------|------------------------------------------------------------------|-------------|
| Field Survey | Documents actors, resources, and relationships before architecture | REQUIRED    |

Architecture documents:

- MUST reference the field survey via `field_survey_ref` in frontmatter
- Stakeholders in architecture SHOULD align with actors from field survey
- Scope statement SHOULD be consistent with field survey scope boundaries

## Coupling Requirement

Every architecture document SHOULD be verified against this spec and validated against the corresponding `guidance-for-architecture` document via appropriate edges. The guidance defines how to evaluate quality and fitness-for-purpose for architecture documents.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections and fields are present
- **Validation** (against guidance-for-architecture): Qualitative assessment that the architecture is complete, coherent, and fit-for-purpose

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:architecture-<name>
name: <string>
tags: [vertex, doc, architecture]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
system_name: <string>
scope: <string>
field_survey_ref: <string>

# Recommended frontmatter
stakeholders: [<stakeholder-categories>]
description: <string>

# Optional frontmatter
dependencies: [<related-architectures>]

# Extended mode frontmatter (all four required for extended mode)
conceptual_architecture_ref: <string>   # Reference to conceptual-architecture doc
functional_architecture_ref: <string>   # Reference to functional-architecture doc
logical_architecture_ref: <string>      # Reference to logical-architecture doc
physical_architecture_ref: <string>     # Reference to physical-architecture doc
requirements_trace_ref: <string>        # RECOMMENDED: Reference to requirements trace report

# Required body sections (markdown)
## Overview
## V-Model Summary (table with 4 layers)
## Conceptual Layer
  ### Problem Statement (ConOps)
  ### Acceptance Criteria
## Functional Layer
  ### Functional Architecture
  ### System Testing Criteria
## Logical Layer
  ### Logical Architecture
  ### Integration Testing Criteria
## Physical Layer
  ### Physical Architecture
  ### Unit Testing Criteria

# Optional body sections
## Traceability Matrix
## Constraints and Assumptions
## Risks and Mitigations
```

**Note:** In extended mode, layer sections may contain abbreviated content with explicit references to extended documents rather than full inline detail.

## Compliance

A document claiming to be an architecture document is compliant with this specification if and only if:

### Standard Mode Compliance

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. V-Model Summary table includes all four layers with both sides
4. Each layer section includes at least the minimum required elements (3+ per layer)
5. Type constraints are satisfied
6. Logical layer content is technology-agnostic

### Extended Mode Compliance

1. All REQUIRED frontmatter fields are present and correctly typed
2. All four extended architecture references are present (`conceptual_architecture_ref`, `functional_architecture_ref`, `logical_architecture_ref`, `physical_architecture_ref`)
3. All REQUIRED body sections are present (may contain abbreviated content with references)
4. V-Model Summary table includes all four layers with both sides
5. Each layer section includes explicit reference to its extended document
6. Type constraints are satisfied
7. Referenced extended documents exist and are valid

---

**Note:** This specification follows the INCOSE SE Handbook patterns for architecture description and aligns with the V-model lifecycle for verification and validation. Extended mode enables detailed traceability through bipartite relationship matrices in the extended architecture documents.
