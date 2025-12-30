---
type: face/doc_kit
extends: face/assurance
id: f:doc_kit:persona
name: Doc-Kit - Persona Documents
description: Complete documentation kit for persona documents including spec, guidance, and example from PPP framework
vertices:
  - v:spec:persona
  - v:guidance:persona
  - v:persona:claude-assistant
edges:
  - e:coupling:persona
  - e:verification:persona-claude:spec
  - e:validation:persona-claude:guidance
face_type: doc_kit
orientation: oriented
target: v:spec:persona
spec: v:spec:persona
guidance: v:guidance:persona
example: v:persona:claude-assistant
coupling_edge: e:coupling:persona
verification_edge: e:verification:persona-claude:spec
validation_edge: e:validation:persona-claude:guidance
doc_type: persona
assurer: mzargham
assurance_method: manual
maintainer: mzargham
tags:
  - face
  - assurance
  - doc_kit
version: 1.0.0
created: 2025-12-27T23:30:00Z
modified: 2025-12-27T23:30:00Z
---

# Doc-Kit - Persona Documents

This doc-kit provides a complete documentation package for **persona** documents, including the specification (structural requirements), guidance (quality criteria and best practices), and a canonical example.

**Doc-kits extend assurance faces** by adding an example document and usage context to help users understand when and how to create instances of this document type.

## Kit Structure

### Vertices

1. **Specification**: [Specification for Persona Documents](../00_vertices/spec-for-persona.md) (`v:spec:persona`)
   - Defines what structural elements MUST be present
   - Requires: Role and Identity, Domain Expertise (2-4 items), Approach and Methodology, Communication Tone, Boundaries and Limitations (≥3 items)
   - Used for deterministic verification

2. **Guidance**: [Guidance for Persona Documents](../00_vertices/guidance-for-persona.md) (`v:guidance:persona`)
   - Defines quality criteria: Role Specificity, Expertise Appropriateness, Approach Clarity, Tone Appropriateness, Boundary Honesty, Internal Coherence
   - Provides section-by-section authoring advice
   - Used for qualitative validation

3. **Example**: [Persona Example](../workshop/input-docs/vv_research/persona/persona_example.yml) (`v:persona:example`)
   - Demonstrates a well-formed persona instance
   - Shows document analyst persona for template extraction
   - Reference for creating new personas

### Edges (Boundary)

1. **Coupling Edge**: `e:coupling:persona` (TO BE CREATED)
   - Connects [[spec-for-persona]] ↔ [[guidance-for-persona]]
   - Ensures they address the same document type
   - Type: `edge/coupling`

2. **Verification Edge**: `e:verification:persona-example:persona` (TO BE CREATED)
   - Example verifies against spec
   - Demonstrates structural compliance
   - Type: `edge/verification`

3. **Validation Edge**: `e:validation:persona-example:persona` (TO BE CREATED)
   - Example validates against guidance
   - Demonstrates quality achievement
   - Type: `edge/validation`

## Document Type Overview

### What Persona Documents Are

Persona documents define **who the AI is** - its professional identity, domain expertise, thinking approach, communication style, and explicit boundaries. In the PPP (Persona-Purpose-Protocol) framework, persona is one of three core components that together define a complete AI model configuration.

Personas establish clear user expectations, build trust through specificity, and guide consistent AI behavior. A well-crafted persona enables users to quickly understand what kind of "expert" they're working with and what limitations to expect.

### Key Characteristics

- **Specific Role Identity**: Not "helpful assistant" but credible professional roles like "expert document analyst" or "experienced teacher"
- **Focused Expertise**: Lists 2-4 specific knowledge domains relevant to purpose
- **Behavioral Approach**: Describes HOW the AI thinks and works (systematic, collaborative, evidence-based)
- **Appropriate Tone**: Communication style matching role and use case
- **Honest Boundaries**: Explicit statements of what the AI does NOT do or claim

### Type Hierarchy

**Extends**: `doc` (standard document)
**Extended By**: None (persona is a leaf type in the PPP framework)
**Composes**: None (persona is atomic, not compositional)
**Used In**: `system_prompt` (as a typed subsection)

## When to Use This Document Type

### Primary Use Cases

Use persona documents when:

1. **Defining AI Models in PPP Framework**: Creating the "who" component of a Persona-Purpose-Protocol system prompt
2. **Establishing AI Identity**: Need to give an AI model a specific, credible professional identity
3. **Managing User Expectations**: Want to clearly communicate what the AI can and cannot do
4. **Ensuring Consistent Behavior**: Defining expertise and approach guides consistent responses
5. **Building Trust**: Honest boundaries and specific expertise build user confidence

### When NOT to Use

Avoid persona documents when:

- **Just Listing Capabilities**: If you're describing what an AI CAN do, you want Purpose (not Persona)
- **Defining Workflow**: If you're describing HOW work gets done step-by-step, you want Protocol (not Persona)
- **Standalone Identity**: Personas should be designed AFTER purpose (to match needed expertise)
- **Generic AI**: If "helpful assistant" is genuinely appropriate, persona framework may be overkill

## How to Create Persona Documents

### Prerequisites

Before creating a persona document:

- [ ] **Purpose is defined**: Know what problem you're solving (persona expertise must enable purpose)
- [ ] **Use case is clear**: Understand the context where this AI will be used
- [ ] **Tone requirements known**: Understand what communication style is appropriate
- [ ] **Read the spec**: Familiar with [[spec-for-persona]] requirements
- [ ] **Review guidance**: Studied [[guidance-for-persona]] quality criteria

### Creation Workflow

1. **Review Purpose First** (10 minutes)
   - Read the purpose document thoroughly
   - Identify what expertise is needed to achieve objectives
   - Consider what professional role would fit
   - **Checkpoint**: Can you identify what kind of expert is needed?

2. **Define Core Identity** (10 minutes)
   - Write specific role statement (not "helpful assistant")
   - Define professional identity clearly
   - Ensure role matches purpose domain
   - **Checkpoint**: Is the role specific, credible, and appropriate for the purpose?

3. **Specify Expertise** (15 minutes)
   - List 2-4 areas of expertise (not too narrow, not impossibly broad)
   - Use domain-appropriate terminology
   - Ensure expertise directly enables purpose objectives
   - Check that breadth is realistic
   - **Checkpoint**: Does this expertise enable the purpose objectives?

4. **Describe Approach and Tone** (15 minutes)
   - Describe HOW the AI thinks and works (behavioral terms)
   - Define communication tone clearly
   - Ensure both match purpose requirements
   - Ensure tone is appropriate for use case
   - **Checkpoint**: Do approach and tone support the intended work?

5. **Set Boundaries** (10 minutes)
   - List at least 3 explicit limitations
   - Be honest about constraints
   - Define scope limits to prevent overreach
   - **Checkpoint**: Are boundaries clear, realistic, and sufficient?

**Total Estimated Time**: 60 minutes

### Verification and Validation

**To verify your persona document**:
```bash
python scripts/verify_template_based.py your-persona.md --templates templates
```

This checks:
- All required frontmatter fields present
- All required sections present (Role, Expertise, Approach, Tone, Boundaries)
- Expertise lists 2-4 items
- Boundaries lists ≥3 items

**To validate quality**:
- Review against [[guidance-for-persona]] quality criteria
- Check role specificity (not vague)
- Verify expertise appropriateness for purpose
- Assess approach clarity and behavioral description
- Evaluate tone appropriateness and consistency
- Confirm boundary honesty and completeness
- Verify internal coherence (all elements align)
- Reference example: `v:persona:example`

## Related Document Types

### Works Together With

- **Purpose**: Persona expertise must enable purpose objectives (design persona AFTER purpose)
- **Protocol**: Persona approach should be reflected in protocol workflow
- **System Prompt**: Persona is a typed subsection in compositional system_prompt documents

### Part of Larger Patterns

**PPP Framework** (Persona-Purpose-Protocol):
- **Design order**: Purpose → Persona → Protocol
- **Integration**: Persona expertise enables Purpose objectives, Protocol operationalizes Purpose through Persona
- **Coherence**: Tone in Persona must be consistent across Purpose and Protocol

## Common Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| **Vague Role** | Generic "helpful assistant" identity doesn't establish credibility | Be specific: "expert document analyst", "experienced teacher" - use credible professional titles |
| **Too Much Expertise** | Claiming to know "everything" or listing 10+ areas destroys credibility | Focus on 2-4 specific, relevant areas. Realistic breadth builds trust |
| **Missing Approach** | Not describing HOW the AI thinks makes behavior unpredictable | Add behavioral description: "systematic and evidence-based", "collaborative and iterative" |
| **No Boundaries** | Claiming unlimited capability sets false expectations | Explicitly list what AI doesn't do (3+ items): "doesn't modify files", "requires 2+ examples" |
| **Tone Mismatch** | Casual tone for analytical work, or formal tone for creative tasks | Match tone to use case: analytical → analytical tone, teaching → patient/encouraging tone |
| **Incoherence** | Expertise doesn't match role, or tone conflicts with approach | Ensure all elements align: if role is "analyst", expertise should be analytical, tone analytical, approach systematic |
| **Designed in Isolation** | Creating persona without knowing purpose wastes effort | ALWAYS design persona AFTER purpose - let purpose requirements drive expertise selection |

## Assurance Triangle Review

### Coupling Coherence

**Assessment**: To be determined (coupling edge not yet created)
**Rationale**: Need to verify [[spec-for-persona]] and [[guidance-for-persona]] properly address the same document type
**Evidence**: Both documents exist and use consistent terminology, but formal coupling edge required

### Example Verification

**Assessment**: To be determined (verification edge not yet created)
**Rationale**: Need to verify canonical example passes all structural checks
**Evidence**: Example exists at `workshop/input-docs/vv_research/persona/persona_example.yml` but needs conversion to markdown and verification

### Example Validation

**Assessment**: To be determined (validation edge not yet created)
**Rationale**: Need to assess example quality against guidance criteria
**Evidence**: Example appears complete but needs formal quality assessment

### Kit Completeness

**Assessment**: Has Gaps (in progress)
**Rationale**: Spec and guidance are complete and verified (7/7), but edges and example need work
**Evidence**:
- ✓ Spec is complete and clear (verified 7/7)
- ✓ Guidance is actionable and comprehensive (verified 7/7)
- ✗ Example needs conversion from YAML to markdown format
- ✓ Usage context documented in this doc-kit
- ✓ Pitfalls and solutions documented
- ✗ Coupling edge not yet created
- ✗ Verification edge not yet created
- ✗ Validation edge not yet created

## Overall Doc-Kit Assessment

**Status**: DRAFT (edges and example need completion)

**Summary**: The persona doc-kit has complete, high-quality spec and guidance documents that successfully define what persona documents are and how to create them. However, the assurance triangle is incomplete - edges need to be created and the example needs conversion to markdown format.

### Doc-Kit Criteria

A complete doc-kit must demonstrate:

1. ✗ **Assurance Triangle**: Partial - spec and guidance exist, example exists but needs conversion, edges not created
2. ✓ **Usage Context**: Clear explanation provided in this document
3. ✓ **Creation Workflow**: 5-step workflow with checkpoints documented
4. ✗ **Quality Example**: Example exists but not yet verified/validated
5. ✓ **Relationship Documentation**: Clear how persona relates to purpose, protocol, system_prompt
6. ✓ **Pitfall Guidance**: 7 common mistakes and solutions documented

**Conclusion**: This doc-kit provides excellent usage documentation and workflow guidance, but needs the assurance triangle completed (create edges, convert example, verify and validate) before it can be considered COMPLETE.

## Accountability Statement

This doc-kit was assembled manually by mzargham as part of implementing the PPP framework in the knowledge complex. The spec and guidance documents have been verified against templates (7/7 checks passing). The assurance triangle assessment will be finalized once edges are created and example is verified.

**Maintainer:** mzargham
**Assurer:** mzargham
**Date:** 2025-12-27

## Doc-Kit Metadata

| Property | Value |
|----------|-------|
| Document Type | persona |
| Specification | [`v:spec:persona`](../00_vertices/spec-for-persona.md) |
| Guidance | [`v:guidance:persona`](../00_vertices/guidance-for-persona.md) |
| Example | `v:persona:example` (needs conversion) |
| Coupling Edge | `e:coupling:persona` (to be created) |
| Verification Edge | `e:verification:persona-example:persona` (to be created) |
| Validation Edge | `e:validation:persona-example:persona` (to be created) |
| Assurance Status | DRAFT |
| Maintainer | mzargham |
| Last Updated | 2025-12-27 |

## Examples in the Wild

Beyond the canonical example, other persona examples will be created as the PPP framework is used:

- (To be populated as personas are created for actual AI models)

---

**Note**: This is the first doc-kit created in the knowledge complex. It demonstrates the pattern of extending assurance faces to provide complete documentation packages for document types. Future doc-kits will follow this template.
