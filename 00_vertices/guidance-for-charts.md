---
type: vertex/guidance
extends: doc
id: v:guidance:chart
name: Guidance for Charts
description: Quality criteria and best practices for creating excellent chart documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T20:00:00Z
modified: 2025-12-27T20:00:00Z
dependencies: []
---

# Guidance for Charts

**This guidance defines quality criteria and best practices for creating excellent chart documents.**

## Purpose

While spec-for-charts defines what structural elements must be present, this guidance helps authors assess **how well** a chart serves its analytical purpose. Great charts are purposeful, coherent, well-scoped, and interpretable.

## Fundamental Distinction: Chart Documents vs Topological Objects

**CRITICAL:** Chart markdown files serve a dual role that must be clearly understood:

### Chart as Document (Vertex)

A chart markdown file is **first and foremost a document** in the knowledge complex:
- **Type:** `vertex/chart` or `chart/<subtype>` (e.g., `chart/assurance_audit`)
- **Inheritance:** `chart` extends `doc` which extends `vertex`
- **Identity:** Has an ID (e.g., `c:boundary-complex`)
- **Assurable:** Because it's a vertex/document, it can be verified and validated
- **Referenceable:** Can be referenced by its ID in other charts

**Example:** The file `boundary-complex.md` is a document/vertex that can be:
- Verified against spec-for-charts (structural compliance)
- Validated against guidance-for-charts (quality assessment)
- Referenced in other charts (e.g., as an audit target)
- Included in assurance networks as a vertex

### Chart as Description (Topological Object)

The same chart markdown file **describes** a topological object:
- **Contains:** Vertices (V), edges (E), faces (F)
- **Properties:** Euler characteristic (χ = V - E + F), dimension
- **Structure:** A simplicial complex with oriented simplices
- **Purpose:** Visualizes/analyzes relationships in the knowledge complex

**Example:** The content within `boundary-complex.md` describes a topological chart with:
- V = 5 vertices (b0:root, v:spec:spec, etc.)
- E = 6 edges (coupling, verification, validation)
- F = 4 faces (assurance triangles)
- χ = 3

### Self-Reference is Valid

**A chart document can reference itself as a vertex:**

```yaml
# In c:assurance_audit:boundary-complex
type: chart/assurance_audit
id: c:assurance_audit:boundary-complex

# This same chart could be referenced in another chart:
# In c:chart-types-audit
vertices:
  - c:assurance_audit:boundary-complex  # Reference to the chart document as a vertex
```

The document `c:assurance_audit:boundary-complex` is a vertex that happens to describe a topological object. That vertex can be referenced by its ID in any chart, including potentially in itself (though this would create a self-referential structure).

### Implications for Chart Authors

**When creating a chart, remember:**

1. **You are writing a document** - Follow document best practices (clear writing, proper structure, metadata)
2. **You are describing an object** - Follow topological rules (valid simplicial complex, proper orientation)
3. **The document can be assured** - Because it's a vertex, it can have verification/validation edges
4. **The document can be referenced** - Other charts can reference this chart by its ID
5. **Don't confuse the two** - The document has type `vertex/chart`; the object it describes has V, E, F

**Common Confusion to Avoid:**
- ❌ "This chart is a topological object, so it can't be a vertex"
- ✅ "This chart **document** is a vertex that **describes** a topological object"

**Example in Practice:**
- Document: `c:assurance_audit:boundary-complex` (type: `vertex/chart`)
- Verifies against: `v:spec:assurance_audit` (checks document structure)
- Validates against: `v:guidance:assurance_audit` (checks document quality)
- Describes: A topological chart with V=5, E=6, F=4 (the object)

This dual nature is what makes charts both analyzable (as documents) and analytical (as descriptions of structure).

## Document Overview

### What This Guidance Covers

This guidance supports authors creating chart documents by providing:
- Quality assessment criteria for charts
- Best practices for chart construction and documentation
- Common pitfalls in chart design and solutions
- Section-by-section authoring advice
- Workflow recommendations for chart creation

### Best Use Cases

Use this guidance when:
- Creating a new chart to visualize or analyze part of the knowledge complex
- Reviewing an existing chart for quality and fitness-for-purpose
- Teaching others how to construct meaningful charts
- Evaluating whether a chart effectively addresses its intended purpose
- Deciding what elements to include or exclude from a chart

## Quality Criteria

### 1. Purpose Clarity

**Excellent:**
- Chart has clear, specific motivation (answers a defined question)
- Intended use and audience are explicit
- Context explains why chart was needed
- Success criteria for chart are stated

**Good:**
- General purpose is clear
- Audience can be inferred
- Some context provided

**Needs Improvement:**
- Purpose is vague ("visualize the system")
- No clear question being answered
- Missing context for why chart exists

### 2. Scope Coherence

**Excellent:**
- Included elements form a meaningful unit
- Exclusions are deliberate and justified
- Boundaries are well-defined
- Chart forms complete subcomplex (no dangling references)

**Good:**
- Elements mostly related
- Most boundaries clear
- Valid subcomplex

**Needs Improvement:**
- Random collection of elements
- No clear inclusion/exclusion rationale
- Incomplete boundaries (missing sources/targets)
- Invalid simplicial complex

### 3. Construction Documentation

**Excellent:**
- Step-by-step construction process documented
- Sources consulted are listed
- Decision rationale explained
- Quality assurance approach described
- Constructor and method clearly stated

**Good:**
- Basic process documented
- Constructor identified
- Some decisions explained

**Needs Improvement:**
- No process documentation
- Unknown how elements were selected
- Missing constructor information

### 4. Element Coverage

**Excellent:**
- All elements listed in structured tables
- Each element has clear role in chart context
- Counts match between frontmatter and body
- All IDs resolve correctly

**Good:**
- Elements listed
- Minor count mismatches
- Most roles clear

**Needs Improvement:**
- Missing elements in tables
- Counts don't match frontmatter
- Unclear what elements represent
- Broken references

### 5. Topological Awareness

**Excellent:**
- Euler characteristic computed correctly
- Connectivity analyzed
- Holes/cycles identified and interpreted
- Structural patterns recognized
- Topological properties related to domain meaning

**Good:**
- Basic topology computed
- Connectivity stated
- Some analysis attempted

**Needs Improvement:**
- No topological analysis
- Incorrect computations
- Properties not interpreted

### 6. Interpretability

**Excellent:**
- Key observations clearly stated
- Insights connect topology to domain
- Implications explained
- Limitations acknowledged
- Anomalies noted and investigated

**Good:**
- Some observations made
- Basic interpretation attempted
- Major insights captured

**Needs Improvement:**
- No interpretation provided
- Just lists elements without insight
- Missing obvious patterns
- Ignores anomalies

### 7. Verifiability

**Excellent:**
- Verification commands provided
- Expected results stated
- All checks documented
- Chart passes structural verification
- All referenced elements exist

**Good:**
- Basic verification described
- Chart mostly verifies
- Few broken references

**Needs Improvement:**
- No verification approach
- Chart fails structural checks
- Many broken references
- Cannot be verified

### 8. Visualization Support

**Excellent (if visualizations exist):**
- Multiple visualization formats available
- Visualization metadata complete (file, format, generator, date)
- Interpretation guide explains how to read visualizations
- Recommended view specified
- Visualizations match chart content

**Good:**
- At least one visualization
- Basic metadata present
- Visualization mostly matches chart

**Needs Improvement:**
- Visualization metadata incomplete
- Visualizations don't match chart
- No interpretation guide

**Note:** Visualizations are optional. Charts without visualizations can still be Excellent if all other criteria are met.

### 9. Metadata Completeness

**Excellent:**
- All construction metadata present (who, how, when)
- Purpose and scope clearly stated
- Version and timestamps current
- Tags appropriate
- Related charts documented

**Good:**
- Core metadata present
- Some optional fields missing
- Generally current

**Needs Improvement:**
- Missing required metadata
- Outdated timestamps
- Inconsistent metadata

### 10. Maintainability

**Excellent:**
- Clear relationship to other charts
- Versioning strategy evident
- Update process documented
- Dependencies tracked
- Owner/maintainer identified

**Good:**
- Version tracked
- Some relationships documented
- Owner can be determined

**Needs Improvement:**
- No version control
- Orphaned chart (no owner)
- Unknown relationships
- Cannot determine update process

### 11. Reference/Referent Clarity

**Excellent:**
- Clear distinction between chart document (reference) and described object (referent)
- Explicitly acknowledges dual nature where relevant
- Uses precise language: "this document" vs "the chart described by this document"
- Frontmatter correctly uses `type: vertex/chart` or `chart/<subtype>`
- No conflation of document properties with object properties
- When discussing topology (V, E, F, χ), clearly states this describes the object
- When discussing assurance, clearly states this applies to the document

**Good:**
- Generally maintains distinction
- Occasional imprecise language but context makes meaning clear
- Type field correct
- Mostly separates document from object properties

**Needs Improvement:**
- Confuses document with object (e.g., "this chart has χ=5" when should say "this document describes a chart with χ=5")
- Incorrect type field (e.g., `type: chart` instead of `type: vertex/chart`)
- Mixes document metadata with object properties without clarification
- Unclear whether statements apply to document or described object
- Claims document has topological properties that belong to described object

**Common Issues to Avoid:**
- ❌ "This chart is a 2-dimensional simplicial complex" (conflates document with object)
- ✅ "This document describes a 2-dimensional simplicial complex"
- ❌ "Type: chart/assurance_audit" in source_type field (should be vertex/chart)
- ✅ "Type: vertex/chart" with subtype assurance_audit in document type field
- ❌ "The chart can be verified" (unclear - document or object?)
- ✅ "The chart document can be verified" or "This document (which describes a chart) can be verified"

**Why This Matters:**
- Prevents confusion in assurance network (what is being assured?)
- Ensures correct typing for verification/validation edges
- Clarifies whether properties are intrinsic to document or described object
- Maintains conceptual clarity in meta-levels (documents about documents about objects)

### 12. Obsidian Compatibility

**Excellent:**
- For small charts (≤25 elements): All vertices, edges, faces linked using `[[element-id]]`
- For all charts: Vertices/edges/faces in element tables include links to their definitions
- Chart metadata links to related specs and guidance
- Tags properly set in frontmatter for graph navigation
- ID follows consistent naming convention (c:<chart-name>)
- File name matches document ID

**Good:**
- Most elements linked for small charts
- Metadata links present
- Tags present
- ID mostly consistent

**Needs Improvement:**
- Small chart (<25 elements) missing element links
- Large chart (>50 elements) attempts to link all elements (discouraged)
- No metadata links
- No tags in frontmatter
- Inconsistent ID format

**Obsidian Linking Guidelines for Charts:**

**Chart Size Categories:**
- **Small (≤25 elements):** Link all vertices, edges, faces in tables - PREFERRED
- **Medium (26-50 elements):** Use judgment - link key elements
- **Large (>50 elements):** DO NOT enumerate all elements - use programmatic access only

**Required Links:**
- Link to specification this chart type follows (e.g., `[[spec-for-charts]]`)
- Link to guidance used for quality (e.g., `[[guidance-for-charts]]`)

**Why This Matters:**
- Small charts benefit from manual navigation in Obsidian
- Large charts create visual clutter and performance issues if fully linked
- Metadata links establish document relationships
- Enables discovery of related charts and specifications

## Section-by-Section Guidance

### Why This Chart Exists

**Purpose:** Justify the chart's existence and set expectations

**Tips:**
- Start with a specific question or need
- Explain what prompted chart creation
- Define intended audience explicitly
- State how success will be measured

**Anti-patterns:**
- ❌ "To visualize things" (too vague)
- ✅ "To identify all verification edges in the boundary complex for validation analysis"
- ❌ "Chart of the system" (no specific purpose)
- ✅ "Chart showing temporal evolution of feature development to identify bottlenecks"

### What This Chart Contains

**Purpose:** Define scope precisely and summarize contents

**Tips:**
- Be explicit about what's included AND excluded
- Explain exclusion rationale
- Provide element counts with descriptions
- State dimension clearly

**Anti-patterns:**
- ❌ Lists elements but doesn't explain why
- ✅ Lists elements with rationale for each inclusion
- ❌ "Includes relevant edges" (what's relevant?)
- ✅ "Includes all coupling edges between boundary complex vertices (4 edges total)"

### How This Chart Was Constructed

**Purpose:** Document process for reproducibility and trust

**Tips:**
- Describe step-by-step process
- List sources consulted
- Explain decision points
- Document QA approach
- Match frontmatter metadata exactly

**Anti-patterns:**
- ❌ "Created manually" (no detail)
- ✅ "1. Listed all vertices in boundary complex from cache, 2. Filtered for type=spec|guidance, 3. Verified all exist, 4. Computed properties"
- ❌ No quality assurance mentioned
- ✅ "Verified with verify_chart.py, checked Euler characteristic manually, confirmed all IDs resolve"

### Element Tables (Vertices, Edges, Faces)

**Purpose:** Provide structured, queryable element listings

**Tips:**
- Include all elements from frontmatter
- Provide meaningful "role in chart" descriptions
- Use consistent formatting
- Link to element files where helpful
- Ensure counts match

**Anti-patterns:**
- ❌ Table has 5 vertices but frontmatter lists 6
- ✅ Counts match exactly between frontmatter and tables
- ❌ "Role in chart: vertex" (not informative)
- ✅ "Role in chart: Self-referential foundation spec enabling spec verification"

### Chart Properties

**Purpose:** Analyze topological and structural characteristics

**Tips:**
- Always compute Euler characteristic if faces present
- State connectivity explicitly
- Identify cycles and their meaning
- Note patterns (regularity, hierarchies, symmetries)
- Connect properties to domain meaning

**Anti-patterns:**
- ❌ χ = 0 (incorrect calculation)
- ✅ χ = V - E + F = 4 - 6 + 3 = 1 (shows work)
- ❌ "Connected: Yes" (no detail)
- ✅ "Connected: Yes (single component, no isolated vertices)"
- ❌ Lists properties without interpretation
- ✅ "Euler characteristic = 1 suggests single hole, corresponding to incomplete tetrahedron"

### Verification

**Purpose:** Make chart verifiable by others

**Tips:**
- Provide exact verification commands
- State expected results
- List all checks performed
- Include topology analysis if relevant
- Make commands copy-pasteable

**Anti-patterns:**
- ❌ "This chart is valid"
- ✅ "python scripts/verify_chart.py charts/test-tetrahedron.md" with expected output
- ❌ No verification commands
- ✅ Complete verification script with expected pass/fail

### Interpretation (Recommended Section)

**Purpose:** Extract insights and meaning from the chart

**Tips:**
- State what the chart reveals clearly
- List key observations as bullets
- Explain implications for decisions or understanding
- Acknowledge limitations explicitly
- Note surprises or anomalies

**Anti-patterns:**
- ❌ Skipping interpretation entirely
- ✅ "This chart reveals that all 4 boundary docs have complete assurance triangles"
- ❌ "Chart shows stuff" (vague)
- ✅ "Chart reveals 3 coupling patterns: self-referential (SS, GG), cross-domain (SG, GS), forming symmetric structure"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define Purpose and Scope** (15-30 min)
   - Write Why section first
   - Define inclusion/exclusion criteria
   - Identify intended audience
   - Set success criteria

2. **Construct Element Lists** (30-60 min)
   - Query cache or manually select elements
   - Populate frontmatter arrays
   - Verify all IDs resolve
   - Check boundaries are complete

3. **Document Construction Process** (15 min)
   - Write How section while fresh in mind
   - Record steps taken
   - Note sources used
   - Document QA approach

4. **Build Element Tables** (30-45 min)
   - Create Vertices, Edges, Faces tables
   - Add meaningful role descriptions
   - Verify counts match frontmatter
   - Check all IDs resolve

5. **Analyze Properties** (20-30 min)
   - Compute Euler characteristic
   - Check connectivity
   - Identify cycles/holes
   - Note structural patterns
   - Run verify_chart.py

6. **Interpret Findings** (30-45 min)
   - Analyze what chart reveals
   - Extract key observations
   - Identify implications
   - Note limitations
   - Document anomalies

7. **Add Verification** (10 min)
   - Provide verification commands
   - State expected results
   - Document checks

8. **Optional: Create Visualizations** (variable)
   - Generate visual artifacts
   - Document in visualizations array
   - Add interpretation guide

### Quality Checkpoints

- **After step 2:** Do all referenced elements exist? Does the chart form a valid subcomplex?
- **After step 4:** Do counts match between frontmatter and tables?
- **After step 5:** Does verify_chart.py pass? Is Euler characteristic correct?
- **After step 6:** Does the interpretation answer the question from step 1?
- **After step 8:** Do visualizations match chart contents exactly?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Scope Creep** | Chart grows to include "everything related" | Return to purpose statement. Ask "Does this element help answer the motivating question?" |
| **Dangling References** | Chart includes edges but not their vertices | Run verify_chart.py early and often. Always include boundary elements. |
| **Missing Motivation** | Chart created "because we can" | Don't create chart until you have a specific question or need. |
| **Count Mismatches** | Frontmatter says 10 vertices but table has 9 | Use script to generate tables from frontmatter, or double-check manually. |
| **Incorrect Topology** | Euler characteristic wrong | Double-check V, E, F counts. Remember χ = V - E + F. Use topology.py to verify. |
| **Uninterpretable** | Chart is structurally valid but meaningless | Add Interpretation section. If you can't extract insights, revisit scope and purpose. |
| **Stale Charts** | Chart created once, never updated | Add Related Charts section. Version charts. Document update criteria. |
| **Tool Failures** | verify_chart.py fails on valid chart | Rebuild cache: `python scripts/build_cache.py`. Check element files exist. |

## Best Practices

### Chart Construction

1. **Start with a question** - Don't create charts without a specific analytical purpose
2. **Define scope before building** - Write inclusion/exclusion criteria first
3. **Verify early and often** - Run verify_chart.py after every major addition
4. **Document as you go** - Write construction process while building, not after
5. **Include complete boundaries** - If you include an edge, include its vertices; if a face, include its edges

### Element Selection

6. **Be deliberate about exclusions** - Explain why elements are NOT included
7. **Form valid subcomplexes** - Chart should be a coherent unit, not random collection
8. **Check all references resolve** - Every ID should point to an existing element
9. **Avoid scope creep** - Resist temptation to include "everything"
10. **Document sources** - Record where elements came from (query, manual selection, etc.)

### Analysis and Interpretation

11. **Compute topology** - Always calculate Euler characteristic if faces present
12. **Interpret properties** - Connect topology to domain meaning
13. **Note anomalies** - Call out surprising patterns or missing elements
14. **State limitations** - Acknowledge what the chart doesn't show
15. **Extract insights** - Don't just list elements, explain what they reveal

### Verification and Quality

16. **Make charts verifiable** - Provide verification commands and expected results
17. **Match counts** - Ensure frontmatter and table counts agree
18. **Test verification** - Actually run verify_chart.py, don't assume it passes
19. **Update timestamps** - Keep modified dates current
20. **Version appropriately** - Bump version when elements change

## Examples

### Excellent Chart Example

[Test Tetrahedron Chart](../charts/test-tetrahedron.md) demonstrates:
- ✓ Clear purpose (validation test baseline)
- ✓ Explicit scope (4 vertices, 6 edges, 3 faces)
- ✓ Deliberate hole (missing beta-gamma-delta face)
- ✓ Complete documentation
- ✓ Topological analysis (χ = 1)
- ✓ Verification commands
- ✓ Expected tool behavior documented

## Validation vs. Verification

**Verification** (deterministic, against spec-for-charts):
- All required frontmatter fields present
- All required sections present
- Element counts match
- Valid simplicial complex
- All IDs resolve

**Validation** (qualitative, against this guidance):
- Purpose is clear and specific
- Scope is coherent and justified
- Construction process documented
- Properties analyzed and interpreted
- Insights extracted
- Limitations acknowledged
- Overall fitness-for-purpose

## Tooling Support

### Verification Commands

```bash
# Verify chart structure
python scripts/verify_chart.py charts/your-chart.md

# Analyze topology
python scripts/topology.py charts/your-chart.md

# Rebuild cache if needed
python scripts/build_cache.py
```

### Validation Support

Chart validation is primarily manual review against the 10 quality criteria above. Future tooling may support:
- Automated element counting verification
- Topology computation verification
- Frontmatter/body consistency checking
- LLM-assisted quality assessment

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

✓ **Purpose Clarity:** Clear statement of helping authors create excellent charts
✓ **Scope Coherence:** Focused on chart documents, not other doc types
✓ **Construction Documentation:** Created following guidance-for-guidance template
✓ **Interpretability:** Provides actionable quality criteria
✓ **Metadata Completeness:** All required frontmatter present
✓ **Maintainability:** Versioned, timestamped, with clear ownership

---

**Note:** This guidance pairs with spec-for-charts via a coupling edge. The spec defines structure; this guidance defines quality. Together they enable full assurance (verification + validation) for chart documents.
