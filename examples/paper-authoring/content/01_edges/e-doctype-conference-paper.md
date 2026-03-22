---
type: edge/DocType
id: e:DocType:conference-paper
name: Conference Paper
source: v:spec:conference-paper
target: v:guidance:conference-paper
description: >
  A structured technical paper suitable for conference submission.
  The document type is defined by the pairing of the Conference Paper Spec
  (structural requirements) and Conference Paper Guidance (quality criteria).
  As a DocType edge, this element is itself addressable and queryable —
  listing all DocType elements gives the complete catalogue of document types
  defined in this knowledge complex.
commonly_used_for: Research results, engineering analyses, empirical studies, system designs
---

# Conference Paper (Document Type)

This edge defines the "conference paper" document type by connecting:

- **Source (spec)**: `v:spec:conference-paper` — what a paper must contain
- **Target (guidance)**: `v:guidance:conference-paper` — how well it must be written

The edge is shared by every assurance triangle for conference papers. Two
papers can be assured by two different faces while both reference this single
DocType edge — the type definition is reused, not copied.
