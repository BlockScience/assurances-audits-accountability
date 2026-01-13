---
type: vertex/guidance
extends: doc
id: v:guidance:assured_signed_chart
name: Guidance for Assured Signed Charts
description: Quality criteria and best practices for creating excellent assured-signed chart documents
tags:
  - vertex
  - doc
  - guidance
  - assurance
  - signature
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies:
  - v:guidance:assurance_audit
---

# Guidance for Assured Signed Charts

**This guidance defines quality criteria and best practices for creating excellent assured-signed chart documents.**

## Purpose

While spec-for-assured-signed-chart defines what structural elements must be present, this guidance helps authors assess **how well** an assured-signed chart establishes accountability. Great assured-signed charts make the chain of trust visible, the common boundaries clear, and the human accountability explicit.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating assured-signed charts by providing:
- Quality assessment criteria for signature networks
- Best practices for common boundary documentation
- Guidance on dependency acknowledgment
- Section-by-section authoring advice
- Accountability chain verification approaches

### Best Use Cases

Use this guidance when:
- Creating a chart that requires complete accountability (assurance + signature)
- Documenting a self-demonstrating system (like the INCOSE paper)
- Establishing trust anchors for downstream consumers
- Creating audit-ready documentation
- Building visualization inputs for accountability networks

## Quality Criteria

### 1. Accountability Clarity

**Excellent:**
- Every document has a clear, named human signer
- Qualification basis for each signature is explicit
- Signing events have verifiable timestamps and commit hashes
- Chain of trust is unambiguous from any document to root

**Good:**
- Most documents have identified signers
- Qualifications mostly documented
- Signing events recorded
- Trust chain generally traceable

**Needs Improvement:**
- Signers not clearly identified
- Qualifications unclear or missing
- Signing events undocumented
- Unclear who is responsible for what

### 2. Common Boundary Visibility

**Excellent:**
- Shared validation edges explicitly listed for each document
- Diagram shows assurance/signature face coupling
- Common boundary property verified programmatically
- Clear explanation of WHY faces share boundaries

**Good:**
- Shared edges documented
- Some visualization of coupling
- Property mostly verified

**Needs Improvement:**
- Common boundaries not documented
- No visualization of face relationships
- Property not verified
- Reader cannot see how faces connect

### 3. Signature Network Completeness

**Excellent:**
- 100% signature coverage (every document signed)
- All qualifies edges current and valid
- No gaps in accountability chain
- Signer qualifications appropriate to content

**Good:**
- ≥90% signature coverage
- Most qualifies edges valid
- Minor gaps documented
- Qualifications generally appropriate

**Needs Improvement:**
- Significant signature gaps
- Expired or missing qualifies edges
- Major accountability holes
- Inappropriate signer assignments

### 4. Dependency Transparency

**Excellent:**
- All dependencies explicitly listed
- Dependency assurance status documented
- Dependency signature status documented
- External dependencies acknowledged with status
- Root anchoring confirmed

**Good:**
- Most dependencies listed
- Status mostly documented
- Major external deps acknowledged
- Root anchoring traced

**Needs Improvement:**
- Dependencies unclear or unlisted
- Status undocumented
- External deps ignored
- Root anchoring unclear

### 5. Topological Coherence

**Excellent:**
- Face pairing is topologically correct (shared edge verified)
- Euler characteristic computed for full complex
- Connectivity of signature network analyzed
- Holes/gaps identified and explained

**Good:**
- Face pairing mostly correct
- Basic topology computed
- Connectivity stated

**Needs Improvement:**
- Topological errors present
- No topology analysis
- Connectivity unknown

### 6. Auditability

**Excellent:**
- All claims verifiable by running scripts
- Audit trail reproducible
- Historical signatures preserved
- Changes trackable through git

**Good:**
- Most claims verifiable
- Audit trail mostly reproducible
- Recent signatures preserved

**Needs Improvement:**
- Claims unverifiable
- No audit trail
- Signatures untrackable

### 7. Visualization Quality

**Excellent:**
- Clear visualization of signature network
- Assurance/signature face pairs visually distinguished
- Common boundaries highlighted
- Layered view (foundation → type → instance)
- Signer attribution visible

**Good:**
- Basic visualization present
- Face pairs distinguishable
- Boundaries shown

**Needs Improvement:**
- No visualization
- Faces indistinguishable
- Boundaries not shown

### 8. Self-Demonstration Readiness

**Excellent:**
- Chart suitable for inclusion in papers/presentations
- Accountability story clear to external reader
- Technical correctness verifiable by third party
- Serves as proof of framework claims

**Good:**
- Chart mostly presentable
- Story generally clear
- Mostly verifiable

**Needs Improvement:**
- Not presentation-ready
- Confusing to external readers
- Hard to verify

## Section-by-Section Guidance

### Signature Network Section

**Purpose:** Make human accountability explicit and complete

**Tips:**
- List every signer with their GitHub username (verifiable identity)
- For each signer, list ALL guidances they're qualified for
- For each document, show exactly which signer signed it
- Include signing timestamps and commit references
- Make it easy to answer "who is responsible for X?"

**Anti-patterns:**
- ❌ "Signed by team" (no individual accountability)
- ✅ "Signed by mzargham (v:signer:mzargham) on 2025-12-30 commit abc123"
- ❌ Listing signers without their qualifications
- ✅ Signer table with "Qualified For" column

**Example:**
```markdown
### Signers

| Signer ID | Name | GitHub | Qualified For |
|-----------|------|--------|---------------|
| v:signer:mzargham | Michael Zargham | mzargham | v:guidance:spec, v:guidance:guidance, v:guidance:incose-paper |

### Signature Coverage

| Document | Signer | Signed | Commit |
|----------|--------|--------|--------|
| v:spec:incose-paper | v:signer:mzargham | 2025-12-30 | abc123 |
```

### Local Constraints Section

**Purpose:** Document the topological coupling that connects assurance to accountability

**Tips:**
- Explain the common boundary property in plain language first
- Show the face structure diagram
- List every (assurance, signature, shared_edge) triple
- Verify the constraint holds for each pair
- Explain why this matters (accountability is connected to quality)

**Anti-patterns:**
- ❌ Just listing faces without showing relationships
- ✅ Explicit table of face pairs with shared edges
- ❌ Assuming reader understands common boundary concept
- ✅ Diagram + explanation + verification

**Example:**
```markdown
### Common Boundary Property

Each document's assurance and signature faces share exactly the validation edge:

```
                    doc
                   / | \
                  /  |  \
         verification | validation (SHARED)
               /     |     \
           spec    signs   guidance
              \      |      /
          coupling   |  qualifies
                 \   |   /
                  signer
```

### Constraint Verification

| Document | Assurance Face | Signature Face | Shared Edge | Valid |
|----------|----------------|----------------|-------------|-------|
| v:spec:incose-paper | f:assurance:incose-paper-spec | f:signature:incose-paper-spec:mzargham | e:validation:incose-paper-spec:guidance-spec | ✓ |
```

### Dependency Acknowledgment Section

**Purpose:** Show that the accountability network is rooted and complete

**Tips:**
- Trace every dependency back to boundary complex
- Show assurance AND signature status for each dependency
- Acknowledge any external dependencies honestly
- Document why external deps can be trusted (or not)
- Make root anchoring explicit

**Anti-patterns:**
- ❌ Ignoring dependencies that aren't assured/signed
- ✅ Acknowledging gaps with remediation plan
- ❌ "All dependencies OK" without evidence
- ✅ Table showing status of each dependency

**Example:**
```markdown
### Dependency Graph

| Document | Depends On | Assured | Signed | Notes |
|----------|------------|---------|--------|-------|
| v:spec:incose-paper | v:spec:spec | ✓ | ✓ | Foundation |
| v:spec:incose-paper | v:guidance:spec | ✓ | ✓ | Foundation |
| v:doc:incose-paper | v:spec:incose-paper | ✓ | ✓ | Type layer |

### Root Anchoring

All assurance chains trace to boundary complex:
- b2:spec-spec (self-referential spec foundation)
- b2:guidance-guidance (self-referential guidance foundation)

All signers qualified through:
- e:qualifies:mzargham:guidance-spec (foundation qualification)
```

## Workflow Guidance

### Recommended Authoring Sequence

1. **Start with Assurance Audit** (prerequisite)
   - Complete spec-for-assurance-audits requirements first
   - Ensure all documents have assurance faces
   - Verify audit passes

2. **Establish Signers** (15-30 min)
   - Create signer vertices for all required signers
   - Verify GitHub usernames
   - Document signing authority

3. **Create Qualifies Edges** (30-45 min)
   - For each signer, create qualifies edges to relevant guidances
   - Document credential evidence
   - Verify no expirations

4. **Create Signs Edges** (30-45 min)
   - For each document, create signs edge from appropriate signer
   - Record signing timestamp and commit hash
   - Reference qualifies edge

5. **Build Signature Faces** (45-60 min)
   - For each document, create signature face
   - Verify common boundary with assurance face
   - Document face structure

6. **Document Common Boundaries** (20-30 min)
   - List all (assurance, signature, shared_edge) triples
   - Verify constraint holds for each
   - Create diagram

7. **Acknowledge Dependencies** (20-30 min)
   - Trace all dependencies
   - Document assurance/signature status
   - Identify external deps

8. **Verify and Visualize** (30-45 min)
   - Run verification scripts
   - Generate visualizations
   - Review audit trail

### Quality Checkpoints

- **After step 2:** Do all signers have valid GitHub accounts?
- **After step 4:** Are all qualifies edges non-expired?
- **After step 5:** Do all signature faces share validation edge with assurance?
- **After step 6:** Does constraint verification table have all ✓?
- **After step 7:** Are all dependencies acknowledged?
- **After step 8:** Does visualization show connected accountability network?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Missing Signer** | Document has assurance but no signature | Create signer vertex, qualifies edge, signs edge, signature face |
| **Expired Qualification** | Qualifies edge has passed expiry_date | Renew qualification or assign to different signer |
| **Common Boundary Violation** | Assurance and signature faces don't share edge | Check face definitions; validation edge ID must match exactly |
| **Unacknowledged Dependency** | Document depends on unmentioned vertex | Add to dependency graph; document status |
| **Broken Trust Chain** | Can't trace to boundary complex | Add intermediate assurance/signature faces |
| **Visualization Confusion** | Can't distinguish assurance from signature faces | Use different colors/shapes for face types |

## Best Practices

### Signer Management

1. **One signer per role** - Avoid spreading signatures across many signers
2. **Document qualifications completely** - Each qualifies edge needs evidence
3. **Use GitHub identity** - Enables commit signature verification
4. **Keep qualifications current** - Check expiry dates regularly
5. **Record signing context** - Why was this signed? What did signer review?

### Common Boundary Documentation

6. **Be explicit** - List every shared edge, don't assume reader knows
7. **Visualize the coupling** - Diagrams make topology clear
8. **Verify programmatically** - Don't just claim, prove with scripts
9. **Explain the purpose** - Why does shared boundary matter?
10. **Check both directions** - Assurance references signature; signature references assurance

### Dependency Management

11. **Trace to root** - Every chain should reach boundary complex
12. **Acknowledge gaps honestly** - Better to document than hide
13. **Include external deps** - Papers cite papers; tools have versions
14. **Update when deps change** - Chart must reflect current state
15. **Consider transitive deps** - A depends on B depends on C

### Auditability

16. **Make everything reproducible** - Scripts, not manual checks
17. **Preserve history** - Git commits are your audit trail
18. **Date everything** - Timestamps on all signing events
19. **Link to evidence** - Don't claim, show
20. **Keep it current** - Stale audits are useless

## Self-Demonstration Application

When creating an assured-signed chart for a self-demonstrating system (like the INCOSE paper):

### The Chart Proves the Framework

- The existence of a valid assured-signed chart IS evidence the framework works
- Show the chart in the paper as a figure
- Explain how the chart demonstrates the claims

### Recursive Accountability

- The paper about accountability must itself be accountable
- Every claim in the paper should be traceable to a signed vertex
- The chart completes the loop: paper → spec → guidance → signer → paper

### Presentation Readiness

- Chart should be visually clear for paper figures
- Layered architecture visible (foundation → type → instance)
- Accountability chain obvious to reader
- Can answer "why should I trust this paper?"

## Validation vs. Verification

**Verification** (deterministic, against spec-for-assured-signed-chart):
- All required frontmatter fields present
- All required sections present
- All faces correctly structured
- Common boundary edges match
- All IDs resolve

**Validation** (qualitative, against this guidance):
- Accountability is clear and complete
- Common boundaries well documented
- Dependencies appropriately acknowledged
- Visualizations support understanding
- Chart serves its demonstration purpose
- External reader can follow trust chain

## Tooling Support

### Verification Commands

```bash
# Verify chart structure (includes signature elements)
python scripts/verify_chart.py charts/<chart>.md

# Audit assurance coverage
python scripts/audit_assurance_chart.py charts/<chart>.md

# Check signature coverage (future tool)
# python scripts/audit_signatures.py charts/<chart>.md

# Verify common boundaries (future tool)
# python scripts/verify_common_boundaries.py charts/<chart>.md
```

### Visualization Commands

```bash
# Export to JSON
python scripts/export_chart_direct.py charts/<chart>.md

# Generate HTML visualization
python scripts/visualize_chart.py charts/<chart>.json
```

## Examples

### Excellent Assured-Signed Chart Characteristics

An excellent assured-signed chart for the INCOSE self-demonstration would:

1. ✓ Cover all documents: spec, guidance, paper content, supporting docs
2. ✓ Have clear signers with documented qualifications
3. ✓ Show common boundaries between all assurance/signature face pairs
4. ✓ Acknowledge all dependencies back to boundary complex
5. ✓ Be visualizable with clear layered structure
6. ✓ Include itself in the audit (self-demonstrating property)
7. ✓ Serve as main figure in the paper
8. ✓ Allow external reader to verify accountability claims

---

**Note:** This guidance pairs with spec-for-assured-signed-chart via a coupling edge. The spec defines structure; this guidance defines quality. Together they enable full assurance (verification + validation) for assured-signed chart documents.
