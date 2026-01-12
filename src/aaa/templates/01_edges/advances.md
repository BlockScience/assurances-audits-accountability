---
type: edge/advances
source: v:learning-module:<module-name>
target: v:student:<student-after>
source_type: vertex/learning-module
target_type: vertex/student
orientation: directed
id: e:advances:<module-name>:<student-after>
name: <module-name> advances <student-after>
description: <module-name> completion advances learner to <student-after> state
tags:
  - edge
  - advances
  - completion
version: 1.0.0
created: <ISO-8601 datetime>
modified: <ISO-8601 datetime>
---

# <module-name> advances <student-after>

## Purpose

This edge represents that completing module **<module-name>** advances the learner to **<student-after>** state. The advances relationship connects learning modules to the resulting student states, and **exists ONLY within completion faces** as the third boundary edge.

## Relationship Type

**Edge Type:** advances (state advancement)

**Direction:** learning-module → student (module advances to student state)

**Participants:**
- **Source:** `v:learning-module:<module-name>` (the completed module)
- **Target:** `v:student:<student-after>` (the resulting learning state)

## Meaning

This edge indicates that completing `<module-name>` advances the learner to `<student-after>` state with an expanded skill set. This edge **only exists within completion face triangles** and serves to close the boundary.

**Key constraint:** This edge type is ONLY used as a boundary edge of completion faces. It does not exist independently outside of completion face topology.

## Completion Face Boundary Pattern

The advances edge is the **third boundary edge** of completion faces:

```
Completion face: (student-before, module, student-after)

Boundary edges:
1. e:studies:student-before:module          (student engages with module)
2. e:transitions-to:student-before:student-after  (state transition)
3. e:advances:module:student-after          (module advances to new state) ← THIS EDGE
```

These 3 edges form a closed triangle representing the complete learning transformation.

## Topological Role

**Closes the completion triangle:**

```
                v:learning-module:<module-name>
                          /\
                         /  \
              studies   /    \  advances (this edge)
                       /      \
                      /        \
                     /          \
                    /  COMPLETION \
                   /     FACE      \
                  /                 \
                 /___________________\
    v:student:<student-before>  v:student:<student-after>
                  transitions-to
```

Without this edge, the completion face would have an open boundary (not a valid 2-simplex).

## Examples

**Foundational Module Completion:**
```yaml
# Module advances learner from entry state to foundational state
source: v:learning-module:simplicial-complex-fundamentals
target: v:student:foundational-learner

# Part of completion face:
# (knowledge-complex-learner, simplicial-complex-fundamentals, foundational-learner)
```

**Intermediate Module Completion:**
```yaml
# Module advances from foundational to intermediate
source: v:learning-module:verification-fundamentals
target: v:student:intermediate-learner

# Part of completion face:
# (foundational-learner, verification-fundamentals, intermediate-learner)
```

## Semantic Meaning

While topologically this edge just closes the triangle, semantically it represents:
- **Input transformation:** Module takes student-before as input
- **Skill development:** Module develops new skills (via develops-skill edges)
- **Output production:** Module advances learner to student-after with accumulated skills

The edge encodes: **module.output = student-after**

## Relationship to develops-skill

**Important distinction:**
- `develops-skill` edges: module → skill (what the module teaches)
- `advances` edge: module → student-after (who the learner becomes)

The student-after has the developed skills via has-skill edges, but the advances edge connects directly to the student vertex to close the completion face triangle.

## Constraints

- Source MUST be a learning-module vertex (v:learning-module:*)
- Target MUST be a student vertex (v:student:*)
- **ONLY exists within completion faces** - not used independently
- Each module-student pair should have at most one advances edge
- Module must be defined (learning-module vertex exists)
- Student must be defined (student vertex exists)
- Target student must have source student's skills ∪ module's developed skills

## Usage Pattern

**Completion face creation:**
```yaml
# Step 1: Create student-before state
v:student:beginner (has skills A, B)

# Step 2: Create module
v:learning-module:fundamentals (requires A, B; develops C)

# Step 3: Create student-after state
v:student:intermediate (has skills A, B, C)

# Step 4: Create boundary edges
e:studies:beginner:fundamentals
e:transitions-to:beginner:intermediate
e:advances:fundamentals:intermediate  ← Create this edge

# Step 5: Create completion face with all 3 edges
f:completion:beginner:fundamentals:intermediate
  edges: [studies, transitions-to, advances]
```

## Anti-Pattern: Independent Usage

**Invalid:**
```yaml
# Advances edge exists without completion face
e:advances:module-A:student-X
# But no completion face references it
❌ INVALID - advances edges ONLY exist in completion faces
```

**Valid:**
```yaml
# Advances edge created for completion face
e:advances:module-A:student-X
# And completion face uses it
f:completion:student-Y:module-A:student-X
  edges: [..., e:advances:module-A:student-X]
✅ VALID - advances edge is boundary of completion face
```

## Verification

This edge can be verified using:

```bash
python scripts/verify_template_based.py 01_edges/<edge-file>.md --templates templates
```

Completion face verification checks that all 3 boundary edges exist and form a closed triangle.

---

**Note:** This template defines the advances relationship that closes completion face triangles. This edge type exists ONLY within completion face topology and represents the module advancing the learner to a new state with expanded skills.
