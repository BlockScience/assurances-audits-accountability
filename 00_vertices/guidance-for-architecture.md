---
type: vertex/guidance
extends: doc
id: v:guidance:architecture
name: Guidance for Architecture Documents
description: Quality criteria and best practices for creating effective architecture documents using the 4-layer SE framework
tags:
  - vertex
  - doc
  - guidance
version: 1.1.0
created: 2025-12-30T12:00:00Z
modified: 2025-01-11T00:00:00Z
dependencies: []
criteria:
  - layer-completeness
  - v-model-alignment
  - traceability
  - testability
  - stakeholder-clarity
  - technology-independence
---

# Guidance for Architecture Documents

**This guidance helps authors create high-quality architecture documents that effectively describe systems across the four-layer SE framework (Conceptual, Functional, Logical, Physical).**

## Purpose

Architecture documents serve as the authoritative description of a system's structure across multiple abstraction levels. This guidance helps authors create architecture documents that are complete, coherent, traceable, and useful for both development and evaluation. It provides quality criteria, section-specific advice, and common pitfalls to avoid.

## Document Overview

### What This Guidance Covers

Architecture documents describe systems using the four-layer framework:
- **Conceptual Layer**: Stakeholder needs and operational context (ConOps)
- **Functional Layer**: What the system must do (functions and behaviors)
- **Logical Layer**: Design-independent component structure
- **Physical Layer**: Specific implementation choices

Each layer corresponds to a V-model evaluation level, creating a complete lifecycle from requirements through testing.

### Best Use Cases

1. **New System Development**: Establishing architecture before implementation begins
2. **System Documentation**: Capturing architecture of existing systems for maintenance
3. **Stakeholder Communication**: Explaining system structure to diverse audiences
4. **Verification Planning**: Defining test criteria at each abstraction level
5. **Self-Demonstrating Projects**: Projects that are instances of what they describe (like this framework)

## Choosing Architecture Mode

Architecture documents can be authored in two modes. Choose the appropriate mode based on your program's complexity and traceability requirements.

### When to Use Standard Mode (Inline Layers)

Use standard mode when:

- **Simple to medium complexity systems** where 3-5 items per layer is sufficient
- **Rapid prototyping** where speed matters more than detailed traceability
- **Internal documentation** where formal matrices aren't required
- **Single-person or small team** authorship
- **Shorter programs** with limited formal assurance requirements

Standard mode produces a single architecture document with all four layers documented inline. This is faster to produce and easier to maintain for smaller systems.

### When to Use Extended Mode (Reference Synthesis)

Use extended mode when:

- **Complex systems** requiring detailed stakeholder analysis
- **Formal programs** requiring acceptance criteria traceability
- **Multi-team projects** where each architecture layer may be owned separately
- **Assurance-critical work** requiring bipartite relationship matrices
- **Evolving designs** where layers change at different rates
- **Compliance requirements** requiring explicit traceability from stakeholder needs to implementation

Extended mode produces four separate extended architecture documents plus a summary architecture:

```text
field-survey (actors, resources)
    │
    ▼
conceptual-architecture (Stakeholder × Acceptance Criteria matrix)
    │
    ▼
functional-architecture (Function × Acceptance Criteria matrix)
    │
    ▼
logical-architecture (Component × Function matrix)
    │
    ▼
physical-architecture (Element × Component matrix)
    │
    ▼
architecture (V-Model synthesis referencing all four)
```

Each extended document contains a bipartite relationship matrix enabling full traceability from stakeholder needs through to implementation elements.

### Mode Comparison

| Aspect | Standard Mode | Extended Mode |
|--------|---------------|---------------|
| Documents produced | 1 architecture document | 4 extended + 1 summary |
| Traceability | Implicit through structure | Explicit via matrices |
| Authoring time | Faster (2-4 hours) | More thorough (1-2 days) |
| Layer ownership | Single owner | Can be distributed |
| Formal assurance | Basic verification | Full assurance with matrices |
| Best for | Small-medium systems | Complex, compliance-critical systems |

### Transitioning Between Modes

It is possible to start with standard mode and upgrade to extended mode later:

1. Extract each inline layer into its own extended architecture document
2. Build the bipartite relationship matrices
3. Update the summary architecture to reference the extended documents
4. Add the four `*_architecture_ref` frontmatter fields

However, starting in extended mode when rigorous traceability is expected will produce better results than retrofitting.

## Quality Criteria

### 1. Layer Completeness

**Excellent:** All four layers are substantively developed with rich detail. Each layer has 5+ elements with clear descriptions. Readers understand the system fully at each abstraction level.

**Good:** All four layers are present with adequate detail. Each layer has 3-4 elements. Readers can understand the system structure at each level.

**Needs Improvement:** Layers are present but thin. Some layers have fewer than 3 elements. Readers cannot fully understand the system from the document alone.

### 2. V-Model Alignment

**Excellent:** Each layer clearly shows both the "idealized" (design/requirements) side and the "realized" (testing/evaluation) side. The V-model table provides a compelling overview. Test criteria are specific and measurable.

**Good:** V-model structure is present and understandable. Both sides are represented for each layer. Test criteria are present but may lack specificity.

**Needs Improvement:** V-model alignment is unclear or inconsistent. Testing criteria are vague or missing for some layers. The relationship between design and testing is not evident.

### 3. Traceability

**Excellent:** Clear threads connect conceptual needs through functions, components, and implementations. A traceability matrix explicitly maps these relationships. Every implementation element traces to a stakeholder need.

**Good:** Logical flow exists from needs to implementation. Traceability is implied through document structure. Most elements can be traced across layers.

**Needs Improvement:** Traceability is weak or absent. Elements at lower layers don't clearly connect to higher-layer needs. Orphan elements exist without clear purpose.

### 4. Testability

**Excellent:** Each layer includes specific, measurable test criteria. Acceptance criteria use concrete success measures. System, integration, and unit tests are well-defined. Tests cover normal and edge cases.

**Good:** Test criteria exist for each layer. Criteria are reasonably specific. Basic coverage of expected behaviors.

**Needs Improvement:** Test criteria are vague ("system works correctly") or missing. No clear way to verify that requirements are met at each level.

### 5. Stakeholder Clarity

**Excellent:** Conceptual layer clearly articulates who the stakeholders are, what they need, and why. Problem statement resonates with stakeholder pain points. Acceptance criteria reflect stakeholder value, not just technical metrics.

**Good:** Stakeholders are identified and their needs described. Problem statement is clear. Acceptance criteria address stakeholder concerns.

**Needs Improvement:** Stakeholders are unclear or too abstract. Problem statement is technical rather than need-focused. Acceptance criteria don't connect to stakeholder value.

### 6. Technology Independence (Logical Layer)

**Excellent:** Logical layer describes components entirely in terms of responsibilities and interfaces, without mentioning specific technologies. The same logical architecture could be implemented with different technology stacks.

**Good:** Logical layer is mostly technology-agnostic. Some technology hints may appear but don't constrain the design.

**Needs Improvement:** Logical layer specifies technologies (e.g., "PostgreSQL database" instead of "persistent data store"). Design decisions are prematurely tied to implementation.

## Section-by-Section Guidance

### Overview

**Purpose:** Orient readers to the system and architecture document scope.

**Tips:**
- Start with the system's primary value proposition (why it exists)
- Define scope boundaries clearly (what's in, what's out)
- Mention who should read this document and what they'll learn
- Keep to 1-3 paragraphs—this is an orientation, not the full story

**Anti-patterns:**

- ❌ Diving into technical details before establishing context

**Preferred:**

- ✅ Start with stakeholder value, then narrow to technical scope

### V-Model Summary Table

**Purpose:** Provide at-a-glance understanding of the full architecture lifecycle.

**Tips:**
- Fill in all cells before detailing individual layers
- Use the "current status" column to show where you are in the lifecycle
- Ensure consistency—descriptions in the table should match section content
- The table is a navigation aid; readers should be able to jump to relevant sections

**Anti-patterns:**

- ❌ Leaving cells empty or writing "TBD"

**Preferred:**

- ✅ Write brief but substantive content for each cell, even if sections need more work

### Conceptual Layer

**Purpose:** Establish why the system exists and for whom.

**Tips:**
- Write problem statements from stakeholder perspective, not system perspective
- Include 3-5 distinct stakeholder needs, not variations of the same need
- Acceptance criteria should be observable/measurable outcomes
- Consider: "If this system succeeds, what will be different for stakeholders?"

**Anti-patterns:**

- ❌ "The system needs to be fast" (vague, not stakeholder-focused)

**Preferred:**

- ✅ "Engineers need to verify documents in under 10 seconds to maintain workflow efficiency"

### Functional Layer

**Purpose:** Define what the system must do to meet conceptual needs.

**Tips:**
- Each function should trace to at least one conceptual need
- Use input/output thinking: what goes in, what comes out, what transforms?
- Functions should be testable at the system level
- Consider both happy path and error handling functions

**Anti-patterns:**

- ❌ Functions that describe implementation ("Parse YAML files")

**Preferred:**

- ✅ Functions that describe behavior ("Verify document structure against specification")

### Logical Layer

**Purpose:** Define components and their interactions without implementation bias.

**Tips:**
- Name components by responsibility, not technology ("Validation Service" not "Python Script")
- Define interfaces in terms of what information flows, not how
- Components should have single, clear responsibilities
- This layer should survive technology changes

**Anti-patterns:**

- ❌ "GitHub Actions CI Pipeline" (implementation-specific)

**Preferred:**

- ✅ "Continuous Verification Service" (responsibility-focused)

### Physical Layer

**Purpose:** Document specific implementation choices and their rationale.

**Tips:**
- Be specific: name actual tools, languages, frameworks
- Explain why each choice was made (not just what)
- Include version information where relevant
- This layer is expected to change; document current state clearly

**Anti-patterns:**

- ❌ "Modern web framework" (too vague for physical layer)

**Preferred:**

- ✅ "Python 3.11 with PyYAML for YAML parsing, pytest for unit testing"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Start with Conceptual** (30 min)
   - Identify stakeholders and their needs first
   - Draft acceptance criteria that would prove success
   - This grounds all subsequent work

2. **Derive Functions** (30 min)
   - For each need, ask: "What must the system do to meet this?"
   - Define system-level test scenarios
   - Ensure coverage of all conceptual needs

3. **Design Components** (45 min)
   - Group functions into cohesive components
   - Define interfaces between components
   - Stay technology-agnostic

4. **Specify Implementation** (30 min)
   - Choose technologies for each component
   - Document rationale for choices
   - Define unit test approach

5. **Complete V-Model Table** (15 min)
   - Summarize each layer in table format
   - Verify bidirectional traceability
   - Mark current lifecycle position

### Quality Checkpoints

- **After Conceptual:** Do stakeholder needs feel genuine and distinct?
- **After Functional:** Can each function be traced to a need?
- **After Logical:** Could this be implemented with different technologies?
- **After Physical:** Are all logical components covered by implementations?
- **Final:** Does the V-model table accurately summarize all sections?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Thin Conceptual Layer | Architecture lacks grounding in real needs | Interview stakeholders or role-play stakeholder perspectives |
| Technology Leakage in Logical | Logical layer prematurely constrains implementation | Rename components to responsibilities; remove tool names |
| Untraceable Elements | Physical elements don't connect to needs | Create explicit traceability matrix; eliminate orphans |
| Vague Test Criteria | "System should work correctly" | Define specific, measurable success conditions |
| Missing V-Model Balance | Design side complete, testing side sparse | Write test criteria before considering them "done" |
| Scope Creep | Architecture covers too much | Revisit Overview and explicitly state what's out of scope |

## Best Practices

1. **Start with the end in mind**: Write acceptance criteria before designing the system
2. **Maintain bidirectional traceability**: Every element should trace up (to needs) and down (to tests)
3. **Separate concerns across layers**: Don't leak implementation into logical, or functions into conceptual
4. **Test your layer independence**: Ask "could this logical design be implemented differently?"
5. **Use the V-model table as a living summary**: Update it as sections evolve
6. **Review with stakeholders**: Validate conceptual layer with actual stakeholders if possible
7. **Document rationale, not just decisions**: Explain why, especially in physical layer
8. **Treat the logical layer as the stable core**: It should change least frequently
9. **Version the document**: Architecture evolves; track changes through semantic versioning
10. **Self-validate**: Architecture documents about architecture frameworks should demonstrate their own principles

## Validation vs. Verification

**Verification** (deterministic checks against spec-for-architecture):
- All required sections present
- V-model table has all four layers
- Each layer has required subsections
- Minimum element counts met
- Frontmatter fields correctly typed

**Validation** (qualitative assessment against this guidance):
- Layer Completeness: Is each layer substantively developed?
- V-Model Alignment: Do design and testing sides balance?
- Traceability: Can elements be traced across layers?
- Testability: Are test criteria specific and measurable?
- Stakeholder Clarity: Does conceptual layer reflect real needs?
- Technology Independence: Is logical layer free of implementation bias?

## Tooling Support

### Verification Commands

```bash
# Verify structure against spec
python scripts/verify_template_based.py 00_vertices/doc-architecture-<name>.md --templates templates
```

### Validation Support

Architecture document validation requires human review against the six quality criteria above. A validator should:
1. Read the complete document
2. Assess each criterion (Excellent/Good/Needs Improvement)
3. Provide specific feedback for any criterion below "Good"
4. Document assessment in a validation edge with `human_approver` field

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

✓ **Layer Completeness**: Covers all aspects of architecture document creation
✓ **V-Model Alignment**: Addresses both creation (workflow) and evaluation (criteria)
✓ **Traceability**: Quality criteria trace to section guidance and common issues
✓ **Testability**: Validation criteria are specific and assessable
✓ **Stakeholder Clarity**: Written for architecture document authors (clear audience)
✓ **Technology Independence**: Advice is framework-agnostic (applicable to any tooling)

---

**Note:** This guidance pairs with `spec-for-architecture.md` via a coupling edge. The spec defines structure; this guidance defines quality.
