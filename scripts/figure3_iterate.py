#!/usr/bin/env python3
"""
Figure 3: Boundary Complex Structure - Iterative refinement

Shows the 5-vertex self-referential foundation with root anchor.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, RegularPolygon, Polygon, FancyArrowPatch
from matplotlib.lines import Line2D
from pathlib import Path

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
})

COLORS = {
    'spec': '#27AE60',
    'guidance': '#E67E22',
    'root': '#F1C40F',
    'verification': '#27AE60',
    'validation': '#E74C3C',
    'coupling': '#8E44AD',
    'boundary': '#95A5A6',
    'face_standard': '#E8F8F5',
    'face_boundary': '#EBF5FB',
    'text': '#2C3E50',
}


def generate_figure3_v1(output_path: Path):
    """
    Version 1: Original 2D layout with root at center (kept for reference)
    """
    pass


def generate_figure3_v2(output_path: Path):
    """
    Version 2: Hierarchical layer style matching Figure 2

    Layout:
        Layer 1 (Spec Type):       [SS]  --------  [SG]
                                     \              /
                                      \            /
        Layer 0 (Guidance Type):   [GS]  --------  [GG]
                                      \            /
                                       \          /
        Anchor:                         [ROOT]

    This is the self-referential boundary complex showing how specs and
    guidance documents verify/validate each other with root anchor.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Y positions for hierarchical layers
    y1 = 0.78  # Layer 1: Spec type vertices
    y0 = 0.48  # Layer 0: Guidance type vertices
    yr = 0.18  # Root anchor

    # Positions
    positions = {
        'ss': (0.25, y1),    # Spec-for-Spec
        'sg': (0.75, y1),    # Spec-for-Guidance
        'gs': (0.25, y0),    # Guidance-for-Spec
        'gg': (0.75, y0),    # Guidance-for-Guidance
        'root': (0.5, yr),   # Root anchor
    }

    labels = {
        'ss': 'SS',
        'sg': 'SG',
        'gs': 'GS',
        'gg': 'GG',
        'root': 'ROOT',
    }

    # Draw layer backgrounds (matching Figure 2 style)
    layer_boxes = [
        (0.03, y1-0.10, 0.94, 0.20, 'Layer 1: Spec Type', COLORS['face_standard']),
        (0.03, y0-0.10, 0.94, 0.20, 'Layer 0: Guidance Type', COLORS['face_boundary']),
        (0.03, yr-0.08, 0.94, 0.16, 'Anchor', '#F5F5F5'),
    ]

    for x, y, w, h, label, color in layer_boxes:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.02",
                               facecolor=color, edgecolor='#CCCCCC', linewidth=1, alpha=0.6)
        ax.add_patch(rect)
        ax.text(0.04, y + h - 0.02, label, fontsize=9, fontweight='bold',
                color='#666666', va='top')

    # Helper functions
    def draw_arrow(start, end, color, style='-', width=2):
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='-|>', color=color,
                                  linewidth=width, linestyle=style,
                                  shrinkA=15, shrinkB=15))

    def draw_line(start, end, color, style='-', width=2):
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=width,
                linestyle=style, zorder=1)

    # EDGES - draw from bottom to top for proper layering

    # Boundary edges to root (dotted gray)
    draw_arrow('ss', 'root', COLORS['boundary'], ':', 1.5)
    draw_arrow('gg', 'root', COLORS['boundary'], ':', 1.5)
    draw_line('root', 'gs', COLORS['boundary'], ':', 1.5)
    draw_line('root', 'sg', COLORS['boundary'], ':', 1.5)

    # Coupling edges (purple solid) - between paired types
    draw_line('ss', 'gs', COLORS['coupling'], '-', 2)  # spec-for-spec ↔ guidance-for-spec
    draw_line('sg', 'gg', COLORS['coupling'], '-', 2)  # spec-for-guidance ↔ guidance-for-guidance
    draw_line('sg', 'gs', COLORS['coupling'], '-', 2)  # Cross-coupling

    # Verification edges (green - directed)
    # SG verifies SS (spec-for-guidance verifies spec-for-spec)
    draw_arrow('sg', 'ss', COLORS['verification'], '-', 2)
    # GS verifies SG (guidance-for-spec verifies spec-for-guidance)
    draw_arrow('gs', 'sg', COLORS['verification'], '-', 2)
    # GG verifies SG (guidance-for-guidance verifies spec-for-guidance)
    draw_arrow('gg', 'sg', COLORS['verification'], '-', 2)

    # Validation edges (red - directed, dashed)
    # SS validates GS (spec-for-spec validates guidance-for-spec)
    draw_arrow('ss', 'gs', COLORS['validation'], '--', 2)
    # SG validates GS (spec-for-guidance validates guidance-for-spec)
    draw_arrow('sg', 'gs', COLORS['validation'], '--', 2)
    # GS validates GG (guidance-for-spec validates guidance-for-guidance)
    draw_arrow('gs', 'gg', COLORS['validation'], '--', 2)

    # VERTICES - draw on top
    vertex_size = 0.05

    # Spec vertices (green squares) - Layer 1
    for v in ['ss', 'sg']:
        x, y = positions[v]
        rect = FancyBboxPatch((x - vertex_size/2, y - vertex_size/2),
                               vertex_size, vertex_size,
                               boxstyle="round,pad=0.005,rounding_size=0.005",
                               facecolor=COLORS['spec'], edgecolor='white',
                               linewidth=2, zorder=10)
        ax.add_patch(rect)
        ax.text(x, y, labels[v], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=11)

    # Guidance vertices (orange rounded) - Layer 0
    for v in ['gs', 'gg']:
        x, y = positions[v]
        rect = FancyBboxPatch((x - vertex_size/2, y - vertex_size/2),
                               vertex_size, vertex_size,
                               boxstyle="round,pad=0.005,rounding_size=0.015",
                               facecolor=COLORS['guidance'], edgecolor='white',
                               linewidth=2, zorder=10)
        ax.add_patch(rect)
        ax.text(x, y, labels[v], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=11)

    # Root (gold hexagon)
    root_x, root_y = positions['root']
    star = RegularPolygon((root_x, root_y), numVertices=6, radius=0.045,
                          facecolor=COLORS['root'], edgecolor='#B7950B',
                          linewidth=2, zorder=10)
    ax.add_patch(star)
    ax.text(root_x, root_y, 'R', ha='center', va='center',
            fontsize=12, fontweight='bold', color='#7D6608', zorder=11)

    # Checkmarks - matching Figure 2 style (green circles with white check)
    for v, pos in positions.items():
        x, y = pos
        # Green circle background
        check_circle = Circle((x + 0.055, y + 0.03), 0.018, facecolor=COLORS['verification'],
                              edgecolor='white', linewidth=1, zorder=12)
        ax.add_patch(check_circle)
        # White "v" as checkmark
        ax.plot([x + 0.048, x + 0.055, x + 0.065], [y + 0.03, y + 0.022, y + 0.042],
                color='white', linewidth=2, solid_capstyle='round', zorder=13)

    # Full labels below vertices
    full_labels_text = [
        (positions['ss'][0], positions['ss'][1] - 0.055, 'spec-for-spec', 7),
        (positions['sg'][0], positions['sg'][1] - 0.055, 'spec-for-guidance', 7),
        (positions['gs'][0], positions['gs'][1] - 0.055, 'guidance-for-spec', 7),
        (positions['gg'][0], positions['gg'][1] - 0.055, 'guidance-for-guidance', 7),
    ]
    for x, y, text, size in full_labels_text:
        ax.text(x, y, text, ha='center', va='top', fontsize=size,
                color='#666666', fontstyle='italic')

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=2.5, marker='>',
               markersize=7, label='Verification (structural)'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=2.5, linestyle='--',
               marker='>', markersize=7, label='Validation (qualitative)'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=2.5,
               label='Coupling (type coherence)'),
        Line2D([0], [0], color=COLORS['boundary'], linewidth=2, linestyle=':',
               label='Boundary (to root)'),
    ]
    leg = ax.legend(handles=legend_elements, loc='upper right', framealpha=0.95,
                    fontsize=9, frameon=True, fancybox=True)
    leg.get_frame().set_edgecolor('#CCCCCC')

    # Statistics box
    stats_text = "V = 5   E = 12   F = 4\nEuler char. = -3"
    ax.text(0.97, 0.02, stats_text, transform=ax.transAxes, fontsize=9,
            ha='right', va='bottom', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.95,
                      edgecolor='#CCCCCC', pad=0.5))

    # Title
    ax.set_title('Boundary Complex Structure', fontsize=15, fontweight='bold',
                 pad=12, color=COLORS['text'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


if __name__ == '__main__':
    output_dir = Path('figures')
    output_dir.mkdir(exist_ok=True)
    generate_figure3_v2(output_dir / 'figure3-v2.png')
    generate_figure3_v2(output_dir / 'figure3-final.png')
    generate_figure3_v2(output_dir / 'figure3-final.pdf')
