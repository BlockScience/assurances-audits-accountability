# How To: Create Your First Document Type

This guide walks you through creating a new document type in the knowledge complex. A document type requires both a **spec** (structural requirements) and **guidance** (quality criteria). Both must pass verification AND validation against the foundational documents, and must be coupled together.

---

## Prerequisites

Before starting, ensure you can run the verification tools:

```bash
# Test that verification works
python scripts/verify_template_based.py 00_vertices/spec-for-spec.md --templates templates
```

---

## Overview: The Four-Document Foundation

Your new document type must satisfy four foundational documents (the "boundary complex"):

| Document | What It Does | Your Doc Must... |
|----------|--------------|------------------|
| **spec-for-spec (SS)** | Defines structure for specs | Your spec must **verify** against SS |
| **guidance-for-spec (GS)** | Defines quality for specs | Your spec must **validate** against GS |
| **spec-for-guidance (SG)** | Defines structure for guidances | Your guidance must **verify** against SG |
| **guidance-for-guidance (GG)** | Defines quality for guidances | Your guidance must **validate** against GG |

```
Your Spec ──verifies against──► spec-for-spec (SS)
    │
    └──validates against──► guidance-for-spec (GS)

Your Guidance ──verifies against──► spec-for-guidance (SG)
    │
    └──validates against──► guidance-for-guidance (GG)

Your Spec ◄──coupling edge──► Your Guidance
```

---

## Step 1: Choose Your Document Type Name

Pick a clear, descriptive name in kebab-case:

- `report` → spec-for-report.md, guidance-for-report.md
- `api-endpoint` → spec-for-api-endpoint.md, guidance-for-api-endpoint.md
- `test-case` → spec-for-test-case.md, guidance-for-test-case.md

**Your IDs will be:**
- Spec: `v:spec:<name>` (e.g., `v:spec:report`)
- Guidance: `v:guidance:<name>` (e.g., `v:guidance:report`)

---

## Step 2: Create the Spec Document

Create `00_vertices/spec-for-<name>.md` using the template:

```yaml
---
type: vertex/spec
extends: doc
id: v:spec:<name>
name: Specification for <Name>
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
description: Defines structural requirements for <name> documents
---

# Specification for <Name>

## Purpose Statement

[Explain what this spec defines and why it exists. 1-3 sentences.]

## Structural Requirements

[Define required frontmatter fields using a table:]

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/<name>` |
| ... | ... | ... | ... |

## Format Constraints

[Specify data types, patterns, enums, validations:]

- `id`: Must match pattern `v:<name>:[a-z0-9-]+`
- `created`: ISO 8601 datetime
- ...

## Schema Definition

[Provide complete schema in YAML or table format]

---

**Note:** This specification enables verification of <name> documents.
```

### Verify Your Spec (against SS)

```bash
python scripts/verify_template_based.py 00_vertices/spec-for-<name>.md --templates templates
```

**Expected output:** `Result: ✓ PASS`

If it fails, check:
- All required frontmatter fields present
- Required body sections: `## Purpose Statement`, `## Structural Requirements`, `## Format Constraints`, `## Schema Definition`
- Tags include full chain: `[vertex, doc, spec]`

---

## Step 3: Create the Guidance Document

Create `00_vertices/guidance-for-<name>.md` using the template:

```yaml
---
type: vertex/guidance
extends: doc
id: v:guidance:<name>
name: Guidance for <Name>
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
description: Quality criteria and best practices for <name> documents
criteria:
  - <criterion-1>
  - <criterion-2>
  - <criterion-3>
rubric: validation-assessment
---

# Guidance for <Name>

## Purpose Statement

[Explain what quality aspects this guidance addresses. Reference the spec.]

While [spec-for-<name>](spec-for-<name>.md) defines **what** structural
elements must be present, this guidance helps assess **how well** the
document serves its purpose.

## Document Overview

### What This Guidance Covers

[List what authors will learn from this guidance]

### Best Use Cases

[When should someone use this guidance?]

## Quality Criteria

### 1. <Criterion Name>

**Definition:** [What does this criterion measure?]

| Level | Indicators |
|-------|------------|
| **Excellent** | [What does excellent look like?] |
| **Good** | [What does good look like?] |
| **Needs Improvement** | [What indicates problems?] |

[Repeat for each criterion...]

## Section-by-Section Guidance

[Provide authoring advice for each section of the document type]

## Workflow Guidance

[Recommended process for creating documents of this type]

## Common Issues and Solutions

[Table of problems and fixes]

## Best Practices

[Numbered list of recommendations]

---

**Note:** This guidance enables validation of <name> documents for
fitness-for-purpose.
```

### Verify Your Guidance (against SG)

```bash
python scripts/verify_template_based.py 00_vertices/guidance-for-<name>.md --templates templates
```

**Expected output:** `Result: ✓ PASS`

If it fails, check:
- All required frontmatter fields present (including `criteria` and `rubric`)
- Required body sections: `## Purpose Statement`, `## Document Overview`, `## Quality Criteria`, `## Section-by-Section Guidance`, `## Workflow Guidance`, `## Common Issues and Solutions`, `## Best Practices`
- Tags include full chain: `[vertex, doc, guidance]`

---

## Step 4: Validate Your Spec (against GS)

Verification checks structure; validation assesses quality. Review your spec against the quality criteria in [guidance-for-spec](00_vertices/guidance-for-spec.md):

**Quality Criteria for Specs:**
1. **Clarity** - Requirements use precise, unambiguous language
2. **Completeness** - All required elements explicitly defined
3. **Testability** - Every requirement is objectively verifiable
4. **Consistency** - Terminology used consistently throughout
5. **Maintainability** - Versioned, modular, dependencies stated
6. **Obsidian Compatibility** - Proper links and tags
7. **Reference/Referent Clarity** - Clear what the spec IS vs what it DESCRIBES

**Self-check questions:**
- [ ] Could a developer implement validation from your schema?
- [ ] Are all requirements objectively checkable (no "should be reasonable")?
- [ ] Do your examples actually satisfy your spec?
- [ ] Would someone unfamiliar with your domain understand the requirements?

---

## Step 5: Validate Your Guidance (against GG)

Review your guidance against the quality criteria in [guidance-for-guidance](00_vertices/guidance-for-guidance.md):

**Quality Criteria for Guidances:**
1. **Clarity** - Criteria are understandable and actionable
2. **Completeness** - All quality dimensions covered
3. **Graduated Assessment** - Clear levels (Excellent/Good/Needs Improvement)
4. **Practical Utility** - Helps authors improve their documents
5. **Coupling Alignment** - Criteria align with spec requirements

**Self-check questions:**
- [ ] Can a human reviewer use these criteria to assess a document?
- [ ] Do the quality criteria cover the important dimensions?
- [ ] Are the level indicators specific enough to distinguish quality?
- [ ] Does the guidance reference the corresponding spec?

---

## Step 6: Create the Coupling Edge

Your spec and guidance must be coupled together. This edge enables assurance faces for documents of your type.

Create `01_edges/coupling-<name>.md`:

```yaml
---
type: edge/coupling
extends: edge
id: e:coupling:<name>
name: Coupling - Spec and Guidance for <Name>
source: v:spec:<name>
target: v:guidance:<name>
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: <ISO-8601-timestamp>
modified: <ISO-8601-timestamp>
---

# Coupling - Spec and Guidance for <Name>

**This coupling connects the specification and guidance for <name> documents.**

## Purpose

Together, these documents enable:

- **Verification:** Checking that a <name> document has required fields and
  structure (against [spec-for-<name>](../00_vertices/spec-for-<name>.md))
- **Validation:** Assessing whether a <name> document meets quality criteria
  (against [guidance-for-<name>](../00_vertices/guidance-for-<name>.md))

## Governed Document Type

Both documents govern all <name> documents in the knowledge complex.

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are <name> documents
- Verification edge: <name>-doc → spec-for-<name>
- Validation edge: <name>-doc → guidance-for-<name>
- Coupling edge: spec-for-<name> ↔ guidance-for-<name> (this edge)

## Semantic Alignment

The structural requirements in spec-for-<name> align with the quality
criteria in guidance-for-<name>:

| Spec Requires | Guidance Assesses |
|---------------|-------------------|
| [requirement 1] | [quality criterion 1] |
| [requirement 2] | [quality criterion 2] |
| ... | ... |
```

### Verify the Coupling Edge

```bash
python scripts/verify_template_based.py 01_edges/coupling-<name>.md --templates templates
```

---

## Step 7: Rebuild the Cache

After creating all three documents:

```bash
python scripts/build_cache.py
```

This updates `complex.json` with your new vertices and edge.

---

## Step 8: Run Full Test Suite

Ensure everything passes:

```bash
python -m pytest tests/ -v --ignore=tests/archive/
```

---

## Step 9: Test with a Real Document

Create a sample document of your new type to verify that your spec and guidance work in practice.

### Create a Test Document

Create `00_vertices/<name>-example.md` following your spec:

```yaml
---
type: vertex/<name>
extends: <parent-type>
id: v:<name>:example
name: Example <Name> Document
# ... all fields required by your spec ...
---

# Example <Name> Document

# ... all sections required by your spec ...
```

### Verify the Test Document (against your spec)

```bash
python scripts/verify_template_based.py 00_vertices/<name>-example.md --templates templates
```

If this fails, your spec may need adjustment. Common issues:
- Spec requires fields that don't make sense in practice
- Template doesn't match spec requirements
- Format constraints are too strict or too loose

### Validate the Test Document (against your guidance)

Manually review your test document against your guidance's quality criteria:
- Does it meet the "Excellent" indicators?
- If not, is that a problem with the document or with your criteria?

This step often reveals that your guidance criteria need refinement.

---

## Step 10 (Optional): Create a Template

If you want others to easily create instances of your document type:

```bash
# Create template directory if needed
mkdir -p templates/00_vertices

# Create template from your spec structure
# (replace specific values with placeholders like <name>, <description>, etc.)
```

---

## Checklist

Before considering your document type complete:

### Documents Created
- [ ] `spec-for-<name>.md` created in `00_vertices/`
- [ ] `guidance-for-<name>.md` created in `00_vertices/`
- [ ] `coupling-<name>.md` created in `01_edges/`

### Verification (Structure)
- [ ] Spec passes verification: `python scripts/verify_template_based.py 00_vertices/spec-for-<name>.md --templates templates`
- [ ] Guidance passes verification: `python scripts/verify_template_based.py 00_vertices/guidance-for-<name>.md --templates templates`
- [ ] Coupling edge passes verification: `python scripts/verify_template_based.py 01_edges/coupling-<name>.md --templates templates`

### Validation (Quality)
- [ ] Spec reviewed against guidance-for-spec (GS) quality criteria
- [ ] Guidance reviewed against guidance-for-guidance (GG) quality criteria

### Integration
- [ ] Cache rebuilt: `python scripts/build_cache.py`
- [ ] Full test suite passes: `python -m pytest tests/ -v --ignore=tests/archive/`

### Testing
- [ ] Test document created using your new type
- [ ] Test document passes verification against your spec
- [ ] Test document reviewed against your guidance criteria

---

## Common Mistakes

### 1. Wrong `extends` field

- Specs must have `extends: doc`
- Guidances must have `extends: doc`

### 2. Missing tag inheritance chain

```yaml
# Wrong
tags:
  - spec

# Correct
tags:
  - vertex
  - doc
  - spec
```

### 3. Missing required body sections

Each document type has specific required sections. Check the templates in `templates/00_vertices/` for the exact structure.

### 4. Putting coupling in dependencies

Spec-guidance coupling is modeled through **coupling edges**, not the `dependencies` field. The `dependencies` field is for same-category dependencies only (specs depend on specs, guidances depend on guidances).

### 5. Skipping validation

Verification (automated) is not enough. You must also validate (human review) your spec against GS and your guidance against GG to ensure quality.

### 6. Not testing with a real document

Creating a test document of your new type often reveals problems with your spec or guidance that aren't obvious otherwise.

---

## Summary: The Complete Document Type

When complete, your document type consists of:

```
00_vertices/
├── spec-for-<name>.md      # Structural requirements
├── guidance-for-<name>.md  # Quality criteria
└── <name>-example.md       # Test document (optional but recommended)

01_edges/
└── coupling-<name>.md      # Links spec ↔ guidance
```

And satisfies:

```
spec-for-<name> ──verified by──► SS (spec-for-spec)
       │
       └──validated by──► GS (guidance-for-spec)

guidance-for-<name> ──verified by──► SG (spec-for-guidance)
       │
       └──validated by──► GG (guidance-for-guidance)

spec-for-<name> ◄──coupled to──► guidance-for-<name>
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Verify single file | `python scripts/verify_template_based.py <file> --templates templates` |
| Rebuild cache | `python scripts/build_cache.py` |
| Run all tests | `python -m pytest tests/ -v --ignore=tests/archive/` |
| Check dependencies | `python scripts/verify_dependency_hierarchy.py` |

| Document | Location |
|----------|----------|
| spec-for-spec (SS) | `00_vertices/spec-for-spec.md` |
| guidance-for-spec (GS) | `00_vertices/guidance-for-spec.md` |
| spec-for-guidance (SG) | `00_vertices/spec-for-guidance.md` |
| guidance-for-guidance (GG) | `00_vertices/guidance-for-guidance.md` |
