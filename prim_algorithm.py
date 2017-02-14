import copy
import networkx as nx
def prim_algorithm(G):
    """Return a minimum spanning tree of an undirected connected
    weighted graph using Prim's Algorithm.

    A minimum spanning tree is a subgraph of the graph (a tree) with
    the minimum sum of edge weights.
    Parameters
    ----------
    G : NetworkX Graph

    Returns
    -------
    prim_MST : NetworkX Graph
       A minimum spanning tree
    """
    # Generates the networkx Graph that will be returned
    prim_MST = nx.Graph()

    # Initializes all nodes predecessors as None, also adding those nodes to our MST networkx Graph
    for node in G.nodes():
        prim_MST.add_node(node)
        G.node[node]['predecessor'] = None
        G.node[node]['entry_cost'] = float('inf')

    # Chooses first node to start algorithm
    G.node[G.nodes()[0]]['entry_cost'] = 0

    Q = copy.deepcopy(G.nodes())
    S = []
    while (len(Q) > 0):
        node = extract_min_node(G, Q)
        S.append(node)
        for neighbor_node in G.neighbors(node):
            if neighbor_node in Q and G.node[neighbor_node]['entry_cost'] > weight(G,node,neighbor_node):
                G.node[neighbor_node]['entry_cost'] = weight(G,node,neighbor_node)
                G.node[neighbor_node]['predecessor'] = node


    for node in G.nodes():
        predecessor = G.node[node]['predecessor']
        w = G.node[node]['entry_cost']
        if predecessor is not None:
            prim_MST.add_edge(predecessor, node, weight=w)
                
    return prim_MST

def extract_min_node(G, Q):
    min_priority = float('inf')
    for node in Q:
        if G.node[node]['entry_cost'] < min_priority:
            min_node = node
    Q.remove(min_node)
    return min_node

def weight(G, from_node, to_node):
    """Return weight of edge from from_node to to_node
    """
    return G.edge[from_node][to_node]['weight']