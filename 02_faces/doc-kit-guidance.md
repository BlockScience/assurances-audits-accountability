---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:guidance
name: Doc-Kit - Guidance Documents
description: Complete documentation kit for guidance documents including spec, guidance-for-guidance, and canonical example
vertices:
  - v:spec:guidance
  - v:guidance:guidance
  - v:guidance:purpose
edges:
  - e:coupling:guidance
  - e:verification:purpose-guidance:guidance
  - e:validation:purpose-guidance:guidance-guidance
face_type: doc_kit
orientation: oriented
target: v:spec:guidance
spec: v:spec:guidance
guidance: v:guidance:guidance
example: v:guidance:purpose
coupling_edge: e:coupling:guidance
verification_edge: e:verification:guidance-purpose:spec
validation_edge: e:validation:guidance-purpose:guidance
doc_type: guidance
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

# Doc-Kit - Guidance Documents

This doc-kit provides a complete documentation package for **guidance** documents, including the specification (structural requirements), guidance-for-guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [Specification for Guidance Documents](../00_vertices/spec-for-guidance.md) (`v:spec:guidance`)
   - Defines what structural elements MUST be present in any guidance
   - Requires: Purpose, Document Overview, Quality Criteria (≥3 with ≥2 levels each), Section-by-Section Guidance
   - Used for deterministic verification

2. **Guidance**: [Guidance for Guidance Documents](../00_vertices/guidance-for-guidance.md) (`v:guidance:guidance`)
   - Defines quality criteria: Empathy and Clarity, Actionability, Comprehensiveness, Leveled Assessment, Usability, Self-Consistency, Obsidian Compatibility
   - Self-referential: validates itself
   - Provides section-by-section authoring advice
   - Used for qualitative validation

3. **Example**: [Guidance for Purpose Documents](../00_vertices/guidance-for-purpose.md) (`v:guidance:purpose`)
   - Demonstrates a well-formed guidance instance
   - Shows quality criteria, section guidance, workflow, best practices
   - Reference for creating new guidance documents

### Edges (Boundary)

1. **Coupling Edge**: [Coupling - Guidance](../01_edges/coupling-guidance.md) (`e:coupling:guidance`)
   - Connects [[spec-for-guidance]] ↔ [[guidance-for-guidance]]
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: Verification - Guidance Purpose (`e:verification:guidance-purpose:spec`)
   - Example verifies against spec-for-guidance
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: Validation - Guidance Purpose (`e:validation:guidance-purpose:guidance`)
   - Example validates against guidance-for-guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What Guidance Documents Are

Guidance documents define **quality criteria** and **best practices** - the "how well" of documentation. While specs define what MUST be present (structure), guidance defines what makes a document good (quality). Guidance uses descriptive, evaluative language and assesses quality on a spectrum, not pass/fail.

Guidance documents are the qualitative complement to specifications. Every spec should have a corresponding guidance document, linked via a coupling edge. Together, they form a complete documentation package: verification (against spec) checks structure, validation (against guidance) assesses quality.

### Key Characteristics

- **Quality Focus**: Defines assessment criteria, not structure
- **Leveled Assessment**: Quality on a spectrum (Excellent/Good/Needs Improvement)
- **Actionable Advice**: Specific, practical tips for each section
- **Self-Referential**: Guidance-for-guidance validates itself
- **Paired with Specs**: Every guidance has a corresponding specification

### Type Hierarchy

**Extends**: `doc` (standard document)
**Extended By**: None (guidance is a leaf type)
**Composes**: None (guidance is atomic)
**Coupled With**: `spec` (via coupling edge)

## When to Use This Document Type

### Primary Use Cases

Use guidance documents when:

1. **Complementing Specifications**: Creating quality criteria for a document type that has a spec
2. **Enabling Validation**: Need qualitative assessment beyond structural verification
3. **Teaching Best Practices**: Want to help users create excellent documents
4. **Establishing Standards**: Defining what "good" looks like for your organization
5. **Creating Coupling Pairs**: Guidance always pairs with specs

### When NOT to Use

Avoid guidance documents when:

- **Defining Structure**: Structural requirements belong in specs, not guidance
- **Binary Criteria**: If requirements are pass/fail, they belong in specs
- **Without Spec Pair**: Every guidance needs corresponding specification
- **Abstract Quality**: Guidance must be specific and actionable, not platitudes

## How to Create Guidance Documents

### Prerequisites

Before creating a guidance document:

- [ ] **Spec exists**: Know the corresponding specification
- [ ] **Read spec-for-guidance**: Familiar with [[spec-for-guidance]] requirements
- [ ] **Review guidance-for-guidance**: Studied [[guidance-for-guidance]] quality criteria
- [ ] **Understand audience**: Know who will use this guidance

### Creation Workflow

1. **Understand the Spec** (15-30 minutes)
   - Read the corresponding specification thoroughly
   - Identify structural requirements
   - Note areas where quality can vary despite structural compliance
   - **Checkpoint**: Can you identify where quality differs from structure?

2. **Draft Quality Criteria** (30-45 minutes)
   - Identify 4-7 distinct quality dimensions
   - Define 2-3 levels for each (Excellent/Good/Needs Improvement)
   - Make levels observable, not subjective
   - **Checkpoint**: Can you distinguish levels for each criterion without ambiguity?

3. **Create Section Guidance** (45-60 minutes)
   - For each section in the supported document type:
     - Purpose (why it exists)
     - Tips (3-5 specific, actionable tips)
     - Anti-patterns with solutions
   - **Checkpoint**: Could someone new to the domain use your guidance successfully?

4. **Design Workflow** (20-30 minutes)
   - Break supported document creation into 3-5 phases
   - Estimate time for each phase
   - Define quality checkpoints
   - **Checkpoint**: Does the workflow feel natural and complete?

5. **Document Common Issues** (20-30 minutes)
   - List 4-8 predictable mistakes
   - Provide specific solutions in table format
   - Draw from real experience
   - **Checkpoint**: Have you covered the most frequent problems?

6. **Articulate Best Practices** (15-30 minutes)
   - Distill lessons into 8-12 practices
   - Make each independently actionable
   - Order from foundational to advanced
   - **Checkpoint**: Is each practice specific enough to act on?

7. **Review for Self-Consistency** (15-30 minutes)
   - Check that guidance demonstrates its own criteria
   - Verify actionability of all advice
   - Ensure comprehensiveness
   - **Checkpoint**: Does this guidance demonstrate excellent quality per its own criteria?

**Total Estimated Time**: 3-4 hours

### Verification and Validation

**To verify your guidance document**:
```bash
python scripts/verify_template_based.py your-guidance.md --templates templates
```

This checks:
- All required frontmatter fields present
- All required sections present (Purpose, Document Overview, Quality Criteria, Section-by-Section Guidance)
- Quality Criteria section has ≥3 criteria with ≥2 levels each
- Type field is exactly `vertex/guidance`

**To validate quality**:
- Review against [[guidance-for-guidance]] quality criteria
- Check empathy and clarity (anticipates user needs)
- Verify actionability (every tip is specific enough to act on)
- Assess comprehensiveness (covers all major sections)
- Confirm leveled assessment (meaningful level distinctions)
- Evaluate usability (well-organized, scannable)
- Check self-consistency (demonstrates own criteria)
- Reference example: [[guidance-for-purpose]]

## Related Document Types

### Works Together With

- **Specification**: Every guidance has a corresponding spec (coupled via coupling edge)
- **All Document Types**: Guidance documents can be created for any document type
- **Validation Edges**: Validation edges reference guidance for qualitative assessment

### Part of Larger Patterns

**Spec-Guidance Coupling**:
- Every document type has a spec (structure) and guidance (quality)
- They're linked via a coupling edge
- Verification checks spec; validation checks guidance
- Assurance combines both via assurance triangle

**Quality Assessment**:
- Guidance enables validation (qualitative assessment)
- Specs enable verification (structural checking)
- Together they provide complete quality infrastructure

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too Abstract** | Advice like "be thoughtful" or "use good judgment" | Provide specific criteria: "Include at least 3 examples" |
| **Structural Focus** | Guidance reads like a spec (required fields, formats) | Move structural requirements to spec; focus on quality |
| **No Levels** | Binary good/bad assessment | Define 2-3 quality levels with observable distinctions |
| **Missing Context** | Criteria without explanation of why they matter | Add "Purpose" to each criterion showing user benefit |
| **Overwhelming** | 20+ criteria or 30+ best practices | Consolidate to 4-7 criteria, 8-12 practices |
| **No Examples** | Only abstract principles | Add concrete examples, anti-patterns, or reference documents |
| **Missing Workflow** | No guidance on authoring sequence | Add phases, time estimates, and quality checkpoints |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: Excellent
**Rationale**: Spec-for-guidance and guidance-for-guidance both address guidance documents consistently, with clear separation of structural requirements from quality criteria
**Evidence**: [[coupling-guidance]] documents alignment between structural requirements and quality assessment

### Example Verification

**Assessment**: Pass
**Rationale**: Example (guidance-for-purpose) passes all structural checks against spec-for-guidance
**Evidence**: Verification results - all checks passed via `verify_template_based.py`
**Reference**: Verification of guidance-for-purpose against spec-for-guidance

### Example Validation

**Assessment**: Excellent
**Rationale**: Example demonstrates quality criteria effectively - clear quality criteria, actionable section guidance, comprehensive workflow, useful best practices
**Evidence**: Validation assessment against guidance-for-guidance criteria
**Reference**: Validation of guidance-for-purpose against guidance-for-guidance

### Kit Completeness

**Assessment**: Complete
**Rationale**: This kit provides everything needed to create good guidance documents
**Evidence**:
- ✓ Spec is complete and clear
- ✓ Guidance is actionable, comprehensive, and self-referential
- ✓ Example demonstrates best practices
- ✓ Usage context is sufficient
- ✓ Pitfalls and solutions documented

## Overall Doc-Kit Assessment

**Status**: COMPLETE

**Summary**: The guidance doc-kit provides a complete, high-quality documentation package for guidance documents. The spec defines structural requirements, the guidance-for-guidance defines quality criteria and is self-referential, and the example demonstrates effective guidance creation.

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✓ **Assurance Triangle**: Complete and coherent (spec, guidance, example, 3 edges)
2. ✓ **Usage Context**: Clear explanation of when/why to use this type
3. ✓ **Creation Workflow**: 7-step workflow with checkpoints documented
4. ✓ **Quality Example**: Example passes verification AND validation
5. ✓ **Relationship Documentation**: Clear how guidance relates to specs, coupling, type system
6. ✓ **Pitfall Guidance**: 7 common mistakes and solutions documented

**Conclusion**: This doc-kit successfully helps users create good guidance documents by providing complete structural requirements, quality guidance, and a practical example.

## Accountability Statement

This doc-kit assessment was generated with assistance from claude-opus-4-5, reviewed and approved by mzargham.

**Maintainer:** mzargham
**Assurer:** mzargham
**Date:** 2025-12-29

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | guidance |
| Specification | [`v:spec:guidance`](../00_vertices/spec-for-guidance.md) |
| Guidance | [`v:guidance:guidance`](../00_vertices/guidance-for-guidance.md) |
| Example | [`v:guidance:purpose`](../00_vertices/guidance-for-purpose.md) |
| Coupling Edge | [`e:coupling:guidance`](../01_edges/coupling-guidance.md) |
| Verification Edge | `e:verification:guidance-purpose:spec` |
| Validation Edge | `e:validation:guidance-purpose:guidance` |
| Assurance Status | COMPLETE |
| Maintainer | mzargham |
| Last Updated | 2025-12-29 |

## Examples in the Wild

Beyond the canonical example, other guidance documents in this knowledge complex include:

- [`v:guidance:purpose`](../00_vertices/guidance-for-purpose.md): Guidance for purpose documents
- [`v:guidance:persona`](../00_vertices/guidance-for-persona.md): Guidance for persona documents
- [`v:guidance:protocol`](../00_vertices/guidance-for-protocol.md): Guidance for protocol documents
- [`v:guidance:spec`](../00_vertices/guidance-for-spec.md): Guidance for specification documents
- [`v:guidance:system_prompt`](../00_vertices/guidance-for-system-prompt.md): Guidance for system prompt documents

---

**Note**: This doc-kit is foundational to the knowledge complex type system. The guidance-for-guidance is self-referential and establishes the pattern for all other guidance documents.
