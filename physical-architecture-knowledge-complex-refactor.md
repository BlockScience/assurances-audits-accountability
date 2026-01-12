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
version: 0.2.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-12T00:00:00Z
system_name: Knowledge Complex Framework
scope: Internal-first deployment using file-based storage with git version control and Python tooling
logical_architecture_ref: v:doc:logical-architecture-knowledge-complex-refactor
element_count: 12
---

# Physical Architecture - Knowledge Complex Framework Refactor

## Purpose

This physical architecture defines the specific technology choices that implement the 14 logical components of the knowledge complex framework. The document specifies 12 physical elements using a minimal, coherent toolchain appropriate for BlockScience's internal-first, IDE-first deployment, where Obsidian Flavored Markdown documents with YAML frontmatter are stored in git repositories and accessed through Obsidian and Claude Code.

## Overview

The logical architecture established 14 technology-agnostic components organized into 6 areas: Type System (C1-C2), Document Management (C3-C5), Coherence Verification (C6-C8), Quality Assessment (C9-C10), Knowledge Graph (C11-C12), and Workflow & Accountability (C13-C14). This physical architecture translates those components into a minimal set of concrete technologies.

The key architectural decisions reflect the constraints from the conceptual architecture and lessons from prototyping:

1. **File-based storage over database**: Documents remain human-readable markdown files in git repositories (constraint C1, C2)
2. **Obsidian Flavored Markdown**: Documents use OFM syntax (CommonMark + GFM tables + wikilinks) for Obsidian compatibility
3. **Git as truth with accountability**: All simplices version-controlled in git; accountability via GitHub username + `git blame` (constraint C2); GPG signatures as future upgrade path
4. **Human-in-the-loop**: Validation edges require explicit human approval captured in YAML frontmatter (constraint C3)
5. **Python-only toolchain**: All programmatic tooling in Python with uv for environment management
6. **IDE-first interfaces**: Obsidian for navigation/review, Claude Code for AI-assisted authoring

The Element-Component Matrix shows how 12 physical elements combine to implement all 14 logical components.

## Logical Architecture Reference

[[logical-architecture-knowledge-complex-refactor]]

### Components Summary

| ID  | Name                | Responsibility                                                           |
| --- | ------------------- | ------------------------------------------------------------------------ |
| C1  | Type Ontology       | Define and manage simplex type hierarchy, inheritance rules, local rules |
| C2  | Schema Registry     | Store schemas for each type defining required YAML fields                |
| C3  | Template Registry   | Store and retrieve document templates by type                            |
| C4  | Document Composer   | Assemble documents from templates and parameters                         |
| C5  | Simplex Store       | Persist and retrieve typed simplices with coherence enforcement          |
| C6  | Schema Verifier     | Verify YAML frontmatter against type schemas                             |
| C7  | Structure Analyzer  | Verify markdown body structure against spec-defined sections             |
| C8  | Boundary Verifier   | Verify simplicial complex rules and local rules                          |
| C9  | Evaluation Engine   | Score documents against guidance criteria                                |
| C10 | Result Presenter    | Format verification and evaluation results for display                   |
| C11 | Search Index        | Support full-text and filtered search across typed simplices             |
| C12 | Graph Navigator     | Traverse typed relationships and discover backlinks                      |
| C13 | Workflow Coordinator| Manage approval requests and runbook execution                           |
| C14 | Simplex Constructor | Create typed edges and faces ensuring coherence                          |

## Physical Architecture

### Element Table

| ID  | Name                 | Technology/Tool        | Version          | Purpose                                                        |
| --- | -------------------- | ---------------------- | ---------------- | -------------------------------------------------------------- |
| E1  | Ontology Files       | OFM + YAML             | OFM 2024         | Load-bearing type definitions; stored separately, change-resistant |
| E2  | Document Files       | OFM + YAML             | OFM 2024         | All simplices (vertices, edges, faces) as markdown with frontmatter |
| E3  | Template Files       | OFM + placeholders     | OFM 2024         | Simple `<placeholder>` syntax for document scaffolding         |
| E4  | Git Repository       | Git                    | 2.40+            | Version control, branching, accountability via git blame       |
| E5  | Python Package       | Python + uv            | 3.12+            | Core library, scripts, virtual environment management          |
| E6  | YAML Parser          | PyYAML                 | 6.0+             | Frontmatter parsing (structural truth for simplicial complex)  |
| E7  | Graph Library        | NetworkX               | 3.2+             | In-memory graph for traversal, topology, boundary verification |
| E8  | Chart Visualization  | matplotlib + plotly    | 3.8+ / 5.18+     | Visualize charts for validation (essential verification step)  |
| E9  | Obsidian             | Obsidian               | 1.5+             | Navigation, search, review, wikilink rendering                 |
| E10 | Claude Code          | Claude Code            | Latest           | LLM-assisted authoring via system prompt                       |
| E11 | GPG Signatures       | GnuPG                  | 2.x              | Sign git commits and accountability edges                      |
| E12 | GitHub Actions       | GitHub Actions         | Latest           | CI enforcement of ontology rules; prevent invalid merges       |

### Markdown Flavor Specification

This architecture uses **Obsidian Flavored Markdown (OFM)**, a layered markdown standard:

| Layer | Standard | Features | Tools Supporting |
|-------|----------|----------|------------------|
| 1 | CommonMark | Headers, lists, code blocks, links, emphasis | All markdown tools |
| 2 | GFM Extensions | Tables, task lists, strikethrough, autolinks | GitHub, Obsidian, most editors |
| 3 | Obsidian Extensions | Wikilinks `[[doc]]`, callouts `> [!note]`, embeds `![[doc]]` | Obsidian only |

**Design principle**: Wikilinks (`[[document-name]]`) serve **Obsidian navigation**. Simplicial complex boundaries (edges, faces) are determined from **YAML frontmatter fields** (`source`, `target`, `boundary_edges`, `boundary_vertices`), not from wikilink presence in body text. This separation ensures:

- Non-Obsidian tools can compute graph structure from YAML alone
- Wikilinks are a UI convenience, not a structural dependency
- Documents remain valid even if wikilinks are removed

### Element Definitions

#### E1: Ontology Files

**Technology:** Obsidian Flavored Markdown with YAML frontmatter
**Version:** OFM 2024 (CommonMark + GFM + Obsidian extensions)

**Purpose:** Store type ontology definitions as load-bearing infrastructure documents that define the type system for the entire knowledge complex.

**Rationale:** Ontology files are conceptually distinct from regular documents—they define the rules that govern all other documents. They should be stored in a protected location and changed rarely. Like database schemas, ontology changes have cascading effects.

**Configuration:**
- Location: Protected directory (e.g., `ontologies/` or package distribution)
- Naming: `ontology-<name>.md`
- Required frontmatter: `type: vertex/ontology`, `extends: doc`
- Body structure: Vertex Types, Edge Types, Face Types, Chart Types, Local Rules sections
- Change control: Requires explicit approval; version-locked in deployments

#### E2: Document Files

**Technology:** Obsidian Flavored Markdown with YAML frontmatter
**Version:** OFM 2024

**Purpose:** All simplices (vertices, edges, faces) stored as human-readable markdown files that can be authored in Obsidian, reviewed, and version-controlled.

**Rationale:** Human-readable markdown is required by constraint C1. YAML frontmatter provides structured metadata that defines the simplicial complex structure. The body contains human-readable content with wikilinks for Obsidian navigation.

**Configuration:**
- Vertices: `00_vertices/` directory
- Edges: `01_edges/` directory
- Faces: `02_faces/` directory
- Charts: `charts/` directory
- File extension: `.md`
- Frontmatter delimiter: `---`
- Structural fields: `source`, `target` (edges); `boundary_edges`, `boundary_vertices` (faces)

#### E3: Template Files

**Technology:** Obsidian Flavored Markdown with simple placeholder syntax
**Version:** OFM 2024

**Purpose:** Document templates with placeholder syntax for scaffolding new documents.

**Rationale:** Templates use simple `<placeholder>` syntax (e.g., `<name>`, `<version>`, `YYYY-MM-DDTHH:MM:SSZ`) rather than a templating engine. This syntax is:
- Human-readable in Obsidian
- Trivial to process with Python string replacement
- Compatible with Obsidian's built-in Templates plugin
- No additional dependency (Jinja2 not needed)

**Configuration:**
- Location: `templates/` directory with subdirectories mirroring document structure
- Naming: `<type-name>.md` (e.g., `spec.md`, `guidance.md`)
- Placeholders: `<name>`, `<version>`, `<description>`, `YYYY-MM-DDTHH:MM:SSZ`
- Required sections: Must match spec-defined required sections for the type

#### E4: Git Repository

**Technology:** Git distributed version control
**Version:** Git 2.40+

**Purpose:** Version control, branching for approval workflows, and accountability via `git blame` attribution.

**Rationale:** Git is required by constraint C2 as the source of truth. The current implementation uses GitHub username + `git blame` for accountability (see Accountability Model section). GPG-signed commits are defined as a future upgrade path for external/adversarial audit contexts.

**Configuration:**
- `.gitignore`: Exclude `.obsidian/`, `__pycache__/`, `.venv/`, `*.pyc`
- Branch strategy: `main` for assured documents, feature branches for drafts
- Signing: `git config commit.gpgsign true` (optional; future requirement)
- Hooks: Pre-commit for verification (optional)

#### E5: Python Package

**Technology:** Python with uv for environment management
**Version:** Python 3.12+, uv latest

**Purpose:** Core library implementing all programmatic logic for verification, graph operations, and visualization.

**Rationale:** Python is BlockScience's primary language. Python 3.12+ provides performance improvements and better error messages. uv provides fast, reliable environment management replacing pip/venv/virtualenv with a single tool.

**Configuration:**
- Package definition: `pyproject.toml` with hatchling build backend
- Environment: `uv venv` for virtual environment, `uv pip install` for dependencies
- Dependencies: PyYAML, NetworkX, matplotlib, plotly, numpy, scipy, pytest
- Scripts: `scripts/` directory for verification, visualization, analysis tools

#### E6: YAML Parser

**Technology:** PyYAML
**Version:** 6.0+

**Purpose:** Parse YAML frontmatter from markdown files to extract structural metadata for the simplicial complex.

**Rationale:** PyYAML is the standard Python YAML parser. It's fast, well-maintained, and sufficient for frontmatter parsing. The frontmatter contains the structural truth—`type`, `source`, `target`, `boundary_edges` fields that define the simplicial complex.

**Configuration:**
- Loading: `yaml.safe_load()` for security (no arbitrary Python execution)
- Frontmatter extraction: Split on `---` delimiters, parse middle section
- Error handling: Catch `yaml.YAMLError` for malformed frontmatter

#### E7: Graph Library

**Technology:** NetworkX
**Version:** 3.2+

**Purpose:** In-memory graph representation for relationship traversal, backlink discovery, topological analysis, and boundary verification.

**Rationale:** NetworkX is Python's standard graph library with algorithms for path finding, cycle detection, and subgraph operations. The knowledge complex graph is built from YAML frontmatter at startup—each edge document's `source` and `target` fields create graph edges.

**Configuration:**

- Graph type: `nx.MultiDiGraph` (directed edges with multiple edge types)
- Node attributes: Vertex type, file path, frontmatter metadata
- Edge attributes: Edge type, source, target, file path
- Queries: `G.predecessors()`, `G.successors()` for traversal

**Relationship to Simplicial Complex:**

NetworkX represents the **1-skeleton** (vertices and edges) of the simplicial complex. Faces (2-simplices) are higher-order objects not directly representable in a graph. The implementation handles this as follows:

- NetworkX stores vertices and edges with their metadata
- Face boundaries (`boundary_edges`, `boundary_vertices` fields) are stored as YAML frontmatter
- The boundary verifier computes face closure from YAML, not from NetworkX structure
- Euler characteristic verification uses both NetworkX (for V, E counts) and YAML (for F count)

#### E8: Chart Visualization

**Technology:** matplotlib + plotly
**Version:** matplotlib 3.8+, plotly 5.18+

**Purpose:** Visualize charts (subcomplexes) for validation—a critical step in verifying chart correctness.

**Rationale:** Visualization is essential for validating charts before approval. Visual inspection catches structural issues that automated checks might miss. matplotlib provides static 2D visualization; plotly provides interactive 3D visualization for complex charts.

**Configuration:**
- matplotlib: 2D graph layouts, assurance triangle diagrams
- plotly: Interactive 3D simplicial complex visualization
- Supporting: numpy for numerical operations, scipy for sparse matrices (Hodge analysis)
- Output: PNG/SVG for static, HTML for interactive

#### E9: Obsidian

**Technology:** Obsidian knowledge base application
**Version:** Obsidian 1.5+

**Purpose:** Primary human interface for navigation, search, document review, and light editing.

**Rationale:** Obsidian is the knowledge explorer interface specified in the field survey. It provides native support for OFM syntax (wikilinks, YAML frontmatter), graph visualization, and backlink discovery. The vault is simply the git repository—no separate data store.

**Configuration:**
- Vault: Point Obsidian at the git repository root
- Recommended plugins: Dataview (for queries), Graph Analysis (for visualization)
- Templates: Configure to use `templates/` directory
- Settings: Enable YAML frontmatter parsing, wikilink auto-completion

#### E10: Claude Code

**Technology:** Claude Code (Anthropic CLI/IDE assistant)
**Version:** Latest

**Purpose:** LLM-assisted authoring with knowledge complex awareness, template filling, verification interpretation, and guided workflow execution.

**Rationale:** Claude Code is the LLM facilitator specified in the field survey. The integration is configuration-based via `.claude/CLAUDE.md` system prompt that teaches Claude about knowledge complex conventions, document types, and verification workflows.

**Configuration:**
- System prompt: Repository's `.claude/CLAUDE.md` file
- Context: Current working directory provides repository context
- Capabilities: Template retrieval, prior work discovery, draft generation, verification interpretation
- Constraints: Human approval required—Claude prepares but doesn't approve validation edges

#### E11: GPG Signatures (Future Capability)

**Technology:** GnuPG (GNU Privacy Guard)
**Version:** GnuPG 2.x
**Status:** Future upgrade path (not currently required)

**Purpose:** Cryptographic signatures for git commits, enabling cryptographically verifiable attribution.

**Current State:** GPG signatures are not currently required. The framework uses GitHub username identity with `git blame` for accountability (see Accountability Model below). GPG is documented here as a planned upgrade path for external/adversarial audit contexts.

**Future Configuration** (when implemented):

- Key generation: `gpg --gen-key` for each signer
- Git integration: `git config user.signingkey <key-id>`, `git config commit.gpgsign true`
- Verification: `git log --show-signature` to verify commit signatures
- Key distribution: Public keys shared via keyserver or repository

### Accountability Model

The framework defines accountability through typed simplices (signs edges, qualifies edges, signature faces). This section describes the physical implementation that enforces these semantics.

#### Current Implementation (Internal Use)

**Identity Mechanism:** GitHub username serves as signer identity.

- The `github_username` field in signer vertices maps to git commit authors
- No cryptographic key infrastructure required
- Sufficient for internal trusted team use

**Attribution Mechanism:** `git blame` provides artifact-level attribution.

- Each accountability file (signs edge, validation edge, signature face) can be traced to the specific commit and author that created/modified it
- Attribution is per-artifact, not per-commit-batch
- Git history provides audit trail

**CI Enforcement:** `validate-accountability.yml` checks accountability constraints.

- Validates that the git commit author matches the `github_username` in the relevant signer vertex
- For LLM-assisted validations, validates that commit author matches `human_approver` field
- Provides per-artifact accountability even when multiple files change in one commit

**Time Authority:** `signing_date` in YAML frontmatter is the authoritative timestamp for qualification expiry checks. Committers are trusted to accurately record signing dates. For internal use with trusted team members, this is sufficient.

#### Future Upgrade Path (Cryptographic Identity)

When cryptographic identity verification is needed (external/adversarial audit contexts):

1. **GPG-signed commits**: Add `commit.gpgsign = true` requirement for accountability files
2. **Content hashing**: Add `content_hash` field (SHA-256 of canonical YAML + body) for tamper detection
3. **Detached signatures**: Support `.sig` files or embedded signature field for artifact-level cryptographic binding
4. **Key distribution**: Establish public key infrastructure for signers
5. **Timestamp correlation**: Enforce that `signing_date` is within tolerance of commit timestamp

These upgrades layer on top of the current implementation without changing the framework design (the ontology's signs/qualifies/signature types remain unchanged).

#### E12: GitHub Actions

**Technology:** GitHub Actions (CI/CD)
**Version:** Latest

**Purpose:** Continuous integration enforcement of ontology rules, preventing merges that would break the simplicial complex or violate type rules.

**Rationale:** While local verification (E5) catches issues during authoring, GitHub Actions provides a repository-level gate that prevents invalid documents from being merged to protected branches. This is essential for maintaining ontology coherence when multiple contributors are working on the same repository. CI enforcement ensures that even if local checks are bypassed, the repository remains consistent.

**Configuration:**

- Workflow file: `.github/workflows/verify.yml`
- Triggers: On pull request to `main`, on push to `main`
- Jobs:
  - `verify-documents`: Run `verify_template_based.py` on all changed documents
  - `verify-types`: Run `verify_typed.py` on all changed documents
  - `verify-boundaries`: Run boundary verification on edges and faces
  - `validate-accountability`: Check git commit author matches accountable party in YAML
  - `verify-qualifications`: Verify signs edges reference valid (non-expired) qualifies edges
  - `verify-charts`: Run chart topology verification if charts are modified
- Branch protection: Require CI pass before merge to `main`
- Caching: Cache Python environment with uv for faster runs

**Example workflow:**
```yaml
name: Verify Knowledge Complex
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync
      - run: uv run python scripts/verify_template_based.py --all
      - run: uv run python scripts/verify_typed.py --all
```

#### Accountability Verification Jobs

The following CI jobs enforce accountability for signing-related documents:

**validate-accountability** (triggered when accountability files are modified):

- Runs when PR includes changes to: `01_edges/signs-*.md`, `02_faces/signature-*.md`, `01_edges/validation-*.md`
- For `manual` validations: checks that git commit author matches the `validator` field
- For `llm-assisted` or `automated` validations: checks that git commit author matches the `human_approver` field
- Maps git author to signer via the `github_username` field in signer vertices
- Posts PR comment on failure with guidance

**verify-qualifications** (triggered when signs edges are modified):

- Runs when PR includes changes to: `01_edges/signs-*.md`
- For each signs edge being created or modified, checks:
  1. The referenced `qualifies_edge` exists
  2. The qualifies edge was valid (not expired) at the `signing_date`
  3. The signer's `github_username` matches the git commit author

These jobs enforce the accountability requirements defined in [[spec-for-signs]] and [[spec-for-qualifies]] using the current implementation (GitHub username + git blame). When GPG signatures are implemented (E11), additional cryptographic verification will be added.

### Deployment View

The knowledge complex framework deploys as a file-based system with GitHub as the remote repository and CI enforcement layer.

#### Deployment Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        User Workstation                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐              ┌───────────────────────────────┐    │
│  │   Obsidian   │              │         VS Code IDE            │    │
│  │    (E9)      │              │  ┌─────────────────────────┐  │    │
│  └──────┬───────┘              │  │     Claude Code (E10)   │  │    │
│         │                      │  │       (extension)       │  │    │
│         │                      │  └─────────────────────────┘  │    │
│         │                      └──────────────┬────────────────┘    │
│         └─────────────┬───────────────────────┘                      │
│                       │                                              │
│                       ▼                                              │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                  Python Package (E5)                          │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────────────────────────┐     │   │
│  │  │  YAML   │ │ NetworkX│ │  Visualization (matplotlib, │     │   │
│  │  │ Parser  │ │  Graph  │ │  plotly, numpy, scipy)      │     │   │
│  │  │  (E6)   │ │  (E7)   │ │        (E8)                 │     │   │
│  │  └─────────┘ └─────────┘ └─────────────────────────────┘     │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                       │                                              │
│                       ▼                                              │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              Git Repository (E4) + Accountability (E11)       │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │   │
│  │  │  Ontology   │ │  Template   │ │  Document   │             │   │
│  │  │  Files (E1) │ │  Files (E3) │ │  Files (E2) │             │   │
│  │  │ (protected) │ │             │ │             │             │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘             │   │
│  │  ┌───────────────────────────────────────────────────────┐   │   │
│  │  │  00_vertices/  │  01_edges/  │  02_faces/  │  charts/  │   │   │
│  │  └───────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                       │                                              │
└───────────────────────┼─────────────────────────────────────────────┘
                        │ git push
                        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          GitHub (Remote)                             │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                  GitHub Actions (E12)                         │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐             │   │
│  │  │   verify-   │ │   verify-   │ │   verify-   │             │   │
│  │  │  documents  │ │    types    │ │  boundaries │             │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘             │   │
│  │  ┌─────────────┐ ┌──────────────┐                            │   │
│  │  │   verify-   │ │    verify-   │                            │   │
│  │  │  signatures │ │qualifications│                            │   │
│  │  └─────────────┘ └──────────────┘                            │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                       │                                              │
│                       ▼                                              │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              Branch Protection Rules                          │   │
│  │  • Require CI pass before merge to main                      │   │
│  │  • Require GPG-signed commits (future; optional for now)     │   │
│  │  • Require pull request reviews (optional)                   │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

#### Environment Configuration

| Environment | Configuration Notes |
|-------------|---------------------|
| Development | Obsidian vault pointed at repo, Claude Code configured with system prompt, Python environment via `uv venv && uv pip install -e .`, GPG key optional (future) |
| CI (GitHub) | GitHub Actions runs verification on PR/push; branch protection requires CI pass; workflow uses `astral-sh/setup-uv` for fast Python setup |
| Production | Same as development for internal-first deployment. GitHub serves as remote with CI enforcement |

## Element-Component Matrix

### Matrix View

|     | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | C13 | C14 |
|-----|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|-----|
| E1  | X  | X  |    |    |    |    |    |    |    |    |     |     |     |     |
| E2  |    |    |    |    | X  |    |    |    |    |    |     |     |     |     |
| E3  |    |    | X  |    |    |    |    |    |    |    |     |     |     |     |
| E4  |    |    |    |    | X  |    |    |    |    |    |     |     | X   |     |
| E5  | S  | S  | S  | X  | S  | X  | X  | X  | X  | X  | S   | S   | X   | X   |
| E6  |    |    |    | P  |    | X  |    |    |    |    |     |     |     | P   |
| E7  |    |    |    |    |    |    |    | X  |    |    |     | X   |     |     |
| E8  |    |    |    |    |    |    |    |    |    | X  |     |     |     |     |
| E9  |    |    |    |    |    |    |    |    |    |    | X   | X   |     |     |
| E10 |    |    |    | P  |    |    |    |    | P  |    | P   |     | P   |     |
| E11 |    |    |    |    |    |    |    |    |    |    |     |     | X   |     |
| E12 |    |    |    |    |    | X  | X  | X  |    |    |     |     |     |     |

**Legend:** X = Primary Implementation, S = Supporting (infrastructure), P = Partial (assists)

### Relationship Details

| Element | Component | Implementation Type | Rationale |
|---------|-----------|---------------------|-----------|
| E1 | C1, C2 | Full | Ontology files define type hierarchy AND serve as schema definitions |
| E2 | C5 | Full | Document files ARE the Simplex Store—persistence as markdown files |
| E3 | C3 | Full | Template files ARE the Template Registry |
| E4 | C5, C13 | Shared | Git provides version control for storage and accountability for workflows |
| E5 | C4, C6-C10, C13-C14 | Full | Python package implements all programmatic logic |
| E6 | C6, C4, C14 | Partial | YAML parser extracts frontmatter for verification and construction |
| E7 | C8, C12 | Full | NetworkX provides boundary verification and graph traversal |
| E8 | C10 | Full | Visualization presents charts for human validation |
| E9 | C11, C12 | Full | Obsidian provides search and graph navigation for humans |
| E10 | C4, C9, C11, C13 | Partial | Claude Code assists with composition, evaluation, search, workflow |
| E11 | C13 | Future | GPG signatures (future); currently GitHub username + git blame |
| E12 | C6, C7, C8 | Full | GitHub Actions enforces verification at repository level |

### Key Implementations

1. **File-Based Storage (E1, E2, E3, E4)**: The simplicial complex is stored entirely as files in a git repository. Ontology files (E1) define types; document files (E2) store simplices; template files (E3) scaffold new documents. Git (E4) provides version control and `git blame` attribution for accountability.

2. **Python Package as Core (E5)**: The Python package implements verification (C6, C7, C8), evaluation (C9), composition (C4), construction (C14), and workflow coordination (C13). It uses PyYAML (E6) for frontmatter parsing and NetworkX (E7) for graph operations.

3. **YAML as Structural Truth (E6)**: The simplicial complex structure is determined entirely from YAML frontmatter fields. Edge documents have `source` and `target`; face documents have `boundary_edges` and `boundary_vertices`. Wikilinks in body text are for Obsidian navigation only.

4. **Dual Interface (E9, E10)**: Obsidian (E9) provides human navigation, search, and review. Claude Code (E10) provides AI-assisted authoring. Both operate on the same git repository.

5. **Visualization for Validation (E8)**: Chart visualization is essential for validating charts before approval. Visual inspection catches structural issues that automated checks miss.

6. **Accountability (E11)**: Current implementation uses GitHub username + `git blame` for attribution. GPG signatures are defined as a future upgrade path for external/adversarial audit contexts (see Accountability Model section).

7. **CI Enforcement (E12)**: GitHub Actions provides repository-level verification gates. Even if local checks are bypassed, CI prevents merging documents that violate ontology rules, maintaining coherence across contributors.

## Unit Testing Strategy

### Test Approach by Element

| Element | Test Framework | Test Method | Success Indicator |
|---------|----------------|-------------|-------------------|
| E1 | pytest | Parse ontology files, verify structure | All ontology files parse correctly |
| E2 | pytest | Read/write document files, verify roundtrip | Content preserved through read/write |
| E3 | pytest | Apply templates with test parameters | Placeholders replaced correctly |
| E4 | pytest + git | Commit operations, signature verification | Git operations succeed, signatures valid |
| E5 | pytest + coverage | Unit tests for each module | >90% coverage, all tests pass |
| E6 | pytest | Parse test YAML files with edge cases | All frontmatter parsed correctly |
| E7 | pytest | Graph construction, traversal, cycle detection | Algorithms return correct results |
| E8 | pytest | Generate visualizations, verify output | Visualizations render without error |
| E9 | Manual | Vault configuration, navigation, search | Obsidian displays correctly |
| E10 | Integration | Claude Code interactions with test repo | AI assistance produces valid outputs |
| E11 | pytest + gpg | Sign and verify test commits | Signatures verify correctly |
| E12 | GitHub Actions | Workflow runs on test repository | All verification jobs pass |

## Traceability to Logical Architecture

### From Components to Elements

| Component | Implemented by Elements | Implementation Notes |
|-----------|------------------------|----------------------|
| C1 Type Ontology | E1, E5 | Ontology files (E1) ARE the definitions; Python (E5) provides access |
| C2 Schema Registry | E1, E5 | Ontology files include schema definitions; specs define required fields |
| C3 Template Registry | E3, E5 | Template files (E3) ARE the registry; Python retrieves them |
| C4 Document Composer | E5, E6, E10 | Python orchestrates; YAML parser extracts; Claude assists |
| C5 Simplex Store | E2, E4 | Document files (E2) ARE storage; Git (E4) provides version control |
| C6 Schema Verifier | E5, E6, E12 | Python implements verification; GitHub Actions enforces |
| C7 Structure Analyzer | E5, E12 | Python analyzes structure; GitHub Actions enforces |
| C8 Boundary Verifier | E5, E7, E12 | Python + NetworkX verify; GitHub Actions enforces |
| C9 Evaluation Engine | E5, E10 | Python implements scoring; Claude assists interpretation |
| C10 Result Presenter | E5, E8 | Python formats results; visualization for charts |
| C11 Search Index | E9, E10 | Obsidian provides search; Claude uses search |
| C12 Graph Navigator | E7, E9 | NetworkX stores graph; Obsidian visualizes |
| C13 Workflow Coordinator | E4, E5, E10, E11 | Git blame for accountability (GPG future); Python for logic; Claude guides |
| C14 Simplex Constructor | E5, E6 | Python implements construction; YAML generates frontmatter |

### Coverage Analysis

- **Complete coverage**: All 14 logical components implemented by the 12 elements
- **File-based foundation**: E1, E2, E3, E4 provide file-based storage (no external services)
- **Python as hub**: E5 implements core logic for most components
- **Dual interface**: E9 (Obsidian) and E10 (Claude Code) provide complementary access
- **Accountability**: E11 enables identity verification (GitHub username now; GPG future)
- **CI enforcement**: E12 (GitHub Actions) prevents invalid documents from reaching main branch

## Deferred Elements

The following elements are deferred to future iterations when scaling or quality-of-life improvements are needed:

| Element | Technology | When Needed |
|---------|------------|-------------|
| JSON Schema Files | JSON Schema Draft 2020-12 | When specs need machine-checkable schemas beyond YAML |
| Markdown AST Parser | markdown-it-py | When structure verification needs deep AST analysis |
| Full-Text Search Engine | Whoosh or Elasticsearch | When Obsidian search insufficient (>10k docs) |
| CLI Framework | Click | When scripts need proper CLI UX for non-IDE users |
| Terminal Formatter | Rich | When terminal output needs polish |
| Document Database | MongoDB or similar | When file-based storage doesn't scale |
| Relational Database | PostgreSQL | For RBAC views, traceability queries, status dashboards |
| LLM Abstraction Layer | OpenRouter | When supporting non-Claude models or cloud deployment |

## Technology Selection Rationale

### Selection Criteria

Technology choices were guided by:

1. **Minimal toolchain**: Fewer dependencies = fewer compatibility issues
2. **Obsidian compatibility**: OFM as primary markdown flavor
3. **Python-only**: No TypeScript/JavaScript toolchain needed
4. **File-based**: No external services for MVP (except GitHub for CI)
5. **Accountability**: GitHub username + git blame (GPG future upgrade)
6. **CI enforcement**: GitHub Actions prevents invalid documents from reaching main

### What This Architecture Eliminates

Compared to the initial 16-element design, this simplified architecture eliminates:

- VS Code extension (TypeScript toolchain) — Claude Code extension suffices
- Jinja2 templating — Simple `<placeholder>` syntax works with Obsidian
- ruamel.yaml — PyYAML sufficient for parsing
- markdown-it-py — Structure verification via spec patterns
- jsonschema — YAML frontmatter + specs sufficient for MVP
- Whoosh search — Obsidian provides search
- Click CLI — Scripts run directly
- Rich formatting — Print statements sufficient for MVP

## Constraints and Assumptions

### Constraints

- **Cst1**: All simplices stored as OFM files with YAML frontmatter (from conceptual C1)
- **Cst2**: Git is the sole version control system; GPG signing optional/future (from conceptual C2)
- **Cst3**: Validation requires human signature; cannot be fully automated (from conceptual C3)
- **Cst4**: Python 3.12+ required; environment managed by uv
- **Cst5**: Simplicial complex boundaries computed from YAML frontmatter, not wikilinks
- **Cst6**: File-based search may not scale beyond ~10,000 documents

### Assumptions

- **Asm1**: Users have Python 3.12+ and uv installed or can install them
- **Asm2**: Users have Obsidian 1.5+ installed
- **Asm3**: Users have access to Claude Code for LLM assistance
- **Asm4**: GPG 2.x available if cryptographic signatures needed (optional for current use)
- **Asm5**: Git 2.40+ is available on user workstations
- **Asm6**: Repository is hosted on GitHub with Actions enabled

---

**Note:** This physical architecture is version 0.2.0, with 12 elements (simplified from initial 16-element design, plus GitHub Actions for CI). It reflects lessons from prototyping: Obsidian Flavored Markdown as the data standard, simple placeholder templates, Python-only toolchain with uv, GitHub username + git blame for accountability (GPG as future upgrade), and GitHub Actions for ontology enforcement. Deferred elements can be added when scaling requires them.
