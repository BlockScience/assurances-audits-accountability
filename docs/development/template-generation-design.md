# Template Generation System Design

**Date**: 2025-12-28
**Status**: Production
**Coverage**: 100% of critical functionality

---

## Overview

The template generation system automatically creates document templates from specification documents. This enables template-spec synchronization and ensures templates stay current with evolving specs.

## Architecture

### Core Components

1. **SpecParser** - Parses spec documents to extract frontmatter requirements
2. **TemplateGenerator** - Generates template content from parsed requirements
3. **BatchTemplateGenerator** - Manages bulk template generation and freshness checking

### File Structure

```
scripts/
├── generate_template_from_spec.py    # Core generation logic
└── generate_all_templates.py         # Batch operations

tests/
└── test_template_generation.py       # 13 comprehensive tests
```

## Spec Parsing

### Supported Spec Patterns

**Flat Fields**:
```markdown
| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `id` | string | REQUIRED | Document ID |
| `name` | string | REQUIRED | Display name |
```

**Nested Objects**:
```markdown
| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `elements` | object | REQUIRED | Chart elements |
| `elements.vertices` | array[string] | REQUIRED | Vertex IDs |
| `elements.edges` | array[string] | REQUIRED | Edge IDs |
```

**Array of Objects**:
```markdown
| `visualizations` | array[object] | OPTIONAL | Visualization files |

#### Visualization Object Structure

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `file` | string | REQUIRED | Path to file |
| `format` | string | REQUIRED | File format |
```

### Field Type Detection

- **Fixed Values**: Detects `Must be \`value\`` → generates `field: value`
- **Format Patterns**: Detects `Format: \`pattern\`` → generates `field: <placeholder>`
- **Datetime Fields**: Auto-detects datetime type → generates `YYYY-MM-DDTHH:MM:SSZ`

## Template Generation

### Generation Rules

1. **Required Fields**: Generate with placeholder or fixed value
2. **Optional Fields**: Generate with `# OPTIONAL` comment
3. **Nested Objects**: Generate hierarchical YAML structure
4. **Arrays**: Generate single-item example with all fields

### Array of Objects Format

**Generated Template**:
```yaml
visualizations:  # OPTIONAL
  -
    file: <path>
    format: <format>
    description: <description>
```

**Note**: Dash on own line, fields indented (fixed in Bug #1)

## Batch Operations

### Generate All Templates

```bash
python scripts/generate_all_templates.py
```

Generates templates for all specs:
- `00_vertices/spec-for-*.md` → `templates/00_vertices/*.md`
- `00_vertices/spec-for-charts.md` → `templates/charts/chart.md`

### Freshness Checking (CI)

```bash
python scripts/generate_all_templates.py --check
```

Verifies templates match their specs. Used in CI to enforce template-spec synchronization.

**Exit Codes**:
- 0: All templates fresh
- 1: One or more templates stale (requires regeneration)

## Bugs Fixed Through Testing

### Bug #1: Incomplete Array of Objects Generation

**Issue**: Only generated first field in array objects
**Test**: test_generate_array_of_objects_frontmatter
**Fix**: [generate_template_from_spec.py:334-365](../scripts/generate_template_from_spec.py#L334-L365)

**Before**:
```yaml
visualizations:  # OPTIONAL
  - file: <path>
    # format field missing!
```

**After**:
```yaml
visualizations:  # OPTIONAL
  -
    file: <path>
    format: <format>
```

### Bug #2: Trailing Newline Required for Table Parsing

**Issue**: Regex missed last row if table had no trailing newline
**Tests**: test_parse_spec_nested_objects, test_field_type_detection_fixed_values
**Fix**: Changed `(?:\|[^\n]+\|\n)+` → `(?:\|[^\n]+\|(?:\n|$))+`

## Testing

### Test Coverage

**13 tests across 4 categories**:
- SpecParser Tests (3): Flat fields, nested objects, array of objects
- TemplateGenerator Tests (6): Frontmatter generation, field type detection
- BatchTemplateGenerator Tests (2): Dry-run, freshness checking
- Real Spec Tests (2): Persona template, chart template

**Test Results**: 100% pass rate

### CI Integration

Template freshness check runs in GitHub Actions:
```yaml
- name: Check template freshness
  run: python scripts/generate_all_templates.py --check
```

Ensures templates stay synchronized with specs.

## Usage Examples

### Generate Single Template

```bash
python scripts/generate_template_from_spec.py 00_vertices/spec-for-persona.md --output templates/00_vertices/persona.md
```

### Generate All Templates

```bash
python scripts/generate_all_templates.py
```

### Check Freshness (CI)

```bash
python scripts/generate_all_templates.py --check
```

### Dry-Run Mode

```bash
python scripts/generate_all_templates.py --dry-run
```

Shows what would change without modifying files.

## Design Decisions

### Why Template Generation?

1. **Single Source of Truth**: Specs define structure, templates auto-generated
2. **Consistency**: All templates follow same patterns
3. **Maintainability**: Update spec once, template regenerates
4. **CI Enforcement**: Freshness check prevents drift

### Why Not Manual Templates?

- Manual templates drift from specs over time
- Inconsistent placeholder formats
- Missing fields when specs evolve
- No automated verification

### Trade-offs

**Pros**:
- Guaranteed spec-template consistency
- Automated updates when specs change
- Comprehensive test coverage

**Cons**:
- Generated templates may lack custom guidance
- Requires spec discipline (proper table formatting)
- Additional tooling complexity

**Decision**: Pros outweigh cons for a specification-driven system

## Future Enhancements

Potential additions:
- Template customization (inject custom sections)
- Multi-level nested object support
- Array of arrays support
- Template inheritance patterns
- Visual template editor

---

**See also:**
- [Test Coverage Documentation](test-coverage.md)
- [Scripts Reference](../../scripts/README.md) (to be created)
- [Learning Path: Templates](../learning/03-templates.md) (to be created)
