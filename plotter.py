import plotly.plotly as py
from plotly.graph_objs import *
import networkx as nx
import pdb

def create_plotly_graph(G, pos, filename, title, text):
    dmin = 1
    ncenter = 0
    for n in pos:
        x,y = pos[n]
        d = (x-0.5)**2 + (y-0.5)**2
        if d < dmin:
            ncenter = n
            dmin = d
            
    p = nx.single_source_shortest_path_length(G,ncenter)

    edge_trace = Scatter(
        x=[], 
        y=[], 
        line=Line(width=0.5,color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x=[], 
        y=[], 
        text=G.nodes(),
        mode='markers+text', 
        hoverinfo='text',
        marker=Marker(
            showscale=True,
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            colorscale='YIGnBu',
            reversescale=True,
            color=[], 
            size=10,         
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    for node, adjacencies in enumerate(G.adjacency_list()):
        node_trace['marker']['color'].append(len(adjacencies))
        node_info = '# of connections: '+str(len(adjacencies))
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
                layout=Layout(
                    title=title,
                    titlefont=dict(size=16),
                    showlegend=False, 
                    width=650,
                    height=650,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text=text,
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))
    py.plot(fig, filename=filename)

def create_plotly_colored_graph(G, pos, groups, filename, title, text):
    dmin = 1
    ncenter = 0
    for n in pos:
        x,y = pos[n]
        d = (x-0.5)**2 + (y-0.5)**2
        if d < dmin:
            ncenter = n
            dmin = d

    edge_trace = Scatter(
        x=[], 
        y=[], 
        line=Line(width=0.5,color='#000'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    node_trace = Scatter(
        x=[], 
        y=[], 
        text=[],
        textposition='center',
        textfont=dict(
        family='sans serif',
        size=18,
        color='#000000'
        ),
        mode='markers+text', 
        hoverinfo='text',
        marker=Marker(
            showscale=False,
            symbol = 'square',
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            colorscale='RdBu',
            reversescale=True,
            color=[], 
            size=22,
            line=dict(width=2)))

    for node in G.nodes():
        x, y = pos[node]
        node_trace['x'].append(x)
        node_trace['y'].append(y)
        number = ''
        if 'number' in G.node[node]:
            number = G.node[node]['number']
        node_trace['marker']['color'].append(number)
        node_info = '{}'.format(number)
        node_trace['text'].append(node_info)

    fig = Figure(data=Data([edge_trace, node_trace]),
                layout=Layout(
                    title=title,
                    titlefont=dict(size=16),
                    showlegend=False, 
                    width=650,
                    height=650,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text=text,
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))
    py.plot(fig, filename=filename)