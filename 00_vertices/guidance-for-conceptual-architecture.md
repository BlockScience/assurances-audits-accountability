---
type: vertex/guidance
extends: doc
id: v:guidance:conceptual-architecture
name: Guidance for Conceptual Architecture Documents
description: Quality criteria and best practices for creating effective conceptual architecture documents with stakeholder-criterion matrices
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies: []
criteria:
  - stakeholder-completeness
  - criterion-quality
  - matrix-accuracy
  - conops-clarity
  - testing-strategy
  - traceability
---

# Guidance for Conceptual Architecture Documents

**This guidance helps authors create high-quality conceptual architecture documents that effectively establish stakeholder needs, acceptance criteria, and the relationships between them.**

## Purpose

Conceptual architecture documents serve as the foundation of the extended architecture chain. They establish who cares about the system, what they need, and how success will be measured. This guidance helps authors create conceptual architectures that are complete, traceable, and provide a solid foundation for subsequent architecture layers (Functional, Logical, Physical).

## Document Overview

### What This Guidance Covers

Conceptual architecture documents focus on the ConOps layer of systems engineering:
- **Stakeholder Identification**: Who are the relevant parties from the field survey?
- **Needs Articulation**: What does each stakeholder need from the system?
- **Acceptance Criteria**: How will we know the system meets those needs?
- **Stakeholder-Criterion Matrix**: Which criteria matter to which stakeholders?
- **Testing Strategy**: How will acceptance be evaluated?

### Best Use Cases

1. **New System Development**: Establishing stakeholder needs before functional design
2. **Requirements Refinement**: Transforming field survey insights into testable criteria
3. **Stakeholder Communication**: Creating a shared understanding of success criteria
4. **Acceptance Planning**: Defining how system acceptance will be evaluated
5. **Architecture Chain Initiation**: Starting the prerequisite chain for a summary architecture

### When NOT to Use

- For systems with a single stakeholder (use simpler ConOps documentation)
- When field survey has not been completed (prerequisite missing)
- For purely technical architectures without stakeholder diversity
- When acceptance criteria are already well-established elsewhere

## Quality Criteria

### 1. Stakeholder Completeness

**Excellent:** All relevant stakeholders from the field survey are included. Stakeholder selection is justified. Each stakeholder has distinct, non-overlapping needs. No important stakeholder perspective is missing.

**Good:** Most relevant stakeholders are included. Selection is reasonable. Some overlap between stakeholder needs may exist but is acknowledged.

**Needs Improvement:** Key stakeholders are missing. Stakeholder selection seems arbitrary. Needs are generic or could apply to any stakeholder. Important perspectives are absent.

**Tips:**
- Review the field survey actor list systematically
- Ask: "Who would be upset if this system failed?" - they should be included
- Distinguish between primary stakeholders (direct users) and secondary (affected parties)
- Justify exclusions explicitly if not all field survey actors are included

### 2. Criterion Quality

**Excellent:** All acceptance criteria are SMART (Specific, Measurable, Achievable, Relevant, Time-bound). Each criterion has clear success/failure conditions. Criteria cover the full range of stakeholder needs. No vague or untestable criteria.

**Good:** Most criteria are specific and measurable. Success conditions are defined. Coverage of stakeholder needs is adequate.

**Needs Improvement:** Criteria are vague ("system should be fast"). Success conditions are undefined. Criteria don't clearly trace to stakeholder needs. Testing approach unclear.

**Tips:**
- Write criteria as if you had to test them tomorrow
- Include concrete numbers, thresholds, or observable outcomes
- Ask: "How would I prove this criterion is met?" - if you can't answer, refine it
- Avoid subjective language ("user-friendly", "efficient") without measurable proxies

### 3. Matrix Accuracy

**Excellent:** Stakeholder-criterion relationships are meaningful and justified. Every relationship has clear rationale. The matrix reveals non-obvious dependencies. Relationship types (Primary Beneficiary, Accountable, etc.) are used appropriately.

**Good:** Relationships are reasonable and mostly justified. Most stakeholders have appropriate criterion coverage. Relationship types are applied consistently.

**Needs Improvement:** Relationships appear forced or arbitrary. Every stakeholder is marked for every criterion (no discrimination). Rationale is missing or generic. Relationship types are misapplied.

**Tips:**
- Not every stakeholder cares about every criterion - sparsity is expected
- Ask for each relationship: "Why does [Stakeholder] care about [Criterion]?"
- Use relationship types to distinguish intensity of concern
- The matrix should reveal something non-obvious about stakeholder priorities

### 4. ConOps Clarity

**Excellent:** Operational context is vivid and specific. A reader can visualize how the system operates day-to-day. Stakeholder interactions are clearly described. Operational scenarios cover normal operation, edge cases, and failure modes.

**Good:** Operational context is clear. Major interactions are described. Normal operation is well-defined.

**Needs Improvement:** Operational context is abstract or generic. Stakeholder interactions are unclear. Scenarios focus only on happy path.

**Tips:**
- Write as if explaining to someone who will operate the system
- Include temporal aspects: when does the system operate? What's the daily rhythm?
- Consider failure scenarios: what happens when things go wrong?
- Use concrete examples rather than abstract descriptions

### 5. Testing Strategy

**Excellent:** Every criterion has a clear test approach. Test methods are specific and executable. Success indicators are unambiguous. Testing strategy considers resource constraints and feasibility.

**Good:** Most criteria have defined test approaches. Methods are reasonable. Success indicators are present.

**Needs Improvement:** Test approaches are vague or missing. Methods are infeasible. Success indicators are undefined or subjective.

**Tips:**
- Match test type to criterion type (usability testing for UX criteria, performance testing for latency criteria)
- Consider who will execute the tests
- Be realistic about testing resources and constraints
- Include both automated and manual test approaches as appropriate

### 6. Traceability

**Excellent:** Clear bidirectional traceability: field survey actors -> stakeholders -> needs -> criteria -> tests. Traceability to Field Survey section explicitly maps relationships. No orphan elements.

**Good:** Forward traceability is clear. Most elements can be traced. Field survey connection is evident.

**Needs Improvement:** Traceability is weak or absent. Elements don't connect clearly. Field survey reference is nominal only.

**Tips:**
- Use consistent IDs (A1, AC1) to enable cross-referencing
- Explicitly map field survey actors to stakeholders used
- Ensure every criterion traces to at least one stakeholder need
- The optional Traceability to Field Survey section is highly recommended

## Section-by-Section Guidance

### Purpose

**Goal:** Orient readers to what this document establishes.

**Tips:**
- State what stakeholder needs and criteria this document defines
- Mention the system being architected
- Keep to 1-3 sentences - this is orientation, not the full story

**Anti-patterns:**
- Diving into technical details before establishing context

**Preferred:**
- Clear, concise statement of document scope and value

### Overview

**Goal:** Provide context and connect to the architecture chain.

**Tips:**
- Reference the field survey explicitly
- Explain where this document fits in the architecture chain
- Mention subsequent architecture documents if planned

**Anti-patterns:**
- Generic descriptions that could apply to any system

**Preferred:**
- Specific context that grounds the reader in this particular system

### Field Survey Reference

**Goal:** Establish prerequisite connection and summarize relevant stakeholders.

**Tips:**
- Use Obsidian link syntax for field survey reference
- Include only stakeholders relevant to this architecture (may be subset of field survey actors)
- Justify stakeholder selection if not using all field survey actors
- The "Role in This Architecture" column should be specific to this system

**Anti-patterns:**
- Copying entire field survey actor table without filtering
- Missing explanation of stakeholder selection criteria

**Preferred:**
- Curated stakeholder list with clear connection to field survey

### Problem Statement (ConOps)

**Goal:** Articulate operational context and stakeholder needs.

**Tips:**
- Write Operational Context as if describing a day in the life of the system
- Make Stakeholder Needs specific to each stakeholder's perspective
- Avoid duplicating the same need across multiple stakeholders
- Include 2-4 needs per stakeholder (not too few, not overwhelming)

**Anti-patterns:**
- Generic needs ("System should work correctly")
- Stakeholder sections that are interchangeable

**Preferred:**
- Needs that reflect each stakeholder's unique perspective and priorities

### Acceptance Criteria

**Goal:** Define measurable success conditions.

**Tips:**
- Use the table for quick reference, Criterion Definitions for depth
- Include measurement approach and target in the table
- Provide rationale and context in Criterion Definitions
- Number criteria sequentially (AC1, AC2, ...) for easy reference

**Anti-patterns:**
- Vague criteria ("System should be usable")
- Missing measurement approaches
- Criteria that can't be tested

**Preferred:**
- Concrete, measurable criteria with clear success thresholds

### Stakeholder-Criterion Matrix

**Goal:** Map relationships between stakeholders and criteria.

**Tips:**
- Matrix View is for quick visual scanning - keep it simple (X marks)
- Relationship Details provides the "why" for each relationship
- Not every cell should be marked - sparsity is normal and expected
- Key Dependencies should highlight the most critical relationships

**Anti-patterns:**
- Fully connected matrix (every stakeholder cares about everything)
- Missing rationale for relationships
- Generic Key Dependencies

**Preferred:**
- Thoughtfully sparse matrix with justified relationships

### Acceptance Testing Strategy

**Goal:** Define how acceptance will be evaluated.

**Tips:**
- Match test methods to criterion types
- Consider feasibility and resource constraints
- Include both the "how" (method) and "what success looks like" (indicator)
- Think about who will execute each test

**Anti-patterns:**
- Vague test methods ("will be tested")
- Infeasible testing approaches
- Missing success indicators

**Preferred:**
- Specific, executable test approaches with clear success indicators

## Workflow Guidance

### Recommended Authoring Sequence

1. **Start with Field Survey Review** (15 min)
   - Read the referenced field survey thoroughly
   - Identify which actors are relevant as stakeholders
   - Note key findings and gaps that this architecture should address

2. **Draft Stakeholder Needs** (30 min)
   - For each stakeholder, ask: "What do they need from this system?"
   - Write 2-4 specific needs per stakeholder
   - Ensure needs are distinct across stakeholders

3. **Define Acceptance Criteria** (30 min)
   - Transform needs into measurable criteria
   - Apply SMART principles
   - Number criteria sequentially

4. **Build the Matrix** (20 min)
   - Map each criterion to relevant stakeholders
   - Add relationship types and rationale
   - Identify key dependencies

5. **Define Testing Strategy** (20 min)
   - For each criterion, define how it will be tested
   - Consider feasibility and resources
   - Specify success indicators

6. **Write Context Sections** (15 min)
   - Purpose, Overview, Operational Context
   - These frame the detailed content

### Quality Checkpoints

- **After Stakeholder Selection:** Are all relevant perspectives represented?
- **After Needs:** Are needs specific and stakeholder-differentiated?
- **After Criteria:** Can each criterion be tested? Is success measurable?
- **After Matrix:** Does every stakeholder have at least one relationship?
- **After Testing:** Is every criterion covered by a test approach?
- **Final:** Does the document trace cleanly from field survey to tests?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Generic Needs | "System should work correctly" | Rewrite from stakeholder perspective with specific outcomes |
| Vague Criteria | "System should be fast" | Add concrete measurement: "Response time < 200ms for 95th percentile" |
| Fully Connected Matrix | Every stakeholder marked for every criterion | Ask "Why does this stakeholder specifically care?" - remove unjustified relationships |
| Missing Rationale | Relationships without explanation | Add rationale column entries explaining the connection |
| Untestable Criteria | No clear way to verify | Rewrite criterion with observable/measurable outcome |
| Orphan Criteria | Criteria with no stakeholder connection | Either remove or identify missing stakeholder |
| Missing Traceability | No clear link to field survey | Add explicit Field Survey Reference section with actor mapping |
| Scope Creep | Document covers too many stakeholders | Focus on stakeholders directly affected by this specific system |

## Best Practices

1. **Start with the field survey**: The field survey is your source of truth for stakeholders
2. **Differentiate stakeholder needs**: Each stakeholder should have a unique perspective
3. **Make criteria testable**: If you can't test it, it's not a criterion
4. **Justify matrix relationships**: Every X in the matrix needs a "why"
5. **Plan for testing early**: Testing strategy should influence criterion design
6. **Maintain traceability**: Use consistent IDs for cross-referencing
7. **Keep the matrix sparse**: Not every stakeholder cares about everything
8. **Include failure scenarios**: Operational context should cover what happens when things go wrong
9. **Version the document**: This is a living document that will evolve
10. **Connect to the chain**: Reference the field survey and (when available) the functional architecture

## Validation vs. Verification

**Verification** (deterministic checks against spec-for-conceptual-architecture):
- All required sections present
- Stakeholder count matches subsection count
- Criterion count matches table rows
- Matrix covers all stakeholders and criteria
- Testing strategy covers all criteria
- Frontmatter fields correctly typed

**Validation** (qualitative assessment against this guidance):
- Stakeholder Completeness: Are all relevant stakeholders included?
- Criterion Quality: Are criteria SMART and testable?
- Matrix Accuracy: Are relationships meaningful and justified?
- ConOps Clarity: Is operational context vivid and specific?
- Testing Strategy: Are test approaches feasible and specific?
- Traceability: Can elements be traced from field survey to tests?

## Tooling Support

### Verification Commands

```bash
# Verify structure against spec
python scripts/verify_template_based.py 00_vertices/conceptual-architecture-<name>.md --templates templates
```

### Validation Support

Conceptual architecture document validation requires human review against the six quality criteria above. A validator should:

1. Read the complete document
2. Assess each criterion (Excellent/Good/Needs Improvement)
3. Provide specific feedback for any criterion below "Good"
4. Document assessment in a validation edge with `human_approver` field

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Stakeholder Completeness**: Written for conceptual architecture authors (clear audience)
- **Criterion Quality**: Quality criteria are specific with three assessment levels
- **Matrix Accuracy**: Section guidance maps to quality criteria
- **ConOps Clarity**: Workflow and checkpoints describe operational use
- **Testing Strategy**: Validation vs. Verification section addresses testing
- **Traceability**: References spec-for-conceptual-architecture for structural requirements

---

**Note:** This guidance pairs with `spec-for-conceptual-architecture.md` via a coupling edge. The spec defines structure; this guidance defines quality.
