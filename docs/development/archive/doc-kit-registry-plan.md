# Doc-Kit Registry Chart Plan

## Purpose

Provide an easy lookup chart showing all available doc-kits (spec + guidance + example packages) in the knowledge complex. Serves as a registry/index for document creators to find templates and examples.

## Chart Metadata

```yaml
type: chart/chart
id: c:doc-kit-registry
name: Doc-Kit Registry
purpose: Provide easy lookup of all available doc-kits for document creation
scope: All doc-kit faces in the knowledge complex
construction_method: automated (can be generated from cache query)
```

## Elements

### Vertices (Doc-Kits)

Currently available:
- **f:doc_kit:persona** - Persona document package
  - Spec: v:spec:persona
  - Guidance: v:guidance:persona
  - Example: v:persona:example (if exists)

Future doc-kits to add:
- f:doc_kit:purpose
- f:doc_kit:protocol
- f:doc_kit:spec
- f:doc_kit:guidance
- f:doc_kit:system_prompt
- f:doc_kit:chart (?)

### Edges

Potentially none - this is a simple registry chart showing available doc-kits. Edges between doc-kits themselves may not be meaningful.

Alternative: Could show inheritance edges between doc-kit types if doc-kit specialization exists.

### Chart Properties

- **Dimension:** 0 (vertices only) or 1 if we add relationships
- **Euler Characteristic:** χ = V (if no edges/faces)
- **Type:** Registry/Catalog chart

## Sections

### Why This Chart Exists

**Motivation:** Users need a quick way to discover what document types are supported and where to find their templates, guidance, and examples.

**Context:** The knowledge complex uses typed documents. Each type should have a complete doc-kit (spec + guidance + example). This chart serves as the index.

**Intended Use:**
- Quick reference for document creators
- Verification that doc-kits are complete
- Discovery of available document types
- Quality check: every document type should have a complete doc-kit

### What This Chart Contains

**Included:**
- All doc-kit faces (type: face/doc_kit)
- Metadata about each doc-kit (what docs it contains)
- Completeness status (has spec? has guidance? has example?)

**Excluded:**
- Individual spec/guidance/example documents (those are vertices OF the doc-kits, not separate)
- Instances of documents (only the doc-kit packages themselves)

### How This Chart Was Constructed

**Method:** Automated (query cache for all face/doc_kit elements)

**Process:**
1. Query cache for all faces with type: face/doc_kit
2. Extract vertices from each doc-kit face
3. Check completeness (spec exists? guidance exists? example exists?)
4. Generate chart with completeness indicators

**Quality Assurance:**
- Verify all doc-kit faces are included
- Check that doc-kit faces reference real vertices
- Ensure completeness indicators are accurate

## Element Tables

### Doc-Kits (0-Cells)

| ID | Name | Spec | Guidance | Example | Status |
|----|------|------|----------|---------|--------|
| f:doc_kit:persona | Persona Doc-Kit | v:spec:persona | v:guidance:persona | v:persona:example | ✅ Complete |
| f:doc_kit:purpose | Purpose Doc-Kit | v:spec:purpose | v:guidance:purpose | v:purpose:example | ⚠️ Missing example |
| f:doc_kit:protocol | Protocol Doc-Kit | v:spec:protocol | v:guidance:protocol | v:protocol:example | ⚠️ Missing example |

(Additional rows as doc-kits are created)

**Total:** N doc-kits

## Interpretation

**What This Chart Reveals:**
- How many document types are fully supported (complete doc-kits)
- Which doc-kits are missing examples
- Coverage of the PPP framework (persona, purpose, protocol all have doc-kits)
- Gap analysis for future doc-kit creation

**Key Observations:**
- Every type in PPP framework should have complete doc-kit
- Missing examples indicate documentation debt
- Doc-kit completeness = quality indicator for type system

**Implications:**
- Users can trust document types with complete doc-kits
- Missing examples mean users must create instances without reference
- Incomplete doc-kits should be prioritized for completion

## Verification

```bash
# Verify this chart structure
python scripts/verify_chart.py charts/doc-kit-registry.md

# Query for all doc-kits
python -c "
import json
cache = json.load(open('complex.json'))
doc_kits = [f for f in cache['elements']['faces'].values()
            if f.get('type') == 'face/doc_kit']
print(f'Found {len(doc_kits)} doc-kits')
for dk in doc_kits:
    print(f\"  - {dk['id']}: {dk['name']}\")
"
```

## Implementation Notes

This chart can be **automatically generated** from the cache:
- Scan for all face/doc_kit elements
- Extract their vertices (spec, guidance, example)
- Check vertex existence in cache
- Generate chart markdown

Regeneration workflow:
```bash
python scripts/generate_doc_kit_registry.py > charts/doc-kit-registry/doc-kit-registry.md
```

This makes the registry self-updating as new doc-kits are added.

## Future Enhancements

- Add "last updated" dates for each doc-kit
- Show version numbers for spec/guidance
- Link to assurance faces for each doc-kit component
- Color-code by completeness status
- Generate Obsidian dataview query version for dynamic updates
