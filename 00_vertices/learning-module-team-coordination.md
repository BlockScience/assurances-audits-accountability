---
type: vertex/learning-module
extends: doc
id: v:learning-module:team-coordination
name: Team Coordination
description: Module teaching coordination chart architecture with staff, team, and role vertices for modeling organizational responsibility structures
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

# Team Coordination

## Purpose

This module teaches students to extend the type system and build coordination charts that model organizational responsibility structures. Students learn to create new vertex types (actor, property, team, staff, role), define coordination-specific edges and faces, and build concrete coordination charts like RACI matrices. The module emphasizes streamlined end-to-end practice: define the types, then immediately build a working chart and visualize it.

**Educational Content:** [module-08.md](../module-08.md)

## Learning Objectives

After completing this module, students will be able to:

- Extend vertex type to create actor and property base types
- Create spec-guidance pairs for new vertex types following established patterns
- Define team and staff as subtypes of actor
- Define role as a subtype of property with actor-binding constraint
- Create coordination chart type restricted to staff, team, and role vertices
- Define member edge (staff→team) with proper semantics
- Define qualified edge (staff→role) with proper semantics
- Define includes edge (team→role) with proper semantics
- Define assignment face (staff, role, team) with correct boundary edge requirements
- Build concrete RACI coordination chart with 4 roles, 5 staff, 2 teams
- Enforce constraint: exactly 1 accountable per team
- Design meaningful team overlap (shared consults/informs, appropriate resource distribution)
- Generate and interpret coordination chart visualizations
- Commit new type definitions to the registry

## Prerequisite Skills

**Required:**
- [[v:skill:reference-reuse]] - Must understand doc-kit pattern for creating reusable type definitions

**Module Prerequisites:**
- Students must have completed [[v:learning-module:reference-reuse]] (Module 07)
- Familiarity with spec-guidance pairs, type extension, and registry patterns is essential

## Module Content

### Section 1: Extending the Type System (60 min)

**Goal:** Create actor and property base vertex types

1. **Review type extension pattern**
   - Vertex types inherit from vertex or other vertex types
   - Each type needs spec (structural requirements) + guidance (quality criteria)
   - Types can be extended further to create subtypes

2. **Create actor vertex type**
   - Purpose: Entities that can perform actions and hold responsibilities
   - Extends: vertex
   - Key properties: Can possess properties, can be assigned roles
   - Write: `spec-for-actor.md` following spec-for-vertex pattern
   - Write: `guidance-for-actor.md` following guidance-for-vertex pattern

3. **Create property vertex type**
   - Purpose: Attributes that can belong to actors
   - Extends: vertex
   - Key properties: Can be possessed by actors, represents capabilities or roles
   - Write: `spec-for-property.md` following spec-for-vertex pattern
   - Write: `guidance-for-property.md` following guidance-for-vertex pattern

4. **Verify both type pairs**
   - Run `verify_template_based.py` on all 4 documents
   - Ensure they pass before proceeding

5. **Exercise:** Create spec-guidance pair for actor or property type

### Section 2: Actor Subtypes - Team and Staff (60 min)

**Goal:** Create team and staff vertex types extending actor

1. **Create team vertex type**
   - Purpose: Group of staff members working together
   - Extends: actor
   - Key properties: Has members (staff), includes roles, operates functions (future)
   - Constraint: Teams can have roles assigned to them
   - Write: `spec-for-team.md` extending spec-for-actor
   - Write: `guidance-for-team.md` extending guidance-for-actor

2. **Create staff vertex type**
   - Purpose: Individual person in an organization
   - Extends: actor
   - Key properties: Can be member of teams, can be qualified for roles
   - Constraint: Staff are the atomic actors (not further decomposed)
   - Write: `spec-for-staff.md` extending spec-for-actor
   - Write: `guidance-for-staff.md` extending guidance-for-actor

3. **Type hierarchy so far**
   ```
   vertex
   └── actor
       ├── team
       └── staff
   └── property
       └── role (next section)
   ```

4. **Verify all type pairs**
   - Run verification on all 4 new documents
   - Check inheritance relationships are correct

5. **Exercise:** Verify team and staff specs inherit properly from actor

### Section 3: Property Subtype - Role (45 min)

**Goal:** Create role vertex type with actor-binding constraint

1. **Create role vertex type**
   - Purpose: A responsibility or function that can be assigned to actors
   - Extends: property
   - Key properties: Can belong to staff (qualified), can be included by teams
   - RACI roles: responsible, accountable, consulted, informed
   - Constraint: Roles make sense only in context of actors

2. **Write role spec and guidance**
   - `spec-for-role.md` extending spec-for-property
   - `guidance-for-role.md` extending guidance-for-property
   - Include constraint: roles are assigned to actors

3. **Complete type hierarchy**
   ```
   vertex
   └── actor
   │   ├── team
   │   └── staff
   └── property
       └── role
   ```

4. **Exercise:** Write spec-for-role with RACI role examples

### Section 4: Coordination Edges (60 min)

**Goal:** Define edges that connect staff, teams, and roles

1. **Member edge (staff→team)**
   - Purpose: Staff belongs to a team
   - Source type: staff
   - Target type: team
   - Semantics: "Alice is a member of Frontend team"
   - Write: `spec-for-member-edge.md`, `guidance-for-member-edge.md`

2. **Qualified edge (staff→role)**
   - Purpose: Staff is qualified for a role
   - Source type: staff
   - Target type: role
   - Semantics: "Alice is qualified as Responsible"
   - Write: `spec-for-qualified-edge.md`, `guidance-for-qualified-edge.md`

3. **Includes edge (team→role)**
   - Purpose: Team includes a role in its structure
   - Source type: team
   - Target type: role
   - Semantics: "Frontend team includes Accountable role"
   - Constraint: Exactly 1 accountable per team
   - Write: `spec-for-includes-edge.md`, `guidance-for-includes-edge.md`

4. **Edge type summary**
   ```
   staff --member--> team
   staff --qualified--> role
   team --includes--> role
   ```

5. **Exercise:** Write spec for one edge type with proper source/target constraints

### Section 5: Assignment Face (45 min)

**Goal:** Define the face that represents complete role assignments

1. **Assignment face structure**
   - Type: face/assignment
   - Vertices: (staff, role, team)
   - Semantics: "This staff member holds this role on this team"

2. **Boundary edge requirements**
   - Edge 1: member (staff→team) - staff is on the team
   - Edge 2: qualified (staff→role) - staff can hold the role
   - Edge 3: includes (team→role) - team has that role
   - All three edges must exist for face to be valid

3. **Write assignment face spec and guidance**
   - `spec-for-assignment-face.md`
   - `guidance-for-assignment-face.md`
   - Include boundary constraint: exactly 3 edges of specified types

4. **Semantic interpretation**
   - Face represents: "Alice is the Accountable person for Frontend team"
   - Requires: Alice is member of Frontend, Alice is qualified as Accountable, Frontend includes Accountable role

5. **Exercise:** Draw assignment face with labeled boundary edges

### Section 6: Coordination Chart Type (30 min)

**Goal:** Define chart type restricted to coordination elements

1. **Coordination chart definition**
   - Type: chart/coordination
   - Extends: chart
   - Allowed vertices: staff, team, role only
   - Allowed edges: member, qualified, includes only
   - Allowed faces: assignment only

2. **Write coordination chart spec**
   - `spec-for-coordination-chart.md`
   - Vertex constraints: Only staff, team, role types
   - Edge constraints: Only member, qualified, includes types
   - Face constraints: Only assignment type

3. **Purpose of restricted chart type**
   - Ensures topological coherence
   - Makes charts interpretable as organizational structures
   - Enables specialized visualization

4. **Exercise:** Verify chart type definition is complete

### Section 7: Building the RACI Chart (90 min)

**Goal:** Build concrete coordination chart and visualize it

1. **Define vertices for RACI example**
   - 4 roles: responsible, accountable, consulted, informed
   - 5 staff: alice, bob, conrad, debbie, erica
   - 2 teams: frontend, backend

2. **Design team composition**
   - Frontend: alice, bob, conrad (members)
   - Backend: bob, conrad, debbie, erica (members)
   - Overlap: bob and conrad are on both teams

3. **Assign roles with constraints**
   - Each team has exactly 1 accountable
   - Frontend accountable: alice
   - Backend accountable: debbie
   - Distribute responsible, consulted, informed appropriately
   - Show overlap in consults/informs across teams

4. **Create edges**
   - Member edges: 7 total (3 frontend + 4 backend)
   - Qualified edges: staff→role for each qualification
   - Includes edges: team→role for each role per team

5. **Create assignment faces**
   - One face per (staff, role, team) assignment
   - Verify boundary edges exist for each face

6. **Write chart document**
   - `charts/raci-example/raci-example.md`
   - List all vertices, edges, faces
   - Calculate topology: V, E, F, χ

7. **Visualize and interpret**
   - Run: `python scripts/export_chart_direct.py charts/raci-example/raci-example.md charts/raci-example/raci-example.json`
   - Run: `python scripts/visualize_chart.py charts/raci-example/raci-example.json`
   - Open visualization, observe topology
   - Identify: Where does coordination complexity concentrate?

8. **Exercise:** Modify chart to add a third team, observe topology change

### Section 8: Registry Commit (30 min)

**Goal:** Add new types to the registry

1. **Collect all new type definitions**
   - Vertex types: actor, property, team, staff, role (5 pairs = 10 docs)
   - Edge types: member, qualified, includes (3 pairs = 6 docs)
   - Face types: assignment (1 pair = 2 docs)
   - Chart types: coordination (1 pair = 2 docs)
   - Total: 20 new documents

2. **Verify all documents**
   - Run `verify_template_based.py` on each
   - Run `build_cache.py` to validate repository

3. **Commit to registry**
   - Follow commit patterns from Module 07
   - Document type relationships in registry

4. **Exercise:** Commit your new types and verify cache builds

## Estimated Time

**Total:** 7-8 hours

- Section 1 (Type Extension): 60 min
- Section 2 (Team and Staff): 60 min
- Section 3 (Role): 45 min
- Section 4 (Coordination Edges): 60 min
- Section 5 (Assignment Face): 45 min
- Section 6 (Chart Type): 30 min
- Section 7 (RACI Chart): 90 min
- Section 8 (Registry Commit): 30 min
- Exercises (integrated): ~60 min
- Assessment: ~30 min

## Resources

**Required:**
- Existing specs: spec-for-spec, spec-for-vertex, spec-for-edge, spec-for-face, spec-for-chart
- Existing guidances: corresponding guidance documents
- Template files: `templates/00_vertices/`, `templates/01_edges/`, `templates/02_faces/`
- Verification script: `scripts/verify_template_based.py`
- Export script: `scripts/export_chart_direct.py`
- Visualization script: `scripts/visualize_chart.py`

**Optional:**
- RACI matrix documentation
- Organizational chart design patterns
- Role-based access control literature

## Success Criteria

Students have successfully completed this module when they can:

- **Extend type system:** Create actor and property vertex types with spec-guidance pairs (verification passes)
- **Create subtypes:** Create team, staff, role subtypes with proper inheritance (verification passes)
- **Define edges:** Create member, qualified, includes edge types (verification passes)
- **Define faces:** Create assignment face type with boundary constraints (verification passes)
- **Build chart:** Create RACI coordination chart with 4 roles, 5 staff, 2 teams (topology correct)
- **Enforce constraints:** Verify exactly 1 accountable per team (constraint check)
- **Visualize:** Generate and interpret coordination chart visualization (visual inspection)
- **Commit:** Add all new types to registry (cache builds successfully)

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:team-coordination]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section exercises: Type creation, edge definition, face drawing (self-check, peer review)
- Verification runs: All new documents pass template verification (automated)
- Chart construction: Incremental building with topology checks (instructor feedback)

**Summative (End of Module):**
- **Type creation:** Create all required vertex, edge, face, chart types (20 docs, verification)
- **RACI chart:** Build complete coordination chart with correct topology (correctness check)
- **Visualization:** Generate visualization and explain coordination patterns (rubric-graded)
- **Registry commit:** All types committed and cache builds (automated verification)

---

**Note:** This module demonstrates streamlined end-to-end type system extension and chart building. Students achieving [[v:skill:team-coordination]] reach the [[v:student:coordination-architect]] state, prepared to add resource flow modeling in Module 09.
