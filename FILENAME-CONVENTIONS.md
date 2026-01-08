# Filename Naming Conventions

## Purpose

This document defines filename and directory naming conventions for this repository to ensure cross-platform compatibility and consistency across Windows, macOS, and Linux environments.

## Core Rules

### 1. Cross-Platform Compatibility

All filenames must be compatible with Windows, macOS, and Linux file systems:

- **Allowed characters**: letters (a-z, A-Z), digits (0-9), hyphens (-), underscores (_), dots (.)
- **Forbidden characters**: `< > : " / \ | ? *` (Windows forbidden characters; slashes are path separators, not filename characters)
- **No trailing spaces or dots**: Windows restriction
- **Maximum length**: 255 characters per path component

### 2. Case Consistency Rules

To prevent case collision issues between case-sensitive (Linux/macOS) and case-insensitive (Windows) file systems:

- **Filename (before extension)**: Must be **all lowercase** OR **all uppercase** (not mixed case)
- **Extension (after final dot)**: Must be **lowercase** (e.g., `.md`, `.py`, `.json`)

**Examples:**
- ✅ `spec-for-guidance.md` (lowercase + lowercase extension)
- ✅ `README.md` (uppercase + lowercase extension)
- ✅ `QUICKSTART.md` (uppercase + lowercase extension)
- ❌ `Spec-For-Guidance.md` (mixed case filename)
- ❌ `readme.MD` (uppercase extension)

### 3. Acronym Exceptions

Allowed acronyms may appear in mixed-case form if **properly separated** by:
- Hyphens (`-`) - word separators
- Underscores (`_`) - field separators
- Dots (`.`) - extension separators

An acronym must be:
- At the start of the filename followed by a separator: `GS-root.md`
- At the end preceded by a separator: `couples-GS.md`
- Surrounded by separators: `couples-GS-root.md`

**Current allowed acronyms:** GS, SG, XML, HTML, JSON, CSV, PDF, API, CLI, GUI, SQL, HTTP, HTTPS, URL, URI, UUID, ISO, ANSI, IEEE, INCOSE, SaaS, PaaS, IaaS

To add new acronyms, edit `ALLOWED_ACRONYMS` in [scripts/verify_filenames.py](scripts/verify_filenames.py).

### 4. Human-Readable Naming

For files intended to be human-readable:

- **Words**: Separate with hyphens (`-`)
  - Example: `spec-for-guidance.md`, `test-results.json`

- **Fields**: Separate with underscores (`_`)
  - Example: `validation-persona_spec.md`, `module_01_intro.md`

**Naming pattern**: `field_field-word-word.extension`

### 5. Exempt Directories

Files in the following directories are exempt from validation (external/legacy content):

- `submission/` - External submission materials
- `.venv/`, `venv/`, `env/` - Virtual environments
- `__pycache__/`, `.pytest_cache/` - Generated caches
- `node_modules/`, `dist/`, `build/` - Build artifacts

## Examples

### ✅ Compliant Filenames

```
spec-for-guidance.md              # Human-readable, words with hyphens
validation-persona_spec.md        # Fields separated by underscore
module_01-introduction.md         # Field (module_01) + words
test_results-2024-01.json        # Field + words with date
scripts/verify_template_based.py  # Snake_case for code
```

### ❌ Non-Compliant Filenames

```
Spec-For-Guidance.md             # Uppercase letters
validation:persona.md            # Forbidden character (:)
test results.md                  # Space instead of hyphen
Module-01-Introduction.md        # Uppercase letters
finalReport.md                   # CamelCase not allowed
```

## Validation

### Automated Validation Script

Use the verification script to check filename compliance:

```bash
# Check all git-tracked files
python scripts/verify_filenames.py

# Check all files (including untracked)
python scripts/verify_filenames.py --all

# Check a single file
python scripts/verify_filenames.py --file path/to/file.md
```

### Pre-commit Hook (Optional)

To automatically verify filenames before commits, add to `.git/hooks/pre-commit`:

```bash
#!/bin/sh
python scripts/verify_filenames.py
if [ $? -ne 0 ]; then
    echo "❌ Filename verification failed. Please fix violations before committing."
    exit 1
fi
```

## Rationale

### Why Lowercase?

1. **Case-sensitive vs case-insensitive file systems**: macOS/Linux are case-sensitive by default, Windows is case-insensitive. Lowercase avoids `file.md` vs `File.md` conflicts.
2. **URL-friendly**: Lowercase filenames work better in web contexts
3. **Shell-friendly**: No need to escape or quote filenames

### Why Hyphens for Words?

1. **Readability**: `test-results` is more readable than `testresults` or `test_results`
2. **SEO-friendly**: Hyphens are treated as word separators by search engines
3. **Conventional**: Common in web URLs and modern documentation

### Why Underscores for Fields?

1. **Distinction**: Clearly separates structural fields from descriptive words
2. **Sorting**: Files with field prefixes group together (e.g., `module_01_*`, `module_02_*`)
3. **Parsing**: Easier to programmatically extract field identifiers

## Migration

For existing files that don't comply:

1. **Identify violations**: Run `python scripts/verify_filenames.py`
2. **Rename files**: Use `git mv old-name new-name` to preserve history
3. **Update references**: Search for and update any links/imports to renamed files
4. **Test thoroughly**: Ensure scripts, documentation links, and imports still work

## Questions or Exceptions?

If you need an exception to these rules or have questions about naming a specific file, please open an issue for discussion.
