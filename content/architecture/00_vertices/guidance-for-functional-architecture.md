---
type: vertex/guidance
extends: doc
id: v:guidance:functional-architecture
name: Guidance for Functional Architecture Documents
description: Quality criteria and best practices for creating effective functional architecture documents with function-criterion matrices
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies: []
criteria:
  - criterion-coverage
  - function-completeness
  - io-clarity
  - technology-independence
  - testing-strategy
  - traceability
---

# Guidance for Functional Architecture Documents

**This guidance helps authors create high-quality functional architecture documents that effectively define system functions and trace them to acceptance criteria.**

## Purpose

Functional architecture documents define what the system must DO to meet stakeholder needs. They bridge the gap between conceptual needs (what stakeholders want) and logical design (how the system is structured). This guidance helps authors create functional architectures that have complete criterion coverage, clear input/output specifications, and maintain technology independence.

## Document Overview

### What This Guidance Covers

Functional architecture documents focus on system behaviors:
- **Function Identification**: What behaviors must the system exhibit?
- **Input/Output Specification**: What data flows in and out of each function?
- **Criterion Tracing**: Which functions address which acceptance criteria?
- **Function-Criterion Matrix**: The bipartite relationship between behaviors and needs
- **System Testing**: How will functions be tested at the system level?

### Best Use Cases

1. **Requirements Refinement**: Translating acceptance criteria into testable functions
2. **Behavior Documentation**: Capturing what the system does without implementation bias
3. **Test Planning**: Establishing system-level test strategies
4. **Design Foundation**: Providing clear requirements for logical architecture
5. **Traceability**: Ensuring all acceptance criteria are addressed by functions

### When NOT to Use

- When conceptual architecture has not been completed (prerequisite missing)
- For pure data models without behavioral requirements
- When system behaviors are already well-documented elsewhere
- For trivial systems with obvious single functions

## Quality Criteria

### 1. Criterion Coverage

**Excellent:** Every acceptance criterion from the conceptual architecture is addressed by at least one function. Coverage analysis explicitly shows how criteria map to functions. No orphan criteria exist.

**Good:** Most acceptance criteria are addressed. Coverage is reasonable with clear justification for any gaps.

**Needs Improvement:** Significant criteria are unaddressed. No clear analysis of coverage. Functions exist without connection to stakeholder needs.

**Tips:**
- Create a reverse traceability table: criteria → functions
- Ask for each criterion: "Which function(s) make this criterion achievable?"
- Orphan criteria indicate missing functions or scope issues
- Document intentional gaps with rationale

### 2. Function Completeness

**Excellent:** Functions cover all system behaviors comprehensively. Both happy path and error handling are addressed. Functions are appropriately granular—neither too coarse nor too fine.

**Good:** Major system behaviors are covered. Some edge cases may be missing but core functionality is complete.

**Needs Improvement:** Key behaviors are missing. Functions are too coarse (doing too much) or too fine (fragmented). Error handling is absent.

**Tips:**
- Walk through operational scenarios from the conceptual architecture
- Ask: "What must the system DO in each scenario?"
- Consider normal operation, error conditions, and edge cases
- Functions should be testable as units of behavior

### 3. I/O Clarity

**Excellent:** Every function has clearly specified inputs and outputs. Data types and constraints are defined. Inputs and outputs are consistent across functions (same data has same name).

**Good:** Inputs and outputs are specified for all functions. Some ambiguity may exist but overall flow is clear.

**Needs Improvement:** Inputs or outputs are vague or missing. Data flows are inconsistent. Reader cannot understand what goes in and comes out.

**Tips:**
- Name inputs/outputs consistently across functions
- Specify data types where relevant (document, configuration, event, etc.)
- Consider both data inputs and trigger conditions
- Outputs should include both results and side effects

### 4. Technology Independence

**Excellent:** Functions describe behaviors without any reference to implementation technology. The same functional architecture could be implemented with different technology stacks. No "how" leaks into the "what."

**Good:** Functions are mostly technology-agnostic. Minor technology hints may appear but don't constrain design.

**Needs Improvement:** Functions reference specific technologies (e.g., "Query PostgreSQL database" instead of "Retrieve stored data"). Implementation decisions are embedded in function descriptions.

**Tips:**
- Use verb-noun naming: "Verify Document", "Generate Report", "Notify User"
- Avoid technology terms: API, database, file, REST, JSON
- Describe what happens, not how it's implemented
- Ask: "Could this function be implemented differently?"

### 5. Testing Strategy

**Excellent:** Every function has a clear system-level test approach. Test methods are specific and executable. Success indicators are measurable. Tests cover both positive and negative cases.

**Good:** Most functions have defined test approaches. Methods are reasonable. Success indicators are present.

**Needs Improvement:** Test approaches are vague or missing. Methods are infeasible. Success indicators are undefined or subjective.

**Tips:**
- System tests verify function behavior end-to-end
- Consider test data and preconditions
- Include both success and failure scenarios
- Test methods should be independent of implementation

### 6. Traceability

**Excellent:** Clear bidirectional traceability: conceptual architecture → functions → logical architecture (when available). Every function traces to criteria. Every criterion traces to functions.

**Good:** Forward traceability is clear. Most elements can be traced. Conceptual architecture connection is evident.

**Needs Improvement:** Traceability is weak or absent. Functions don't connect to criteria. Conceptual architecture reference is nominal only.

**Tips:**
- Use consistent IDs (AC1, F1) for cross-referencing
- The Function-Criterion Matrix is your traceability artifact
- Verify matrix completeness before finalizing
- Consider creating reverse traceability view (criteria → functions)

## Section-by-Section Guidance

### Purpose

**Goal:** Orient readers to what this document establishes.

**Tips:**
- State what system functions this document defines
- Mention the system being architected
- Keep to 1-3 sentences

**Anti-patterns:**
- Describing implementation details

**Preferred:**
- Clear, concise statement of functional scope

### Overview

**Goal:** Provide context and connect to the architecture chain.

**Tips:**
- Reference the conceptual architecture explicitly
- Explain where this document fits in the chain
- Mention what functions will enable

**Anti-patterns:**
- Generic descriptions that could apply to any system

**Preferred:**
- Specific context grounding the reader

### Conceptual Architecture Reference

**Goal:** Establish prerequisite connection and summarize acceptance criteria.

**Tips:**
- Use Obsidian link syntax
- Include all acceptance criteria that functions must address
- Keep the summary concise—details are in the source document

**Anti-patterns:**
- Copying entire conceptual architecture content

**Preferred:**
- Curated criteria summary with clear traceability intent

### Functional Architecture

**Goal:** Define all system functions with clear I/O.

**Tips:**
- Start with Function Table for overview, then detail each
- Use consistent ID format (F1, F2, F3...)
- Make inputs and outputs specific and named
- Behavior descriptions should explain what, not how

**Anti-patterns:**
- "Process data" (too vague)
- "Call REST API to fetch records" (technology-specific)

**Preferred:**
- "Retrieve configuration parameters for the specified context"
- "Validate document structure against specification requirements"

### Function-Criterion Matrix

**Goal:** Map functions to acceptance criteria.

**Tips:**
- Matrix View is for quick scanning—keep it simple (X marks)
- Relationship Details provides the "how" for each relationship
- Not every function addresses every criterion—sparsity is expected
- Key Traces should highlight the most critical relationships

**Anti-patterns:**
- Fully connected matrix (every function addresses everything)
- Missing rationale for relationships

**Preferred:**
- Thoughtfully sparse matrix with justified relationships

### System Testing Strategy

**Goal:** Define how system-level testing will verify functions.

**Tips:**
- System tests are end-to-end, not unit tests
- Consider integration with other functions
- Include both positive and negative test cases
- Success indicators should be observable

**Anti-patterns:**
- Vague test methods ("will be tested")
- Implementation-specific tests

**Preferred:**
- Specific, executable test approaches with clear success criteria

## Workflow Guidance

### Recommended Authoring Sequence

1. **Review Conceptual Architecture** (15 min)
   - Read acceptance criteria thoroughly
   - Understand stakeholder needs
   - Note operational scenarios

2. **Identify Functions** (30 min)
   - For each criterion, ask: "What must the system DO?"
   - List candidate functions
   - Group related behaviors

3. **Specify I/O** (30 min)
   - For each function, define inputs
   - For each function, define outputs
   - Ensure consistency across functions

4. **Build the Matrix** (20 min)
   - Map each function to relevant criteria
   - Add contribution types and rationale
   - Identify key traces

5. **Define Testing Strategy** (20 min)
   - For each function, define system test approach
   - Consider positive and negative cases
   - Specify success indicators

6. **Write Context Sections** (15 min)
   - Purpose, Overview, Conceptual Architecture Reference
   - These frame the detailed content

### Quality Checkpoints

- **After Function Identification:** Do functions cover all acceptance criteria?
- **After I/O Specification:** Are inputs and outputs clear and consistent?
- **After Matrix:** Does every function contribute to at least one criterion?
- **After Testing:** Is every function covered by a test approach?
- **Final:** Does the document trace cleanly from criteria to functions to tests?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Orphan Criteria | Acceptance criteria with no addressing function | Add functions or document why criterion is out of scope |
| Technology Leakage | Functions reference specific technologies | Rewrite using behavior-focused language |
| Vague I/O | "Input: data" without specificity | Name and describe each input/output |
| Coarse Functions | Single function does too much | Decompose into smaller, testable behaviors |
| Missing Error Handling | Only happy path functions defined | Add functions for error conditions |
| Untestable Functions | No clear way to verify behavior | Rewrite with observable outcomes |

## Best Practices

1. **Start from criteria**: Every function should trace to at least one acceptance criterion
2. **Keep functions focused**: Each function should have a single, clear purpose
3. **Be specific about I/O**: Named, typed inputs and outputs enable clear testing
4. **Stay technology-agnostic**: Describe what, not how
5. **Plan for testing**: If you can't test it, it's not well-defined
6. **Maintain traceability**: Use consistent IDs for cross-referencing
7. **Consider error cases**: Systems fail—functions should handle it
8. **Review with stakeholders**: Validate that functions address their needs
9. **Version the document**: Functional architecture evolves with understanding
10. **Connect the chain**: Reference conceptual architecture and (when available) logical architecture

## Validation vs. Verification

**Verification** (deterministic checks against spec-for-functional-architecture):
- All required sections present
- Function count matches subsection count
- Matrix covers all functions and criteria
- Testing strategy covers all functions
- Frontmatter fields correctly typed

**Validation** (qualitative assessment against this guidance):
- Criterion Coverage: Are all acceptance criteria addressed?
- Function Completeness: Do functions cover all behaviors?
- I/O Clarity: Are inputs and outputs specific?
- Technology Independence: Are functions free of implementation details?
- Testing Strategy: Are test approaches feasible and specific?
- Traceability: Can elements be traced from criteria to functions to tests?

## Tooling Support

### Verification Commands

```bash
# Verify structure against spec
python scripts/verify_template_based.py 00_vertices/functional-architecture-<name>.md --templates templates
```

### Validation Support

Functional architecture document validation requires human review against the six quality criteria above. A validator should:

1. Read the complete document
2. Assess each criterion (Excellent/Good/Needs Improvement)
3. Provide specific feedback for any criterion below "Good"
4. Document assessment in a validation edge with `human_approver` field

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Criterion Coverage**: Written for functional architecture authors (clear audience)
- **Function Completeness**: Covers all aspects of document creation
- **I/O Clarity**: Quality criteria inputs (document) and outputs (assessment) are clear
- **Technology Independence**: Advice is framework-agnostic
- **Testing Strategy**: Validation vs. Verification section addresses testing
- **Traceability**: References spec-for-functional-architecture for structural requirements

---

**Note:** This guidance pairs with `spec-for-functional-architecture.md` via a coupling edge. The spec defines structure; this guidance defines quality.
