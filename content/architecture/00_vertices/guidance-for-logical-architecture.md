---
type: vertex/guidance
extends: doc
id: v:guidance:logical-architecture
name: Guidance for Logical Architecture Documents
description: Quality criteria and best practices for creating effective logical architecture documents with component-function matrices
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies: []
criteria:
  - function-coverage
  - component-cohesion
  - interface-clarity
  - technology-independence
  - testing-strategy
  - traceability
---

# Guidance for Logical Architecture Documents

**This guidance helps authors create high-quality logical architecture documents that effectively define system components and trace them to the functions they realize.**

## Purpose

Logical architecture documents define HOW the system is structured to perform its functions. They bridge the gap between functional requirements (what the system does) and physical implementation (what technologies are used). This guidance helps authors create logical architectures that maintain strict technology independence, have clear component responsibilities, and well-defined interfaces.

## Document Overview

### What This Guidance Covers

Logical architecture documents focus on system structure:
- **Component Identification**: What are the building blocks of the system?
- **Responsibility Assignment**: What is each component responsible for?
- **Interface Definition**: How do components interact?
- **Function Allocation**: Which components realize which functions?
- **Integration Testing**: How will component interactions be tested?

### Best Use Cases

1. **Design Documentation**: Capturing system structure before implementation
2. **Component Specification**: Defining building blocks independent of technology
3. **Interface Contracts**: Establishing how components communicate
4. **Test Planning**: Establishing integration test strategies
5. **Technology Flexibility**: Creating designs that can be implemented multiple ways

### When NOT to Use

- When functional architecture has not been completed (prerequisite missing)
- For trivial systems with single components
- When technology choices are already fixed and documented elsewhere
- For pure data architectures without behavioral components

## Quality Criteria

### 1. Function Coverage

**Excellent:** Every function from the functional architecture is realized by at least one component. Coverage analysis explicitly shows how functions map to components. No orphan functions exist.

**Good:** Most functions are realized. Coverage is reasonable with clear justification for any gaps.

**Needs Improvement:** Significant functions are unrealized. No clear analysis of coverage. Components exist without connection to system behaviors.

**Tips:**
- Create a reverse traceability table: functions → components
- Ask for each function: "Which component(s) perform this?"
- Orphan functions indicate missing components
- Multiple components can collaborate on one function

### 2. Component Cohesion

**Excellent:** Each component has a single, clear responsibility. Components are appropriately sized—neither too large (doing too much) nor too small (fragmented). Component names reflect responsibilities.

**Good:** Components have clear responsibilities. Some overlap may exist but boundaries are reasonable.

**Needs Improvement:** Components have multiple unrelated responsibilities. Components are too coarse (god components) or too fine (over-decomposition). Responsibilities are unclear.

**Tips:**
- Apply Single Responsibility Principle: one reason to change
- Component names should be nouns describing what it IS, not what it DOES
- If responsibility description needs "and", consider splitting
- Components should be independently replaceable

### 3. Interface Clarity

**Excellent:** Every interface is clearly defined with from/to components, data exchanged, and direction. Interface protocols are specified at a logical level. Interface specifications enable independent development.

**Good:** Interfaces are specified for all component interactions. Some details may be missing but overall contracts are clear.

**Needs Improvement:** Interfaces are vague or missing. Data flows are unclear. Components are described in isolation without interaction specification.

**Tips:**
- Every component should have at least one interface
- Specify direction: who initiates, who responds
- Name the data exchanged, don't just say "data"
- Keep protocols logical (request-response, event, stream) not technical (REST, gRPC)

### 4. Technology Independence

**Excellent:** Components describe responsibilities and interfaces without ANY reference to implementation technology. The same logical architecture could be implemented with different technology stacks. Component names use domain terms, not technology terms.

**Good:** Components are mostly technology-agnostic. Minor technology hints may appear but don't constrain implementation.

**Needs Improvement:** Components reference specific technologies (e.g., "PostgreSQL Database" instead of "Persistent Data Store"). Implementation decisions are embedded in component descriptions.

**Tips:**
- Use responsibility-focused names: "Validation Service" not "Python Validator"
- Avoid technology terms: database, API, REST, file, JSON, HTTP
- Describe what the component IS responsible for, not HOW it works
- Ask: "Could this be implemented with completely different technology?"
- This is the MOST CRITICAL quality criterion for logical architecture

### 5. Testing Strategy

**Excellent:** Every interface has a clear integration test approach. Test methods verify component interactions. Success indicators are measurable. Tests cover both successful and failed interactions.

**Good:** Most interfaces have defined test approaches. Methods are reasonable. Success indicators are present.

**Needs Improvement:** Test approaches are vague or missing. Methods focus on components in isolation, not integration. Success indicators are undefined.

**Tips:**
- Integration tests verify component INTERACTIONS, not components in isolation
- Test the interface contract: does data flow correctly?
- Consider failure modes: what if a component is unavailable?
- Test methods should be independent of specific technology

### 6. Traceability

**Excellent:** Clear bidirectional traceability: functional architecture → components → physical architecture (when available). Every component traces to functions. Every function traces to components.

**Good:** Forward traceability is clear. Most elements can be traced. Functional architecture connection is evident.

**Needs Improvement:** Traceability is weak or absent. Components don't connect to functions. Functional architecture reference is nominal only.

**Tips:**
- Use consistent IDs (F1, C1) for cross-referencing
- The Component-Function Matrix is your traceability artifact
- Verify matrix completeness before finalizing
- Consider creating reverse traceability view (functions → components)

## Section-by-Section Guidance

### Purpose

**Goal:** Orient readers to what this document establishes.

**Tips:**
- State what system components this document defines
- Mention the system being architected
- Keep to 1-3 sentences

**Anti-patterns:**
- Describing implementation details

**Preferred:**
- Clear, concise statement of structural scope

### Overview

**Goal:** Provide context and connect to the architecture chain.

**Tips:**
- Reference the functional architecture explicitly
- Explain where this document fits in the chain
- Mention what components will enable

**Anti-patterns:**
- Generic descriptions that could apply to any system

**Preferred:**
- Specific context grounding the reader

### Functional Architecture Reference

**Goal:** Establish prerequisite connection and summarize functions.

**Tips:**
- Use Obsidian link syntax
- Include all functions that components must realize
- Keep the summary concise—details are in the source document

**Anti-patterns:**
- Copying entire functional architecture content

**Preferred:**
- Curated function summary with clear traceability intent

### Logical Architecture

**Goal:** Define all system components with clear responsibilities and interfaces.

**Tips:**
- Start with Component Table for overview, then detail each
- Use consistent ID format (C1, C2, C3...)
- Single responsibility per component
- Define all interfaces in Interface Specifications

**Anti-patterns:**
- "Database Component" (technology-specific)
- "Core Component" (vague responsibility)
- Components without interfaces

**Preferred:**
- "Persistent Data Store" (responsibility: durably store and retrieve data)
- "Validation Engine" (responsibility: verify document compliance)

### Component-Function Matrix

**Goal:** Map components to functions.

**Tips:**
- Matrix View is for quick scanning—keep it simple (X marks)
- Relationship Details provides the "how" for each relationship
- Multiple components often collaborate on one function
- Key Allocations should highlight the most critical mappings

**Anti-patterns:**
- One-to-one mapping (every function = one component)
- Missing rationale for relationships

**Preferred:**
- Thoughtful allocation showing collaboration patterns

### Integration Testing Strategy

**Goal:** Define how integration testing will verify interfaces.

**Tips:**
- Integration tests verify INTERACTIONS between components
- Focus on interface contracts
- Include both success and failure scenarios
- Success indicators should be observable at interfaces

**Anti-patterns:**
- Unit tests masquerading as integration tests
- Technology-specific test approaches

**Preferred:**
- Specific, executable test approaches verifying component contracts

## Workflow Guidance

### Recommended Authoring Sequence

1. **Review Functional Architecture** (15 min)
   - Read functions thoroughly
   - Understand I/O relationships
   - Note function groupings

2. **Identify Components** (30 min)
   - Group related functions
   - Define component responsibilities
   - Name components by responsibility

3. **Define Interfaces** (30 min)
   - Identify component interactions
   - Specify data exchanged
   - Define protocols at logical level

4. **Build the Matrix** (20 min)
   - Map each component to realized functions
   - Add realization types and rationale
   - Identify key allocations

5. **Define Testing Strategy** (20 min)
   - For each interface, define integration test approach
   - Consider success and failure cases
   - Specify success indicators

6. **Write Context Sections** (15 min)
   - Purpose, Overview, Functional Architecture Reference
   - These frame the detailed content

### Quality Checkpoints

- **After Component Identification:** Do components realize all functions?
- **After Interface Definition:** Are all component interactions specified?
- **After Matrix:** Does every component realize at least one function?
- **After Testing:** Is every interface covered by a test approach?
- **Technology Check:** Could this be implemented with different technology? (CRITICAL)
- **Final:** Does the document trace cleanly from functions to components to tests?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Orphan Functions | Functions with no realizing component | Add components or document why function is out of scope |
| Technology Leakage | Components reference specific technologies | Rename to responsibility-focused terms; remove technology references |
| God Component | Single component does everything | Decompose by responsibility |
| Missing Interfaces | Components defined in isolation | Add Interface Specifications connecting all components |
| Vague Responsibilities | "Handles processing" | Be specific: "Validates document structure against specification" |
| One-to-One Mapping | Every function = exactly one component | Allow collaboration; components can share function realization |

## Best Practices

1. **Start from functions**: Every component should realize at least one function
2. **Single responsibility**: Each component has one clear purpose
3. **Name by responsibility**: Component names describe what it IS, not what technology it uses
4. **Define all interfaces**: No component is an island
5. **Stay technology-agnostic**: This is the stable core—it should survive technology changes
6. **Plan for integration**: If you can't test the interface, it's not well-defined
7. **Maintain traceability**: Use consistent IDs for cross-referencing
8. **Allow collaboration**: Multiple components can realize one function together
9. **Version the document**: Logical architecture should change less than physical
10. **Connect the chain**: Reference functional architecture and (when available) physical architecture

## Validation vs. Verification

**Verification** (deterministic checks against spec-for-logical-architecture):
- All required sections present
- Component count matches subsection count
- Matrix covers all components and functions
- Integration testing strategy covers all interfaces
- Frontmatter fields correctly typed

**Validation** (qualitative assessment against this guidance):
- Function Coverage: Are all functions realized?
- Component Cohesion: Do components have single responsibilities?
- Interface Clarity: Are interfaces well-defined?
- Technology Independence: Are components free of technology references? (CRITICAL)
- Testing Strategy: Are integration test approaches specific?
- Traceability: Can elements be traced from functions to components to tests?

## Tooling Support

### Verification Commands

```bash
# Verify structure against spec
python scripts/verify_template_based.py 00_vertices/logical-architecture-<name>.md --templates templates
```

### Validation Support

Logical architecture document validation requires human review against the six quality criteria above. A validator should:

1. Read the complete document
2. Assess each criterion (Excellent/Good/Needs Improvement)
3. **Pay special attention to Technology Independence** (most common failure)
4. Provide specific feedback for any criterion below "Good"
5. Document assessment in a validation edge with `human_approver` field

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Function Coverage**: Written for logical architecture authors (clear audience)
- **Component Cohesion**: Sections have single purposes
- **Interface Clarity**: Quality criteria inputs and outputs are clear
- **Technology Independence**: Advice is framework-agnostic
- **Testing Strategy**: Validation vs. Verification section addresses testing
- **Traceability**: References spec-for-logical-architecture for structural requirements

---

**Note:** This guidance pairs with `spec-for-logical-architecture.md` via a coupling edge. The spec defines structure; this guidance defines quality.
