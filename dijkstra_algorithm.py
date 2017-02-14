import copy
import networkx as nx
import pdb

def dijkstra_algorithm(G):
    return dijkstra_algorithm_with_k_sources(G, 1)

def dijkstra_algorithm_with_k_sources(G, k):    
    """Return a minimum spanning tree of an undirected connected
    weighted graph using Prim's Algorithm.

    A minimum spanning tree is a subgraph of the graph (a tree) with
    the minimum sum of edge weights.
    Parameters
    ----------
    G : NetworkX Graph

    Returns
    -------
    mst : NetworkX Graph
       A minimum spanning tree
    """

    # Generates the networkx Graph that will be returned
    djikstra_MST = nx.Graph()    

    # Initializes all nodes predecessors as None, their entry cost as infinity and adds those nodes to our MST networkx Graph
    for node in G.nodes():
        djikstra_MST.add_node(node)
        G.node[node]['predecessor'] = None
        G.node[node]['entry_cost'] = float('inf')

    # Chooses first k node as source
    for i in range(k):
        G.node[G.nodes()[i]]['entry_cost'] = 0
    pdb.set_trace()

    Q = copy.deepcopy(G.nodes())
    S = []

    while (len(Q) > 0):
        u = extract_min_node(G, Q)
        S.append(u)
        for v in G.neighbors(u):
            relax(G, u, v)


    for node in G.nodes():
        predecessor = G.node[node]['predecessor']
        w = G.node[node]['entry_cost']
        if predecessor is not None:
            djikstra_MST.add_edge(predecessor, node, weight=w)
                


    return djikstra_MST

def relax(G, u, v): 
    if G.node[v]['entry_cost'] > G.node[u]['entry_cost'] + weight(G, u, v):
        G.node[v]['entry_cost'] = G.node[u]['entry_cost'] + weight(G, u, v)
        G.node[v]['predecessor'] = u

def weight(G, u, v):
    """Return weight of edge from u to v
    """
    return G.edge[u][v]['weight']

def extract_min_node(G, Q):
    min_priority = float('inf')
    for node in Q:
        if G.node[node]['entry_cost'] < min_priority:
            min_node = node
    Q.remove(min_node)
    return min_node