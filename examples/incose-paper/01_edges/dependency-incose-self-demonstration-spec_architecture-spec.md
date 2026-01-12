---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-spec:architecture-spec
name: Dependency - Self-Demonstration Spec requires Architecture Spec
description: Self-demonstrating papers must have an architecture document conforming to spec-for-architecture
source: v:spec:incose-self-demonstration
target: v:spec:architecture
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: supporting_document
subsection_field: supporting_documents.architecture
required: true
tags:
  - edge
  - dependency
  - self-demonstration
version: 1.0.0
created: 2025-12-30T22:00:00Z
modified: 2025-12-30T22:00:00Z
---

# Dependency - Self-Demonstration Spec requires Architecture Spec

**Self-demonstrating INCOSE papers require an architecture document that conforms to the architecture specification.**

## Dependency Relationship

**Dependent:** `v:spec:incose-self-demonstration` (Specification for Self-Demonstrating Papers)
**Dependency:** `v:spec:architecture` (Specification for Architecture Documents)
**Relationship:** Self-demonstration spec requires architecture spec (supporting document dependency)

**Usage:** Self-demonstrating papers must have an architecture document available at time of production. The architecture document captures the framework's conceptual, functional, logical, and physical layers. The paper's content must be consistent with this architecture document.

**Assurance Note:** This dependency edge tracks compositional requirements and is separate from the assurance DAG. For assurance, `spec-for-incose-self-demonstration` verifies against `spec-for-spec` (because it is a spec), not against `spec-for-architecture`.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `supporting_documents.architecture` in paper metadata |
| **Required** | Yes - architecture document MUST exist |
| **Cardinality** | One architecture document per self-demonstrating paper |
| **Assurance Status** | Architecture document SHOULD be assured before paper finalization |

### Consistency Checks Enabled

This dependency enables the following consistency checks (from spec-for-incose-self-demonstration):

| Check | Description |
|-------|-------------|
| C1.1 | All four architecture layers (Conceptual, Functional, Logical, Physical) must be referenced in paper |
| C1.2 | V-model mapping must be consistent between architecture and paper |
| C1.3 | Stakeholder needs from architecture must align with paper's problem statement |
| C1.4 | Physical implementation choices must match between documents |
| C1.5 | Functional requirements must map to demonstrated capabilities |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers claim "the paper is its own proof." For this claim to be credible, the paper must accurately reflect the framework it describes. The architecture document serves as the authoritative technical reference:

1. **Conceptual Layer** → Defines the problem and stakeholder needs the paper addresses
2. **Functional Layer** → Defines what the framework does (what the paper must demonstrate)
3. **Logical Layer** → Defines the components (what the paper must explain)
4. **Physical Layer** → Defines the implementation (what the paper must reference correctly)

Without an architecture document, the paper's claims about the framework would be unconstrained—anything could be claimed without a reference point for consistency checking.

### Difference from Inheritance

This is a **uses/has-a** relationship, not an **is-a** relationship:
- Self-demonstration spec is NOT a specialized kind of architecture spec
- Self-demonstration spec USES architecture spec to define what supporting document is needed
- The architecture document is a required component, not a parent type

### Difference from Assurance

This is a **compositional** relationship, not an **assurance** relationship:
- Self-demonstration spec does NOT verify against architecture spec
- Self-demonstration spec verifies against spec-for-spec (because it's a spec)
- This dependency captures requirements for supporting documents, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Direction: arrow from self-demonstration-spec toward architecture-spec

---

**Note:** This dependency is one of four supporting document dependencies for self-demonstrating papers. The others are: lifecycle, literature-review, and novel-contributions.