---
type: vertex/learning-module
extends: doc
id: v:learning-module:organizational-topology
name: Organizational Topology
description: Capstone module teaching chart composition, Hodge analysis, and comprehensive organizational modeling
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

# Organizational Topology

## Purpose

This capstone module teaches students to compose coordination and management charts into complete organizational models and analyze them using algebraic topology. Students learn to paste charts together via shared team vertices, discover new semantic relationships in the composed structure, and apply Hodge decomposition and edge PageRank when visualization becomes unwieldy. The module culminates with the chief-engineer role and two capstone skills: topological-data-analysis and organizational-design-analysis.

**Educational Content:** [module-10.md](../module-10.md)

## Learning Objectives

After completing this module, students will be able to:

- Compose coordination charts (staff, team, role) with management charts (resource, function, team)
- Identify team vertices as the shared elements for chart composition
- Explore composed charts for new semantically meaningful edges and faces
- Navigate dense organizational structures that resist visual inspection
- Run edge PageRank to identify structurally important edges
- Apply Hodge decomposition to edge flows
- Interpret harmonic edges as boundaries of topological holes
- Interpret gradient edges as structural bridges
- Interpret curl edges as confluence/circulation patterns
- Connect topological features to organizational meaning
- Design organizational models satisfying given constraints
- Communicate organizational analysis to stakeholders

## Prerequisite Skills

**Required (3 skills):**
- [[v:skill:team-coordination]] - Must understand coordination charts (Module 08)
- [[v:skill:resource-management]] - Must understand management charts (Module 09)
- [[v:skill:composing-typed-simplicial-complexes]] - Must understand composition operations (Module 03)

**Module Prerequisites:**
- Students must have completed Modules 03, 08, and 09
- This is the only module with 3 prerequisites, reflecting its capstone nature

## Module Content

### Section 1: Chart Composition (60 min)

**Goal:** Compose coordination and management charts via shared vertices

1. **Review the two chart types**
   - Coordination: staff, team, role vertices; member, qualified, includes edges; assignment faces
   - Management: team, function, resource vertices; operates, produces, consumes edges; dependency faces
   - Shared element: team appears in both

2. **Composition operation**
   - Identify team vertices in both charts
   - Match teams by identity (frontend = frontend, backend = backend)
   - Paste charts together, merging matched vertices
   - Result: single complex with all vertex types

3. **Resulting structure**
   - Vertices: staff, team, role, function, resource
   - Edges: all from both charts, plus potential new edges
   - Faces: all from both charts, plus potential new faces

4. **Build the composed chart**
   - Start with RACI coordination chart from Module 08
   - Add management chart from Module 09
   - Merge via team identification
   - Write composed chart document

5. **Exercise:** Compose two small charts, verify topology

### Section 2: Semantic Discovery (75 min)

**Goal:** Find new meaningful relationships in composed structure

1. **New edge opportunities**
   - Staff → Function: "operates as" (staff member operates a function via team)
   - Staff → Resource: "produces/consumes via" (staff indirectly related to resources)
   - Role → Function: "responsible for" (role implies function responsibility)
   - Role → Resource: "accountable for" (role implies resource accountability)

2. **New face opportunities**
   - (staff, function, team): Staff operates function as team member
   - (role, function, resource): Role responsibility includes function and its resources
   - (staff, role, resource): Complete accountability chain

3. **Iterative exploration**
   - Examine each potential edge: Is it semantically meaningful?
   - Examine each potential face: Does it capture a real organizational relationship?
   - Add edges and faces that pass semantic test
   - Document rationale for each addition

4. **Density observation**
   - Composed charts get dense quickly
   - Many potential edges and faces
   - Visual inspection becomes difficult
   - Need algebraic tools

5. **Exercise:** Identify 3 new edges and 2 new faces, justify semantically

### Section 3: Edge PageRank (60 min)

**Goal:** Identify structurally important edges

1. **Why edge PageRank?**
   - Large charts have many edges
   - Not all edges are equally important
   - Need to identify critical structural elements
   - PageRank generalizes to edges via line graph

2. **Running the analysis**
   - Export chart to JSON
   - Run edge PageRank script
   - Examine ranked edge list
   - Identify top-ranked edges

3. **Interpreting results**
   - High-ranked edges: structural bridges, critical connections
   - Low-ranked edges: peripheral, redundant connections
   - Clusters of high-ranked edges: structural hubs

4. **Organizational meaning**
   - High-ranked member edge: critical team membership
   - High-ranked operates edge: bottleneck function
   - High-ranked produces edge: critical resource production

5. **Exercise:** Run PageRank, identify top 5 edges, explain significance

### Section 4: Hodge Decomposition (90 min)

**Goal:** Decompose edge flows into interpretable components

1. **Hodge decomposition overview**
   - Any edge flow can be decomposed into 3 orthogonal components
   - Harmonic: on boundary of topological holes
   - Gradient: along structural bridges (source to sink)
   - Curl: circulation/confluence patterns

2. **Running the decomposition**
   - Export chart to JSON
   - Run Hodge analysis script
   - Examine the three components
   - Visualize each component separately

3. **Interpreting harmonic component**
   - Edges on boundaries of topological holes
   - Cycles that don't bound any face
   - Organizational meaning: structural gaps, missing coordination
   - Example: circular dependencies with no resolution

4. **Interpreting gradient component**
   - Edges along structural bridges
   - Flow from source to sink
   - Organizational meaning: clear hierarchy, well-defined flow
   - Example: authority flowing from leadership to teams

5. **Interpreting curl component**
   - Edges in circulation patterns
   - Confluence where multiple paths meet
   - Organizational meaning: coordination complexity, shared resources
   - Example: multiple teams consuming same resource

6. **Exercise:** Run Hodge decomposition, identify one edge in each component, explain meaning

### Section 5: Analysis at Scale (60 min)

**Goal:** Work with charts too complex for visualization

1. **The scale problem**
   - Real organizational charts can have 50+ vertices
   - Visualization becomes unreadable
   - Need algebraic methods

2. **Algebraic workflow**
   - Export to JSON (structured data)
   - Run PageRank (identify critical edges)
   - Run Hodge decomposition (understand flow patterns)
   - Query specific substructures
   - Generate focused visualizations of subcharts

3. **Combining methods**
   - Use PageRank to find important edges
   - Use Hodge to understand their role (harmonic, gradient, curl)
   - Extract subcharts around important edges
   - Visualize focused subcharts

4. **Reporting**
   - Summarize topological findings
   - Connect to organizational insights
   - Recommend structural changes
   - Communicate to stakeholders

5. **Exercise:** Analyze a 20+ vertex chart without visualization, write summary

### Section 6: Chief Engineer Synthesis (45 min)

**Goal:** Integrate all skills into chief engineer capability

1. **The chief engineer role**
   - Comprehensive organizational modeling capability
   - Combines all previous skills
   - Can design, analyze, and communicate organizational structures

2. **Skill synthesis**
   - Simplicial complex fundamentals: Structure
   - Typed simplicial complexes: Semantics
   - Composition: Combining structures
   - Verification/validation: Quality assurance
   - Assurance: Complete quality networks
   - Reference/reuse: Pattern libraries
   - Team coordination: People structures
   - Resource management: Operational structures
   - Topological data analysis: Algebraic methods
   - Organizational design & analysis: Holistic modeling

3. **Application domains**
   - Organizational design and restructuring
   - Process improvement
   - Resource allocation analysis
   - Accountability mapping
   - Cross-functional coordination

4. **Exercise:** Design an organizational model for a given scenario

## Estimated Time

**Total:** 6.5-7.5 hours

- Section 1 (Chart Composition): 60 min
- Section 2 (Semantic Discovery): 75 min
- Section 3 (Edge PageRank): 60 min
- Section 4 (Hodge Decomposition): 90 min
- Section 5 (Analysis at Scale): 60 min
- Section 6 (Chief Engineer Synthesis): 45 min
- Exercises (integrated): ~60 min
- Assessment: ~30 min

## Resources

**Required:**
- RACI coordination chart from Module 08
- Management chart from Module 09
- Hodge analysis scripts: `scripts/hodge_analysis.py` (to be ported)
- Edge PageRank script: `scripts/edge_pagerank.py` (to be ported)
- Export script: `scripts/export_chart_direct.py`
- Visualization script: `scripts/visualize_chart.py`

**Optional:**
- Linear algebra reference
- Hodge theory background
- Organizational design literature

## Success Criteria

Students have successfully completed this module when they can:

- **Compose charts:** Combine coordination and management charts correctly (topology verified)
- **Discover semantics:** Identify 3+ new edges and 2+ new faces with justification
- **Run PageRank:** Execute edge PageRank and interpret results (top 5 explained)
- **Run Hodge:** Execute Hodge decomposition and interpret all 3 components
- **Analyze at scale:** Work with 20+ vertex chart using algebraic methods
- **Synthesize:** Design organizational model satisfying given constraints
- **Communicate:** Present analysis to non-technical audience

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:topological-data-analysis]] and [[v:skill:organizational-design-analysis]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section exercises: Composition, discovery, analysis (self-check, peer review)
- Script runs: PageRank and Hodge produce expected output (automated)
- Interpretation: Explain results in organizational terms (instructor feedback)

**Summative (End of Module):**
- **Composition:** Build composed organizational chart (correctness check)
- **Analysis:** Run PageRank and Hodge, write interpretation report (rubric-graded)
- **Design:** Create organizational model for scenario (rubric-graded)
- **Presentation:** Communicate findings to stakeholders (rubric-graded)

---

**Note:** This capstone module develops two skills simultaneously: topological-data-analysis and organizational-design-analysis. Students achieving both skills reach the [[v:student:chief-engineer]] terminal state, representing complete mastery of knowledge complex organizational modeling. The combination of algebraic rigor and semantic interpretation enables analysis of arbitrarily complex organizational structures.
