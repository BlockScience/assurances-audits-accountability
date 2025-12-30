---
type: vertex/guidance
extends: doc
id: v:guidance:assurance_audit
name: Guidance for Assurance Audit Documents
description: Best practices and quality criteria for creating effective assurance audit charts
tags:
  - vertex
  - doc
  - guidance
  - assurance
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
dependencies: []
---

# Guidance for Assurance Audit Documents

**This guidance provides best practices, patterns, and quality criteria for creating effective assurance audit charts in the knowledge complex.**

## Purpose

While spec-for-assurance-audits defines what assurance audits MUST contain, this guidance helps you create HIGH-QUALITY audits that provide maximum trust and value.

## Fundamental Distinction: Assurance-Audit Documents vs Topological Objects

**CRITICAL:** Assurance-audit chart files are a special case of charts with the same dual nature:

### Assurance-Audit as Document (Vertex)

An assurance-audit markdown file is **a document** in the knowledge complex:
- **Type:** `vertex/chart` or `chart/assurance_audit` (extends chart, extends doc, extends vertex)
- **Inheritance Chain:** `assurance_audit` → `chart` → `doc` → `vertex`
- **Identity:** Has an ID (e.g., `c:assurance_audit:boundary-complex`)
- **Assurable:** Because it's a vertex/document, it can be verified and validated
- **Referenceable:** Can be referenced by its ID in other charts

**Example:** The file `boundary-complex-assurance-audit.md` is a document/vertex that:
- Verifies against spec-for-assurance-audits (structural compliance)
- Validates against guidance-for-assurance-audits (this guidance - quality assessment)
- Can be referenced in other charts (e.g., in chart-types-audit)
- Participates in assurance networks as a vertex

### Assurance-Audit as Description (Topological Object)

The same assurance-audit markdown file **describes** a topological chart focused on assurance:
- **Contains:** Vertices (being audited), edges (assurance relationships), faces (assurance triangles)
- **Properties:** Euler characteristic, audit coverage percentage
- **Structure:** A simplicial complex representing the assurance network
- **Purpose:** Documents and validates assurance status of target vertices

**Example:** The content within `boundary-complex-assurance-audit.md` describes a topological chart with:
- V = 5 vertices (the elements being audited: b0:root, v:spec:spec, etc.)
- E = 6 edges (verification, validation, coupling edges)
- F = 4 faces (assurance triangles proving vertices are assured)
- Audit verdict: PASS, 100% coverage

### Critical Implication for Assurance-Audits

**The assurance-audit document itself can and should be assured:**

```yaml
# The document c:assurance_audit:boundary-complex is a vertex
# It has its own assurance triangle:

Vertices: [c:assurance_audit:boundary-complex, v:spec:assurance_audit, v:guidance:assurance_audit]
Edges: [verification, validation, coupling]
Face: f:assurance:boundary-complex-assurance-audit

# This assurance triangle proves the AUDIT DOCUMENT is trustworthy
# Separately, the audit document describes vertices being audited
```

**Two levels of assurance:**
1. **The audit document is assured** - We trust the audit itself is valid (via f:assurance:boundary-complex-assurance-audit)
2. **The audit assures other vertices** - The audit document describes which vertices are assured (its content)

### Self-Reference in Assurance-Audits

**An assurance-audit can reference itself as a vertex:**

If you create an assurance-audit that audits chart instances, the audit document itself could theoretically be one of the audit targets (though this would be uncommon in practice).

**More common:** An assurance-audit is assured by its own assurance face, then referenced in a higher-level audit:

```yaml
# In c:assurance_audit:chart-types
audit_targets:
  - v:spec:chart
  - v:spec:assurance_audit
  - c:assurance_audit:boundary-complex  # Reference to another audit as vertex
```

### Implications for Audit Authors

**When creating an assurance-audit, remember:**

1. **You are writing a document** - It must verify against spec-for-assurance-audits
2. **You are describing an assurance network** - The object contains vertices, edges, faces
3. **The document itself needs assurance** - Create verification/validation edges for the audit document
4. **The document describes assurance of others** - The content audits target vertices
5. **Document type is `vertex/chart`** - Even though it describes a chart, it's a vertex in the knowledge complex

**Common Confusion to Avoid:**
- ❌ "This is an assurance-audit chart, so it's type chart/assurance_audit, not vertex"
- ✅ "This **document** has type vertex/chart (with subtype assurance_audit) and **describes** an assurance-audit chart"
- ❌ "Assurance-audits audit things, so they don't need their own assurance"
- ✅ "Assurance-audit **documents** must be assured to establish trust in the audit results"

**Example in Practice:**
- Audit Document: `c:assurance_audit:boundary-complex` (type: `vertex/chart`)
- Document's Assurance: Verified against `v:spec:assurance_audit`, validated against `v:guidance:assurance_audit`
- Document's Purpose: Describes assurance status of boundary complex vertices
- Described Object: Topological chart with V=5, E=6, F=4 (the assurance network being documented)

**Why This Matters:**
- Ensures audit documents are trustworthy (document-level assurance)
- Ensures audit results are valid (content-level verification)
- Enables audits to be referenced in higher-level analyses
- Maintains consistency: all charts follow the same patterns

## When to Create an Assurance Audit

### Good Use Cases ✅

**Quality Gates:**
- Before releasing a new version of documentation
- Before promoting content from draft to stable
- At milestones in knowledge complex development

**Trust Establishment:**
- When stakeholders need proof of assurance
- When documenting foundational elements
- When establishing baseline trust anchors

**Compliance Verification:**
- Periodic compliance checks
- After major structural changes
- When assurance patterns change

**Scope Validation:**
- Validating a specific subdomain is fully assured
- Checking assurance of a release candidate
- Verifying assurance propagation after changes

### Poor Use Cases ❌

**Too Broad:**
- Entire knowledge complex (may be infeasible)
- Unrelated scattered elements
- Multiple independent domains mixed

**Too Narrow:**
- Single vertex (trivial, not worth audit overhead)
- Elements known to lack assurance
- Draft/experimental content

**Premature:**
- Before content is stable
- During active development
- When assurance is incomplete by design

## Audit Scope Selection

### Principles for Good Scope

**Coherent:**
- Elements should relate to each other
- Should form a meaningful subcomplex
- Should have clear boundaries

**Complete:**
- Include all vertices in scope
- Include all assurance faces for those vertices
- Don't cherry-pick passing elements

**Purposeful:**
- Scope should answer a specific question
- Should support a specific use case
- Should have clear stakeholders

### Scope Patterns

**Domain Audit:**
```
Scope: All vertices of type X and their assurance
Example: All chart-type vertices (chart, assurance_audit)
```

**Layer Audit:**
```
Scope: All vertices at abstraction level Y
Example: All foundational documents (SS, SG, GS, GG)
```

**Release Audit:**
```
Scope: All vertices changed in release Z
Example: All new content in v2.0.0
```

**Dependency Audit:**
```
Scope: Vertex V and all its dependencies
Example: assurance_audit type and everything it depends on
```

## Assurance Coverage Strategies

### 100% Coverage (PASS Status)

**When to Aim For:**
- Foundational elements
- Production-ready content
- Trust-critical domains

**How to Achieve:**
- Start with spec and guidance for domain
- Create verification edges with structural checks
- Create validation edges with quality assessments
- Build assurance faces completing triangles
- Use boundary assurance (b2) for self-referential cases

**Validation:**
- Every vertex has >= 1 valid assurance face
- All faces form valid triangles
- All edges have results
- No gaps in coverage

### Partial Coverage (PARTIAL Status)

**When Acceptable:**
- Work in progress documentation
- Non-critical auxiliary content
- Known gaps with remediation plan

**How to Document:**
- Clearly identify assured vs unassured vertices
- Categorize gaps by severity
- Provide remediation timeline
- Document blockers

### Identifying Gaps

**Gap Categories:**

**Critical Gaps (🔴):**
- Foundational vertices without assurance
- Required dependencies unassured
- Trust-anchor elements missing

**Warning Gaps (🟡):**
- Important but not foundational
- Partial assurance present
- Non-blocking for most use cases

**Minor Gaps (🟢):**
- Optional/auxiliary elements
- Low-priority content
- Experimental features

## Assurance Quality Assessment

### Evaluating Assurance Strength

**Strong Assurance:**
- Multiple assurance faces per vertex
- Verification checks comprehensive (>15 checks)
- Validation assessment detailed and recent
- Clear coupling alignment
- Evidence of thorough review

**Adequate Assurance:**
- One assurance face per vertex
- Verification checks pass (>10 checks)
- Validation assessment present
- Coupling exists
- Basic review completed

**Weak Assurance:**
- Minimal verification checks (<10)
- Validation perfunctory
- Coupling unclear
- Limited review

### Red Flags

**Structural Issues:**
- Self-loops without boundary resolution
- Degenerate triangles (edges don't connect properly)
- Missing edges in assurance triangles
- Invalid face topology

**Process Issues:**
- Verification without actual checks
- Validation without quality assessment
- Automatic generation without review
- Stale assurance (old timestamps)

**Coverage Issues:**
- Cherry-picked passing elements
- Excluded critical dependencies
- Incomplete face sets
- Missing boundary elements for self-referential cases

## Documentation Best Practices

### Vertex Assurance Status Table

**Good Example:**

| Vertex ID | Name | Status | Face(s) | Type | Notes |
|-----------|------|--------|---------|------|-------|
| v:spec:chart | Spec for Charts | ✅ ASSURED | f:assurance:chart | standard | Comprehensive verification (17 checks) |
| v:guidance:chart | Guidance for Charts | ✅ ASSURED | f:assurance:chart | standard | Excellent quality assessment |

**What Makes It Good:**
- Clear status indicators (✅/❌)
- Lists specific assurance faces
- Notes assurance type (standard/boundary/mixed)
- Provides relevant context

**Poor Example:**

| Vertex | Status |
|--------|--------|
| chart | OK |
| audit | OK |

**What's Wrong:**
- No vertex IDs
- Vague status
- No face references
- No context

### Assurance Face Validation Table

**Good Example:**

| Face ID | Target | Type | Edges | Status | Notes |
|---------|--------|------|-------|--------|-------|
| f:assurance:chart | v:spec:chart | standard | ✅ (3/3) | VALID | Coupling + verification + validation all valid |
| b2:spec-spec | v:spec:spec | boundary | ✅ (3/3) | VALID | Boundary assurance via root, resolves self-reference |

**What Makes It Good:**
- Specific face and target IDs
- Clear type distinction
- Edge validation count
- Explanatory notes

### Gap Analysis

**Good Gap Documentation:**

```markdown
## Assurance Gaps

### Critical Gaps

None identified ✅

### Warnings

**v:guidance:assurance_audit** - Only single assurance face
- **Severity:** 🟡 Warning
- **Impact:** Guidance adequately assured but could be strengthened
- **Remediation:** Add cross-domain assurance from chart guidance
- **Timeline:** Next release
- **Blocker:** None

### Minor Gaps

None
```

**What Makes It Good:**
- Categorized by severity
- Specific vertex IDs
- Impact assessment
- Remediation plan
- Timeline and blockers

## Audit Execution Process

### Step 1: Define Scope

1. Identify purpose of audit
2. Select vertices to include
3. Determine boundaries
4. Document inclusion/exclusion criteria

### Step 2: Gather Elements

1. List all vertices in scope
2. Find all assurance faces referencing those vertices
3. Identify all edges in those faces
4. Check for missing faces

### Step 3: Validate Assurance

1. For each vertex, verify at least one valid assurance face
2. For each face, verify valid triangle structure
3. For each edge, verify validation results exist
4. Document findings

### Step 4: Analyze Coverage

1. Calculate coverage percentage
2. Categorize assurance types (standard/boundary/mixed)
3. Assess assurance depth (# faces per vertex)
4. Identify gaps

### Step 5: Assess Compliance

1. Check against Assurance Triangle Specification
2. Verify proper use of boundary elements
3. Validate edge check results
4. Document deviations

### Step 6: Determine Status

1. If 100% coverage + all valid → PASS
2. If some gaps with plan → PARTIAL
3. If critical gaps → FAIL

### Step 7: Document Results

1. Complete all required sections
2. Provide evidence and commands
3. Include reproducibility instructions
4. Add interpretation and recommendations

## Common Patterns

### Foundational Domain Audit

**Pattern:**
- Scope: Self-referential foundational vertices (SS, GG) + cross-domain (SG, GS) + root
- Assurance: Mixed (boundary for SS/GG, standard for SG/GS)
- Status: PASS (100% coverage required for foundation)

**Example:** Boundary Complex audit

### Extension Domain Audit

**Pattern:**
- Scope: Extended type + its spec and guidance
- Assurance: Standard (non-self-referential)
- Status: PASS (extensions must be fully assured)

**Example:** Chart types audit (chart + assurance_audit)

### Release Audit

**Pattern:**
- Scope: New/modified vertices in release
- Assurance: Mixed depending on elements
- Status: PASS or PARTIAL (may have planned future work)

**Example:** v2.0.0 release audit

## Quality Checklist

### Before Declaring PASS

- [ ] Every vertex has >= 1 valid assurance face
- [ ] All faces form valid triangles (3 vertices, 3 edges)
- [ ] All verification edges have structural check results
- [ ] All validation edges have quality assessments
- [ ] All coupling edges properly align spec and guidance
- [ ] Boundary elements (b0/b1/b2) used correctly
- [ ] No degenerate structures
- [ ] Documentation complete
- [ ] Reproducible verification commands provided
- [ ] Compliance against specification verified
- [ ] Reference/referent clarity maintained (document vs described object)

### Reference/Referent Clarity Assessment

**Excellent:**
- Audit document clearly distinguishes itself (the document) from the assurance network it describes (the object)
- Uses precise language: "this audit document" vs "the assurance network described in this document"
- Correctly uses `type: vertex/chart` with subtype `assurance_audit`
- When reporting topology (V, E, F, χ), clearly states these are properties of the described assurance network
- When discussing document assurance, clearly states this applies to the audit document itself
- No conflation of "audit targets" (vertices being audited) with "audit document" (the vertex describing the audit)

**Good:**
- Generally maintains distinction
- Occasional imprecise language but context makes meaning clear
- Type fields correct in frontmatter
- Separates document from network properties

**Needs Improvement:**
- Confuses audit document with assurance network (e.g., "this audit has 5 vertices" when should say "this audit document describes an assurance network with 5 vertices")
- Incorrect type field (e.g., missing `vertex/` prefix)
- Mixes document metadata with network properties
- Unclear whether "assurance" refers to document assurance or assurance of targets
- Claims document has network properties that belong to described network

**Common Issues to Avoid:**
- ❌ "This audit is a simplicial complex with 8 faces" (conflates document with network)
- ✅ "This audit document describes an assurance network (a simplicial complex) with 8 faces"
- ❌ "The audit can be verified" (unclear - document or network?)
- ✅ "The audit document can be verified against spec-for-assurance-audits"
- ❌ "The audit assures these vertices" (audit is the document, not the assurance network)
- ✅ "This audit document describes an assurance network that assures these vertices"

**Two Levels of Assurance:**
1. **Document-Level:** The audit document itself must be assured (verified against SAA, validated against GAA)
2. **Content-Level:** The audit document DESCRIBES which vertices are assured in the network

**Why This Matters for Audits:**
- Prevents confusion about what is being assured (the audit itself vs the audit's targets)
- Clarifies that audit documents need their own assurance to be trustworthy
- Ensures correct typing in assurance networks (audit documents are vertices)
- Maintains clarity in meta-levels (audits about audits about documents)

### Obsidian Compatibility

- [ ] For small audits (≤25 elements): All audit targets, edges, faces linked using `[[element-id]]`
- [ ] For all audits: Audit targets table includes links to target documents
- [ ] Audit metadata links to spec-for-assurance-audits and guidance-for-assurance-audits
- [ ] Tags properly set in frontmatter
- [ ] ID follows consistent naming convention (c:assurance_audit:<name>)
- [ ] File name matches document ID

**Obsidian Linking for Assurance Audits:**

**Required Links:**
- Link to `[[spec-for-assurance-audits]]` (specification being followed)
- Link to `[[guidance-for-assurance-audits]]` (guidance used for quality)
- Link all audit targets using `[[target-id]]` in audit targets section

**Size-Based Linking:**
- **Small audits (≤25 vertices audited):** Link all vertices, edges, faces in tables
- **Medium audits (26-50 vertices):** Link audit targets and key assurance faces
- **Large audits (>50 vertices):** Link audit targets only, use programmatic access for full network

**Why This Matters:**
- Enables navigation from audit to audited elements
- Shows audit coverage in Obsidian graph view
- Supports traceability of audit findings
- Balances manual linking (small audits) with programmatic access (large audits)

### Before Declaring PARTIAL

- [ ] Coverage percentage calculated accurately
- [ ] All gaps identified and categorized
- [ ] Gap severity assessed (critical/warning/minor)
- [ ] Remediation plan documented
- [ ] Timeline for remediation provided
- [ ] Blockers identified
- [ ] Non-critical gaps justified

### Before Declaring FAIL

- [ ] Critical gaps clearly documented
- [ ] Impact assessment completed
- [ ] Root cause analysis performed
- [ ] Remediation path identified
- [ ] Responsible parties assigned
- [ ] Considered whether scope is appropriate

## Recommendations

### Dos ✅

- **Do** start with small, focused audits
- **Do** document your methodology
- **Do** provide reproducible verification
- **Do** be honest about gaps
- **Do** provide remediation plans
- **Do** update audits when scope changes
- **Do** version your audits
- **Do** link to evidence

### Don'ts ❌

- **Don't** cherry-pick passing elements
- **Don't** hide gaps
- **Don't** claim PASS with known unassured vertices
- **Don't** skip documentation
- **Don't** use stale validation results
- **Don't** mix unrelated scopes
- **Don't** create audits for unstable content
- **Don't** forget to update modified timestamp

## Continuous Assurance

### Maintaining Audit Validity

**When to Re-Audit:**
- Vertices in scope are modified
- Assurance faces are added/removed
- Verification/validation results change
- Specification requirements change
- Quality thresholds change

**Incremental Updates:**
- Update modified timestamp
- Re-verify affected elements
- Update status if needed
- Document changes since last audit

**Audit Cadence:**
- Critical audits: After every change
- Important audits: Monthly or quarterly
- Standard audits: Per release
- Experimental: As needed

## Related Guidance

- **Guidance-for-Charts:** General chart creation guidance
- **Guidance-for-Specs:** Writing good specifications
- **Guidance-for-Verification:** Creating effective verification checks
- **Guidance-for-Validation:** Quality assessment practices

---

**Version:** 1.0.0

**Status:** Active

**Last Modified:** 2025-12-27
