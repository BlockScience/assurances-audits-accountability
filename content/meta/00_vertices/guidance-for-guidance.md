---
type: vertex/guidance
extends: doc
id: v:guidance:guidance
name: Guidance for Guidance Documents
description: Quality criteria and best practices for creating excellent guidance documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T16:00:00Z
modified: 2025-12-27T16:00:00Z
dependencies: []
---

# Guidance for Guidance Documents

**This guidance defines quality criteria and best practices for creating excellent guidance documents.**

## Purpose

While spec-for-guidance defines what structural elements must be present, this guidance helps authors assess **how well** a guidance document serves its purpose. Great guidance documents are empathetic, actionable, comprehensive, and usable.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating guidance documents by providing:
- Quality assessment criteria specific to guidance documents
- Best practices for writing helpful, actionable advice
- Common pitfalls in guidance authoring
- Section-by-section authoring recommendations
- Workflow for guidance creation

### Best Use Cases

Use this guidance when:
- Creating a new guidance document
- Reviewing existing guidance for quality and usefulness
- Teaching others how to write effective guidance
- Establishing guidance quality standards for your organization
- Evaluating whether guidance effectively supports its users

## Quality Criteria

### 1. Empathy and Clarity

**Excellent:**
- Anticipates user confusion and addresses it proactively
- Uses clear, jargon-free language (or defines necessary jargon)
- Provides context for why criteria matter
- Examples are realistic and relatable

**Good:**
- Generally clear and accessible
- Most user needs addressed
- Some helpful examples

**Needs Improvement:**
- Assumes too much knowledge
- Uses unexplained jargon
- Abstract advice without concrete examples
- Doesn't address "why" behind criteria

### 2. Actionability

**Excellent:**
- Every tip is specific enough to act on immediately
- Concrete examples show exactly what to do
- Anti-patterns paired with corrective actions
- Checklists enable self-assessment

**Good:**
- Most advice actionable
- Some examples provided
- General direction clear

**Needs Improvement:**
- Vague advice ("be thoughtful", "use good judgment")
- No examples or only trivial ones
- Tells what not to do without showing alternatives
- No way to self-assess compliance

### 3. Comprehensiveness

**Excellent:**
- Covers all major sections of supported document type
- Addresses common edge cases and pitfalls
- Provides workflow with time estimates
- Includes quality checkpoints
- Best practices cover full authoring lifecycle

**Good:**
- Major sections covered
- Common issues addressed
- Workflow present
- Some checkpoints

**Needs Improvement:**
- Missing guidance for key sections
- No workflow or checkpoints
- Leaves users uncertain about completeness
- Important pitfalls undocumented

### 4. Leveled Assessment

**Excellent:**
- Quality criteria use consistent, clear levels (Excellent/Good/Needs Improvement)
- Distinctions between levels are meaningful and observable
- Criteria cover different aspects (not all structural or all stylistic)
- Levels help authors gauge where they stand

**Good:**
- Criteria have levels
- Levels generally distinguishable
- Covers multiple quality dimensions

**Needs Improvement:**
- Binary pass/fail criteria (belongs in spec, not guidance)
- Unclear distinctions between levels
- Only one quality dimension covered
- Levels not actually observable

### 5. Usability

**Excellent:**
- Well-organized with clear sections
- Can be used as a reference (not just read linearly)
- Tables and lists used effectively for scannability
- Quick-reference checklists provided
- Time estimates help planning

**Good:**
- Organized logically
- Reasonably scannable
- Main points findable

**Needs Improvement:**
- Wall of text without structure
- Can't quickly find relevant section
- No checklists or summaries
- No time estimates

### 6. Self-Consistency

**Excellent:**
- Guidance document demonstrates its own quality criteria
- Examples within the guidance are high quality
- Follows its own best practices
- Meta-guidances validate themselves

**Good:**
- Generally follows own advice
- Minor inconsistencies

**Needs Improvement:**
- Guidance violates its own recommendations
- Examples are poor quality
- Doesn't demonstrate criteria it defines

### 7. Obsidian Compatibility

**Excellent:**
- All boundary elements explicitly linked using `[[file-id]]` syntax
  - Specifications link to parent spec and related guidance
  - Guidance links to related specifications and parent guidance
  - Charts link to vertices, edges, faces for small charts (≤25 elements)
  - Edges link to source and target vertices
  - Faces link to bounding edges
- Tags properly set in frontmatter for Obsidian graph navigation
- IDs follow consistent naming convention (documented below)
- File names match document IDs for easy reference
- Cross-references are bidirectional where appropriate

**Good:**
- Most boundary elements linked
- Tags present
- IDs mostly consistent
- Some cross-references missing

**Needs Improvement:**
- Missing boundary element links (edges without vertex links, faces without edge links)
- No tags in frontmatter
- Inconsistent ID naming
- File names don't match IDs
- Large charts (>50 elements) enumerate all elements in tables (should use programmatic references instead)

**Obsidian Linking Guidelines:**

**Required Links (Boundary Elements):**
- **Edges MUST link** to source and target vertices: `source: [[spec-for-charts]]`, `target: [[guidance-for-charts]]`
- **Faces MUST link** to bounding edges: `edges: [[e:coupling:chart]], [[e:verification:chart:spec-spec]], [[e:validation:chart:chart]]`
- **Specifications MUST link** to parent spec and related guidance
- **Guidance MUST link** to related spec

**Optional Links (Chart Elements):**
- **Charts with ≤25 elements:** Enumerate vertices, edges, faces in tables with links (PREFERRED)
- **Charts with 26-50 elements:** Linking optional, use judgment
- **Charts with >50 elements:** DO NOT enumerate all elements (DISCOURAGED - use programmatic access)

**ID Consistency Requirements:**

**ID Format Pattern:**
```
<prefix>:<type>:<name>

Prefixes:
- v:  vertex (documents)
- e:  edge
- f:  face
- c:  chart
- b0: boundary 0-simplex (root vertex)
- b1: boundary 1-simplex
- b2: boundary 2-simplex

Examples:
- v:spec:chart (specification vertex)
- e:coupling:chart (coupling edge)
- f:assurance:chart (assurance face)
- c:boundary-complex (chart document)
```

**Naming Conventions:**
- Use lowercase with hyphens for multi-word names
- Be descriptive but concise
- Match domain terminology
- For edges, include meaningful context (e.g., `e:verification:chart:spec-spec` not just `e:verification:chart`)

**Why This Matters:**
- Enables Obsidian graph visualization of knowledge complex structure
- Allows quick navigation between related documents
- Supports bidirectional linking for context
- Maintains reference integrity (broken links are detectable)
- Consistent IDs enable programmatic analysis and validation
- Small charts benefit from manual linking; large charts need tooling

## Section-by-Section Guidance

### Purpose Statement

**Purpose:** Explain what this guidance helps assess

**Tips:**
- Start with the user's goal ("This guidance helps you assess...")
- Distinguish from what the spec defines
- Keep to 1-2 sentences
- Connect to user outcomes

**Example:**
> "This guidance helps you assess how well your specification document serves its users by evaluating clarity, completeness, and maintainability."

### Document Overview

**Purpose:** Provide context and set expectations

**Tips:**
- **What This Guidance Covers**: List specific support areas
- **Best Use Cases**: Give 3-5 concrete scenarios
- Include both positive uses and non-uses (when NOT to use)
- Address target audience explicitly

**Anti-patterns:**
- ❌ Generic descriptions that could apply to any guidance

**Preferred:**

- ✅ Specific scenarios that show unique value

### Quality Criteria

**Purpose:** Define what "good" looks like across multiple dimensions

**Tips:**
- Choose 4-7 distinct criteria (too few = shallow, too many = overwhelming)
- Each criterion should assess a different quality aspect
- Use consistent levels across all criteria (e.g., Excellent/Good/Needs Improvement)
- Make levels observable (not subjective feelings)
- Include examples or indicators for each level

**Best Practices:**
- Cover both content (what) and form (how presented)
- Include process criteria (how easy to complete) and outcome criteria (quality of result)
- Make distinctions between levels meaningful (not just "more" vs. "less")

**Anti-patterns:**

- ❌ Binary criteria (that's verification, not validation)
- ❌ All criteria about same dimension (e.g., all about formatting)
- ❌ Levels that aren't actually distinguishable

**Preferred:**

- ✅ 4-7 distinct criteria covering different quality dimensions
- ✅ Consistent levels (Excellent/Good/Needs Improvement) with observable distinctions

### Section-by-Section Guidance

**Purpose:** Help authors complete each section successfully

**Tips:**

- Cover every major section of the supported document type
- For each section, provide:
  - Purpose (why it exists)
  - Tips (how to do it well)
  - Anti-patterns (common mistakes)
  - Preferred patterns (what good looks like)
- Order sections to match the supported document's structure
- Be specific: "Include 4-8 items" not "Include several items"

**Anti-pattern/Preferred Format:**

Always pair anti-patterns with preferred alternatives using this structure:

```markdown
**Anti-patterns:**

- ❌ Bad pattern description
- ❌ Another bad pattern

**Preferred:**

- ✅ Good pattern that addresses the anti-pattern
- ✅ Another good alternative
```

**Quality Indicators:**

- Could a novice successfully complete a section using only your guidance?
- Are anti-patterns paired with preferred alternatives?
- Do preferred patterns directly address what the anti-patterns get wrong?

### Workflow Guidance

**Purpose:** Guide authors through creation process

**Tips:**
- Break into 3-5 phases (not too granular)
- Provide time estimates for each phase
- Include quality checkpoints (questions to ask after each phase)
- Show dependencies (what must complete before what)
- Acknowledge iteration (perfection not required first pass)

**Example Structure:**
```markdown
### Recommended Authoring Sequence

1. **Define Core Criteria** (30-45 min)
   - Draft 4-7 quality criteria
   - Define levels for each

### Quality Checkpoints

- **After Phase 1:** Can you distinguish levels for each criterion?
```

**Time Estimates:**
- Be realistic (not aspirational)
- Provide ranges (30-45 min, not exactly 37 min)
- Include total estimate at end

### Common Issues and Solutions

**Purpose:** Prevent predictable mistakes

**Tips:**
- Use table format for scannability
- Each row: Issue name | Problem description | Solution
- Cover 4-8 most common issues
- Solutions should be specific, actionable
- Draw from real experience or testing

**Example:**
| Issue | Problem | Solution |
|-------|---------|----------|
| Too Abstract | "Be thoughtful" doesn't tell me what to do | "List 3-5 concrete examples per criterion" |

### Best Practices

**Purpose:** Distill wisdom into actionable principles

**Tips:**
- List 8-12 practices (enough for comprehensive guidance)
- Each practice should be independently actionable
- Order from foundational to advanced
- Use imperative voice ("Start simple" not "It is good to start simply")
- Explain the "why" briefly when not obvious

**Anti-patterns:**

- ❌ Platitudes ("Quality matters")
- ❌ Contradictory practices
- ❌ Practices requiring extensive explanation (those need their own sections)

**Preferred:**

- ✅ Actionable imperatives: "Start simple" not "It is good to start simply"
- ✅ 8-12 practices ordered from foundational to advanced

## Workflow Guidance

### Recommended Authoring Sequence

1. **Understand the Spec** (15-30 min)
   - Read the corresponding specification thoroughly
   - Identify structural requirements
   - Note areas where quality can vary despite structural compliance

2. **Draft Quality Criteria** (30-45 min)
   - Identify 4-7 distinct quality dimensions
   - Define 2-3 levels for each
   - Make levels observable
   - Provide indicators or examples

3. **Create Section Guidance** (45-60 min)
   - For each section in spec, write:
     - Purpose
     - Tips (3-5 per section)
     - Anti-patterns with solutions
   - Prioritize sections users struggle with most

4. **Design Workflow** (20-30 min)
   - Break supported document creation into phases
   - Estimate time for each phase
   - Define quality checkpoints
   - Acknowledge iteration

5. **Document Common Issues** (20-30 min)
   - List predictable mistakes
   - Provide specific solutions
   - Use table format

6. **Articulate Best Practices** (15-30 min)
   - Distill lessons into 8-12 practices
   - Make each actionable
   - Order logically

7. **Add Examples and Tools** (15-30 min)
   - Reference excellent examples
   - Document tooling support
   - Include commands or links

8. **Review for Self-Consistency** (15-30 min)
   - Check that guidance demonstrates its own criteria
   - Verify actionability of all advice
   - Ensure comprehensiveness

**Total estimated time:** 3-4 hours for a comprehensive guidance document

### Quality Checkpoints

- **After step 2:** Can you distinguish quality levels for each criterion without ambiguity?
- **After step 3:** Could someone new to the domain use your section guidance successfully?
- **After step 4:** Does the workflow feel natural and complete?
- **After step 8:** Does this guidance document demonstrate excellent quality per its own criteria?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Too Abstract** | Advice like "be thorough" or "use good judgment" | Provide specific criteria: "Include at least 3 examples" or "Cover all 5 quality dimensions" |
| **Structural Focus** | Guidance reads like a spec (required fields, formats) | Move structural requirements to spec; guidance focuses on quality within those constraints |
| **No Levels** | Binary good/bad assessment | Define 2-3 quality levels with observable distinctions |
| **Missing Context** | Criteria without explanation of why they matter | Add "Purpose" to each criterion showing user benefit |
| **Overwhelming** | 20+ criteria or 30+ best practices | Consolidate to 4-7 criteria, 8-12 practices |
| **No Examples** | Only abstract principles | Add concrete examples, anti-patterns, or reference documents |
| **Missing Workflow** | No guidance on authoring sequence | Add phases, time estimates, and quality checkpoints |
| **Passive Voice** | "It is recommended that consideration be given..." | Use imperative: "Consider the user's needs" or "Provide 3-5 examples" |

## Best Practices

1. **Know Your Audience** - Write for the least experienced user who should use this guidance
2. **Be Specific** - "3-5 examples" beats "several examples", "30-45 minutes" beats "not too long"
3. **Show, Don't Just Tell** - Every principle should have a concrete example
4. **Use Consistent Levels** - Pick level names (Excellent/Good/Needs Improvement) and stick with them
5. **Cover Multiple Dimensions** - Quality criteria should address different aspects, not variations on one theme
6. **Pair Problems with Solutions** - Anti-patterns are only useful if you show the correct pattern
7. **Provide Time Estimates** - Users need to plan; be realistic about time required
8. **Include Checkpoints** - Quality checkpoints help users assess progress
9. **Distinguish from Specs** - Guidance defines quality assessment, not structural requirements
10. **Test Your Guidance** - Have someone use it and watch where they struggle
11. **Iterate Based on Use** - Update guidance when patterns emerge from actual usage
12. **Demonstrate Quality** - Your guidance should exemplify the criteria it defines

## Validation vs. Verification

**Verification** (deterministic, against spec-for-guidance):
- Are all required sections present?
- Does it have ≥3 quality criteria?
- Do criteria have ≥2 levels each?
- Is section-by-section guidance provided?

**Validation** (qualitative, against this guidance):
- Is the guidance empathetic and clear?
- Are all tips specific and actionable?
- Does it cover all major sections comprehensively?
- Are quality levels meaningfully distinguishable?
- Is it well-organized and usable?
- Does it demonstrate its own quality criteria?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

✓ **Empathy and Clarity:** Uses clear language, anticipates user needs, provides extensive examples
✓ **Actionability:** Every tip is specific ("8-12 practices" not "many practices"), examples concrete
✓ **Comprehensiveness:** Covers all major sections from Purpose through Self-Consistency
✓ **Leveled Assessment:** All criteria use consistent Excellent/Good/Needs Improvement levels
✓ **Usability:** Well-organized with tables, lists, clear sections, time estimates provided
✓ **Self-Consistency:** This very checklist demonstrates self-validation

## Examples

| Document Name | Purpose | Key Features |
|---------------|---------|--------------|
| Guidance-for-Spec | Guide specification authoring | 5 quality criteria, section-by-section tips, workflow with checkpoints |
| Guidance-for-Guidance (this) | Guide guidance authoring | Self-referential validation, comprehensive coverage of guidance quality |

## Tooling Support

### Verification Commands

```bash
# Verify guidance structure against spec-for-guidance
python scripts/verify_structure.py 00_vertices/my-guidance.md --type vertex

# Verify complete chart including guidance
python scripts/verify_chart.py charts/my-chart.md
```

### Validation Support

Human review using this guidance document. Future tools may include:
- Readability analyzers
- Actionability linters (detect vague language)
- Completeness checkers (section coverage)
- Example validators

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | v:spec:guidance (spec-for-guidance) |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Terminology | VERIFICATION = structural compliance; VALIDATION = quality assessment |
| Self-Reference | This guidance validates itself per its own criteria |

---

**Note:** This guidance is coupled with spec-for-guidance via a coupling edge, forming part of the boundary complex's self-referential foundation.
