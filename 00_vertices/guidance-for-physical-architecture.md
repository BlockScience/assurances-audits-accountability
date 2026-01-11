---
type: vertex/guidance
extends: doc
id: v:guidance:physical-architecture
name: Guidance for Physical Architecture Documents
description: Quality criteria and best practices for creating effective physical architecture documents with element-component matrices
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-11T00:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies: []
criteria:
  - component-coverage
  - technology-specificity
  - rationale-clarity
  - deployment-clarity
  - testing-strategy
  - traceability
---

# Guidance for Physical Architecture Documents

**This guidance helps authors create high-quality physical architecture documents that effectively define concrete technology choices and trace them to logical components.**

## Purpose

Physical architecture documents define WHAT specific technologies implement the system design. They complete the architecture chain by translating abstract logical components into concrete tools, frameworks, and services. This guidance helps authors create physical architectures that have complete component coverage, specific technology choices with versions, clear rationale, and well-defined deployment configurations.

## Document Overview

### What This Guidance Covers

Physical architecture documents focus on implementation specifics:
- **Technology Selection**: What specific tools, frameworks, and services are used?
- **Version Management**: What versions of technologies are deployed?
- **Implementation Rationale**: Why was each technology chosen?
- **Component Implementation**: Which elements implement which components?
- **Deployment Configuration**: How are elements deployed together?
- **Unit Testing**: How are individual elements tested?

### Best Use Cases

1. **Implementation Documentation**: Recording technology decisions and rationale
2. **Deployment Planning**: Defining how technologies are configured together
3. **Technology Governance**: Establishing what technologies are approved for use
4. **Test Planning**: Defining unit test strategies per technology
5. **Architecture Completion**: Finishing the chain from needs to implementation

### When NOT to Use

- When logical architecture has not been completed (prerequisite missing)
- For technology-agnostic documentation (use logical architecture instead)
- When technologies are still under evaluation
- For theoretical designs without planned implementation

## Quality Criteria

### 1. Component Coverage

**Excellent:** Every logical component is implemented by at least one physical element. Coverage analysis explicitly shows how components map to elements. No orphan components exist.

**Good:** Most components are implemented. Coverage is reasonable with clear justification for any gaps.

**Needs Improvement:** Significant components are unimplemented. No clear analysis of coverage. Elements exist without connection to logical design.

**Tips:**
- Create a reverse traceability table: components → elements
- Ask for each component: "What technology implements this?"
- Orphan components indicate missing elements or deferred implementation
- Multiple elements can collaborate to implement one component

### 2. Technology Specificity

**Excellent:** Every element names a specific technology with version. No vague references like "a database" or "some framework." Technologies are named precisely enough to be installed/configured.

**Good:** Technologies are specific. Some minor version ambiguity may exist but implementations are identifiable.

**Needs Improvement:** Elements use vague technology references. Versions are missing. Reader cannot determine what to install.

**Tips:**
- Name specific products: "PostgreSQL 15.2" not "a relational database"
- Include versions or version constraints: "Python 3.11+" not just "Python"
- Distinguish between products and categories: "GitHub Actions" not "CI/CD tool"
- If technology is TBD, document that explicitly with selection criteria

### 3. Rationale Clarity

**Excellent:** Every technology choice includes clear rationale explaining why it was selected. Alternatives considered are documented. Trade-offs are acknowledged. Reader understands the decision-making process.

**Good:** Rationale exists for most technology choices. Reasoning is clear. Some alternatives may be mentioned.

**Needs Improvement:** Technology choices have no rationale. Reader cannot understand why specific tools were chosen. Decisions appear arbitrary.

**Tips:**
- Answer "why this technology?" for each element
- Document alternatives considered
- Acknowledge trade-offs and limitations
- Reference organizational standards if applicable
- Consider: cost, familiarity, performance, ecosystem, support

### 4. Deployment Clarity

**Excellent:** Deployment view clearly explains how elements are configured and deployed together. Environment-specific configurations are documented. Dependencies between elements are clear. Reader could replicate the deployment.

**Good:** Deployment is described adequately. Major configuration aspects are covered. Environment differences noted.

**Needs Improvement:** Deployment view is vague or missing. Configuration is unclear. Reader cannot understand how elements work together.

**Tips:**
- Describe the deployment topology (single server, distributed, cloud, etc.)
- Document environment-specific configurations
- Note element dependencies and startup order
- Include configuration file examples where helpful
- Consider: development, staging, production environments

### 5. Testing Strategy

**Excellent:** Every element has a clear unit test approach. Test frameworks are specific and appropriate for the technology. Success indicators are measurable. Test coverage expectations are defined.

**Good:** Most elements have defined test approaches. Frameworks are reasonable. Success indicators are present.

**Needs Improvement:** Test approaches are vague or missing. Frameworks are unspecified. Success indicators are undefined.

**Tips:**
- Unit tests verify individual elements in isolation
- Match test framework to technology (pytest for Python, Jest for JavaScript)
- Define meaningful success indicators
- Consider mocking strategies for dependencies
- Include both positive and negative test cases

### 6. Traceability

**Excellent:** Clear bidirectional traceability: logical architecture → physical elements. Every element traces to components. Every component traces to elements. Full chain visible from stakeholder needs to implementation.

**Good:** Forward traceability is clear. Most elements can be traced. Logical architecture connection is evident.

**Needs Improvement:** Traceability is weak or absent. Elements don't connect to components. Logical architecture reference is nominal only.

**Tips:**
- Use consistent IDs (C1, E1) for cross-referencing
- The Element-Component Matrix is your traceability artifact
- Verify matrix completeness before finalizing
- Consider creating full-chain traceability (needs → criteria → functions → components → elements)

## Section-by-Section Guidance

### Purpose

**Goal:** Orient readers to what this document establishes.

**Tips:**
- State what technology choices this document defines
- Mention the system being implemented
- Keep to 1-3 sentences

**Anti-patterns:**
- Describing logical architecture content

**Preferred:**
- Clear, concise statement of implementation scope

### Overview

**Goal:** Provide context and connect to the architecture chain.

**Tips:**
- Reference the logical architecture explicitly
- Explain where this document fits in the chain
- Mention that this completes the extended architecture series

**Anti-patterns:**
- Generic descriptions that could apply to any system

**Preferred:**
- Specific context grounding the reader in implementation decisions

### Logical Architecture Reference

**Goal:** Establish prerequisite connection and summarize components.

**Tips:**
- Use Obsidian link syntax
- Include all components that elements must implement
- Keep the summary concise—details are in the source document

**Anti-patterns:**
- Copying entire logical architecture content

**Preferred:**
- Curated component summary with clear traceability intent

### Physical Architecture

**Goal:** Define all physical elements with specific technologies and rationale.

**Tips:**
- Start with Element Table for overview, then detail each
- Use consistent ID format (E1, E2, E3...)
- ALWAYS include version information
- ALWAYS include rationale for each choice
- Deployment View should enable someone to set up the system

**Anti-patterns:**
- "Database" (too vague)
- "Latest version" (not specific)
- Technology choice without rationale

**Preferred:**
- "PostgreSQL 15.2 (chosen for JSONB support, team familiarity, and cost)"

### Element-Component Matrix

**Goal:** Map elements to components.

**Tips:**
- Matrix View is for quick scanning—keep it simple (X marks)
- Relationship Details provides the "how" for each relationship
- Some elements implement multiple components (shared infrastructure)
- Key Implementations should highlight critical technology decisions

**Anti-patterns:**
- Elements that don't map to any component
- Missing rationale for implementation relationships

**Preferred:**
- Clear mapping with justified relationships

### Unit Testing Strategy

**Goal:** Define how unit testing will verify individual elements.

**Tips:**
- Unit tests verify elements in ISOLATION
- Match test framework to technology stack
- Include mocking/stubbing strategy
- Success indicators should be specific and measurable

**Anti-patterns:**
- Integration tests masquerading as unit tests
- Vague test approaches

**Preferred:**
- Specific, executable test approaches with appropriate frameworks

## Workflow Guidance

### Recommended Authoring Sequence

1. **Review Logical Architecture** (15 min)
   - Read components thoroughly
   - Understand responsibilities and interfaces
   - Note technology constraints from higher layers

2. **Select Technologies** (45 min)
   - For each component, identify implementation options
   - Evaluate alternatives against criteria
   - Document selection rationale

3. **Define Elements** (30 min)
   - Name elements with specific technologies
   - Include versions
   - Document rationale

4. **Build the Matrix** (20 min)
   - Map each element to implemented components
   - Add implementation types and rationale
   - Identify key implementations

5. **Define Deployment** (20 min)
   - Describe deployment topology
   - Document environment configurations
   - Note element dependencies

6. **Define Testing Strategy** (15 min)
   - For each element, define unit test approach
   - Select appropriate frameworks
   - Specify success indicators

7. **Write Context Sections** (10 min)
   - Purpose, Overview, Logical Architecture Reference
   - These frame the detailed content

### Quality Checkpoints

- **After Technology Selection:** Are all components covered by elements?
- **After Element Definition:** Are technologies specific with versions?
- **After Rationale:** Is every choice justified?
- **After Matrix:** Does every element implement at least one component?
- **After Deployment:** Could someone set up the system from this document?
- **After Testing:** Is every element covered by a test approach?
- **Final:** Does the document complete the traceability chain?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Orphan Components | Logical components with no implementing element | Add elements or document why implementation is deferred |
| Vague Technologies | "A database" instead of specific product | Name specific product with version |
| Missing Versions | Technology named without version | Add version or version constraint |
| No Rationale | Technology choice without explanation | Document why this technology was selected |
| Missing Deployment | Elements defined but not deployment | Add Deployment View explaining configuration |
| Integration as Unit | Tests verify multiple elements together | Separate unit tests (isolation) from integration tests |

## Best Practices

1. **Be specific**: Name exact technologies with versions
2. **Explain choices**: Every technology needs rationale
3. **Complete the chain**: Ensure all components are implemented
4. **Plan for deployment**: Document how elements work together
5. **Version everything**: Include version constraints even if flexible
6. **Consider alternatives**: Document why rejected options weren't chosen
7. **Match test frameworks**: Use appropriate test tools for each technology
8. **Document dependencies**: Note what elements depend on each other
9. **Think about environments**: Consider dev/staging/prod differences
10. **Maintain traceability**: Use consistent IDs across the architecture chain

## Validation vs. Verification

**Verification** (deterministic checks against spec-for-physical-architecture):
- All required sections present
- Element count matches subsection count
- Matrix covers all elements and components
- Unit testing strategy covers all elements
- Frontmatter fields correctly typed

**Validation** (qualitative assessment against this guidance):
- Component Coverage: Are all components implemented?
- Technology Specificity: Are technologies named with versions?
- Rationale Clarity: Are choices explained?
- Deployment Clarity: Is deployment well-defined?
- Testing Strategy: Are unit test approaches specific?
- Traceability: Can elements be traced from components to tests?

## Tooling Support

### Verification Commands

```bash
# Verify structure against spec
python scripts/verify_template_based.py 00_vertices/physical-architecture-<name>.md --templates templates
```

### Validation Support

Physical architecture document validation requires human review against the six quality criteria above. A validator should:

1. Read the complete document
2. Assess each criterion (Excellent/Good/Needs Improvement)
3. **Pay special attention to Technology Specificity** (must have versions)
4. Provide specific feedback for any criterion below "Good"
5. Document assessment in a validation edge with `human_approver` field

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Component Coverage**: Written for physical architecture authors (clear audience)
- **Technology Specificity**: Quality criteria are specific and measurable
- **Rationale Clarity**: Each criterion explains why it matters
- **Deployment Clarity**: Workflow section explains how to use this guidance
- **Testing Strategy**: Validation vs. Verification section addresses testing
- **Traceability**: References spec-for-physical-architecture for structural requirements

---

**Note:** This guidance pairs with `spec-for-physical-architecture.md` via a coupling edge. The spec defines structure; this guidance defines quality.
