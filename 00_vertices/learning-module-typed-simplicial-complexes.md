---
type: vertex/learning-module
extends: doc
id: v:learning-module:typed-simplicial-complexes
name: Typed Simplicial Complexes - From Structure to Semantics
description: Module teaching semantic type systems for simplicial complexes using Module 1's syllabus chart as the primary learning artifact
tags:
  - vertex
  - doc
  - learning-module
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: beginner
dependencies: []
---

# Typed Simplicial Complexes - From Structure to Semantics

## Purpose

This module teaches students how semantic type systems organize and constrain simplicial complexes beyond pure topology. By analyzing the syllabus chart from [[v:learning-module:simplicial-complex-fundamentals]] (Module 1), students learn how types like `vertex/student`, `vertex/skill`, and `vertex/learning-module` create semantic meaning, how edge types enforce valid relationships, and how face types validate type consistency.

**Meta-Learning Approach:** Students already completed Module 1 and interacted with its typed syllabus chart. This module makes that implicit type system explicit, helping students understand WHAT they were working with and WHY types matter.

## Learning Objectives

After completing this module, students will be able to:

- Identify semantic vertex types in typed simplicial complexes (student, skill, module, etc.)
- Read and interpret type annotations in document frontmatter (`type: vertex/student`)
- Explain why certain edge relationships are valid or invalid based on type constraints
- Validate that faces connect correctly typed vertices (prerequisite/completion/skill-gain patterns)
- Apply typing discipline to design custom typed simplicial complexes for new domains
- Articulate the benefits of typed vs untyped simplicial complexes

## Prerequisite Skills

**Required:**
- [[v:skill:simplicial-complex-fundamentals]] - Must understand vertices, edges, faces, and Euler characteristic

**Module Prerequisite:**
- Students must have completed [[v:learning-module:simplicial-complex-fundamentals]] (Module 1)
- Familiarity with Module 1's syllabus chart is essential (it's THE learning artifact)

## Module Content

### Section 1: Reviewing Module 1's Chart Structure (30 min)

**Goal:** Reactivate student familiarity with Module 1's syllabus chart as foundation for type analysis

1. **Open Module 1's visualization** (`charts/learning-journey-module-01/learning-journey-module-01.html`)
   - Observe color-coded vertices: blue (students), green (skills), purple (module)
   - Notice different edge colors connecting different vertex types
   - Identify the three face types: orange (prerequisite), blue (completion), dark green (skill-gain)

2. **Review chart topology**
   - Count: V=6 (2 students, 3 skills, 1 module)
   - Count: E=11 (various relationship types)
   - Count: F=4 (1 prerequisite, 1 completion, 1 skill-gain, 1 extra prerequisite)
   - Calculate: χ = 6 - 11 + 4 = -1

3. **Question for reflection:** "Why are vertices colored differently? What do the colors mean?"
   - This sets up the transition to type systems

### Section 2: Types as Semantic Categories (45 min)

**Goal:** Understand that vertex types represent semantic categories, not just arbitrary labels

1. **Examine vertex documents from Module 1**
   - Read `00_vertices/student-knowledge-complex-learner.md` frontmatter
   - Observe: `type: vertex/student` - this is a TYPE ANNOTATION
   - Read `00_vertices/skill-simplicial-complex-fundamentals.md`
   - Observe: `type: vertex/skill` - different type!
   - Read `00_vertices/learning-module-simplicial-complex-fundamentals.md`
   - Observe: `type: vertex/learning-module` - third type!

2. **Understand type hierarchies**
   - `vertex/student` extends `vertex/actor` extends `vertex/doc`
   - `vertex/skill` extends `vertex/property` extends `vertex/doc`
   - `vertex/learning-module` extends `doc`
   - All share `vertex/doc` root, but have different semantic meanings

3. **Semantic meaning of types**
   - **Student types**: Represent learning states (snapshots of skill possession)
   - **Skill types**: Represent capabilities (can be possessed by students)
   - **Module types**: Represent learning transformations (require skills, develop skills)

4. **Exercise:** Classify 5 unlabeled vertices by examining their descriptions
   - Determine if each represents a learning state, capability, or transformation
   - Assign appropriate type annotations

### Section 3: Type-Driven Edge Constraints (60 min)

**Goal:** Understand how edge types enforce semantically valid relationships

1. **Examine edge types in Module 1**
   - **has-skill edges** (student → skill): Students possess capabilities
   - **requires-skill edges** (module → skill): Modules need prerequisites
   - **develops-skill edges** (module → skill): Modules produce outcomes
   - **studies edges** (student → module): Students engage with modules
   - **transitions-to edges** (student → student): Learning state progression
   - **advances edges** (module → student): Module completion advances student

2. **Type constraints on edges**
   - Read `01_edges/has-skill-knowledge-complex-learner-basic-graph-knowledge.md`
   - Observe frontmatter: `source_type: vertex/student`, `target_type: vertex/skill`
   - **Type constraint:** has-skill MUST connect student to skill (not skill to student!)
   - **Why:** Semantically, students possess skills, not vice versa

3. **Analyze invalid edge examples**
   - Why is `has-skill: skill → student` invalid? (Skills don't possess students)
   - Why is `requires-skill: skill → module` invalid? (Skills don't require modules)
   - Why is `transitions-to: skill → skill` invalid? (Skills don't transition)

4. **Edge orientation and types**
   - Read `orientation: directed` in edge frontmatter
   - Understand: direction matters BECAUSE types matter
   - `student → skill` (valid) ≠ `skill → student` (invalid)

5. **Exercise:** Validate 10 edge relationships
   - Given edge descriptions, determine if source/target types are valid
   - Explain WHY each edge is valid or invalid based on semantics

### Section 4: Face Type Patterns and Validation (60 min)

**Goal:** Understand how faces validate that connected elements have compatible types

1. **Three face types in learning journeys**
   - **Prerequisite faces:** `(student, skill, module)` - validate student has required skill
   - **Completion faces:** `(student-before, module, student-after)` - validate state transition
   - **Skill-gain faces:** `(student-after, module, skill)` - validate skill acquisition

2. **Prerequisite face type analysis**
   - Read `02_faces/prerequisite-knowledge-complex-learner-basic-graph-knowledge-simplicial-complex-fundamentals.md`
   - Vertices: student, skill, module (three DIFFERENT types)
   - Boundary edges: has-skill (student → skill), requires-skill (module → skill), studies (student → module)
   - **Type validation:** All three edge types connect correctly typed vertices
   - **Semantic meaning:** "This student possesses the skill this module requires"

3. **Completion face type analysis**
   - Read `02_faces/completion-knowledge-complex-learner-simplicial-complex-fundamentals-foundational-learner.md`
   - Vertices: student (before), module, student (after) - two student instances, one module
   - Boundary edges: studies, transitions-to, advances
   - **Type pattern:** (student, module, student) - input state, transformation, output state
   - **Semantic meaning:** "Module transforms student-before into student-after"

4. **Skill-gain face type analysis**
   - Read `02_faces/skill-gain-foundational-learner-simplicial-complex-fundamentals-simplicial-complex-fundamentals.md`
   - Vertices: student (after), module, skill - three different types
   - Boundary edges: advances (module → student), has-skill (student → skill), develops-skill (module → skill)
   - **Type pattern:** (student, module, skill) - beneficiary, source, outcome
   - **Semantic meaning:** "Student gained this skill from completing this module"

5. **Exercise:** Type-validate 5 faces
   - Given face vertex descriptions, identify face type (prerequisite/completion/skill-gain)
   - Verify all boundary edges have correct source/target types
   - Explain semantic meaning of each face

### Section 5: Applying Types to New Domains (45 min)

**Goal:** Generalize typing principles beyond learning journeys to custom domains

1. **Design exercise: Library knowledge complex**
   - Domain: Books, readers, genres, recommendations
   - Identify vertex types: What are the "actors"? What are the "properties"?
   - Possible: `vertex/reader`, `vertex/book`, `vertex/genre`, `vertex/library`

2. **Design typed edges**
   - What relationships exist? (readers borrow books, books belong to genres, etc.)
   - Define edge types with source/target constraints
   - Example: `has-read: reader → book`, `belongs-to: book → genre`

3. **Design typed faces**
   - What triangular relationships validate constraints?
   - Example: `(reader, genre, book)` - reader interested in genre, book is that genre, reader reads book
   - Boundary: `interested-in: reader → genre`, `belongs-to: book → genre`, `has-read: reader → book`

4. **Generalization principles**
   - Types encode domain semantics (not just arbitrary labels)
   - Edge type constraints prevent nonsensical relationships
   - Faces validate multi-vertex patterns
   - Type systems make implicit constraints explicit

5. **Final exercise:** Design typed complex for chosen domain
   - Choose: recipe domain, music domain, course curriculum domain, or custom
   - Define 3+ vertex types
   - Define 4+ edge types with source/target constraints
   - Define 2+ face types with semantic meaning
   - Validate type consistency

## Estimated Time

**Total:** 4.5-5 hours

- Section 1 (Review): 30 min
- Section 2 (Types): 45 min
- Section 3 (Edges): 60 min
- Section 4 (Faces): 60 min
- Section 5 (Application): 45 min
- Exercises (integrated): ~30 min
- Assessment: ~30 min

## Resources

**Required:**
- [[c:learning-journey-module-01]] - Module 1's syllabus chart (THE primary learning artifact)
- `charts/learning-journey-module-01/learning-journey-module-01.html` - Interactive visualization
- Vertex documents from Module 1 (in `00_vertices/`)
- Edge documents from Module 1 (in `01_edges/`)
- Face documents from Module 1 (in `02_faces/`)

**Optional:**
- [[v:spec:student]] - Formal specification for student vertex type
- [[v:spec:skill]] - Formal specification for skill vertex type
- [[v:spec:learning-module]] - Formal specification for learning module vertex type
- Type system documentation from programming language theory (for advanced learners)

## Success Criteria

Students have successfully completed this module when they can:

- **Type annotation:** Add correct type annotations to 3 untyped vertex documents
- **Edge validation:** Correctly validate 10 edge relationships as type-consistent or type-violating
- **Face validation:** Identify face types and validate boundary edge types for 5 faces
- **Domain design:** Design a complete typed simplicial complex for a custom domain with:
  - 3+ vertex types with clear semantic meaning
  - 4+ edge types with correct source/target type constraints
  - 2+ face types with validated boundary patterns
- **Explanation:** Write 2-3 paragraphs explaining benefits of typing vs untyped complexes

**Standard:** 80% accuracy on all exercises and assessment demonstrates skill acquisition

## Assessment Methods

**Formative (During Module):**
- Section 2 exercise: Classify 5 vertices by type (immediate feedback)
- Section 3 exercise: Validate 10 edge relationships (self-check with answer key)
- Section 4 exercise: Type-validate 5 faces (peer review)
- Section 5 exercises: Domain design iterations (instructor feedback)

**Summative (End of Module):**
- **Comprehensive domain design:** Create typed complex for chosen domain (graded)
- **Type validation exam:** Validate 15 vertex/edge/face combinations (80% threshold)
- **Written explanation:** Benefits of type systems in simplicial complexes (rubric-graded)
- **Practical application:** Add type annotations to provided untyped chart (correctness check)

---

**Note:** This module leverages meta-learning by analyzing the very chart students used in Module 1. By making the implicit type system explicit, students gain deeper understanding of HOW types organize simplicial complexes and WHY semantic constraints matter. This prepares them for chart creation, verification, and assurance work in future modules.
