---
type: vertex/learning-module
extends: doc
id: v:learning-module:reference-reuse
name: Reference & Reuse via Doc-Kits
description: Module teaching doc-kit pattern for extending assurance with usage documentation and maintaining reusable pattern registries
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

# Reference & Reuse via Doc-Kits

## Purpose

This module teaches students to create and maintain reusable documentation patterns through the doc-kit pattern. Students learn to extend assurance faces by adding usage documentation ("When to Use", "How to Create", "Common Pitfalls"), create canonical example documents, and organize pattern libraries in doc-kit registries. The module culminates with creating a 5-pattern registry for foundational spec-guidance pairs (SS-GS, SG-GG, SC-GC, SA-GA, SP-GP), enabling systematic knowledge reuse and efficient onboarding.

**Educational Content:** [module-07.md](../module-07.md)

## Learning Objectives

After completing this module, students will be able to:

- Distinguish assurance faces from doc-kit faces (assurance + usage documentation)
- Identify doc-kit components (Spec, Guidance, Canonical Example, Usage Context)
- Write "When to Use This Document Type" sections with decision criteria and anti-patterns
- Document "How to Create" workflows with step-by-step instructions and verification checkpoints
- Create "Related Document Types" sections mapping inheritance, composition, and alternatives
- Document "Common Pitfalls" with error patterns and solutions
- Maintain "Examples in the Wild" registries for pattern instances
- Create doc-kit faces with proper structure, assurance, and accountability
- Build doc-kit registry charts organizing foundational patterns
- Use doc-kits systematically to create new document instances
- Trace doc-kits to boundary complex through assurance relationships
- Maintain living documentation patterns that evolve with usage

## Prerequisite Skills

**Required:**
- [[v:skill:assurance-audits]] - Must understand complete assurance faces before extending them with usage documentation

**Module Prerequisites:**
- Students must have completed [[v:learning-module:assurance-audits]] (Module 05)
- Familiarity with assurance faces, assurance networks, and boundary complex is essential

## Module Content

### Section 1: From Assurance to Doc-Kit (60 min)

**Goal:** Understand how doc-kits extend assurance with reusability

1. **Review assurance faces**
   - Structure: (doc, spec, guidance) + (verification, validation, coupling)
   - Purpose: Complete quality testimony for one document
   - Limitation: Proves quality but doesn't explain HOW to create similar documents

2. **Introduce doc-kit pattern**
   - Extends: `face/assurance` → `face/doc_kit`
   - Adds: Usage documentation sections beyond basic assurance
   - Purpose: Make pattern reusable, not just quality-assured

3. **Doc-kit structure from template**
   - Inherits: All assurance vertices and edges
   - Adds: "When to Use This Document Type"
   - Adds: "How to Create" workflow with checkpoints
   - Adds: "Related Document Types" relationships
   - Adds: "Common Pitfalls" error table
   - Adds: "Examples in the Wild" registry

4. **Compare assurance vs doc-kit**
   - Assurance: Proves one document's quality
   - Doc-kit: Makes pattern reusable for creating many documents
   - Analogy: Assurance is unit test, doc-kit is template library

5. **Read example**
   - Examine: `02_faces/doc-kit-persona.md` (if exists, else use template)
   - Identify: Sections beyond basic assurance
   - Understand: Usage context makes pattern accessible

6. **Exercise:** Read doc-kit, identify sections beyond assurance triangle

### Section 2: Anatomy of a Doc-Kit Face (75 min)

**Goal:** Master complete doc-kit structure and semantics

1. **Vertices and edges (inherited)**
   - Same as assurance: spec, guidance, example document
   - Same edges: coupling (spec ↔ guidance), verification (example → spec), validation (example → guidance)

2. **Frontmatter**
   - Type: `type: face/doc_kit`
   - Extends: `extends: face/assurance`
   - References: Same 6 vertex/edge references as assurance

3. **Body sections**
   - **Face Structure** (inherited): 3 vertices, 3 edges
   - **Assurance Triangle Review** (inherited): Coherence analysis
   - **When to Use:** Scenarios, anti-patterns, decision criteria
   - **How to Create:** Step-by-step with verification checkpoints
   - **Related Types:** Inheritance, composition, alternatives
   - **Common Pitfalls:** Error patterns table with solutions
   - **Examples:** Registry of instances

4. **Accountability**
   - Assurer signs off on both quality AND reusability
   - Testifies that example is canonical reference
   - Certifies usage documentation is complete and accurate

5. **Exercise:** Create "When to Use" section for a document type

### Section 3: Building Doc-Kits for Foundational Types (90 min)

**Goal:** Create 5 doc-kits for spec-guidance pairs that assure all other documents

1. **Foundational pair 1: SS-GS (spec-for-spec + guidance-for-spec)**
   - Purpose: Defines how to write specifications
   - Example: `spec-for-persona.md`
   - When to use: Defining structural requirements for new document type
   - Related: Inherits from `spec-for-doc.md`
   - Connection to boundary: SS uses boundary face with root

2. **Foundational pair 2: SG-GG (spec-for-guidance + guidance-for-guidance)**
   - Purpose: Defines how to write guidance
   - Example: `guidance-for-spec.md`
   - When to use: Defining quality criteria for document type
   - Related: Pairs with corresponding spec
   - Connection to boundary: GG uses boundary face with root

3. **Foundational pair 3: SC-GC (spec-for-chart + guidance-for-chart)**
   - Purpose: Defines how to encode simplicial complexes
   - Example: `boundary-complex.md`
   - When to use: Creating charts for validation/teaching
   - Related: Extends for subtypes (assurance_audit, syllabus)

4. **Foundational pair 4: SA-GA (spec-for-actor + guidance-for-actor)**
   - Purpose: Defines how to specify roles and personas
   - Example: `persona-claude-assistant.md`
   - When to use: Defining actors, personas, accountable parties
   - Related: Students, staff, teams extend actor

5. **Foundational pair 5: SP-GP (spec-for-property + guidance-for-property)**
   - Purpose: Defines how to specify attributes and capabilities
   - Example: `skill-simplicial-complex-fundamentals.md`
   - When to use: Defining skills, attributes, properties
   - Related: Roles extend property

6. **Why these 5?**
   - They connect to boundary complex (SS and GG via boundary faces, SG and GS via standard assurance)
   - They enable assurance of all other document types
   - They form minimal reusable pattern library

7. **Exercise:** Pick one pair, draft "How to Create" workflow

### Section 4: The Doc-Kit Registry Chart (90 min)

**Goal:** Organize patterns in central catalog

1. **Registry chart purpose**
   - Central catalog of all reusable documentation patterns
   - Type: `chart/doc_kit_registry` (extends chart)
   - Makes patterns discoverable and accessible

2. **Vertices (15+)**
   - 5 specs: spec-for-spec, spec-for-guidance, spec-for-chart, spec-for-actor, spec-for-property
   - 5 guidances: (corresponding)
   - 5 examples: One canonical instance per pair

3. **Edges (20+)**
   - 5 coupling edges (spec ↔ guidance)
   - 5 verification edges (example → spec)
   - 5 validation edges (example → guidance)
   - Dependencies, inherits as needed

4. **Faces (5)**
   - 5 doc-kit faces:
     - `f:doc_kit:spec` (SS-GS pair with spec example)
     - `f:doc_kit:guidance` (SG-GG pair with guidance example)
     - `f:doc_kit:chart` (SC-GC pair with chart example)
     - `f:doc_kit:actor` (SA-GA pair with actor example)
     - `f:doc_kit:property` (SP-GP pair with property example)

5. **Assurance network**
   - All doc-kits trace back to boundary complex
   - SS-GS connects directly (boundary faces)
   - SG-GG connects directly (boundary faces)
   - Others connect through standard assurance

6. **Topology**
   - Calculate: V, E, F, χ for registry chart
   - Expected: χ = 0 (torus-like, typical for registries)

7. **Exercise:** Draw registry chart topology, calculate Euler characteristic

### Section 5: Using Doc-Kits to Create New Documents (75 min)

**Goal:** Apply doc-kits systematically for creating new instances

1. **Doc-kit usage workflow**
   - **Step 1:** Identify need (e.g., "create new learning module")
   - **Step 2:** Find relevant doc-kit in registry (e.g., `doc_kit:learning-module`)
   - **Step 3:** Read "When to Use" - confirm doc type is appropriate
   - **Step 4:** Follow "How to Create" workflow step-by-step
   - **Step 5:** Use example as reference (not copy-paste)
   - **Step 6:** Verify against spec using `verify_template_based.py`
   - **Step 7:** Validate against guidance (LLM-assisted or manual)
   - **Step 8:** Create assurance face for new document
   - **Step 9:** (Optional) Add to "Examples in the Wild" registry

2. **Example: Creating new skill using doc-kit**
   - Find: `doc_kit:property` (skills extend property)
   - Read: "When to Use" confirms skill is appropriate
   - Follow: "How to Create" step-by-step
   - Reference: `skill-simplicial-complex-fundamentals.md` as canonical example
   - Verify: Run `verify_template_based.py` on new skill
   - Validate: Assess against `guidance-for-property`
   - Assure: Create assurance face

3. **Key principle: Doc-kits are living documents**
   - Update "How to Create" as best practices evolve
   - Add new pitfalls as they're discovered
   - Expand "Examples in the Wild" as usage grows
   - Refine "When to Use" based on experience

4. **Exercise:** Use a doc-kit to create new document instance, verify it passes

## Estimated Time

**Total:** 6.5-7.5 hours

- Section 1 (Assurance to Doc-Kit): 60 min
- Section 2 (Doc-Kit Anatomy): 75 min
- Section 3 (Foundational Types): 90 min
- Section 4 (Registry Chart): 90 min
- Section 5 (Using Doc-Kits): 75 min
- Exercises (integrated): ~60 min
- Assessment: ~30 min

## Resources

**Required:**
- Doc-kit template: `templates/02_faces/doc-kit.md`
- Example doc-kits: `02_faces/doc-kit-*.md` (5 to be created)
- Registry chart: `charts/doc-kit-registry/doc-kit-registry.md` (to be created)
- Boundary complex chart: `charts/boundary-complex/boundary-complex.md`
- Foundational specs: spec-for-spec, spec-for-guidance, spec-for-chart, spec-for-actor, spec-for-property
- Foundational guidances: (corresponding)
- Canonical examples: One per foundational pair

**Optional:**
- Pattern library theory
- Design pattern cataloging methodologies
- Knowledge management systems

## Success Criteria

Students have successfully completed this module when they can:

- **Distinguish doc-kit from assurance:** Explain how doc-kit extends assurance with usage context (written, 2-3 paragraphs)
- **Create doc-kit faces:** Write 2 complete doc-kit faces with all required sections (rubric-graded)
- **Write usage criteria:** Create "When to Use" sections for 3 document types (decision criteria + anti-patterns)
- **Document workflows:** Create "How to Create" workflows for 3 document types with checkpoints (correctness check)
- **Map relationships:** Identify inheritance, composition, alternatives for 5 document types (diagram)
- **Build registry:** Create doc-kit registry chart with 5 foundational patterns (V, E, F, χ calculated)
- **Use doc-kit:** Create new document instance using doc-kit workflow, verify it passes assurance (practical exam)
- **Trace to boundary:** Trace 3 doc-kits to boundary complex through assurance (diagram + explanation)

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:reference-reuse]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section 1 exercise: Identify doc-kit sections beyond assurance (self-check)
- Section 2 exercise: Create "When to Use" section (peer review)
- Section 3 exercise: Draft "How to Create" workflow (instructor feedback)
- Section 4 exercise: Draw registry topology (self-check with calculations)
- Section 5 exercise: Use doc-kit to create instance (automated verification + discussion)

**Summative (End of Module):**
- **Doc-kit creation:** Create 2 complete doc-kit faces for chosen foundational pairs (rubric-graded)
- **Registry construction:** Build doc-kit registry chart with all 5 patterns, verify topology (correctness check)
- **Pattern usage:** Use doc-kit to create new document, verify + validate, create assurance (practical exam, rubric-graded)
- **Written explanation:** Explain doc-kit pattern, registry purpose, and boundary connection (3-5 paragraphs, rubric-graded)

---

**Note:** This module enables systematic knowledge reuse through pattern libraries. Students achieving [[v:skill:reference-reuse]] reach the [[v:student:document-architect]] state alongside those completing Module 06, prepared for maintaining organization-wide documentation systems with quality-assured reusable patterns.
