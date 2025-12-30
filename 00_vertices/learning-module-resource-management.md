---
type: vertex/learning-module
extends: doc
id: v:learning-module:resource-management
name: Resource Management
description: Module teaching management chart architecture with resource, function, and team vertices for modeling organizational resource flows
tags:
  - vertex
  - doc
  - learning-module
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: advanced
dependencies: []
---

# Resource Management

## Purpose

This module teaches students to extend coordination charts with resource and function modeling. Students learn to create resource and function vertex types, define flow edges (operates, produces, consumes), and build concrete management charts that reveal cross-team resource dependencies. The module emphasizes how tangled input/output relationships create rich topologies that expose peer team relationships.

**Educational Content:** [module-09.md](../module-09.md)

## Learning Objectives

After completing this module, students will be able to:

- Create resource vertex type for things that flow between functions
- Create function vertex type for operations with inputs and outputs
- Define operates edge (team→function) with exactly 1 team per function constraint
- Define produces edge (function→resource) for outputs
- Define consumes edge (function→resource) for inputs
- Define resource dependency faces with correct boundary edge requirements
- Build concrete management chart with 2 teams, 3 functions, 3 resources
- Design tangled dependency structures where teams have mutual resource needs
- Identify where resource dependency faces cut across team boundaries
- Recognize peer team relationships from topology
- Generate and interpret management chart visualizations

## Prerequisite Skills

**Required:**
- [[v:skill:team-coordination]] - Must understand coordination charts before adding resource flows

**Module Prerequisites:**
- Students must have completed [[v:learning-module:team-coordination]] (Module 08)
- Familiarity with staff, team, role vertices and coordination chart patterns is essential

## Module Content

### Section 1: From Coordination to Management (45 min)

**Goal:** Understand how management charts extend coordination charts

1. **Review coordination charts**
   - Vertices: staff, team, role
   - Edges: member, qualified, includes
   - Faces: assignment (staff, role, team)
   - Purpose: Model responsibility structures

2. **Introduce management charts**
   - Add: resource vertices (things that flow)
   - Add: function vertices (operations)
   - Add: flow edges (operates, produces, consumes)
   - Purpose: Model operational resource flows

3. **Key insight: Tangled dependencies**
   - Unlike syllabus input/output rules with clear directionality
   - Resource flows can be circular or mutual
   - Creates peer relationships between teams
   - Richer topology than coordination alone

4. **Exercise:** Identify resources and functions in a familiar system

### Section 2: Resource and Function Vertices (60 min)

**Goal:** Create resource and function vertex types

1. **Create resource vertex type**
   - Purpose: Things that flow between functions
   - Extends: vertex (or property)
   - Examples: GUI, API, database, document, artifact
   - Key property: Can be produced and consumed
   - Write: `spec-for-resource.md`, `guidance-for-resource.md`

2. **Create function vertex type**
   - Purpose: Operations that transform resources
   - Extends: vertex
   - Examples: UI dev, business logic design, data engineering
   - Key properties: Has inputs (consumes), has outputs (produces), operated by team
   - Write: `spec-for-function.md`, `guidance-for-function.md`

3. **Relationship to coordination types**
   - Teams (from Module 08) operate functions
   - Resources bridge between functions (and thus teams)
   - Staff don't directly appear in management charts (abstracted to team level)

4. **Verify type definitions**
   - Run `verify_template_based.py` on all 4 documents

5. **Exercise:** Create spec for resource or function type

### Section 3: Flow Edges (60 min)

**Goal:** Define edges that connect teams, functions, and resources

1. **Operates edge (team→function)**
   - Purpose: Team is responsible for operating a function
   - Source type: team
   - Target type: function
   - Constraint: Exactly 1 team per function
   - Semantics: "Frontend team operates UI dev function"
   - Write: `spec-for-operates-edge.md`, `guidance-for-operates-edge.md`

2. **Produces edge (function→resource)**
   - Purpose: Function produces a resource as output
   - Source type: function
   - Target type: resource
   - Semantics: "UI dev produces GUI"
   - Write: `spec-for-produces-edge.md`, `guidance-for-produces-edge.md`

3. **Consumes edge (function→resource)**
   - Purpose: Function consumes a resource as input
   - Source type: function
   - Target type: resource
   - Semantics: "UI dev consumes API"
   - Write: `spec-for-consumes-edge.md`, `guidance-for-consumes-edge.md`

4. **Edge type summary**
   ```
   team --operates--> function
   function --produces--> resource
   function --consumes--> resource
   ```

5. **Exercise:** Write spec for one edge type with proper constraints

### Section 4: Resource Dependency Faces (45 min)

**Goal:** Define faces that capture cross-team resource flows

1. **Resource dependency face structure**
   - Type: face/resource-dependency
   - Vertices: (function-producer, resource, function-consumer)
   - Or: (team, function, resource) for ownership context

2. **Boundary edge requirements**
   - Option 1 (function-centric): produces + consumes + (implicit function relationship)
   - Option 2 (team-centric): operates + produces/consumes

3. **Cross-team significance**
   - When producer-function and consumer-function have different operating teams
   - The face represents a cross-team dependency
   - These are coordination points requiring communication

4. **Write face spec and guidance**
   - `spec-for-resource-dependency-face.md`
   - `guidance-for-resource-dependency-face.md`

5. **Exercise:** Identify boundary edges for a resource dependency face

### Section 5: Building the Management Chart (90 min)

**Goal:** Build concrete management chart and visualize it

1. **Define the example scenario**
   - 2 teams: frontend, backend
   - 3 resources: GUI, API, database
   - 3 functions: UI dev, business logic design, data engineering

2. **Assign functions to teams**
   - Frontend operates: UI dev
   - Backend operates: business logic design, data engineering

3. **Define production relationships**
   - UI dev produces: GUI
   - Business logic design produces: API
   - Data engineering produces: database

4. **Define consumption relationships (the tangled part)**
   - UI dev consumes: API, database
   - Business logic design consumes: GUI, database
   - Data engineering consumes: (none, or could consume API for migrations)

5. **Observe the peer relationship**
   - Frontend needs API and database (from Backend)
   - Backend needs GUI (from Frontend)
   - Neither team is purely upstream or downstream
   - They are peers with mutual dependencies

6. **Create edges**
   - Operates edges: 3 (one per function)
   - Produces edges: 3 (one per function-resource output)
   - Consumes edges: 4+ (multiple inputs per function)

7. **Create resource dependency faces**
   - One face per cross-team resource flow
   - Count: Multiple faces cutting across the frontend/backend boundary

8. **Write chart document**
   - `charts/management-example/management-example.md`
   - List all vertices, edges, faces
   - Calculate topology: V, E, F, χ

9. **Visualize and interpret**
   - Run export and visualization scripts
   - Open visualization, observe topology
   - Identify: Where do resource dependencies concentrate?
   - Identify: Which faces cross team boundaries?

10. **Exercise:** Add a third team and observe topology change

### Section 6: Comparing Coordination and Management (30 min)

**Goal:** Understand the relationship between the two chart types

1. **Coordination chart focus**
   - People (staff) and responsibilities (roles)
   - Who does what on which team
   - RACI-style accountability

2. **Management chart focus**
   - Functions and resources
   - What produces what, what consumes what
   - Operational dependencies

3. **Shared element: Team**
   - Teams appear in both chart types
   - This is the glue for composition in Module 10

4. **Topological differences**
   - Coordination: faces are assignments (staff-role-team)
   - Management: faces are resource dependencies (function-resource-function or team-function-resource)
   - Management tends to have more tangled structure

5. **Exercise:** Sketch how coordination and management charts could be composed

## Estimated Time

**Total:** 5.5-6.5 hours

- Section 1 (Coordination to Management): 45 min
- Section 2 (Resource and Function): 60 min
- Section 3 (Flow Edges): 60 min
- Section 4 (Dependency Faces): 45 min
- Section 5 (Management Chart): 90 min
- Section 6 (Comparison): 30 min
- Exercises (integrated): ~45 min
- Assessment: ~30 min

## Resources

**Required:**
- Module 08 types: team, staff, role, coordination chart
- Template files: `templates/00_vertices/`, `templates/01_edges/`, `templates/02_faces/`
- Verification script: `scripts/verify_template_based.py`
- Export script: `scripts/export_chart_direct.py`
- Visualization script: `scripts/visualize_chart.py`

**Optional:**
- Data flow diagram notation
- Supply chain modeling
- Input-output economics

## Success Criteria

Students have successfully completed this module when they can:

- **Create vertex types:** Create resource and function vertex types (verification passes)
- **Define edges:** Create operates, produces, consumes edge types (verification passes)
- **Define faces:** Create resource dependency face type (verification passes)
- **Build chart:** Create management chart with 2 teams, 3 functions, 3 resources (topology correct)
- **Enforce constraints:** Verify exactly 1 team operates each function (constraint check)
- **Identify dependencies:** Find resource flows that cross team boundaries (analysis)
- **Recognize peers:** Identify mutual team dependencies from topology (interpretation)
- **Visualize:** Generate and interpret management chart visualization (visual inspection)

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:resource-management]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section exercises: Type creation, edge definition, face identification (self-check, peer review)
- Verification runs: All new documents pass template verification (automated)
- Chart construction: Incremental building with topology checks (instructor feedback)

**Summative (End of Module):**
- **Type creation:** Create all required vertex, edge, face types (verification)
- **Management chart:** Build complete chart with correct topology (correctness check)
- **Dependency analysis:** Identify cross-team resource flows (rubric-graded)
- **Visualization:** Generate visualization and explain peer relationships (rubric-graded)

---

**Note:** This module adds resource flow modeling to coordination capabilities. Students achieving [[v:skill:resource-management]] reach the [[v:student:management-architect]] state, prepared for chart composition and Hodge analysis in Module 10.
