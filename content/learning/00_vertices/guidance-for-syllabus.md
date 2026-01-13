---
type: vertex/guidance
extends: vertex/doc
id: v:guidance:syllabus
name: Guidance for Creating Syllabus Charts
description: Best practices and workflow for designing and validating syllabus chart documents representing learning journeys
tags:
  - vertex
  - guidance
  - chart-type
  - syllabus
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies:
  - v:guidance:chart
---

# Guidance for Creating Syllabus Charts

## Purpose

This guidance provides practical workflow and best practices for creating syllabus chart documents that satisfy [[v:spec:syllabus]]. Use this when designing learning journeys with prerequisite validation and skill accumulation tracking.

## When to Use Syllabus Charts

**Use syllabus charts when:**
- Designing structured learning paths with prerequisites
- Tracking skill accumulation across modules
- Validating that students have required knowledge before studying
- Representing state-based learning progression
- Encoding causal relationships (module completion → skill acquisition)

**Don't use syllabus charts for:**
- Unstructured knowledge graphs without learning progression
- Non-educational simplicial complexes
- Charts without prerequisite/skill concepts
- Generic relationship networks (use standard charts instead)

## Quality Criteria

### Completeness

**Good syllabus charts have:**
- ✅ All prerequisite faces for all student-module-skill combinations
- ✅ Completion faces for all module transitions
- ✅ Skill-gain faces for all developed skills
- ✅ Entry and exit states clearly defined
- ✅ All vertices participate in at least one face

**Avoid:**
- ❌ Missing prerequisite validation faces
- ❌ Orphan vertices not in any face
- ❌ Skill-gain faces without corresponding completion faces
- ❌ Modules without develops-skill edges

### Consistency

**Good syllabus charts have:**
- ✅ Student skill sets match face computations
- ✅ Module prerequisites align with prerequisite faces
- ✅ Developed skills match skill-gain faces
- ✅ Acyclic student state progression

**Avoid:**
- ❌ Student vertex documentation contradicts face structure
- ❌ Skill accumulation violations (losing skills)
- ❌ Circular student transitions
- ❌ Prerequisite faces for non-existent requirements

### Clarity

**Good syllabus charts have:**
- ✅ Clear learning path from entry to exit
- ✅ Well-named student states (beginner, intermediate, expert)
- ✅ Descriptive skill names
- ✅ Module sequence documentation
- ✅ Constraint validation section showing compliance

**Avoid:**
- ❌ Ambiguous student state names
- ❌ Unclear progression paths
- ❌ Missing learning path structure section
- ❌ Undocumented branching or convergent paths

## Workflow

### Phase 1: Design Learning Path (60-90 minutes)

**Step 1.1: Define Learning Outcomes**
- Identify skills students should gain
- Determine entry prerequisites
- List all developed skills

**Step 1.2: Design Module Sequence**
- Break curriculum into modules
- For each module, define:
  - Required prerequisite skills
  - Developed outcome skills
  - Estimated learning time
- Ensure logical prerequisite ordering

**Step 1.3: Define Student States**
- Create entry state (initial skill set)
- Create intermediate states (after each module)
- Create exit state(s) (final skill sets)
- Verify skill accumulation: each state ⊇ previous state

**Example:**
```
Entry: beginner {computer-literacy}
After Module 1: novice-programmer {computer-literacy, python-basics}
After Module 2: programmer {computer-literacy, python-basics, control-flow}
```

### Phase 2: Create Vertices (30-45 minutes)

**Step 2.1: Create Student Vertices**
- Use spec-for-student to create each state
- Document skill set for each state
- Link to prerequisite skills (has-skill edges conceptually)

**Step 2.2: Create Skill Vertices**
- Use spec-for-skill for each skill
- Distinguish entry prerequisites vs developed skills
- Document acquisition method

**Step 2.3: Create Module Vertices**
- Use spec-for-learning-module for each module
- Document prerequisite skills
- Document developed skills
- List learning objectives

### Phase 3: Create Edges (45-60 minutes)

**Step 3.1: Create Possession Edges (has-skill)**
- For each student state, create has-skill edge to each possessed skill
- Entry state → entry prerequisites
- Intermediate states → accumulated skills
- Exit states → all entry + developed skills

**Step 3.2: Create Requirement Edges (requires-skill)**
- For each module, create requires-skill edge to each prerequisite
- Foundational modules may have zero requires-skill edges

**Step 3.3: Create Development Edges (develops-skill)**
- For each module, create develops-skill edge to each outcome skill
- Every module must develop at least one skill

**Step 3.4: Create Learning Edges**
- **studies:** student-before → module for each completion
- **transitions-to:** student-before → student-after for each module completion
- **advances:** module → student-after for each completion (created with completion face)

**Verification checkpoint:** Run `python scripts/build_cache.py` to ensure all edges parse correctly.

### Phase 4: Create Faces (60-90 minutes)

**Step 4.1: Create Prerequisite Faces**

For each (student, module) pair where student studies module:
- For each skill in module.requires-skills:
  - Create face (student, skill, module)
  - Boundary: has-skill, requires-skill, studies
  - Validates: student has the required skill

**Cardinality check:**
```
prerequisite_faces = Σ(students × modules × required_skills)
```

**Step 4.2: Create Completion Faces**

For each module completion:
- Create face (student-before, module, student-after)
- Boundary: studies, transitions-to, advances
- Validates: state transition with skill accumulation

**Create advances edge:** When creating completion face, also create the advances edge (module → student-after) that forms the third boundary.

**Cardinality check:**
```
completion_faces = number of distinct student transitions
```

**Step 4.3: Create Skill-Gain Faces**

For each completion face:
- For each skill in module.develops-skills:
  - Create face (student-after, module, skill)
  - Boundary: advances (from completion), has-skill, develops-skill
  - Validates: student gains skill from module

**Cardinality check:**
```
skill_gain_faces = Σ(completion_faces × developed_skills)
```

**Verification checkpoint:** Run `python scripts/verify_chart.py charts/<syllabus>/<syllabus>.md` to verify face boundaries.

### Phase 5: Create Chart Document (45-60 minutes)

**Step 5.1: Write Frontmatter**
- Set type to `chart/syllabus`
- Add learning_path metadata (entry/exit states)
- Add prerequisites metadata (entry skills)
- Add outcomes metadata (developed skills)
- List all vertices, edges, faces in elements section

**Step 5.2: Write Body**
- Purpose section: Why this syllabus exists
- Structure section: Categorize vertices/edges/faces by type
- Topological Properties: Calculate V, E, F, χ
- **Learning Path Structure:** Document progression (NEW)
- **Constraint Validation:** Validate all local constraints (NEW)
- Expected Tool Behavior: Verification commands

**Step 5.3: Validate Constraints**

In Constraint Validation section, explicitly check:

```markdown
## Constraint Validation

### Prerequisite Constraints
For completion face (student-A, module-X, student-B):
- Prerequisite face (student-A, skill-1, module-X)? ✓
- Prerequisite face (student-A, skill-2, module-X)? ✓
- All prerequisites validated

### Skill Accumulation
- student-A.skills = {skill-1, skill-2}
- module-X.develops = {skill-3}
- student-B.skills = {skill-1, skill-2, skill-3}
- student-B.skills ⊇ student-A.skills? ✓
- student-B.skills = student-A ∪ module-X.develops? ✓

### Skill Attribution
For skill-gain face (student-B, module-X, skill-3):
- module-X develops skill-3? ✓
- student-B has skill-3? ✓
- Completion face exists? ✓
```

### Phase 6: Verification and Refinement (30-45 minutes)

**Step 6.1: Run Verification Tools**

```bash
# Build cache
python scripts/build_cache.py

# Verify chart structure
python scripts/verify_chart.py charts/<syllabus>/<syllabus>.md --root .

# Analyze topology
python scripts/topology.py charts/<syllabus>/<syllabus>.md --root .

# Export to JSON
python scripts/export_chart_direct.py charts/<syllabus>/<syllabus>.md charts/<syllabus>/<syllabus>.json --root .

# Generate specialized syllabus visualization
python scripts/visualize_syllabus.py charts/<syllabus>/<syllabus>.json
```

**Expected output:** Interactive HTML file with semantic color coding:

- **Students** (blue vertices) - Learning states
- **Skills** (green vertices) - Capabilities to acquire
- **Modules** (purple vertices) - Learning units
- **Prerequisite faces** (orange triangles) - Skill validation
- **Completion faces** (blue triangles) - State transitions
- **Skill-gain faces** (dark green triangles) - Skill acquisition

**Step 6.2: Visual Inspection**

Open the generated HTML file in a browser and verify:

- **Prerequisite validation:** Orange triangles correctly connect students → skills → modules
- **State transitions:** Blue triangles show student-before → module → student-after progression
- **Skill acquisition:** Green triangles show student-after → module → developed-skill causality
- **Learning path flow:** Color patterns reveal clear entry → modules → exit progression
- **Topology correctness:** No orphan vertices, all faces properly formed
- **Edge semantics:** Edges colored by type (has-skill, requires-skill, develops-skill, studies, transitions-to, advances)

**Step 6.3: Constraint Audit**
- Check all prerequisite faces exist
- Verify skill accumulation is supermodular
- Confirm no cycles in transitions-to edges
- Validate cardinality formulas

## Common Pitfalls

### 1. Missing Prerequisite Faces

**Problem:** Module requires skill but no prerequisite face validates student has it.

**Fix:** For each module requiring N skills studied by M students, create N × M prerequisite faces.

### 2. Incorrect Skill Accumulation

**Problem:** Student-after has fewer skills than student-before.

**Fix:** Ensure student-after.skills = student-before.skills ∪ module.develops-skills (union, not replacement).

### 3. Orphan Skill-Gain Faces

**Problem:** Skill-gain face without corresponding completion face.

**Fix:** Skill-gain faces require advances edge from completion face. Create completion face first.

### 4. Circular Student Progression

**Problem:** Student states form cycle (A → B → C → A).

**Fix:** Student transitions must be acyclic. Redraw progression as DAG.

### 5. Advances Edge Misuse

**Problem:** Advances edge used outside completion faces.

**Fix:** Advances edges ONLY exist within completion faces. Don't create standalone.

### 6. Wrong Face Vertex Order

**Problem:** Face vertices in wrong positions.

**Fix:**
- Prerequisite: (student, skill, module)
- Completion: (student-before, module, student-after)
- Skill-gain: (student-after, module, skill)

## Design Patterns

### Single Module Syllabus

```yaml
Vertices: 2 students, N skills, 1 module
Edges: has-skill, requires-skill, develops-skill, studies, transitions-to, advances
Faces:
  - Prerequisite: R faces (R = required skills)
  - Completion: 1 face
  - Skill-gain: D faces (D = developed skills)

χ = 2 + N + 1 - (edges) + (R + 1 + D)
```

**Example:** learning-journey-module-01
- 2 students, 3 skills, 1 module
- 11 edges
- 2 prerequisite + 1 completion + 1 skill-gain = 4 faces
- χ = 6 - 11 + 4 = -1

### Sequential Multi-Module Syllabus

```yaml
Vertices: (M+1) students, K skills, M modules
Pattern: Entry → Module1 → Intermediate → Module2 → ... → Exit

For each module i:
  - Prerequisite faces: students × required_skills_i
  - Completion face: 1
  - Skill-gain faces: developed_skills_i

Total faces ≈ Σ(prerequisite + completion + skill-gain per module)
```

### Branching Syllabus

```yaml
Vertices: Entry + multiple paths + multiple exits
Pattern: Entry → {Path A, Path B} → {Exit A, Exit B}

Students can choose modules based on interests
Different skill outcomes per path
Multiple completion faces from same entry state
```

## Best Practices

1. **Start with Entry/Exit:** Define initial and final states first, then fill in the path
2. **Document as you build:** Don't wait until the end to write documentation
3. **Verify incrementally:** Run verification after adding vertices, edges, faces
4. **Use templates:** All edge/face types have templates - use them
5. **Check cardinality:** Use formulas to ensure you haven't missed faces
6. **Visualize early:** Generate HTML to spot structural issues
7. **Validate constraints explicitly:** Don't assume - check and document in Constraint Validation section

## Estimated Time

**First syllabus chart (learning curve):** 5-7 hours
- Phase 1 (Design): 90 minutes
- Phase 2 (Vertices): 45 minutes
- Phase 3 (Edges): 60 minutes
- Phase 4 (Faces): 90 minutes
- Phase 5 (Chart doc): 60 minutes
- Phase 6 (Verification): 45 minutes

**Subsequent syllabi (familiar with process):** 3-4 hours
- Phases become faster with practice
- Template reuse accelerates creation
- Verification becomes routine

**Single-module syllabus:** 2-3 hours (simpler structure)

## Tools and Scripts

- `verify_chart.py`: Validates simplicial complex structure
- `topology.py`: Calculates Euler characteristic and identifies holes
- `build_cache.py`: Parses all elements into complex.json
- `export_chart_direct.py`: Exports to JSON for visualization
- `visualize_syllabus.py`: **Specialized syllabus visualizer** with semantic color coding for learning journeys (recommended)
- `visualize_chart.py`: General chart visualizer
- `verify_template_based.py`: Validates individual documents against templates

## Example Reference

See [[c:learning-journey-module-01]] for a complete single-module syllabus demonstrating all patterns and constraints.

---

**Note:** This guidance extends [[v:guidance:chart]] with syllabus-specific workflow emphasizing prerequisite validation, skill accumulation, and local constraint checking. Follow this workflow to create well-formed learning journey representations.
