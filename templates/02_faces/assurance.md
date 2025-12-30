---
type: face/assurance
extends: face
id: f:assurance:<name>
name: Assurance Face - <Descriptive Name>
description: Complete assurance pattern for <target document>
boundary:
  - <coupling-edge-id>
  - <verification-edge-id>
  - <validation-edge-id>
vertices:
  - <target-vertex-id>
  - <spec-vertex-id>
  - <guidance-vertex-id>
target: <target-vertex-id>
spec: <spec-vertex-id>
guidance: <guidance-vertex-id>
coupling_edge: <coupling-edge-id>
verification_edge: <verification-edge-id>
validation_edge: <validation-edge-id>
assurer: "<person-name or system-name>"
assurance_method: manual | llm-assisted | automated
llm_model: "<model-name>"  # REQUIRED for llm-assisted
human_approver: "<username>"  # REQUIRED for llm-assisted/automated
tags:
  - face
  - assurance
version: 1.0.0
created: YYYY-MM-DDTHH:MM:SSZ
modified: YYYY-MM-DDTHH:MM:SSZ
---

# Assurance Face - <Descriptive Name>

This assurance face represents the complete quality assurance pattern for [target document](<path>), consisting of a specification, guidance, and the three edges that form the assurance triangle: coupling, verification, and validation.

## Face Structure

### Vertices

1. **Target Document**: [<name>](<path>) - The document being assured
2. **Specification**: [<name>](<path>) - Structural requirements for the target
3. **Guidance**: [<name>](<path>) - Quality criteria for the target

### Edges (Boundary)

1. **Coupling Edge**: [<name>](<path>)
   - Connects specification and guidance
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: [<name>](<path>)
   - Target verifies against specification
   - Deterministic structural checking
   - Type: `edge/verification`

3. **Validation Edge**: [<name>](<path>)
   - Target validates against guidance
   - Qualitative quality assessment
   - Type: `edge/validation`

## Assurance Triangle

```
         Guidance (quality criteria)
              /\
             /  \
  Validation/    \Coupling
           /      \
          /        \
         /          \
    Target -------- Spec
         Verification
```

The three edges form a closed boundary creating the assurance face.

## Assurance Assessment

**Assurer:** <person or system name>
**Method:** <manual/llm-assisted/automated>
**Human Approver:** <username> (for llm-assisted/automated)
**Date:** YYYY-MM-DD

### Triangle Coherence Review

This section reviews whether the assurance triangle works together as a coherent whole.

#### Coupling Coherence

**Assessment**: [Excellent/Good/Needs Improvement]
**Rationale**: Does the coupling between spec and guidance make sense? Do they actually address the same document type? Are they properly aligned?
**Evidence**: [Specific observations about the coupling edge, how spec and guidance relate]

#### Verification Completeness

**Assessment**: [Pass/Fail]
**Rationale**: Did verification pass? Are all structural requirements met? Is the verification edge current and accurate?
**Evidence**: [Verification results - N/N checks passed, date, any notes]

#### Validation Quality

**Assessment**: [Pass/Fail/Needs Work]
**Rationale**: Did validation pass? Was the quality assessment thorough? Is the validation edge current and reflects actual quality?
**Evidence**: [Validation results - overall recommendation, method used, quality level achieved]

#### Triangle Integration

**Assessment**: [Coherent/Has Issues]
**Rationale**: Do the three edges work together? Does the target actually comply with spec AND meet guidance quality? Are there contradictions or gaps?
**Evidence**: [Observations about how the pieces fit together, any tensions or alignments]

## Overall Assurance

**Status**: [ASSURED/NEEDS WORK/INCOMPLETE]

**Summary**: [2-3 sentence summary of the overall assurance status, highlighting key strengths or concerns]

### Assurance Criteria

A fully assured document must demonstrate:

1. ✓/✗ **Structural Compliance**: Pass verification against specification
2. ✓/✗ **Quality Achievement**: Pass validation against guidance
3. ✓/✗ **Coupling Integrity**: Spec and guidance properly coupled for the document type
4. ✓/✗ **Currency**: All edges current and reflect actual document state
5. ✓/✗ **Coherence**: Triangle works together without contradictions

**Conclusion**: [Detailed conclusion about trustworthiness of this document based on the complete assurance pattern]

## Accountability Statement

[For manual: "This assurance assessment was performed manually by <assurer>, who takes full responsibility for reviewing the complete assurance triangle and attesting to its trustworthiness."]

[For llm-assisted: "This assurance assessment was generated with assistance from <llm_model>. The assessment was reviewed and approved by <human_approver>, who takes full responsibility for its accuracy and the trustworthiness attestation."]

[For automated: "This assurance assessment was performed by automated system <assurer>. The system's behavior and output are the responsibility of <human_approver>, who approves this assurance."]

**Signed:** <human name>
**Date:** YYYY-MM-DD

## Assurance Metadata

| Property | Value |
|----------|-------|
| Target Document | [<name>](<id>) |
| Specification | [<name>](<id>) |
| Guidance | [<name>](<id>) |
| Coupling Edge | [<name>](<id>) |
| Verification Edge | [<name>](<id>) |
| Validation Edge | [<name>](<id>) |
| Assurance Method | <manual/llm-assisted/automated> |
| Assurer | <name> |
| Human Approver | <username> (if applicable) |
| Date Assured | YYYY-MM-DD |
| Assurance Status | <ASSURED/NEEDS WORK/INCOMPLETE> |

## Template Usage

### When to Create an Assurance Face

Create an assurance face when you have a complete assurance triangle:
1. A target document that needs quality assurance
2. A specification defining its required structure
3. A guidance document defining its quality criteria
4. A coupling edge linking the spec and guidance
5. A verification edge showing structural compliance (passed)
6. A validation edge showing quality assessment (passed)

### Accountability in Assurance

The assurance face is where a human (or system with human approval) says: **"I have reviewed this complete assurance triangle and attest that you can trust this document."**

This is a significant claim requiring:
- **Review of all three edges**: Not just checking they exist, but evaluating their quality
- **Triangle coherence assessment**: Ensuring the pieces work together
- **Currency verification**: Confirming edges reflect current document state
- **Explicit accountability**: Someone's name attached to the trust claim

### Three Assurance Methods

**Manual** (`assurance_method: manual`):
- Human reviews all edges and vertices
- Human makes coherence assessment
- `assurer` is the person who performed review
- No `human_approver` needed (assurer is accountable)
- Use for: Critical foundations, novel patterns, high-stakes documents

**LLM-Assisted** (`assurance_method: llm-assisted`):
- LLM generates assurance assessment
- `assurer` is the LLM (with version)
- `llm_model` field REQUIRED (same as assurer, for consistency)
- `human_approver` REQUIRED - person who reviews and accepts responsibility
- Use for: Routine assurance, well-established patterns, when speed matters

**Automated** (`assurance_method: automated`):
- System automatically generates assurance assessment
- `assurer` is the system name/version
- `human_approver` REQUIRED - person responsible for system behavior
- Use for: Repeated patterns, automated workflows, continuous integration

### How to Fill This Template

1. **Replace all `<placeholders>`** with actual values

2. **Update frontmatter**:
   - Set `id`, `name`, `description`
   - List all 3 boundary edge IDs
   - List all 3 vertex IDs (may have duplicates in self-referential cases)
   - Set individual edge and vertex ID fields
   - Set `assurer`, `assurance_method`
   - Add `llm_model` if llm-assisted
   - Add `human_approver` if llm-assisted or automated
   - Update timestamps

3. **Complete Assurance Assessment**:
   - Review coupling coherence
   - Check verification completeness (reference actual verification results)
   - Evaluate validation quality (reference actual validation results)
   - Assess triangle integration (how pieces fit together)
   - Make overall assurance determination

4. **Write Accountability Statement**:
   - Choose appropriate template based on method
   - Fill in actual names
   - Sign and date

5. **Verify all links** resolve to actual files

## Related Templates

- [Coupling Edge Template](../01_edges/coupling.md)
- [Verification Edge Template](../01_edges/verification.md)
- [Validation Edge Template](../01_edges/validation.md)
- [Spec Template](../00_vertices/spec.md)
- [Guidance Template](../00_vertices/guidance.md)

---

**Note**: This template defines the structure and accountability framework for assurance faces. An assurance face is a trust attestation - someone putting their name on the claim that a document is trustworthy based on complete review of its assurance triangle.
