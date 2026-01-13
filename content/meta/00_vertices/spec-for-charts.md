---
type: vertex/spec
extends: doc
id: v:spec:chart
name: Specification for Chart Documents
description: Defines what makes a valid chart document in the knowledge complex
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-27T20:00:00Z
modified: 2025-12-27T20:00:00Z
dependencies: []
---

# Specification for Chart Documents

**This specification defines the structure and requirements for all chart documents in the knowledge complex.**

## Purpose

Charts are named collections of vertices, edges, and faces that form coherent subcomplexes within the knowledge complex. This spec-for-charts establishes what fields, sections, and properties must be present in any valid chart document.

## Required Frontmatter Fields

All chart documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `chart/chart` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `c:<name>`) |
| `name` | string | REQUIRED | Human-readable chart name |
| `tags` | array[string] | REQUIRED | Must include `[chart]` at minimum |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Chart Construction Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `constructed_by` | string | REQUIRED | Person or system who constructed this chart |
| `construction_method` | enum | REQUIRED | One of: `manual`, `assisted`, `automated` |
| `construction_date` | datetime | REQUIRED | ISO 8601 timestamp when chart was constructed |

### Chart Purpose and Scope

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `purpose` | string | REQUIRED | Why this chart was constructed - the motivation or question it addresses |
| `scope` | string | REQUIRED | What is included in this chart and what is deliberately excluded |

### Chart Elements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `elements` | object | REQUIRED | Container for element arrays |
| `elements.vertices` | array[string] | REQUIRED | Array of vertex IDs (may be empty) |
| `elements.edges` | array[string] | REQUIRED | Array of edge IDs (may be empty) |
| `elements.faces` | array[string] | OPTIONAL | Array of face IDs (may be omitted if no faces) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of what this chart represents |
| `visualizations` | array[object] | OPTIONAL | References to visualization artifacts |

#### Visualization Object Structure

If `visualizations` array is present, each object MUST contain:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `file` | string | REQUIRED | Path to visualization file |
| `format` | string | REQUIRED | File format (svg, png, pdf, html, dot, etc.) |
| `description` | string | REQUIRED | What this visualization shows |
| `generated` | datetime | REQUIRED | ISO 8601 timestamp when generated |
| `generator` | string | REQUIRED | Tool or person who generated it |

## Required Body Sections

The markdown body of a chart document MUST contain:

### 1. Chart Overview

A brief description of the chart and its purpose.

**Format:**
```markdown
# Chart: <Chart Name>

<Brief description of the chart and its purpose>
```

### 2. Why This Chart Exists

Explains the motivation, context, and intended use of the chart.

**Format:**
```markdown
## Why This Chart Exists

**Motivation:** <Why was this chart constructed? What question does it answer?>

**Context:** <What was happening that led to creating this chart?>

**Intended Use:** <How should this chart be used? Who is the audience?>
```

**Requirements:**
- MUST include all three subsections: Motivation, Context, Intended Use
- Each subsection MUST have substantive content (not just placeholders)

### 3. What This Chart Contains

Defines the scope and provides an element summary.

**Format:**
```markdown
## What This Chart Contains

### Scope Definition

**Included:**
- <What elements are included in this chart>
- <What relationships are shown>

**Excluded:**
- <What elements are deliberately not included>
- <Why certain elements were excluded>

**Boundaries:**
- <Where this chart begins and ends>

### Element Summary

**Vertices (N):** <Brief description of what the vertices represent>

**Edges (M):** <Brief description of what the edges represent>

**Faces (P):** <Brief description of what the faces represent>

**Dimension:** <Highest dimensional cells included>
```

**Requirements:**
- MUST include Scope Definition with Included, Excluded, and Boundaries
- MUST include Element Summary with counts and descriptions
- Dimension MUST be 0 (vertices only), 1 (includes edges), 2 (includes faces), or higher

### 4. How This Chart Was Constructed

Documents the construction process, constructor, and quality assurance.

**Format:**
```markdown
## How This Chart Was Constructed

**Construction Method:** <manual | assisted | automated>

**Process:**
1. <Step-by-step description of how the chart was built>
2. <What sources were consulted>
3. <What decisions were made>

**Constructor:** <Person or system who constructed this chart>

**Date Constructed:** YYYY-MM-DD

**Quality Assurance:**
- <How was completeness verified?>
- <How were errors checked?>
```

**Requirements:**
- MUST match `construction_method` frontmatter value
- Constructor MUST match `constructed_by` frontmatter value
- Process MUST have at least 2 steps
- Quality Assurance MUST describe verification approach

### 5. Element Tables

Structured tables listing all vertices, edges, and faces in the chart.

**Format:**
```markdown
## Vertices (0-Cells)

List of vertices in this chart:

| ID | Name | Type | Role in Chart |
|----|------|------|---------------|
| <vertex-id> | <name> | <type> | <what this vertex represents> |

**Total:** N vertices

## Edges (1-Cells)

List of edges in this chart:

| ID | Name | Type | Source | Target | Relationship |
|----|------|------|--------|--------|-----------------|
| <edge-id> | <name> | <type> | <source-id> | <target-id> | <what this edge represents> |

**Total:** M edges

## Faces (2-Cells)

List of faces in this chart (if any):

| ID | Name | Type | Boundary Edges | Represents |
|----|------|------|----------------|------------|
| <face-id> | <name> | <type> | <edge-ids> | <what this face represents> |

**Total:** P faces
```

**Requirements:**
- MUST include Vertices section (even if empty)
- MUST include Edges section (even if empty)
- Faces section OPTIONAL if no faces in chart
- Table row counts MUST match Element Summary counts
- Element IDs in tables MUST match frontmatter element arrays

### 6. Chart Properties

Describes topological and structural properties.

**Format:**
```markdown
## Chart Properties

### Topological Properties

- **Euler Characteristic:** χ = V - E + F = <value>
- **Connected:** Yes/No (<number of components>)
- **Cycles:** <List any significant cycles>

### Structural Properties

- **Completeness:** <Is this a complete subcomplex?>
- **Regularity:** <Any regular patterns?>
- **Hierarchies:** <Any hierarchical structure?>
```

**Requirements:**
- MUST include Topological Properties
- MUST compute Euler characteristic if faces present
- MUST state connectivity

### 7. Verification

Provides commands for verifying the chart structure.

**Format:**
```markdown
## Verification

### Structural Verification

\`\`\`bash
# Verify this chart structure
python scripts/verify_chart.py charts/<chart-name>.md
\`\`\`

**Expected Result:** ✓ Valid simplicial complex

**Checks:**
- All referenced elements exist
- Edges have valid boundaries
- Faces have valid boundaries
- Forms valid simplicial complex
```

**Requirements:**
- MUST include verification commands
- MUST state expected results
- MUST list what checks are performed

## Recommended Body Sections

### Interpretation

Analysis of what the chart reveals, key observations, and implications.

**Format:**
```markdown
## Interpretation

**What This Chart Reveals:** <What insights does this chart provide?>

**Key Observations:**
- <Important observation 1>
- <Important observation 2>

**Implications:**
- <What does this chart tell us?>
- <What decisions might this inform?>

**Limitations:**
- <What this chart doesn't show>
- <Where interpretation should be cautious>
```

**Requirement:** RECOMMENDED (strongly encouraged for meaningful charts)

### Visualizations

References to visual artifacts if they exist.

**Format:**
```markdown
## Visualizations

### Available Visualizations

| Format | File | Description | Generated |
|--------|------|-------------|-----------|
| <format> | [link](<path>) | <what it shows> | YYYY-MM-DD |

### Visualization Notes

**Recommended View:** <Which visualization is best?>

**Interpretation Guide:** <How to read the visualizations?>
```

**Requirement:** OPTIONAL (only include if visualizations exist)

### Chart Metadata

Summary table of all chart metadata.

**Format:**
```markdown
## Chart Metadata

| Property | Value |
|----------|-------|
| Chart ID | c:<name> |
| Constructed By | <constructor> |
| Construction Method | <method> |
| Vertices | N |
| Edges | M |
| Faces | P |
```

**Requirement:** RECOMMENDED

### Related Charts

Links to related charts.

**Format:**
```markdown
## Related Charts

| Chart | Relationship | Notes |
|-------|--------------|-------|
| [Chart Name](path.md) | <extends/overlaps/complements> | <description> |
```

**Requirement:** OPTIONAL

## Type Constraints

1. **Type Field:** MUST be exactly `chart/chart`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `c:[kebab-case-name]`
4. **Element IDs:** All vertex IDs MUST start with `v:`, edge IDs with `e:`, face IDs with `f:`
5. **Element Existence:** All referenced elements MUST exist in the knowledge complex

## Content Requirements

1. **Constructive Language:** Charts document what was constructed and why
2. **Completeness:** All included elements must be listed in tables
3. **Coherence:** Element lists in frontmatter and body must match exactly
4. **Verification:** Charts must be verifiable as valid simplicial complexes
5. **Documentation:** Purpose, scope, and construction process must be clearly stated

## Simplicial Complex Requirements

For a chart to be a valid simplicial complex:

1. **Element Existence:** All referenced vertices, edges, and faces must exist in the cache
2. **Edge Boundaries:** For each edge in the chart, both source and target vertices must be in the chart
3. **Face Boundaries:** For each face in the chart, all boundary edges must be in the chart
4. **Boundary Matching:** Face vertices must match edge endpoints consistently

These requirements are checked by `verify_chart.py`.

## Schema Summary

```yaml
# Required frontmatter
type: chart/chart
extends: doc
id: c:<name>
name: <string>
tags: [chart]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
dependencies: []

# Chart construction metadata
constructed_by: <string>
construction_method: manual | assisted | automated
construction_date: <ISO8601>

# Chart purpose and scope
purpose: <string>
scope: <string>

# Chart elements
elements:
  vertices: [<v:id>, ...]
  edges: [<e:id>, ...]
  faces: [<f:id>, ...]  # OPTIONAL

# Optional frontmatter
description: <string>
visualizations:  # OPTIONAL
  - file: <path>
    format: <format>
    description: <string>
    generated: <ISO8601>
    generator: <string>

# Required body sections (markdown)
# Chart: <Chart Name>
## Why This Chart Exists
  **Motivation:** ...
  **Context:** ...
  **Intended Use:** ...
## What This Chart Contains
  ### Scope Definition
  ### Element Summary
## How This Chart Was Constructed
  **Construction Method:** ...
  **Process:** ...
  **Constructor:** ...
  **Quality Assurance:** ...
## Vertices (0-Cells)
  [table]
  **Total:** N vertices
## Edges (1-Cells)
  [table]
  **Total:** M edges
## Faces (2-Cells)  # OPTIONAL if no faces
  [table]
  **Total:** P faces
## Chart Properties
  ### Topological Properties
  ### Structural Properties
## Verification

# Recommended body sections
## Interpretation
## Visualizations  # only if visualizations exist
## Chart Metadata
## Related Charts
```

## Compliance

A document claiming `type: chart/chart` is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present
3. Element arrays in frontmatter match element tables in body
4. All referenced elements exist (verifiable via cache)
5. Construction metadata is complete and consistent
6. Purpose and scope are clearly stated
7. Forms valid simplicial complex (verifiable via `verify_chart.py`)

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that structural requirements are met
- **Validation** (against guidance-for-charts): Qualitative assessment of chart quality and fitness-for-purpose

---

**Note:** Charts extend `doc` and can thus participate in the full assurance framework (coupling, verification, validation, assurance) once paired with guidance-for-charts.
