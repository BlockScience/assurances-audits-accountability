---
type: vertex/guidance
extends: doc
id: v:guidance:learning-module
name: Guidance for Learning Module Documents
description: Quality criteria and best practices for creating excellent learning module documents defining effective, well-structured learning units
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies: []
---

# Guidance for Learning Module Documents

**This guidance defines quality criteria and best practices for creating excellent learning module documents.**

## Purpose

While [[spec-for-learning-module]] defines what structural elements must be present, this guidance helps authors assess **how well** a learning module creates effective, achievable learning experiences with clear objectives, appropriate scope, and meaningful assessments. Great learning modules have realistic time estimates, coherent content progression, and observable success criteria.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating learning module documents by providing:
- Quality assessment criteria for learning modules
- Best practices for defining objectives, content, and assessments
- Guidance on module scope and granularity
- Understanding modules as vertices in syllabus charts
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations for module creation

### Best Use Cases

Use this guidance when:
- Creating a new learning module for a syllabus or learning path
- Reviewing an existing module for educational effectiveness
- Teaching others how to design effective learning units
- Evaluating whether a module's scope is appropriate
- Designing prerequisite chains for curriculum development

## Quality Criteria

### 1. Learning Objective Clarity

**Excellent:**
- Objectives are concrete and observable (not vague)
- Uses action verbs from Bloom's taxonomy (explain, implement, analyze, create)
- At least 2 distinct, meaningful objectives
- Objectives are achievable within module scope and time
- Easy to assess whether objectives are met

**Good:**
- Objectives are stated clearly
- Mostly uses action verbs
- Generally measurable
- 2+ objectives listed

**Needs Improvement:**
- Objectives are vague or abstract ("understand concepts")
- Non-action verbs or passive voice
- Fewer than 2 objectives
- Objectives are too broad for module scope
- No clear way to assess achievement

### 2. Prerequisite Appropriateness

**Excellent:**
- Prerequisites are clearly listed (or explicitly "None" for foundational)
- Each prerequisite is justified (why it's needed)
- Prerequisites reference actual skill vertex documents
- No circular dependencies with other modules
- Prerequisite level matches module entry level

**Good:**
- Prerequisites are listed
- Generally logical and appropriate
- Some references to skill specs
- No obvious circular issues

**Needs Improvement:**
- Prerequisites unclear or unjustified
- Circular dependencies present (module A requires B requires A)
- Prerequisites don't actually enable module content
- Missing critical prerequisites
- Prerequisites too advanced or too basic

### 3. Content Structure Coherence

**Excellent:**
- Content flows logically from fundamentals to advanced
- Clear organization (sections, subsections, steps)
- Each section builds on previous sections
- Internal steps enumerated for progress tracking (at least 2)
- Progression supports learning objectives

**Good:**
- Content is organized
- Generally logical flow
- Some internal structure
- Supports most objectives

**Needs Improvement:**
- Disorganized or random topic order
- No clear progression
- Doesn't build concepts systematically
- No internal step enumeration
- Content doesn't align with objectives

### 4. Time Estimate Realism

**Excellent:**
- Time estimate is realistic and achievable
- Broken down by major sections or activities
- Includes study, practice, and assessment time
- Appropriate for target learner level
- Validated with actual learners when possible

**Good:**
- Time estimate provided
- Generally realistic
- Some breakdown offered
- Appropriate for level

**Needs Improvement:**
- No time estimate
- Wildly unrealistic (10 hours for basic concepts, 15 minutes for complex skills)
- No breakdown (only total given)
- Doesn't account for practice or assessment
- Doesn't match content scope

### 5. Resource Sufficiency

**Excellent:**
- Provides all resources needed to complete module
- Includes internal references (knowledge complex docs)
- Includes external references where appropriate
- Distinguishes required vs. optional resources
- Resources are accessible and current

**Good:**
- Resources are listed
- Generally sufficient
- Some internal/external mix
- Mostly accessible

**Needs Improvement:**
- No resources provided
- Resources don't support objectives
- All resources external (no use of knowledge complex)
- Resources are inaccessible or outdated
- Required vs. optional not distinguished

### 6. Success Criteria Observability

**Excellent:**
- Criteria are concrete and observable
- At least 2 success criteria listed
- Criteria align directly with learning objectives
- Students can self-assess using criteria
- Clear indicators of completion

**Good:**
- Criteria are stated
- Generally observable
- 2+ criteria listed
- Some alignment with objectives

**Needs Improvement:**
- Vague criteria ("understand the material")
- Fewer than 2 criteria
- Criteria don't match objectives
- No way to self-assess
- Subjective only ("feel confident")

### 7. Assessment Alignment

**Excellent:**
- Assessment methods directly test learning objectives
- Includes both formative (during) and summative (end) assessment
- Methods are practical and achievable
- Provides clear rubrics or standards
- Multiple assessment types (practice, exercises, explanation)

**Good:**
- Assessment methods present
- Generally align with objectives
- Some formative and summative mix
- Achievable methods

**Needs Improvement:**
- No assessment methods
- Methods don't test objectives
- Only one assessment type
- Unrealistic or impractical methods
- No standards or rubrics

### 8. Scope Appropriateness

**Excellent:**
- Module scope is focused and achievable
- Not too broad (covering too much)
- Not too narrow (trivial content)
- Right size for a learning unit
- Fits naturally in syllabus sequence

**Good:**
- Scope is reasonable
- Generally appropriate size
- Usable in practice
- Fits in sequence

**Needs Improvement:**
- Too broad (trying to teach everything)
- Too narrow (single concept that could be a section)
- Scope doesn't match time estimate
- Multiple unrelated topics (should be separate modules)
- Doesn't fit in any logical sequence

## Section-by-Section Guidance

### Overview

**Tips:**

- Write a concise abstract (2-4 sentences) summarizing the module's educational content
- Describe what topics, concepts, or skills will be covered
- Create a separate plain markdown file with the actual educational material
- Link to that file clearly so students know where to find the content
- The overview provides context; the linked file provides instruction

**Purpose of Separation:**

- **Module document (vertex):** Structure, metadata, objectives, assessments - part of the knowledge complex topology
- **Educational content (external file):** Actual learning material, explanations, examples, exercises - what students engage with

**Excellent Example:**
```markdown
## Overview

This module introduces the foundational concepts of simplicial complexes: vertices, edges, and faces. Students will learn how simplicial complexes generalize graphs and practice constructing, visualizing, and interpreting charts. The module walks learners through building and analyzing their first chart—a tetrahedron with one missing face—to understand topological holes.

**Educational Content:** [Simplicial Complex Fundamentals - Learning Material](../../learning-content/simplicial-complex-fundamentals.md)
```

**Good Example:**
```markdown
## Overview

This module covers typed simplicial complexes where vertices carry semantic type annotations. Students will analyze Module 1's chart to understand how types organize complexes beyond pure topology.

**Educational Content:** See `learning-content/typed-simplicial-complexes.md`
```

**Needs Improvement:**
```markdown
## Overview

This module is about complexes. (Too vague, no content link)
```

### Purpose

**Tips:**

- State clearly what the module teaches
- Explain why this content matters
- Indicate target learner level
- Keep concise (2-4 sentences)

**Examples:**
- ✅ "This module teaches verification patterns for knowledge complex documents, enabling students to create template-based verification edges. Students will learn to write verification criteria and interpret test results."
- ✅ "Foundational module introducing simplicial complex topology for beginners with no prior background."
- ❌ "This module teaches stuff about complexes" (too vague)

### Learning Objectives

**Tips:**
- Use Bloom's taxonomy action verbs:
  - **Remember:** List, recall, identify, define
  - **Understand:** Explain, describe, summarize, interpret
  - **Apply:** Implement, use, execute, solve
  - **Analyze:** Compare, examine, differentiate, organize
  - **Evaluate:** Assess, critique, judge, justify
  - **Create:** Design, construct, develop, formulate
- List at least 2 objectives
- Make each objective measurable
- Ensure objectives are achievable in module scope

**Excellent Example (Beginner Module):**
```markdown
## Learning Objectives

After completing this module, students will be able to:

- Identify vertices, edges, and faces in a simplicial complex diagram
- Calculate the Euler characteristic (χ = V - E + F) for a given complex
- Explain the topological significance of holes detected by χ
```

**Excellent Example (Advanced Module):**
```markdown
## Learning Objectives

After completing this module, students will be able to:

- Design custom chart types for new knowledge domains
- Evaluate trade-offs between different chart architectures
- Implement verification scripts for domain-specific constraints
```

**Needs Improvement:**
```markdown
## Learning Objectives

- Understand simplicial complexes (vague, not observable)
- Know about topology (not measurable)
```

### Prerequisite Skills

**Tips:**
- List prerequisites explicitly (or "None")
- Reference skill vertex documents
- Explain WHY each is needed
- Check for circular dependencies
- Match to module entry level

**Foundational Module:**
```markdown
## Prerequisite Skills

None - this is a foundational module requiring no prior knowledge of knowledge complexes.

**Note:** Learners will benefit from basic comfort with structured documents (markdown, YAML) and general technical literacy, but these are not hard requirements.
```

**Intermediate Module:**
```markdown
## Prerequisite Skills

- **[[v:skill:simplicial-complex-fundamentals]]**: Understanding vertices, edges, faces needed to comprehend verification patterns
- **[[v:skill:document-structure]]**: Ability to read and write markdown documents with YAML frontmatter
```

**Circular Dependency Check:**
```
Module A: Prerequisite = Skill X (gained from Module B)
Module B: Prerequisite = Skill Y (gained from Module A)
❌ CIRCULAR - learner can't start either module!

Fix: Identify which is truly foundational or split prerequisites differently
```

### Module Content

**Tips:**
- Organize into clear sections
- Show logical progression
- Enumerate internal steps (at least 2)
- Include time estimates per section if helpful
- Align with learning objectives

**Excellent Example:**
```markdown
## Module Content

### Section 1: Fundamentals (45 minutes)
1. What are simplicial complexes?
2. Why use them for knowledge?
3. Basic element types

### Section 2: Topological Properties (60 minutes)
1. Vertices (0-dimensional)
2. Edges (1-dimensional)
3. Faces (2-dimensional)
4. Euler characteristic formula

### Section 3: Practical Application (45 minutes)
1. Analyzing example charts
2. Calculating χ step-by-step
3. Interpreting topological holes
```

**Needs Improvement:**
```markdown
## Module Content

- Some stuff about topology
- Other things
- Exercises
```

### Estimated Time

**Tips:**
- Be realistic (test with actual learners if possible)
- Break down by sections or activities
- Include study + practice + assessment
- Account for target learner level
- Provide ranges if appropriate

**Excellent Example:**
```markdown
## Estimated Time

**Total:** 3-4 hours

- Section 1 (Fundamentals): 45 minutes
- Section 2 (Properties): 60 minutes
- Section 3 (Application): 45 minutes
- Practice exercises: 60 minutes
- Self-assessment: 30 minutes
```

**Needs Improvement:**
```markdown
## Estimated Time

About an hour (doesn't match complex content scope)
```

### Resources

**Tips:**
- Provide all necessary resources
- Include knowledge complex documents
- Add external references when helpful
- Distinguish required vs. optional
- Ensure accessibility

**Excellent Example:**
```markdown
## Resources

**Required:**
- [[v:spec:chart]]: Chart specification document
- Example charts: `/charts/test-tetrahedron/`
- Verification script: `scripts/verify_chart.py`

**Optional:**
- External: "Introduction to Algebraic Topology" (mathematical background)
- Tool: `visualize_chart.py` for interactive exploration
```

**Needs Improvement:**
```markdown
## Resources

- Look online for information (too vague, not actionable)
```

### Success Criteria

**Tips:**
- List at least 2 criteria
- Make criteria observable/testable
- Align with learning objectives
- Enable self-assessment
- Provide clear completion indicators

**Excellent Example:**
```markdown
## Success Criteria

Students have successfully completed this module when they can:

- Calculate χ correctly for 5 different complexes (tests objective 2)
- Identify holes by analyzing Euler characteristic (tests objective 3)
- Explain vertices, edges, faces to someone else (tests objective 1)
- Complete module exercises with 80% accuracy (overall competency)
```

**Needs Improvement:**
```markdown
## Success Criteria

- Feel like you learned something (not observable)
- Completed the reading (doesn't test objectives)
```

### Assessment Methods

**Tips:**
- Include formative (during) and summative (end)
- Align directly with objectives
- Provide practical, achievable methods
- Include multiple assessment types
- Consider self-assessment and peer assessment

**Excellent Example:**
```markdown
## Assessment Methods

**Formative (During Module):**
- Self-check questions after each section
- Practice calculations with immediate feedback
- Concept mapping exercise

**Summative (End of Module):**
- Problem set: Calculate χ for 10 complexes
- Written explanation: Describe hole detection process
- Practical analysis: Evaluate a repository chart
- Peer teaching: Explain one concept to another learner
```

**Needs Improvement:**
```markdown
## Assessment Methods

- Take a test (what does it test? when? how?)
```

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define Learning Objectives** (20 minutes)
   - What should students be able to DO after this module?
   - Use action verbs from Bloom's taxonomy
   - Keep scope manageable (2-4 objectives typically)
   - **Checkpoint:** Are objectives observable and achievable?

2. **Identify Prerequisites** (15 minutes)
   - What must students already know/do?
   - Reference skill vertices
   - Check for circular dependencies
   - **Checkpoint:** Are prerequisites necessary and sufficient?

3. **Outline Module Content** (30 minutes)
   - Plan logical progression of topics
   - Organize into sections/steps
   - Enumerate internal steps for tracking
   - Ensure content supports objectives
   - **Checkpoint:** Does content flow logically to objectives?

4. **Estimate Time** (15 minutes)
   - Be realistic about study time
   - Break down by sections
   - Include practice and assessment
   - **Checkpoint:** Does time match scope?

5. **List Resources** (15 minutes)
   - Internal knowledge complex docs
   - External references if needed
   - Tools and scripts
   - Mark required vs. optional
   - **Checkpoint:** Can students access everything they need?

6. **Define Success Criteria** (15 minutes)
   - How will students know they're done?
   - Align with objectives
   - Make observable
   - **Checkpoint:** Can students self-assess?

7. **Design Assessment** (20 minutes)
   - Formative (during learning)
   - Summative (completion)
   - Multiple methods
   - Practical and achievable
   - **Checkpoint:** Do assessments test objectives?

8. **Write Purpose** (10 minutes)
   - Concise summary of module
   - Target level indicated
   - Why it matters
   - **Checkpoint:** Is purpose clear and motivating?

### Total Estimated Time: 140 minutes (~2.5 hours)

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Vague Objectives | "Understand X" | Use action verbs: "Explain X", "Implement X", "Analyze X" |
| No Prerequisites | Every module is foundational | Identify actual prerequisite skills needed |
| Circular Dependencies | Module A needs B needs A | Break circle, find true starting point |
| Disorganized Content | Random topic order | Organize by logical progression (simple → complex) |
| Unrealistic Time | 30 min for complex topic | Test with learners, account for practice time |
| No Resources | Students don't know where to look | Provide specific internal and external resources |
| Unobservable Criteria | "Feel confident" | Use concrete criteria: "Can do X correctly" |
| Assessment Mismatch | Tests don't match objectives | Design assessments that directly test each objective |
| Scope Too Broad | Trying to teach everything | Focus on 2-4 key objectives, save rest for other modules |

## Best Practices

1. **Start with Objectives** - Know what students will DO before planning content
2. **Use Action Verbs** - Follow Bloom's taxonomy for observable outcomes
3. **Be Realistic with Time** - Test estimates with actual learners when possible
4. **Provide Sufficient Resources** - Include both internal and external references
5. **Enable Self-Assessment** - Clear success criteria let students track progress
6. **Align Assessment with Objectives** - Every objective should be tested
7. **Keep Scope Focused** - Better to do 3 things well than 10 things poorly
8. **Reference Skill Vertices** - Link to actual skill documents for prerequisites
9. **Check Dependency Chains** - Avoid circular prerequisites
10. **Enumerate Internal Steps** - Help students track progress within the module

## Module Granularity Guidance

### Choosing Appropriate Scope

**Too Broad (Avoid):**
- "Master all knowledge complex concepts" (too much for one module)
- "Learn everything about topology" (unbounded scope)
- "Complete guide to documentation systems" (could be 10 modules)

**Too Narrow (Avoid):**
- "Learn what the letter V means in χ = V - E + F" (trivial, could be one step)
- "Understand one specific edge type" (too small for standalone module)
- "Read the spec-for-chart document" (activity, not module)

**Appropriate Granularity:**
- **Broad Module:** "Simplicial Complex Fundamentals" (2-4 hours, multiple concepts)
- **Moderate Module:** "Verification Edge Creation" (1-2 hours, focused skill)
- **Narrow Module:** "Calculating Euler Characteristic" (1 hour, specific technique)

**Choose granularity based on:**
- Learning objectives (2-4 objectives suggests moderate scope)
- Time estimate (1-4 hours is typical for one module)
- Prerequisite chain (modules should build logically)
- Syllabus structure (how modules combine in learning path)

### Module Sequencing Considerations

Remember: **Modules are vertices, syllabi are charts**

- Modules don't define their own sequencing
- Syllabus charts assemble modules using prerequisite faces
- Each module should work as standalone unit (given prerequisites)
- Design modules to combine flexibly in multiple syllabi

**Example:**
```
Module A (foundational) → Syllabus 1 (linear path)
Module B (builds on A)  → Syllabus 2 (branching path)
Module C (builds on A)  → Syllabus 3 (custom combination)
```

## Validation vs. Verification

**Verification** (deterministic):
- All required sections present
- Learning Objectives lists 2+ objectives
- Prerequisite Skills lists 0+ items (or "None")
- Module Content has 2+ steps
- Success Criteria lists 2+ criteria
- Assessment Methods has 1+ method
- ID format correct (v:learning-module:<name>)
- Tags include [vertex, doc, learning-module]

**Validation** (qualitative):
- Learning objective clarity and observability
- Action verbs used appropriately (Bloom's taxonomy)
- Prerequisite appropriateness and coherence
- No circular dependencies
- Content structure and logical progression
- Time estimate realism
- Resource sufficiency and accessibility
- Success criteria observability and alignment
- Assessment alignment with objectives
- Scope appropriateness (not too broad, not too narrow)
- Overall module quality and effectiveness

---

**Note:** Learning modules are individual learning units (vertices) that get assembled into learning paths by syllabus charts. Great modules have clear objectives, appropriate scope, realistic time estimates, and observable success criteria that enable effective learning and self-assessment.
