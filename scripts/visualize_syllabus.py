#!/usr/bin/env python3
"""
Create interactive 3D visualization of syllabus charts with learning journey-specific color coding.

This specialized visualizer renders learning journey charts with:
- Color-coded vertices by role (students, skills, modules)
- Color-coded edges by relationship type (has-skill, requires-skill, studies, etc.)
- Color-coded faces by semantic meaning (prerequisite, completion, skill-gain)
- Meaningful labels showing learning progression

Usage:
    python scripts/visualize_syllabus.py charts/learning-journey-module-01/learning-journey-module-01.json

Output:
    charts/learning-journey-module-01/learning-journey-module-01.html
"""

import sys
import json
from pathlib import Path
import plotly.graph_objects as go
import networkx as nx


# Learning journey color palette
COLORS = {
    # Vertex types
    'student': '#3498db',           # Blue - student learning states
    'skill': '#2ecc71',             # Green - skills to acquire
    'learning_module': '#9b59b6',   # Purple - learning modules
    'actor': '#3498db',             # Blue - actors (students extend actor)
    'property': '#2ecc71',          # Green - properties (skills extend property)

    # Edge types
    'has_skill': '#27ae60',         # Dark green - student possesses skill
    'requires_skill': '#e67e22',    # Orange - module requires skill
    'develops_skill': '#8e44ad',    # Dark purple - module develops skill
    'studies': '#3498db',           # Blue - student studies module
    'transitions_to': '#16a085',    # Teal - student state transition
    'advances': '#9b59b6',          # Purple - module advances student (from completion)

    # Face types
    'prerequisite': '#f39c12',      # Orange - prerequisite validation
    'completion': '#3498db',        # Blue - state transition
    'skill_gain': '#27ae60',        # Dark green - skill acquisition

    # Default
    'default': '#95a5a6'            # Gray
}


def load_chart_json(json_path: Path) -> dict:
    """Load chart JSON data."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_vertex_type_category(vertex: dict) -> str:
    """Get vertex category for color coding."""
    vtype = vertex.get('type', '')

    if 'student' in vtype:
        return 'student'
    elif 'skill' in vtype:
        return 'skill'
    elif 'learning-module' in vtype or 'learning_module' in vtype:
        return 'learning_module'
    elif 'actor' in vtype:
        return 'actor'
    elif 'property' in vtype:
        return 'property'
    else:
        return 'default'


def get_edge_type_category(edge: dict) -> str:
    """Get edge category for color coding."""
    etype = edge.get('type', '')

    if 'has-skill' in etype:
        return 'has_skill'
    elif 'requires-skill' in etype:
        return 'requires_skill'
    elif 'develops-skill' in etype:
        return 'develops_skill'
    elif 'studies' in etype:
        return 'studies'
    elif 'transitions-to' in etype:
        return 'transitions_to'
    elif 'advances' in etype:
        return 'advances'
    else:
        return 'default'


def get_face_type_category(face: dict) -> str:
    """Get face category for color coding."""
    ftype = face.get('type', '')

    if 'prerequisite' in ftype:
        return 'prerequisite'
    elif 'completion' in ftype:
        return 'completion'
    elif 'skill-gain' in ftype or 'skill_gain' in ftype:
        return 'skill_gain'
    else:
        return 'default'


def extract_short_label(vertex: dict) -> str:
    """Extract meaningful short label for vertex."""
    v_id = vertex['id']
    name = vertex.get('name', '')

    # Student vertices: use last word (beginner, foundational, etc.)
    if 'student' in v_id:
        # Extract learning state name
        parts = v_id.split(':')
        if len(parts) >= 3:
            state_name = parts[2]
            # Convert kebab-case to readable
            readable = state_name.replace('-', ' ').title()
            # Use initials if too long
            if len(readable) > 18:
                words = readable.split()
                if len(words) > 1:
                    return ''.join(w[0] for w in words)
            return readable
        return name.split()[-1] if name else 'Student'

    # Skill vertices: use descriptive short name
    elif 'skill' in v_id:
        # Extract skill name
        parts = v_id.split(':')
        if len(parts) >= 3:
            skill_name = parts[2]
            # Convert kebab-case to readable, shorten if needed
            readable = skill_name.replace('-', ' ').title()
            # Use abbreviation for common patterns
            if 'basic' in readable.lower():
                readable = readable.replace('Basic ', '')
            # Smart abbreviations for long skill names
            abbreviations = {
                'Composing Typed Simplicial Complexes': 'Composition',
                'Typed Simplicial Complexes': 'Typed SC',
                'Simplicial Complex Fundamentals': 'SC Fundamentals',
                'Verification Validation': 'V&V',
                'Assurance Audits': 'Assurance',
                'Document Composition': 'Doc Composition',
                'Reference Reuse': 'Ref & Reuse',
                'Team Coordination': 'Coordination',
                'Resource Management': 'Resources',
                'Topological Data Analysis': 'TDA',
                'Organizational Design Analysis': 'Org Analysis',
                'Sets And Graphs': 'Sets & Graphs',
            }
            if readable in abbreviations:
                return abbreviations[readable]
            if len(readable) > 18:
                words = readable.split()
                if len(words) > 2:
                    # Take first letters of all but last word, keep last word
                    return ''.join(w[0] for w in words[:-1]) + ' ' + words[-1]
            return readable
        return name.split()[-1] if name else 'Skill'

    # Module vertices: use meaningful abbreviations
    elif 'learning-module' in v_id or 'module' in v_id:
        parts = v_id.split(':')
        if len(parts) >= 3:
            module_name = parts[2]
            # Convert to readable
            readable = module_name.replace('-', ' ').title()
            # Smart abbreviations for module names
            abbreviations = {
                'Simplicial Complex Fundamentals': 'M01: SC Basics',
                'Typed Simplicial Complexes': 'M02: Typed SC',
                'Composing Typed Simplicial Complexes': 'M03: Composition',
                'Verification Validation': 'M04: V&V',
                'Assurance Audits': 'M05: Assurance',
                'Document Composition': 'M06: Doc Arch',
                'Reference Reuse': 'M07: Doc-Kits',
                'Team Coordination': 'M08: Teams',
                'Resource Management': 'M09: Resources',
                'Organizational Topology': 'M10: Org Topology',
            }
            if readable in abbreviations:
                return abbreviations[readable]
            # Fallback: shorten common patterns
            if 'simplicial' in readable.lower():
                readable = readable.replace('Simplicial Complex', 'SC')
            if 'typed' in readable.lower() and 'simplicial' in readable.lower():
                readable = 'Typed SC'
            if len(readable) > 18:
                words = readable.split()
                if len(words) >= 2:
                    # Use first word + initials
                    return words[0] + ' ' + ''.join(w[0] for w in words[1:])
            return readable
        return 'Module'

    # Default: use last part of name
    return name.split()[-1] if ' ' in name else name[:12]


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


def compute_3d_layout(G: nx.MultiDiGraph) -> dict:
    """Compute 3D spring layout with learning journey structure."""
    # Use spring layout with parameters tuned for learning paths
    G_undirected = G.to_undirected()
    pos = nx.spring_layout(
        G_undirected,
        dim=3,
        seed=42,        # Reproducible layout
        k=0.7,          # Spacing between nodes
        iterations=100  # More iterations for better layout
    )
    return pos


def create_edge_legend_html() -> str:
    """Create HTML legend for edge types."""
    legend_items = [
        ('has-skill', COLORS['has_skill'], 'Student possesses skill'),
        ('requires-skill', COLORS['requires_skill'], 'Module requires skill'),
        ('develops-skill', COLORS['develops_skill'], 'Module develops skill'),
        ('studies', COLORS['studies'], 'Student studies module'),
        ('transitions-to', COLORS['transitions_to'], 'Student state transition'),
        ('advances', COLORS['advances'], 'Module advances student'),
    ]

    html = '<div style="position: absolute; top: 120px; right: 20px; background: rgba(255,255,255,0.9); padding: 15px; border-radius: 5px; font-family: Arial; font-size: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">'
    html += '<div style="font-weight: bold; margin-bottom: 8px; border-bottom: 1px solid #ddd; padding-bottom: 5px;">Edge Types</div>'

    for label, color, description in legend_items:
        html += f'<div style="margin: 4px 0; display: flex; align-items: center;">'
        html += f'<div style="width: 20px; height: 3px; background: {color}; margin-right: 8px;"></div>'
        html += f'<span style="color: #333;"><b>{label}</b>: {description}</span>'
        html += '</div>'

    html += '</div>'
    return html


def create_face_legend_html() -> str:
    """Create HTML legend for face types."""
    legend_items = [
        ('Prerequisite', COLORS['prerequisite'], 'Validates student has required skill'),
        ('Completion', COLORS['completion'], 'Student state transition through module'),
        ('Skill-Gain', COLORS['skill_gain'], 'Student gains skill from module'),
    ]

    html = '<div style="position: absolute; top: 350px; right: 20px; background: rgba(255,255,255,0.9); padding: 15px; border-radius: 5px; font-family: Arial; font-size: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">'
    html += '<div style="font-weight: bold; margin-bottom: 8px; border-bottom: 1px solid #ddd; padding-bottom: 5px;">Face Types</div>'

    for label, color, description in legend_items:
        html += f'<div style="margin: 4px 0; display: flex; align-items: center;">'
        html += f'<div style="width: 20px; height: 20px; background: {color}; opacity: 0.7; margin-right: 8px; border-radius: 3px;"></div>'
        html += f'<span style="color: #333;"><b>{label}</b>: {description}</span>'
        html += '</div>'

    html += '</div>'
    return html


def create_visualization(chart_data: dict) -> go.Figure:
    """Create 3D Plotly visualization with learning journey styling."""
    # Build graph and compute layout
    G = build_network_graph(chart_data)
    pos_3d = compute_3d_layout(G)

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

            # Thicker lines for important edges
            line_width = 6 if edge_category in ['studies', 'transitions_to', 'advances'] else 4

            # Extract edge type from full type string
            edge_type = edge['type'].split('/')[-1] if '/' in edge['type'] else edge['type']

            trace = go.Scatter3d(
                x=[x0, x1],
                y=[y0, y1],
                z=[z0, z1],
                mode='lines',
                line=dict(width=line_width, color=edge_color),
                hovertext=f"{edge_type}: {edge['name']}",
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

            # Larger markers for students and modules
            size = 16 if vertex_category in ['student', 'learning_module'] else 13
            vertex_sizes.append(size)

            # Extract type for display
            vtype = vertex['type'].split('/')[-1] if '/' in vertex['type'] else vertex['type']

            vertex_hover.append(
                f"<b>{vertex['name']}</b><br>"
                f"Type: {vtype}<br>"
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
            opacity=0.9
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
                face_color = COLORS.get(face_category, COLORS['default'])

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
                    opacity=0.6,
                    hovertext=f"<b>{ftype}</b><br>{face['name']}",
                    hoverinfo='text',
                    showlegend=False
                )
                fig.add_trace(mesh_trace)

    # Update layout with learning journey styling
    title_text = f"<b>{chart_data['name']}</b>"
    if chart_data.get('description'):
        title_text += f"<br><sub style='color: #7f8c8d;'>{chart_data['description']}</sub>"

    euler_char = chart_data['topology']['euler_characteristic']
    v_count = chart_data['element_counts']['vertices']
    e_count = chart_data['element_counts']['edges']
    f_count = chart_data['element_counts']['faces']

    # Extract learning path metadata if available
    learning_metadata = ""
    metadata = chart_data.get('metadata', {})
    if 'learning_path' in metadata:
        lp = metadata['learning_path']
        entry = lp.get('entry_state', 'Unknown')
        exits = lp.get('exit_states', [])
        exit_str = ', '.join([e.split(':')[-1] for e in exits]) if exits else 'Unknown'
        learning_metadata = f"<br>Entry: {entry.split(':')[-1]} → Exit: {exit_str}"

    fig.update_layout(
        title=dict(
            text=title_text,
            x=0.5,
            xanchor='center',
            font=dict(size=18)
        ),
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            zaxis=dict(showgrid=False, zeroline=False, visible=False),
            bgcolor='#f8f9fa',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.2)  # Better viewing angle
            )
        ),
        showlegend=False,
        width=1400,
        height=900,
        margin=dict(l=0, r=280, t=120, b=0),
        paper_bgcolor='#ffffff',
        annotations=[
            # Topology info
            dict(
                text=f"<b>Topology:</b> V={v_count}, E={e_count}, F={f_count}, χ={euler_char}{learning_metadata}",
                xref="paper",
                yref="paper",
                x=0.02,
                y=0.98,
                showarrow=False,
                font=dict(size=13, color='#2c3e50', family='Arial'),
                bgcolor='rgba(255, 255, 255, 0.95)',
                borderpad=8,
                bordercolor='#bdc3c7',
                borderwidth=1
            ),
            # Vertex legend
            dict(
                text=(
                    "<b>Vertex Types:</b><br>"
                    f"<span style='color: {COLORS['student']}'>● Students</span> - Learning states<br>"
                    f"<span style='color: {COLORS['skill']}'>● Skills</span> - Capabilities to acquire<br>"
                    f"<span style='color: {COLORS['learning_module']}'>● Modules</span> - Learning units"
                ),
                xref="paper",
                yref="paper",
                x=0.98,
                y=0.98,
                xanchor='right',
                showarrow=False,
                font=dict(size=12, color='#2c3e50', family='Arial'),
                bgcolor='rgba(255, 255, 255, 0.95)',
                borderpad=8,
                bordercolor='#bdc3c7',
                borderwidth=1,
                align='left'
            )
        ]
    )

    return fig


def add_legends_to_html(html_path: Path):
    """Add interactive legends to the HTML file."""
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Add edge and face legends before closing body tag
    edge_legend = create_edge_legend_html()
    face_legend = create_face_legend_html()

    html_content = html_content.replace('</body>', f'{edge_legend}{face_legend}</body>')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)


def main():
    """Generate syllabus visualization from chart JSON."""
    if len(sys.argv) < 2:
        print("Usage: python scripts/visualize_syllabus.py charts/learning-journey-module-01/learning-journey-module-01.json")
        sys.exit(1)

    json_path = Path(sys.argv[1])

    if not json_path.exists():
        print(f"Error: JSON file not found: {json_path}")
        print(f"Run: python scripts/export_chart_direct.py {json_path.with_suffix('.md')} {json_path} first")
        sys.exit(1)

    # Load chart data
    print(f"Loading: {json_path.name}")
    chart_data = load_chart_json(json_path)

    # Verify this is a syllabus chart
    chart_type = chart_data.get('type', '')
    if 'syllabus' not in chart_type:
        print(f"Warning: Chart type is '{chart_type}', expected 'chart/syllabus'")
        print("This visualizer is optimized for syllabus charts. Continuing anyway...")

    # Create visualization
    print(f"Creating syllabus visualization...")
    fig = create_visualization(chart_data)

    # Save HTML
    output_path = json_path.with_suffix('.html')
    fig.write_html(str(output_path))

    # Add legends
    print(f"Adding interactive legends...")
    add_legends_to_html(output_path)

    print(f"✓ Syllabus visualization saved to: {output_path.name}")
    print(f"  Open in browser to view interactive learning journey")
    print(f"  Color-coded vertices: Students (blue), Skills (green), Modules (purple)")
    print(f"  Color-coded faces: Prerequisite (orange), Completion (blue), Skill-gain (green)")


if __name__ == '__main__':
    main()
