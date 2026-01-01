---
type: vertex/guidance
extends: guidance
id: v:guidance:background-section
name: Guidance for INCOSE Paper Background/Related Work Section
tags:
  - vertex
  - guidance
  - background
version: 1.0.0
created: 2025-12-31T19:35:00Z
modified: 2025-12-31T19:35:00Z
description: Quality criteria and best practices for writing excellent Background sections in INCOSE symposium papers
criteria:
  - synthesis-quality
  - gap-articulation
  - citation-appropriateness
  - balance-and-proportion
  - accessibility
rubric: validation-assessment
dependencies:
  - v:spec:background-section
---

# Guidance for INCOSE Paper Background/Related Work Section

## Purpose Statement

While [spec-for-background-section](spec-for-background-section.md) defines **what** structural elements the Background must contain, this guidance helps authors assess **how well** the Background contextualizes the contribution and positions the work.

Great Background sections synthesize rather than survey, identify genuine gaps, and provide just enough context for readers to understand the contribution without overwhelming them.

## Quality Criteria

### 1. Synthesis Quality

**Definition:** The Background synthesizes related work to identify patterns, gaps, and opportunities rather than just listing prior art.

| Level | Indicators |
|-------|------------|
| **Excellent** | Identifies themes across multiple works. Compares/contrasts approaches. Shows how different threads connect. Reader gains insight beyond individual paper summaries. Clear narrative emerges. |
| **Good** | Groups related work reasonably. Some synthesis present. Most connections are explicit. Minor missed opportunities for deeper integration. |
| **Needs Improvement** | Reads like annotated bibliography. Papers listed sequentially without connections. No synthesis or patterns identified. "Author X did Y, Author Z did W..." |

**Strong Synthesis Example:**
"Carlsson \parencite{Carlsson2009}, Ghrist \parencite{Ghrist2008}, and Reimann et al. \parencite{Reimann2017} demonstrate topology's power for analyzing complex data structures—from high-dimensional datasets to neural networks. What these applications share is using topological invariants to reveal structural features invisible to traditional methods."

**Weak Survey Example:**
"Carlsson (2009) studied topology and data. Ghrist (2008) worked on barcodes. Reimann et al. (2017) applied this to neurons."

### 2. Gap Articulation

**Definition:** The gap between existing work and your contribution is explicitly identified and justified.

| Level | Indicators |
|-------|------------|
| **Excellent** | Gap is specific and well-motivated. Prior work is acknowledged fairly. Clear explanation of why gap matters. Sets up contribution naturally without forced positioning. |
| **Good** | Gap is identified though may lack specificity. Connection to contribution is present. Some justification for why gap matters. |
| **Needs Improvement** | No explicit gap, or gap is vague. Straw man arguments against prior work. Unclear why gap matters. Contribution seems disconnected from background. |

**Effective Gap Statement:**
"While these standards codify V&V processes, they do not formalize the relationship between verification criteria and validation criteria. The spec-guidance coupling remains implicit."

**Ineffective Gap:**
"No one has done exactly what we're doing." (Probably not true, and not useful)

### 3. Citation Appropriateness

**Definition:** Citations are to primary sources, fairly represent work cited, and support claims made.

| Level | Indicators |
|-------|------------|
| **Excellent** | Cites primary sources (original papers, not surveys citing them). Citations accurately represent work. Balance of foundational classics and recent work. No drive-by citations. |
| **Good** | Mostly primary sources with occasional secondary. Citations generally accurate. Reasonable recency balance. |
| **Needs Improvement** | Cites surveys instead of originals. Misrepresents cited work. All old citations or all brand new. Citations dropped without context. |

**Citation Best Practices:**
- ✅ Boehm's original 1984 paper for V&V distinction
- ✅ Current version of standards (IEEE 1012-2016, not 1998 version)
- ✅ Ghrist's 2008 Barcodes paper for persistent homology
- ❌ Citing review paper about Boehm instead of Boehm directly
- ❌ "Many researchers have studied this \parencite{Random2020}" (who? which researchers?)

### 4. Balance and Proportion

**Definition:** Background provides necessary context without overwhelming contribution or creating imbalance.

| Level | Indicators |
|-------|----------||
| **Excellent** | Background is substantial but proportional (15-20% of paper). No subsection dominates. Each topic gets appropriate depth. Reader has context needed, no more. |
| **Good** | Generally balanced with minor proportion issues. One subsection may be slightly long but doesn't distort paper. Adequate context provided. |
| **Needs Improvement** | Background overwhelms paper (>30% of length). One topic gets excessive depth while others are superficial. Imbalanced subsections. Reader lost in details. |

**Balance Check:**
- Background should be shorter than your contribution sections combined
- No single subsection > 500 words unless truly foundational
- If Background > 2000 words, question whether all content is necessary

### 5. Accessibility

**Definition:** Background is accessible to INCOSE's diverse audience while maintaining rigor.

| Level | Indicators |
|-------|------------|
| **Excellent** | Technical concepts explained clearly. Jargon defined. Examples ground abstractions. SE practitioners can follow without being domain experts. Mathematically rigorous without being inaccessible. |
| **Good** | Generally accessible with minor technical barriers. Most concepts explained. Occasional undefined terms but context helps. |
| **Needs Improvement** | Assumes specialist knowledge. Undefined jargon. Abstract mathematical exposition without examples. Excludes non-expert readers. |

**Accessibility Techniques:**
- Define on first use: "simplicial complexes (combinatorial structures built from vertices, edges, and higher-dimensional faces)"
- Ground with examples: "For document assurance, vertices represent documents..."
- Explain significance: "This matters because..."
- Use analogies carefully: "Like triangulation in surveying..."

## Validation Assessment Rubric

### Scoring System

Each criterion scored 0-4:
- **4 - Excellent**: Meets all "Excellent" indicators
- **3 - Good**: Meets most "Good" indicators
- **2 - Acceptable**: Has issues but fundamentally sound
- **1 - Needs Revision**: Significant problems
- **0 - Missing/Failed**: Criterion not met

**Total possible**: 20 points (5 criteria × 4 points)

**Targets:**
- **17-20**: Excellent Background, ready for integration
- **13-16**: Good Background, minor revisions recommended
- **10-12**: Acceptable but needs improvement
- **<10**: Requires significant revision

## Common Issues and Solutions

### Issue: Literature dump without synthesis

**Symptoms:** Each paragraph describes one paper, no connections drawn

**Solutions:**
- Organize by theme, not chronologically
- Group related approaches together
- Explicitly state patterns: "These approaches share..."
- Compare and contrast: "Unlike X which..., Y provides..."
- Identify trends: "Recent work increasingly focuses on..."

### Issue: Background overwhelming contribution

**Symptoms:** Background is longest section, detailed exposition of others' work

**Solutions:**
- Cut to essentials: keep only what's needed for your contribution
- Move excessive detail to citations ("for details, see \parencite{...}")
- Ask: "Does reader need this to understand our work?"
- Aim for 15-20% of paper length, not 30-40%

### Issue: Straw man arguments

**Symptoms:** Misrepresenting prior work to make yours look better

**Solutions:**
- Cite fairly and accurately
- Acknowledge what prior work accomplished
- Identify genuine gaps, not fabricated weaknesses
- Distinguish "doesn't address X" from "fails at X"
- Be generous: "While effective for Y, doesn't handle Z"

### Issue: Missing recent work

**Symptoms:** All citations >5 years old, ignoring current state

**Solutions:**
- Search recent conferences (INCOSE IS, IEEE SysCon)
- Include 2023-2025 work if relevant
- Balance: foundational classics + recent advances
- Acknowledge if recent work is sparse in your niche

### Issue: Orphaned background

**Symptoms:** Topics introduced but never used later in paper

**Solutions:**
- Review: is every concept in Background referenced later?
- Remove tangential material no matter how interesting
- If introducing technique, show where you use it
- Ensure technical terms defined here appear in Framework

## Best Practices

### Organizing Background

**By Theme (Recommended):**
```latex
\subsection{V\&V Foundations}
...
\subsection{Algebraic Topology}
...
\subsection{AI Accountability}
...
```

**NOT Chronologically:**
```latex
\subsection{Early Work (1980s)}  % ❌ Don't do this
\subsection{Recent Advances (2020s)}  % ❌ Don't do this
```

### Handling Standards

First mention: spell out + cite
```latex
IEEE Standard 1012 \parencite{IEEE1012} codifies...
```

Subsequent mentions: abbreviation
```latex
As IEEE 1012 specifies...
```

### Comparison Tables

Effective for synthesizing related approaches:

```latex
\begin{table}[H]
\centering
\begin{tabular}{lllll}
\toprule
Framework & Verification & Validation & Coupling & Accountability \\
\midrule
IEEE 1012 & Yes & Yes & Implicit & Process-based \\
ISO 15288 & Yes & Yes & Implicit & Role-based \\
Ours & Yes & Yes & Explicit & Structural \\
\bottomrule
\end{tabular}
\caption{Comparison of V\&V Frameworks}
\label{tab:vv-comparison}
\end{table}
```

### Positioning Prior Art

When closely related work exists:

**Acknowledge fairly:**
"Ghrist's 'The Forge' \parencite{Ghrist2025Forge} demonstrates that procedural accountability is achievable through disciplined practice."

**Distinguish clearly:**
"Our contribution differs: where Ghrist's approach is *procedural* (documenting how he maintained accountability), ours is *structural* (enforcing accountability through type system requirements)."

**Show respect:**
"Ghrist's methodological insight—'Every sentence... passed through my judgment'—informs our design goal: make such accountability structurally required, not merely aspirational."

### Transitioning to Framework

**Optional but effective:**
End Background with brief synthesis paragraph:

"While these foundations provide [list what exists], they lack [gap]. The framework presented in Section 3 addresses this by [preview contribution]."

## Self-Editing Checklist

Before submitting for validation:

- [ ] Organized by theme, not chronologically
- [ ] Each subsection has clear purpose
- [ ] All technical terms defined
- [ ] At least 10 citations total
- [ ] Citations are to primary sources
- [ ] Prior work represented fairly
- [ ] Gap explicitly identified
- [ ] Balance: Background < Contribution sections
- [ ] No orphaned content
- [ ] Accessible to SE practitioners
- [ ] Synthesis present, not just survey
- [ ] Transitions between subsections smooth

---

**Note:** This guidance enables validation of Background sections for fitness-for-purpose. Used with [spec-for-background-section](spec-for-background-section.md), it supports complete V&V for Background development.
