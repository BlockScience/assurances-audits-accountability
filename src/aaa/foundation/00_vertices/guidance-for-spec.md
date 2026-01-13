---
type: vertex/guidance
extends: doc
id: v:guidance:spec
name: Guidance for Specifications
description: Quality criteria and best practices for creating excellent specification documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T16:00:00Z
modified: 2025-12-27T16:00:00Z
dependencies: []
---

# Guidance for Specifications

**This guidance defines quality criteria and best practices for creating excellent specification documents.**

## Purpose

While the spec-for-spec defines what structural elements must be present, this guidance helps authors assess **how well** a specification serves its purpose. Great specs are clear, complete, testable, and maintainable.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating specification documents by providing:
- Quality assessment criteria
- Best practices for clarity and completeness
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations

### Best Use Cases

Use this guidance when:
- Creating a new specification document
- Reviewing an existing spec for quality
- Teaching others how to write good specs
- Establishing spec quality standards for your organization
- Evaluating whether a spec is fit-for-purpose

## Quality Criteria

### 1. Clarity

**Excellent:**
- Requirements use precise, unambiguous language
- Technical terms defined or linked to definitions
- Examples provided for complex requirements
- No contradictory statements

**Good:**
- Generally clear with minor ambiguities
- Most terms defined
- Some examples provided

**Needs Improvement:**
- Vague requirements ("should be good", "reasonable")
- Undefined jargon
- Contradictory requirements

### 2. Completeness

**Excellent:**
- All required elements explicitly defined
- Edge cases and special conditions addressed
- Optional elements clearly marked as optional
- Boundaries of scope well-defined

**Good:**
- Core requirements present
- Major cases covered
- Minor gaps don't impact usability

**Needs Improvement:**
- Missing critical requirements
- Undefined required fields
- Unclear scope boundaries

### 3. Testability

**Excellent:**
- Every requirement is objectively verifiable
- Pass/fail criteria are deterministic
- Examples demonstrate compliance
- Validation rules are automatable

**Good:**
- Most requirements verifiable
- Some subjective elements remain
- Basic test cases implied

**Needs Improvement:**
- Requirements cannot be objectively checked
- No clear pass/fail criteria
- Verification depends on interpretation

### 4. Consistency

**Excellent:**
- Terminology used consistently throughout
- Format consistent across similar elements
- No internal contradictions
- Cross-references all resolve

**Good:**
- Minor terminology variations
- Generally consistent structure
- No major contradictions

**Needs Improvement:**
- Same concept described differently
- Inconsistent formatting
- Contradictory requirements

### 5. Maintainability

**Excellent:**
- Versioned with clear changelog
- Modular structure allows updates
- Dependencies explicitly stated
- Deprecation path defined for breaking changes

**Good:**
- Version tracked
- Structure allows some flexibility
- Major dependencies noted

**Needs Improvement:**
- No version tracking
- Monolithic structure hard to update
- Dependencies unclear

### 6. Obsidian Compatibility

**Excellent:**
- Links to parent specification using `[[parent-spec-id]]`
- Links to related guidance using `[[guidance-id]]`
- For extended specs, links to base spec
- Tags properly set in frontmatter
- ID follows consistent naming convention (v:spec:<name>)
- File name matches document ID

**Good:**
- Parent spec link present
- Tags present
- ID mostly consistent

**Needs Improvement:**
- Missing links to parent spec or related guidance
- No tags in frontmatter
- Inconsistent ID format
- File name doesn't match ID

**Required Links for Specifications:**
- **Parent specification:** Link to the spec being extended (e.g., spec-for-charts links to spec-for-specs)
- **Related guidance:** Link to corresponding guidance document (e.g., spec-for-charts links to guidance-for-charts)

**Why This Matters:**
- Enables navigation through specification hierarchy
- Shows relationships in Obsidian graph view
- Makes extension chain visible
- Supports spec/guidance coupling validation

### 7. Reference/Referent Clarity

**Excellent:**
- Clear distinction between the spec document itself (the reference) and what it describes (the referent)
- Examples distinguish specification requirements from instance content
- Document type reflects what the spec IS, not what it DESCRIBES
- Explanation clarifies this distinction when it may be confusing

**Good:**
- Generally clear about spec vs instance
- Some examples show the distinction
- Type is correct

**Needs Improvement:**
- Confuses spec document with what it describes
- Examples mix specification and instance content
- Type choice unclear or incorrect

**Critical Principle: Referent vs Reference**

**The document type describes what the document IS (its role in the knowledge complex), not what it's ABOUT (what it describes).**

Examples:
- **spec-for-verification.md** is a VERTEX (it's a spec document that exists in 00_vertices/) even though it DESCRIBES edges (verification relationships)
- **spec-for-charts.md** is a VERTEX (it's a spec document) even though it DESCRIBES charts (which are also vertices but of a different nature)
- **spec-for-assurance-audits.md** is a VERTEX (it's a spec document) even though it DESCRIBES assurance audits (analytical documents)

**Why This Matters:**
- Prevents confusion about document classification
- Ensures correct file organization (specs for edges still go in 00_vertices/)
- Maintains type system consistency
- Clarifies that "what it describes" (referent) ≠ "what it is" (reference)

**Guidance for Spec Authors:**
- When creating a spec for edges, faces, or other complex types, remember the spec itself is still a vertex
- Use the Purpose section to clearly state what the spec describes vs what it is
- Provide examples that show both the spec structure AND instance structure to clarify the distinction
- If confusion is likely, add an explicit note about the reference/referent distinction

## Section-by-Section Guidance

### Purpose Statement

**Purpose:** Explain why this spec exists and what it governs

**Tips:**
- Start with the problem or need
- State what will be standardized
- Keep to 1-3 sentences
- Avoid implementation details

**Example:**
> "This specification defines the required frontmatter fields for all vertex documents in the knowledge complex, ensuring consistent metadata across the repository."

### Structural Requirements

**Purpose:** Define what elements MUST be present

**Tips:**
- Use tables for field definitions (clearer than prose)
- Include: field name, type, requirement level, description
- Mark REQUIRED vs OPTIONAL explicitly
- Specify cardinality (single vs array, min/max items)

**Anti-pattern:** Mixing structure with quality criteria
- ❌ "The name field should be descriptive and meaningful"
- ✅ "The name field is REQUIRED (type: string)"

### Format Constraints

**Purpose:** Specify data types, patterns, validations

**Tips:**
- Use precise type names (string, integer, boolean, datetime, enum)
- Provide regex patterns for string formats
- Specify ISO standards for dates/times
- Define enum values explicitly
- Give format examples

**Example:**
```yaml
id: string (pattern: ^v:spec:[a-z0-9-]+$)
created: datetime (ISO 8601 format)
status: enum (values: draft, active, deprecated)
```

### Schema Definition

**Purpose:** Provide the complete structural blueprint

**Tips:**
- Choose schema format appropriate to domain (YAML, JSON Schema, tables)
- Make schema copy-paste ready for implementers
- Include all required and optional elements
- Show nesting and relationships clearly

**Avoid:** Partial schemas that require readers to infer missing pieces

### Examples

**Purpose:** Demonstrate compliance concretely

**Tips:**
- Provide at least one complete, valid example
- Show both minimal and full-featured instances
- Annotate complex examples with explanations
- Use realistic (not toy) data

**Quality indicators:**
- Example is itself valid against the spec
- Example includes edge cases if relevant
- Comments explain non-obvious choices

### Validation Rules

**Purpose:** Enable automated compliance checking

**Tips:**
- Number rules for reference
- State each rule independently (no compound rules)
- Use imperative language (MUST, SHALL)
- Indicate severity if rules have different priorities

**Example:**
> 1. The `type` field MUST be exactly "vertex/spec"
> 2. The `id` field MUST match pattern ^v:spec:[a-z0-9-]+$
> 3. Tags array MUST include "vertex", "doc", and "spec"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define Purpose** (5 min)
   - Why does this spec exist?
   - What problem does it solve?

2. **Identify Required Elements** (15-30 min)
   - What MUST be present for compliance?
   - What is OPTIONAL but supported?

3. **Specify Formats** (15-30 min)
   - Data types for each element
   - Patterns, enums, constraints

4. **Create Schema** (20-40 min)
   - Formalize structure in chosen format
   - Ensure completeness

5. **Write Examples** (15-30 min)
   - Minimal valid example
   - Full-featured example
   - Edge cases if relevant

6. **Define Validation Rules** (10-20 min)
   - Extract checkable rules
   - Order by importance

7. **Review and Refine** (15-30 min)
   - Check against quality criteria
   - Ensure self-consistency
   - Remove ambiguity

**Total estimated time:** 2-3 hours for a typical spec

### Quality Checkpoints

After completing each phase:

- **After step 2:** Can you list all required elements without consulting other docs?
- **After step 4:** Could a developer implement validation from your schema?
- **After step 5:** Do your examples actually satisfy your spec?
- **After step 7:** Would someone unfamiliar with your domain understand the requirements?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Too Vague** | Requirements like "should be reasonable" or "appropriate format" | Use specific constraints: "MUST be 1-100 characters" or "MUST match ISO 8601 format" |
| **Mixing Concerns** | Spec includes quality criteria like "should be well-written" | Move quality criteria to guidance; keep spec structural only |
| **Incomplete Schema** | Missing fields that are referenced elsewhere | Ensure every referenced field is defined in schema |
| **Untestable Requirements** | "Should generally follow best practices" | Make requirements objective: "MUST include error handling for network failures" |
| **No Examples** | Only abstract requirements without concrete instances | Add at least one complete, valid example |
| **Version Drift** | Spec updated but version unchanged | Update version field and add changelog entry |

## Best Practices

1. **Start Simple** - Begin with minimal required fields, add optional ones iteratively
2. **Test with Examples** - Write examples first, derive spec from what works
3. **Be Deterministic** - Every requirement should be objectively checkable
4. **Use Standards** - ISO 8601 for dates, semver for versions, kebab-case for IDs
5. **Separate Structure from Quality** - Spec defines "what", guidance defines "how well"
6. **Version Carefully** - Breaking changes require major version bump
7. **Couple with Guidance** - Every spec should have corresponding guidance document
8. **Self-Consistency** - Meta-specs (like spec-for-spec) should verify themselves
9. **Avoid Over-Specification** - Don't constrain what doesn't need constraining
10. **Maintain Backward Compatibility** - Design for evolution, deprecate gracefully

## Validation vs. Verification

**Verification** (deterministic):
- Does the document structurally comply with spec-for-spec?
- Are all required fields present?
- Do types match schema?
- Do patterns validate?

**Validation** (qualitative):
- Is the spec clear and unambiguous?
- Does it serve its purpose well?
- Is it maintainable and testable?
- Does it follow best practices?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document is itself an instance of type `vertex/guidance` and demonstrates the quality criteria it defines:

✓ Clear purpose and scope
✓ Quality criteria with leveled assessments
✓ Practical section-by-section advice
✓ Common issues with solutions
✓ Best practices enumerated
✓ Examples provided
✓ Workflow with time estimates

## Tooling Support

### Verification Commands

```bash
# Verify spec structure against spec-for-spec
python scripts/verify_structure.py 00_vertices/my-spec.md --type vertex

# Verify complete chart including spec
python scripts/verify_chart.py charts/my-chart.md
```

### Validation Support

Human review using this guidance document. Future tools may include:
- Style linters for spec language
- Completeness checkers
- Example validators
- Cross-reference resolution

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | v:spec:spec (spec-for-spec) |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Terminology | VERIFICATION = structural compliance; VALIDATION = fitness assessment |
| Self-Reference | This guidance validates itself per its own criteria |

---

**Note:** This guidance is coupled with spec-for-spec via a coupling edge, forming part of the boundary complex's self-referential foundation.
