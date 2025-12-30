---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:purpose
name: Doc-Kit - Purpose Documents
description: Complete documentation kit for purpose documents including spec, guidance, and example from PPP framework
vertices:
  - v:spec:purpose
  - v:guidance:purpose
  - v:purpose:claude-assistant
edges:
  - e:coupling:purpose
  - e:verification:purpose-claude:spec
  - e:validation:purpose-claude:guidance
face_type: doc_kit
orientation: oriented
target: v:spec:purpose
spec: v:spec:purpose
guidance: v:guidance:purpose
example: v:purpose:claude-assistant
coupling_edge: e:coupling:purpose
verification_edge: e:verification:purpose-claude:spec
validation_edge: e:validation:purpose-claude:guidance
doc_type: purpose
assurer: mzargham
assurance_method: llm-assisted
llm_model: claude-opus-4-5
human_approver: mzargham
maintainer: mzargham
tags:
  - face
  - assurance
  - doc_kit
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
---

# Doc-Kit - Purpose Documents

This doc-kit provides a complete documentation package for **purpose** documents, including the specification (structural requirements), guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [Specification for Purpose Documents](../00_vertices/spec-for-purpose.md) (`v:spec:purpose`)
   - Defines what structural elements MUST be present
   - Requires: Purpose Statement, Problem Statement, Core Objectives (3-6), Specific Deliverables (≥2), Constraints and Boundaries (≥3), Success Criteria
   - Used for deterministic verification

2. **Guidance**: [Guidance for Purpose Documents](../00_vertices/guidance-for-purpose.md) (`v:guidance:purpose`)
   - Defines quality criteria: Problem Specificity, Objectives Quality, Deliverable Concreteness, Constraint Clarity, Success Measurability, User-Centeredness
   - Provides section-by-section authoring advice
   - Used for qualitative validation

3. **Example**: [Purpose - Claude Knowledge Complex Assistant](../00_vertices/purpose-claude-assistant.md) (`v:purpose:claude-assistant`)
   - Demonstrates a well-formed purpose instance
   - Shows how to define problem, objectives, deliverables, constraints, success criteria
   - Reference for creating new purpose documents

### Edges (Boundary)

1. **Coupling Edge**: [Coupling - Purpose](../01_edges/coupling-purpose.md) (`e:coupling:purpose`)
   - Connects [[spec-for-purpose]] ↔ [[guidance-for-purpose]]
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: [Verification - Purpose Claude](../01_edges/verification-purpose-claude:spec.md) (`e:verification:purpose-claude:spec`)
   - Example verifies against spec
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: [Validation - Purpose Claude](../01_edges/validation-purpose-claude:guidance.md) (`e:validation:purpose-claude:guidance`)
   - Example validates against guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What Purpose Documents Are

Purpose documents define **what problem the AI solves** - the user need, core objectives, specific deliverables, constraints, and success criteria. In the PPP (Persona-Purpose-Protocol) framework, purpose is the **anchor** that is designed FIRST. It establishes what value is delivered, which then informs persona expertise and protocol workflow.

Purpose documents are user-centered by design. They focus on the problem being solved, not AI capabilities. They define measurable success criteria and explicit constraints to prevent scope creep.

### Key Characteristics

- **User-Centered Problem**: Addresses real user needs, not AI features
- **Measurable Objectives**: 3-6 specific objectives using action verbs
- **Typed Deliverables**: Concrete artifacts with spec references
- **Explicit Constraints**: Clear boundaries to manage expectations
- **Verifiable Success**: Measurable criteria for determining success

### Type Hierarchy

**Extends**: `doc` (standard document)
**Extended By**: None (purpose is a leaf type in the PPP framework)
**Composes**: None (purpose is atomic, not compositional)
**Used In**: `system_prompt` (as a typed subsection)

## When to Use This Document Type

### Primary Use Cases

Use purpose documents when:

1. **Anchoring PPP Design**: Creating the "what problem" component of Persona-Purpose-Protocol (design FIRST)
2. **Defining AI Value**: Need to clearly state what value an AI model delivers
3. **Managing Scope**: Want to prevent scope creep through explicit constraints
4. **Enabling Measurement**: Need verifiable success criteria for AI work

### When NOT to Use

Avoid purpose documents when:

- **Describing Identity**: If you're defining WHO the AI is, you want Persona (not Purpose)
- **Defining Workflow**: If you're describing HOW work gets done step-by-step, you want Protocol (not Purpose)
- **Purpose Before Requirements**: Don't start Purpose until you understand user needs
- **Feature Lists**: Purpose is not a capability list - focus on problems solved

## How to Create Purpose Documents

### Prerequisites

Before creating a purpose document:

- [ ] **User needs are clear**: Understand what problem users face
- [ ] **Use case is defined**: Know the context where this AI will be used
- [ ] **Read the spec**: Familiar with [[spec-for-purpose]] requirements
- [ ] **Review guidance**: Studied [[guidance-for-purpose]] quality criteria

### Creation Workflow

1. **Identify Core Problem** (10 minutes)
   - What struggle do users face?
   - What takes too much time without help?
   - State specific user problem, not general "help"
   - **Checkpoint**: Can you state the problem using "help users [solve specific problem]"?

2. **Define Objectives** (15 minutes)
   - List 3-6 specific objectives
   - Use action verbs (analyzing, extracting, generating, validating)
   - Ensure each objective directly addresses the problem
   - **Checkpoint**: Are objectives measurable and realistic?

3. **Specify Deliverables** (10 minutes)
   - Name specific artifacts users will receive
   - Reference specs for deliverable types (e.g., "conforming to [[spec-for-charts]]")
   - List at least 2 concrete deliverables
   - **Checkpoint**: Can you name the specific outputs?

4. **Set Constraints** (10 minutes)
   - Define what is OUT of scope
   - List at least 3 explicit boundaries
   - Manage expectations realistically
   - **Checkpoint**: Are boundaries clear to prevent scope creep?

5. **Define Success Criteria** (10 minutes)
   - Make criteria measurable, not subjective
   - Mix quality, completeness, usability measures
   - Use format: "Your work is successful when:"
   - **Checkpoint**: Can success be verified?

**Total Estimated Time**: 55 minutes

### Verification and Validation

**To verify your purpose document**:
```bash
python scripts/verify_template_based.py your-purpose.md --templates templates
```

This checks:
- All required frontmatter fields present
- All required sections present (Purpose, Problem Statement, Core Objectives, Specific Deliverables, Constraints and Boundaries, Success Criteria)
- Core Objectives lists 3-6 items
- Specific Deliverables lists ≥2 items
- Constraints and Boundaries lists ≥3 items

**To validate quality**:
- Review against [[guidance-for-purpose]] quality criteria
- Check problem specificity (user-centered, not feature-focused)
- Verify objectives quality (action verbs, measurable)
- Assess deliverable concreteness (typed with spec references)
- Evaluate constraint clarity (explicit boundaries)
- Confirm success measurability (verifiable criteria)
- Reference example: [[purpose-claude-assistant]]

## Related Document Types

### Works Together With

- **Persona**: Persona expertise must enable purpose objectives (design persona AFTER purpose)
- **Protocol**: Protocol operationalizes purpose objectives through persona expertise
- **System Prompt**: Purpose is a typed subsection in compositional system_prompt documents

### Part of Larger Patterns

**PPP Framework** (Persona-Purpose-Protocol):
- **Design order**: Purpose (FIRST) → Persona → Protocol
- **Anchor role**: Purpose is the anchor - everything else serves the defined purpose
- **Integration**: Persona matches expertise to purpose, Protocol achieves purpose through persona

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too Broad** | Trying to solve too many problems | Narrow focus to specific problem area |
| **Feature-Focused** | Describing AI capabilities instead of user problems | Reframe: what problem does this solve for users? |
| **No Constraints** | Unlimited scope invites scope creep | Explicitly state what's out of scope (3+ items) |
| **Unmeasurable Success** | "Users are happy" can't be verified | Use verifiable criteria (tests pass, tasks completed) |
| **Vague Objectives** | "Help users" isn't actionable | Use action verbs + specific outcomes |
| **Untyped Deliverables** | Deliverables without spec references | Reference specs explicitly; create new spec if needed |
| **Purpose Last** | Designing purpose after persona/protocol | Purpose is the ANCHOR - design it FIRST |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: Excellent
**Rationale**: Spec and guidance both address purpose documents consistently, with matching section requirements and quality criteria
**Evidence**: [[coupling-purpose]] documents alignment between structural requirements and quality assessment

### Example Verification

**Assessment**: Pass
**Rationale**: Example passes all structural checks against spec
**Evidence**: Verification results - all checks passed via `verify_template_based.py`
**Reference**: [[verification-purpose-claude:spec]]

### Example Validation

**Assessment**: Excellent
**Rationale**: Example demonstrates quality criteria effectively - user-centered problem, measurable objectives, typed deliverables, clear constraints
**Evidence**: Validation assessment against guidance criteria
**Reference**: [[validation-purpose-claude:guidance]]

### Kit Completeness

**Assessment**: Complete
**Rationale**: This kit provides everything needed to create good purpose documents
**Evidence**:
- ✓ Spec is complete and clear
- ✓ Guidance is actionable and comprehensive
- ✓ Example demonstrates best practices
- ✓ Usage context is sufficient
- ✓ Pitfalls and solutions documented

## Overall Doc-Kit Assessment

**Status**: COMPLETE

**Summary**: The purpose doc-kit provides a complete, high-quality documentation package for purpose documents. The spec defines structural requirements, the guidance provides quality criteria and authoring advice, and the example demonstrates effective purpose definition within the PPP framework.

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✓ **Assurance Triangle**: Complete and coherent (spec, guidance, example, 3 edges)
2. ✓ **Usage Context**: Clear explanation of when/why to use this type
3. ✓ **Creation Workflow**: 5-step workflow with checkpoints documented
4. ✓ **Quality Example**: Example passes verification AND validation
5. ✓ **Relationship Documentation**: Clear how purpose relates to persona, protocol, system_prompt
6. ✓ **Pitfall Guidance**: 7 common mistakes and solutions documented

**Conclusion**: This doc-kit successfully helps users create good purpose documents by providing complete structural requirements, quality guidance, and a practical example.

## Accountability Statement

This doc-kit assessment was generated with assistance from claude-opus-4-5, reviewed and approved by mzargham.

**Maintainer:** mzargham
**Assurer:** mzargham
**Date:** 2025-12-29

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | purpose |
| Specification | [`v:spec:purpose`](../00_vertices/spec-for-purpose.md) |
| Guidance | [`v:guidance:purpose`](../00_vertices/guidance-for-purpose.md) |
| Example | [`v:purpose:claude-assistant`](../00_vertices/purpose-claude-assistant.md) |
| Coupling Edge | [`e:coupling:purpose`](../01_edges/coupling-purpose.md) |
| Verification Edge | [`e:verification:purpose-claude:spec`](../01_edges/verification-purpose-claude:spec.md) |
| Validation Edge | [`e:validation:purpose-claude:guidance`](../01_edges/validation-purpose-claude:guidance.md) |
| Assurance Status | COMPLETE |
| Maintainer | mzargham |
| Last Updated | 2025-12-29 |

## Examples in the Wild

Beyond the canonical example, other purpose documents in this knowledge complex include:

- [`v:purpose:claude-assistant`](../00_vertices/purpose-claude-assistant.md): Demonstrates comprehensive purpose for knowledge complex assistant role

---

**Note**: This doc-kit is part of the PPP framework documentation. Purpose is the **anchor** of PPP design - it should be created FIRST to establish what value is delivered, before persona and protocol.
