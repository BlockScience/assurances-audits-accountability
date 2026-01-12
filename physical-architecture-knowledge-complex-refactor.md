---
type: vertex/doc
extends: doc
id: v:doc:physical-architecture-knowledge-complex-refactor
name: Physical Architecture - Knowledge Complex Framework Refactor
description: Physical elements, technology choices, and element-component matrix for the knowledge complex framework refactor
tags:
  - vertex
  - doc
  - physical-architecture
version: 0.1.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-11T00:00:00Z
system_name: Knowledge Complex Framework
scope: Internal-first deployment using file-based storage with git version control and Python tooling
logical_architecture_ref: v:doc:logical-architecture-knowledge-complex-refactor
element_count: 16
---

# Physical Architecture - Knowledge Complex Framework Refactor

## Purpose

This physical architecture defines the specific technology choices that implement the 14 logical components of the knowledge complex framework. The document specifies 16 physical elements using Python libraries, file formats, and tool integrations appropriate for BlockScience's internal-first deployment, where markdown documents with YAML frontmatter are stored in git repositories and accessed through VS Code, Claude Code, and Obsidian.

## Overview

The logical architecture established 14 technology-agnostic components organized into 6 areas: Type System (C1-C2), Document Management (C3-C5), Coherence Verification (C6-C8), Quality Assessment (C9-C10), Knowledge Graph (C11-C12), and Workflow & Accountability (C13-C14). This physical architecture translates those components into concrete technologies.

The key architectural decisions reflect the constraints from the conceptual architecture:

1. **File-based storage over database**: Documents remain human-readable markdown files in git repositories (constraint C1, C2)
2. **Python ecosystem**: Leverage Python for all programmatic tooling, consistent with BlockScience's technical stack
3. **Git as truth**: All simplices (vertices, edges, faces) stored as markdown files version-controlled in git (constraint C2)
4. **Human-in-the-loop**: Validation edges require explicit human approval captured in YAML frontmatter (constraint C3)
5. **Familiar interfaces**: VS Code for authoring, Obsidian for navigation, Claude Code for AI assistance (field survey resources R12-R14)

The Element-Component Matrix shows how 16 physical elements combine to implement all 14 logical components, completing the traceability chain from stakeholder needs through functions and components to concrete implementation.

## Logical Architecture Reference

[[logical-architecture-knowledge-complex-refactor]]

### Components Summary

| ID | Name | Responsibility |
|----|------|----------------|
| C1 | Type Ontology | Define and manage simplex type hierarchy, inheritance rules, and local rules |
| C2 | Schema Registry | Store schemas for each type defining required YAML fields and inheritance chains |
| C3 | Template Registry | Store and retrieve document templates by type, linked to schemas |
| C4 | Document Composer | Assemble documents from templates and parameters ensuring type compliance |
| C5 | Simplex Store | Persist and retrieve typed simplices with coherence enforcement |
| C6 | Schema Verifier | Verify YAML frontmatter against type schemas |
| C7 | Structure Analyzer | Verify markdown body structure against spec-defined sections |
| C8 | Boundary Verifier | Verify simplicial complex rules and local rules |
| C9 | Evaluation Engine | Score documents against guidance criteria |
| C10 | Result Presenter | Format verification and evaluation results for display |
| C11 | Search Index | Support full-text and filtered search across typed simplices |
| C12 | Graph Navigator | Traverse typed relationships and discover backlinks |
| C13 | Workflow Coordinator | Manage approval requests and runbook execution |
| C14 | Simplex Constructor | Create typed edges and faces ensuring coherence |

## Physical Architecture

### Element Table

| ID  | Name                    | Technology/Tool      | Version                   | Purpose                                                            |
| --- | ----------------------- | -------------------- | ------------------------- | ------------------------------------------------------------------ |
| E1  | Ontology Files          | Markdown + YAML      | CommonMark 0.30+          | Store type definitions as human-readable ontology documents        |
| E2  | Schema Files            | JSON Schema          | Draft 2020-12             | Machine-readable schemas for frontmatter validation                |
| E3  | Template Files          | Markdown + Jinja2    | Jinja2 3.1+               | Parameterized templates with placeholder syntax                    |
| E4  | Python Package          | Python               | 3.11+                     | Core library implementing all programmatic components              |
| E5  | Document Files          | Markdown + YAML      | CommonMark 0.30+          | All simplices stored as markdown with YAML frontmatter             |
| E6  | Git Repository          | Git                  | 2.40+                     | Version control, branching, and commit-based accountability        |
| E7  | YAML Parser             | PyYAML + ruamel.yaml | PyYAML 6.0+, ruamel 0.18+ | Parse and emit YAML frontmatter with comment preservation          |
| E8  | Markdown Parser         | markdown-it-py       | 3.0+                      | Parse markdown structure for section analysis                      |
| E9  | JSON Schema Validator   | jsonschema           | 4.20+                     | Validate frontmatter against JSON Schema definitions               |
| E10 | Graph Data Structure    | NetworkX             | 3.2+                      | In-memory graph for relationship traversal and topological queries |
| E11 | Full-Text Search        | Whoosh               | 2.7+                      | File-based search index for content discovery                      |
| E12 | CLI Framework           | Click                | 8.1+                      | Command-line interface for all operations                          |
| E13 | VS Code Extension       | TypeScript           | 5.0+                      | IDE integration for authoring and verification                     |
| E14 | Obsidian Vault          | Obsidian             | 1.5+                      | Knowledge navigation and review interface                          |
| E15 | Claude Code Integration | Claude Code          | Latest                    | LLM-assisted authoring with system prompt configuration            |
| E16 | Result Formatter        | Rich                 | 13.0+                     | Terminal output formatting for verification and evaluation results |

### Element Definitions

#### E1: Ontology Files

**Technology:** Markdown files with YAML frontmatter (CommonMark specification)
**Version:** CommonMark 0.30+

**Purpose:** Store type ontology definitions as human-readable documents that can be version-controlled and reviewed like any other knowledge complex artifact.

**Rationale:** The ontology is itself a knowledge complex artifact—it should be stored in the same format as the documents it governs. This enables self-demonstration (AC9) where the framework's own documents pass verification. Markdown with YAML frontmatter is human-readable (constraint C1) and git-friendly (constraint C2).

**Configuration:**
- Location: Repository root or `00_vertices/` directory
- Naming: `ontology-<name>.md`
- Required frontmatter: `type: vertex/ontology`, `extends: doc`
- Body structure: Vertex Types, Edge Types, Face Types, Chart Types, Local Rules sections

#### E2: Schema Files

**Technology:** JSON Schema
**Version:** Draft 2020-12

**Purpose:** Machine-readable schema definitions that can be used for automated frontmatter validation.

**Rationale:** JSON Schema is the industry standard for validating structured data. It provides formal definitions that complement the human-readable specs. Using JSON Schema 2020-12 provides `$ref` for schema composition, `prefixItems` for tuple validation, and `dependentRequired` for conditional fields.

**Configuration:**
- Location: `schemas/` directory
- Naming: `<type-name>.schema.json`
- Base schema: `vertex.schema.json` with type-specific extensions
- Composition: Use `$ref` to inherit from parent type schemas

#### E3: Template Files

**Technology:** Markdown with Jinja2 template syntax
**Version:** Jinja2 3.1+

**Purpose:** Parameterized templates for document creation with placeholder syntax for context injection.

**Rationale:** Jinja2 is Python's standard templating engine with clear placeholder syntax (`{{ variable }}`), conditionals (`{% if %}`), and loops. Templates remain readable markdown when placeholders are unfilled. Jinja2 integrates naturally with the Python package (E4).

**Configuration:**
- Location: `templates/` directory
- Naming: `template-<type-name>.md`
- Placeholders: `{{ system_name }}`, `{{ created_date }}`, `{{ id }}`
- Required sections: Must match spec-defined required sections

#### E4: Python Package

**Technology:** Python package (pip-installable)
**Version:** Python 3.11+

**Purpose:** Core library implementing all programmatic logic for verification, validation, graph operations, and workflow management.

**Rationale:** Python is BlockScience's primary language for analytical work. Python 3.11+ provides significant performance improvements, better error messages, and tomllib for TOML configuration. A pip-installable package enables reuse across projects and aligns with the public registry vision (resource R10).

**Configuration:**
- Package name: `knowledge-complex` (PyPI) or `kcomplex` (import name)
- Entry points: CLI via `kc` command
- Dependencies: See E7-E12 for required libraries
- Structure: `src/kcomplex/` layout with submodules for each component area

#### E5: Document Files

**Technology:** Markdown files with YAML frontmatter
**Version:** CommonMark 0.30+

**Purpose:** All simplices (vertices, edges, faces) stored as human-readable markdown files that can be authored, reviewed, and version-controlled.

**Rationale:** Human-readable markdown is required by constraint C1. YAML frontmatter provides structured metadata while keeping the body human-readable. This format integrates with VS Code, Obsidian, and standard markdown tooling.

**Configuration:**
- Vertices: `00_vertices/` or repository root
- Edges: `01_edges/` directory
- Faces: `02_faces/` directory
- Charts: `03_charts/` directory
- File extension: `.md`
- Frontmatter delimiter: `---`

#### E6: Git Repository

**Technology:** Git distributed version control
**Version:** Git 2.40+

**Purpose:** Version control, branching for approval workflows, and commit-based accountability for all changes.

**Rationale:** Git is required by constraint C2 as the source of truth. Git 2.40+ provides improved performance for large repositories, better merge conflict resolution, and `safe.directory` improvements. Commit hashes provide immutable references for accountability edges.

**Configuration:**
- `.gitignore`: Exclude caches, search indices, temporary files
- Branch strategy: `main` for assured documents, feature branches for drafts
- Hooks: Pre-commit for verification, post-merge for index updates
- Signature: Use `git commit -S` for GPG-signed commits when available

#### E7: YAML Parser

**Technology:** PyYAML + ruamel.yaml
**Version:** PyYAML 6.0+, ruamel.yaml 0.18+

**Purpose:** Parse YAML frontmatter for schema validation and emit YAML for document generation with comment preservation.

**Rationale:** PyYAML is fast for parsing; ruamel.yaml preserves comments and formatting when modifying frontmatter. Using both provides optimal read performance with high-fidelity write operations. Comment preservation is important for documents with inline documentation.

**Configuration:**
- Reading: PyYAML `safe_load()` for security
- Writing: ruamel.yaml `YAML(typ='rt')` for round-trip
- Frontmatter extraction: Split on `---` delimiters

#### E8: Markdown Parser

**Technology:** markdown-it-py
**Version:** 3.0+

**Purpose:** Parse markdown structure for section analysis, heading extraction, and body structure verification.

**Rationale:** markdown-it-py is a Python port of the standard markdown-it parser with full CommonMark compliance. It provides a token-based AST that enables programmatic analysis of document structure (heading levels, section nesting, table parsing). It's actively maintained and extensible.

**Configuration:**
- Extensions: tables, footnotes (if used)
- Parsing mode: CommonMark strict
- Output: Token stream for structure analysis (not HTML rendering)

#### E9: JSON Schema Validator

**Technology:** jsonschema library
**Version:** 4.20+

**Purpose:** Validate YAML frontmatter against JSON Schema definitions for automated schema verification.

**Rationale:** jsonschema is the reference implementation for JSON Schema in Python. Version 4.20+ supports Draft 2020-12 with `format_nongpl` validators for format checking without GPL dependencies. The library provides detailed error messages for validation failures.

**Configuration:**
- Draft version: 2020-12
- Format validation: Enabled for datetime, uri-reference
- Error handling: Collect all errors (not fail-fast) for complete reporting

#### E10: Graph Data Structure

**Technology:** NetworkX
**Version:** 3.2+

**Purpose:** In-memory graph representation for relationship traversal, backlink discovery, and topological analysis.

**Rationale:** NetworkX is Python's standard graph library with extensive algorithms for path finding, cycle detection (DAG verification), and subgraph operations. Version 3.2+ provides improved performance and better typing support. The graph is built from document files at startup and updated on changes.

**Configuration:**
- Graph type: `nx.MultiDiGraph` (directed edges with multiple edge types)
- Node attributes: Vertex type, file path, frontmatter metadata
- Edge attributes: Edge type, source, target, file path
- Neighborhood queries: `G.predecessors()`, `G.successors()`, `G.neighbors()`

#### E11: Full-Text Search

**Technology:** Whoosh
**Version:** 2.7+

**Purpose:** File-based search index for full-text content discovery across the knowledge complex.

**Rationale:** Whoosh is a pure-Python search library that stores indices as files—no external services required. This aligns with the file-based architecture and git-friendly approach. It supports fielded search (type, tags, content) and relevance ranking. For larger deployments, this could be upgraded to Elasticsearch/OpenSearch.

**Configuration:**
- Index location: `.whoosh_index/` directory (gitignored)
- Schema: id, type, name, tags, content, path
- Analyzers: Stemming for content, keyword for type/tags
- Update strategy: Incremental on file change, full rebuild on request

#### E12: CLI Framework

**Technology:** Click
**Version:** 8.1+

**Purpose:** Command-line interface for all knowledge complex operations—verification, validation, graph queries, and workflow management.

**Rationale:** Click is the standard Python CLI framework with automatic help generation, argument validation, and composable command groups. It integrates well with Rich (E16) for formatted output. Click's decorator-based API enables rapid development of CLI commands.

**Configuration:**
- Entry point: `kc` command
- Command groups: `kc verify`, `kc validate`, `kc graph`, `kc workflow`
- Global options: `--repo`, `--verbose`, `--format`
- Output formats: text (default), json, markdown

#### E13: VS Code Extension

**Technology:** VS Code Extension API (TypeScript)
**Version:** TypeScript 5.0+, VS Code Extension API 1.85+

**Purpose:** IDE integration for real-time verification feedback, template insertion, and knowledge complex navigation.

**Rationale:** VS Code is BlockScience's standard IDE (assumption A2 from conceptual architecture). The extension provides integration with the Python tooling via subprocess calls or Language Server Protocol. TypeScript is required for VS Code extensions.

**Configuration:**
- Extension ID: `blockscience.knowledge-complex`
- Activation: On `.md` file open in knowledge complex repository
- Features: Frontmatter validation on save, template snippets, graph view panel
- Communication: Calls Python CLI (E12) for verification operations

#### E14: Obsidian Vault

**Technology:** Obsidian knowledge base application
**Version:** Obsidian 1.5+

**Purpose:** Knowledge navigation, graph visualization, backlink discovery, and document review interface.

**Rationale:** Obsidian is specified as the knowledge explorer interface (resource R14, assumption A4). It provides native support for markdown with YAML frontmatter, wikilink navigation (`[[doc-name]]`), and graph visualization. The vault is simply the git repository—no separate data store.

**Configuration:**
- Vault: Point Obsidian at the git repository root
- Plugins: Dataview (for queries), Graph Analysis (for visualization)
- Templates: Configure Obsidian to use `templates/` directory
- Settings: Enable YAML frontmatter parsing, wikilink auto-completion

#### E15: Claude Code Integration

**Technology:** Claude Code (Anthropic CLI assistant)
**Version:** Latest

**Purpose:** LLM-assisted authoring with knowledge complex awareness, template filling, and guided workflow execution.

**Rationale:** Claude Code is specified as the LLM facilitator (resource R13, assumption A3). It provides AI assistance within the terminal/IDE context. The integration consists primarily of a system prompt (`.claude/CLAUDE.md`) that teaches Claude about knowledge complex conventions.

**Configuration:**
- System prompt: Repository's `.claude/CLAUDE.md` file
- Context: Current working directory provides repository context
- Capabilities: Template retrieval, prior work discovery, draft generation, verification interpretation
- Constraints: Human approval required—Claude prepares but doesn't approve

#### E16: Result Formatter

**Technology:** Rich terminal formatting library
**Version:** Rich 13.0+

**Purpose:** Format verification results, evaluation scores, and workflow status for readable terminal output.

**Rationale:** Rich provides cross-platform terminal formatting with tables, syntax highlighting, progress bars, and panels. It integrates with Click (E12) for consistent CLI output. Rich renders markdown for displaying document excerpts.

**Configuration:**
- Theme: Default or custom knowledge complex theme
- Tables: For verification results, matrix views
- Panels: For evaluation summaries with criteria scores
- Markdown: For document previews and help text

### Deployment View

The knowledge complex framework deploys as a file-based system with no external services required for basic operation.

#### Deployment Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          User Workstation                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐                │
│  │   VS Code    │   │   Obsidian   │   │  Claude Code │                │
│  │    (E13)     │   │    (E14)     │   │    (E15)     │                │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘                │
│         │                  │                  │                          │
│         └─────────────────┼──────────────────┘                          │
│                           │                                              │
│                           ▼                                              │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │                    Python Package (E4)                          │     │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │     │
│  │  │  CLI    │ │  YAML   │ │Markdown │ │  JSON   │ │ Search  │  │     │
│  │  │  (E12)  │ │ Parser  │ │ Parser  │ │ Schema  │ │ Index   │  │     │
│  │  │         │ │  (E7)   │ │  (E8)   │ │  (E9)   │ │ (E11)   │  │     │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘  │     │
│  │  ┌─────────┐ ┌─────────────────────────────────┐              │     │
│  │  │  Rich   │ │         NetworkX (E10)          │              │     │
│  │  │  (E16)  │ │       In-Memory Graph           │              │     │
│  │  └─────────┘ └─────────────────────────────────┘              │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                           │                                              │
│                           ▼                                              │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │                    Git Repository (E6)                          │     │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │     │
│  │  │  Ontology   │ │   Schema    │ │  Template   │               │     │
│  │  │  Files (E1) │ │  Files (E2) │ │  Files (E3) │               │     │
│  │  └─────────────┘ └─────────────┘ └─────────────┘               │     │
│  │  ┌───────────────────────────────────────────────────────┐    │     │
│  │  │               Document Files (E5)                      │    │     │
│  │  │  00_vertices/  │  01_edges/  │  02_faces/  │ 03_charts/ │    │     │
│  │  └───────────────────────────────────────────────────────┘    │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Environment Configuration

| Environment | Configuration Notes |
|-------------|---------------------|
| Development | Full toolchain: VS Code, Obsidian, Claude Code, Python package installed in editable mode (`pip install -e .`). Search index in `.whoosh_index/` (gitignored). Pre-commit hooks enabled. |
| Production | Same as development for internal-first deployment. No separate production environment—users work directly with git repositories. For future client deployments, may add CI/CD verification gates. |

## Element-Component Matrix

### Matrix View

|      | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 |
|------|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|
| E1   | X  |    |    |    |    |    |    |    |    |    |     |     |     |     |
| E2   |    | X  |    |    |    |    |    |    |    |    |     |     |     |     |
| E3   |    |    | X  |    |    |    |    |    |    |    |     |     |     |     |
| E4   | S  | S  | S  | X  | S  | S  | S  | S  | X  | S  | S   | S   | X   | X   |
| E5   |    |    |    |    | X  |    |    |    |    |    |     |     |     |     |
| E6   |    |    |    |    | X  |    |    |    |    |    |     |     | X   |     |
| E7   |    |    |    | X  |    | X  |    |    |    |    |     |     |     | X   |
| E8   |    |    |    |    |    |    | X  |    |    |    |     |     |     |     |
| E9   |    | X  |    |    |    | X  |    |    |    |    |     |     |     |     |
| E10  |    |    |    |    |    |    |    | X  |    |    |     | X   |     |     |
| E11  |    |    |    |    |    |    |    |    |    |    | X   |     |     |     |
| E12  | S  | S  | S  | S  | S  | S  | S  | S  | S  | S  | S   | S   | S   | S   |
| E13  |    |    | X  | X  |    | X  | X  |    |    | X  |     |     |     |     |
| E14  |    |    |    |    |    |    |    |    |    |    | X   | X   |     |     |
| E15  |    |    |    | X  |    |    |    |    | X  |    | X   |     | X   |     |
| E16  |    |    |    |    |    |    |    |    |    | X  |     |     |     |     |

**Legend:** X = Primary Implementation, S = Supporting (infrastructure)

### Relationship Details

| Element | Component | Implementation Type | Rationale |
|---------|-----------|---------------------|-----------|
| E1 | C1 | Full Implementation | Ontology files ARE the Type Ontology—definitions stored as markdown documents |
| E2 | C2 | Full Implementation | JSON Schema files ARE the Schema Registry—schemas stored as files |
| E3 | C3 | Full Implementation | Template files ARE the Template Registry—templates stored as markdown |
| E4 | C1 | Shared Implementation | Python package provides programmatic access to ontology definitions |
| E4 | C2 | Shared Implementation | Python package loads and queries schema files |
| E4 | C3 | Shared Implementation | Python package retrieves templates for composition |
| E4 | C4 | Full Implementation | Python package implements template instantiation and parameter injection |
| E4 | C5 | Shared Implementation | Python package implements coherence enforcement on file operations |
| E4 | C6-C8 | Shared Implementation | Python package orchestrates verification using E7, E8, E9, E10 |
| E4 | C9 | Full Implementation | Python package implements guidance-based evaluation logic |
| E4 | C10 | Shared Implementation | Python package formats results using E16 |
| E4 | C11-C12 | Shared Implementation | Python package provides search and graph APIs using E10, E11 |
| E4 | C13 | Full Implementation | Python package implements workflow coordination logic |
| E4 | C14 | Full Implementation | Python package implements simplex construction with coherence checks |
| E5 | C5 | Full Implementation | Document files ARE the Simplex Store—persistence as markdown files |
| E6 | C5 | Shared Implementation | Git provides version control and accountability for stored simplices |
| E6 | C13 | Shared Implementation | Git commits provide accountability timestamps for workflow events |
| E7 | C4 | Partial Implementation | YAML parser enables parameter extraction and frontmatter manipulation |
| E7 | C6 | Partial Implementation | YAML parser extracts frontmatter for schema verification |
| E7 | C14 | Partial Implementation | YAML parser generates frontmatter for constructed simplices |
| E8 | C7 | Full Implementation | Markdown parser analyzes document structure for section verification |
| E9 | C2 | Partial Implementation | JSON Schema validator uses schema files for validation |
| E9 | C6 | Partial Implementation | JSON Schema validator performs frontmatter validation |
| E10 | C8 | Full Implementation | NetworkX provides graph queries for boundary and local rule verification |
| E10 | C12 | Full Implementation | NetworkX provides relationship traversal and backlink discovery |
| E11 | C11 | Full Implementation | Whoosh provides full-text search across document content |
| E12 | All | Shared Implementation | CLI provides user interface to all component operations |
| E13 | C3 | Partial Implementation | VS Code extension provides template insertion snippets |
| E13 | C4 | Partial Implementation | VS Code extension triggers document composition |
| E13 | C6-C7 | Partial Implementation | VS Code extension displays verification results inline |
| E13 | C10 | Partial Implementation | VS Code extension presents formatted results in panels |
| E14 | C11 | Partial Implementation | Obsidian provides search UI for content discovery |
| E14 | C12 | Partial Implementation | Obsidian provides graph navigation and backlink panels |
| E15 | C4 | Partial Implementation | Claude Code assists with template filling and draft generation |
| E15 | C9 | Partial Implementation | Claude Code helps interpret evaluation results and suggest improvements |
| E15 | C11 | Partial Implementation | Claude Code uses search to find prior work |
| E15 | C13 | Partial Implementation | Claude Code guides operators through runbook steps |
| E16 | C10 | Full Implementation | Rich formats terminal output for verification and evaluation results |

### Key Implementations

1. **File-Based Storage (E1, E2, E3, E5, E6)**: The simplicial complex is stored entirely as files in a git repository. Ontologies, schemas, templates, and all simplices (vertices, edges, faces) are markdown files with YAML frontmatter. This implements C1 (Type Ontology), C2 (Schema Registry), C3 (Template Registry), and C5 (Simplex Store) without any database dependencies. Git (E6) provides version control, branching, and commit-based accountability.

2. **Python Package as Orchestrator (E4)**: The Python package implements the core logic for all components, using specialized libraries (E7-E11) for parsing, validation, and graph operations. It provides both a programmatic API and CLI (E12) for all operations. This is the "core" package referenced in the field survey (resource R1).

3. **Multi-Parser Verification (E7, E8, E9, E10)**: Verification uses specialized parsers for each concern: PyYAML/ruamel for YAML frontmatter (C6), markdown-it-py for body structure (C7), jsonschema for schema validation (C6), and NetworkX for graph-based coherence (C8). This separation of concerns enables focused testing and extensibility.

4. **Triple Interface Strategy (E13, E14, E15)**: Three complementary interfaces serve different user needs: VS Code (E13) for authoring with real-time feedback, Obsidian (E14) for navigation and review, and Claude Code (E15) for AI-assisted workflows. All three operate on the same git repository—no synchronization needed.

5. **Search and Graph Navigation (E10, E11, E14)**: Discovery combines full-text search (Whoosh/E11) with graph traversal (NetworkX/E10), exposed through Obsidian's native features (E14) and the Python API. This implements C11 (Search Index) and C12 (Graph Navigator).

6. **Evaluation Engine (E4, E15)**: The evaluation engine (C9) is implemented in Python (E4) with guidance-parsing logic, while Claude Code (E15) provides AI-assisted interpretation and improvement suggestions. This hybrid approach combines deterministic scoring with contextual guidance.

## Unit Testing Strategy

### Test Approach by Element

| Element | Test Framework | Test Method | Success Indicator |
|---------|----------------|-------------|-------------------|
| E1 | pytest | Parse ontology files, verify structure | All ontology files parse correctly, counts match |
| E2 | pytest + jsonschema | Validate test documents against schemas | Valid docs pass, invalid docs fail with correct errors |
| E3 | pytest + jinja2 | Render templates with test parameters | Rendered output matches expected structure |
| E4 | pytest + coverage | Unit tests for each module, integration tests for workflows | >90% coverage, all integration scenarios pass |
| E5 | pytest | Read/write document files, verify roundtrip fidelity | Content preserved exactly through read/write cycle |
| E6 | pytest + git | Commit operations, branch workflows, signature verification | Git operations succeed, hooks execute correctly |
| E7 | pytest | Parse test YAML files, verify roundtrip with comments | Comments preserved, Unicode handled correctly |
| E8 | pytest | Parse test markdown files, extract section structure | Section hierarchy matches expected structure |
| E9 | pytest + jsonschema | Validate frontmatter against schemas with edge cases | All validation rules enforced correctly |
| E10 | pytest + networkx | Graph construction, traversal, cycle detection | Graph algorithms return correct results |
| E11 | pytest + whoosh | Index documents, execute searches, verify relevance | Search returns expected results in correct order |
| E12 | pytest + click.testing | Invoke CLI commands, verify output and exit codes | Commands execute successfully, output formatted correctly |
| E13 | VS Code Extension Tests | Extension activation, command execution, UI updates | Extension functions correctly in VS Code environment |
| E14 | Manual Testing | Vault configuration, plugin functionality, navigation | Obsidian displays and navigates correctly |
| E15 | Integration Testing | Claude Code interactions with test repository | AI assistance produces valid outputs |
| E16 | pytest + rich | Format test results, verify terminal output | Output renders correctly across terminal types |

## Traceability to Logical Architecture

### From Components to Elements

| Component | Implemented by Elements | Implementation Notes |
|-----------|------------------------|----------------------|
| C1 Type Ontology | E1, E4 | Ontology files (E1) ARE the storage; Python (E4) provides access |
| C2 Schema Registry | E2, E4, E9 | Schema files (E2) ARE the storage; Python uses jsonschema (E9) |
| C3 Template Registry | E3, E4, E13 | Template files (E3) ARE the storage; Python and VS Code provide access |
| C4 Document Composer | E4, E7, E13, E15 | Python (E4) orchestrates; YAML parser (E7), VS Code (E13), Claude (E15) assist |
| C5 Simplex Store | E5, E6, E4 | Document files (E5) ARE the storage; Git (E6) provides version control |
| C6 Schema Verifier | E4, E7, E9, E13 | Python orchestrates; YAML parser (E7), jsonschema (E9); VS Code displays |
| C7 Structure Analyzer | E4, E8, E13 | Python orchestrates; markdown parser (E8) analyzes; VS Code displays |
| C8 Boundary Verifier | E4, E10 | Python orchestrates; NetworkX (E10) provides graph queries |
| C9 Evaluation Engine | E4, E15 | Python (E4) implements scoring; Claude Code (E15) assists interpretation |
| C10 Result Presenter | E4, E16, E13 | Python orchestrates; Rich (E16) formats terminal; VS Code formats IDE |
| C11 Search Index | E11, E4, E14, E15 | Whoosh (E11) indexes; Python provides API; Obsidian and Claude search |
| C12 Graph Navigator | E10, E4, E14 | NetworkX (E10) stores graph; Python provides API; Obsidian visualizes |
| C13 Workflow Coordinator | E4, E6, E15 | Python (E4) implements logic; Git (E6) provides accountability; Claude guides |
| C14 Simplex Constructor | E4, E7 | Python (E4) implements construction; YAML parser (E7) generates frontmatter |

### Coverage Analysis

- **Complete coverage**: All 14 logical components are implemented by at least one physical element
- **File-based foundation**: E1, E2, E3, E5, E6 provide file-based storage for all data (no external services)
- **Python as hub**: E4 touches all components, providing the programmatic core that orchestrates all operations
- **Specialized parsers**: E7, E8, E9, E10 handle specific parsing/validation concerns
- **Multi-interface access**: E13, E14, E15 provide three complementary user interfaces
- **CLI and formatting**: E12, E16 provide command-line access with formatted output

## Technology Selection Rationale

### Selection Criteria

Technology choices were guided by:

1. **File-based over database**: Constraints C1 and C2 require human-readable files in git
2. **Python ecosystem**: BlockScience's primary language for analytical work
3. **Existing toolchain**: VS Code, Obsidian, Claude Code specified in field survey
4. **No external services**: Internal deployment should not require databases or cloud services
5. **Maintainability**: Standard libraries preferred over custom implementations
6. **Future extensibility**: Upgrade path to more scalable solutions if needed

### Alternatives Considered

| Element | Technology Chosen | Alternatives Considered | Why Chosen |
|---------|-------------------|------------------------|------------|
| E5 | Markdown files | SQLite, PostgreSQL | Constraint C1 requires human-readable; git-friendly |
| E7 | PyYAML + ruamel.yaml | strictyaml, pyyaml-safe | Best balance of speed (PyYAML) and fidelity (ruamel) |
| E8 | markdown-it-py | mistune, commonmark | Most complete CommonMark implementation in Python |
| E10 | NetworkX | igraph, graph-tool | Pure Python, sufficient for expected graph sizes |
| E11 | Whoosh | SQLite FTS, Elasticsearch | Pure Python, file-based, no external service |
| E12 | Click | argparse, typer | Mature, well-documented, Click is standard for Python CLIs |
| E16 | Rich | colorama, blessed | Best terminal formatting with markdown support |

## Constraints and Assumptions

### Constraints

- **Cst1**: All simplices stored as markdown files with YAML frontmatter (from conceptual C1)
- **Cst2**: Git is the sole version control system; no alternative persistence (from conceptual C2)
- **Cst3**: Validation requires human signature; cannot be fully automated (from conceptual C3)
- **Cst4**: Python 3.11+ required for performance and language features
- **Cst5**: File-based search may not scale beyond ~10,000 documents; upgrade path to Elasticsearch if needed
- **Cst6**: VS Code extension requires TypeScript; separate build from Python package

### Assumptions

- **Asm1**: Users have Python 3.11+ installed or can install it
- **Asm2**: Users have VS Code 1.85+ installed and are willing to use extensions
- **Asm3**: Users have Obsidian 1.5+ installed or can install it
- **Asm4**: Users have access to Claude Code for LLM assistance
- **Asm5**: Git 2.40+ is available on user workstations
- **Asm6**: Repository sizes will remain manageable (<10,000 documents) for file-based search

---

**Note:** This physical architecture is the fourth and final extended architecture document. It completes the chain: Conceptual Architecture (stakeholder needs, acceptance criteria) → Functional Architecture (24 functions) → Logical Architecture (14 components, 40 interfaces) → Physical Architecture (16 elements implementing the components). The next step is the summary Architecture document that consolidates key decisions.