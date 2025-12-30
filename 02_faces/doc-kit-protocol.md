---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:protocol
name: Doc-Kit - Protocol Documents
description: Complete documentation kit for protocol documents including spec, guidance, and example from PPP framework
vertices:
  - v:spec:protocol
  - v:guidance:protocol
  - v:protocol:claude-assistant
edges:
  - e:coupling:protocol
  - e:verification:protocol-claude:spec
  - e:validation:protocol-claude:guidance
face_type: doc_kit
orientation: oriented
target: v:spec:protocol
spec: v:spec:protocol
guidance: v:guidance:protocol
example: v:protocol:claude-assistant
coupling_edge: e:coupling:protocol
verification_edge: e:verification:protocol-claude:spec
validation_edge: e:validation:protocol-claude:guidance
doc_type: protocol
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

# Doc-Kit - Protocol Documents

This doc-kit provides a complete documentation package for **protocol** documents, including the specification (structural requirements), guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [Specification for Protocol Documents](../00_vertices/spec-for-protocol.md) (`v:spec:protocol`)
   - Defines what structural elements MUST be present
   - Requires: Purpose Statement, Workflow Overview, Phase Definitions (3-5), User Collaboration Points, Quality Assurance, Tools and Scripts, Consistent Principles (3-5)
   - Used for deterministic verification

2. **Guidance**: [Guidance for Protocol Documents](../00_vertices/guidance-for-protocol.md) (`v:guidance:protocol`)
   - Defines quality criteria: Workflow Clarity, Phase Structure, Collaboration Balance, Quality Rigor, Principle Consistency, Tool Documentation
   - Provides section-by-section authoring advice
   - Used for qualitative validation

3. **Example**: [Protocol - Claude Knowledge Complex Assistant](../00_vertices/protocol-claude-assistant.md) (`v:protocol:claude-assistant`)
   - Demonstrates a well-formed protocol instance
   - Shows 4-phase workflow with clear steps, collaboration points, and tool documentation
   - Reference for creating new protocol documents

### Edges (Boundary)

1. **Coupling Edge**: [Coupling - Protocol](../01_edges/coupling-protocol.md) (`e:coupling:protocol`)
   - Connects [[spec-for-protocol]] ↔ [[guidance-for-protocol]]
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: [Verification - Protocol Claude](../01_edges/verification-protocol-claude:spec.md) (`e:verification:protocol-claude:spec`)
   - Example verifies against spec
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: [Validation - Protocol Claude](../01_edges/validation-protocol-claude:guidance.md) (`e:validation:protocol-claude:guidance`)
   - Example validates against guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What Protocol Documents Are

Protocol documents define **how the AI works systematically** - the workflow, phases, user collaboration points, quality assurance, and consistent principles. In the PPP (Persona-Purpose-Protocol) framework, protocol is designed **LAST** because it operationalizes purpose objectives through persona expertise.

Protocols establish systematic workflows with clear phases, defined outputs, and explicit quality checks. They specify when and how to engage users, document the tools used, and define cross-phase principles that ensure consistent behavior.

### Key Characteristics

- **Phased Workflow**: 3-5 distinct phases with clear triggers and transitions
- **Actionable Steps**: Concrete, executable steps (3-6 per phase)
- **User Collaboration**: Explicit points for validation, input, and approval
- **Quality Assurance**: Defined checks for input, process, and output
- **Tool Documentation**: Explicit enumeration of all tools used
- **Consistent Principles**: Cross-phase behaviors that apply throughout

### Type Hierarchy

**Extends**: `doc` (standard document)
**Extended By**: None (protocol is a leaf type in the PPP framework)
**Composes**: None (protocol is atomic, not compositional)
**Used In**: `system_prompt` (as a typed subsection)

## When to Use This Document Type

### Primary Use Cases

Use protocol documents when:

1. **Completing PPP Design**: Creating the "how" component of Persona-Purpose-Protocol (design LAST)
2. **Defining Systematic Workflows**: Need to specify phased work processes with quality gates
3. **Documenting Tool Usage**: Want to explicitly enumerate tools and when to use them
4. **Establishing User Collaboration**: Need to define when and how to engage users
5. **Ensuring Consistent Behavior**: Want cross-phase principles that guide all work

### When NOT to Use

Avoid protocol documents when:

- **Describing Identity**: If you're defining WHO the AI is, you want Persona (not Protocol)
- **Defining Value**: If you're describing WHAT problem is solved, you want Purpose (not Protocol)
- **Protocol Before Purpose**: Don't start Protocol until Purpose and Persona are defined
- **Non-Systematic Work**: If workflow doesn't need phases or quality gates, protocol may be overkill

## How to Create Protocol Documents

### Prerequisites

Before creating a protocol document:

- [ ] **Purpose is defined**: Know what objectives the protocol must achieve
- [ ] **Persona is defined**: Know what expertise/approach the protocol will use
- [ ] **Workflow is clear**: Have a mental model of the phases
- [ ] **Read the spec**: Familiar with [[spec-for-protocol]] requirements
- [ ] **Review guidance**: Studied [[guidance-for-protocol]] quality criteria

### Creation Workflow

1. **Review Purpose and Persona** (10 minutes)
   - Understand what objectives protocol must achieve
   - Identify what persona expertise is available
   - Consider how workflow integrates both
   - **Checkpoint**: Can you state the goal of the workflow?

2. **Define Phases** (20 minutes)
   - Identify 3-5 distinct phases
   - For each phase: trigger, 3-6 steps, outputs, transition
   - Ensure logical progression between phases
   - **Checkpoint**: Do phases cover full workflow with clear transitions?

3. **Specify User Collaboration** (10 minutes)
   - Define validation points (when to confirm findings)
   - Define input gathering (when to ask questions)
   - Define approval steps (when to get permission)
   - **Checkpoint**: Is user engagement balanced (not too frequent, not absent)?

4. **Define Quality Assurance** (15 minutes)
   - Input validation (what to check before starting)
   - Process verification (what to check during)
   - Output quality checks (what to check in deliverables)
   - Error prevention (how to avoid common mistakes)
   - **Checkpoint**: Are quality gates defined for each phase?

5. **Document Tools and Principles** (15 minutes)
   - List all tools referenced in phases
   - For each: path, when to use, what it does, command syntax
   - Define 3-5 cross-phase principles
   - **Checkpoint**: Are all tools documented? Are principles cross-cutting?

**Total Estimated Time**: 70 minutes

### Verification and Validation

**To verify your protocol document**:
```bash
python scripts/verify_template_based.py your-protocol.md --templates templates
```

This checks:
- All required frontmatter fields present
- All required sections present (Purpose, Workflow Overview, Phase Definitions, User Collaboration Points, Quality Assurance, Tools and Scripts, Consistent Principles)
- Phase Definitions includes 3-5 phases
- Each phase has trigger, steps (3-6), outputs, transition
- Consistent Principles lists 3-5 items

**To validate quality**:
- Review against [[guidance-for-protocol]] quality criteria
- Check workflow clarity (understandable phases, logical flow)
- Verify phase structure (proper triggers, outputs, transitions)
- Assess collaboration balance (appropriate user engagement)
- Evaluate quality rigor (comprehensive checks)
- Confirm tool documentation completeness
- Reference example: [[protocol-claude-assistant]]

## Related Document Types

### Works Together With

- **Purpose**: Protocol achieves purpose objectives (design protocol AFTER purpose)
- **Persona**: Protocol uses persona expertise and reflects persona approach
- **System Prompt**: Protocol is a typed subsection in compositional system_prompt documents

### Part of Larger Patterns

**PPP Framework** (Persona-Purpose-Protocol):
- **Design order**: Purpose → Persona → Protocol (LAST)
- **Integration role**: Protocol integrates persona expertise to achieve purpose objectives
- **Operational focus**: Protocol defines HOW, not WHO or WHAT

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Vague Steps** | Steps like "analyze stuff" aren't executable | Use concrete, specific actions (3-6 per phase) |
| **Too Many Phases** | More than 5 phases adds unnecessary complexity | Consolidate into 3-5 well-defined phases |
| **Missing Transitions** | Unclear how to move between phases | Each phase must specify "Next:" transition |
| **No User Engagement** | Protocol runs without collaboration | Add validation points, input gathering, approvals |
| **Undocumented Tools** | Tools mentioned but not documented | List ALL tools with path, when, what, command |
| **Phase-Specific Principles** | Principles only apply to one phase | Principles must be cross-cutting (apply to all phases) |
| **Protocol Before Purpose** | Designing workflow without knowing objectives | Protocol is LAST in PPP - design after purpose and persona |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: Excellent
**Rationale**: Spec and guidance both address protocol documents consistently, with matching section requirements and quality criteria
**Evidence**: [[coupling-protocol]] documents alignment between structural requirements and quality assessment

### Example Verification

**Assessment**: Pass
**Rationale**: Example passes all structural checks against spec - 4 phases with proper structure, complete tool documentation
**Evidence**: Verification results - all checks passed via `verify_template_based.py`
**Reference**: [[verification-protocol-claude:spec]]

### Example Validation

**Assessment**: Excellent
**Rationale**: Example demonstrates quality criteria effectively - clear phases, balanced collaboration, comprehensive quality checks, complete tool documentation
**Evidence**: Validation assessment against guidance criteria
**Reference**: [[validation-protocol-claude:guidance]]

### Kit Completeness

**Assessment**: Complete
**Rationale**: This kit provides everything needed to create good protocol documents
**Evidence**:
- ✓ Spec is complete and clear
- ✓ Guidance is actionable and comprehensive
- ✓ Example demonstrates best practices
- ✓ Usage context is sufficient
- ✓ Pitfalls and solutions documented

## Overall Doc-Kit Assessment

**Status**: COMPLETE

**Summary**: The protocol doc-kit provides a complete, high-quality documentation package for protocol documents. The spec defines structural requirements for phased workflows, the guidance provides quality criteria for systematic design, and the example demonstrates effective protocol creation within the PPP framework.

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✓ **Assurance Triangle**: Complete and coherent (spec, guidance, example, 3 edges)
2. ✓ **Usage Context**: Clear explanation of when/why to use this type
3. ✓ **Creation Workflow**: 5-step workflow with checkpoints documented
4. ✓ **Quality Example**: Example passes verification AND validation
5. ✓ **Relationship Documentation**: Clear how protocol relates to persona, purpose, system_prompt
6. ✓ **Pitfall Guidance**: 7 common mistakes and solutions documented

**Conclusion**: This doc-kit successfully helps users create good protocol documents by providing complete structural requirements, quality guidance, and a practical example.

## Accountability Statement

This doc-kit assessment was generated with assistance from claude-opus-4-5, reviewed and approved by mzargham.

**Maintainer:** mzargham
**Assurer:** mzargham
**Date:** 2025-12-29

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | protocol |
| Specification | [`v:spec:protocol`](../00_vertices/spec-for-protocol.md) |
| Guidance | [`v:guidance:protocol`](../00_vertices/guidance-for-protocol.md) |
| Example | [`v:protocol:claude-assistant`](../00_vertices/protocol-claude-assistant.md) |
| Coupling Edge | [`e:coupling:protocol`](../01_edges/coupling-protocol.md) |
| Verification Edge | [`e:verification:protocol-claude:spec`](../01_edges/verification-protocol-claude:spec.md) |
| Validation Edge | [`e:validation:protocol-claude:guidance`](../01_edges/validation-protocol-claude:guidance.md) |
| Assurance Status | COMPLETE |
| Maintainer | mzargham |
| Last Updated | 2025-12-29 |

## Examples in the Wild

Beyond the canonical example, other protocol documents in this knowledge complex include:

- [`v:protocol:claude-assistant`](../00_vertices/protocol-claude-assistant.md): Demonstrates comprehensive 4-phase workflow for knowledge complex development

---

**Note**: This doc-kit is part of the PPP framework documentation. Protocol is designed **LAST** - it integrates persona expertise to achieve purpose objectives through systematic workflow.
