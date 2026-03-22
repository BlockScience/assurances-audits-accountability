# CLI Reference

The `aaa` CLI is the primary interface for working with knowledge complexes.

## Commands

### `aaa init`

Initialize a new knowledge complex project.

```bash
aaa init <name>              # Create a new project
aaa init <name> --no-git     # Skip git initialization
```

Creates a project directory with:

- `00_vertices/`, `01_edges/`, `02_faces/` — simplicial complex element directories
- `charts/` — chart definitions
- Foundation files — core specs, guidances, and boundary elements
- `.gitignore` and `README.md`

### `aaa verify`

Verify a document against its type's Pydantic model.

```bash
aaa verify <file>            # Verify a single document
```

Checks that the document's YAML frontmatter conforms to the schema for its declared type.

### `aaa build`

Build an RDF graph from all markdown documents in the project.

```bash
aaa build                    # Build from current directory
aaa build <path>             # Build from a specific path
aaa build -o graph.ttl       # Specify output file
aaa build --format json-ld   # Output as JSON-LD
aaa build --strict           # Fail on first validation error
```

Walks the directory tree, parses each markdown document using its type's codec, and produces an RDF graph.

### `aaa audit`

Audit assurance coverage for a chart.

```bash
aaa audit <chart-dir>        # Audit a chart's assurance coverage
aaa audit <chart> -g graph.ttl  # Specify the RDF graph to use
aaa audit <chart> --no-tiling   # Skip tiling completeness check
```

Materializes the chart's SPARQL query against the graph and checks that every document in the resulting subcomplex has at least one assurance face.

### `aaa check`

Run topological and structural checks.

```bash
aaa check topology <chart>   # Euler characteristic, Betti numbers
aaa check types              # List all registered DocType edges
aaa check types -g graph.ttl # Specify the graph
```

## Output Formats

The `aaa build` command supports multiple RDF serialization formats:

| Format | Flag | Extension |
|--------|------|-----------|
| Turtle | `--format turtle` (default) | `.ttl` |
| JSON-LD | `--format json-ld` | `.jsonld` |
| N-Triples | `--format n-triples` | `.nt` |
