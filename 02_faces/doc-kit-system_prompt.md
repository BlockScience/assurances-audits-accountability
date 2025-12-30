---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:system_prompt
name: Doc-Kit - System Prompt Documents
description: Complete documentation kit for system prompt documents using the PPP (Persona-Purpose-Protocol) framework
vertices:
  - v:spec:system_prompt
  - v:guidance:system_prompt
  - v:system_prompt:claude-assistant-compiled
edges:
  - e:coupling:system_prompt
  - e:verification:system_prompt-compiled:spec
  - e:validation:system_prompt-compiled:guidance
face_type: doc_kit
orientation: oriented
target: v:spec:system_prompt
spec: v:spec:system_prompt
guidance: v:guidance:system_prompt
example: v:system_prompt:claude-assistant-compiled
coupling_edge: e:coupling:system_prompt
verification_edge: e:verification:system_prompt-compiled:spec
validation_edge: e:validation:system_prompt-compiled:guidance
doc_type: system_prompt
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

# Doc-Kit - System Prompt Documents

This doc-kit provides a complete documentation package for **system prompt** documents, including the specification (structural requirements), guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [Specification for System Prompt Documents](../00_vertices/spec-for-system-prompt.md) (`v:spec:system_prompt`)
   - Defines what structural elements MUST be present
   - Requires: Purpose Statement, Persona Section (typed), Purpose Section (typed), Protocol Section (typed), Integration Validation
   - Demonstrates **typed subsection pattern** - sections must conform to other specs
   - Used for deterministic verification

2. **Guidance**: [Guidance for System Prompt Documents](../00_vertices/guidance-for-system-prompt.md) (`v:guidance:system_prompt`)
   - Defines quality criteria: Component Verification, Persona-Purpose Alignment, Purpose-Protocol Alignment, Persona-Protocol Consistency, Tone Consistency, No Contradictions, Integration Validation
   - Provides workflow guidance for PPP design order
   - Used for qualitative validation

3. **Example**: [System Prompt - Claude Knowledge Complex Assistant](../00_vertices/system_prompt-claude-assistant.md) (`v:system_prompt:claude-assistant`)
   - Demonstrates a well-formed system prompt instance
   - Shows compositional structure with embedded persona, purpose, protocol
   - Reference for creating new system prompt documents

### Edges (Boundary)

1. **Coupling Edge**: [Coupling - System Prompt](../01_edges/coupling-system_prompt.md) (`e:coupling:system_prompt`)
   - Connects [[spec-for-system-prompt]] ↔ [[guidance-for-system-prompt]]
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: [Verification - System Prompt Compiled](../01_edges/verification-system_prompt-compiled:spec.md) (`e:verification:system_prompt-compiled:spec`)
   - Example verifies against spec
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: [Validation - System Prompt Compiled](../01_edges/validation-system_prompt-compiled:guidance.md) (`e:validation:system_prompt-compiled:guidance`)
   - Example validates against guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What System Prompt Documents Are

System prompt documents define **complete AI model configurations** using the PPP (Persona-Purpose-Protocol) framework. They are **compositional documents** where each major section (Persona, Purpose, Protocol) is a **typed subsection** that must conform to its own specification.

System prompts are the integration layer that combines:
- **Persona**: WHO the AI is (identity, expertise, approach, tone, boundaries)
- **Purpose**: WHAT problem the AI solves (objectives, deliverables, constraints, success criteria)
- **Protocol**: HOW the AI works (workflow, phases, collaboration, quality checks)

**Key Innovation**: This spec demonstrates the **typed subsection pattern** - sections that must conform to other spec documents, analogous to typing fields with schema types.

### Key Characteristics

- **Compositional Structure**: Built from typed subsections (persona, purpose, protocol)
- **Design Order**: Purpose → Persona → Protocol (Purpose is the anchor)
- **Integration Validation**: Must validate component alignment
- **Tone Consistency**: Persona tone maintained throughout
- **No Contradictions**: Components must not conflict

### Type Hierarchy

**Extends**: `doc` (standard document)
**Extended By**: None (system_prompt is a leaf type)
**Composes**: `persona`, `purpose`, `protocol` (via typed subsections)
**Coupled With**: `guidance:system_prompt` (via coupling edge)

## When to Use This Document Type

### Primary Use Cases

Use system prompt documents when:

1. **Configuring AI Models**: Creating complete model configurations using PPP framework
2. **Integrating Components**: Need to combine persona, purpose, and protocol into one document
3. **Ensuring Coherence**: Want to validate that AI identity, objectives, and workflow align
4. **Typed Composition**: Want subsections that conform to other specifications
5. **Deployment-Ready**: Creating system prompts for actual AI model deployment

### When NOT to Use

Avoid system prompt documents when:

- **Single Component**: If you only need persona, purpose, or protocol individually
- **No Integration**: If components don't need to work together
- **Simple Prompts**: If PPP framework is overkill for your use case
- **Component-First**: Create individual components first, then compose into system_prompt

## How to Create System Prompt Documents

### Prerequisites

Before creating a system prompt document:

- [ ] **PPP components planned**: Know what persona, purpose, and protocol you need
- [ ] **Read spec-for-system-prompt**: Familiar with [[spec-for-system-prompt]] requirements
- [ ] **Review guidance-for-system-prompt**: Studied [[guidance-for-system-prompt]] quality criteria
- [ ] **Understand component specs**: Read [[spec-for-persona]], [[spec-for-purpose]], [[spec-for-protocol]]

### Creation Workflow (CRITICAL: Design Order)

1. **Design Purpose FIRST** (40 minutes)
   - Purpose is the anchor of PPP design
   - Define problem, objectives, deliverables, constraints, success criteria
   - Verify against [[spec-for-purpose]]
   - **Checkpoint**: Does purpose clearly define the value being delivered?

2. **Design Persona to Match** (30 minutes)
   - What expertise is needed for this Purpose?
   - Define role, expertise, approach, tone, boundaries
   - Ensure expertise enables purpose objectives
   - Verify against [[spec-for-persona]]
   - **Checkpoint**: Does persona expertise specifically enable purpose objectives?

3. **Design Protocol to Deliver** (60 minutes)
   - How to achieve Purpose through Persona?
   - Define workflow, phases, collaboration, quality, principles
   - Ensure protocol workflow achieves purpose deliverables
   - Verify against [[spec-for-protocol]]
   - **Checkpoint**: Does protocol systematically achieve purpose objectives?

4. **Compose System Prompt** (20 minutes)
   - Create system prompt document with all three sections
   - Use Obsidian embeds (`![[...]]`) for compositional documents OR inline content
   - Add purpose meta-statement at top
   - **Checkpoint**: Are all three components present and complete?

5. **Validate Integration** (20 minutes)
   - Check all components verify individually against their specs
   - Verify Persona enables Purpose
   - Verify Protocol achieves Purpose
   - Check for contradictions between components
   - Ensure tone consistency across all components
   - **Checkpoint**: Do components work together seamlessly?

**Total Estimated Time**: 2.5 hours

### Verification and Validation

**To verify your system prompt document**:
```bash
python scripts/verify_template_based.py your-system-prompt.md --templates templates
```

This checks:
- All required frontmatter fields present
- Dependencies field lists persona, purpose, protocol specs
- All required sections present (Purpose meta-statement, Persona, Purpose, Protocol, Integration Validation)
- Type field is exactly `vertex/system_prompt`

**For compositional documents (with embeds)**, compile first:
```bash
python scripts/compile_document.py your-system-prompt.md your-system-prompt-compiled.md
python scripts/verify_template_based.py your-system-prompt-compiled.md --templates templates
```

**To validate quality**:
- Review against [[guidance-for-system-prompt]] quality criteria
- Check component verification (each section passes its spec)
- Verify Persona-Purpose alignment (expertise enables objectives)
- Verify Purpose-Protocol alignment (workflow achieves deliverables)
- Check Persona-Protocol consistency (protocol reflects approach)
- Confirm tone consistency across components
- Check for contradictions
- Reference example: [[system_prompt-claude-assistant]]

## Related Document Types

### Works Together With

- **Persona**: Typed subsection defining WHO the AI is
- **Purpose**: Typed subsection defining WHAT problem is solved (design FIRST)
- **Protocol**: Typed subsection defining HOW the AI works (design LAST)
- **Compiled Documents**: System prompts can compile to standalone documents

### Part of Larger Patterns

**PPP Framework**:
- **Design Order**: Purpose → Persona → Protocol
- **Anchor Role**: Purpose is the anchor - everything else serves purpose
- **Integration**: All components must align without contradictions

**Typed Subsections Pattern**:
- Sections that conform to other specifications
- Analogous to typing fields with schemas
- Enables modular, reusable document components
- Verification requires checking both document AND subsection conformance

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Wrong Design Order** | Designing persona or protocol before purpose | ALWAYS design Purpose → Persona → Protocol |
| **Components in Isolation** | No integration between sections | Design each component with others in mind |
| **Misaligned Expertise** | Persona doesn't enable Purpose | Ensure persona expertise specifically supports purpose objectives |
| **Protocol Doesn't Achieve Purpose** | Workflow doesn't deliver | Map protocol phases to purpose objectives explicitly |
| **Contradictions** | Boundaries vs constraints conflict | Check alignment: persona boundaries should match purpose constraints |
| **Inconsistent Tone** | Tone varies across components | Verify tone in persona is maintained in purpose and protocol |
| **Failed Component Verification** | Subsection doesn't meet its spec | Each section MUST verify against its spec before integration |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: Excellent
**Rationale**: Spec-for-system-prompt and guidance-for-system-prompt both address system prompt documents consistently, with clear separation of structural requirements from quality criteria
**Evidence**: [[coupling-system_prompt]] documents alignment between structural requirements and quality assessment

### Example Verification

**Assessment**: Pass
**Rationale**: Example (system_prompt-claude-assistant) passes all structural checks against spec-for-system-prompt
**Evidence**: Verification results - all checks passed via `verify_template_based.py`
**Reference**: [[verification-system_prompt-compiled:spec]]

### Example Validation

**Assessment**: Excellent
**Rationale**: Example demonstrates quality criteria effectively - all components verify, align, and work together coherently
**Evidence**: Validation assessment against guidance criteria
**Reference**: [[validation-system_prompt-compiled:guidance]]

### Kit Completeness

**Assessment**: Complete
**Rationale**: This kit provides everything needed to create good system prompt documents
**Evidence**:
- ✓ Spec is complete and demonstrates typed subsection pattern
- ✓ Guidance is actionable with clear design order workflow
- ✓ Example demonstrates best practices (compositional Claude assistant)
- ✓ Usage context is sufficient
- ✓ Pitfalls and solutions documented

## Overall Doc-Kit Assessment

**Status**: COMPLETE

**Summary**: The system prompt doc-kit provides a complete, high-quality documentation package for system prompt documents. The spec defines structural requirements including typed subsections, the guidance provides quality criteria for component integration, and the example demonstrates effective PPP framework usage.

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✓ **Assurance Triangle**: Complete and coherent (spec, guidance, example, 3 edges)
2. ✓ **Usage Context**: Clear explanation of when/why to use this type
3. ✓ **Creation Workflow**: 5-step workflow with checkpoints and design order
4. ✓ **Quality Example**: Example passes verification AND validation
5. ✓ **Relationship Documentation**: Clear how system_prompt relates to PPP components
6. ✓ **Pitfall Guidance**: 7 common mistakes and solutions documented

**Conclusion**: This doc-kit successfully helps users create good system prompt documents by providing complete structural requirements, quality guidance, and a practical example of the PPP framework.

## Accountability Statement

This doc-kit assessment was generated with assistance from claude-opus-4-5, reviewed and approved by mzargham.

**Maintainer:** mzargham
**Assurer:** mzargham
**Date:** 2025-12-29

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | system_prompt |
| Specification | [`v:spec:system_prompt`](../00_vertices/spec-for-system-prompt.md) |
| Guidance | [`v:guidance:system_prompt`](../00_vertices/guidance-for-system-prompt.md) |
| Example | [`v:system_prompt:claude-assistant`](../00_vertices/system_prompt-claude-assistant.md) |
| Coupling Edge | [`e:coupling:system_prompt`](../01_edges/coupling-system_prompt.md) |
| Verification Edge | [`e:verification:system_prompt-compiled:spec`](../01_edges/verification-system_prompt-compiled:spec.md) |
| Validation Edge | [`e:validation:system_prompt-compiled:guidance`](../01_edges/validation-system_prompt-compiled:guidance.md) |
| Assurance Status | COMPLETE |
| Maintainer | mzargham |
| Last Updated | 2025-12-29 |

## Examples in the Wild

Beyond the canonical example, system prompts in this knowledge complex include:

- [`v:system_prompt:claude-assistant`](../00_vertices/system_prompt-claude-assistant.md): Compositional system prompt using Obsidian embeds
- [`v:system_prompt:claude-assistant-compiled`](../00_vertices/system_prompt-claude-assistant-compiled.md): Compiled standalone version with embeds expanded

---

**Note**: This doc-kit is the capstone of the PPP framework documentation. System prompts demonstrate the **typed subsection pattern** where sections must conform to other specifications, enabling modular, reusable document components.
