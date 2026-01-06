#!/usr/bin/env python3
"""
Create interactive 3D visualization of assured-signed charts with accountability-specific color coding.

This specialized visualizer renders assured-signed charts with:
- Semantic layering by architecture tier (boundary → foundation → type → instance)
- Color-coded vertices by role (boundary, spec, guidance, doc, signer)
- Color-coded edges by relationship type (coupling, verification, validation, signs, qualifies)
- Color-coded faces by semantic meaning (assurance vs signature faces)
- Common boundary highlighting (shared validation edges)

Usage:
    python scripts/visualize_assured_signed.py charts/assured-signed-incose/assured-signed-incose.json

Output:
    charts/assured-signed-incose/assured-signed-incose.html
"""

import sys
import json
from pathlib import Path
import plotly.graph_objects as go
import networkx as nx


# Assured-signed color palette
COLORS = {
    # Vertex types
    'boundary': '#FFD700',          # Gold - boundary anchor (b0:root)
    'spec': '#3498db',              # Blue - specification documents
    'guidance': '#2ecc71',          # Green - guidance documents
    'doc': '#9b59b6',               # Purple - content documents
    'signer': '#e67e22',            # Orange - human signers

    # Edge types
    'coupling': '#9b59b6',          # Purple - spec ↔ guidance alignment
    'verification': '#3498db',      # Blue - doc → spec conformance
    'validation': '#2ecc71',        # Green - doc → guidance assessment
    'signs': '#e67e22',             # Orange - signer → doc attestation
    'qualifies': '#1abc9c',         # Teal - signer → guidance credential
    'boundary_edge': '#FFD700',     # Gold - connections to root
    'dependency': '#95a5a6',        # Gray - requirement dependencies

    # Face types
    'assurance': 'rgba(52, 152, 219, 0.5)',     # Blue semi-transparent
    'signature': 'rgba(230, 126, 34, 0.5)',     # Orange semi-transparent
    'boundary_face': 'rgba(255, 215, 0, 0.5)', # Gold semi-transparent

    # Default
    'default': '#95a5a6'            # Gray
}

# Layer heights for semantic positioning
LAYER_Z = {
    'boundary': 0.0,     # Bottom layer - root anchor
    'foundation': 0.5,   # Foundation specs and guidances (SS, SG, GS, GG)
    'type': 1.0,         # Type-specific specs and guidances
    'instance': 1.5,     # Content documents
    'accountability': 1.3,  # Signers (slightly below instance)
}


def load_chart_json(json_path: Path) -> dict:
    """Load chart JSON data."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_vertex_type_category(vertex: dict) -> str:
    """Get vertex category for color coding."""
    v_id = vertex.get('id', '')
    vtype = vertex.get('type', '')

    # Check ID patterns first (more specific)
    if v_id.startswith('b0:') or v_id == 'b0:root':
        return 'boundary'
    elif v_id.startswith('v:signer:'):
        return 'signer'
    elif v_id.startswith('v:spec:'):
        return 'spec'
    elif v_id.startswith('v:guidance:'):
        return 'guidance'
    elif v_id.startswith('v:doc:'):
        return 'doc'

    # Fall back to type check
    if 'signer' in vtype:
        return 'signer'
    elif 'spec' in vtype:
        return 'spec'
    elif 'guidance' in vtype:
        return 'guidance'
    elif 'doc' in vtype:
        return 'doc'
    elif 'boundary' in vtype:
        return 'boundary'

    return 'default'


def get_vertex_layer(vertex: dict) -> str:
    """Determine which architectural layer a vertex belongs to."""
    v_id = vertex.get('id', '')

    # Boundary anchor
    if v_id.startswith('b0:'):
        return 'boundary'

    # Foundation layer - the four core vertices
    foundation_ids = [
        'v:spec:spec', 'v:spec:guidance',
        'v:guidance:spec', 'v:guidance:guidance'
    ]
    if v_id in foundation_ids:
        return 'foundation'

    # Signers
    if v_id.startswith('v:signer:'):
        return 'accountability'

    # Content documents (not spec or guidance)
    if v_id.startswith('v:doc:'):
        return 'instance'

    # Type-specific specs and guidances
    if v_id.startswith('v:spec:') or v_id.startswith('v:guidance:'):
        return 'type'

    return 'foundation'  # Default


def get_edge_type_category(edge: dict) -> str:
    """Get edge category for color coding."""
    etype = edge.get('type', '')
    e_id = edge.get('id', '')

    # Check ID patterns first
    if e_id.startswith('b1:'):
        return 'boundary_edge'
    elif e_id.startswith('e:coupling:'):
        return 'coupling'
    elif e_id.startswith('e:verification:'):
        return 'verification'
    elif e_id.startswith('e:validation:'):
        return 'validation'
    elif e_id.startswith('e:signs:'):
        return 'signs'
    elif e_id.startswith('e:qualifies:'):
        return 'qualifies'
    elif e_id.startswith('e:dependency:'):
        return 'dependency'

    # Fall back to type check
    if 'coupling' in etype:
        return 'coupling'
    elif 'verification' in etype:
        return 'verification'
    elif 'validation' in etype:
        return 'validation'
    elif 'signs' in etype:
        return 'signs'
    elif 'qualifies' in etype:
        return 'qualifies'
    elif 'boundary' in etype:
        return 'boundary_edge'

    return 'default'


def get_face_type_category(face: dict) -> str:
    """Get face category for color coding."""
    ftype = face.get('type', '')
    f_id = face.get('id', '')

    # Check ID patterns
    if f_id.startswith('b2:'):
        return 'boundary_face'
    elif f_id.startswith('f:signature:'):
        return 'signature'
    elif f_id.startswith('f:assurance:'):
        return 'assurance'

    # Fall back to type check
    if 'signature' in ftype:
        return 'signature'
    elif 'assurance' in ftype:
        return 'assurance'
    elif 'boundary' in ftype:
        return 'boundary_face'

    return 'default'


def extract_short_label(vertex: dict) -> str:
    """Extract clear, readable label for vertex - longer names for static snapshots."""
    v_id = vertex['id']
    name = vertex.get('name', '')

    # Explicit label mapping for all known vertex types
    # Using clear, descriptive names that work without hover
    labels = {
        # Boundary
        'b0:root': 'ROOT',

        # Foundation layer - use standard abbreviations
        'v:spec:spec': 'Spec-for-Spec',
        'v:spec:guidance': 'Spec-for-Guidance',
        'v:guidance:spec': 'Guidance-for-Spec',
        'v:guidance:guidance': 'Guidance-for-Guidance',

        # INCOSE paper type layer
        'v:spec:incose-paper': 'Spec: Paper',
        'v:guidance:incose-paper': 'Guidance: Paper',
        'v:spec:incose-self-demonstration': 'Spec: Self-Demo',
        'v:guidance:incose-self-demonstration': 'Guidance: Self-Demo',

        # Supporting document types
        'v:spec:architecture': 'Spec: Architecture',
        'v:guidance:architecture': 'Guidance: Architecture',
        'v:spec:lifecycle': 'Spec: Lifecycle',
        'v:guidance:lifecycle': 'Guidance: Lifecycle',
        'v:spec:incose-literature-review': 'Spec: Lit Review',
        'v:guidance:incose-literature-review': 'Guidance: Lit Review',
        'v:spec:novel-contributions': 'Spec: Novel Contrib',
        'v:guidance:novel-contributions': 'Guidance: Novel Contrib',

        # Supporting document instances
        'v:doc:architecture-incose-paper': 'Doc: Architecture',
        'v:doc:lifecycle-incose-paper': 'Doc: Lifecycle',
        'v:doc:literature-review-incose-paper': 'Doc: Lit Review',
        'v:doc:novel-contributions-incose-paper': 'Doc: Novel Contrib',

        # The paper itself
        'v:doc:incose-paper-2026': 'THE PAPER',

        # Chart infrastructure (if included)
        'v:spec:chart': 'Spec: Chart',
        'v:guidance:chart': 'Guidance: Chart',
        'v:spec:assurance_audit': 'Spec: Audit',
        'v:guidance:assurance_audit': 'Guidance: Audit',
    }

    if v_id in labels:
        return labels[v_id]

    # Signer vertices - show as @username
    if v_id.startswith('v:signer:'):
        username = v_id.split(':')[-1]
        return f"Signer: @{username}"

    # Generic fallback based on ID structure
    parts = v_id.split(':')
    if len(parts) >= 3:
        vtype = parts[1]  # spec, guidance, doc, signer
        vname = parts[2].replace('-', ' ').title()

        # Truncate long names intelligently
        if len(vname) > 20:
            words = vname.split()
            if len(words) > 2:
                vname = ' '.join(words[:2])

        type_prefix = {
            'spec': 'Spec:',
            'guidance': 'Guide:',
            'doc': 'Doc:',
            'signer': 'Signer:'
        }.get(vtype, '')

        return f"{type_prefix} {vname}" if type_prefix else vname

    # Ultimate fallback - use the full name, truncated
    if name:
        if len(name) > 25:
            return name[:22] + '...'
        return name

    return v_id.split(':')[-1]


def build_network_graph(chart_data: dict) -> nx.MultiDiGraph:
    """Build NetworkX graph for layout computation."""
    G = nx.MultiDiGraph()

    # Add vertices
    for vertex in chart_data['elements']['vertices']:
        G.add_node(vertex['id'], **vertex)

    # Add edges
    for edge in chart_data['elements']['edges']:
        G.add_edge(edge['source'], edge['target'], **edge)

    return G


def compute_layered_3d_layout(G: nx.MultiDiGraph, chart_data: dict) -> dict:
    """Compute 3D layout with semantic layering by architecture tier."""
    # Start with spring layout for x,y positioning
    G_undirected = G.to_undirected()
    pos_2d = nx.spring_layout(
        G_undirected,
        dim=2,
        seed=42,
        k=0.6,
        iterations=80
    )

    # Build vertex lookup for layer assignment
    vertex_lookup = {v['id']: v for v in chart_data['elements']['vertices']}

    # Assign z-coordinate based on layer
    pos_3d = {}
    for v_id, (x, y) in pos_2d.items():
        vertex = vertex_lookup.get(v_id, {'id': v_id})
        layer = get_vertex_layer(vertex)
        z = LAYER_Z.get(layer, 0.5)

        # Add small jitter within layer to avoid overlapping
        import random
        random.seed(hash(v_id) % 2**32)
        z += random.uniform(-0.05, 0.05)

        pos_3d[v_id] = (x, y, z)

    return pos_3d


def create_edge_legend_html() -> str:
    """Create HTML legend for edge types."""
    legend_items = [
        ('coupling', COLORS['coupling'], 'Spec ↔ Guidance alignment'),
        ('verification', COLORS['verification'], 'Doc → Spec conformance'),
        ('validation', COLORS['validation'], 'Doc → Guidance assessment'),
        ('signs', COLORS['signs'], 'Signer → Doc attestation'),
        ('qualifies', COLORS['qualifies'], 'Signer → Guidance credential'),
        ('dependency', COLORS['dependency'], 'Doc → Doc citation/requirement'),
        ('boundary', COLORS['boundary_edge'], 'Connection to root'),
    ]

    html = '<div style="position: absolute; top: 120px; right: 20px; background: rgba(255,255,255,0.95); padding: 15px; border-radius: 8px; font-family: Arial; font-size: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); border: 1px solid #ddd;">'
    html += '<div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #ddd; padding-bottom: 6px; color: #2c3e50;">Edge Types</div>'

    for label, color, description in legend_items:
        html += f'<div style="margin: 6px 0; display: flex; align-items: center;">'
        html += f'<div style="width: 24px; height: 3px; background: {color}; margin-right: 10px; border-radius: 2px;"></div>'
        html += f'<span style="color: #333;"><b>{label}</b>: {description}</span>'
        html += '</div>'

    html += '</div>'
    return html


def create_face_legend_html() -> str:
    """Create HTML legend for face types."""
    legend_items = [
        ('Assurance', '#3498db', 'Doc + Spec + Guidance triangle'),
        ('Signature', '#e67e22', 'Doc + Guidance + Signer triangle'),
        ('Boundary', '#FFD700', 'Self-referential foundation'),
    ]

    html = '<div style="position: absolute; top: 340px; right: 20px; background: rgba(255,255,255,0.95); padding: 15px; border-radius: 8px; font-family: Arial; font-size: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); border: 1px solid #ddd;">'
    html += '<div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #ddd; padding-bottom: 6px; color: #2c3e50;">Face Types</div>'

    for label, color, description in legend_items:
        html += f'<div style="margin: 6px 0; display: flex; align-items: center;">'
        html += f'<div style="width: 20px; height: 16px; background: {color}; opacity: 0.6; margin-right: 10px; border-radius: 3px;"></div>'
        html += f'<span style="color: #333;"><b>{label}</b>: {description}</span>'
        html += '</div>'

    html += '</div>'
    return html


def create_vertex_legend_html() -> str:
    """Create HTML legend for vertex types."""
    legend_items = [
        ('Boundary', COLORS['boundary'], 'Root anchor (b0:root)'),
        ('Spec', COLORS['spec'], 'Specification documents'),
        ('Guidance', COLORS['guidance'], 'Guidance documents'),
        ('Doc', COLORS['doc'], 'Content documents'),
        ('Signer', COLORS['signer'], 'Human signers'),
    ]

    html = '<div style="position: absolute; top: 500px; right: 20px; background: rgba(255,255,255,0.95); padding: 15px; border-radius: 8px; font-family: Arial; font-size: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); border: 1px solid #ddd;">'
    html += '<div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #ddd; padding-bottom: 6px; color: #2c3e50;">Vertex Types</div>'

    for label, color, description in legend_items:
        html += f'<div style="margin: 6px 0; display: flex; align-items: center;">'
        html += f'<div style="width: 14px; height: 14px; background: {color}; margin-right: 10px; border-radius: 50%; border: 2px solid white; box-shadow: 0 1px 2px rgba(0,0,0,0.2);"></div>'
        html += f'<span style="color: #333;"><b>{label}</b>: {description}</span>'
        html += '</div>'

    html += '</div>'
    return html


def create_layer_legend_html() -> str:
    """Create HTML legend for architectural layers."""
    html = '<div style="position: absolute; top: 680px; right: 20px; background: rgba(255,255,255,0.95); padding: 15px; border-radius: 8px; font-family: Arial; font-size: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); border: 1px solid #ddd;">'
    html += '<div style="font-weight: bold; margin-bottom: 10px; border-bottom: 1px solid #ddd; padding-bottom: 6px; color: #2c3e50;">Architecture Layers</div>'
    html += '<div style="margin: 6px 0; color: #333;">↑ <b>Instance</b> - Content docs</div>'
    html += '<div style="margin: 6px 0; color: #333;">↑ <b>Accountability</b> - Signers</div>'
    html += '<div style="margin: 6px 0; color: #333;">↑ <b>Type</b> - Type specs/guidance</div>'
    html += '<div style="margin: 6px 0; color: #333;">↑ <b>Foundation</b> - SS, SG, GS, GG</div>'
    html += '<div style="margin: 6px 0; color: #333;">↓ <b>Boundary</b> - Root anchor</div>'
    html += '</div>'
    return html


def create_visualization(chart_data: dict) -> go.Figure:
    """Create 3D Plotly visualization with assured-signed styling."""
    # Build graph and compute layout
    G = build_network_graph(chart_data)
    pos_3d = compute_layered_3d_layout(G, chart_data)

    # Create figure
    fig = go.Figure()

    # Add edges as colored lines
    edge_traces = []
    for edge in chart_data['elements']['edges']:
        source_id = edge['source']
        target_id = edge['target']

        if source_id in pos_3d and target_id in pos_3d:
            x0, y0, z0 = pos_3d[source_id]
            x1, y1, z1 = pos_3d[target_id]

            # Get edge type and color
            edge_category = get_edge_type_category(edge)
            edge_color = COLORS.get(edge_category, COLORS['default'])

            # Variable line width by importance
            line_width = 4
            if edge_category in ['signs', 'qualifies']:
                line_width = 5  # Accountability edges slightly thicker
            elif edge_category == 'coupling':
                line_width = 3  # Coupling edges slightly thinner

            # Extract edge type for display
            edge_type = edge['type'].split('/')[-1] if '/' in edge['type'] else edge['type']

            trace = go.Scatter3d(
                x=[x0, x1],
                y=[y0, y1],
                z=[z0, z1],
                mode='lines',
                line=dict(width=line_width, color=edge_color),
                hovertext=f"<b>{edge_type}</b><br>{edge['name']}<br>ID: {edge['id']}",
                hoverinfo='text',
                showlegend=False
            )
            edge_traces.append(trace)

    for trace in edge_traces:
        fig.add_trace(trace)

    # Add vertices as colored scatter points
    vertex_x = []
    vertex_y = []
    vertex_z = []
    vertex_text = []
    vertex_colors = []
    vertex_hover = []
    vertex_sizes = []

    for vertex in chart_data['elements']['vertices']:
        v_id = vertex['id']
        if v_id in pos_3d:
            x, y, z = pos_3d[v_id]
            vertex_x.append(x)
            vertex_y.append(y)
            vertex_z.append(z)

            # Get short label
            short_name = extract_short_label(vertex)
            vertex_text.append(short_name)

            # Get color by vertex category
            vertex_category = get_vertex_type_category(vertex)
            vertex_color = COLORS.get(vertex_category, COLORS['default'])
            vertex_colors.append(vertex_color)

            # Size by importance
            size = 14
            if vertex_category == 'boundary':
                size = 18  # Root is largest
            elif vertex_category == 'signer':
                size = 16  # Signers prominent
            elif vertex_category == 'doc':
                size = 15  # Documents slightly larger

            vertex_sizes.append(size)

            # Get layer for hover
            layer = get_vertex_layer(vertex)

            # Extract type for display
            vtype = vertex['type'].split('/')[-1] if '/' in vertex['type'] else vertex['type']

            vertex_hover.append(
                f"<b>{vertex['name']}</b><br>"
                f"Type: {vtype}<br>"
                f"Layer: {layer}<br>"
                f"ID: {vertex['id']}"
            )

    vertex_trace = go.Scatter3d(
        x=vertex_x,
        y=vertex_y,
        z=vertex_z,
        mode='markers+text',
        marker=dict(
            size=vertex_sizes,
            color=vertex_colors,
            line=dict(width=2, color='white'),
            opacity=0.95
        ),
        text=vertex_text,
        textposition='top center',
        textfont=dict(size=11, color='black', family='Arial Black'),
        hovertext=vertex_hover,
        hoverinfo='text',
        name='Vertices'
    )
    fig.add_trace(vertex_trace)

    # Add faces as semi-transparent colored triangular meshes
    for face in chart_data['elements']['faces']:
        face_vertices = face.get('vertices', [])

        # Only render triangular faces (3 vertices)
        if len(face_vertices) == 3:
            # Get positions of all three vertices
            positions = []
            valid = True
            for v_id in face_vertices:
                if v_id in pos_3d:
                    positions.append(pos_3d[v_id])
                else:
                    valid = False
                    break

            if valid and len(positions) == 3:
                x_coords = [p[0] for p in positions]
                y_coords = [p[1] for p in positions]
                z_coords = [p[2] for p in positions]

                # Get face color by type
                face_category = get_face_type_category(face)

                # Use RGBA colors for faces
                if face_category == 'signature':
                    face_color = COLORS['signature']
                    opacity = 0.55
                elif face_category == 'boundary_face':
                    face_color = COLORS['boundary_face']
                    opacity = 0.45
                else:  # assurance
                    face_color = COLORS['assurance']
                    opacity = 0.5

                # Extract face type for display
                ftype = face['type'].split('/')[-1] if '/' in face['type'] else face['type']

                mesh_trace = go.Mesh3d(
                    x=x_coords,
                    y=y_coords,
                    z=z_coords,
                    i=[0],
                    j=[1],
                    k=[2],
                    color=face_color,
                    opacity=opacity,
                    hovertext=f"<b>{ftype}</b><br>{face['name']}<br>ID: {face['id']}",
                    hoverinfo='text',
                    showlegend=False
                )
                fig.add_trace(mesh_trace)

    # Update layout with assured-signed styling
    title_text = f"<b>{chart_data['name']}</b>"
    if chart_data.get('description'):
        desc = chart_data['description']
        if len(desc) > 80:
            desc = desc[:77] + '...'
        title_text += f"<br><sub style='color: #7f8c8d;'>{desc}</sub>"

    euler_char = chart_data['topology']['euler_characteristic']
    v_count = chart_data['element_counts']['vertices']
    e_count = chart_data['element_counts']['edges']
    f_count = chart_data['element_counts']['faces']

    # Count face types for metadata (b2 boundary faces count as assurance)
    assurance_count = sum(1 for f in chart_data['elements']['faces']
                          if get_face_type_category(f) in ('assurance', 'boundary_face'))
    signature_count = sum(1 for f in chart_data['elements']['faces']
                          if get_face_type_category(f) == 'signature')

    fig.update_layout(
        title=dict(
            text=title_text,
            x=0.5,
            xanchor='center',
            font=dict(size=20, family='Arial')
        ),
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            zaxis=dict(showgrid=False, zeroline=False, visible=False, title='Layer'),
            bgcolor='#f8f9fa',
            camera=dict(
                eye=dict(x=1.6, y=1.6, z=1.0)  # Angle showing layered structure
            )
        ),
        showlegend=False,
        width=1500,
        height=950,
        margin=dict(l=0, r=320, t=100, b=0),
        paper_bgcolor='#ffffff',
        annotations=[
            # Topology info
            dict(
                text=(
                    f"<b>Topology:</b> V={v_count}, E={e_count}, F={f_count}, χ={euler_char}<br>"
                    f"<b>Faces:</b> {assurance_count} assurance, {signature_count} signature"
                ),
                xref="paper",
                yref="paper",
                x=0.02,
                y=0.98,
                showarrow=False,
                font=dict(size=13, color='#2c3e50', family='Arial'),
                bgcolor='rgba(255, 255, 255, 0.95)',
                borderpad=10,
                bordercolor='#bdc3c7',
                borderwidth=1,
                align='left'
            ),
        ]
    )

    return fig


def add_legends_to_html(html_path: Path):
    """Add interactive legends to the HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Add all legends before closing body tag
    edge_legend = create_edge_legend_html()
    face_legend = create_face_legend_html()
    vertex_legend = create_vertex_legend_html()
    layer_legend = create_layer_legend_html()

    legends = f'{edge_legend}{face_legend}{vertex_legend}{layer_legend}'
    html_content = html_content.replace('</body>', f'{legends}</body>')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)


def main():
    """Generate assured-signed visualization from chart JSON."""
    if len(sys.argv) < 2:
        print("Usage: python scripts/visualize_assured_signed.py charts/<chart>/<chart>.json")
        sys.exit(1)

    json_path = Path(sys.argv[1])

    if not json_path.exists():
        print(f"Error: JSON file not found: {json_path}")
        print(f"Run: python scripts/export_chart_direct.py {json_path.with_suffix('.md')} first")
        sys.exit(1)

    # Load chart data
    print(f"Loading: {json_path.name}")
    chart_data = load_chart_json(json_path)

    # Verify this looks like an assured-signed chart
    chart_type = chart_data.get('type', '')
    if 'assured_signed' not in chart_type and 'assurance' not in chart_type:
        print(f"Note: Chart type is '{chart_type}'")
        print("This visualizer is optimized for assured-signed/assurance charts. Continuing...")

    # Create visualization
    print(f"Creating assured-signed visualization...")
    fig = create_visualization(chart_data)

    # Save HTML
    output_path = json_path.with_suffix('.html')
    fig.write_html(str(output_path))

    # Add legends
    print(f"Adding interactive legends...")
    add_legends_to_html(output_path)

    # Summary
    v_count = chart_data['element_counts']['vertices']
    e_count = chart_data['element_counts']['edges']
    f_count = chart_data['element_counts']['faces']

    print(f"\n✓ Visualization saved to: {output_path}")
    print(f"  Open in browser to view interactive 3D accountability complex")
    print(f"  Elements: {v_count} vertices, {e_count} edges, {f_count} faces")
    print(f"  Color coding: Specs (blue), Guidance (green), Docs (purple), Signers (orange)")
    print(f"  Faces: Assurance (blue), Signature (orange), Boundary (gold)")


if __name__ == '__main__':
    main()
