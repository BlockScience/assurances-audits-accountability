---
type: vertex/guidance
extends: doc
id: v:guidance:student
name: Guidance for Student Documents
description: Quality criteria and best practices for creating excellent student documents defining learners who possess skills and study modules
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies:
  - v:guidance:actor
---

# Guidance for Student Documents

**This guidance defines quality criteria and best practices for creating excellent student documents.**

## Purpose

While [[spec-for-student]] defines what structural elements must be present, this guidance helps authors assess **how well** a student document establishes clear learning context, appropriate skill prerequisites and goals, and coherent progression. Great students have realistic skill profiles and meaningful learning objectives.

## Inheritance

This guidance **extends** [[guidance-for-actor]] (v:guidance:actor).

All quality criteria from guidance-for-actor apply, PLUS the additional criteria defined here for learning-specific sections.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating student documents by providing:
- Quality assessment criteria for students (inheriting from actor guidance)
- Best practices for defining learning context, skills, and goals
- Guidance on skill coherence (prerequisites → goals)
- Common pitfalls and solutions
- Section-by-section authoring advice for learning-specific sections
- Workflow recommendations for student creation

### Best Use Cases

Use this guidance when:
- Creating a student for an educational syllabus or learning path
- Reviewing an existing student for learning coherence
- Teaching others how to model learners in knowledge complexes
- Evaluating whether a student's skill profile is realistic
- Designing generic vs. specific student instances

## Quality Criteria (Student-Specific)

These criteria are IN ADDITION to those inherited from guidance-for-actor.

### 1. Learning Context Clarity

**Excellent:**
- Learning situation is clearly described
- Goals and environment are explicit
- Easy to understand what/why the student is learning
- Context aligns with domain and purpose

**Good:**
- Learning context is stated
- Generally clear situation
- Some explanation provided

**Needs Improvement:**
- No clear learning context
- Vague about goals or environment
- Context doesn't align with domain
- Unclear why this student exists

### 2. Prerequisite Skill Coherence

**Excellent:**
- Prerequisites are clearly listed (or explicitly none for beginners)
- Each skill is relevant to learning context
- Skills reference skill vertex documents when available
- Skill levels are appropriate (not claiming too much or too little)
- Prerequisites are realistic for the student profile

**Good:**
- Prerequisites are listed
- Generally relevant
- Some references to skill specs

**Needs Improvement:**
- Prerequisites unclear or unrealistic
- Skills don't match learning context
- Claiming expert-level prerequisites for beginner context
- No explanation of what prerequisites mean

### 3. Learning Goal Appropriateness

**Excellent:**
- Learning goals are clearly specified (at least 1)
- Goals are achievable through available learning modules
- Goals represent meaningful skill progression from prerequisites
- Each goal references or describes a skill vertex
- Goals align with learning context

**Good:**
- Goals are listed
- Generally achievable
- Some progression from prerequisites

**Needs Improvement:**
- No learning goals specified
- Goals are unrealistic or unachievable
- No connection to prerequisites (huge gaps or no progression)
- Goals don't match learning context

### 4. Skill Progression Coherence

**Excellent:**
- Clear progression from prerequisites → goals
- Logical skill dependency chain
- Reasonable learning curve (not too steep, not trivial)
- Goals build on prerequisites in sensible way

**Good:**
- Some progression evident
- Generally logical dependencies
- Reasonable learning curve

**Needs Improvement:**
- No clear progression (goals unrelated to prerequisites)
- Unrealistic jumps (beginner prerequisites → expert goals)
- Trivial progression (goals same as prerequisites)
- Circular dependencies

### 5. Generic vs. Specific Balance

**Excellent:**
- If generic student: Clearly represents "the learner" for syllabus
- If specific student: Provides concrete, believable learner profile
- Purpose is clear (template vs. instance)
- Appropriate level of detail for purpose

**Good:**
- Purpose is generally clear
- Appropriate detail level
- Usable for intended purpose

**Needs Improvement:**
- Unclear if generic or specific
- Too detailed for generic student
- Too vague for specific student
- Purpose doesn't match detail level

## Section-by-Section Guidance (Learning-Specific)

These sections are SPECIFIC to student, in addition to inherited actor sections.

### Learning Context

**Purpose:** Describe the learning situation and environment

**Tips:**
- Be specific about what the student is trying to learn
- Explain the educational setting or context
- Clarify the student's motivation or goals
- Make it clear why this student is engaging in learning

**Examples:**
- ✅ "Generic learner for knowledge complex syllabi, starting with basic concepts"
- ✅ "Software engineer learning testing practices to improve code quality"
- ❌ "Someone who learns" (too vague)

**Generic vs. Specific:**
- **Generic:** "Learner engaging with knowledge complex educational materials"
- **Specific:** "Alice, a researcher learning knowledge complexes for documentation projects"

### Prerequisite Skills

**Purpose:** Define what skills the student already possesses (input state)

**Tips:**
- List skills explicitly (or explicitly state "none" for absolute beginners)
- Reference skill vertex documents when available
- Explain skill level or proficiency
- Ensure prerequisites are realistic for the learning context

**Beginner Student:**
```markdown
## Prerequisite Skills

None - this student is a complete beginner with no prior knowledge.
```

**Intermediate Student:**
```markdown
## Prerequisite Skills

- **[[v:skill:python-basics]]**: Basic Python programming (variables, functions, loops)
- **[[v:skill:git-fundamentals]]**: Git version control fundamentals
```

**Anti-patterns:**
- ❌ Claiming expert prerequisites for beginner context
- ❌ Vague skills without definition
- ✅ Clear, specific, achievable prerequisites

### Learning Goals

**Purpose:** Define what skills the student aims to acquire (output state)

**Tips:**
- List at least 1 concrete learning goal
- Goals should be achievable through learning modules
- Reference skill vertex documents when possible
- Show progression from prerequisites
- Make goals measurable or observable

**Examples:**
- ✅ "**[[v:skill:simplicial-complexes]]**: Understand vertices, edges, faces, Euler characteristic"
- ✅ "**[[v:skill:assurance-patterns]]**: Apply verification-validation-assurance triangles"
- ❌ "Learn stuff" (not specific)
- ❌ "Become expert in everything" (unrealistic)

**Progression Check:**
```
Prerequisites: Python basics, Git fundamentals
↓
Learning Goals: Test-driven development, CI/CD pipelines
✅ Logical progression (builds on prerequisites)

Prerequisites: None
↓
Learning Goals: Expert-level distributed systems design
❌ Unrealistic jump
```

### Current Progress (Optional)

**Purpose:** Track what modules the student has completed or is studying

**Tips:**
- Only include if tracking actual progress (not for generic students)
- Organize by status: completed, in progress, planned
- Reference actual learning module vertices
- Keep updated as student progresses

**When to Include:**
- Specific student instances tracking real progress
- Demonstration or example students showing progression
- Case studies of learning paths

**When to Omit:**
- Generic "the learner" students for syllabi
- Template students
- Students representing capability, not progress

## Workflow Guidance

### Recommended Authoring Sequence

1. **Start with Actor Sections** (see guidance-for-actor) (60 minutes)
   - Complete all actor-required sections first
   - Ensure actor identity, capabilities, properties are solid
   - **Checkpoint:** Does this satisfy actor requirements?

2. **Define Learning Context** (15 minutes)
   - Describe the learning situation
   - Explain what/why student is learning
   - Set appropriate level (beginner, intermediate, advanced)
   - **Checkpoint:** Is the learning context clear and realistic?

3. **Identify Prerequisites** (20 minutes)
   - List existing skills (or none)
   - Reference skill vertex documents
   - Ensure prerequisites match context
   - **Checkpoint:** Are prerequisites realistic for this student?

4. **Define Learning Goals** (20 minutes)
   - List target skills (at least 1)
   - Ensure goals build on prerequisites
   - Reference skill vertex documents
   - Check goals are achievable
   - **Checkpoint:** Do goals show logical progression?

5. **Verify Coherence** (10 minutes)
   - Check prerequisites → goals progression
   - Ensure context aligns with skills
   - Verify all sections support each other
   - **Checkpoint:** Is the overall student profile coherent?

### Total Estimated Time: 125 minutes (65 min actor + 60 min student-specific)

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Vague Context | "A student" | Be specific: "Learner for knowledge complex syllabi" |
| Unrealistic Prerequisites | Expert skills for beginner | Match prerequisites to learning context |
| No Learning Goals | Missing skill targets | List at least 1 specific, achievable goal |
| No Progression | Goals unrelated to prerequisites | Ensure logical skill progression |
| Too Specific for Generic | Generic student with personal history | Keep generic students abstract |
| Too Generic for Specific | Specific student with no details | Add concrete details for specific instances |

## Best Practices

1. **Complete Actor Requirements First** - Satisfy all actor criteria before adding student-specific sections
2. **Be Clear About Context** - Explicitly state the learning situation and environment
3. **List Prerequisites Explicitly** - Even if "none", say it clearly
4. **Show Skill Progression** - Goals should build logically on prerequisites
5. **Reference Skill Specs** - Link to actual skill vertex documents when available
6. **Match Detail to Purpose** - Generic students stay abstract, specific students get concrete
7. **Keep Realistic** - Prerequisites and goals should be achievable and coherent

## Generic vs. Specific Students

### Generic Student (For Syllabi)

**Purpose:** Represents "the learner" for a learning path

**Characteristics:**
- Abstract identity ("learner", "student")
- No personal details or history
- Prerequisites represent target audience
- Goals represent learning path outcomes
- Reusable across multiple learners

**Example:**
```yaml
id: v:student:knowledge-complex-learner
name: Knowledge Complex Learner
# Generic student for knowledge complex syllabi
```

### Specific Student (For Examples/Demos)

**Purpose:** Concrete learner instance for demonstrations

**Characteristics:**
- Specific identity (name, background)
- Personal context and motivation
- Actual skill profile
- Concrete learning goals
- Progress tracking (optional)

**Example:**
```yaml
id: v:student:alice-researcher
name: Alice - Research Documentation Student
# Researcher learning knowledge complexes for documentation
```

## Validation vs. Verification

**Verification** (deterministic):
- All actor requirements satisfied
- All student-specific sections present
- Learning Goals lists 1+ goal
- ID format correct (v:student:<name>)
- Tags include [vertex, actor, student]
- Dependencies include v:spec:actor

**Validation** (qualitative):
- Satisfies all actor validation criteria (from guidance-for-actor)
- Learning context clarity and appropriateness
- Prerequisite skill coherence and realism
- Learning goal appropriateness and achievability
- Skill progression logic (prerequisites → goals)
- Generic vs. specific purpose clarity
- Overall student profile coherence

---

**Note:** Student extends actor to represent learners. Good student documents inherit actor quality while adding coherent learning context and realistic skill progression from prerequisites to goals.
