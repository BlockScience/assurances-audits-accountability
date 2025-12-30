---
type: vertex/learning-module
extends: doc
id: v:learning-module:document-composition
name: Document Composition - Modular Architecture
description: Module teaching compositional document architecture using Obsidian embeds, typed subsections, and the PPP framework with systematic assurance workflows
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

# Document Composition - Modular Architecture

## Purpose

This module teaches students to design compositional document architectures where complex documents are assembled from independently assured components. Students learn to use Obsidian embed syntax (`![[reference]]`) for inline inclusion, define typed subsections in specs, apply the PPP (Persona-Purpose-Protocol) framework, compile reference documents using `compile_document.py`, and execute the systematic workflow: build components → assure components → compile compound → assure compound. The module integrates quality assurance and composition skills.

**Educational Content:** [module-06.md](../module-06.md)

## Learning Objectives

After completing this module, students will be able to:

- Design compositional document architectures with independently maintained components
- Use Obsidian embed syntax (`![[reference]]`) to include documents inline
- Define typed subsections in specs as references to other specs with type constraints
- Explain and apply the PPP (Persona-Purpose-Protocol) framework
- Compile reference documents into standalone deployable artifacts using `compile_document.py`
- Track composition relationships using `edge/dependency` with compositional and compilation types
- Independently assure constituent components (verification + validation)
- Assure compiled compound documents as complete artifacts
- Verify compositional references exist and satisfy type constraints
- Apply single-source-of-truth principles to avoid duplication

## Prerequisite Skills

**Required:**
- [[v:skill:assurance-audits]] - Must understand complete assurance workflow before applying to compositions
- [[v:skill:composing-typed-simplicial-complexes]] - Must understand identification and composition operations

**Module Prerequisites:**
- Students must have completed [[v:learning-module:assurance-audits]] (Module 05)
- Students must have completed [[v:learning-module:composing-typed-simplicial-complexes]] (Module 03)
- Familiarity with assurance faces and chart composition is essential

## Module Content

### Section 1: Compositional Documents - The Problem (45 min)

**Goal:** Understand limitations of monolithic documents and benefits of composition

1. **Monolithic document problems**
   - Duplication: Same content repeated in multiple places
   - Inconsistency: Updates miss some instances
   - Maintenance burden: Changes require editing many files
   - Assurance complexity: Must re-assure entire document for small changes

2. **Single-source-of-truth principle**
   - Define content once in canonical location
   - Reuse through reference, not duplication
   - Update once, propagate everywhere
   - Assure independently, compose with confidence

3. **Compositional approach**
   - Documents include other documents as components
   - Each component is standalone, independently assured
   - Compound document assembled from components
   - Example: System prompt = Persona + Purpose + Protocol

4. **Benefits**
   - Modularity: Components are self-contained units
   - Reusability: Components used in multiple compounds
   - Independent assurance: Assure components separately
   - Easier updates: Change component once

5. **Exercise:** Identify duplication in a monolithic document, propose compositional structure

### Section 2: Obsidian Embeds and Typed Subsections (60 min)

**Goal:** Master syntax and semantics of compositional inclusion

1. **Obsidian embed syntax**
   - Format: `![[reference-document]]` includes document inline
   - Behavior: Content from reference inserted at embed location
   - Nesting: Embeds can reference documents that have embeds (recursive)
   - Limit: 100 iterations max to prevent infinite loops

2. **Typed subsections in specs**
   - Specs define sections as references to other specs
   - Example from `spec-for-system_prompt.md`:
     ```yaml
     sections:
       - name: Persona
         spec_reference: v:spec:persona
       - name: Purpose
         spec_reference: v:spec:purpose
       - name: Protocol
         spec_reference: v:spec:protocol
     ```
   - Type constraints: Each section must reference correct type (persona spec, not persona doc)

3. **Dependency tracking**
   - Edge type: `edge/dependency` with `dependency_type: compositional`
   - Tracks which components belong to which compound
   - Example: `system_prompt-claude-assistant` → `persona-claude-assistant`

4. **Read example**
   - Examine: `00_vertices/system_prompt-claude-assistant.md`
   - Identify: All `![[reference]]` embeds
   - Map: Sections to component documents

5. **Exercise:** Read compositional document, identify all embeds, map to typed subsections in spec

### Section 3: The PPP Framework - Worked Example (90 min)

**Goal:** Understand Persona-Purpose-Protocol pattern through complete example

1. **PPP framework components**
   - **Persona:** Role, expertise, approach, tone, boundaries
   - **Purpose:** Problem statement, objectives, deliverables, constraints, success criteria
   - **Protocol:** Workflow phases, quality checks, tools, user collaboration
   - Composition: Persona + Purpose + Protocol → System Prompt

2. **Examine components**
   - Read: `00_vertices/persona-claude-assistant.md` (standalone, independently assured)
   - Read: `00_vertices/purpose-claude-assistant.md` (standalone, independently assured)
   - Read: `00_vertices/protocol-claude-assistant.md` (standalone, independently assured)
   - Observe: Each has frontmatter, complete content, can be used independently

3. **Examine composition**
   - Read: `00_vertices/system_prompt-claude-assistant.md` (reference with embeds)
   - Identify: `![[persona-claude-assistant]]`, `![[purpose-claude-assistant]]`, `![[protocol-claude-assistant]]`
   - Understand: This is SOURCE document (for authoring)

4. **Map to spec**
   - Read: `00_vertices/spec-for-system_prompt.md`
   - Observe: typed subsections define Persona, Purpose, Protocol sections
   - Understand: Type constraints ensure correct components

5. **Why PPP pattern works**
   - Persona can be reused across different purposes
   - Purpose can be reused with different personas
   - Protocol can be reused for similar workflows
   - Modular composition enables systematic reuse

6. **Exercise:** Map sections in `system_prompt-claude-assistant.md` to component documents

### Section 4: Compilation with compile_document.py (60 min)

**Goal:** Master deterministic compilation from reference to standalone

1. **Two document forms**
   - **Reference (authoring):** Contains `![[embeds]]` for maintenance
   - **Compiled (deployment):** Standalone with all embeds expanded inline

2. **How `compile_document.py` works**
   - Step 1: Reads source document
   - Step 2: Finds all `![[reference]]` embeds
   - Step 3: Loads referenced files, strips frontmatter
   - Step 4: Expands embeds inline recursively (up to 100 iterations)
   - Step 5: Writes standalone markdown

3. **Deterministic compilation**
   - Same input → same output (always)
   - No human decisions during compilation
   - Reproducible: Can recompile anytime

4. **Usage**
   - Command: `python scripts/compile_document.py source.md output.md`
   - Example: `python scripts/compile_document.py 00_vertices/system_prompt-claude-assistant.md 00_vertices/system_prompt-claude-assistant-compiled.md`

5. **Examine compiled output**
   - Read: `00_vertices/system_prompt-claude-assistant-compiled.md`
   - Compare: Side-by-side with reference document
   - Observe: All embeds expanded, standalone deployment-ready

6. **Exercise:** Compile a compositional document, diff source vs compiled, verify standalone completeness

### Section 5: Assurance Workflow for Compositional Documents (90 min)

**Goal:** Execute complete workflow from component design through compound assurance

1. **The compositional assurance workflow**
   - **Step 1:** Build constituent documents (persona, purpose, protocol)
   - **Step 2:** Assure each constituent separately (verification + validation + assurance faces)
   - **Step 3:** Create reference document with embeds (`system_prompt.md`)
   - **Step 4:** Compile reference → standalone (`system_prompt-compiled.md`)
   - **Step 5:** Verify compiled document against `spec-for-system_prompt`
   - **Step 6:** Validate compiled document against `guidance-for-system_prompt`
   - **Step 7:** Create assurance face for compiled document

2. **Why compile-then-assure?**
   - Assurance targets deployable artifact, not authoring reference
   - Users interact with compiled document, not reference
   - Verification checks compiled result matches spec
   - Validation assesses compiled quality

3. **Dependency edge types**
   - **compositional:** Tracks component → parent relationship (before compilation)
   - **compilation:** Tracks reference → compiled derived relationship (after compilation)
   - Example: `edge/dependency` with `dependency_type: compilation` from reference to compiled

4. **Worked example workflow**
   - Assume: persona, purpose, protocol already assured (from Module 05 work)
   - Step 1: Create `system_prompt-claude-assistant.md` with embeds
   - Step 2: Run `compile_document.py` → generate compiled version
   - Step 3: Verify compiled: `python scripts/verify_template_based.py system_prompt-claude-assistant-compiled.md --templates templates`
   - Step 4: Validate compiled against `guidance-for-system_prompt`
   - Step 5: Create assurance face for compiled document

5. **Exercise:** Trace complete assurance network for `system_prompt-claude-assistant-compiled.md`

### Section 6: Verification of Composition References (75 min)

**Goal:** Ensure compositional integrity through reference checking

1. **Compositional integrity checks**
   - All referenced components exist (no broken links)
   - Component types match spec requirements (persona must be type `vertex/persona`)
   - All embeds successfully expanded (no recursion limit hit)
   - Compiled document structure matches spec

2. **Use `verify_template_based.py`**
   - Checks compiled document against spec
   - Validates typed subsections present
   - Ensures structure matches requirements

3. **Dependency edge validation**
   - All components have `edge/dependency` linking to parent
   - Dependency type is correct (compositional or compilation)
   - No orphaned components

4. **Boundary validation**
   - All embedded content preserved correctly
   - Frontmatter stripped from embeds
   - No content loss during compilation

5. **Exercise:** Run verification on compiled system prompt, verify all compositional references satisfied

## Estimated Time

**Total:** 7-8 hours

- Section 1 (Compositional Problem): 45 min
- Section 2 (Embeds & Subsections): 60 min
- Section 3 (PPP Framework): 90 min
- Section 4 (Compilation): 60 min
- Section 5 (Assurance Workflow): 90 min
- Section 6 (Reference Verification): 75 min
- Exercises (integrated): ~60 min
- Assessment: ~30 min

## Resources

**Required:**
- Compilation script: `scripts/compile_document.py`
- Verification script: `scripts/verify_template_based.py`
- PPP examples: `persona-claude-assistant.md`, `purpose-claude-assistant.md`, `protocol-claude-assistant.md`
- Reference document: `system_prompt-claude-assistant.md`
- Compiled document: `system_prompt-claude-assistant-compiled.md`
- Spec: `spec-for-system_prompt.md`
- Guidance: `guidance-for-system_prompt.md`
- Dependency edges: `edge/dependency` examples

**Optional:**
- Additional compositional examples
- Diff tools for comparing reference vs compiled
- Modular software architecture patterns

## Success Criteria

Students have successfully completed this module when they can:

- **Design compositional architecture:** Identify reusable components and define composition relationships (1 architecture design)
- **Use Obsidian embeds:** Write reference documents with correct `![[embed]]` syntax (3 instances)
- **Define typed subsections:** Create specs with typed subsection references (1 spec)
- **Explain PPP framework:** Describe Persona-Purpose-Protocol pattern and benefits (2-3 paragraphs)
- **Compile documents:** Use `compile_document.py` to expand embeds to standalone (2 compilations, correctness check)
- **Assure components:** Independently verify + validate 3 constituent documents
- **Assure compounds:** Verify + validate compiled document, create assurance face
- **Track dependencies:** Create compositional and compilation dependency edges (2+ edges)
- **Verify references:** Check all embedded components exist and match type constraints

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:document-composition]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section 1 exercise: Identify duplication, propose composition (peer review)
- Section 2 exercise: Map embeds to typed subsections (self-check)
- Section 3 exercise: Map PPP sections to components (instructor feedback)
- Section 4 exercise: Compile + diff documents (automated check)
- Section 5 exercise: Trace assurance network (diagram review)
- Section 6 exercise: Verify compositional references (automated + discussion)

**Summative (End of Module):**
- **Compositional design:** Design modular document architecture for provided domain (rubric-graded)
- **PPP creation:** Create Persona-Purpose-Protocol → System Prompt composition (correctness + compilation)
- **Assurance workflow:** Execute complete workflow (component assurance → compilation → compound assurance) (rubric-graded)
- **Written explanation:** Explain single-source-of-truth, typed subsections, and compile-then-assure workflow (3-5 paragraphs, rubric-graded)

---

**Note:** This module integrates Module 03's composition understanding with Module 05's assurance capability to enable systematic design of modular documentation systems. Students achieving [[v:skill:document-composition]] reach the [[v:student:document-architect]] state, prepared for advanced documentation architecture work.
