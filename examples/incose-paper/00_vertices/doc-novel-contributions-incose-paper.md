---
type: vertex/doc
extends: doc
id: v:doc:novel-contributions-incose-paper
name: Novel Research Contributions - INCOSE IS 2026 Paper
description: Enumeration and ranking of intellectual contributions from the assurance framework research for the INCOSE IS 2026 submission
tags:
  - vertex
  - doc
  - novel-contributions
version: 1.0.0
created: 2025-12-30T20:00:00Z
modified: 2025-12-30T20:00:00Z
context: incose-is-2026
contribution_count: 8
novelty_levels:
  - Highly Novel
  - Novel
  - Moderately Novel
  - Incremental
  - Discovered
target_venue: INCOSE International Symposium 2026
related_artifacts:
  - v:doc:architecture-incose-paper
  - v:doc:lifecycle-incose-paper
  - v:doc:literature-review-incose-paper
dependencies: []
---

# Novel Research Contributions - INCOSE IS 2026 Paper

This document enumerates the novel intellectual contributions arising from the development and experimental application of a typed simplicial complex framework for document verification, validation, and assurance with human accountability. These contributions were discovered through hands-on implementation during preparation of an INCOSE International Symposium 2026 paper.

The contributions are organized by novelty level, ranked from highest impact to incremental. This inventory serves as the authoritative reference for positioning claims in the paper, ensuring honest characterization of what is genuinely new versus what builds on established practice.

---

## 1. HIGHLY NOVEL: Structural Accountability Enforcement

**What:** The framework makes human accountability structurally required—validation edges and assurance faces cannot exist without a named `human_approver` field. This is not a recommendation or best practice; it's enforced by the type system.

**Why it's highly novel:**
- Ghrist's "The Forge" (2025) demonstrates that procedural accountability is achievable through disciplined practice
- Our contribution: formalizing accountability as enforceable structure, not just documented process
- The distinction is between "I followed a process" (procedural) and "this data structure requires a name" (structural)
- Schema validation catches missing accountability before documents enter the network
- This directly addresses "who is responsible for LLM-generated content?" with a structural answer

**Evidence from experiment:**
- All validation edges include `human_approver: mzargham` as a required field (not optional)
- All assurance faces require `human_approver` for triangle closure
- Documents cannot pass verification without accountability attribution
- `check_accountability.py` script validates approver presence and validity

**Prior Art:** Ghrist [Ghrist-2025] achieves accountability through disciplined practice: "Every sentence... passed through my judgment." We formalize what Ghrist practices—the structural enforcement is our novel contribution.

**Projection to paper:** Position as the key differentiation from Ghrist's procedural approach. "The Forge demonstrates accountability is achievable; we demonstrate it can be enforced."

---

## 2. HIGHLY NOVEL: Explicit Coupling of Specification and Guidance

**What:** The framework requires explicit coupling edges between specifications (structural requirements) and guidance documents (quality criteria), making the relationship between verification and validation first-class and traceable.

**Why it's highly novel:**
- Traditional V&V treats verification and validation as separate, parallel activities
- We formalize their relationship: verification alone is insufficient (you can be structurally correct but useless); validation alone is subjective (quality without structure)
- The coupling edge creates a coherent "document type": you cannot verify against one spec and validate against unrelated guidance
- This is the missing link in most QA frameworks—the formal connection between "did we build it right?" and "did we build the right thing?"

**Evidence from experiment:**
- Created `coupling-incose-paper.md` explicitly connecting spec-for-incose-paper ↔ guidance-for-incose-paper
- Without the coupling edge, the assurance triangle cannot close (topologically incomplete)
- The boundary complex demonstrates coupling as foundational: spec-for-spec is coupled to guidance-for-spec
- Framework enforces that verification and validation edges must use coupled pairs

**Projection to paper:** Key framework innovation. Position as the answer to "how do verification and validation relate?"—a question practitioners frequently ask but existing frameworks leave implicit.

---

## 3. NOVEL: Assurance Triangle as 2-Simplex

**What:** Using algebraic topology (specifically, typed simplicial complexes) to model document assurance, where the assurance triangle is a face (2-simplex), not merely a diagram or metaphor.

**Why it's novel:**
- Triangular quality diagrams are common in QA literature; treating them as simplicial faces with mathematical properties is new
- Mathematical properties become available: boundary operators, Euler characteristic, face closure conditions
- Topological invariants (χ = V - E + F) can audit structural integrity of the entire assurance network
- Composition rules from algebraic topology apply: faces must close, boundaries must match

**Evidence from experiment:**
- Charts report topological properties: V=8, E=20, F=7 for the INCOSE paper chart
- Audit script validates invariants (boundary complex: χ = V - F = 1)
- Boundary complex uses 2-simplices to resolve self-referential type definitions without paradox
- Face closure enforced: all three edges (verification, coupling, validation) must exist for face to close

**Projection to paper:** Mathematical foundation section. The topology gives precision to what's otherwise a vague "quality triangle" concept. Emphasize that it enables tooling and auditing, not just theory.

---

## 4. NOVEL: Boundary Complex for Bootstrap

**What:** The framework bootstraps through a unique "boundary complex" structure with a root vertex (b0:root), enabling self-referential type definitions (spec-for-spec, guidance-for-guidance) without logical paradox.

**Why it's novel:**
- Self-referential type systems typically have bootstrap problems: what validates the validators?
- The root vertex provides an axiomatic anchor outside the typed system—an explicit foundation
- Boundary faces (b2:spec-spec, b2:guidance-guidance) use the root to close their triangles
- This is a clean mathematical resolution to a real philosophical problem in quality frameworks

**Evidence from experiment:**
- Boundary complex exists with 5 vertices including b0:root
- New document types (spec-for-incose-paper) verify against foundational spec-for-spec
- Chain of trust traces back to explicit axioms (the root vertex)
- The Euler characteristic invariant (χ = V - F = 1) validates boundary complex integrity

**Projection to paper:** Theoretical elegance that distinguishes from ad-hoc frameworks. Position as "we've thought carefully about the foundations." The bootstrap is explicit, not hidden.

---

## 5. MODERATELY NOVEL: Test-Driven Document Development

**What:** Applying Test-Driven Development (TDD) principles to documentation: write the specification first, then write the document to pass verification, iterate until compliant.

**Why it's moderately novel:**
- TDD for code is well-established in software engineering practice
- TDD for documentation is less formalized, though the concept is intuitive
- The verification script acts like a test runner: spec defines expectations, script checks compliance
- The "red-green-refactor" cycle maps to: verify fails → write content → verify passes → refine

**Evidence from experiment:**
- Created spec-for-incose-paper BEFORE writing paper content
- Ran `verify_template_based.py` (like running tests) after each edit
- Iterated until 100% verification pass rate
- Phase 1-4 workflow in protocol mirrors TDD ceremony

**Projection to paper:** Accessible framing that connects to known software practice. Not groundbreaking for an SE audience, but practical and immediately applicable. Use to make framework accessible.

---

## 6. MODERATELY NOVEL: Typed Simplicial Complex for Knowledge Graphs

**What:** Extending simplicial complexes with a formal type system where vertices, edges, and faces have declared types with inheritance (spec extends doc, verification extends edge, etc.).

**Why it's moderately novel:**
- Typed graphs are common in knowledge representation (RDF, property graphs)
- Typed simplicial complexes combining type inheritance with topological structure are less common
- Type system enables meaningful composition: can't create verification edge to wrong target type
- Types enable automatic template generation and verification tooling

**Evidence from experiment:**
- Frontmatter includes `type: vertex/spec`, `type: edge/verification`, `type: face/assurance`
- Templates derived from types (spec template, guidance template, edge templates)
- Scripts check type consistency: verification edge must connect spec to spec
- Type violations caught during verification, before documents enter the network

**Projection to paper:** Technical foundation section. Important for understanding how the framework works, but may not excite practitioners who just want results. Include as background, not highlight.

---

## 7. INCREMENTAL: Verification Scripts and Tooling

**What:** Python scripts implementing template-based verification, chart export, visualization, and assurance audit functionality.

**Why it's incremental:**
- Implementation of the theoretical framework, not theory itself
- Standard scripting patterns: YAML parsing, markdown generation, tree traversal
- Useful engineering but not intellectually novel
- Any competent developer could build similar tooling given the specification

**Evidence from experiment:**
- `verify_template_based.py` - template checking, works as expected
- `export_chart_direct.py` - JSON export for visualization
- `visualize_chart.py` - HTML visualization generation
- `audit_assurance_chart.py` - coverage and integrity checking

**Projection to paper:** Mention for completeness in implementation section. Don't emphasize; reviewers care about concepts, not code. Note: source code will be released upon acceptance.

---

## 8. DISCOVERED: Audit Script Design Gap and Fix

**What:** During experimental application, the audit script was found to infer face targets from naming conventions rather than reading explicit `target:` metadata, causing incorrect coverage reports.

**Why this is valuable:**
- Demonstrates framework in action: using it revealed a gap in the tooling
- Discovery led to immediate fix with explicit `get_face_target()` function
- Fix validated by re-running audit on both INCOSE paper chart and boundary complex
- Shows iterative improvement and honest acknowledgment of limitations

**Evidence from experiment:**
- Initial audit showed 85.7% coverage (paper content marked unassured)
- Root cause: script didn't read `target:` field from face frontmatter
- Fix: added function to load face file and read explicit target
- Post-fix: 100% coverage for INCOSE paper chart, boundary complex unchanged (regression-safe)

**Projection to paper:** Future work / limitations section. Honest acknowledgment that tooling evolved during use. Demonstrates the framework's value: it surfaced a problem and guided the fix.

---

## Summary: Contribution Hierarchy

| Rank | Contribution | Novelty | Paper Treatment |
|------|--------------|---------|-----------------|
| 1 | Structural accountability enforcement | Highly Novel | Key differentiation from Ghrist |
| 2 | Explicit coupling of spec/guidance | Highly Novel | Core framework innovation |
| 3 | Assurance triangle as 2-simplex | Novel | Mathematical foundation |
| 4 | Boundary complex bootstrap | Novel | Theoretical elegance |
| 5 | Test-driven document development | Moderately Novel | Accessible framing |
| 6 | Typed simplicial complexes | Moderately Novel | Technical background |
| 7 | Tooling implementation | Incremental | Supporting material |
| 8 | Discovered audit gap | Discovered | Future work, honest limitation |

---

## Key Insights for Paper

1. **Lead with structural accountability**: The key differentiation from Ghrist's "The Forge" is that we formalize accountability as enforceable structure, not just documented process. "The Forge demonstrates accountability is achievable; we demonstrate it can be enforced."

2. **Position coupling as the core innovation**: The explicit relationship between verification (structural) and validation (quality) is what's missing from existing V&V frameworks. This answers a real practitioner question.

3. **Acknowledge Ghrist as sole prior art**: "The Forge" (2025) is the only known prior art on AI-generated content methodology. The same author's barcodes paper (2008) informs our topological foundation.

4. **Math provides precision, not just metaphor**: Simplicial complexes aren't decoration—they enable topological invariants, auditing, and composition rules. Ghrist's own topological methods inform both our mathematical foundation and our acknowledgment of his methodological prior art.

5. **Bootstrap elegantly solves a real problem**: The boundary complex with root vertex is philosophically satisfying and practically necessary. "Who validates the validators?" has an explicit answer.

6. **Connect to known practices**: TDD framing makes the framework accessible to software engineers. V-model alignment connects to systems engineering traditions. Use bridges.

7. **Acknowledge limitations honestly**: The discovered audit gap shows the framework's self-correcting nature. Honesty about what was fixed builds credibility.

---

**Conclusion:** The experimental application of the assurance framework confirmed its capabilities and revealed one tooling gap that was immediately fixed. The novel contributions are genuine and substantial, with structural accountability enforcement (differentiating from Ghrist's procedural approach) and explicit spec/guidance coupling being the strongest claims. The acknowledgment of "The Forge" as the only known prior art on AI-generated content methodology demonstrates intellectual honesty about the existing landscape.
