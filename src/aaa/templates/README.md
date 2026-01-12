# Templates

Type definitions for knowledge complex elements. Templates define the required structure for each simplex type.

## Structure

| Directory | Contains | Count |
|-----------|----------|-------|
| `00_vertices/` | Vertex type templates | 19 |
| `01_edges/` | Edge type templates | 12 |
| `02_faces/` | Face type templates | 6 |
| `charts/` | Chart type templates | 2 |

## Usage

Templates are used by `verify_template_based.py` to validate documents:

```bash
python scripts/verify_template_based.py <document.md> --templates templates
```

The script automatically matches documents to templates based on the `type` field in YAML frontmatter.

## Creating New Types

1. Create template in appropriate directory
2. Follow naming convention: `<type-name>.md`
3. Include all required YAML frontmatter fields
4. Document field constraints in markdown body

See existing templates for examples.

## Template Structure

Each template defines:
- **Required fields** - YAML frontmatter fields that must be present
- **Field types** - Expected data types (string, list, etc.)
- **Content sections** - Markdown sections that should appear in documents

## See Also

- [Scripts README](../scripts/README.md) - CLI tools including verification
- [Main README](../README.md) - Repository overview
