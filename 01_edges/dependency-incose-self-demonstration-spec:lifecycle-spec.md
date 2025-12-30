---
type: edge/dependency
extends: edge
id: e:dependency:incose-self-demonstration-spec:lifecycle-spec
name: Dependency - Self-Demonstration Spec requires Lifecycle Spec
description: Self-demonstrating papers must have a lifecycle document conforming to spec-for-lifecycle
source: v:spec:incose-self-demonstration
target: v:spec:lifecycle
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: supporting_document
subsection_field: supporting_documents.lifecycle
required: true
tags:
  - edge
  - dependency
  - self-demonstration
version: 1.0.0
created: 2025-12-30T22:00:00Z
modified: 2025-12-30T22:00:00Z
---

# Dependency - Self-Demonstration Spec requires Lifecycle Spec

**Self-demonstrating INCOSE papers require a lifecycle document that conforms to the lifecycle specification.**

## Dependency Relationship

**Dependent:** `v:spec:incose-self-demonstration` (Specification for Self-Demonstrating Papers)
**Dependency:** `v:spec:lifecycle` (Specification for Lifecycle Documents)
**Relationship:** Self-demonstration spec requires lifecycle spec (supporting document dependency)

**Usage:** Self-demonstrating papers must have a lifecycle document available at time of production. The lifecycle document describes the engineering process for producing assured documents. The paper's production must visibly enact this lifecycle.

**Assurance Note:** This dependency edge tracks compositional requirements and is separate from the assurance DAG. For assurance, `spec-for-incose-self-demonstration` verifies against `spec-for-spec` (because it is a spec), not against `spec-for-lifecycle`.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `supporting_documents.lifecycle` in paper metadata |
| **Required** | Yes - lifecycle document MUST exist |
| **Cardinality** | One lifecycle document per self-demonstrating paper |
| **Assurance Status** | Lifecycle document SHOULD be assured before paper finalization |

### Consistency Checks Enabled

This dependency enables the following consistency checks (from spec-for-incose-self-demonstration):

| Check | Description |
|-------|-------------|
| C2.1 | Paper MUST follow the lifecycle phases described in the lifecycle document |
| C2.2 | Lifecycle phases referenced in paper MUST match lifecycle document terminology |
| C2.3 | If paper describes its own production process, it MUST match lifecycle document |
| C2.4 | Foundation/boundary complex assumptions MUST be consistent between documents |

## Compositional Justification

### Why This Dependency Makes Sense

Self-demonstrating papers must demonstrate that the framework works by showing it was used to produce the paper itself. The lifecycle document defines *how* assured documents are produced:

1. **Phases** → What stages the paper went through (Type Definition, Architecture, Content, Post-Processing)
2. **Gates** → What verification and validation checks the paper passed
3. **Iteration** → How the paper was refined through feedback cycles
4. **Human Accountability** → Who approved the paper at each stage

Without a lifecycle document, claims about "following the process" would be vague and unverifiable. The lifecycle document provides the reference point for checking that the paper was produced correctly.

### Difference from Inheritance

This is a **uses/has-a** relationship, not an **is-a** relationship:
- Self-demonstration spec is NOT a specialized kind of lifecycle spec
- Self-demonstration spec USES lifecycle spec to define what supporting document is needed
- The lifecycle document is a required component, not a parent type

### Difference from Assurance

This is a **compositional** relationship, not an **assurance** relationship:
- Self-demonstration spec does NOT verify against lifecycle spec
- Self-demonstration spec verifies against spec-for-spec (because it's a spec)
- This dependency captures requirements for supporting documents, not structural compliance

## Visualization Notes

In 3D visualization:
- Render as dependency edge (distinct from assurance edges)
- Color: suggest using a neutral color (gray/silver) to distinguish from verification (green) and validation (blue)
- Direction: arrow from self-demonstration-spec toward lifecycle-spec

---

**Note:** This dependency is one of four supporting document dependencies for self-demonstrating papers. The others are: architecture, literature-review, and novel-contributions.