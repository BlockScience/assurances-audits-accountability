---
type: face/prerequisite
vertices:
  - v:student:<student-name>
  - v:skill:<skill-name>
  - v:learning-module:<module-name>
edges:
  - e:has-skill:<student-name>:<skill-name>
  - e:requires-skill:<module-name>:<skill-name>
  - e:studies:<student-name>:<module-name>
orientation: oriented
id: f:prerequisite:<student-name>:<skill-name>:<module-name>
name: Prerequisite triangle - <student-name> with <skill-name> for <module-name>
description: <student-name> possessing <skill-name> can study <module-name> which requires that skill
tags:
  - face
  - prerequisite
  - triangle
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# Prerequisite Triangle: <student-name> with <skill-name> for <module-name>

## Purpose

This face represents a **prerequisite triangle** validating that student **<student-name>** possesses skill **<skill-name>** and can therefore study module **<module-name>** which requires that skill. The prerequisite face is a 2-dimensional structure (triangle) in the simplicial complex that "completes the circuit" between students, skills, and modules.

## Face Type

**Face Type:** prerequisite (2-simplex / triangle)

**Dimension:** 2 (connects 3 vertices)

**Boundary Edges:**
1. `e:has-skill:<student-name>:<skill-name>` - Student possesses skill
2. `e:requires-skill:<module-name>:<skill-name>` - Module requires skill
3. `e:studies:<student-name>:<module-name>` - Student studies module

## Vertices

The prerequisite triangle connects three vertices in a specific pattern:

1. **Student vertex:** `v:student:<student-name>` - The learner
2. **Skill vertex:** `v:skill:<skill-name>` - The prerequisite capability
3. **Learning-Module vertex:** `v:learning-module:<module-name>` - The learning unit

## Meaning

This face validates the **prerequisite relationship pattern**:

```
Student HAS skill (has-skill edge)
     +
Module REQUIRES skill (requires-skill edge)
     =
Student CAN STUDY module (studies edge is valid)
```

The triangle "fills in" the relationship between all three vertices, asserting that the prerequisite is satisfied.

## Topological Structure

```
                    v:skill:<skill-name>
                          /\
                         /  \
          has-skill     /    \  requires-skill
                       /      \
                      /        \
                     /          \
                    /            \
                   /   TRIANGLE   \
                  /   (this face)  \
                 /                  \
                /____________________\
     v:student:<student-name>    v:learning-module:<module-name>
                   studies edge
```

The face is the **filled triangle** (interior), not just the edges.

## Examples

**Foundational Module (No Prerequisites):**
```yaml
# Module has no prerequisites
# No prerequisite faces needed (no requires-skill edges exist)
```

**Beginner Student with Foundational Skill:**
```yaml
type: face/prerequisite
vertices:
  - v:student:knowledge-complex-learner
  - v:skill:simplicial-complex-fundamentals
  - v:learning-module:verification-fundamentals

# Validation:
# - Student HAS simplicial-complex-fundamentals (has-skill edge exists)
# - Module REQUIRES simplicial-complex-fundamentals (requires-skill edge exists)
# - Student CAN STUDY verification-fundamentals (studies edge is valid)
```

**Advanced Student with Multiple Prerequisites:**
```yaml
# Multiple triangles for multiple prerequisites
type: face/prerequisite
vertices:
  - v:student:alice-researcher
  - v:skill:chart-creation
  - v:learning-module:advanced-chart-design

type: face/prerequisite
vertices:
  - v:student:alice-researcher
  - v:skill:type-system-understanding
  - v:learning-module:advanced-chart-design

# Both triangles must exist to validate all prerequisites
```

## Validation Logic

The prerequisite face is **valid** if and only if:

1. All three vertices exist in the knowledge complex
2. All three boundary edges exist:
   - `e:has-skill:<student-name>:<skill-name>` exists
   - `e:requires-skill:<module-name>:<skill-name>` exists
   - `e:studies:<student-name>:<module-name>` exists OR is intended to exist
3. The skill vertex matches in both edges (same skill)
4. The student and module vertices match their respective edges

**Invalid Prerequisite:**
```
Student: beginner-learner
  has-skill: [none]

Module: advanced-topics
  requires-skill: expert-knowledge

❌ CANNOT CREATE TRIANGLE - student lacks skill!
```

**Valid Prerequisite:**
```
Student: intermediate-learner
  has-skill: foundational-concepts

Module: intermediate-topics
  requires-skill: foundational-concepts

✅ CAN CREATE TRIANGLE - prerequisite satisfied
```

## Multiple Prerequisites Pattern

When a module requires multiple skills, create **multiple prerequisite faces**:

```
Module: advanced-module
  requires-skill: skill-A
  requires-skill: skill-B
  requires-skill: skill-C

Student: prepared-learner
  has-skill: skill-A
  has-skill: skill-B
  has-skill: skill-C

Prerequisite Faces:
  1. Triangle(prepared-learner, skill-A, advanced-module)
  2. Triangle(prepared-learner, skill-B, advanced-module)
  3. Triangle(prepared-learner, skill-C, advanced-module)

ALL three triangles must exist for student to study module validly.
```

## Syllabus Chart Integration

Prerequisite faces are used by **syllabus charts** to:

1. Validate learning path sequences (ensure prerequisites are satisfied)
2. Detect when students are ready for next modules
3. Identify missing prerequisites that block progression
4. Visualize dependency structure of learning paths

## Topological Properties

**Euler Characteristic Contribution:**

Each prerequisite face contributes to the Euler characteristic:

```
χ = V - E + F

Adding this face:
V: +0 (vertices already exist)
E: +0 (edges already exist)
F: +1 (this new face)

χ increases by 1
```

**Hole Filling:**

Prerequisite faces "fill holes" in the student-skill-module relationship graph:
- Without face: Three edges form a hole (unfilled triangle)
- With face: Triangle is filled (complete 2-simplex)

## Constraints

- Must reference exactly 3 vertices (triangle)
- Vertex order convention: [student, skill, learning-module]
- All three vertices must exist
- All three boundary edges should exist (or studies edge is being created)
- Skill vertex must match in both has-skill and requires-skill edges
- Should not create faces for modules with no prerequisites (no requires-skill edges)
- Multiple faces can share vertices and edges (multiple prerequisites)

## Verification

This face can be verified using:

```bash
python scripts/verify_template_based.py 02_faces/<face-file>.md --templates templates
```

Chart-level verification can check prerequisite face completeness:

```bash
python scripts/verify_chart.py charts/<syllabus>/<syllabus>.md
```

---

**Note:** This template defines the prerequisite face relationship (triangle) connecting students, skills, and learning modules. Prerequisite faces validate that students with required skills can study modules that require those skills, and are essential for syllabus chart sequencing and learning path validation.
