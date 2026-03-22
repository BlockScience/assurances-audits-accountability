---
type: vertex/spec
id: v:spec:conference-paper
name: Conference Paper Spec
version: "1.0"
description: >
  Structural requirements for a conference paper.
  Required sections: Abstract (250 words max), Introduction,
  Approach or Methods, Results or Findings, Conclusion, References.
  Required frontmatter fields: title, authors, venue, abstract, keywords.
  The abstract must be a standalone section, not inline in frontmatter.
tags:
  - spec
  - paper
  - academic
---

# Conference Paper Spec

A conference paper must demonstrate a complete research or engineering contribution
with sufficient detail for a qualified reader to assess and reproduce the claims.

## Required Structure

| Section | Requirement |
|---------|-------------|
| Abstract | 150–250 words; self-contained summary of contribution, method, and result |
| Introduction | Problem motivation, gap in literature, paper's claims |
| Approach / Methods | Reproducible description of how the work was done |
| Results / Findings | Empirical or analytical results addressing each claim |
| Conclusion | Summary, limitations, and future work |
| References | All cited works in a consistent format |

## Required Frontmatter

- `title`: Full paper title
- `authors`: List of author names
- `venue`: Target conference or journal
- `keywords`: 3–6 keywords
