# Specs vs Templates: Why We Have Both

This document explains the relationship between specification documents (`00_vertices/spec-for-*.md`) and templates (`templates/`), and why both exist in the knowledge complex.

---

## The Short Answer

**Specs are the authoritative source of truth. Templates are derived artifacts that serve two purposes:**

1. **Automated verification** — The verification scripts parse templates to extract structural requirements
2. **Obsidian compatibility** — Obsidian's Templater plugin uses templates to create new documents

Templates are *generated from* specs, not the other way around.

---

## The Spec → Template Pipeline

```
spec-for-spec.md          →  templates/00_vertices/spec.md
spec-for-guidance.md      →  templates/00_vertices/guidance.md
spec-for-charts.md        →  templates/charts/chart.md
...
```

The script `scripts/generate_all_templates.py` extracts the structural requirements from specs and produces templates in a format that both:
- The verification toolchain can parse programmatically
- Obsidian's Templater can use to scaffold new documents

---

## Why Not Just Use Specs Directly?

### 1. Verification Tooling Needs Parseable Structure

Specs are written for humans. They contain:
- Explanatory prose
- Examples and edge cases
- Rationale for design decisions
- References to other specs

The verification script needs a clean, machine-parseable definition of:
- Required YAML frontmatter fields
- Expected field types
- Required markdown sections

Templates provide this stripped-down, parseable format.

### 2. Obsidian Templater Integration

Obsidian's Templater plugin inserts template content directly into new files. When you create a new spec document in Obsidian:

1. Templater reads `templates/00_vertices/spec.md`
2. Inserts the YAML frontmatter skeleton with placeholder values
3. Inserts the required section headers

This provides a scaffold that ensures new documents start with correct structure.

### 3. Separation of Concerns

| Artifact | Purpose | Audience |
|----------|---------|----------|
| Spec | Define requirements, explain rationale | Humans writing/reviewing documents |
| Template | Provide structural skeleton | Tools (verification scripts, Obsidian) |

Specs are documentation. Templates are tooling artifacts.

---

## Keeping Them in Sync

Templates must stay synchronized with their source specs. The generation script includes a check mode:

```bash
# Check if templates are stale
python scripts/generate_all_templates.py --check

# Regenerate all templates
python scripts/generate_all_templates.py
```

If you modify a spec's structural requirements, regenerate its template.

---

## The Verification Flow

When you run verification:

```bash
python scripts/verify_template_based.py 00_vertices/my-doc.md --templates templates
```

The verifier:
1. Reads `my-doc.md` and extracts its `type` field (e.g., `vertex/spec`)
2. Loads the corresponding template (`templates/00_vertices/spec.md`)
3. Parses the template to extract required fields and sections
4. Checks that `my-doc.md` satisfies all template requirements
5. Reports pass/fail with specific check results

The spec (`spec-for-spec.md`) is the authoritative definition. The template is the verification interface.

---

## Summary

| Question | Answer |
|----------|--------|
| Which is authoritative? | Specs |
| Which is derived? | Templates |
| Why not just specs? | Tooling needs parseable format |
| Why not just templates? | Humans need explanations and rationale |
| How to keep in sync? | `generate_all_templates.py` |

Both exist because they serve different audiences: specs for humans, templates for tools.
