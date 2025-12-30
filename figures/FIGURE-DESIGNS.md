# Detailed Figure Designs for INCOSE Paper

## Figure 1: The Assurance Triangle Pattern

### Geometry Specification

**Canvas:** 350px × 280px (3.5" × 2.8" at 100dpi)

**Triangle Layout:**
- Equilateral triangle, point-down orientation
- Top-left vertex: Document (the target of assurance)
- Top-right vertex: Guidance (qualitative standard)
- Bottom vertex: Specification (structural standard)

**Coordinates (centered in canvas):**
```
Document:      (100, 60)   - top left
Guidance:      (250, 60)   - top right
Specification: (175, 210)  - bottom center
```

### Visual Encoding

**Vertices (nodes):**
| Vertex | Shape | Size | Fill | Stroke | Label Position |
|--------|-------|------|------|--------|----------------|
| Document | Circle | r=25 | #4A90D9 (blue) | #2E5A87 2px | Inside, white text |
| Specification | Rectangle | 50×35 | #2ECC71 (green) | #1D8348 2px | Inside, white text |
| Guidance | Rounded Rect | 50×35, r=8 | #E67E22 (orange) | #A04000 2px | Inside, white text |

**Edges:**
| Edge | Line Style | Color | Width | Arrow | Label |
|------|-----------|-------|-------|-------|-------|
| Verification | Solid | #2ECC71 | 2.5px | → to Spec | "Verification" |
| Validation | Dashed (5,3) | #E67E22 | 2.5px | → to Guidance | "Validation" |
| Coupling | Double line | #9B59B6 (purple) | 2px each, 3px gap | None | "Coupling" |

**Face (triangle interior):**
- Fill: #F8F9FA (very light gray)
- Opacity: 0.6
- Border: None (edges define boundary)

**Annotations (small text):**
| Near Edge | Text | Font Size | Color |
|-----------|------|-----------|-------|
| Verification | "Structural compliance" | 9pt | #666 |
| Validation | "Quality assessment" | 9pt | #666 |
| Coupling | "Type coherence" | 9pt | #666 |

### Legend
Position: Bottom right, 80×60px box
- Small icons for each edge type with labels
- Font: 8pt sans-serif

---

## Figure 2: INCOSE Paper Audit Chart (Hero Figure)

### Geometry Specification

**Canvas:** 550px × 400px (5.5" × 4" at 100dpi)

**Hierarchical Layout (3 layers):**

```
Layer 2 (Top):     [THIS PAPER]  ← highlighted
                      ↓ ↓
Layer 1 (Middle):  [I-S]    [I-G]
                    ↓ ↓      ↓ ↓
Layer 0 (Bottom):  [SS] [SG] [GS] [GG]
                       \  ↑ /
                        [★]  ← root
```

**Vertex Positions:**
```python
# Layer 2 - The Paper
"v:doc:incose-paper-2026": (275, 50)

# Layer 1 - INCOSE Type Documents
"v:spec:incose-paper":     (175, 140)
"v:guidance:incose-paper": (375, 140)

# Layer 0 - Boundary Complex Foundation
"v:spec:spec":      (75, 250)
"v:spec:guidance":  (175, 250)
"v:guidance:spec":  (275, 250)
"v:guidance:guidance": (375, 250)

# Root (slightly below center of Layer 0)
"b0:root": (225, 340)
```

### Visual Encoding

**Vertices by Type:**
| Type | Shape | Size | Fill | Stroke | Label |
|------|-------|------|------|--------|-------|
| b0:root | Star (6-point) | r=18 | #FFD700 (gold) | #B8860B 2px | "★" |
| v:spec:* | Rectangle | 45×30 | #2ECC71 (green) | #1D8348 2px | Abbrev |
| v:guidance:* | Rounded Rect | 45×30, r=6 | #E67E22 (orange) | #A04000 2px | Abbrev |
| v:doc:* | Circle | r=28 | #3498DB (blue) | #2471A3 3px | "PAPER" |

**Vertex Labels (abbreviated):**
```
b0:root                 → "★"
v:spec:spec            → "SS"
v:spec:guidance        → "SG"
v:guidance:spec        → "GS"
v:guidance:guidance    → "GG"
v:spec:incose-paper    → "I-S"
v:guidance:incose-paper → "I-G"
v:doc:incose-paper-2026 → "PAPER"
```

**Edges by Type:**
| Type | Line Style | Color | Width | Arrow |
|------|-----------|-------|-------|-------|
| verification | Solid | #2ECC71 | 1.5px | → |
| validation | Dashed (4,2) | #E67E22 | 1.5px | → |
| coupling | Solid double | #9B59B6 | 1px×2 | None |
| b1 (boundary) | Dotted (2,2) | #95A5A6 | 1.5px | → |

**Faces (triangular fills):**
| Face ID | Fill | Opacity | Highlight |
|---------|------|---------|-----------|
| b2:spec-spec | #E8F6FF | 0.5 | Blue boundary |
| b2:guidance-guidance | #E8F6FF | 0.5 | Blue boundary |
| f:assurance:spec-guidance | #E8F8E8 | 0.4 | None |
| f:assurance:guidance-spec | #E8F8E8 | 0.4 | None |
| f:assurance:incose-paper-spec | #E8F8E8 | 0.4 | None |
| f:assurance:incose-paper-guidance | #E8F8E8 | 0.4 | None |
| f:assurance:incose-paper-content | #FFF8E8 | 0.6 | Gold border 2px |

**Layer Labels (left margin):**
- "Layer 2: This Paper" at y=50
- "Layer 1: Paper Type" at y=140
- "Layer 0: Foundation" at y=250

**Assurance Indicators:**
- Checkmark (✓) next to each vertex in green
- "100% Coverage" badge in top-right corner

**Statistics Box (bottom-right):**
```
V = 8, E = 20, F = 7
χ = -5
Coverage: 7/7 (100%)
```

---

## Figure 3: Boundary Complex Structure

### Geometry Specification

**Canvas:** 350px × 280px (3.5" × 2.8" at 100dpi)

**Pentagon Layout with Root at Center:**

```
           [SS]  ─────────  [SG]
            │ ╲           ╱ │
            │   ╲   ★   ╱   │
            │     ╲   ╱     │
            │      ╲ ╱      │
           [GS] ─────────  [GG]
```

**Vertex Positions (symmetric pentagon + center):**
```python
# Root at center
"b0:root": (175, 150)

# Four foundational vertices in rectangle around root
"v:spec:spec":         (75, 80)    # top-left
"v:spec:guidance":     (275, 80)   # top-right
"v:guidance:spec":     (75, 220)   # bottom-left
"v:guidance:guidance": (275, 220)  # bottom-right
```

### Visual Encoding

**Vertices:**
| Vertex | Shape | Size | Fill | Stroke |
|--------|-------|------|------|--------|
| b0:root | Star (8-point) | r=22 | #FFD700 | #B8860B 2.5px |
| v:spec:spec | Rectangle | 50×35 | #2ECC71 | #1D8348 2px |
| v:spec:guidance | Rectangle | 50×35 | #2ECC71 | #1D8348 2px |
| v:guidance:spec | Rounded Rect | 50×35, r=8 | #E67E22 | #A04000 2px |
| v:guidance:guidance | Rounded Rect | 50×35, r=8 | #E67E22 | #A04000 2px |

**Vertex Labels:**
```
b0:root             → "ROOT" (inside star)
v:spec:spec         → "Spec-for-Spec" (full, below)
v:spec:guidance     → "Spec-for-Guidance" (full, below)
v:guidance:spec     → "Guidance-for-Spec" (full, above)
v:guidance:guidance → "Guidance-for-Guidance" (full, above)
```

**Edges:**

Standard edges (between foundational vertices):
| From | To | Type | Style |
|------|-----|------|-------|
| SS | GS | coupling | Purple double |
| SG | GG | coupling | Purple double |
| SG | GS | cross-coupling | Purple double |
| SG | SS | verification | Green solid → |
| GS | SG | verification | Green solid → |
| GG | SG | verification | Green solid → |
| SS | GS | validation | Orange dashed → |
| SG | GS | validation | Orange dashed → |
| GS | GG | validation | Orange dashed → |

Boundary edges (to root):
| From | To | Type | Style |
|------|-----|------|-------|
| SS | root | self-verification | Gray dotted → |
| GG | root | self-validation | Gray dotted → |
| root | GS | coupling proxy | Gray dotted ← |
| root | SG | coupling proxy | Gray dotted ← |

**Faces (4 triangles):**
| Face | Vertices | Fill | Label |
|------|----------|------|-------|
| b2:spec-spec | root, GS, SS | #E0F0FF (light blue) | "b2" |
| b2:guidance-guidance | root, SG, GG | #E0F0FF (light blue) | "b2" |
| f:assurance:spec-guidance | SG, SS, GS | #E0FFE0 (light green) | "f" |
| f:assurance:guidance-spec | GS, SG, GG | #E0FFE0 (light green) | "f" |

### Legend
Position: Top-right corner, small box
- "b2: Boundary Face (self-referential)" in blue
- "f: Standard Assurance Face" in green
- Root symbol explanation

---

## Color Palette Summary

| Purpose | Color | Hex | Usage |
|---------|-------|-----|-------|
| Specification | Green | #2ECC71 | Spec vertices, verification edges |
| Guidance | Orange | #E67E22 | Guidance vertices, validation edges |
| Document | Blue | #3498DB / #4A90D9 | Doc vertices, primary focus |
| Coupling | Purple | #9B59B6 | Coupling edges |
| Boundary | Gray | #95A5A6 | Boundary edges |
| Root/Highlight | Gold | #FFD700 | Root vertex, paper highlight |
| Face Fill (standard) | Light Green | #E8F8E8 | Standard assurance faces |
| Face Fill (boundary) | Light Blue | #E0F0FF | Boundary faces |
| Face Fill (paper) | Light Gold | #FFF8E8 | Paper's assurance face |

## Typography

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Vertex Labels (abbrev) | Arial/Helvetica | 11pt | Bold |
| Vertex Labels (full) | Arial/Helvetica | 9pt | Normal |
| Edge Labels | Arial/Helvetica | 9pt | Normal |
| Annotations | Arial/Helvetica | 8pt | Normal |
| Layer Labels | Arial/Helvetica | 10pt | Bold |
| Statistics | Consolas/Monospace | 9pt | Normal |
| Legend | Arial/Helvetica | 8pt | Normal |

## Output Requirements

- Format: SVG (vector, scalable)
- Secondary: PNG at 300 DPI for backup
- Grayscale compatibility: All colors should have sufficient contrast when converted
- Print size: Match specifications (3.5" × 2.8" for Fig 1&3, 5.5" × 4" for Fig 2)
