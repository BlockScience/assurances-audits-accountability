# Module 07: Reference & Reuse

**Learning Journey: Knowledge Complexes**
**Module:** 07 of 07
**Skill Developed:** Reference & Reuse (Doc-Kit Patterns)

## Learning Goals

By the end of this module, you will be able to:

1. Extend assurance faces into doc-kits with usage documentation
2. Create doc-kit pattern libraries for systematic document creation
3. Build a registry chart cataloging reusable patterns
4. Use doc-kits to systematically create new documents
5. Understand how reference materials connect to the boundary complex
6. Establish living documentation that evolves with the knowledge complex

## Prerequisites

Before starting this module, you should have completed:

- **Module 05:** Assurance & Audits
- **Skills Required:** Creating assurance faces, running assurance audits

You should be familiar with:
- The assurance triangle (verification + validation + coupling)
- Running `audit_assurance_chart.py` and interpreting results
- Tracing assurance paths to the boundary complex
- Human accountability in assurance workflows

**Note:** Unlike Module 06, this module does NOT require Module 03 (composition). You only need assurance skills.

## Module Roadmap

This module extends assurance from "proving quality" to "enabling reuse."

In Module 05, you learned to create assurance faces that attest to document quality. Now we'll extend those faces with **usage documentation** that explains HOW to create similar documents.

We'll learn to:
1. Transform assurance faces into doc-kits
2. Build a library of pattern doc-kits
3. Create a registry chart connecting patterns to the boundary complex
4. Use doc-kits as guides for systematic document creation

---

## Section 1: From Assurance to Doc-Kits

**Time:** 60 minutes

### The Assurance Limitation

An assurance face proves a document is trustworthy. It answers:
- "Does this document meet structural requirements?" (verification)
- "Is this document fit for purpose?" (validation)
- "Who attests to its quality?" (accountability)

But it doesn't answer:
- "How do I create another document like this?"
- "What patterns should I follow?"
- "What are common mistakes to avoid?"
- "What examples can guide me?"

### What is a Doc-Kit?

A **doc-kit** extends an assurance face with usage documentation:

```
ASSURANCE FACE (proves quality)
├── Verification results
├── Validation assessment
├── Triangle coherence review
└── Accountability statement

DOC-KIT (extends assurance with usage)
├── [Everything from assurance face]
├── Usage Guide
│   ├── When to use this pattern
│   ├── Prerequisites
│   └── Expected outcomes
├── Step-by-Step Process
│   ├── Preparation steps
│   ├── Creation workflow
│   └── Verification checklist
├── Common Patterns
│   ├── Typical structures
│   └── Example snippets
├── Anti-Patterns
│   ├── Common mistakes
│   └── How to avoid them
└── Related Doc-Kits
    └── Links to complementary patterns
```

### Doc-Kit = Assurance + Guidance for Creation

Think of a doc-kit as a "kit" for creating new documents:
- **Assurance**: Proves the exemplar document is trustworthy
- **Usage Guide**: Explains when and why to use this pattern
- **Process**: Step-by-step instructions for creating similar documents
- **Patterns/Anti-Patterns**: What to do and what to avoid
- **Examples**: Concrete guidance from the assured document

### Exercise 1.1: Examine an Assurance Face

**Task:** Read an assurance face and identify what's missing for reuse.

```bash
# Read an assurance face
cat 02_faces/assurance-spec-guidance.md
```

**Questions:**
1. What does this assurance face prove?
2. If you wanted to create a similar spec document, what guidance is missing?
3. What questions would you have about the creation process?
4. How would step-by-step instructions help?

---

## Section 2: Creating Doc-Kits

**Time:** 90 minutes

### Doc-Kit Structure

A doc-kit extends the assurance face template with additional sections:

```yaml
---
type: face/doc-kit
extends: face/assurance
id: dk:spec-guidance
# ... all assurance face fields ...
---

# Doc-Kit - Spec for Guidance

## [Standard Assurance Sections]

[Face Structure, Assurance Triangle, Triangle Coherence Review, etc.]

## Usage Guide

### When to Use This Pattern

[Description of when this doc-kit pattern is appropriate]

### Prerequisites

[What you need before using this pattern]

### Expected Outcomes

[What you'll have after successfully using this pattern]

## Step-by-Step Process

### Step 1: Preparation

[Preparation activities]

### Step 2: Creation

[Document creation workflow]

### Step 3: Verification

[How to verify your work]

### Step 4: Validation

[How to validate your work]

### Step 5: Assurance

[How to create your own assurance face]

## Common Patterns

### Typical Structure

[Common structural patterns from the exemplar]

### Example Snippets

[Code/content snippets that demonstrate patterns]

## Anti-Patterns

### Common Mistakes

[Things to avoid]

### How to Avoid Them

[Guidance for avoiding mistakes]

## Related Doc-Kits

[Links to complementary patterns]
```

### Building on Existing Assurance

To create a doc-kit:

1. **Start with the assurance face** for the exemplar document
2. **Keep all assurance content** - this proves the pattern is trustworthy
3. **Add usage sections** explaining how to replicate the pattern
4. **Extract patterns** from the exemplar document
5. **Document anti-patterns** from validation experience
6. **Link to related doc-kits** for complementary patterns

### The Five Foundational Doc-Kits

The boundary complex defines 5 foundational doc-kit domains:

| Doc-Kit | Exemplar | Creates |
|---------|----------|---------|
| `dk:spec-spec` | spec-for-spec | New spec documents |
| `dk:spec-guidance` | spec-for-guidance | Spec documents for new domains |
| `dk:guidance-spec` | guidance-for-spec | Guidance documents for specs |
| `dk:guidance-guidance` | guidance-for-guidance | New guidance documents |
| `dk:spec-guidance-pair` | coupling-spec | Coupled spec-guidance pairs |

These five doc-kits form the **foundation** for creating all other documentation.

### Exercise 2.1: Sketch a Doc-Kit

**Task:** Sketch the usage sections for a spec doc-kit.

**Document to extend:** `02_faces/assurance-spec-guidance.md`

**Write (on paper or in a file):**
1. **When to Use This Pattern**: When would someone create a spec for a guidance domain?
2. **Prerequisites**: What do they need before starting?
3. **Step 1-5**: Brief outline of the creation process
4. **Common Patterns**: What structural patterns appear in spec-for-guidance?
5. **Common Mistakes**: What errors might someone make?

---

## Section 3: The Doc-Kit Registry

**Time:** 75 minutes

### What is a Registry?

A **registry** is a chart that catalogs all available doc-kits and their relationships to the boundary complex.

**Structure:**
```
Registry Chart
├── Boundary Complex (foundation)
│   ├── b0:root
│   ├── v:spec:spec (SS)
│   ├── v:spec:guidance (SG)
│   ├── v:guidance:spec (GS)
│   └── v:guidance:guidance (GG)
├── Doc-Kit Vertices
│   ├── dk:spec-spec
│   ├── dk:spec-guidance
│   ├── dk:guidance-spec
│   ├── dk:guidance-guidance
│   └── dk:spec-guidance-pair
└── Usage Edges
    └── dk:* → boundary complex vertices
```

### Registry Purpose

The registry serves multiple purposes:

1. **Discovery**: Find available doc-kits for your needs
2. **Traceability**: Every doc-kit traces to boundary complex
3. **Completeness**: Identify gaps in doc-kit coverage
4. **Navigation**: Find related and complementary patterns

### Registry-Boundary Connection

Every doc-kit connects to the boundary complex through its exemplar:

```
dk:spec-guidance
  └── exemplar → v:spec:guidance
      └── assurance → f:assurance:spec-guidance
          └── trace → b2:guidance-guidance, b2:spec-spec
              └── anchor → b0:root
```

This means:
- The doc-kit is trustworthy (its exemplar is assured)
- The pattern is grounded (traces to root)
- The guidance is authoritative (comes from boundary complex)

### Registry as Living Document

The registry evolves as new doc-kits are created:

1. **New domain** → Create spec-guidance pair → Add to registry
2. **New pattern** → Create doc-kit for pattern → Add to registry
3. **Improved process** → Update doc-kit → Registry reflects changes

### Exercise 3.1: Design Registry Structure

**Task:** Sketch a registry chart for the five foundational doc-kits.

**Elements to include:**
1. Boundary complex vertices (5)
2. Doc-kit vertices (5)
3. Edges connecting doc-kits to their exemplars
4. Edges connecting to boundary assurance faces

**Questions:**
1. How many vertices in your registry?
2. How many edges connect doc-kits to boundary complex?
3. Does every doc-kit trace to root?
4. What is the Euler characteristic?

---

## Section 4: Using Doc-Kits

**Time:** 60 minutes

### The Doc-Kit Workflow

When creating a new document using a doc-kit:

**1. Select the Right Doc-Kit**
- What type of document are you creating?
- Which doc-kit matches that type?
- Review the "When to Use" section

**2. Check Prerequisites**
- Do you have all required inputs?
- Are prerequisite documents assured?
- Do you have necessary tools?

**3. Follow the Process**
- Work through Step 1-5 in order
- Don't skip verification or validation
- Use the exemplar as your model

**4. Apply Patterns**
- Use common patterns from the doc-kit
- Copy structure from the exemplar
- Adapt examples to your context

**5. Avoid Anti-Patterns**
- Review common mistakes before starting
- Check your work against anti-patterns
- Fix issues before proceeding

**6. Create Your Own Assurance**
- Verify your document
- Validate your document
- Create assurance face
- Get human approval

### Example: Using dk:spec-guidance

Let's trace through creating a new spec using the spec-for-guidance doc-kit:

**Scenario:** Creating `spec-for-persona`

**Step 1: Check Prerequisites**
- Guidance exists: `guidance-for-spec` (for validating specs)
- Coupling exists: `coupling-spec` (SS↔GS pair)
- Tools available: `verify_template_based.py`

**Step 2: Review Exemplar**
- Read `spec-for-guidance` carefully
- Note the structure: frontmatter schema, body structure, validation rules, examples
- Identify what changes for persona domain

**Step 3: Create Document**
- Copy structure from exemplar
- Adapt frontmatter for persona
- Write persona-specific requirements
- Add persona-specific examples

**Step 4: Verify**
```bash
python scripts/verify_template_based.py 00_vertices/spec-for-persona.md --templates templates
```

**Step 5: Validate**
- LLM-assisted validation against guidance-for-spec
- Human review and approval

**Step 6: Assure**
- Create assurance face for spec-for-persona
- Link verification, validation, coupling edges
- Human signs accountability

### Exercise 4.1: Trace a Doc-Kit Usage

**Task:** Document how you would use dk:guidance-spec to create a new guidance document.

**Scenario:** Creating `guidance-for-persona`

**Write:**
1. What prerequisites do you need?
2. What exemplar will you study?
3. What structure will you follow?
4. How will you verify?
5. How will you validate?
6. What assurance face will you create?

---

## Section 5: Living Documentation

**Time:** 45 minutes

### Doc-Kits as Living Documentation

Doc-kits are **living documentation** - they evolve as the knowledge complex grows:

1. **New patterns discovered** → Add to doc-kit
2. **New anti-patterns identified** → Add warnings
3. **Better examples found** → Update examples
4. **Process improvements** → Update steps

### Maintaining Doc-Kits

When you learn something new:

1. **Update the relevant doc-kit** with new knowledge
2. **Re-verify** the doc-kit passes template checks
3. **Note the change** in modification history
4. **Update related doc-kits** if necessary

### Doc-Kit Versioning

Doc-kits should be versioned:

```yaml
---
type: face/doc-kit
version: 1.2.0
changelog:
  - "1.2.0: Added anti-pattern for missing validation"
  - "1.1.0: Added step-by-step process"
  - "1.0.0: Initial doc-kit creation"
---
```

### Exercise 5.1: Plan a Doc-Kit Update

**Task:** Plan how you would update a doc-kit after learning a new pattern.

**Scenario:** You discovered that specs often fail validation because they lack sufficient examples.

**Write:**
1. Which doc-kit would you update?
2. What section would you add or modify?
3. What anti-pattern would you document?
4. How would you version this change?

---

## Summary

### Key Takeaways

1. **Doc-Kits Extend Assurance**
   - Assurance proves quality; doc-kits enable reuse
   - Doc-kit = assurance face + usage documentation
   - Every doc-kit is grounded in an assured exemplar

2. **Foundational Doc-Kits**
   - Five doc-kits from boundary complex
   - SS, SG, GS, GG, and spec-guidance-pair
   - Foundation for all other documentation

3. **Registry Catalogs Patterns**
   - Central chart of available doc-kits
   - Every doc-kit traces to boundary complex
   - Living document that grows with the system

4. **Systematic Creation Workflow**
   - Select doc-kit → Check prerequisites → Follow process
   - Apply patterns → Avoid anti-patterns → Create assurance
   - Consistent quality through systematic approach

5. **Living Documentation**
   - Doc-kits evolve with new knowledge
   - Update when patterns or anti-patterns are discovered
   - Version changes for traceability

### Skill Checklist

You should now be able to:

- Extend assurance faces into doc-kits with usage documentation
- Create doc-kit pattern libraries for systematic reuse
- Design registry charts connecting patterns to boundary complex
- Use doc-kits to systematically create new documents
- Maintain doc-kits as living documentation
- Version doc-kit changes appropriately

### Convergence with Module 06

If you've completed both Module 06 AND Module 07:

**Combined Skills:**
- Compositional document design (Module 06)
- Doc-kit pattern reuse (Module 07)

**Together These Enable:**
- Create compositional documents using doc-kit patterns
- Assure both components and compositions
- Build reusable pattern libraries for compositional architectures
- Systematic quality at all levels

**Total Skills:** 7 (fundamentals, types, composition, verification-validation, assurance, document-composition, reference-reuse)

---

## Assessment

### Final Exercise: Create a Simple Doc-Kit

**Task:** Create a doc-kit extending an existing assurance face.

**Requirements:**

1. **Select an Assurance Face** (10 points)
   - Choose any existing assurance face from `02_faces/`
   - The exemplar document should be well-suited for creating a pattern

2. **Create Doc-Kit Document** (50 points)
   - Copy the assurance face content
   - Add Usage Guide section (when to use, prerequisites, outcomes)
   - Add Step-by-Step Process (at least 4 steps)
   - Add Common Patterns section (at least 2 patterns)
   - Add Anti-Patterns section (at least 2 anti-patterns)
   - Add Related Doc-Kits section

3. **Verify Doc-Kit** (15 points)
   - Run template verification on your doc-kit
   - Ensure all required sections are present
   - Fix any structural issues

4. **Document the Pattern** (25 points)
   - Write a summary (200-300 words) explaining:
     - What document type does this doc-kit help create?
     - What is the key pattern from the exemplar?
     - What is the most important anti-pattern to avoid?
     - How does this doc-kit connect to the boundary complex?

**Deliverables:**
- Doc-kit file in `02_faces/` (e.g., `dk-spec-persona.md`)
- Summary write-up (can be in the doc-kit or separate file)

**Success Criteria:**
- Doc-kit includes all required sections
- Passes template verification
- Patterns are concrete and actionable
- Anti-patterns warn about real mistakes
- Trace to boundary complex is clear

---

## Additional Resources

### Templates

**Doc-Kit Template:** `templates/02_faces/doc-kit.md`

Extends the assurance template with:
- Usage Guide section
- Step-by-Step Process section
- Common Patterns section
- Anti-Patterns section
- Related Doc-Kits section

### Example Files to Study

**Assurance Faces (base for doc-kits):**
- `02_faces/assurance-spec-guidance.md` - SG assurance
- `02_faces/assurance-guidance-spec.md` - GS assurance
- `02_faces/assurance-spec-spec.md` - SS assurance (boundary)
- `02_faces/assurance-guidance-guidance.md` - GG assurance (boundary)

**Boundary Complex:**
- `charts/boundary-complex/boundary-complex.md` - Foundation structure
- `00_vertices/b0-root.md` - The root anchor

### Key Concepts for Review

1. **Doc-Kit**: Assurance face extended with usage documentation
2. **Exemplar**: The assured document that a doc-kit is based on
3. **Registry**: Chart cataloging available doc-kits
4. **Living Documentation**: Documents that evolve with the system
5. **Foundational Doc-Kits**: Five doc-kits from boundary complex
6. **Pattern**: Reusable structure or approach from an exemplar
7. **Anti-Pattern**: Common mistake to avoid

### Relationship to Other Modules

| Module | Skill | Relationship |
|--------|-------|-------------|
| 01 | Fundamentals | Basic structures for doc-kit elements |
| 02 | Types | Typed doc-kits (face/doc-kit) |
| 03 | Composition | Optional - enables compositional doc-kits |
| 04 | Verification | Verification in doc-kit process |
| 05 | Assurance | Foundation that doc-kits extend |
| 06 | Composition | Parallel path - both lead to document-architect |
| 07 | Reference | THIS MODULE |

### Learning Journey Completion

**Congratulations!** You have completed the Learning Journey for Knowledge Complexes.

**Skills Acquired (via Module 07 path):**
1. Simplicial Complex Fundamentals (Module 01)
2. Typed Simplicial Complexes (Module 02)
3. Verification & Validation (Module 04)
4. Assurance & Audits (Module 05)
5. Reference & Reuse (Module 07)

**Optional Additional Skill (via Module 06):**
6. Composing Typed Simplicial Complexes (Module 03)
7. Document Composition (Module 06)

**Terminal State:** Document Architect - equipped to design, create, verify, validate, assure, and systematically reuse documentation within knowledge complex frameworks.

---

**Module 07 Complete**

You've learned how to extend assurance faces into doc-kits, create pattern libraries for systematic reuse, build registry charts, and use doc-kits as living documentation for ongoing quality.

**Learning Journey Complete!**
