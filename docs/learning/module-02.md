# Module 02 - Typed Simplicial Complexes: From Structure to Semantics

Welcome to Module 2! In Module 1, you learned about vertices, edges, and faces as the building blocks of simplicial complexes. You practiced calculating the Euler characteristic and interpreting charts. Now, we'll add a crucial layer: **semantic types**.

In this module, you'll discover how types organize simplicial complexes, enforce meaningful constraints, and prevent nonsensical relationships. You'll use the syllabus chart from Module 1 as your primary learning artifact—analyzing the very chart you completed to understand how types work.

## What You'll Learn

By the end of this module, you'll be able to:

- Identify semantic types in typed simplicial complexes
- Read and interpret type annotations in chart documents
- Explain why certain edge orientations are valid while others are not
- Validate type constraints in faces
- Apply typing discipline to design new charts for different domains

## Prerequisites

This module assumes you've completed Module 1 and possess:

- Understanding of vertices, edges, and faces
- Ability to calculate the Euler characteristic (χ = V - E + F)
- Familiarity with chart document structure
- Experience reading and visualizing charts

## Section 1: Reviewing Module 1's Chart Structure

Let's start by revisiting the syllabus chart you completed in Module 1. This chart represents your learning journey through simplicial complex basics.

### Exercise 1: Load Your Learning Journey Chart

Open the Module 1 syllabus chart:

```bash
# Read the chart document
cat charts/learning-journey-module-01/learning-journey-module-01.md
```

You should see a chart with these elements:

**Vertices (4):**
- `v:student:knowledge-complex-newcomer`
- `v:skill:basic-graph-knowledge`
- `v:skill:simplicial-complex-fundamentals`
- `v:learning-module:simplicial-complex-fundamentals`

**Edges (6):**
- `e:has-skill:knowledge-complex-newcomer:basic-graph-knowledge`
- `e:requires-skill:simplicial-complex-fundamentals:basic-graph-knowledge`
- `e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals`
- `e:studies:knowledge-complex-newcomer:simplicial-complex-fundamentals`
- Plus edges showing skill accumulation

**Faces (2):**
- Prerequisite face validating you had the required skill
- Completion face showing skill acquisition

### What Did These Elements Represent?

In Module 1, you understood these as:

- **Vertices**: Points in the structure
- **Edges**: Connections between points
- **Faces**: Triangular relationships

But there's more structure here than just topology. Notice the patterns:

- All vertex IDs start with `v:` followed by a category like `student:`, `skill:`, or `learning-module:`
- All edge IDs start with `e:` followed by a relationship type like `has-skill:` or `requires-skill:`
- Edges have direction: `student` → `skill`, not `skill` → `student`

These patterns aren't arbitrary. They reflect **semantic types**.

### Reflection Questions

Before reading on, consider:

1. Why does the edge go `student → skill` rather than `skill → student`?
2. What would it mean if an edge went from `learning-module` to `student`?
3. Are all edge directions equally sensible, or do some make more sense than others?

**Key Insight:** The structure you learned in Module 1 wasn't just topological—it was **typed**. Types were implicit in the naming conventions and relationship patterns. In this module, we'll make types explicit and understand why they matter.

## Section 2: Types as Semantic Categories

A **type** is a semantic category that groups elements by their meaning and role. In typed simplicial complexes, vertices, edges, and faces carry type annotations that constrain what relationships are valid.

### Vertex Types

Look again at Module 1's vertices:

```yaml
vertices:
  - v:student:knowledge-complex-newcomer
  - v:skill:basic-graph-knowledge
  - v:skill:simplicial-complex-fundamentals
  - v:learning-module:simplicial-complex-fundamentals
```

Each vertex has a **vertex type** indicated in its ID:

- `v:student:*` — vertices of type "student"
- `v:skill:*` — vertices of type "skill"
- `v:learning-module:*` — vertices of type "learning-module"

**What does a vertex type mean?**

A vertex type defines:

1. **What the vertex represents** (its semantic role)
2. **What properties it has** (attributes required)
3. **What edges can connect to it** (valid relationships)

For example:

- **Type:** `student`
- **Represents:** A learner in a particular learning state
- **Properties:** Learning goals, possessed skills
- **Valid incoming edges:** None directly (students don't receive edges from skills)
- **Valid outgoing edges:** `has-skill` (to skills), `studies` (to modules)

### Edge Types

Edges also have types, indicated by their relationship name:

```yaml
edges:
  - e:has-skill:knowledge-complex-newcomer:basic-graph-knowledge
  - e:requires-skill:simplicial-complex-fundamentals:basic-graph-knowledge
  - e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals
  - e:studies:knowledge-complex-newcomer:simplicial-complex-fundamentals
```

Each edge has:

1. **Edge type** (the relationship): `has-skill`, `requires-skill`, `develops-skill`, `studies`
2. **Source vertex type** (where it originates)
3. **Target vertex type** (where it points)

**Type constraints on edges:**

Edge types enforce **source-target type constraints**:

| Edge Type | Valid Source Type | Valid Target Type | Meaning |
|-----------|-------------------|-------------------|---------|
| `has-skill` | `student` | `skill` | Student possesses this skill |
| `requires-skill` | `learning-module` | `skill` | Module requires this prerequisite |
| `develops-skill` | `learning-module` | `skill` | Module develops this skill |
| `studies` | `student` | `learning-module` | Student studies this module |

### Exercise 2: Type Validation

For each potential edge below, determine if it's **valid** or **invalid** based on type constraints:

1. `e:has-skill:basic-graph-knowledge:knowledge-complex-newcomer`
   - Source type: `skill`
   - Target type: `student`
   - Valid? ______

2. `e:requires-skill:simplicial-complex-fundamentals:basic-graph-knowledge`
   - Source type: `learning-module`
   - Target type: `skill`
   - Valid? ______

3. `e:studies:simplicial-complex-fundamentals:knowledge-complex-newcomer`
   - Source type: `learning-module`
   - Target type: `student`
   - Valid? ______

4. `e:develops-skill:basic-graph-knowledge:simplicial-complex-fundamentals`
   - Source type: `skill`
   - Target type: `learning-module`
   - Valid? ______

**Answers:**

1. **Invalid** — `has-skill` requires source=`student`, target=`skill` (reversed here)
2. **Valid** — `requires-skill` requires source=`learning-module`, target=`skill` ✓
3. **Invalid** — `studies` requires source=`student`, target=`learning-module` (reversed here)
4. **Invalid** — `develops-skill` requires source=`learning-module`, target=`skill` (types wrong)

**Key Takeaway:** Types prevent nonsensical relationships. A skill can't "study" a module. A module can't "have" a skill (only students have skills). Types encode domain semantics directly into the structure.

### Why Types Matter

Without types, you could create topologically valid but semantically meaningless structures:

- A triangle connecting three skills (what would that mean?)
- An edge from a skill to a student claiming the skill "possesses" the student
- A face connecting two modules and a student (what relationship is this?)

Types provide **semantic guardrails** that ensure your simplicial complex represents something meaningful.

## Section 3: Type-Driven Edge Constraints

Now let's see how types constrain edge formation and orientation.

### Edge Orientation and Types

In Module 1, you learned that edges are **directed**: they go from a source to a target. But WHY does the direction matter?

**Answer:** Types give edges semantic meaning that depends on direction.

Consider `has-skill` edges:

```yaml
# Correct orientation
e:has-skill:knowledge-complex-newcomer:basic-graph-knowledge
# student → skill (student HAS skill)

# Incorrect orientation would be:
e:has-skill:basic-graph-knowledge:knowledge-complex-newcomer
# skill → student (skill HAS student?? Meaningless!)
```

The type `has-skill` defines:

- **Domain** (source type): `student`
- **Codomain** (target type): `skill`
- **Semantics**: The source possesses the target as a capability

Reversing the edge violates the type constraint and creates a meaningless relationship.

### Type Constraints Across Edge Types

Let's examine all edge types in Module 1's chart:

**1. `has-skill` edges**

```yaml
# Pattern: student → skill
e:has-skill:knowledge-complex-newcomer:basic-graph-knowledge
```

**Constraint:** Source MUST be `student`, target MUST be `skill`

**Semantics:** Student possesses skill as a capability

**2. `requires-skill` edges**

```yaml
# Pattern: learning-module → skill
e:requires-skill:simplicial-complex-fundamentals:basic-graph-knowledge
```

**Constraint:** Source MUST be `learning-module`, target MUST be `skill`

**Semantics:** Module requires skill as a prerequisite for study

**3. `develops-skill` edges**

```yaml
# Pattern: learning-module → skill
e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals
```

**Constraint:** Source MUST be `learning-module`, target MUST be `skill`

**Semantics:** Module develops skill as a learning outcome

**4. `studies` edges**

```yaml
# Pattern: student → learning-module
e:studies:knowledge-complex-newcomer:simplicial-complex-fundamentals
```

**Constraint:** Source MUST be `student`, target MUST be `learning-module`

**Semantics:** Student engages with module as learning activity

### Exercise 3: Design a Two-Module Learning Path

Now let's apply what you've learned about types to design a new chart.

**Scenario:** You want to create a syllabus chart for a two-module learning path:

1. **Module A:** "Introduction to Python" (develops skill "python-basics")
2. **Module B:** "Data Analysis with Pandas" (requires "python-basics", develops "data-analysis")

**Your task:** Design the typed structure for this two-module path.

**Step 1: Identify the vertices and their types**

List all vertices needed:

- Students (how many states?): ________________
- Skills (how many?): ________________
- Modules (how many?): ________________

**Step 2: Design the edges**

For each edge, specify:

- Edge type
- Source vertex (with type)
- Target vertex (with type)

Example format:
```
e:has-skill:beginner-student:python-basics
  Type: has-skill
  Source: v:student:beginner-student
  Target: v:skill:python-basics
```

**Step 3: Validate type constraints**

For each edge you designed, check:

1. Does the source type match the edge type's domain?
2. Does the target type match the edge type's codomain?
3. Does the semantic meaning make sense?

**Step 4: Calculate topology**

Count your vertices, edges, and faces (you'll need prerequisite and completion faces for each module):

- V = ______
- E = ______
- F = ______
- χ = V - E + F = ______

**Solution Discussion:**

You should have identified:

**Vertices (6-7):**
- 3 student states: absolute-beginner (no Python) → python-learner (has python-basics) → data-analyst (has both skills)
- 2 skills: python-basics, data-analysis
- 2 modules: intro-to-python, data-analysis-with-pandas

**Edges (12-14):**
- `has-skill` edges showing skill accumulation across student states
- `requires-skill` edges showing module prerequisites
- `develops-skill` edges showing module outcomes
- `studies` edges showing student-module engagement
- `transitions-to` edges showing student state progression

**Faces (4-6):**
- Prerequisite faces validating students have required skills
- Completion faces showing state transitions after module completion

**Topology:**
- χ will likely be 0 or 1 depending on exact structure

**Key Insight:** By following type constraints, you ensured every edge has valid source/target types and semantic meaning. The structure is both topologically and semantically valid.

## Section 4: Face Type Patterns

Faces in typed simplicial complexes also carry semantic meaning. Let's examine the face types from Module 1.

### Prerequisite Faces

A **prerequisite face** validates that a student has the skill required by a module:

```yaml
type: face/prerequisite
vertices:
  - v:student:knowledge-complex-newcomer
  - v:skill:basic-graph-knowledge
  - v:learning-module:simplicial-complex-fundamentals
```

**Boundary edges:**
1. `e:has-skill:knowledge-complex-newcomer:basic-graph-knowledge` (student HAS the skill)
2. `e:requires-skill:simplicial-complex-fundamentals:basic-graph-knowledge` (module REQUIRES the skill)
3. `e:studies:knowledge-complex-newcomer:simplicial-complex-fundamentals` (student STUDIES the module)

**Type constraint:** Prerequisite faces MUST have vertices typed as `(student, skill, learning-module)` in that semantic relationship.

**Semantic meaning:** This face validates that the student possesses the prerequisite skill needed to study the module. If this face exists, the student is **qualified** to begin the module.

### Completion Faces

A **completion face** represents a student completing a module and transitioning to a new learning state:

```yaml
type: face/completion
vertices:
  - v:student:knowledge-complex-newcomer
  - v:learning-module:simplicial-complex-fundamentals
  - v:student:foundational-learner
```

**Boundary edges:**
1. `e:studies:knowledge-complex-newcomer:simplicial-complex-fundamentals` (student STUDIES module)
2. `e:transitions-to:knowledge-complex-newcomer:foundational-learner` (student TRANSITIONS to new state)
3. `e:advances:simplicial-complex-fundamentals:foundational-learner` (module ADVANCES student to new state)

**Type constraint:** Completion faces MUST have vertices typed as `(student-before, learning-module, student-after)`.

**Semantic meaning:** This face represents the state transition caused by module completion. The student enters in one state and exits in another, with accumulated skills.

### Skill-Gain Faces

A **skill-gain face** attributes a specific skill to module completion:

```yaml
type: face/skill-gain
vertices:
  - v:student:foundational-learner
  - v:learning-module:simplicial-complex-fundamentals
  - v:skill:simplicial-complex-fundamentals
```

**Boundary edges:**
1. `e:has-skill:foundational-learner:simplicial-complex-fundamentals` (student HAS new skill)
2. `e:develops-skill:simplicial-complex-fundamentals:simplicial-complex-fundamentals` (module DEVELOPS the skill)
3. `e:advances:simplicial-complex-fundamentals:foundational-learner` (module ADVANCES to student state)

**Type constraint:** Skill-gain faces MUST have vertices typed as `(student-after, learning-module, skill-developed)`.

**Semantic meaning:** This face establishes causality—the student gained this specific skill BECAUSE they completed this module.

### Face Type Summary

| Face Type | Vertex Types | Validates |
|-----------|--------------|-----------|
| `prerequisite` | (student, skill, module) | Student has required skill before studying |
| `completion` | (student-before, module, student-after) | State transition through module completion |
| `skill-gain` | (student-after, module, skill) | Skill acquired from specific module |

### Exercise 4: Validate Face Boundaries

For the completion face in Module 1's chart:

```yaml
vertices:
  - v:student:knowledge-complex-newcomer
  - v:learning-module:simplicial-complex-fundamentals
  - v:student:foundational-learner
```

**Question 1:** List the three boundary edges this face requires (use the edge patterns from Section 3).

**Question 2:** For each boundary edge, identify:
- Edge type
- Source type
- Target type
- Does it satisfy the completion face pattern?

**Question 3:** What happens if one of these edges is missing? Is the face still valid topologically? Is it valid semantically?

**Answers:**

**Question 1:**
1. `e:studies:knowledge-complex-newcomer:simplicial-complex-fundamentals`
2. `e:transitions-to:knowledge-complex-newcomer:foundational-learner`
3. `e:advances:simplicial-complex-fundamentals:foundational-learner`

**Question 2:**

Edge 1: `studies`
- Source type: `student` (knowledge-complex-newcomer)
- Target type: `learning-module` (simplicial-complex-fundamentals)
- Satisfies pattern: ✓ (student engages with module)

Edge 2: `transitions-to`
- Source type: `student` (knowledge-complex-newcomer)
- Target type: `student` (foundational-learner)
- Satisfies pattern: ✓ (state transition)

Edge 3: `advances`
- Source type: `learning-module` (simplicial-complex-fundamentals)
- Target type: `student` (foundational-learner)
- Satisfies pattern: ✓ (module causes advancement)

**Question 3:**

If an edge is missing:
- **Topologically:** Face is invalid (boundary edges must form a closed triangle)
- **Semantically:** Face is invalid (cannot validate completion without all relationships)

**Key Takeaway:** Faces encode complex validation logic. The completion face validates that the module completion CAUSED the state transition AND that the student engaged with the module. All three edges are necessary for semantic validity.

## Section 5: Applying Types to New Domains

The power of typed simplicial complexes is that typing discipline transfers across domains. Once you understand the pattern, you can apply it to any domain with entities and relationships.

### Domain Examples

**1. Software Dependencies**

Vertices:
- Type: `package` (software packages)
- Type: `version` (specific releases)
- Type: `environment` (deployment contexts)

Edges:
- `depends-on`: package → package
- `provides`: package → version
- `deploys-to`: version → environment

Faces:
- `compatibility`: (package, version, environment) validates deployment

**2. Organizational Structure**

Vertices:
- Type: `person` (employees)
- Type: `role` (job functions)
- Type: `project` (work initiatives)

Edges:
- `has-role`: person → role
- `requires-role`: project → role
- `assigned-to`: person → project

Faces:
- `qualification`: (person, role, project) validates assignment

**3. Biological Pathways**

Vertices:
- Type: `protein` (molecular entities)
- Type: `reaction` (biochemical processes)
- Type: `pathway` (functional modules)

Edges:
- `catalyzes`: protein → reaction
- `participates-in`: reaction → pathway
- `regulates`: protein → pathway

Faces:
- `catalytic-role`: (protein, reaction, pathway) validates mechanism

### Exercise 5: Design a Typed Chart for Your Domain

Choose a domain you're familiar with (academic courses, project management, recipe ingredients, etc.).

**Step 1: Define vertex types**

What are the 3-4 main entity types in your domain?

1. Type: ________________ (represents: ________________)
2. Type: ________________ (represents: ________________)
3. Type: ________________ (represents: ________________)

**Step 2: Define edge types**

What are the 3-5 main relationships between entities?

For each relationship:
- Edge type name: ________________
- Source vertex type: ________________
- Target vertex type: ________________
- Semantic meaning: ________________

**Step 3: Define face types**

What triangular patterns validate important constraints in your domain?

For each face type:
- Face type name: ________________
- Vertex types: (______________, ______________, ______________)
- What it validates: ________________

**Step 4: Create a small example**

Instantiate your typed schema with 2-3 vertices of each type and a few edges/faces. Verify that all type constraints are satisfied.

### Reflection: What Makes a Good Type System?

Consider:

1. **Specificity:** Are vertex types specific enough to carry meaningful semantics, but general enough to avoid explosion of types?

2. **Constraint Utility:** Do edge type constraints prevent actual errors you'd make in your domain?

3. **Validation Patterns:** Do face types capture real validation logic you care about?

4. **Extensibility:** Can you add new edge/face types without redesigning vertex types?

**Key Insight:** Type systems are design choices. Good type systems make invalid states unrepresentable and important constraints explicit. The types in Module 1's syllabus chart weren't arbitrary—they were designed to prevent nonsensical learning paths and validate skill prerequisites.

## Self-Assessment

Test your understanding with these questions:

**Conceptual Understanding:**

1. What is a vertex type, and how does it differ from a vertex ID?

2. Why do edge types specify both source and target vertex types?

3. What is the difference between topological validity and semantic validity?

4. Can a simplicial complex be topologically valid (correct χ, all boundaries closed) but semantically invalid (type violations)? Give an example.

**Applied Skills:**

5. Given this edge: `e:mentors:alice:bob`, design a type system that makes this valid. What vertex types do `alice` and `bob` need? What does the `mentors` edge type require?

6. Create a prerequisite face for a cooking domain where a recipe requires a cooking technique and a chef has that technique. Specify all vertex types, edge types, and boundary edges.

7. Design a typed chart representing a library system with books, authors, and readers. Include at least 3 vertex types, 4 edge types, and 1 face type.

**Critical Thinking:**

8. In Module 1's chart, could you swap the types of `knowledge-complex-newcomer` and `basic-graph-knowledge` (make the student a skill and the skill a student) and still have the same topology (same V, E, F, χ)? Why or why not?

9. If you removed all type annotations from Module 1's chart, would it still be a valid simplicial complex? What would you lose?

10. Design a type system for a domain where the same entity can have multiple types simultaneously (e.g., a person who is both a student and a teacher). How would you represent this?

## Practice Problems

### Problem 1: Type Violation Detection

Which of these edges violate type constraints? Explain why.

```yaml
# Assume these vertex types:
# v:student:* (type: student)
# v:skill:* (type: skill)
# v:learning-module:* (type: learning-module)

edges:
  a. e:has-skill:python-learner:python-basics
  b. e:requires-skill:python-basics:intro-to-python
  c. e:develops-skill:intro-to-python:data-analysis
  d. e:studies:intro-to-python:python-learner
  e. e:has-skill:intro-to-python:python-basics
```

### Problem 2: Face Boundary Validation

A prerequisite face has vertices `(v:student:alice, v:skill:algebra, v:learning-module:calculus)`.

List the three boundary edges required and specify their types. Then verify each edge's source and target types are correct.

### Problem 3: Chart Extension

Extend Module 1's chart to include a second module that requires `simplicial-complex-fundamentals` as a prerequisite and develops a new skill `chart-design`.

How many new vertices, edges, and faces do you need to add? What is the new Euler characteristic?

### Problem 4: Domain Translation

Translate this learning journey pattern to a software onboarding domain:

- **Learning journey:** (student, skill, learning-module)
- **Software onboarding:** (engineer, __________, __________)

Design the complete type system with 3 vertex types, 4 edge types, and 2 face types.

## Next Steps

Congratulations! You now understand typed simplicial complexes and can apply typing discipline to organize knowledge across domains.

### Immediate Practice

1. **Visualize Module 2's chart:** Just like you did for Module 1, generate and explore the 3D visualization of the Module 2 syllabus chart (`learning-journey-module-02`). Notice how it extends Module 1's structure with the new skill and student state.

2. **Analyze the knowledge complex repository:** Explore the `/00_vertices/`, `/01_edges/`, and `/02_faces/` directories. Read a few documents and identify their types. Notice how the type system organizes the entire repository.

3. **Create a typed chart:** Design a small typed chart (5-10 vertices) for a domain you care about. Write out the vertex/edge/face documents following the type patterns you learned.

### Continuing Your Learning Journey

Consider these next modules:

- **Module 3: Composing Typed Simplicial Complexes** — Learn how to combine charts through identification (pasting) while preserving type consistency and topological validity
- **Module 4: Verification and Validation Patterns** — Learn how to verify type constraints programmatically and validate semantic correctness
- **Module 5: Chart Creation and Design** — Develop skills in designing effective typed charts for complex domains

### Deeper Exploration

- **Type Theory Foundations:** Explore the mathematical foundations of type systems (dependent types, subtyping, polymorphism)
- **Domain-Specific Type Systems:** Study how type systems are designed for programming languages, databases, and knowledge graphs
- **Compositional Design:** Learn how typed simplicial complexes enable compositional reasoning about complex systems

## Glossary

**Codomain:** The target vertex type required by an edge type

**Completion Face:** Face type representing student state transition through module completion, with vertices (student-before, learning-module, student-after)

**Domain (of edge type):** The source vertex type required by an edge type

**Edge Type:** A semantic category defining valid source vertex type, target vertex type, and relationship meaning

**Face Type:** A semantic category defining valid vertex type patterns and validation semantics for triangular relationships

**Prerequisite Face:** Face type validating student has required skill before studying module, with vertices (student, skill, learning-module)

**Semantic Type:** A category grouping elements by meaning and role, constraining valid relationships

**Semantic Validity:** Property of a simplicial complex where all type constraints are satisfied and relationships are meaningful

**Skill-Gain Face:** Face type attributing skill acquisition to specific module completion, with vertices (student-after, learning-module, skill-developed)

**Type Annotation:** Explicit declaration of an element's semantic type, often in the ID or frontmatter

**Type Constraint:** A rule restricting valid combinations of types (e.g., edge source/target types, face vertex types)

**Type System:** The complete set of types and type constraints defining valid structures in a domain

**Typed Simplicial Complex:** A simplicial complex where vertices, edges, and faces carry semantic type annotations that constrain valid relationships

**Vertex Type:** A semantic category defining what a vertex represents, its properties, and valid incident edges

---

**Module 2 Complete!** You've learned how types organize simplicial complexes and enforce semantic correctness. You can now design typed charts that are both topologically and semantically valid. In the next module, you'll learn how to verify these properties programmatically and build confidence through systematic validation.
