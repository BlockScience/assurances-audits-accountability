# Specs vs Templates: Analysis of Auto-Generation Feasibility

**Date**: 2025-12-28
**Author**: Claude (analysis requested by mzargham)

## Executive Summary

**Question**: Can templates be deterministically computed from specs via scripts?

**Answer**: **Yes, with high fidelity** - but there are important tradeoffs to consider.

**Recommendation**: **Specs are the authoritative type system. Templates should be generated from specs** for Obsidian compatibility, not vice versa.

---

## Current State Analysis

### What Are Specs?

Specs (e.g., `spec-for-persona.md`) are **prescriptive documents** that define:
- **Required frontmatter fields** with types and constraints
- **Required body sections** with formatting requirements
- **Validation rules** (e.g., "MUST be specific", "SHOULD use active voice")
- **Semantic requirements** (what makes content valid vs invalid)

**Example from spec-for-persona.md:**
```markdown
| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/persona` |
| `extends` | string | REQUIRED | Must be `doc` |
```

### What Are Templates?

Templates (e.g., `templates/00_vertices/persona.md`) are **Obsidian-compatible scaffolds** that:
- Provide placeholder structure for creating new documents
- Use `<name>` placeholders for variable content
- Include example formats and helper text
- Are designed for **human instantiation** (copy → fill in blanks)

**Example from persona template:**
```markdown
---
type: vertex/persona
extends: doc
id: v:persona:<name>
name: <Persona Name>
---

## Purpose

This persona defines [role/identity description].
```

### Current Relationship

**Right now:**
- **Specs** define the requirements (authoritative type system)
- **Templates** implement those requirements (Obsidian tooling)
- **verify_template_based.py** reads templates to verify documents
- Templates are **manually maintained** to match specs

**Problem**: Two sources of truth that can drift out of sync.

---

## Can Templates Be Auto-Generated from Specs?

### YES - High Fidelity Generation Is Possible

#### What Can Be Auto-Generated

| Spec Content | Template Equivalent | Feasibility |
|--------------|---------------------|-------------|
| Required frontmatter fields | Field placeholders | ✅ **Easy** |
| Field types (string, array, etc.) | Placeholder format | ✅ **Easy** |
| Fixed values (`type: vertex/persona`) | Literal values | ✅ **Easy** |
| Required body sections | Section headers | ✅ **Easy** |
| Section format examples | Template examples | ✅ **Medium** |
| Conditional requirements | Conditional placeholders | ⚠️ **Hard** |

#### Example Auto-Generation

**From this spec:**
```markdown
| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/persona` |
| `id` | string | REQUIRED | Format: `v:persona:<name>` |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, persona]` |
```

**Generate this template:**
```markdown
---
type: vertex/persona
extends: doc
id: v:persona:<name>
name: <Persona Name>
tags:
  - vertex
  - doc
  - persona
---
```

**From this spec:**
```markdown
### 2. Role and Identity

**Format:**
\`\`\`markdown
## Role and Identity

[1-2 paragraphs defining who the AI is]
\`\`\`
```

**Generate this template:**
```markdown
## Role and Identity

[1-2 paragraphs defining who the AI is - specific role, professional identity, character]
```

### Extraction Algorithm

```python
def generate_template_from_spec(spec_path: Path) -> str:
    """
    Generate Obsidian template from specification document.

    Extraction rules:
    1. Parse frontmatter requirements table
    2. Extract fixed values (type: vertex/X) → literal
    3. Extract variable values (id: v:X:<name>) → placeholder
    4. Extract required sections from body
    5. Extract format examples from code blocks
    6. Build template structure
    """

    # Parse spec
    spec_content = spec_path.read_text()
    frontmatter_table = extract_table(spec_content, header_pattern="Required Frontmatter")
    body_sections = extract_sections(spec_content, pattern=r"### \d+\. (.+)")

    # Build frontmatter
    template_fm = {}
    for row in frontmatter_table:
        field = row['Field']
        requirement = row['Requirement']
        description = row['Description']

        if 'Must be' in description:
            # Fixed value - extract literal
            value = extract_literal(description)
            template_fm[field] = value
        elif 'Format:' in description or '<' in description:
            # Variable value - create placeholder
            placeholder = create_placeholder(field, description)
            template_fm[field] = placeholder
        elif row['Type'] == 'array[string]':
            # Array - check if fixed or variable
            if 'Must include' in description:
                template_fm[field] = extract_array(description)
            else:
                template_fm[field] = [f'<{field}_item>']

    # Build body
    template_body = []
    for section in body_sections:
        header = section['name']
        format_example = section.get('format_block', '')
        requirements = section.get('requirements', [])

        template_body.append(f"## {header}")
        template_body.append("")

        if format_example:
            # Use format example from spec
            template_body.append(format_example)
        else:
            # Generate placeholder from requirements
            placeholder = generate_placeholder_text(requirements)
            template_body.append(placeholder)

        template_body.append("")

    # Combine
    return format_template(template_fm, template_body)
```

---

## Tradeoffs and Considerations

### Advantages of Auto-Generation

1. **Single Source of Truth**
   - Specs define the type system authoritatively
   - Templates guaranteed to match specs (no drift)
   - Changes to specs automatically propagate to templates

2. **Consistency**
   - All templates follow the same generation rules
   - No manual maintenance errors
   - Easier to update all templates at once

3. **Auditability**
   - Can verify templates are spec-compliant
   - Clear lineage (spec → template)
   - Version control shows intent

4. **Scalability**
   - Adding new document types is easier (write spec → generate template)
   - Less manual work as type system grows

### Disadvantages of Auto-Generation

1. **Loss of Template Nuance**
   - Hand-crafted templates can include helpful hints
   - Generated templates may be more mechanical
   - Less human polish

2. **Spec Format Coupling**
   - Specs must follow strict formatting for parsing
   - Tables must be consistently structured
   - Code blocks must follow patterns
   - Changes to spec format may break generation

3. **Complexity in Edge Cases**
   - Conditional requirements hard to express
   - Optional vs required sections need clear markers
   - Nested structures (dependencies arrays) need special handling

4. **Obsidian-Specific Features**
   - Templates may want Obsidian-specific placeholders ({{date}}, etc.)
   - Templates may include UI hints (<!--- comments --->)
   - Generated templates may not be as Obsidian-native

---

## Recommended Architecture

### Specs as Authority

**Specs are the type system:**
- Define structure, requirements, validation rules
- Written in human-readable markdown with structured tables
- Versioned and assured (self-referential via boundary complex)
- **Authority**: Changes to specs change the type system

**Templates are generated artifacts:**
- Auto-generated from specs via `scripts/generate_templates.py`
- Committed to git for convenience (Obsidian can use them directly)
- Can be regenerated anytime with `python scripts/generate_templates.py`
- **Derivative**: Templates reflect specs, not vice versa

### Workflow

```
1. Edit spec (spec-for-persona.md)
   ↓
2. Run generator: python scripts/generate_templates.py
   ↓
3. Template updated: templates/00_vertices/persona.md
   ↓
4. Commit both spec and generated template
   ↓
5. verify_template_based.py uses template to verify documents
```

### Verification Uses Templates (Not Specs)

**Why?**
- Templates are already in a machine-parseable format
- template_parser.py already exists and works well
- Keeps verification simple and fast
- Specs can remain human-optimized

**Key Insight:**
- **Specs → Templates** (generation)
- **Templates → Verification** (enforcement)
- **Specs are source of truth, templates are compiled form**

---

## Implementation Plan

### Phase 1: Proof of Concept

**Goal**: Demonstrate auto-generation for one document type

**Tasks**:
1. Write `scripts/generate_template_from_spec.py`
2. Parse spec-for-persona.md tables and sections
3. Generate templates/00_vertices/persona.md
4. Compare to hand-crafted version
5. Verify generated template passes verification

**Success Criteria**: Generated template ≥95% matches hand-crafted version

### Phase 2: Full Generator

**Goal**: Generate all templates from all specs

**Tasks**:
1. Extend generator to handle all document types
2. Add support for edges (source/target fields)
3. Add support for faces (vertices/edges arrays)
4. Add support for conditional requirements
5. Add Obsidian-specific enhancements (optional)

**Output**: `python scripts/generate_templates.py` regenerates all templates

### Phase 3: CI Integration

**Goal**: Ensure templates never drift from specs

**Tasks**:
1. Add CI check: templates are up-to-date with specs
2. Fail PR if specs changed but templates not regenerated
3. Optionally: auto-commit generated templates on spec changes

### Phase 4: Documentation

**Goal**: Make the architecture clear

**Tasks**:
1. Document: "Specs are authority, templates are generated"
2. Add regeneration instructions to README
3. Update contributing guide
4. Add comments to templates: "AUTO-GENERATED - DO NOT EDIT"

---

## Alternative: Templates as Authority

**Could we go the other way?** Templates → Specs?

**Answer**: **No, bad idea.**

**Why?**
1. **Templates are implementation-specific** (Obsidian placeholders)
2. **Templates lack semantic validation** ("MUST be specific", "SHOULD use active voice")
3. **Templates are tool-coupled** (Obsidian-specific features)
4. **Specs are documentation** - they explain WHY, not just WHAT
5. **Specs include examples and guidance** beyond structure

**Templates are narrow** (just structure).
**Specs are broad** (structure + semantics + rationale).

Going from narrow → broad is lossy. Going broad → narrow preserves intent.

---

## Conclusion

### Recommendation

**Specs should be the authoritative type system.**
**Templates should be auto-generated from specs.**

**Benefits:**
- Single source of truth (specs)
- No drift between specs and templates
- Easier to maintain type system
- Clear lineage and auditability

**Implementation:**
- Create `generate_templates.py` script
- Add CI check for template freshness
- Document architecture clearly
- Mark templates as auto-generated

**Timeline**:
- Phase 1 POC: 2-3 hours
- Phase 2 Full generator: 4-6 hours
- Phase 3 CI integration: 1-2 hours
- Phase 4 Documentation: 1 hour
- **Total**: 8-12 hours

**This aligns with the philosophy**:
- **Specs define the type system** (prescriptive)
- **Templates support tooling** (Obsidian compatibility)
- **Verification enforces compliance** (template-based checks)

---

**Note**: This analysis supports treating templates as **generated artifacts** rather than primary sources, establishing specs as the canonical definition of the knowledge complex type system.
