---
type: vertex/learning-module
extends: doc
id: v:learning-module:assurance-audits
name: Assurance & Audits - Complete Quality Networks
description: Module teaching assurance triangles, assurance network auditing, and boundary complex self-referential foundations
tags:
  - vertex
  - doc
  - learning-module
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: intermediate
dependencies: []
---

# Assurance & Audits - Complete Quality Networks

## Purpose

This module teaches students to construct complete assurance faces by combining verification, validation, and coupling edges into coherent triangles. Students learn to audit assurance networks using `audit_assurance_chart.py`, trace assurance paths back to the boundary complex root, and understand how the boundary complex resolves self-referential dependencies through the root vertex and boundary faces. The module culminates with exploration of the SS-GS, SG-GG kernel pattern as the foundation for all quality assurance.

**Educational Content:** [module-05.md](../module-05.md)

## Learning Objectives

After completing this module, students will be able to:

- Construct assurance triangles from verification + validation + coupling edges
- Write triangle coherence reviews assessing how edges integrate
- Create assurance face documents with proper structure and accountability
- Run `audit_assurance_chart.py` to validate assurance network completeness
- Interpret audit results including coverage, trace paths, and root anchoring
- Explain the boundary complex structure (b0:root, SS, SG, GS, GG)
- Understand boundary faces and their role in resolving self-reference
- Trace assurance paths from arbitrary documents to boundary complex
- Recognize the SS-GS, SG-GG kernel pattern as foundational pairs
- Articulate how assurance networks enable systematic quality testimony

## Prerequisite Skills

**Required:**
- [[v:skill:verification-validation]] - Must understand verification and validation before combining into assurance

**Module Prerequisites:**
- Students must have completed [[v:learning-module:verification-validation]] (Module 04)
- Familiarity with verification edges, validation edges, and coupling edges is essential

## Module Content

### Section 1: The Assurance Triangle (60 min)

**Goal:** Understand how three edges form complete quality testimony

1. **Review prerequisite edges**
   - Verification edge: doc → spec (structural compliance)
   - Validation edge: doc → guidance (fitness-for-purpose)
   - Coupling edge: spec ↔ guidance (alignment)

2. **Introduce assurance face**
   - Type: `face/assurance`
   - 3 vertices: doc, spec, guidance
   - 3 edges: verification, validation, coupling
   - Semantics: Complete quality testimony for one document

3. **Anatomy of assurance face**
   - Frontmatter: Links to target doc, spec, guidance, and 3 edges
   - Body: Triangle coherence review (how edges integrate)
   - Assurer: Human who testifies to overall quality (not just LLM)
   - Assurance method: Manual, LLM-assisted, or automated (with human approver)

4. **Read example**
   - Examine: `02_faces/assurance-spec-guidance.md`
   - Identify: 3 vertices, 3 boundary edges
   - Understand: Coherence review integrates verification + validation

5. **Exercise:** Identify vertices and edges in 3 assurance face documents

### Section 2: Building an Assurance Face (75 min)

**Goal:** Create complete assurance faces from existing edges

1. **Prerequisites for assurance**
   - Verification edge must exist (doc → spec)
   - Validation edge must exist (doc → guidance)
   - Coupling edge must exist (spec ↔ guidance)
   - All three must reference compatible vertices

2. **Create assurance face**
   - Read template: `templates/02_faces/assurance.md`
   - Structure: Frontmatter with 6 vertex/edge references
   - Body sections: Face Structure, Assurance Triangle Review, Accountability

3. **Triangle coherence review**
   - Analyze coupling: Are spec and guidance aligned?
   - Review verification: Did doc pass structural checks?
   - Review validation: Did doc meet quality criteria?
   - Integrate: How do three edges work together to encode complete quality?

4. **Assurer accountability**
   - Human must sign off on overall assurance (not just LLM validation)
   - Assurer testifies that doc satisfies both structural and qualitative requirements
   - Assurance is professional judgment, not automated output

5. **Exercise:** Create assurance face for document students verified/validated in Module 04

### Section 3: Assurance Auditing with Scripts (90 min)

**Goal:** Master assurance network validation using audit tools

1. **Introduce `audit_assurance_chart.py`**
   - Purpose: Validate assurance network completeness
   - Usage: `python scripts/audit_assurance_chart.py charts/<chart>/<chart>.md`
   - What it checks: Coverage, trace paths, root anchoring

2. **Audit criteria**
   - **Coverage:** All vertices in audit target list have assurance faces
   - **Trace paths:** Each assured vertex traces back through assurance network
   - **Root anchoring:** All traces terminate at boundary complex

3. **Run audit on example**
   - Execute: `python scripts/audit_assurance_chart.py charts/boundary-complex/boundary-complex.md`
   - Observe: 100% coverage, all traces resolve to root
   - Examine: Generated audit trail (`boundary-complex-audit-trail.md`)

4. **Interpret audit results**
   - Pass/fail for each target vertex
   - Trace path visualization (vertex → ... → root)
   - Coverage percentage (vertices assured / vertices targeted)
   - Missing assurances identified

5. **Exercise:** Run audit on 2 charts, interpret results, identify missing assurances

### Section 4: The Boundary Complex - Self-Referential Foundation (90 min)

**Goal:** Understand how boundary complex resolves circular dependencies

1. **The self-referential problem**
   - spec-for-spec is verified against... itself? (circular)
   - guidance-for-guidance is validated against... itself? (circular)
   - Cannot have infinite regress of specs

2. **The boundary complex solution**
   - Structure: 5 vertices (b0:root, SS, SG, GS, GG)
   - Root vertex: `b0:root` serves as topological anchor (no content, only structural)
   - Boundary edges: `b1` edges from root
   - Boundary faces: `b2` faces using root as 3rd vertex

3. **Boundary complex structure**
   - **Vertices (5):** root, spec-for-spec, spec-for-guidance, guidance-for-spec, guidance-for-guidance
   - **Edges (11):** 2 coupling, 4 verification, 4 validation, 1 b1 boundary edge
   - **Faces (4):** 2 standard assurance (SG, GS), 2 boundary assurance (SS, GG)

4. **How boundary faces work**
   - Cannot create standard assurance for SS (would require spec-for-spec-for-spec)
   - Solution: Use root as 3rd vertex → `(spec-for-spec, guidance-for-spec, root)`
   - Boundary face structure: (self-ref doc, corresponding guidance, root)
   - Valid triangle without infinite regress

5. **Trace assurance paths**
   - Example: `spec-for-persona` → verified against `spec-for-spec` → boundary face resolves to root
   - All specs trace to SS-GS pair
   - All guidance trace to SG-GG pair
   - Root anchors entire assurance network

6. **Exercise:** Trace 5 documents from arbitrary vertex to boundary complex root

### Section 5: The Kernel Pattern - SS, SG, GS, GG (75 min)

**Goal:** Recognize foundational mutually assured pairs

1. **Boundary kernel definition**
   - Minimal viable assurance foundation
   - Four foundational documents that define and assure themselves

2. **Four foundational pairs**
   - **SS-GS:** spec-for-spec + guidance-for-spec (how to write specifications)
   - **SG-GG:** spec-for-guidance + guidance-for-guidance (how to write guidance)

3. **Mutual assurance**
   - SS uses boundary face (with root)
   - GG uses boundary face (with root)
   - SG uses standard assurance (SS verified against itself, GS provides guidance)
   - GS uses standard assurance (SG verified against itself, GG provides guidance)

4. **Self-referential closure**
   - These 4 documents define the type system for specs and guidances
   - They assure each other and themselves
   - All other specs inherit assurance from this foundation

5. **Audit results**
   - Run: `audit_assurance_chart.py` on boundary-complex chart
   - Observe: 100% coverage for all 5 vertices
   - Understand: This is the assurance base case

6. **Exercise:** Draw assurance network diagram showing all 4 assurance faces

## Estimated Time

**Total:** 6.5-7.5 hours

- Section 1 (Assurance Triangle): 60 min
- Section 2 (Building Faces): 75 min
- Section 3 (Auditing): 90 min
- Section 4 (Boundary Complex): 90 min
- Section 5 (Kernel Pattern): 75 min
- Exercises (integrated): ~60 min
- Assessment: ~30 min

## Resources

**Required:**
- Assurance audit script: `scripts/audit_assurance_chart.py`
- Assurance face template: `templates/02_faces/assurance.md`
- Boundary complex chart: `charts/boundary-complex/boundary-complex.md`
- Boundary kernel chart: `charts/boundary-kernel/boundary-kernel.md`
- Assurance face examples: `02_faces/assurance-*.md`
- Boundary face examples: `02_faces/b2-spec-spec.md`, `02_faces/b2-guidance-guidance.md`
- Boundary complex visualization: `charts/boundary-complex/boundary-complex.html`

**Optional:**
- Topology analysis: `scripts/topology.py`
- Chart visualization: `scripts/visualize_chart.py`
- Self-referential systems theory (for advanced learners)

## Success Criteria

Students have successfully completed this module when they can:

- **Construct assurance triangles:** Identify verification + validation + coupling edges and combine into assurance face (3 instances)
- **Write coherence reviews:** Analyze how three edges integrate to form complete quality testimony (rubric-graded)
- **Create assurance faces:** Write complete assurance face documents with accountability (2 instances, correctness check)
- **Run assurance audits:** Execute `audit_assurance_chart.py` on 2 charts, interpret results (100% correctness)
- **Trace to root:** Follow assurance paths from 5 documents to boundary complex (diagram with explanations)
- **Explain boundary complex:** Describe root vertex role and boundary face pattern (2-3 paragraphs, rubric-graded)
- **Recognize kernel:** Identify SS-GS, SG-GG pairs and explain mutual assurance (written + diagram)

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:assurance-audits]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section 1 exercise: Identify vertices/edges in assurance faces (peer review)
- Section 2 exercise: Create assurance face from Module 04 work (instructor feedback)
- Section 3 exercise: Run audits, interpret results (automated + discussion)
- Section 4 exercise: Trace 5 documents to root (self-check with diagrams)
- Section 5 exercise: Draw assurance network for kernel (peer review)

**Summative (End of Module):**
- **Assurance face creation:** Create 2 complete assurance faces with coherence reviews (rubric-graded)
- **Audit mastery:** Run audit on provided chart, interpret all results, propose fixes for missing assurances (correctness check)
- **Trace mastery:** Trace 5 arbitrary documents to boundary complex with diagrams and explanations (rubric-graded)
- **Written explanation:** Explain boundary complex, root anchoring, and kernel pattern (3-5 paragraphs, rubric-graded)

---

**Note:** This module completes the assurance network foundation established in Module 04. Students learn to combine individual quality checks into complete assurance testimonies and understand the self-referential foundation that makes systematic quality assurance possible. This prepares them for advanced compositional and pattern library work in Modules 06 and 07.
