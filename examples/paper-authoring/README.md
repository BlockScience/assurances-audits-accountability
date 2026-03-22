# Paper Authoring Demo

A self-contained demonstration of the AAA framework showing the complete
workflow for defining a document type, authoring documents, and building
assurance through topological closure.

## What This Shows

**Scenario**: Two conference papers on knowledge complexes are defined,
authored, verified, validated, and assured within a single knowledge complex.

The demo illustrates three core properties of the framework:

1. **Document types are KC elements** — a "conference paper" type is a
   `DocType` edge connecting a spec vertex to a guidance vertex. It is
   queryable, addressable, and shared across all papers of that type.

2. **Assurance is topological closure** — a paper is assured when its
   verification edge (doc↔spec), validation edge (doc↔guidance), and
   DocType edge (spec↔guidance) form a closed triangle (a face element).

3. **Composition via charts** — the paper-series chart is a SPARQL query
   that materializes the closure of all assurance faces. New papers appear
   in the chart automatically when their triangles are added.

## Structure

```
content/
  00_vertices/
    spec-conference-paper.md       # Structural requirements for a paper
    guidance-conference-paper.md   # Quality criteria for a paper
    doc-kc-assurance-paper.md      # Paper 1: Knowledge Complexes for Assurance
    doc-audit-methods-paper.md     # Paper 2: Topological Audit Methods
    chart-paper-series.md          # Chart: SPARQL query for the paper series
  01_edges/
    e-doctype-conference-paper.md  # DocType: spec ↔ guidance
    e-verification-kc-paper.md     # Verification: paper 1 against spec
    e-validation-kc-paper.md       # Validation: paper 1 against guidance
    e-verification-audit-paper.md  # Verification: paper 2 against spec
    e-validation-audit-paper.md    # Validation: paper 2 against guidance
  02_faces/
    f-assurance-kc-paper.md        # Assurance face for paper 1
    f-assurance-audit-paper.md     # Assurance face for paper 2
```

## Running

```bash
# From the repo root
cd examples/paper-authoring
python demo.py

# Or use the CLI directly on the content:
aaa build content/ --output /tmp/papers.ttl
aaa verify content/00_vertices/spec-conference-paper.md --verbose
aaa verify content/02_faces/f-assurance-kc-paper.md --verbose
```

## Topology

The knowledge complex has the following structure:

```
        v:spec:conference-paper
       /                        \
e:verification:*       e:DocType:conference-paper
     /                              \
v:doc:*                        v:guidance:conference-paper
     \                              /
      e:validation:*         ------
              \             /
               (assurance face)
```

Two assurance triangles share the `e:DocType:conference-paper` edge.
The document type definition is a shared structural element — not
duplicated per paper.

- V = 5 (spec, guidance, 2 docs, 1 chart)
- E = 5 (1 DocType, 2 verification, 2 validation)
- F = 2 (2 assurance faces)
- χ = V − E + F = 2
