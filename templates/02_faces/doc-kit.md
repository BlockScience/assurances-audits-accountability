---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:<type-name>
name: Doc-Kit - <Type Name>
description: Complete documentation kit for <type> documents including spec, guidance, and example
boundary:
  - <coupling-edge-id>
  - <verification-edge-id>
  - <validation-edge-id>
vertices:
  - <spec-vertex-id>
  - <guidance-vertex-id>
  - <example-vertex-id>
target: <spec-vertex-id>
spec: <spec-vertex-id>
guidance: <guidance-vertex-id>
example: <example-vertex-id>
coupling_edge: <coupling-edge-id>
verification_edge: <verification-edge-id>
validation_edge: <validation-edge-id>
doc_type: <type-name>
assurer: "<person-name or system-name>"
assurance_method: manual | llm-assisted | automated
llm_model: "<model-name>"  # REQUIRED for llm-assisted
human_approver: "<username>"  # REQUIRED for llm-assisted/automated
maintainer: "<person-name>"
tags:
  - face
  - assurance
  - doc_kit
version: 1.0.0
created: YYYY-MM-DDTHH:MM:SSZ
modified: YYYY-MM-DDTHH:MM:SSZ
---

# Doc-Kit - <Type Name>

This doc-kit provides a complete documentation package for **<type>** documents, including the specification (structural requirements), guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [<spec-name>](<spec-path>) (`<spec-id>`)
   - Defines what structural elements MUST be present
   - Provides schema and format constraints
   - Used for deterministic verification

2. **Guidance**: [<guidance-name>](<guidance-path>) (`<guidance-id>`)
   - Defines quality criteria and best practices
   - Provides section-by-section authoring advice
   - Used for qualitative validation

3. **Example**: [<example-name>](<example-path>) (`<example-id>`)
   - Demonstrates a well-formed instance
   - Shows how to apply spec and guidance
   - Reference for creating new instances

### Edges (Boundary)

1. **Coupling Edge**: [<coupling-name>](<coupling-path>) (`<coupling-id>`)
   - Connects spec ↔ guidance
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: [<verification-name>](<verification-path>) (`<verification-id>`)
   - Example verifies against spec
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: [<validation-name>](<validation-path>) (`<validation-id>`)
   - Example validates against guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What <Type> Documents Are

[1-2 paragraphs explaining what this document type is for and its role in the knowledge complex]

### Key Characteristics

- **Characteristic 1**: [Description]
- **Characteristic 2**: [Description]
- **Characteristic 3**: [Description]
- **Characteristic 4**: [Description]

### Type Hierarchy

**Extends**: [parent-type]
**Extended By**: [child-types, if any]
**Composes**: [If compositional, list component types]

## When to Use This Document Type

### Primary Use Cases

Use <type> documents when:

1. **Use Case 1**: [Specific scenario]
2. **Use Case 2**: [Specific scenario]
3. **Use Case 3**: [Specific scenario]
4. **Use Case 4**: [Specific scenario]

### When NOT to Use

Avoid <type> documents when:

- **Anti-use 1**: [Scenario where this type is wrong choice]
- **Anti-use 2**: [Scenario where another type is better]
- **Anti-use 3**: [Common misuse pattern]

## How to Create <Type> Documents

### Prerequisites

Before creating a <type> document:

- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]
- [ ] [Prerequisite 3]

### Creation Workflow

1. **[Step 1 Name]** (estimated time)
   - [Action description]
   - [What to accomplish]
   - **Checkpoint**: [How to know this step is complete]

2. **[Step 2 Name]** (estimated time)
   - [Action description]
   - [What to accomplish]
   - **Checkpoint**: [How to know this step is complete]

3. **[Step 3 Name]** (estimated time)
   - [Action description]
   - [What to accomplish]
   - **Checkpoint**: [How to know this step is complete]

**Total Estimated Time**: [X minutes/hours]

### Verification and Validation

**To verify your <type> document**:
```bash
python scripts/verify_template_based.py your-file.md --templates templates
```

**To validate quality**:
- Review against guidance: [`<guidance-id>`](<guidance-path>)
- Reference example: [`<example-id>`](<example-path>)
- Check quality criteria in guidance document

## Related Document Types

### Works Together With

- **[Related Type 1]**: [How they interact]
- **[Related Type 2]**: [How they interact]
- **[Related Type 3]**: [How they interact]

### Part of Larger Patterns

[If this type participates in specific patterns or frameworks, describe them]

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **[Pitfall 1]** | [What goes wrong] | [How to avoid/fix] |
| **[Pitfall 2]** | [What goes wrong] | [How to avoid/fix] |
| **[Pitfall 3]** | [What goes wrong] | [How to avoid/fix] |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: [Excellent/Good/Needs Improvement]
**Rationale**: [Do spec and guidance properly address <type> documents?]
**Evidence**: [Reference to coupling edge, observations about alignment]

### Example Verification

**Assessment**: [Pass/Fail]
**Rationale**: [Does example pass all structural checks?]
**Evidence**: [Verification results - N/N checks passed]
**Reference**: [`<verification-id>`](<verification-path>)

### Example Validation

**Assessment**: [Excellent/Good/Acceptable/Needs Improvement]
**Rationale**: [Does example demonstrate quality criteria?]
**Evidence**: [Validation results - quality assessment]
**Reference**: [`<validation-id>`](<validation-path>)

### Kit Completeness

**Assessment**: [Complete/Has Gaps]
**Rationale**: [Does this kit provide everything needed to create good <type> documents?]
**Evidence**:
- ✓/✗ Spec is complete and clear
- ✓/✗ Guidance is actionable and comprehensive
- ✓/✗ Example demonstrates best practices
- ✓/✗ Usage context is sufficient
- ✓/✗ Pitfalls and solutions documented

## Overall Doc-Kit Assessment

**Status**: [COMPLETE/NEEDS WORK/DRAFT]

**Summary**: [2-3 sentence summary of doc-kit quality and usefulness]

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✓/✗ **Assurance Triangle**: Complete and coherent (spec, guidance, example, 3 edges)
2. ✓/✗ **Usage Context**: Clear explanation of when/why to use this type
3. ✓/✗ **Creation Workflow**: Step-by-step guide for creating instances
4. ✓/✗ **Quality Example**: Example passes verification AND validation
5. ✓/✗ **Relationship Documentation**: Clear how this type relates to others
6. ✓/✗ **Pitfall Guidance**: Common mistakes and solutions documented

**Conclusion**: [Assessment of whether this doc-kit successfully helps users create good <type> documents]

## Accountability Statement

[For manual: "This doc-kit was assembled and reviewed by <maintainer>. The assurance triangle was assessed by <assurer>."]

[For llm-assisted: "This doc-kit assessment was generated with assistance from <llm_model>, reviewed and approved by <human_approver>."]

[For automated: "This doc-kit assessment was generated by <assurer>, with oversight by <human_approver>."]

**Maintainer:** <person maintaining this doc-kit>
**Assurer:** <person/system who verified assurance triangle>
**Date:** YYYY-MM-DD

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | <type-name> |
| Specification | [`<spec-id>`](<spec-path>) |
| Guidance | [`<guidance-id>`](<guidance-path>) |
| Example | [`<example-id>`](<example-path>) |
| Coupling Edge | [`<coupling-id>`](<coupling-path>) |
| Verification Edge | [`<verification-id>`](<verification-path>) |
| Validation Edge | [`<validation-id>`](<validation-path>) |
| Assurance Status | <status> |
| Maintainer | <maintainer-name> |
| Last Updated | YYYY-MM-DD |

## Examples in the Wild

Beyond the canonical example, other good <type> documents include:

- [`<example-2-id>`](<path>): [What makes it noteworthy]
- [`<example-3-id>`](<path>): [What makes it noteworthy]

## Template Usage

### When to Create a Doc-Kit

Create a doc-kit face when you have:
1. A complete assurance triangle (spec, guidance, example + 3 edges)
2. Usage context to document (when/why/how to use this document type)
3. A document type that users will create instances of

**Doc-kits are organizational faces** that help users navigate the knowledge complex by providing complete documentation packages for each document type.

### How to Fill This Template

1. **Replace all `<placeholders>`** with actual values

2. **Update frontmatter**:
   - Set `id`, `name`, `description` for the doc-kit
   - Set `doc_type` to match the document type name
   - List all 3 boundary edge IDs
   - List all 3 vertex IDs (spec, guidance, example)
   - Set individual edge and vertex ID fields
   - Set `maintainer`, `assurer`, `assurance_method`
   - Update timestamps

3. **Document the Type**:
   - Explain what this document type is
   - List key characteristics
   - Specify when to use (and when NOT to use)

4. **Provide Creation Guidance**:
   - List prerequisites
   - Break down creation workflow (3-5 steps)
   - Include checkpoints for each step
   - Document verification/validation process

5. **Document Relationships**:
   - How does this type relate to others?
   - What patterns does it participate in?

6. **Review Assurance Triangle**:
   - Assess coupling, verification, validation
   - Evaluate kit completeness
   - Make overall determination

7. **Add Practical Wisdom**:
   - Common pitfalls and solutions
   - Examples beyond the canonical one
   - Tips from experience

### Difference from Assurance Faces

**Assurance Face**: [target, spec, guidance] - Proves a specific document is assured
**Doc-Kit Face**: [spec, guidance, example] - Documents how to use a document **type**

Doc-kits **extend** assurance by adding:
- Usage context (when/why/how)
- Creation workflow guidance
- Relationship documentation
- Common pitfalls
- Additional examples

## Related Templates

- [Assurance Face Template](assurance.md) - Parent template
- [Coupling Edge Template](../01_edges/coupling.md)
- [Verification Edge Template](../01_edges/verification.md)
- [Validation Edge Template](../01_edges/validation.md)

---

**Note**: Doc-kits are faces that extend the assurance pattern to provide complete documentation packages for document types. They help users understand not just THAT a type exists, but WHEN to use it, WHY to use it, and HOW to create good instances.
