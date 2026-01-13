---
type: vertex/guidance
extends: doc
id: v:guidance:requirements-trace
name: Guidance for Requirements Trace Documents
description: Quality criteria and best practices for creating effective requirements traceability reports
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2026-01-12T00:00:00Z
modified: 2026-01-12T00:00:00Z
dependencies: []
criteria:
  - completeness
  - bidirectionality
  - gap-identification
  - actionability
  - accuracy
---

# Guidance for Requirements Trace Documents

**This guidance helps authors create high-quality requirements traceability reports that demonstrate complete coverage from stakeholder needs through implementation.**

## Purpose

Requirements trace documents serve as evidence that an architecture is both complete (all needs are addressed) and justified (all implementations have purpose). This guidance helps authors create trace documents that are comprehensive, accurate, and useful for both verification and decision-making. It provides quality criteria, section-specific advice, and common pitfalls to avoid.

## Document Overview

### What This Guidance Covers

Requirements trace documents analyze the four-layer architecture chain:
- **Stakeholder Needs → Acceptance Criteria**: How needs become measurable criteria
- **Acceptance Criteria → Functions**: How criteria drive functional requirements
- **Functions → Components**: How functions are allocated to logical components
- **Components → Elements**: How components are realized in physical elements

The trace must be bidirectional: forward (needs → implementation) and backward (implementation → needs).

### Best Use Cases

1. **Architecture Completion**: Verifying that a new architecture addresses all stakeholder needs
2. **Gap Analysis**: Identifying missing requirements or orphan implementations
3. **Change Impact Assessment**: Understanding which elements are affected by requirement changes
4. **Compliance Demonstration**: Providing evidence of requirements coverage for audits
5. **Implementation Readiness**: Confirming the architecture is ready for development

## Quality Criteria

### 1. Completeness

**Excellent:** Every item at every layer is accounted for in both forward and backward traces. Coverage table shows 100% for all layers. No items are missing from the analysis.

**Good:** All layers are traced with few gaps. Coverage is >95% for all layers. Any gaps are explicitly documented.

**Needs Improvement:** Significant items are missing. Coverage is incomplete for one or more layers. Gaps exist without documentation.

### 2. Bidirectionality

**Excellent:** Forward trace (needs → elements) and backward trace (elements → needs) are both complete. The two traces are consistent—items appear in both directions. Readers can start from either end and follow the chain.

**Good:** Both forward and backward traces exist. Coverage is mostly consistent between directions. Minor asymmetries may exist.

**Needs Improvement:** Only one direction is traced, or traces are inconsistent. Forward and backward analyses don't align.

### 3. Gap Identification

**Excellent:** Gap analysis is thorough and honest. All gaps are explicitly identified with impact assessment and recommendations. "No gaps identified" is stated clearly when applicable. Potential risks are noted even if not technically gaps.

**Good:** Gap analysis is present. Major gaps are identified. Impact is described. Basic recommendations provided.

**Needs Improvement:** Gap analysis is superficial or missing. Gaps may exist but aren't acknowledged. No recommendations for improvement.

### 4. Actionability

**Excellent:** Findings lead to clear next steps. Recommendations are specific and implementable. Gap remediation paths are defined. Implementation readiness assessment is unambiguous.

**Good:** Findings are useful for decision-making. Recommendations exist. Overall assessment is clear.

**Needs Improvement:** Findings are abstract. Recommendations are vague. Reader is unsure what actions to take.

### 5. Accuracy

**Excellent:** All counts match the source architecture documents. All references are correct. Trace chains are verifiable by following links. No errors in mappings or categorizations.

**Good:** Counts are mostly accurate. References are correct. Minor discrepancies may exist.

**Needs Improvement:** Counts don't match source documents. References are broken. Trace chains have errors.

## Section-by-Section Guidance

### Executive Summary

**Purpose:** Provide at-a-glance understanding of traceability status.

**Tips:**
- Lead with the coverage table—readers want to know status immediately
- Keep the summary focused on facts, not interpretation
- Use checkmarks (✓) and crosses (✗) for quick visual scanning
- Summarize key findings in 3-5 bullet points

**Anti-patterns:**

- ❌ Burying the coverage status deep in the document

**Preferred:**

- ✅ Lead with the coverage table, then provide context

### Forward Traceability

**Purpose:** Demonstrate that all stakeholder needs flow through to implementation.

**Tips:**
- Work systematically layer by layer (don't skip ahead)
- Use tables or matrices for clear visual mapping
- Include all items at each layer, even if mappings are obvious
- Group related items to show patterns

**Anti-patterns:**

- ❌ "Functions implement the acceptance criteria" (too vague)

**Preferred:**

- ✅ Explicit table: "AC1 → F1, F3 | AC2 → F5, F6, F7"

### Backward Traceability

**Purpose:** Demonstrate that all implementation elements are justified.

**Tips:**
- For each element, trace the complete chain back to stakeholder value
- This is where orphan elements are discovered
- Use hierarchical visualization (element → component → function → criterion → need)
- Highlight any elements that don't trace cleanly

**Anti-patterns:**

- ❌ Assuming backward trace is just forward trace reversed

**Preferred:**

- ✅ Explicitly trace from each element to verify nothing is orphaned

### Gap Analysis

**Purpose:** Identify and assess any traceability issues.

**Tips:**
- Be honest—gaps are not failures, they're findings
- Distinguish between gaps (missing coverage) and risks (potential issues)
- Provide impact assessment for each gap
- Include clear recommendations for remediation
- If no gaps exist, state "No gaps identified" explicitly

**Anti-patterns:**

- ❌ Hiding gaps by not analyzing thoroughly
- ❌ Omitting gap analysis section when no gaps found

**Preferred:**

- ✅ "Gap Analysis: No gaps identified. All 24 stakeholder needs trace to implementation."

### Traceability Summary

**Purpose:** Provide the complete picture and final assessment.

**Tips:**
- Include a visual representation of the full chain (ASCII diagram, flowchart reference)
- Summarize counts in a single table
- State the final coverage assessment clearly
- This should be quotable for executive communications

**Anti-patterns:**

- ❌ Repeating all the detail from earlier sections

**Preferred:**

- ✅ Concise summary with references to detailed sections

## Workflow Guidance

### Recommended Authoring Sequence

1. **Gather Source Documents** (15 min)
   - Collect architecture documents (main + extended if applicable)
   - Extract counts: stakeholders, criteria, functions, components, elements
   - Verify documents are current versions

2. **Build Forward Trace** (45 min)
   - Start from stakeholder needs
   - Map needs → criteria → functions → components → elements
   - Create tables/matrices at each step
   - Note any items that don't map clearly

3. **Build Backward Trace** (30 min)
   - Start from each physical element
   - Trace back to stakeholder value
   - Identify any orphan elements
   - Verify consistency with forward trace

4. **Analyze Gaps** (20 min)
   - Compare forward and backward traces
   - Identify any unmapped items
   - Assess impact of any gaps
   - Develop recommendations

5. **Write Summary** (15 min)
   - Create executive summary with coverage table
   - Write key findings
   - State implementation readiness
   - Add recommendations if applicable

### Quality Checkpoints

- **After Forward Trace:** Do all criteria map to functions? All functions to components?
- **After Backward Trace:** Do all elements trace to stakeholder value?
- **After Gap Analysis:** Are all gaps documented with impact and recommendations?
- **Final:** Do counts match source documents? Is coverage status accurate?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Count Mismatch | Trace counts don't match architecture documents | Re-extract counts from source documents; verify versions match |
| Orphan Elements | Physical elements without stakeholder justification | Either trace to needs (may be implicit) or flag as unnecessary |
| Missing Criteria Coverage | Some acceptance criteria not traced to functions | Review functional architecture; may need additional functions |
| Vague Mappings | "All functions implement all criteria" | Create explicit mapping tables; avoid many-to-many without detail |
| Stale Trace | Trace document doesn't reflect current architecture | Re-run analysis; note architecture version in frontmatter |
| Incomplete Gap Analysis | "No issues found" without evidence | Show the analysis that proves no gaps; be explicit |

## Best Practices

1. **Use the architecture documents as source of truth**: Extract counts and relationships directly, don't guess
2. **Create explicit mappings**: Tables and matrices are clearer than prose descriptions
3. **Trace both directions independently**: Don't assume backward trace is forward trace reversed
4. **Be honest about gaps**: Gaps discovered are better than gaps hidden
5. **Include impact assessment**: Gaps without impact analysis aren't actionable
6. **Version your trace**: Architecture changes; keep traces in sync
7. **Use visual summaries**: ASCII diagrams or flowcharts aid comprehension
8. **Quote specific IDs**: Reference AC1, F5, C12, E4 explicitly, not "some criteria"
9. **State conclusions clearly**: "Ready for implementation" or "Gaps require resolution"
10. **Update when architecture changes**: Trace documents are living artifacts

## Validation vs. Verification

**Verification** (deterministic checks against spec-for-requirements-trace):
- All required sections present
- Counts in frontmatter are integers
- Coverage status is valid enum value
- Architecture reference exists
- Forward and backward trace sections exist

**Validation** (qualitative assessment against this guidance):
- Completeness: Are all items at all layers traced?
- Bidirectionality: Are both forward and backward traces consistent?
- Gap Identification: Are gaps honest and thoroughly analyzed?
- Actionability: Are recommendations specific and implementable?
- Accuracy: Do counts and mappings match source documents?

## Tooling Support

### Verification Commands

```bash
# Verify structure against spec
python scripts/verify_template_based.py 00_vertices/requirements-trace-<name>.md --templates templates
```

### Validation Support

Requirements trace validation benefits from automated comparison with architecture documents:

1. Extract counts from architecture frontmatter
2. Compare with trace document frontmatter counts
3. Verify referenced documents exist
4. Flag any count mismatches

Human review should assess:
- Mapping accuracy (spot-check trace chains)
- Gap analysis completeness
- Recommendation actionability

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

✓ **Completeness**: Covers all aspects of requirements trace creation
✓ **Bidirectionality**: Addresses both creation workflow and evaluation criteria
✓ **Gap Identification**: Includes troubleshooting for common issues
✓ **Actionability**: Provides specific, implementable advice
✓ **Accuracy**: References correct spec and follows established patterns

---

**Note:** This guidance pairs with `spec-for-requirements-trace.md` via a coupling edge. The spec defines structure; this guidance defines quality.
