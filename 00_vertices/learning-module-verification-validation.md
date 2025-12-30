---
type: vertex/learning-module
extends: doc
id: v:learning-module:verification-validation
name: Verification & Validation - Quality Assurance Fundamentals
description: Module teaching structural verification and qualitative validation of documents using automated tools and human judgment
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

# Verification & Validation - Quality Assurance Fundamentals

## Purpose

This module teaches students the distinction between structural verification ("did we build it right?") and qualitative validation ("did we build the right thing?"). Students learn to use verification scripts (`verify_spec.py`, `verify_template_based.py`) for deterministic checking, perform LLM-assisted validation with human accountability, and create verification and validation edges with proper payloads. The module introduces Doc, Spec, and Guidance vertex types as the foundation for systematic quality assurance.

**Educational Content:** [module-04.md](module-04.md)

## Learning Objectives

After completing this module, students will be able to:

- Distinguish between verification (structural compliance) and validation (fitness-for-purpose)
- Identify and explain Doc, Spec, and Guidance vertex types
- Run `verify_spec.py` and `verify_template_based.py` on documents and interpret results
- Create verification edges with tool output payloads
- Perform LLM-assisted validation with proper human accountability
- Create validation edges with quality assessment payloads
- Understand coupling edges that pair specs with guidance
- Recognize accountability models (manual, LLM-assisted, automated) for validation
- Explain how verification and validation work together for complete quality assurance

## Prerequisite Skills

**Required:**
- [[v:skill:typed-simplicial-complexes]] - Must understand semantic types and type-driven constraints before learning verification patterns

**Module Prerequisites:**
- Students must have completed [[v:learning-module:typed-simplicial-complexes]] (Module 2)
- Familiarity with typed document structures is essential

## Module Content

### Section 1: Introduction to Doc, Spec, and Guidance Types (60 min)

**Goal:** Understand the three fundamental document types for quality assurance

1. **Define vertex types**
   - `vertex/doc`: Instance documents (actual content)
   - `vertex/spec`: Structural rule documents (what a doc should look like)
   - `vertex/guidance`: Quality criteria documents (what makes a good doc)

2. **Examine examples**
   - Read `00_vertices/spec-for-spec.md` - spec that defines spec structure
   - Read `00_vertices/guidance-for-spec.md` - guidance for writing good specs
   - Understand relationship: specs define structure, guidance defines quality

3. **Three-way relationship**
   - Every Doc should have a Spec (structural requirements)
   - Every Doc should have Guidance (quality criteria)
   - Spec and Guidance should be coupled (aligned for same purpose)

4. **Exercise:** Read 3 spec-guidance pairs, identify structural vs qualitative requirements

### Section 2: Verification - "Did We Build It Right?" (75 min)

**Goal:** Master deterministic structural verification using automated tools

1. **Define verification**
   - Deterministic: Same input always produces same result
   - Automated: Tools execute checks without human judgment
   - Structural: Checks document structure against spec requirements
   - Binary: Pass or fail, no ambiguity

2. **Introduce verification scripts**
   - `verify_spec.py`: Checks spec documents for compliance
   - `verify_template_based.py`: Checks any document against its template
   - Usage: `python scripts/verify_template_based.py <file> --templates templates`

3. **Run verification (live demo)**
   - Execute: `python scripts/verify_template_based.py 00_vertices/spec-for-persona.md --templates templates`
   - Examine output: Checks passed/failed, error messages, line numbers

4. **Create verification edge**
   - Read template: `templates/01_edges/verification.md`
   - Structure: `edge/verification` with verification_result, verifier, tool_used in frontmatter
   - Payload: Body contains complete tool output
   - Example: `01_edges/verification-spec-spec.md`

5. **Exercise:** Run verification on 3 documents, create verification edges with payloads

### Section 3: Validation - "Did We Build the Right Thing?" (75 min)

**Goal:** Master qualitative validation using expert judgment and LLM assistance

1. **Define validation**
   - Qualitative: Requires expert judgment on fitness-for-purpose
   - Human-centered: Humans make final validation decisions
   - Criteria-driven: Guided by quality criteria from guidance documents
   - Nuanced: Not binary, includes degree of quality

2. **Validation methods**
   - Manual: Human reads guidance, assesses document, creates validation edge
   - LLM-assisted: LLM performs assessment, human reviews and approves
   - Automated: Automated checks with human approver sign-off (for specific criteria)

3. **Perform LLM-assisted validation**
   - Read guidance document: `00_vertices/guidance-for-spec.md`
   - Use LLM to assess target against criteria
   - Human reviews LLM assessment critically
   - Human approves or modifies assessment

4. **Create validation edge**
   - Read template: `templates/01_edges/validation.md`
   - Structure: `edge/validation` with validation_result, validator, validation_method, human_approver
   - Payload: Quality assessment against guidance criteria
   - Accountability: MUST include human approver (cannot be LLM-only)
   - Example: `01_edges/validation-persona-claude:guidance.md`

5. **Exercise:** Perform LLM-assisted validation on 3 documents, create validation edges with accountability

### Section 4: Coupling and Edge Payloads (60 min)

**Goal:** Understand how coupling edges pair specs with guidance and how payloads work

1. **Introduce coupling edges**
   - Type: `edge/coupling` (undirected)
   - Purpose: Pair spec with guidance for same document type
   - Example: `spec-for-persona` coupled with `guidance-for-persona`
   - Why: Ensures structural and qualitative requirements are aligned

2. **Edge payloads explained**
   - Verification payloads: Complete tool output (deterministic evidence)
   - Validation payloads: Quality assessment with reasoning (expert judgment)
   - Coupling payloads: Alignment rationale (why these pair together)
   - Structure: Frontmatter metadata + body content

3. **Read coupling example**
   - Examine: `01_edges/coupling-persona.md`
   - Observe: source and target (spec and guidance)
   - Understand: Coupling ensures consistency of requirements

4. **Exercise:** Create coupling edges for 3 spec-guidance pairs, explain alignment

### Section 5: Worked Example - Assuring a Spec Document (90 min)

**Goal:** Complete end-to-end workflow from verification through validation

1. **Choose example:** `spec-for-persona.md`

2. **Step 1: Structural verification**
   - Run: `python scripts/verify_template_based.py 00_vertices/spec-for-persona.md --templates templates`
   - Interpret results: All checks passed
   - Create: `01_edges/verification-persona:spec.md` with tool output payload

3. **Step 2: Qualitative validation**
   - Read guidance: `00_vertices/guidance-for-spec.md` quality criteria
   - Assess spec-for-persona against criteria using LLM assistance
   - Human reviews assessment
   - Create: `01_edges/validation-persona:spec.md` with assessment payload and human approver

4. **Step 3: Identify coupling**
   - Examine: `01_edges/coupling-spec.md` already exists
   - Understand: Pairs spec-for-spec with guidance-for-spec

5. **Step 4: Preview assurance triangle**
   - Three edges: verification (doc → spec), validation (doc → guidance), coupling (spec ↔ guidance)
   - Three vertices form triangle: doc, spec, guidance
   - Next module (05) will combine these into assurance face

6. **Exercise:** Students assure their own document (verification + validation + coupling identification)

## Estimated Time

**Total:** 6-7 hours

- Section 1 (Doc/Spec/Guidance): 60 min
- Section 2 (Verification): 75 min
- Section 3 (Validation): 75 min
- Section 4 (Coupling & Payloads): 60 min
- Section 5 (Worked Example): 90 min
- Exercises (integrated): ~60 min
- Assessment: ~30 min

## Resources

**Required:**
- Verification scripts: `scripts/verify_spec.py`, `scripts/verify_template_based.py`
- Template directory: `templates/`
- Example spec: `00_vertices/spec-for-spec.md`
- Example guidance: `00_vertices/guidance-for-spec.md`
- Verification edge examples: `01_edges/verification-*.md`
- Validation edge examples: `01_edges/validation-*.md`
- Coupling edge examples: `01_edges/coupling-*.md`

**Optional:**
- Accountability checking: `scripts/check_accountability.py`
- Additional spec-guidance pairs for practice
- Quality assurance methodologies from software engineering

## Success Criteria

Students have successfully completed this module when they can:

- **Distinguish verification from validation:** Explain "did we build it right?" vs "did we build the right thing?" (written)
- **Run verification scripts:** Execute `verify_spec.py` and `verify_template_based.py` on 5 documents, interpret all results correctly
- **Create verification edges:** Write verification edge documents with proper payloads for 3 documents
- **Perform LLM-assisted validation:** Assess 3 documents against guidance criteria with human accountability
- **Create validation edges:** Write validation edge documents with accountability statements for 3 documents
- **Understand coupling:** Identify coupling edges for 5 spec-guidance pairs, explain alignment
- **Complete workflow:** Execute full verification + validation workflow on 1 document independently

**Standard:** 80% accuracy on all exercises and assessment demonstrates [[v:skill:verification-validation]] acquisition

## Assessment Methods

**Formative (During Module):**
- Section 2 exercise: Run verification on 3 documents (automated feedback)
- Section 3 exercise: Create validation edges with accountability (peer review)
- Section 4 exercise: Create coupling edges (instructor review)
- Section 5 exercise: Complete workflow on chosen document (checkpoints)

**Summative (End of Module):**
- **Verification mastery:** Run verification on 5 new documents, interpret results (100% correctness)
- **Validation mastery:** Perform LLM-assisted validation on 3 documents with proper accountability (rubric-graded)
- **Edge creation:** Create verification + validation edges for 2 documents (correctness check)
- **Written explanation:** Distinguish verification from validation and explain accountability models (2-3 paragraphs, rubric-graded)

---

**Note:** This module establishes the quality assurance foundation for all future work. Students learn to systematically ensure document quality through both deterministic tools (verification) and expert judgment (validation), preparing them for complete assurance network construction in Module 05.
