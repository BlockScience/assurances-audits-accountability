# Module 06: Document Composition

**Learning Journey: Knowledge Complexes**
**Module:** 06 of 07
**Skill Developed:** Document Composition

## Learning Goals

By the end of this module, you will be able to:

1. Understand the limitations of monolithic documents and why composition matters
2. Use Obsidian embeds (`![[file]]`) to build modular documents
3. Apply the PPP (Persona-Purpose-Protocol) framework for AI agent design
4. Compile compositional documents into standalone artifacts
5. Assure both component documents AND compiled compositions
6. Design compositional architectures for maintainability and reuse

## Prerequisites

Before starting this module, you should have completed:

- **Module 03:** Composing Typed Simplicial Complexes (composition operations)
- **Module 05:** Assurance & Audits (assurance triangles, audit workflows)
- **Skills Required:** Creating assurance faces, running assurance audits, composition operations

You should be familiar with:
- The assurance triangle (verification + validation + coupling)
- Running `audit_assurance_chart.py` and interpreting results
- Understanding how charts represent typed simplicial complexes
- Composition operations: unions, intersections, and subset operations

## Module Roadmap

This module builds on two prerequisite paths:
1. **From Module 03**: You learned how typed simplicial complexes compose
2. **From Module 05**: You learned how to assure documents with assurance faces

Now we'll combine these skills to design **compositional document architectures** - systems where component documents are independently assured and then systematically composed into larger artifacts.

We'll learn to:
1. Recognize when monolithic documents become unmaintainable
2. Use Obsidian embeds for modular document structure
3. Apply the PPP framework as a worked example of compositional design
4. Compile references using `compile_document.py`
5. Establish assurance workflows for compositional documents

---

## Section 1: The Problem with Monolithic Documents

**Time:** 45 minutes

### When Monolithic Fails

Consider a complex AI agent configuration. You need to define:
- **Persona**: Who is this agent?
- **Purpose**: What does it accomplish?
- **Protocol**: How does it work?
- **Tool configurations**: What tools are available?
- **Context references**: What knowledge does it need?

A monolithic approach puts everything in one massive document:

```markdown
# Agent Configuration

## Persona
[200 lines of persona definition]

## Purpose
[150 lines of purpose specification]

## Protocol
[400 lines of protocol details]

## Tools
[300 lines of tool configurations]

## Context
[500 lines of reference material]
```

**Problems:**
1. **Maintenance burden**: Changing anything requires understanding the whole document
2. **Validation complexity**: How do you verify 1500+ lines against a spec?
3. **Reuse impossible**: Can't share the persona definition with another agent
4. **Accountability unclear**: Who is responsible for which sections?
5. **Testing difficulty**: Can't independently test components

### The Compositional Solution

Instead of one monolithic document, we create **component documents** that compose:

```
agent-config.md (compositional)
  ├── ![[persona-agent.md]]     (verified, validated, assured)
  ├── ![[purpose-agent.md]]     (verified, validated, assured)
  ├── ![[protocol-agent.md]]    (verified, validated, assured)
  └── tool configs (inline)
```

**Benefits:**
1. **Component independence**: Each component can be verified/validated separately
2. **Clear accountability**: Each component has its own human approver
3. **Reusability**: Persona could be reused in a different agent
4. **Incremental assurance**: Assure components first, then the composition
5. **Simpler maintenance**: Change one component without touching others

### Exercise 1.1: Identify Compositional Candidates

**Task:** Review the PPP system prompt structure.

```bash
# Look at the compiled system prompt structure
cat 00_vertices/system_prompt-claude.md | head -100
```

**Questions:**
1. What are the major components embedded in this document?
2. Which components could be independently assured?
3. What would change if we modified the persona?
4. How does this differ from a monolithic approach?

---

## Section 2: Obsidian Embeds for Modular Documents

**Time:** 60 minutes

### Embed Syntax

Obsidian provides a simple embedding syntax:

```markdown
# Full file embed
![[filename.md]]

# Section embed
![[filename.md#Section Name]]

# Block embed (with ^block-id)
![[filename.md#^block-id]]
```

When you write `![[persona-agent.md]]`, the entire contents of that file are logically included at that point.

### Embed Resolution

Embeds create **reference relationships**:

```
system_prompt-claude.md
    └── EMBEDS ──→ persona-claude.md
    └── EMBEDS ──→ purpose-claude.md
    └── EMBEDS ──→ protocol-claude.md
```

These are **typed relationships** - the embedding document depends on the embedded documents.

### Typed Subsections

When a document embeds typed components, we call these **typed subsections**:

```yaml
---
type: vertex/system_prompt
id: v:system_prompt:claude
components:
  persona: v:persona:claude
  purpose: v:purpose:claude
  protocol: v:protocol:claude
---

# System Prompt - Claude Assistant

## Persona

![[persona-claude.md]]

## Purpose

![[purpose-claude.md]]

## Protocol

![[protocol-claude.md]]
```

The frontmatter declares the **type** of each embedded component, creating a typed structure.

### Real Example: The Claude System Prompt

Let's examine the actual PPP structure in this knowledge complex:

```bash
# Read the system prompt definition
cat 00_vertices/system_prompt-claude.md
```

**Structure:**
1. **Frontmatter** declares type, ID, and component references
2. **Persona section** embeds the persona document
3. **Purpose section** embeds the purpose document
4. **Protocol section** embeds the protocol document

### Exercise 2.1: Trace Embed References

**Task:** Map the embed structure of the Claude system prompt.

```bash
# Find all embeds in the system prompt
grep -n '!\[\[' 00_vertices/system_prompt-claude.md
```

**Questions:**
1. How many embeds are in the system prompt?
2. What type is each embedded document?
3. Are the embedded documents independently typed?
4. How would you verify each component separately?

---

## Section 3: The PPP Framework - A Worked Example

**Time:** 90 minutes

### PPP Design Philosophy

The **Persona-Purpose-Protocol** framework is a compositional pattern for AI agent design:

1. **Purpose (designed FIRST)**: What value does the agent deliver?
2. **Persona (designed SECOND)**: What expertise matches that purpose?
3. **Protocol (designed LAST)**: How does the persona accomplish the purpose?

**Design Order Matters:**
- Purpose anchors the design (what problem are we solving?)
- Persona is selected to match purpose (who has the right expertise?)
- Protocol operationalizes both (how do they work together?)

### PPP as Typed Simplicial Complex

The PPP framework forms a **typed simplicial complex**:

**Vertices:**
- `v:persona:claude` - The persona document
- `v:purpose:claude` - The purpose document
- `v:protocol:claude` - The protocol document
- `v:system_prompt:claude` - The composed system prompt

**Edges (dependencies):**
- Protocol depends on Purpose (implements the goals)
- Protocol depends on Persona (uses the expertise)
- System prompt depends on all three components

**Faces:**
- Each component has an assurance face
- The composition has its own assurance face

### Assuring PPP Components

Each PPP component is independently assured:

**Persona Assurance:**
```
persona-claude.md
  → verified against spec-for-persona.md
  → validated against guidance-for-persona.md
  → coupled via coupling-persona.md
  → assured via f:assurance:persona-claude
```

**Purpose Assurance:**
```
purpose-claude.md
  → verified against spec-for-purpose.md
  → validated against guidance-for-purpose.md
  → coupled via coupling-purpose.md
  → assured via f:assurance:purpose-claude
```

**Protocol Assurance:**
```
protocol-claude.md
  → verified against spec-for-protocol.md
  → validated against guidance-for-protocol.md
  → coupled via coupling-protocol.md
  → assured via f:assurance:protocol-claude
```

### Assuring the Composition

After components are assured, we assure the **composition**:

**System Prompt Assurance:**
```
system_prompt-claude.md
  → verified against spec-for-system_prompt.md
  → validated against guidance-for-system_prompt.md
  → coupled via coupling-system_prompt.md
  → assured via f:assurance:system_prompt-claude
```

**Important:** The composition is assured separately from its components. This creates a two-level assurance:
1. **Component-level**: Each embedded document is assured
2. **Composition-level**: The composed document is assured

### Exercise 3.1: Examine PPP Assurance

**Task:** Trace the assurance for the Claude system prompt.

```bash
# Find assurance faces for PPP components
ls 02_faces/assurance-persona*.md
ls 02_faces/assurance-purpose*.md
ls 02_faces/assurance-protocol*.md
ls 02_faces/assurance-system_prompt*.md
```

**Questions:**
1. Does each PPP component have its own assurance face?
2. Does the composed system prompt have an assurance face?
3. What specs verify each component type?
4. How does the two-level assurance provide stronger guarantees?

---

## Section 4: Compiling Compositional Documents

**Time:** 60 minutes

### Why Compile?

Obsidian embeds are convenient for editing, but some contexts require **standalone documents**:

1. **Deployment**: LLM APIs need a single system prompt string
2. **Archival**: Preserve the exact content at a point in time
3. **Sharing**: Recipients may not have access to component files
4. **Verification**: Some tools work better with expanded content

### The compile_document.py Script

The `compile_document.py` script expands Obsidian embeds into a single standalone document:

```bash
# Compile system prompt to standalone version
python scripts/compile_document.py 00_vertices/system_prompt-claude.md 00_vertices/system_prompt-compiled.md
```

**What it does:**
1. Reads the source document
2. Finds all `![[embed]]` references
3. Recursively expands embedded content
4. Writes a standalone document with all embeds resolved

### Deterministic Compilation

Compilation is **deterministic**: the same inputs always produce the same output.

This is critical for assurance:
- If component A, B, C are assured
- And compilation is deterministic
- Then compiled(A, B, C) is reproducible
- We can assure the compiled document knowing it derives from assured components

### Verifying Compiled Documents

After compilation, we verify the compiled document:

```bash
# Verify the compiled system prompt
python scripts/verify_template_based.py 00_vertices/system_prompt-compiled.md --templates templates
```

The compiled document should:
1. Pass template verification for its type
2. Contain all expanded content from components
3. Have no remaining unresolved embed references

### Exercise 4.1: Compile and Verify

**Task:** Compile the Claude system prompt and verify the result.

```bash
# Compile
python scripts/compile_document.py 00_vertices/system_prompt-claude.md /tmp/system_prompt-test.md

# Verify no remaining embeds
grep '!\[\[' /tmp/system_prompt-test.md

# Check the compiled length vs original
wc -l 00_vertices/system_prompt-claude.md
wc -l /tmp/system_prompt-test.md
```

**Questions:**
1. How many lines is the source vs compiled document?
2. Are there any remaining `![[embed]]` references after compilation?
3. What content was expanded from each component?

---

## Section 5: Assurance Workflow for Compositions

**Time:** 75 minutes

### The Two-Level Assurance Pattern

Compositional documents require **two-level assurance**:

**Level 1: Component Assurance**
```
For each component (persona, purpose, protocol):
  1. Verify component against its spec
  2. Validate component against its guidance
  3. Create coupling edge for component domain
  4. Create assurance face for component
  5. Human approves component assurance
```

**Level 2: Composition Assurance**
```
After all components are assured:
  1. Compile the compositional document
  2. Verify compiled document against composition spec
  3. Validate compiled document against composition guidance
  4. Create coupling edge for composition domain
  5. Create assurance face for composition
  6. Human approves composition assurance
```

### Why Both Levels?

Component assurance proves each part is correct:
- Persona is a valid persona
- Purpose is a valid purpose
- Protocol is a valid protocol

Composition assurance proves they work together:
- Components integrate correctly
- Cross-references are valid
- The whole is coherent

**Analogy:** Individual tests pass, but integration tests might still fail.

### Composition Assurance Dependencies

A composition assurance face depends on its component assurance faces:

```
f:assurance:system_prompt-claude
  ├── depends on → f:assurance:persona-claude
  ├── depends on → f:assurance:purpose-claude
  └── depends on → f:assurance:protocol-claude
```

The audit trail for the system prompt should trace through all component assurance faces.

### Auditing Compositional Structures

Running an assurance audit on a compositional chart should show:
1. All components are assured
2. The composition is assured
3. All traces reach the boundary complex

```bash
# Audit a compositional chart (example)
python scripts/audit_assurance_chart.py charts/ppp-assurance/ppp-assurance.md
```

### Exercise 5.1: Design a Compositional Assurance Chart

**Task:** Design (on paper or in a text file) a chart for PPP assurance.

**Elements to include:**
1. Vertices for all PPP components (persona, purpose, protocol, system_prompt)
2. Vertices for their type specs and guidances
3. Edges for verification, validation, coupling, and dependencies
4. Faces for component assurance and composition assurance

**Questions:**
1. How many vertices in your chart?
2. How many assurance faces?
3. Does the composition face depend on component faces?
4. How does the audit trace reach boundary complex?

---

## Summary

### Key Takeaways

1. **Monolithic Documents Have Limits**
   - Maintenance burden increases with size
   - Validation becomes complex
   - Reuse is impossible
   - Accountability is unclear

2. **Compositional Design Solves These Problems**
   - Component documents are independently maintainable
   - Each component is separately verified and validated
   - Components can be reused across compositions
   - Clear accountability for each component

3. **Obsidian Embeds Enable Composition**
   - `![[file.md]]` syntax for embedding
   - Typed subsections declare component types
   - Reference relationships create dependencies
   - Composition creates typed simplicial complex structure

4. **PPP Framework Exemplifies Composition**
   - Purpose designed FIRST (anchor)
   - Persona designed SECOND (expertise match)
   - Protocol designed LAST (operationalization)
   - Each component independently assured

5. **Compilation Creates Standalone Artifacts**
   - `compile_document.py` expands embeds
   - Deterministic compilation enables reproducibility
   - Compiled documents can be verified
   - Useful for deployment and archival

6. **Two-Level Assurance for Compositions**
   - Component assurance proves each part is correct
   - Composition assurance proves parts work together
   - Composition depends on component assurance
   - Audit traces through both levels

### Skill Checklist

You should now be able to:

- Recognize when monolithic documents need compositional refactoring
- Use Obsidian embed syntax (`![[file.md]]`) effectively
- Understand typed subsections and reference relationships
- Apply the PPP framework design pattern
- Compile compositional documents to standalone artifacts
- Design two-level assurance workflows
- Understand composition dependencies in assurance traces

### What's Next

In **Module 07: Reference & Reuse**, you'll learn to:

- Create doc-kit pattern libraries for systematic reuse
- Extend assurance faces with usage documentation
- Build a registry of reusable document patterns
- Use doc-kits to systematically create new documents
- Establish reference materials for ongoing quality

The composition skills from this module prepare you for building reusable documentation patterns.

---

## Assessment

### Final Exercise: Design a Compositional Document

**Task:** Design and implement a simple compositional document using the PPP pattern.

**Requirements:**

1. **Create Component Documents** (40 points)
   - Create a minimal persona document (can be brief, 50-100 lines)
   - Create a minimal purpose document (50-100 lines)
   - Create a minimal protocol document (100-150 lines)
   - All components must pass template verification

2. **Create Composition Document** (25 points)
   - Create a system prompt document embedding all three components
   - Use proper typed subsection frontmatter
   - Embed using `![[component.md]]` syntax
   - Pass template verification

3. **Compile and Verify** (15 points)
   - Use `compile_document.py` to create standalone version
   - Verify no remaining embed references
   - Verify compiled document passes template checks

4. **Design Assurance Strategy** (20 points)
   - Document (in writing) your two-level assurance approach
   - List which specs verify each component
   - List which guidances validate each component
   - Explain how composition assurance depends on components

**Deliverables:**
- Three component documents in `00_vertices/`
- One composition document in `00_vertices/`
- One compiled document (can be in `/tmp/`)
- Write-up (200-300 words) explaining your assurance strategy

**Success Criteria:**
- All component documents pass template verification
- Composition document properly embeds all components
- Compiled document has no remaining embed references
- Write-up clearly explains two-level assurance approach

---

## Additional Resources

### Scripts Reference

```bash
# Compile compositional document
python scripts/compile_document.py <source.md> <output.md>

# Verify document structure
python scripts/verify_template_based.py <file.md> --templates templates

# Run assurance audit
python scripts/audit_assurance_chart.py charts/<chart>/<chart>.md
```

### Example Files to Study

**PPP Components:**
- `00_vertices/persona-claude.md` - Persona definition
- `00_vertices/purpose-claude.md` - Purpose definition
- `00_vertices/protocol-claude.md` - Protocol definition
- `00_vertices/system_prompt-claude.md` - Composed system prompt

**Specs for PPP Types:**
- `00_vertices/spec-for-persona.md` - Persona spec
- `00_vertices/spec-for-purpose.md` - Purpose spec
- `00_vertices/spec-for-protocol.md` - Protocol spec
- `00_vertices/spec-for-system_prompt.md` - System prompt spec

**Assurance Examples:**
- `02_faces/assurance-persona-claude.md` - Component assurance
- `02_faces/assurance-system_prompt-compiled.md` - Composition assurance

### Key Concepts for Review

1. **Compositional Design**: Breaking monolithic documents into composable components
2. **Obsidian Embeds**: `![[file.md]]` syntax for document composition
3. **Typed Subsections**: Declaring component types in frontmatter
4. **PPP Framework**: Purpose-first design for AI agents
5. **Deterministic Compilation**: Reproducible expansion of embeds
6. **Two-Level Assurance**: Component assurance + composition assurance
7. **Composition Dependencies**: How composition assurance depends on components

### Next Steps

When you're ready, proceed to **Module 07: Reference & Reuse** to learn:
- Creating doc-kit pattern libraries
- Extending assurance with usage documentation
- Building reusable document registries
- Systematic document creation workflows

---

**Module 06 Complete**

You've learned how to design compositional document architectures, use Obsidian embeds for modular structure, apply the PPP framework, compile documents to standalone artifacts, and establish two-level assurance workflows for compositional documents.
