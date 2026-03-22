---
type: vertex/chart
id: v:chart:paper-series
name: Paper Series on Knowledge Complexes
version: "1.0"
description: >
  A chart materializing all elements that participate in at least one
  assurance face. The query walks the boundary hierarchy from assurance
  faces down to their boundary edges and further to the boundary vertices.
  The result is the closure of all assurance faces — the minimal subcomplex
  covering every assured document in the series.
tags:
  - chart
  - paper-series
  - assurance
query: |
  PREFIX aaa: <https://example.org/aaa#>
  PREFIX kc: <https://w3id.org/kc#>
  SELECT DISTINCT ?elem WHERE {
    { ?elem a aaa:assurance . }
    UNION
    { ?face a aaa:assurance . ?face kc:boundedBy ?elem . }
    UNION
    { ?face a aaa:assurance . ?face kc:boundedBy ?edge . ?edge kc:boundedBy ?elem . }
  }
---

# Paper Series on Knowledge Complexes

A chart whose SPARQL query materializes the closure of all assurance faces
in this knowledge complex. This includes:

- Every assurance face (2-simplex)
- Every edge in the boundary of an assurance face (DocType, verification, validation)
- Every vertex in the boundary of those edges (docs, specs, guidances)

The resulting subcomplex represents the complete "paper series" — all
documents and their assurance infrastructure — without needing to enumerate
them explicitly. New papers added to the complex appear automatically in
the chart when their assurance faces are added.
