# Figure Specifications for INCOSE IS 2026 Paper

**Document Purpose:** Define high-value figures with detailed requirements for maximum impact within page constraints.

**Design Philosophy:**
- Each figure must directly support a core claim
- Minimize page footprint while maximizing information density
- Figures should be interpretable without extensive captions
- Prefer static figures over references to interactive tools

---

## Executive Summary: Recommended Figures

| # | Figure | Supports Claim | Est. Size | Priority |
|---|--------|---------------|-----------|----------|
| 1 | Assurance Triangle Pattern | Core innovation (coupling) | 1/4 page | REQUIRED |
| 2 | INCOSE Paper Audit Chart | Self-demonstration proof | 1/2 page | REQUIRED |
| 3 | Boundary Complex Structure | Bootstrap mechanism | 1/4 page | RECOMMENDED |

**Total estimated page allocation:** ~1 page of figures (reasonable for 7000-word paper)

**Figures NOT recommended:**
- 3D interactive visualization (not printable, unclear in PDF)
- Workflow diagrams (can be described in text)
- Code listings (use minimal inline code only)
- Tables that could be sentences (integrate into text)

---

## Figure 1: The Assurance Triangle Pattern

### Purpose
Illustrate the core innovation: how verification, validation, and coupling form a closed assurance pattern.

### Claim Supported
"The key innovation is the **assurance triangle**: a 2-simplex (face) formed by three edges connecting a document to its specification, guidance, and the coupling between them."

### Requirements

**Geometry:**
- Single triangle with labeled vertices and edges
- Clear vertex labels: Document, Specification, Guidance
- Clear edge labels: Verification, Validation, Coupling
- Edge directionality indicated (verification/validation are directed; coupling is undirected)

**Visual Encoding:**
- Vertices: Distinct shapes or colors by type
  - Document: Circle (target of assurance)
  - Specification: Rectangle (structural)
  - Guidance: Rounded rectangle (qualitative)
- Edges: Different line styles by type
  - Verification: Solid arrow (deterministic)
  - Validation: Dashed arrow (qualitative)
  - Coupling: Double line, no arrow (undirected)
- Face: Light fill to indicate closure (optional)

**Annotations:**
- Small text indicating what each edge represents:
  - Verification: "Structural compliance"
  - Validation: "Quality assessment"
  - Coupling: "Type coherence"

**Size:**
- Width: Single column (~3.5 inches)
- Height: ~2.5 inches
- Total: ~1/4 page

**Caption:**
"Figure 1. The Assurance Triangle. A document achieves assurance when verification (structural compliance against specification), validation (quality assessment against guidance), and coupling (coherent type system) form a closed triangle. Human approval is required for validation edges and the assurance face."

### Data Source
Conceptual diagram - no data export needed.

### Production Notes
- Create in vector format (SVG, PDF, or high-resolution PNG)
- Ensure readability in grayscale (conference may print B&W)
- Use INCOSE template fonts if specified

---

## Figure 2: INCOSE Paper Audit Chart (Primary Empirical Result)

### Purpose
Visualize the complete assurance network for this paper, demonstrating self-application of the framework.

### Claim Supported
"The audit chart showing 100% assurance coverage is our primary empirical result."

"This paper demonstrates the framework by being an instance of it."

### Requirements

**Structure - Hierarchical Layout:**
The figure should show three distinct layers:

1. **Layer 0 (Bottom): Boundary Complex Foundation**
   - 5 vertices: root, spec-for-spec, spec-for-guidance, guidance-for-spec, guidance-for-guidance
   - 4 boundary faces (2 standard green, 2 boundary blue)
   - This is the "axiomatic foundation"

2. **Layer 1 (Middle): INCOSE Paper Type**
   - 2 vertices: spec-for-incose-paper, guidance-for-incose-paper
   - Verification/validation edges to Layer 0
   - 2 assurance faces

3. **Layer 2 (Top): This Paper**
   - 1 vertex: doc-incose-paper-2026
   - Verification/validation edges to Layer 1
   - 1 assurance face

**Visual Encoding:**
- Vertices by type:
  - Root (b0): Star or diamond (special anchor)
  - Spec: Green squares/rectangles
  - Guidance: Orange squares/rectangles
  - Doc: Blue circle (the paper itself - highlight this)
- Edges by type:
  - Verification: Blue arrows
  - Validation: Red arrows
  - Coupling: Purple undirected lines
  - Boundary (b1): Dashed lines
- Faces:
  - Standard assurance: Light green fill
  - Boundary assurance (b2): Light blue fill
  - Paper's assurance face: Highlighted (golden border or similar)

**Labels:**
- Abbreviated vertex labels for space:
  - SS = spec-for-spec
  - SG = spec-for-guidance
  - GS = guidance-for-spec
  - GG = guidance-for-guidance
  - I-S = spec-for-incose-paper
  - I-G = guidance-for-incose-paper
  - PAPER = doc-incose-paper-2026 (or "This Paper")
- Layer labels on left margin

**Key Visual Message:**
The paper (top) traces assurance through the type layer to the foundation. The chain is complete and auditable.

**Audit Status Indicator:**
- Checkmarks (✓) next to each vertex indicating ASSURED status
- Or a small "100% Coverage" badge

**Size:**
- Width: Full column or 2/3 page width (~5-6 inches)
- Height: ~3-4 inches
- Total: ~1/2 page

**Caption:**
"Figure 2. Audit Chart for This Paper. The paper (top) is assured through verification against spec-for-incose-paper and validation against guidance-for-incose-paper. These type documents are themselves assured against the boundary complex (bottom), which provides the axiomatic foundation. All 8 vertices achieve 100% assurance coverage. χ = -5."

### Data Source
```
charts/incose-paper-assurance/incose-paper-assurance.json
```

Key data points:
- V = 8, E = 20, F = 7, χ = -5
- 100% vertex coverage (7/7 targets assured)
- 7 faces: 4 boundary + 3 INCOSE-specific

### Production Notes
- This is the MOST IMPORTANT figure - invest effort here
- Consider hand-drawn aesthetic for clearer hierarchical layout
- Current 3D visualization is not suitable for print (too complex, unclear in 2D)
- Recommend 2D hierarchical layout with clear layer separation
- Ensure all text is legible at print size

---

## Figure 3: Boundary Complex Structure (Optional but Recommended)

### Purpose
Explain how the framework bootstraps itself through self-referential types anchored by a root vertex.

### Claim Supported
"The framework bootstraps itself through a boundary complex: four foundational vertices connected in a self-referential pattern. A unique root vertex resolves the self-referential paradox."

### Requirements

**Structure:**
Show the 5-vertex boundary complex with:
- Central root vertex (b0:root) at center or top
- Four foundational vertices arranged around it:
  - SS (spec-for-spec)
  - SG (spec-for-guidance)
  - GS (guidance-for-spec)
  - GG (guidance-for-guidance)

**Key Relationships to Show:**
1. **Standard coupling edges:**
   - SS ↔ GS (coupling:spec)
   - SG ↔ GG (coupling:guidance)
   - SG ↔ GS (cross-domain coupling)

2. **Boundary edges (b1) to root:**
   - SS → root (self-verification anchor)
   - GG → root (self-validation anchor)
   - root → GS (coupling proxy)
   - root → SG (coupling proxy)

3. **Two face types:**
   - Standard faces (green): f:assurance:spec-guidance, f:assurance:guidance-spec
   - Boundary faces (blue): b2:spec-spec, b2:guidance-guidance

**Visual Encoding:**
- Root: Star shape at center
- Spec vertices (SS, SG): One color
- Guidance vertices (GS, GG): Another color
- Faces shown as filled triangles with transparency

**Key Visual Message:**
Root provides an anchor point that allows self-referential types to close their assurance triangles without circular dependency.

**Size:**
- Width: Single column (~3.5 inches)
- Height: ~2.5 inches
- Total: ~1/4 page

**Caption:**
"Figure 3. Boundary Complex. The root vertex (center) anchors self-referential assurance for spec-for-spec and guidance-for-guidance. This 5-vertex structure provides the axiomatic foundation for all other document types."

### Data Source
```
charts/boundary-complex/boundary-complex.json
```

### Production Notes
- This figure explains the mathematical elegance but is less critical than Figures 1 and 2
- Include only if space permits and reviewers need to understand bootstrap mechanism
- Alternative: Describe in text with inline notation

---

## Figures NOT Recommended

### Interactive 3D Visualization
**Why not:** Cannot be rendered in PDF, unclear when flattened, adds complexity without clarity.

### Workflow Diagram (4-Phase Process)
**Why not:** Can be described in text as a numbered list. The 4 phases (Clarify → Test → Generate → Assure) are simple enough to state.

### Code Listings
**Why not:** Takes excessive space. Use minimal inline code for key commands only. Reference GitHub for full implementation.

### Detailed Edge/Face Tables
**Why not:** The JSON data has this, but a table of 20 edges doesn't aid understanding. The hierarchical visualization (Figure 2) communicates structure better.

### Before/After Comparison
**Why not:** No clear "before" state to compare against. The contribution is the framework itself, not a transformation.

---

## Figure Production Workflow

### Recommended Tools
1. **Conceptual diagrams (Figure 1, 3):** Draw.io, Lucidchart, or Figma
2. **Data-driven diagram (Figure 2):**
   - Option A: Hand-layout using diagramming tool with JSON data as reference
   - Option B: Custom script to generate SVG from JSON (recommended for precision)
   - Option C: Modify existing visualize_chart.py to output 2D hierarchical SVG

### Quality Checklist
- [ ] Readable at 50% zoom (test print scaling)
- [ ] Legible in grayscale
- [ ] Vector format (PDF, SVG, or 300+ DPI PNG)
- [ ] Consistent styling across all figures
- [ ] Fonts match paper template
- [ ] Captions are complete and standalone

### File Deliverables
For each figure, produce:
1. Source file (editable format)
2. PDF export (for LaTeX/Word inclusion)
3. PNG export at 300 DPI (backup)

---

## Summary

**Three figures total**, consuming approximately 1 page:

| Figure | What it shows | Why it matters |
|--------|---------------|----------------|
| 1. Assurance Triangle | The core pattern | Explains the innovation simply |
| 2. Audit Chart | This paper's assurance network | Proves self-demonstration claim |
| 3. Boundary Complex | Bootstrap mechanism | Shows mathematical foundation |

Figure 2 is the "hero figure" - it IS the empirical result. Figures 1 and 3 provide conceptual context. Together, they tell the complete story with minimal page footprint.
