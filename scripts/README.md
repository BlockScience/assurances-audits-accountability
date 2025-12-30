# Scripts

CLI tools for working with knowledge complexes.

## Categories

### Verification & Validation

| Script | Purpose |
|--------|---------|
| `verify_template_based.py` | Verify document against its template |
| `verify_chart.py` | Validate chart structure and references |
| `verify_structure.py` | Check YAML frontmatter structure |
| `verify_spec.py` | Validate spec documents |
| `verify_typed.py` | Check type consistency |
| `verify_dependency_hierarchy.py` | Validate dependency ordering |
| `check_accountability.py` | Validate accountability statements |

### Analysis & Visualization

| Script | Purpose |
|--------|---------|
| `topology.py` | Calculate Euler characteristic, detect holes |
| `visualize_chart.py` | Generate interactive 3D HTML visualization |
| `visualize_syllabus.py` | Learning path visualization for syllabus charts |
| `hodge_analysis.py` | Algebraic topology analysis (advanced) |

### Build & Export

| Script | Purpose |
|--------|---------|
| `build_cache.py` | Generate complex.json cache for all elements |
| `export_chart_direct.py` | Export chart to JSON format |
| `compile_document.py` | Expand Obsidian embeds to standalone markdown |
| `parse_chart.py` | Parse chart markdown to structured data |

### Composition

| Script | Purpose |
|--------|---------|
| `compose_charts.py` | Compose two charts via identification |
| `compose_charts_multi.py` | Iteratively compose multiple charts |

### Audit

| Script | Purpose |
|--------|---------|
| `audit_assurance_chart.py` | Verify complete assurance coverage |

### Generation

| Script | Purpose |
|--------|---------|
| `generate_template_from_spec.py` | Generate template from spec document |
| `generate_all_templates.py` | Batch generate all templates |
| `generate_assurance_audit_elements.py` | Generate assurance audit elements |

### Internal

| Script | Purpose |
|--------|---------|
| `template_parser.py` | Template parsing utilities |
| `test_*.py` | Test scripts |

## Common Usage

```bash
# Build cache (run first after setup)
python scripts/build_cache.py

# Verify a document against its template
python scripts/verify_template_based.py <file.md> --templates templates

# Verify a chart
python scripts/verify_chart.py charts/<chart>/<chart>.md

# Analyze chart topology
python scripts/topology.py charts/<chart>/<chart>.md --root .

# Export and visualize
python scripts/export_chart_direct.py charts/<chart>/<chart>.md output.json --root .
python scripts/visualize_chart.py output.json

# Compose two charts
python scripts/compose_charts.py chart1.json chart2.json output.json

# Audit assurance coverage
python scripts/audit_assurance_chart.py charts/<chart>/<chart>.md
```

## See Also

- [Templates README](../templates/README.md) - Type definitions
- [Main README](../README.md) - Repository overview
