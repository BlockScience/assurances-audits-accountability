---
type: vertex/guidance
extends: doc
id: v:guidance:skill
name: Guidance for Skill Documents
description: Quality criteria and best practices for creating excellent skill documents defining learnable capabilities possessed by actors and required by learning modules
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies:
  - v:guidance:property
---

# Guidance for Skill Documents

**This guidance defines quality criteria and best practices for creating excellent skill documents.**

## Purpose

While [[spec-for-skill]] defines what structural elements must be present, this guidance helps authors assess **how well** a skill document establishes learnable capabilities with clear outcomes, appropriate prerequisites, and meaningful progression paths. Great skills understand the property reference/referent distinction while adding learning-specific rigor.

## Inheritance

This guidance **extends** [[guidance-for-property]] (v:guidance:property).

All quality criteria from guidance-for-property apply, PLUS the additional criteria defined here for learning-specific sections.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating skill documents by providing:
- Quality assessment criteria for skills (inheriting from property guidance)
- Best practices for defining learning outcomes, prerequisites, and progression
- Guidance on skill granularity and dependency chains
- Understanding skills as both referents (abstract) and learning objectives (concrete goals)
- Common pitfalls and solutions
- Section-by-section authoring advice for learning-specific sections
- Workflow recommendations for skill creation

### Best Use Cases

Use this guidance when:
- Creating a new skill for an educational syllabus or learning path
- Reviewing an existing skill for learning coherence
- Teaching others how to model learnable capabilities
- Evaluating whether a skill's outcomes are observable and assessable
- Designing skill dependency chains for curriculum development

## Quality Criteria (Skill-Specific)

These criteria are IN ADDITION to those inherited from guidance-for-property.

### 1. Learning Outcome Observability

**Excellent:**
- Outcomes are clearly observable or measurable
- Each outcome uses action verbs (explain, implement, analyze, create)
- Outcomes follow pedagogical frameworks (e.g., Bloom's taxonomy)
- At least 2 distinct, meaningful outcomes listed
- Easy to assess whether outcomes are achieved

**Good:**
- Outcomes are mostly observable
- Action verbs used
- Generally measurable
- 2+ outcomes listed

**Needs Improvement:**
- Outcomes are vague or abstract
- Non-action verbs ("understand", "know" without specifics)
- Fewer than 2 outcomes
- No clear way to assess achievement
- Outcomes not actually learnable

### 2. Prerequisite Skill Coherence

**Excellent:**
- Prerequisites are clearly listed (or explicitly "none" for foundational skills)
- Each prerequisite is justified (explains why needed)
- Prerequisites reference actual skill vertex documents
- No circular dependencies (skill A requires skill B requires skill A)
- Dependency chain is logical and achievable

**Good:**
- Prerequisites are listed
- Generally logical
- Some references to skill specs
- No obvious circular dependencies

**Needs Improvement:**
- Prerequisites unclear or unjustified
- Circular dependencies present
- Prerequisites don't actually enable this skill
- Missing critical prerequisites
- Every skill claiming to need this skill (over-specified)

### 3. Progression Path Clarity

**Excellent:**
- "Enables" section shows clear progression path
- Lists at least 1 meaningful next step (module, skill, capability)
- Progression is logical and motivated
- Easy to see how this skill fits in larger learning journey
- Connects to actual learning modules or advanced skills

**Good:**
- Progression path is present
- Shows some next steps
- Generally logical

**Needs Improvement:**
- No progression path shown
- "Enables" section is vague or empty
- No connection to learning modules
- Unclear how skill fits in larger context

### 4. Granularity Appropriateness

**Excellent:**
- Skill granularity matches domain and context
- Not too broad (impossibly large scope)
- Not too narrow (trivial or atomic)
- Right size for assessment and learning modules
- Appropriate for target learner level

**Good:**
- Granularity is reasonable
- Generally appropriate scope
- Usable in practice

**Needs Improvement:**
- Too broad ("master all of computer science")
- Too narrow ("know the syntax of one Python operator")
- Granularity doesn't match assessment capability
- Multiple unrelated outcomes (should be separate skills)

### 5. Assessment Feasibility

**Excellent:**
- Clear methods for assessing skill possession
- Assessment aligns with learning outcomes
- Multiple assessment methods suggested
- Assessment is realistic and achievable
- Methods are observable or demonstrable

**Good:**
- Assessment methods are present
- Generally aligned with outcomes
- Realistic methods

**Needs Improvement:**
- No assessment methods specified
- Assessment doesn't match outcomes
- Unrealistic or impossible to assess
- Only subjective assessment ("I feel like I know it")

### 6. Domain Specificity

**Excellent:**
- Skill is clearly scoped to a knowledge domain
- Domain field is specified and appropriate
- Skill level is indicated (beginner, intermediate, advanced)
- Terminology matches domain conventions
- Fits naturally in domain's learning progression

**Good:**
- Domain is specified
- Generally appropriate scope
- Some level indication

**Needs Improvement:**
- Domain unclear or missing
- Skill spans multiple unrelated domains
- No level indication
- Doesn't fit domain context

## Section-by-Section Guidance (Learning-Specific)

These sections are SPECIFIC to skill, in addition to inherited property sections.

### Learning Outcomes

**Purpose:** Define observable indicators that demonstrate skill possession

**Tips:**
- Use action verbs from Bloom's taxonomy:
  - **Remember:** List, recall, identify, define
  - **Understand:** Explain, describe, summarize, interpret
  - **Apply:** Implement, use, execute, solve
  - **Analyze:** Compare, examine, differentiate, organize
  - **Evaluate:** Assess, critique, judge, justify
  - **Create:** Design, construct, develop, formulate
- List at least 2 distinct outcomes
- Make each outcome measurable or observable
- Ensure outcomes align with skill level

**Examples:**

**Excellent (Beginner Skill):**
```markdown
## Learning Outcomes

After acquiring this skill, a learner can:

- Identify vertices, edges, and faces in a simplicial complex diagram
- Explain the purpose of each element type in clear terms
- Calculate the Euler characteristic (χ = V - E + F) for a given complex
```

**Excellent (Advanced Skill):**
```markdown
## Learning Outcomes

After acquiring this skill, a learner can:

- Design simplicial complex structures for new domains
- Analyze topological properties to detect structural gaps
- Evaluate trade-offs between different complex architectures
```

**Needs Improvement:**
```markdown
## Learning Outcomes

- Understand simplicial complexes (vague, not observable)
- Know about vertices (not measurable)
```

### Prerequisite Skills

**Purpose:** Define what skills must be possessed before learning this skill

**Tips:**
- List prerequisites explicitly (or "None" for foundational skills)
- Reference actual skill vertex documents
- Explain WHY each prerequisite is needed
- Check for circular dependencies
- Ensure prerequisite chain is achievable

**Foundational Skill:**
```markdown
## Prerequisite Skills

None - this is a foundational skill requiring no prior knowledge.
```

**Intermediate Skill:**
```markdown
## Prerequisite Skills

- **[[v:skill:simplicial-complexes]]**: Understanding of vertices, edges, faces needed to comprehend assurance triangles
- **[[v:skill:document-verification]]**: Knowledge of verification processes needed for assurance context
```

**Circular Dependency Check:**
```
Skill A: Prerequisite = Skill B
Skill B: Prerequisite = Skill A
❌ CIRCULAR - both can't require each other!

Fix: Identify which is truly foundational
```

**Dependency Chain Check:**
```
None → Skill A → Skill B → Skill C
✅ Valid linear progression

None → Skill A → Skill B
         ↓
     Skill C
✅ Valid branching progression
```

### Enables

**Purpose:** Show what this skill enables (progression path)

**Tips:**
- List at least 1 concrete next step
- Reference learning modules that require this skill
- Reference advanced skills that build on this
- Show how skill connects to capabilities
- Make progression motivating and clear

**Examples:**

**Excellent:**
```markdown
## Enables

- **[[v:learning-module:advanced-topology]]**: Can study advanced topological analysis
- **[[v:skill:homology-theory]]**: Foundation for learning algebraic topology
- **Chart Design**: Can create custom chart types for new domains
```

**Good:**
```markdown
## Enables

- Study of advanced topics
- Creation of complex structures
```

**Needs Improvement:**
```markdown
## Enables

- More learning (too vague)
```

### Assessment Methods (Optional but Recommended)

**Purpose:** Explain how skill possession can be assessed

**Tips:**
- Provide multiple assessment methods
- Align methods with learning outcomes
- Include both formative and summative assessment
- Make methods concrete and achievable

**Examples:**

**Excellent:**
```markdown
## Assessment Methods

- **Problem-Solving Exercises**: Given a complex, calculate χ and identify holes
- **Code Review**: Implement verification functions demonstrating understanding
- **Written Explanation**: Describe the assurance triangle pattern clearly
- **Practical Application**: Create an assurance audit for a new document
```

**Good:**
```markdown
## Assessment Methods

- Complete exercises demonstrating skill
- Explain concepts to others
```

## Skill Granularity Guidance

### Choosing Appropriate Granularity

**Too Broad (Avoid):**
- "Master all of programming"
- "Expert in all knowledge complex concepts"
- "Understand everything about mathematics"

**Too Narrow (Avoid):**
- "Know the syntax of Python's += operator"
- "Understand what the letter 'V' means in χ = V - E + F"
- "Can spell 'simplicial'"

**Appropriate Granularity:**
- **Broad:** "Python programming", "Knowledge complex fundamentals"
- **Moderate:** "Simplicial complex topology", "Assurance triangle patterns"
- **Narrow:** "Euler characteristic calculation", "Verification edge creation"

**Choose granularity based on:**
- Learning context (course, workshop, self-study)
- Assessment capability (can you test it?)
- Module size (fits in learning module)
- Learner level (beginner needs narrower, advanced can handle broader)

### Domain and Level Fields

**Domain Examples:**
- `programming`, `mathematics`, `topology`, `documentation`, `knowledge-complexes`

**Level Examples:**
- `beginner` - Foundational, no prerequisites
- `intermediate` - Builds on beginner skills
- `advanced` - Requires multiple intermediate skills
- `expert` - Mastery level, extensive prerequisites

Use these fields to help learners find appropriate skills.

## Workflow Guidance

### Recommended Authoring Sequence

1. **Start with Property Sections** (see guidance-for-property) (70 minutes)
   - Complete all property-required sections first
   - Ensure property definition, acquisition, applicability are solid
   - **Checkpoint:** Does this satisfy property requirements?

2. **Define Learning Outcomes** (20 minutes)
   - List observable, measurable outcomes (2+ items)
   - Use action verbs from Bloom's taxonomy
   - Align with skill level (beginner, intermediate, advanced)
   - **Checkpoint:** Are outcomes observable and assessable?

3. **Identify Prerequisites** (15 minutes)
   - List prerequisite skills (or "None")
   - Reference skill vertex documents
   - Explain why each is needed
   - Check for circular dependencies
   - **Checkpoint:** Is prerequisite chain logical and achievable?

4. **Define Progression Path** (15 minutes)
   - List what this skill enables (1+ items)
   - Reference learning modules or advanced skills
   - Show how skill fits in learning journey
   - **Checkpoint:** Is progression path clear and motivating?

5. **Specify Assessment** (15 minutes)
   - List assessment methods
   - Align with learning outcomes
   - Ensure methods are achievable
   - **Checkpoint:** Can skill possession be assessed?

6. **Verify Granularity** (10 minutes)
   - Check skill is not too broad or too narrow
   - Verify domain and level are specified
   - Ensure fits in learning module context
   - **Checkpoint:** Is granularity appropriate?

### Total Estimated Time: 145 minutes (70 min property + 75 min skill-specific)

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Vague Outcomes | "Understand X" | Use action verbs: "Explain X", "Implement X" |
| No Prerequisites | Every skill foundational | Identify actual prerequisite dependencies |
| Circular Dependencies | A requires B requires A | Break circle, identify true foundation |
| No Progression | Skill leads nowhere | Show what modules/skills it enables |
| Too Broad | "Master all of X" | Scope to learnable, assessable chunk |
| Too Narrow | Single syntax rule | Combine related narrow skills |
| No Assessment | Can't verify possession | Define observable assessment methods |

## Best Practices

1. **Complete Property Requirements First** - Satisfy all property criteria before adding skill-specific sections
2. **Use Action Verbs for Outcomes** - Follow Bloom's taxonomy for observable outcomes
3. **Build Dependency Chains Carefully** - Avoid circular prerequisites, ensure logical progression
4. **Show Progression Path** - Explain what this skill enables (modules, skills, capabilities)
5. **Choose Appropriate Granularity** - Not too broad, not too narrow, right for context
6. **Specify Domain and Level** - Help learners find appropriate skills
7. **Define Assessment Methods** - Make skill possession verifiable
8. **Reference Actual Vertices** - Link to skill, module, and actor specs when available

## Skill Dependency Patterns

### Linear Dependency Chain

```
Skill A (foundational)
  ↓
Skill B (requires A)
  ↓
Skill C (requires B)
```

**Use when:** Skills build sequentially

### Branching Dependencies

```
Skill A (foundational)
  ↓
  ├→ Skill B (specialization 1)
  └→ Skill C (specialization 2)
```

**Use when:** Multiple paths from foundation

### Converging Dependencies

```
Skill A    Skill B
  ↓          ↓
  └→ Skill C ←┘
```

**Use when:** Advanced skill requires multiple prerequisites

### No Dependencies

```
Skill A (foundational, standalone)
```

**Use when:** True foundational skill, no prerequisites

## Validation vs. Verification

**Verification** (deterministic):
- All property requirements satisfied
- All skill-specific sections present
- Learning Outcomes lists 2+ outcomes
- Enables lists 1+ progression item
- ID format correct (v:skill:<name>)
- Tags include [vertex, property, skill]
- Dependencies include v:spec:property
- No circular prerequisite dependencies

**Validation** (qualitative):
- Satisfies all property validation criteria (from guidance-for-property)
- Learning outcome observability and measurability
- Action verbs used appropriately
- Prerequisite skill coherence and logic
- Progression path clarity and motivation
- Granularity appropriateness for context
- Assessment feasibility and alignment
- Domain specificity and level appropriateness
- Overall skill definition quality

---

**Note:** Skill extends property to represent learnable capabilities. Good skill documents inherit property abstraction while adding rigorous learning outcomes, clear prerequisites, and observable assessment methods. Skills form the currency of educational progression in syllabi.
