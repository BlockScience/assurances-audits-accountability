---
type: vertex/spec
extends: vertex/doc
id: v:spec:syllabus
name: Specification for Syllabus Charts
description: Defines the structure and constraints for syllabus chart type documents representing learning journeys with prerequisite validation and skill accumulation
tags:
  - vertex
  - spec
  - chart-type
  - syllabus
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies:
  - v:spec:chart
---

# Specification for Syllabus Charts

## Purpose

This specification defines the **syllabus chart type** - a specialized chart representing learning journeys through structured curriculum with prerequisite validation, skill accumulation tracking, and state-based progression.

Syllabus charts encode learning paths as simplicial complexes where:
- **Vertices** represent students (learning states), skills (capabilities), and modules (instruction units)
- **Edges** represent relationships (possession, requirement, development, study, transition)
- **Faces** represent validation constraints (prerequisites), state transitions (completion), and causal acquisition (skill-gain)

## Document Type

**Type:** `chart/syllabus`

**Extends:** `chart/chart` (inherits all chart requirements plus syllabus-specific constraints)

## Required Frontmatter Fields

All fields from `chart/chart` specification PLUS:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `type` | string | Must be `chart/syllabus` | Yes |
| `extends` | string | Must be `chart` | Yes |
| `learning_path` | object | Defines entry/exit states | Yes |
| `learning_path.entry_state` | string | Initial student state vertex ID | Yes |
| `learning_path.exit_states` | list[string] | Completion student state vertex IDs | Yes |
| `prerequisites` | object | Entry requirements | Yes |
| `prerequisites.entry_skills` | list[string] | Skills required to start (may be empty) | Yes |
| `outcomes` | object | Learning outcomes | Yes |
| `outcomes.developed_skills` | list[string] | All skills developed across modules | Yes |

### Example Frontmatter

```yaml
---
type: chart/syllabus
extends: chart
id: c:intro-programming-syllabus
name: Introduction to Programming Syllabus
description: Foundational programming curriculum with 3 modules

# Chart construction metadata
constructed_by: "Alice Teacher"
construction_method: manual
construction_date: 2025-12-28T00:00:00Z

# Chart purpose
purpose: Teach foundational programming concepts through structured modules
scope: 3 modules covering basics, control flow, and functions

# Learning path metadata
learning_path:
  entry_state: v:student:beginner
  exit_states:
    - v:student:programmer

prerequisites:
  entry_skills:
    - v:skill:basic-computer-literacy

outcomes:
  developed_skills:
    - v:skill:python-basics
    - v:skill:control-flow
    - v:skill:function-design

# Elements comprising this chart
elements:
  vertices: [...]
  edges: [...]
  faces: [...]

tags:
  - chart
  - syllabus
  - programming
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
---
```

## Required Body Sections

All sections from `chart/chart` specification PLUS syllabus-specific sections:

### 1. Purpose (from chart spec)

### 2. Structure (ENHANCED)

Must document vertices, edges, and faces with **syllabus-specific categorization**:

#### Vertices (categorized by type)

**Students (minimum 2):**
- Initial state(s) - entry point(s) for syllabus
- Intermediate state(s) - states between modules (if multi-module)
- Completion state(s) - exit point(s) after completing syllabus

**Skills (minimum 1):**
- Entry prerequisites - skills required to start
- Developed skills - skills gained through modules

**Modules (minimum 1):**
- Learning units with prerequisites and outcomes

#### Edges (categorized by relationship type)

**Possession edges (has-skill):**
- student → skill relationships

**Requirement edges (requires-skill):**
- module → skill prerequisites

**Development edges (develops-skill):**
- module → skill learning outcomes

**Learning edges:**
- studies: student → module (engagement)
- transitions-to: student → student (state progression)
- advances: module → student (advancement - in completion faces only)

#### Faces (categorized by semantic type)

**Prerequisite faces:**
- Pattern: `(student, skill, module)`
- Count: For each student-module pair, one per required skill
- Purpose: Validates student has skills module requires

**Completion faces:**
- Pattern: `(student-before, module, student-after)`
- Count: One per module completion path
- Purpose: Represents state transition through module

**Skill-gain faces:**
- Pattern: `(student-after, module, skill)`
- Count: For each completion, one per developed skill
- Purpose: Represents causal skill acquisition

### 3. Topological Properties (from chart spec)

Must calculate and document V, E, F, and χ

### 4. Learning Path Structure (NEW - required for syllabus)

Must document the progression structure:

```markdown
## Learning Path Structure

### Entry Point
- **Initial State:** [student vertex]
- **Entry Skills:** [prerequisite skills list]

### Module Sequence
[For each module, document:]
- **Module:** [module name]
- **Prerequisites:** [required skills]
- **Develops:** [outcome skills]
- **Input States:** [student states that can study this]
- **Output States:** [student states after completion]

### Exit Points
- **Completion States:** [final student states]
- **Total Skills Gained:** [all developed skills]
```

### 5. Constraint Validation (NEW - required for syllabus)

Must validate and document compliance with local constraints:

```markdown
## Constraint Validation

### Prerequisite Constraints
For each completion face, validate:
- ✓ Student-before has all required skills (prerequisite faces exist)
- ✓ Prerequisite faces use correct edges (has-skill, requires-skill, studies)

### Skill Accumulation Constraints
For each completion face, validate:
- ✓ student-after.skills ⊇ student-before.skills (supermodular)
- ✓ student-after.skills = student-before.skills ∪ module.develops-skills
- ✓ |student-after.skills| ≥ |student-before.skills| (monotonic)

### Skill Attribution Constraints
For each skill-gain face, validate:
- ✓ Module develops the skill (develops-skill edge exists)
- ✓ Student has the skill (has-skill edge exists)
- ✓ Completion face exists (advances edge from completion)

### Acyclic Progression Constraint
- ✓ transitions-to edges form DAG (no cycles)
- ✓ No student transitions to state with fewer skills
```

### 6. Expected Tool Behavior (from chart spec)

## Local Constraint Rules

Syllabus charts MUST satisfy these local constraints:

### Vertex Type Constraints

1. **Student vertices** (`vertex/student`):
   - Minimum count: 2
   - Each represents discrete learning state with skill set
   - Must include at least one entry state and one exit state

2. **Skill vertices** (`vertex/skill`):
   - Minimum count: 1
   - Represents capabilities possessed or developed
   - Entry prerequisites + developed skills

3. **Module vertices** (`vertex/learning-module`):
   - Minimum count: 1
   - Each has prerequisite skills and developed skills
   - Forms transformation: prerequisites → outcomes

### Edge Type Constraints

1. **has-skill edges** (student → skill):
   - Required for all student skill possessions
   - Used in prerequisite and skill-gain faces

2. **requires-skill edges** (module → skill):
   - Required for all module prerequisites
   - Used in prerequisite faces

3. **develops-skill edges** (module → skill):
   - Required for all module learning outcomes
   - Used in skill-gain faces

4. **studies edges** (student → module):
   - Required for student-module engagement
   - Used in prerequisite and completion faces

5. **transitions-to edges** (student → student):
   - Required for state transitions
   - MUST form directed acyclic graph (DAG)
   - Used in completion faces

6. **advances edges** (module → student):
   - Required ONLY in completion faces
   - Closes completion face triangle
   - One per module → student-after transition

### Face Type Constraints

1. **Prerequisite faces** `(student, skill, module)`:
   - **Count:** For student S studying module M requiring skills {R₁, R₂, ...Rₙ}, create n prerequisite faces
   - **Boundary edges:**
     - `e:has-skill:S:Rᵢ` (student has skill)
     - `e:requires-skill:M:Rᵢ` (module requires skill)
     - `e:studies:S:M` (student studies module)
   - **Validation:** All three edges must exist

2. **Completion faces** `(student-before, module, student-after)`:
   - **Count:** One per module completion path
   - **Boundary edges:**
     - `e:studies:student-before:module`
     - `e:transitions-to:student-before:student-after`
     - `e:advances:module:student-after`
   - **Validation:**
     - Prerequisite faces exist for all required skills
     - student-after.skills = student-before.skills ∪ module.develops-skills
     - |student-after.skills| ≥ |student-before.skills|

3. **Skill-gain faces** `(student-after, module, skill)`:
   - **Count:** For completion of module M developing skills {D₁, D₂, ...Dₘ} to student-after, create m skill-gain faces
   - **Boundary edges:**
     - `e:advances:module:student-after` (from completion face)
     - `e:has-skill:student-after:Dᵢ` (student has skill)
     - `e:develops-skill:module:Dᵢ` (module develops skill)
   - **Validation:** Completion face must exist for this module → student-after

### Completeness Constraints

1. **All vertices in elements.vertices must be referenced in at least one face**
2. **All edges in elements.edges must be referenced in at least one face** (except standalone structural edges)
3. **Entry state must have has-skill edges for all entry_skills**
4. **Exit states must have has-skill edges for all developed_skills in their path**

### Cardinality Formulas

For syllabus with:
- M modules
- S student states
- K skills total (entry + developed)
- Module i requiring rᵢ skills and developing dᵢ skills

Minimum face counts:
- **Prerequisite faces:** Σ(students studying module i) × rᵢ
- **Completion faces:** Σ(distinct student transitions via module i)
- **Skill-gain faces:** Σ(completion faces for module i) × dᵢ

## Multi-Module Patterns

### Sequential Modules

```
Module A → Intermediate State → Module B

Constraints:
- Module B prerequisites ⊆ (entry skills ∪ Module A outcomes)
- Intermediate state.skills = entry state.skills ∪ Module A.develops
- Completion face A: (entry, module-A, intermediate)
- Prerequisite faces B validate intermediate.skills ⊇ module-B.requires
- Completion face B: (intermediate, module-B, exit)
```

### Branching Paths

```
Same entry, different module choices:

Constraints:
- Modules may require same or different prerequisites
- Different developed skills
- Multiple completion faces from same student-before
- Different exit states (or same if skills converge)
```

### Convergent Paths

```
Different entries, same exit:

Constraints:
- Different initial skill sets
- Different modules or module sequences
- Exit state has union of all skills from both paths
- Multiple transitions-to edges to same exit state
```

## Quality Criteria

A well-formed syllabus chart:

1. **Completeness:** All required faces exist per cardinality formulas
2. **Consistency:** Skill sets computed via faces match student vertex documentation
3. **Validity:** All local constraints satisfied
4. **Acyclic:** No cycles in student state transitions
5. **Traceable:** Clear path from entry to exit states
6. **Minimal:** No redundant faces or edges

## Anti-Patterns

### Invalid Skill Accumulation

```yaml
# INVALID: Student loses skills
student-before.skills = {A, B, C}
module.develops = {D}
student-after.skills = {A, D}  # Lost B and C!
❌ Violates supermodular constraint
```

### Missing Prerequisite Faces

```yaml
# INVALID: Module requires skill but no prerequisite face
module.requires = {skill-X}
student.studies = module
# But no prerequisite face (student, skill-X, module)
❌ Constraint validation incomplete
```

### Circular Student Progression

```yaml
# INVALID: Cycle in state transitions
student-A --transitions-to--> student-B
student-B --transitions-to--> student-C
student-C --transitions-to--> student-A
❌ Violates acyclic constraint
```

### Orphan Skill-Gain Face

```yaml
# INVALID: Skill-gain without completion
(student-X, module-Y, skill-Z) skill-gain face exists
# But no completion face (student-W, module-Y, student-X)
❌ No advances edge to close boundary
```

## Verification

Syllabus charts can be verified using:

```bash
# Standard chart verification
python scripts/verify_chart.py charts/<syllabus>/<syllabus>.md

# Topology analysis
python scripts/topology.py charts/<syllabus>/<syllabus>.md

# Syllabus-specific validation (if implemented)
python scripts/validate_syllabus.py charts/<syllabus>/<syllabus>.md
```

## Visualization

**Required:** Syllabus charts MUST include visualization guidance in the Expected Tool Behavior section.

### Recommended Visualizer

Use the specialized syllabus visualizer for learning journey charts:

```bash
# Export chart to JSON
python scripts/export_chart_direct.py charts/<syllabus>/<syllabus>.md charts/<syllabus>/<syllabus>.json --root .

# Generate interactive 3D visualization with semantic color coding
python scripts/visualize_syllabus.py charts/<syllabus>/<syllabus>.json
```

**Output:** Interactive HTML file (`charts/<syllabus>/<syllabus>.html`) with:

- **Color-coded vertices:** Students (blue), Skills (green), Modules (purple)
- **Color-coded edges:** Relationship types (has-skill, requires-skill, develops-skill, studies, transitions-to, advances)
- **Color-coded faces:** Prerequisite (orange), Completion (blue), Skill-gain (dark green)
- **Interactive legends:** Vertex types, edge types, face types with descriptions
- **Topology info:** V, E, F, χ values with learning path metadata
- **3D navigation:** Rotate, zoom, pan to inspect learning journey structure

### Visualization Benefits

The specialized visualizer enables:

- **Visual prerequisite validation:** Orange triangles show which skills students must have
- **State transition flow:** Blue triangles show student progression through modules
- **Skill acquisition causality:** Green triangles show skill gains from module completion
- **Learning path clarity:** Color patterns reveal entry → modules → exit progression
- **Topological inspection:** Identify missing faces, orphan vertices, or constraint violations visually

---

**Note:** This specification extends chart/chart with learning-journey-specific structure and constraints. Syllabus charts use simplicial topology to encode prerequisite validation, skill accumulation, and state-based learning progression through local constraint checking.
