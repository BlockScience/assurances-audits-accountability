# Module 04: Verification & Validation

**Learning Journey: Knowledge Complexes**
**Module:** 04
**Skill Developed:** Verification & Validation

## Learning Goals

By the end of this module, you will be able to:

1. Distinguish verification (structural compliance) from validation (qualitative fitness)
2. Run verification scripts and interpret tool output
3. Create verification edges with tool output payloads
4. Perform LLM-assisted validation with human accountability
5. Create validation edges with quality assessments
6. Understand coupling edges and their role in quality assurance
7. Recognize edge payloads as executable documentation

## Prerequisites

Before starting this module, you should have completed:

- **Module 02:** Typed Simplicial Complexes
- **Skill Required:** Understanding of typed vertices (doc, spec, guidance) and edge types

You should be familiar with:
- The knowledge complex type system
- Basic frontmatter metadata structure
- Reading and interpreting markdown documents

## Module Roadmap

This module introduces the critical distinction between two types of quality checking:

1. **Verification** - "Did we build it right?" (structural, deterministic, automated)
2. **Validation** - "Did we build the right thing?" (qualitative, fitness-for-purpose, human judgment)

We'll learn to use scripts for verification, perform LLM-assisted validation with human oversight, and document both processes using edges with payloads. By the end, you'll have created three types of edges (verification, validation, and coupling) that serve as the building blocks for assurance triangles in Module 05.

**Note:** This module focuses on creating individual edges. In Module 05, you'll combine these edges into complete assurance faces and learn to audit assurance networks.

---

## Section 1: Introduction to Doc, Spec, and Guidance Types

### The Three Document Types

The knowledge complex type system uses three fundamental vertex types for documentation:

1. **`vertex/doc`** - Concrete instances (actual documents you create)
2. **`vertex/spec`** - Structural rules (what must be present)
3. **`vertex/guidance`** - Quality criteria (what makes it good)

Think of it this way:
- **Spec** answers: "What structure is required?"
- **Guidance** answers: "What makes this document high quality?"
- **Doc** answers: "Here's an actual instance following the spec and guidance"

### Example: Specifications vs Guidance

Let's examine a real spec-guidance pair from the knowledge complex.

**Spec: [[spec-for-spec.md]]**

This spec defines the structural requirements for specification documents. Key sections:

```yaml
frontmatter_schema:
  required_fields:
    - type: "vertex/spec"
    - extends: "vertex/doc"
    - id: Must follow pattern "v:spec:<name>"
    - name: Human-readable name
    - description: Purpose of this spec

required_sections:
  - Frontmatter Schema: Define required/optional fields
  - Body Structure: Define required sections
  - Validation Rules: Constraints and invariants
  - Examples: At least one valid instance
```

This is **deterministic** - you can check mechanically whether these sections exist.

**Guidance: [[00_vertices/guidance-for-spec.md]]**

This guidance defines quality criteria for specifications. Key sections:

```yaml
quality_criteria:
  clarity:
    - Use precise, unambiguous language
    - Define all technical terms
    - Provide concrete examples

  completeness:
    - Cover all structural requirements
    - Address edge cases
    - Specify error conditions

  usability:
    - Include usage examples
    - Explain rationale for requirements
    - Provide troubleshooting guidance
```

This is **qualitative** - requires human judgment about clarity, completeness, usability.

### The Relationship: Spec → Verification, Guidance → Validation

- **Specs** enable **verification**: automated structural checks
- **Guidance** enables **validation**: qualitative fitness assessment

Both are needed for complete quality assurance. Specs ensure correctness; guidance ensures fitness-for-purpose.

### Exercise 1.1: Compare Spec vs Guidance

**Task:** Read both documents and identify the difference.

```bash
# Read the spec
cat 00_vertices/spec-for-spec.md

# Read the guidance
cat 00_vertices/guidance-for-spec.md
```

**Questions:**
1. What sections are required by the spec?
2. What quality criteria does the guidance emphasize?
3. Which document could be checked by a script? Which requires human judgment?

**Expected Insight:** Specs are mechanical (checkable), guidance is qualitative (requires judgment).

---

## Section 2: Verification - "Did We Build It Right?"

### What is Verification?

**Verification** is the deterministic, automated checking of structural compliance against a specification.

Key characteristics:
- **Deterministic**: Same input → same output, always
- **Automated**: Run by scripts, no human judgment required
- **Structural**: Checks presence/absence of required elements
- **Boolean**: Pass or fail, no ambiguity

### Verification Scripts

The knowledge complex provides two main verification scripts:

1. **`verify_spec.py`** - Verifies spec documents against spec-for-spec
2. **`verify_template_based.py`** - Verifies any document against its template

### Running Verification: Example 1

Let's verify the spec-for-spec document against itself (a self-referential check).

```bash
# Verify spec-for-spec passes its own requirements
python scripts/verify_spec.py 00_vertices/spec-for-spec.md
```

**Expected Output:**
```
Checking 00_vertices/spec-for-spec.md against spec-for-spec requirements...

✓ 18/18 checks PASS

Checks passed:
  ✓ Type is vertex/spec
  ✓ Extends vertex/doc
  ✓ ID follows pattern v:spec:spec
  ✓ Name field present
  ✓ Description field present
  ✓ Frontmatter Schema section exists
  ✓ Body Structure section exists
  ✓ Validation Rules section exists
  ✓ Examples section exists
  ...

VERIFICATION: PASS
```

Each check is deterministic - the script looks for specific fields and sections.

### Running Verification: Example 2

Let's verify a different spec using template-based verification.

```bash
# Verify spec-for-persona against the spec template
python scripts/verify_template_based.py 00_vertices/spec-for-persona.md --templates templates
```

**Expected Output:**
```
Verifying 00_vertices/spec-for-persona.md against templates/00_vertices/spec.md

✓ 7/7 checks PASS

Checks passed:
  ✓ Required field: type = vertex/spec
  ✓ Required field: extends = vertex/doc
  ✓ Required field: id matches pattern
  ✓ Required section: Frontmatter Schema
  ✓ Required section: Body Structure
  ✓ Required section: Validation Rules
  ✓ Required section: Examples

VERIFICATION: PASS
```

### Anatomy of Verification Output

Verification output includes:
1. **Summary**: X/Y checks PASS or FAIL
2. **Details**: Which specific checks passed/failed
3. **Error messages**: What's missing or incorrect (if failed)
4. **Final verdict**: PASS or FAIL

This output becomes the **payload** for verification edges.

### Creating a Verification Edge

A verification edge documents that verification was performed. It has three vertices:
- **v1 (source)**: The document being verified
- **v2 (target)**: The spec it was verified against
- **Payload**: The verification output

**Example: [[verification-spec-spec.md]]**

```yaml
---
type: edge/verification
extends: edge
id: e:verification:spec-spec
v1: v:spec:spec
v2: v:spec:spec
verified_by: verify_spec.py
verification_date: 2025-12-28
verification_status: PASS
checks_passed: 18
checks_total: 18
---

# Verification: spec-for-spec against spec-for-spec

This edge documents the verification of `spec-for-spec.md` against its own structural requirements (self-verification).

## Verification Method

Script: `verify_spec.py`
Command: `python scripts/verify_spec.py 00_vertices/spec-for-spec.md`

## Verification Results

✓ 18/18 checks PASS

### Checks Passed
- ✓ Type is vertex/spec
- ✓ Extends vertex/doc
- ✓ ID follows pattern v:spec:spec
...

## Interpretation

The spec-for-spec document satisfies all structural requirements defined in its own specification. This self-verification demonstrates internal consistency.
```

### Exercise 2.1: Run Verification and Interpret Results

**Task:** Verify a spec document and interpret the output.

```bash
# Run verification on spec-for-persona
python scripts/verify_template_based.py 00_vertices/spec-for-persona.md --templates templates
```

**Questions:**
1. How many checks passed?
2. What does each check verify?
3. If a check failed, what would you need to fix?

### Exercise 2.2: Create a Verification Edge

**Task:** Document the verification you just performed by creating a verification edge.

1. Copy the verification edge template: `templates/01_edges/verification.md`
2. Fill in the frontmatter with your verification details
3. Include the full verification output in the body
4. Save as `01_edges/verification-persona-spec.md` (or similar name)

**Success Criteria:**
- Edge passes template verification
- Output accurately reflects what the script reported
- Interpretation section explains what was verified

---

## Section 3: Validation - "Did We Build the Right Thing?"

### What is Validation?

**Validation** is the qualitative assessment of a document's fitness-for-purpose against guidance criteria.

Key characteristics:
- **Qualitative**: Requires human judgment
- **Contextual**: Depends on intended use
- **Nuanced**: Not binary pass/fail, but levels of quality
- **Accountable**: Human must review and approve

### Validation Methods

Three approaches to validation:

1. **Manual**: Human reads document and guidance, makes assessment
2. **LLM-assisted**: LLM drafts assessment, human reviews and approves
3. **Automated**: Script checks guidance criteria (when possible)

**Important:** Even with LLM assistance, a human must review and sign off on validation. This is an accountability requirement.

### Manual Validation Example

**Example: [[validation-spec-spec.md]]**

This validation edge documents a manual assessment of spec-for-spec against guidance-for-spec.

```yaml
---
type: edge/validation
extends: edge
id: e:validation:spec-spec
v1: v:spec:spec
v2: v:guidance:spec
validator: human
human_approver: mzargham
validation_date: 2025-12-28
validation_status: APPROVED
validation_method: manual
---

# Validation: spec-for-spec against guidance-for-spec

This edge documents the validation of `spec-for-spec.md` against quality criteria defined in `guidance-for-spec.md`.

## Validation Assessment

### Clarity (Rating: Excellent)
- ✓ Precise, unambiguous language throughout
- ✓ All technical terms defined
- ✓ Concrete examples provided

### Completeness (Rating: Excellent)
- ✓ All structural requirements covered
- ✓ Edge cases addressed (self-referential specs)
- ✓ Error conditions specified

### Usability (Rating: Good)
- ✓ Usage examples included
- ✓ Rationale for requirements explained
- ~ Could add more troubleshooting guidance

## Overall Assessment

The spec-for-spec document meets all quality criteria defined in the guidance. Minor enhancement opportunity in troubleshooting section, but document is fit for purpose.

**Status:** APPROVED

**Human Approver:** mzargham
**Approval Date:** 2025-12-28
```

Notice the structure:
- Each quality criterion from guidance is assessed
- Ratings are qualitative (Excellent, Good, Needs Work)
- Overall judgment is made
- **Human accountability** is clear (approver name and date)

### LLM-Assisted Validation Example

**Example: [[validation-persona-claude:guidance.md]]**

This validation edge documents LLM-assisted assessment with human approval.

```yaml
---
type: edge/validation
extends: edge
id: e:validation:persona-claude:guidance
v1: v:persona:claude-assistant
v2: v:guidance:persona
validator: llm-assisted
llm_model: claude-sonnet-4.5
human_approver: mzargham
validation_date: 2025-12-28
validation_status: APPROVED
validation_method: llm-assisted
---

# Validation: persona-claude-assistant against guidance-for-persona

This edge documents the LLM-assisted validation of the Claude assistant persona document.

## Validation Process

1. **LLM Assessment:** Claude Sonnet 4.5 analyzed the persona document against guidance criteria
2. **Human Review:** mzargham reviewed the LLM assessment for accuracy and completeness
3. **Human Approval:** mzargham approved the assessment and overall validation

## LLM Assessment

[Generated by Claude Sonnet 4.5]

### Role Clarity (Rating: Excellent)
- ✓ Role clearly defined as "executive assistant and technical understudy"
- ✓ Relationship to chief engineer explicitly stated
- ✓ Boundaries well-articulated

### Domain Expertise (Rating: Excellent)
- ✓ Four expertise areas clearly defined
- ✓ Each area has specific scope
- ✓ Growing competency areas acknowledged

### Approach and Methodology (Rating: Excellent)
- ✓ Systematic, verification-focused approach clearly described
- ✓ Learning methodology specified (hands-on)
- ✓ Decision-making process defined (ask vs assume)

### Communication Tone (Rating: Excellent)
- ✓ Professional and precise tone maintained
- ✓ Appropriate formality level
- ✓ Clear communication principles

### Boundaries and Limitations (Rating: Excellent)
- ✓ Authority boundaries clearly stated
- ✓ What not to do is explicit
- ✓ Expertise limitations acknowledged

## Human Review

[Reviewed by mzargham]

I reviewed the LLM assessment and find it accurate and complete. The persona document meets all quality criteria defined in the guidance. The LLM correctly identified the key strengths:
- Clear role definition
- Well-articulated expertise areas
- Systematic approach
- Appropriate boundaries

I approve this validation.

**Status:** APPROVED

**Human Approver:** mzargham
**Approval Date:** 2025-12-28
```

### Accountability in Validation

**Critical Rule:** Validation edges MUST have human accountability.

Required fields:
- `validator`: "human", "llm-assisted", or "automated"
- `human_approver`: Name of person who approved
- `validation_date`: When approved
- `validation_status`: APPROVED, REJECTED, or NEEDS_WORK

The human approver is responsible for:
- Reviewing LLM assessments for accuracy (if LLM-assisted)
- Making final judgment on fitness-for-purpose
- Signing off on overall validation status

This can be checked with:

```bash
# Check accountability in validation edges
python scripts/check_accountability.py 01_edges/validation-spec-spec.md
python scripts/check_accountability.py 01_edges/validation-persona-claude:guidance.md
```

**Expected Output:**
```
Checking accountability in 01_edges/validation-spec-spec.md...
✓ human_approver field present: mzargham
✓ validation_date field present: 2025-12-28
✓ validation_status field present: APPROVED
✓ Human review section present

ACCOUNTABILITY: COMPLETE
```

### Exercise 3.1: Perform LLM-Assisted Validation

**Task:** Validate a document with LLM assistance and create a validation edge.

1. Choose a document to validate (e.g., `00_vertices/purpose-claude-assistant.md`)
2. Find its corresponding guidance document (e.g., `00_vertices/guidance-for-purpose.md`)
3. Ask an LLM (like Claude) to assess the document against the guidance criteria
4. Review the LLM assessment for accuracy
5. Create a validation edge documenting the process
6. Include your human approval statement

**Template to use:** `templates/01_edges/validation.md`

**Success Criteria:**
- Edge includes LLM assessment
- Edge includes human review section
- human_approver field has your name
- validation_status reflects your judgment

### Exercise 3.2: Write an Accountability Statement

**Task:** Review the LLM assessment from Exercise 3.1 and write a human accountability statement.

Your statement should:
- Confirm you reviewed the LLM assessment
- State whether you agree or disagree with the assessment
- Provide your own judgment on fitness-for-purpose
- Approve, reject, or request revisions

**Example format:**
```markdown
## Human Review

[Reviewed by YOUR_NAME]

I reviewed the LLM assessment and [AGREE/DISAGREE] with its findings.

[Your analysis of the assessment]

[Your independent judgment on document quality]

**Status:** [APPROVED/REJECTED/NEEDS_WORK]

**Human Approver:** YOUR_NAME
**Approval Date:** YYYY-MM-DD
```

---

## Section 4: Coupling and Edge Payloads

### What is a Coupling Edge?

A **coupling edge** is an undirected edge that pairs a spec with its corresponding guidance.

Key characteristics:
- **Undirected**: No source/target, just two paired vertices
- **Semantic**: Declares "these two documents are paired for the same domain"
- **Enables triangles**: Required for assurance faces (Module 05)

**Example: [[knowledge-complex-demo/01_edges/coupling-spec.md]]**

```yaml
---
type: edge/coupling
extends: edge
id: e:coupling:spec
v1: v:spec:spec
v2: v:guidance:spec
coupling_type: spec-guidance-pair
domain: specification-documents
created: 2025-12-28
---

# Coupling: spec-for-spec ↔ guidance-for-spec

This edge declares that `spec-for-spec.md` and `guidance-for-spec.md` are paired documents for the specification domain.

## Coupling Semantics

- **v1 (spec):** Defines structural requirements for specs
- **v2 (guidance):** Defines quality criteria for specs
- **Domain:** Specification documents
- **Pairing reason:** Both documents govern the creation of specification documents

## Why This Coupling Matters

The coupling ensures that:
1. Verification (against spec) and validation (against guidance) are aligned
2. Both documents evolve together to remain consistent
3. Assurance triangles can reference both structural and qualitative checks

## Coupling Invariants

- Both documents must address the same domain (specification documents)
- Structural requirements in spec should enable quality criteria in guidance
- Updates to one document should be reviewed for impact on the other
```

### Why Coupling Matters

Coupling edges ensure that specs and guidances stay aligned. When you:
1. **Verify** a document against a spec (structural check)
2. **Validate** that same document against guidance (quality check)
3. **Couple** the spec and guidance

...you create the foundation of an **assurance triangle** (covered in Module 05).

### Edge Payloads: Verification Edges

**Edge payloads** are the content in the body of an edge document that provides evidence.

For verification edges, the payload includes:
- **Verification method**: What script was run
- **Verification command**: Exact command used
- **Verification results**: Full output from the script
- **Interpretation**: What the results mean

**Example payload structure:**

```markdown
## Verification Method

Script: `verify_template_based.py`
Command: `python scripts/verify_template_based.py 00_vertices/spec-for-persona.md --templates templates`

## Verification Results

✓ 7/7 checks PASS

### Checks Passed
- ✓ Required field: type = vertex/spec
- ✓ Required field: extends = vertex/doc
...

## Interpretation

All structural requirements defined in the spec template are satisfied. The document is structurally correct and ready for validation.
```

This payload is **executable documentation** - someone can reproduce the verification by running the exact command.

### Edge Payloads: Validation Edges

For validation edges, the payload includes:
- **Validation assessment**: Quality criteria evaluation
- **Evidence**: Specific examples from the document
- **Human review**: Approver's independent judgment
- **Approval statement**: Final decision with accountability

**Example payload structure:**

```markdown
## Validation Assessment

### Clarity (Rating: Excellent)
- ✓ Precise, unambiguous language throughout
- Evidence: "Verification is the deterministic, automated checking..."

### Completeness (Rating: Good)
- ✓ All major criteria covered
- ~ Missing guidance on X

## Human Review

[Reviewed by mzargham]

I reviewed the assessment and agree with the findings. The document meets quality criteria for its intended purpose.

**Status:** APPROVED
**Human Approver:** mzargham
**Approval Date:** 2025-12-28
```

### Payload as Executable Documentation

Edge payloads are not just records - they're **executable documentation**:

1. **Reproducible**: Anyone can re-run the verification command
2. **Traceable**: Full provenance from tool output to edge
3. **Accountable**: Human approvers are named
4. **Evidentiary**: Provides evidence for assurance claims

This makes edges **first-class documentation artifacts**, not just metadata.

### Exercise 4.1: Create a Coupling Edge

**Task:** Create a coupling edge for a spec-guidance pair.

1. Choose a spec-guidance pair (e.g., spec-for-persona + guidance-for-persona)
2. Use the coupling edge template: `templates/01_edges/coupling.md`
3. Fill in the frontmatter with the two vertex IDs
4. Write the body explaining why these documents are coupled
5. Verify the edge passes template checks

```bash
# Verify your coupling edge
python scripts/verify_template_based.py 01_edges/coupling-persona.md --templates templates
```

### Exercise 4.2: Examine Payload Structure

**Task:** Compare payload structures across edge types.

```bash
# Read a verification edge payload
cat 01_edges/verification-spec-spec.md

# Read a validation edge payload
cat 01_edges/validation-spec-spec.md

# Read a coupling edge payload
cat 01_edges/coupling-spec.md
```

**Questions:**
1. What information is in the verification payload?
2. What information is in the validation payload?
3. How do payloads differ between deterministic (verification) and qualitative (validation) edges?
4. What makes payloads "executable documentation"?

---

## Summary

### Key Takeaways

1. **Verification vs Validation**
   - Verification: "Did we build it right?" (structural, deterministic)
   - Validation: "Did we build the right thing?" (qualitative, judgment)
   - Both are necessary for complete quality assurance

2. **Specs Enable Verification**
   - Specs define structural requirements
   - Verification scripts check compliance deterministically
   - Output is pass/fail with detailed check results

3. **Guidance Enables Validation**
   - Guidance defines quality criteria and assessment levels
   - Validation assesses fitness-for-purpose
   - Requires human judgment and accountability

4. **Edge Payloads Are Executable Documentation**
   - Verification edges contain tool output (evidence of structural compliance)
   - Validation edges contain assessments and approvals (evidence of quality)
   - Payloads provide traceability and reproducibility

5. **Coupling Pairs Specs with Guidance**
   - Coupling edges declare that a spec and guidance address the same domain
   - Enable verification + validation to work together coherently
   - Foundation for creating assurance triangles (Module 05)

6. **Three Edge Types Work Together**
   - Verification edge: doc → spec (structural proof)
   - Validation edge: doc → guidance (quality proof)
   - Coupling edge: spec ↔ guidance (domain alignment)
   - These edges provide the building blocks for assurance

### Skill Checklist

You should now be able to:

- ✓ Distinguish verification from validation
- ✓ Run `verify_spec.py` and `verify_template_based.py`
- ✓ Interpret verification output (checks passed, errors)
- ✓ Create verification edges with tool output payloads
- ✓ Perform LLM-assisted validation with human oversight
- ✓ Create validation edges with accountability statements
- ✓ Understand coupling edges and their role
- ✓ Recognize edge payloads as executable documentation

### What's Next

In **Module 05: Assurance & Audits**, you'll learn to:

- Combine verification + validation + coupling edges into complete assurance faces
- Work through a complete example of creating an assurance face
- Use `audit_assurance_chart.py` to validate assurance network completeness
- Understand the boundary complex as self-referential foundation
- Trace assurance paths from any document to the root

The three edges you learned to create in this module are the building blocks for assurance faces in Module 05.

---

## Assessment

### Final Exercise: Complete Assurance Foundation

**Task:** Demonstrate mastery by creating a complete assurance foundation for a new document.

**Choose one:**
- A spec document you haven't yet assured
- A guidance document
- A persona, purpose, or protocol document

**Requirements:**

1. **Verification** (20 points)
   - Run appropriate verification script
   - Create verification edge with complete output
   - Edge passes template verification

2. **Validation** (30 points)
   - Perform validation (manual or LLM-assisted)
   - Create validation edge with quality assessment
   - Include human approval with your name and date
   - Edge passes template verification

3. **Coupling** (10 points)
   - Identify or create coupling edge for the spec-guidance pair
   - Edge passes template verification

4. **Documentation Quality** (20 points)
   - All edges have complete payloads
   - Interpretations explain what was checked/assessed
   - Evidence supports claims

5. **Accountability** (20 points)
   - Validation has clear human approver
   - Approval date documented
   - Validation status reflects your judgment

**Deliverables:**
- Three edge files (verification, validation, coupling)
- Brief write-up (200-300 words) explaining:
  - What document you assured
  - What you verified (structural checks)
  - What you validated (quality criteria)
  - Your overall quality judgment

**Success Criteria:**
- All edges pass `verify_template_based.py`
- Verification output is complete and accurate
- Validation includes human accountability
- Write-up clearly explains the assurance foundation

**Submission:**
- Save all files in your `01_edges/` directory
- Run final verification on all edges
- Review your write-up for clarity

---

## Additional Resources

### Scripts Reference

```bash
# Verify a spec document
python scripts/verify_spec.py <file>

# Verify any document against template
python scripts/verify_template_based.py <file> --templates templates

# Check accountability in validation edge
python scripts/check_accountability.py <validation-edge-file>
```

### Example Files to Study

**Verification Edges:**
- `01_edges/verification-spec-spec.md` - Self-verification example
- Browse `01_edges/verification-*.md` for 22+ examples

**Validation Edges:**
- `01_edges/validation-spec-spec.md` - Manual validation
- `01_edges/validation-persona-claude:guidance.md` - LLM-assisted
- Browse `01_edges/validation-*.md` for 22+ examples

**Coupling Edges:**
- `01_edges/coupling-spec.md` - Spec-guidance coupling
- `01_edges/coupling-persona.md` - Persona domain coupling

### Templates

All templates are in `templates/01_edges/`:
- `verification.md` - Verification edge template
- `validation.md` - Validation edge template
- `coupling.md` - Coupling edge template

### Next Steps

When you're ready, proceed to **Module 05: Assurance & Audits** to learn:
- Creating assurance faces from verification + validation + coupling
- Running assurance audits with `audit_assurance_chart.py`
- Understanding the boundary complex and self-referential foundation
- Tracing assurance paths to ensure complete quality testimony

---

**Module 04 Complete** ✓

You've learned the foundation of quality assurance: verification (structural) and validation (qualitative) as complementary approaches to ensuring document quality. These skills are essential for maintaining high-quality knowledge complexes.
