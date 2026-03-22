---
type: vertex/guidance
extends: guidance-for-incose-paper
id: v:guidance:incose-self-demonstration
name: Guidance for INCOSE Self-Demonstrating Paper
description: Quality criteria for INCOSE papers that demonstrate their framework by being instances of it, with emphasis on coherence across supporting documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-30T21:00:00Z
modified: 2025-12-30T21:00:00Z
dependencies:
  - v:guidance:incose-paper
---

# Guidance for INCOSE Self-Demonstrating Paper

## Purpose

This guidance **extends** `guidance-for-incose-paper` with quality criteria specific to papers that demonstrate their framework by being instances of it. While the parent guidance addresses general paper quality, this guidance focuses on:

- **Coherence** across the paper and its supporting documents (architecture, lifecycle, literature review, novel contributions)
- **Integrity** of the self-demonstration claim
- **Completeness** of coverage relative to supporting documents
- **Credibility** of the recursive proof

A self-demonstrating paper must not only be a good INCOSE paper—it must convincingly show that the framework works by virtue of its own existence.

---

## Inheritance

This guidance inherits ALL quality criteria from `guidance-for-incose-paper` v2.0.0. A paper validated against this guidance MUST also score well against parent guidance criteria:

- Relevance to SE Community
- Accessibility and Clarity
- Rigor and Validity
- Novelty and Contribution
- Theme Alignment
- Engagement and Impact

This guidance adds criteria specific to self-demonstrating papers.

---

## Quality Criteria for Self-Demonstration

### SD1: Coherence Across Documents

The paper and its supporting documents must tell a consistent, unified story.

#### Excellent (Target)

- Paper reads as a natural condensation of the supporting documents
- Terminology is perfectly consistent across all five documents
- Architecture layers map clearly to paper sections
- Lifecycle phases are visibly enacted in the paper's production
- Literature review themes correspond to paper's Background organization
- Contributions in paper precisely match novel contributions document
- Reader moving between documents experiences seamless continuity
- No contradictions or inconsistencies discoverable

#### Good

- Generally consistent terminology
- Most architectural elements reflected
- Literature review largely aligned
- Contributions recognizable across documents
- Minor inconsistencies that don't undermine claims

#### Needs Improvement

- Terminology drift between documents
- Paper introduces concepts not in architecture
- Citations in paper not traceable to literature review
- Contributions in paper differ from novel contributions document
- Reader confusion when cross-referencing documents
- Inconsistencies that undermine credibility

#### Assessment Questions

- [ ] Can I find the source in supporting documents for every major claim?
- [ ] Does the paper use the exact same terms as the architecture?
- [ ] Are all citations in the paper also in the literature review?
- [ ] Do the contributions in abstract/conclusion match the novel contributions document exactly?

---

### SD2: Architecture Alignment

The paper must reflect its architecture document faithfully and completely.

#### Excellent (Target)

- All four layers (Conceptual, Functional, Logical, Physical) are clearly represented
- V-model mapping from architecture informs paper's V&V discussion
- Stakeholder needs from architecture appear as paper's motivation
- Physical implementation details match exactly
- Paper demonstrates understanding of architectural choices
- Reader can trace paper content back to architecture sections

#### Good

- Most layers represented
- V-model connection present
- Implementation details consistent
- Some gaps in coverage

#### Needs Improvement

- Layers missing or misrepresented
- V-model discussion inconsistent with architecture
- Implementation differs from architecture
- Architecture seems separate from paper rather than its foundation

#### Alignment Tips

- **Quote the architecture** - Use exact language from architecture when describing framework
- **Reference layers explicitly** - "At the conceptual layer (see Architecture §2)..."
- **Show the V** - If architecture has V-model mapping, paper should reflect both sides
- **Match physical details** - Tool names, script names, technologies must be identical

---

### SD3: Lifecycle Enactment

The paper must visibly enact the lifecycle it describes.

#### Excellent (Target)

- Paper production followed the lifecycle phases
- Reader can see lifecycle phases in the paper's story
- Phase outputs (spec, guidance, verification, validation) are referenced
- Iteration is acknowledged where it occurred
- Human accountability moments are identified
- The lifecycle "comes alive" through the paper's example

#### Good

- Lifecycle phases recognizable
- Most phases referenced
- Process is implicit but traceable

#### Needs Improvement

- Paper seems produced differently than lifecycle describes
- Lifecycle phases not evident in paper's narrative
- Claimed lifecycle doesn't match visible process
- Disconnect between described process and enacted process

#### Enactment Strategies

- **Narrate your process** - "Following Phase 3 of our lifecycle, we iteratively developed..."
- **Show the artifacts** - Reference actual edges and faces created
- **Acknowledge iteration** - "The verification loop required three revision cycles..."
- **Name the humans** - "Human approver [name] validated against guidance..."

---

### SD4: Literature Foundation

The paper must demonstrably build on its literature review.

#### Excellent (Target)

- Background section structure mirrors literature review themes
- Every citation in paper appears in literature review catalog
- Gap analysis from literature review directly motivates contribution
- Positioning statement from literature review appears (refined) in paper
- Reader can use literature review as expanded bibliography
- New citations (if any) are justified and minimal

#### Good

- Most citations from literature review
- Themes generally aligned
- Gap connection clear
- Few unexplained new citations

#### Needs Improvement

- Many citations not in literature review
- Background structure diverges from literature review themes
- Gap analysis not reflected in paper's motivation
- Positioning inconsistent between documents

#### Foundation Tips

- **Structure your Background by theme** - Use literature review themes as subsection organizers
- **Cite from the catalog** - Every citation should ideally come from the literature review
- **Echo the gaps** - Paper's contribution should directly address literature review gaps
- **Use the positioning** - Literature review's positioning statement is draft for paper

---

### SD5: Contribution Integrity

The paper must accurately represent its contributions as defined in the novel contributions document.

#### Excellent (Target)

- All contributions from novel contributions document appear in paper
- Contribution language is consistent across documents
- No overclaiming beyond novel contributions document
- Evidence for each contribution matches that in novel contributions document
- Differentiation arguments are consistent
- Reader cannot find contribution in paper not in novel contributions document
- Reader cannot find contribution in novel contributions document missing from paper

#### Good

- Contributions largely match
- Minor language variation
- Evidence generally consistent
- No major overclaims

#### Needs Improvement

- Contributions differ between documents
- Paper overclaims relative to novel contributions document
- Missing contributions
- Evidence inconsistencies
- Differentiation arguments conflict

#### Integrity Tips

- **Copy contribution statements** - Use exact wording from novel contributions document
- **Don't improvise claims** - If it's not in novel contributions document, don't add it
- **Match evidence** - Same evidence cited in both documents
- **Preserve differentiation** - How you distinguish from prior work must match

---

### SD6: Self-Demonstration Credibility

The recursive "paper proves itself" claim must be credible.

#### Excellent (Target)

- Self-demonstration is explicit and prominent
- Audit results are concrete and verifiable
- Assurance chart is visualized or clearly described
- Reader can independently verify the framework works
- The proof feels genuine, not hand-wavy
- Skeptical reader would be convinced
- Framework limitations are demonstrable in the paper itself

#### Good

- Self-demonstration stated
- Some verification evidence
- Framework clearly used
- Mostly convincing

#### Needs Improvement

- Self-demonstration vague or hidden
- No concrete audit results
- "Trust us" without evidence
- Framework could have been described without using it
- Skeptical reader would doubt the claim

#### Credibility Builders

- **Show the audit trail** - Include actual audit output showing PASS
- **Visualize the chart** - Figure showing paper as vertex in assurance complex
- **Reference the artifacts** - Point to actual spec, guidance, edges, faces
- **Be specific about verification** - "This paper passes 6/6 verification checks..."
- **Acknowledge what's NOT self-demonstrated** - Limitations section should note what the paper can't prove about itself

---

### SD7: Traceability Experience

A reader should be able to trace claims across documents.

#### Excellent (Target)

- Any claim in paper can be traced to supporting document
- Cross-references are explicit (or easily derivable)
- Documents feel like views of the same underlying truth
- Moving between documents is seamless
- Terminology lookup is trivial
- Complete traceability matrix could be constructed

#### Good

- Most claims traceable
- Some cross-references present
- Documents generally aligned

#### Needs Improvement

- Claims appear from nowhere
- No cross-references
- Documents feel disconnected
- Terminology requires mental translation
- Traceability would require significant effort

#### Traceability Tips

- **Use consistent identifiers** - Same IDs in paper and supporting documents
- **Include a traceability section** - Optional but helpful mapping
- **Footnote sources** - "See Architecture Document §3.2 for detailed component description"
- **Reference by section** - Enable readers to find sources

---

## Section-Specific Guidance (Extended)

### Abstract (Extended Guidance)

In addition to parent guidance, self-demonstrating paper abstract SHOULD:

- Explicitly mention self-demonstration as part of contribution
- Reference that supporting documents exist (implicitly or explicitly)
- Make "paper is its own proof" claim compelling in ~2 sentences

**Example Addition:**
> "We demonstrate the framework by using it to write this paper—the paper itself is an assured vertex in a simplicial complex, verified against its specification, validated against its guidance, with complete audit trail."

### Background (Extended Guidance)

- Structure SHOULD mirror literature review themes
- Gap identification MUST align with literature review gap analysis
- Citations SHOULD come from literature review catalog
- Positioning MUST be consistent with literature review positioning statement

### Methodology (Extended Guidance)

- SHOULD reference architecture document for framework description
- SHOULD reference lifecycle document for process description
- Terminology MUST match supporting documents exactly
- MAY include table mapping paper sections to architecture layers

### Results (Extended Guidance)

For self-demonstrating papers, Results MUST include:

1. **Audit Results** - Concrete verification/validation outcomes
2. **Assurance Status** - Pass/fail, coverage percentage, invariant check
3. **Self-Demonstration Evidence** - How the paper proves the framework

**Quality Indicators:**
- Audit output is quoted or shown
- Assurance chart is visualized
- Verification checks are enumerated
- Human approver is named

### Discussion (Extended Guidance)

Limitations section SHOULD address:

- What aspects of the framework the paper cannot self-demonstrate
- Scope limitations acknowledged in supporting documents
- Single-instance limitation (N=1)
- Gap between source and submitted artifact (post-processing)

---

## Cross-Document Quality Workflow

### Recommended Production Sequence

For self-demonstrating papers, follow this sequence:

1. **Literature Review First** - Establishes scholarly foundation
2. **Novel Contributions Second** - Defines what you're claiming
3. **Architecture Third** - Captures technical framework
4. **Lifecycle Fourth** - Documents how you'll produce the paper
5. **Paper Last** - Synthesizes and demonstrates all of the above

### Quality Checkpoints

| After Document | Checkpoint |
|----------------|------------|
| Literature Review | Are gaps clear? Will paper fill them? |
| Novel Contributions | Are claims specific and defensible? |
| Architecture | Does it cover the framework completely? |
| Lifecycle | Can paper production follow this process? |
| Paper Draft | Does it align with all supporting documents? |
| Paper Final | Do all consistency checks pass? |

### Cross-Document Review

Before finalizing the paper, review for:

| Check | How to Verify |
|-------|---------------|
| Terminology consistency | Search for key terms across all documents |
| Citation alignment | Compare paper references to literature review catalog |
| Contribution match | Compare paper abstract/conclusion to novel contributions |
| Architecture coverage | Check all four layers mentioned in paper |
| Lifecycle enactment | Verify paper was produced using lifecycle phases |

---

## Common Issues and Solutions

### Coherence Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Terminology drift** | Same concept, different names | Create terminology glossary, use search-replace |
| **Orphan citations** | Paper cites sources not in literature review | Add to literature review or remove from paper |
| **Contribution creep** | Paper claims more than novel contributions | Align claims or update novel contributions (then re-assure) |
| **Architecture gaps** | Paper mentions components not in architecture | Add to architecture or remove from paper |

### Self-Demonstration Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Vague proof** | "We demonstrated by using it" without specifics | Add concrete audit results, assurance chart |
| **Missing evidence** | Claims of verification without output | Include actual verification results |
| **Invisible process** | Can't see lifecycle in paper's production | Narrate the process explicitly in Results |
| **Unstated self-reference** | Paper doesn't explicitly claim self-demonstration | Add explicit statement in Introduction and Results |

### Completeness Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Theme gaps** | Literature review theme not reflected in Background | Add subsection for missing theme |
| **Contribution omission** | Novel contribution not mentioned in paper | Add discussion of that contribution |
| **Layer missing** | Architecture layer not represented | Add content addressing missing layer |
| **Stakeholder forgotten** | Architecture stakeholder need unaddressed | Add motivation connecting to that need |

---

## Self-Assessment Rubric (Extended)

### Extended Quality Assessment

In addition to parent rubric, assess:

| Criterion | Poor (1) | Fair (2) | Good (3) | Excellent (4) |
|-----------|----------|----------|----------|---------------|
| Document Coherence | Major inconsistencies | Some drift | Generally aligned | Perfect consistency |
| Architecture Alignment | Layers missing | Most present | All covered | Deeply integrated |
| Lifecycle Enactment | Not visible | Implied | Referenced | Narrated |
| Literature Foundation | Citations mismatch | Mostly aligned | Well grounded | Themes mirrored |
| Contribution Integrity | Claims differ | Minor variation | Largely consistent | Exact match |
| Self-Demo Credibility | Hand-wavy | Some evidence | Convincing | Bulletproof |
| Traceability | Disconnected | Some links | Generally traceable | Seamlessly traceable |

**Extended Scoring:**
- 24-28: Excellent - compelling self-demonstration
- 18-23: Good - credible with minor gaps
- 12-17: Fair - significant coherence work needed
- 7-11: Poor - documents not aligned

**Combined Score (Parent + Extended):**
- Parent rubric: 24 max
- Extended rubric: 28 max
- Total: 52 max
- Target: ≥40 for excellent self-demonstrating paper

---

## Validation vs. Verification (Extended)

### Verification (Against spec-for-incose-self-demonstration)

Deterministic checks with yes/no answers:

- Do all four supporting documents exist?
- Are all consistency checks (C1-C4) satisfied?
- Are all completeness checks (CP1-CP4) satisfied?
- Does paper exist as vertex in assurance chart?
- Are self-demonstration checks (SD1-SD3) satisfied?

**Tool:** Cross-document checklist, automated consistency checks

### Validation (Against This Guidance)

Qualitative assessment requiring judgment:

- Is the coherence across documents compelling?
- Does the architecture alignment feel deep or superficial?
- Is the lifecycle visibly enacted?
- Does the literature foundation feel solid?
- Are the contributions credibly supported?
- Is the self-demonstration believable to a skeptic?
- Can a reader trace claims across documents?

**Tool:** Expert review, self-assessment against extended criteria

---

## Best Practices for Self-Demonstrating Papers

### The 10 Practices of Excellent Self-Demonstrations

1. **Prepare Supporting Documents First** - Paper is the capstone, not the starting point
2. **Use Exact Terminology** - Copy-paste key terms from supporting documents
3. **Structure Background by Theme** - Mirror literature review organization
4. **Quote the Architecture** - Use architecture document language when describing framework
5. **Narrate the Lifecycle** - Show readers you followed your own process
6. **Match Contributions Exactly** - Novel contributions document is authoritative
7. **Show Concrete Evidence** - Audit results, not just claims
8. **Visualize the Assurance** - A figure is worth a thousand words of proof
9. **Acknowledge Limitations Honestly** - What can't the paper prove about itself?
10. **Enable Traceability** - Readers should be able to follow the thread

---

## Related Documents

| Document | Relationship | Purpose |
|----------|--------------|---------|
| `v:guidance:incose-paper` | Parent guidance | Base quality criteria |
| `v:spec:incose-self-demonstration` | Coupled specification | Structural requirements |
| `v:guidance:architecture` | Supporting doc guidance | Architecture quality |
| `v:guidance:lifecycle` | Supporting doc guidance | Lifecycle quality |
| `v:guidance:incose-literature-review` | Supporting doc guidance | Literature review quality |
| `v:guidance:novel-contributions` | Supporting doc guidance | Novel contributions quality |

---

## Self-Consistency Note

This guidance document demonstrates the criteria it defines:

- **Coherence:** Consistent terminology with parent guidance and coupled specification
- **Architecture Alignment:** Extends parent structure faithfully
- **Traceability:** Clear inheritance from `guidance-for-incose-paper`
- **Completeness:** Covers all spec requirements with quality criteria
- **Credibility:** Specific assessment criteria, not vague platitudes

---

**Note:** This guidance extends `guidance-for-incose-paper` for self-demonstrating papers. The additional criteria ensure that "the paper is its own proof" is a credible, verifiable claim—not just marketing language. When a paper meets these criteria, the recursive self-demonstration genuinely advances the argument.
