---
type: vertex/spec
extends: doc
id: v:spec:requirements-trace
name: Specification for Requirements Trace Documents
description: Defines what makes a valid requirements traceability report in the knowledge complex
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2026-01-12T00:00:00Z
modified: 2026-01-12T00:00:00Z
dependencies:
  - v:spec:architecture
---

# Specification for Requirements Trace Documents

**This specification defines the structure and requirements for requirements traceability reports in the knowledge complex.**

## Purpose

Requirements trace documents provide **bidirectional traceability analysis** across the four-layer architecture chain (Conceptual → Functional → Logical → Physical). They demonstrate that every stakeholder need is addressed by implementation elements and that every implementation element is justified by stakeholder needs. This spec-for-requirements-trace establishes what fields, sections, and properties must be present in any valid requirements trace document.

## Required Frontmatter Fields

All requirements trace documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:requirements-trace-<system-name>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, requirements-trace]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Architecture References

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `architecture_ref` | string | REQUIRED | ID of the architecture document being traced |
| `conceptual_ref` | string | OPTIONAL | ID of conceptual architecture if in extended mode |
| `functional_ref` | string | OPTIONAL | ID of functional architecture if in extended mode |
| `logical_ref` | string | OPTIONAL | ID of logical architecture if in extended mode |
| `physical_ref` | string | OPTIONAL | ID of physical architecture if in extended mode |

### Trace Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `stakeholder_count` | integer | REQUIRED | Number of stakeholders traced |
| `criteria_count` | integer | REQUIRED | Number of acceptance criteria traced |
| `function_count` | integer | REQUIRED | Number of functions traced |
| `component_count` | integer | REQUIRED | Number of components traced |
| `element_count` | integer | REQUIRED | Number of elements traced |
| `coverage_status` | enum | REQUIRED | Overall coverage: `complete`, `partial`, `gaps-identified` |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of trace scope |
| `trace_date` | datetime | OPTIONAL | Date when traceability analysis was performed |

## Required Body Sections

The markdown body of a requirements trace document MUST contain:

### 1. Executive Summary

Overview of traceability coverage and key findings.

**Format:**
```markdown
## Executive Summary

### Coverage Overview

| Layer | Count | Status |
|-------|-------|--------|
| Stakeholder Needs | N | ✓/✗ All traced |
| Acceptance Criteria | N | ✓/✗ All traced |
| Functions | N | ✓/✗ All traced |
| Components | N | ✓/✗ All traced |
| Elements | N | ✓/✗ All traced |

### Key Findings

[Summary of trace results, gaps if any]
```

**Requirements:**
- MUST include coverage table with counts for each layer
- MUST indicate trace status for each layer
- MUST summarize key findings

### 2. Forward Traceability

Trace from stakeholder needs through to implementation elements.

**Format:**
```markdown
## Forward Traceability

### Stakeholder Needs → Acceptance Criteria

[Matrix or table showing which criteria address which needs]

### Acceptance Criteria → Functions

[Matrix or table showing which functions implement which criteria]

### Functions → Components

[Matrix or table showing which components implement which functions]

### Components → Elements

[Matrix or table showing which elements realize which components]
```

**Requirements:**
- MUST trace each layer to the next layer
- MUST cover all acceptance criteria
- MUST show explicit mappings

### 3. Backward Traceability

Trace from implementation elements back to stakeholder needs.

**Format:**
```markdown
## Backward Traceability

### Elements → Components → Functions → Criteria → Needs

[For each element, trace back through the chain to stakeholder needs]
```

**Requirements:**
- MUST demonstrate that every element traces to stakeholder value
- MUST identify any orphan elements without clear justification

### 4. Gap Analysis

Analysis of any gaps or issues in traceability.

**Format:**
```markdown
## Gap Analysis

### Coverage Gaps

| Gap Type | Description | Impact | Recommendation |
|----------|-------------|--------|----------------|
| [Type] | [Description] | [Impact] | [Recommendation] |

### Assessment

[Summary assessment: NONE IDENTIFIED or description of gaps]
```

**Requirements:**
- MUST explicitly state whether gaps were identified
- If gaps exist, MUST describe impact and recommendations
- If no gaps, MUST state "No gaps identified"

### 5. Traceability Summary

Complete chain visualization or summary table.

**Format:**
```markdown
## Traceability Summary

### Complete Requirements Chain

[Visual or tabular representation of the full trace chain]

### Key Traceability Numbers

| Dimension | Count | Status |
|-----------|-------|--------|
| [Layer] | N | ✓/✗ ALL TRACED |
```

**Requirements:**
- MUST provide a summary view of the complete chain
- MUST include final assessment of coverage

## Optional Body Sections

### Feature-Specific Traceability

Detailed trace for specific features or subsystems.

**Format:**
```markdown
### [Feature Name] Traceability

[Detailed backward trace for this specific feature]
```

### Implementation Readiness

Assessment of readiness based on traceability.

**Format:**
```markdown
## Implementation Readiness

**Status:** [READY/NOT READY]

[Assessment based on traceability findings]
```

### Recommendations

Suggestions based on the analysis.

**Format:**
```markdown
## Recommendations

1. [Recommendation 1]
2. [Recommendation 2]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:requirements-trace-[system-name]`
4. **Tag Inheritance:** Tags MUST include: `[vertex, doc, requirements-trace]`
5. **Architecture Reference:** MUST reference a valid architecture document
6. **Coverage Status:** MUST be one of: `complete`, `partial`, `gaps-identified`

## Content Requirements

1. **Bidirectional Trace:** MUST trace both forward (needs → elements) and backward (elements → needs)
2. **Complete Coverage:** All items at each layer MUST be accounted for
3. **Explicit Gaps:** Any coverage gaps MUST be explicitly identified
4. **Quantitative:** MUST include counts for each layer
5. **Deterministic:** Coverage assessment MUST be objectively verifiable

## Verification vs. Validation

- **Verification** (against this spec): Check all required sections present, counts match architecture documents, coverage status accurate
- **Validation** (against guidance-for-requirements-trace): Assess whether trace is complete, gaps are reasonable, recommendations are actionable

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:requirements-trace-<system-name>
name: <string>
tags: [vertex, doc, requirements-trace]
version: <semver>
architecture_ref: <architecture-doc-id>
stakeholder_count: <integer>
criteria_count: <integer>
function_count: <integer>
component_count: <integer>
element_count: <integer>
coverage_status: complete | partial | gaps-identified
created: <ISO8601>
modified: <ISO8601>

# Optional frontmatter
description: <string>
trace_date: <ISO8601>
conceptual_ref: <doc-id>
functional_ref: <doc-id>
logical_ref: <doc-id>
physical_ref: <doc-id>

# Required body sections (markdown)
## Executive Summary
  ### Coverage Overview (table)
  ### Key Findings
## Forward Traceability
  ### Stakeholder Needs → Acceptance Criteria
  ### Acceptance Criteria → Functions
  ### Functions → Components
  ### Components → Elements
## Backward Traceability
## Gap Analysis
  ### Coverage Gaps
  ### Assessment
## Traceability Summary
  ### Complete Requirements Chain
  ### Key Traceability Numbers

# Optional body sections
### [Feature] Traceability
## Implementation Readiness
## Recommendations
```

## Compliance

A document claiming to be a requirements trace document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Counts match the referenced architecture documents
4. Both forward and backward traceability are provided
5. Gap analysis explicitly states whether gaps exist
6. Type constraints are satisfied
7. Coverage status accurately reflects the analysis

---

**Note:** Requirements trace documents are essential for demonstrating that an architecture is complete and justified. They should be created after architecture documents are stable and updated when architecture changes.
