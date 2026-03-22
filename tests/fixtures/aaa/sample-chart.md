---
type: vertex/chart
id: v:chart:sample
name: Sample Chart
extends: doc
description: A minimal chart for testing.
query: |
  PREFIX aaa: <https://example.org/aaa#>
  SELECT ?element WHERE {
    ?element a ?type .
    ?type rdfs:subClassOf* aaa:doc .
  }
tags:
  - vertex
  - doc
  - chart
---

# Sample Chart

A minimal chart that selects all doc-typed elements.
