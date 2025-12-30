---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:spec
name: Doc-Kit - Specification Documents
description: Complete documentation kit for specification documents including spec-for-spec, guidance, and canonical example
vertices:
  - v:spec:spec
  - v:guidance:spec
  - v:spec:purpose
edges:
  - e:coupling:spec
  - e:verification:purpose:spec
  - e:validation:purpose:guidance-spec
face_type: doc_kit
orientation: oriented
target: v:spec:spec
spec: v:spec:spec
guidance: v:guidance:spec
example: v:spec:purpose
coupling_edge: e:coupling:spec
verification_edge: e:verification:spec-purpose:spec
validation_edge: e:validation:spec-purpose:guidance
doc_type: spec
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

# Doc-Kit - Specification Documents

This doc-kit provides a complete documentation package for **specification** documents, including the spec-for-spec (structural requirements), guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [Specification for Specifications](../00_vertices/spec-for-spec.md) (`v:spec:spec`)
   - Defines what structural elements MUST be present in any spec
   - Requires: Purpose Statement, Structural Requirements, Format Constraints, Schema Definition
   - Self-referential: verifies itself
   - Used for deterministic verification

2. **Guidance**: [Guidance for Specifications](../00_vertices/guidance-for-spec.md) (`v:guidance:spec`)
   - Defines quality criteria: Clarity, Completeness, Testability, Consistency, Maintainability, Obsidian Compatibility, Reference/Referent Clarity
   - Provides section-by-section authoring advice
   - Used for qualitative validation

3. **Example**: [Specification for Purpose Documents](../00_vertices/spec-for-purpose.md) (`v:spec:purpose`)
   - Demonstrates a well-formed specification instance
   - Shows how to define structural requirements for a document type
   - Reference for creating new specification documents

### Edges (Boundary)

1. **Coupling Edge**: [Coupling - Spec](../01_edges/coupling-spec.md) (`e:coupling:spec`)
   - Connects [[spec-for-spec]] ↔ [[guidance-for-spec]]
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: Verification - Spec Purpose (`e:verification:spec-purpose:spec`)
   - Example verifies against spec-for-spec
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: Validation - Spec Purpose (`e:validation:spec-purpose:guidance`)
   - Example validates against guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What Specification Documents Are

Specification documents define **structural requirements** and **schema constraints** - the "what" of documentation. Specs establish what fields, sections, and properties MUST be present in valid documents. They use prescriptive language (MUST, SHALL, REQUIRED) and are focused on deterministic, objectively verifiable requirements.

Specifications are the foundation of the type system. Every document type (persona, purpose, protocol, guidance, chart, etc.) has a corresponding spec that defines its required structure. Specs enable automated verification - if a document passes verification against its spec, it has all required structural elements.

### Key Characteristics

- **Structural Focus**: Defines what MUST be present, not quality
- **Prescriptive Language**: Uses MUST, SHALL, REQUIRED
- **Deterministic**: Requirements are objectively checkable
- **Self-Referential**: The spec-for-spec verifies itself
- **Paired with Guidance**: Every spec should have corresponding guidance

### Type Hierarchy

**Extends**: `doc` (standard document)
**Extended By**: None (spec is a leaf type, but defines other specs)
**Composes**: None (spec is atomic)
**Coupled With**: `guidance` (via coupling edge)

## When to Use This Document Type

### Primary Use Cases

Use specification documents when:

1. **Defining New Document Types**: Creating structural requirements for a new vertex, edge, or face type
2. **Formalizing Structure**: Need deterministic verification of document structure
3. **Enabling Automation**: Want to automate compliance checking
4. **Establishing Type System**: Building the foundation for typed documentation
5. **Creating Coupling Pairs**: Specs always pair with guidance documents

### When NOT to Use

Avoid specification documents when:

- **Defining Quality**: Quality criteria belong in guidance, not specs
- **Subjective Requirements**: If requirements can't be objectively checked, they're not spec material
- **Without Guidance Pair**: Every spec needs corresponding guidance
- **Mixing Concerns**: Don't combine structural requirements with best practices

## How to Create Specification Documents

### Prerequisites

Before creating a specification document:

- [ ] **Use case is clear**: Know what document type you're specifying
- [ ] **Read spec-for-spec**: Familiar with [[spec-for-spec]] requirements
- [ ] **Review guidance-for-spec**: Studied [[guidance-for-spec]] quality criteria
- [ ] **Plan guidance pair**: Know you'll create corresponding guidance

### Creation Workflow

1. **Define Purpose** (5 minutes)
   - Why does this spec exist?
   - What problem does it solve?
   - Keep to 1-3 sentences
   - **Checkpoint**: Can you state why this spec is needed?

2. **Identify Required Elements** (15-30 minutes)
   - What MUST be present for compliance?
   - What is OPTIONAL but supported?
   - Use tables for field definitions
   - **Checkpoint**: Can you list all required elements without consulting other docs?

3. **Specify Formats** (15-30 minutes)
   - Data types for each element (string, integer, boolean, datetime, enum)
   - Patterns, enums, constraints
   - Use precise type names and regex patterns
   - **Checkpoint**: Are all format constraints deterministic?

4. **Create Schema** (20-40 minutes)
   - Formalize structure in chosen format (YAML, tables, JSON Schema)
   - Ensure completeness
   - Make schema copy-paste ready
   - **Checkpoint**: Could a developer implement validation from your schema?

5. **Write Examples** (15-30 minutes)
   - Minimal valid example
   - Full-featured example
   - Ensure examples actually satisfy the spec
   - **Checkpoint**: Do your examples pass verification?

6. **Define Validation Rules** (10-20 minutes)
   - Extract checkable rules
   - Number rules for reference
   - Use imperative language (MUST, SHALL)
   - **Checkpoint**: Are all rules objectively verifiable?

**Total Estimated Time**: 2-3 hours

### Verification and Validation

**To verify your specification document**:
```bash
python scripts/verify_template_based.py your-spec.md --templates templates
```

This checks:
- All required frontmatter fields present
- All required sections present (Purpose, Structural Requirements, Format Constraints, Schema Definition)
- Type field is exactly `vertex/spec`
- ID matches pattern `v:spec:<name>`

**To validate quality**:
- Review against [[guidance-for-spec]] quality criteria
- Check clarity (unambiguous language, defined terms)
- Verify completeness (all elements defined, edge cases addressed)
- Assess testability (objectively verifiable requirements)
- Confirm consistency (no contradictions, consistent terminology)
- Evaluate maintainability (versioned, modular)
- Reference example: [[spec-for-purpose]]

## Related Document Types

### Works Together With

- **Guidance**: Every spec should have corresponding guidance (coupled via coupling edge)
- **All Document Types**: Specs define the structural requirements for vertices, edges, and faces
- **Templates**: Templates implement spec requirements for automated verification

### Part of Larger Patterns

**Spec-Guidance Coupling**:
- Every document type has a spec (structure) and guidance (quality)
- They're linked via a coupling edge
- Verification checks spec; validation checks guidance
- Assurance combines both via assurance triangle

**Type System Foundation**:
- Specs are the foundation of the knowledge complex type system
- All typed documents reference their spec for verification
- The spec-for-spec is self-referential (verifies itself)

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Too Vague** | Requirements like "should be reasonable" | Use specific constraints: "MUST be 1-100 characters" |
| **Mixing Concerns** | Spec includes quality criteria | Move quality criteria to guidance; keep spec structural only |
| **Incomplete Schema** | Missing fields referenced elsewhere | Ensure every referenced field is defined in schema |
| **Untestable Requirements** | "Should follow best practices" | Make requirements objective and deterministic |
| **No Examples** | Only abstract requirements | Add at least one complete, valid example |
| **No Guidance Pair** | Spec without corresponding guidance | Always create spec-guidance coupling |
| **Subjective Language** | "Should be well-written" | Focus on structure, not quality (that's guidance's job) |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: Excellent
**Rationale**: Spec-for-spec and guidance-for-spec both address specification documents consistently, with clear separation of structural requirements from quality criteria
**Evidence**: [[coupling-spec]] documents alignment between structural requirements and quality assessment

### Example Verification

**Assessment**: Pass
**Rationale**: Example (spec-for-purpose) passes all structural checks against spec-for-spec
**Evidence**: Verification results - all checks passed via `verify_template_based.py`
**Reference**: Verification of spec-for-purpose against spec-for-spec

### Example Validation

**Assessment**: Excellent
**Rationale**: Example demonstrates quality criteria effectively - clear purpose, complete requirements, testable constraints, consistent formatting
**Evidence**: Validation assessment against guidance criteria
**Reference**: Validation of spec-for-purpose against guidance-for-spec

### Kit Completeness

**Assessment**: Complete
**Rationale**: This kit provides everything needed to create good specification documents
**Evidence**:
- ✓ Spec is complete, clear, and self-referential
- ✓ Guidance is actionable and comprehensive
- ✓ Example demonstrates best practices
- ✓ Usage context is sufficient
- ✓ Pitfalls and solutions documented

## Overall Doc-Kit Assessment

**Status**: COMPLETE

**Summary**: The specification doc-kit provides a complete, high-quality documentation package for specification documents. The spec-for-spec defines structural requirements and is self-referential, the guidance provides quality criteria for clear and testable specs, and the example demonstrates effective specification creation.

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✓ **Assurance Triangle**: Complete and coherent (spec, guidance, example, 3 edges)
2. ✓ **Usage Context**: Clear explanation of when/why to use this type
3. ✓ **Creation Workflow**: 6-step workflow with checkpoints documented
4. ✓ **Quality Example**: Example passes verification AND validation
5. ✓ **Relationship Documentation**: Clear how spec relates to guidance, templates, type system
6. ✓ **Pitfall Guidance**: 7 common mistakes and solutions documented

**Conclusion**: This doc-kit successfully helps users create good specification documents by providing complete structural requirements, quality guidance, and a practical example.

## Accountability Statement

This doc-kit assessment was generated with assistance from claude-opus-4-5, reviewed and approved by mzargham.

**Maintainer:** mzargham
**Assurer:** mzargham
**Date:** 2025-12-29

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | spec |
| Specification | [`v:spec:spec`](../00_vertices/spec-for-spec.md) |
| Guidance | [`v:guidance:spec`](../00_vertices/guidance-for-spec.md) |
| Example | [`v:spec:purpose`](../00_vertices/spec-for-purpose.md) |
| Coupling Edge | [`e:coupling:spec`](../01_edges/coupling-spec.md) |
| Verification Edge | `e:verification:spec-purpose:spec` |
| Validation Edge | `e:validation:spec-purpose:guidance` |
| Assurance Status | COMPLETE |
| Maintainer | mzargham |
| Last Updated | 2025-12-29 |

## Examples in the Wild

Beyond the canonical example, other specification documents in this knowledge complex include:

- [`v:spec:purpose`](../00_vertices/spec-for-purpose.md): Specification for purpose documents
- [`v:spec:persona`](../00_vertices/spec-for-persona.md): Specification for persona documents
- [`v:spec:protocol`](../00_vertices/spec-for-protocol.md): Specification for protocol documents
- [`v:spec:guidance`](../00_vertices/spec-for-guidance.md): Specification for guidance documents
- [`v:spec:system_prompt`](../00_vertices/spec-for-system-prompt.md): Specification for system prompt documents
- [`v:spec:chart`](../00_vertices/spec-for-charts.md): Specification for chart documents

---

**Note**: This doc-kit is foundational to the knowledge complex type system. The spec-for-spec is self-referential and establishes the pattern for all other specifications.
