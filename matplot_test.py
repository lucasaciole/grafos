import matplotlib.pyplot as plt
import networkx as nx
from pqdict import PQDict

def prim(G,start):
    """Function recives a graph and a starting node, and returns a MST"""
    stopN = G.number_of_nodes() - 1
    current = start
    closedSet = set()
    pq = PQDict()
    mst = []

    while len(mst) < stopN:
        for node in G.neighbors(current):
            if node not in closedSet and current not in closedSet:
                if (current,node) not in pq and (node,current) not in pq:
                    w = G.edge[current][node]['weight']
                    pq.additem((current,node), w)
        closedSet.add(current)
        tup, wght = pq.popitem()
        while(tup[1] in closedSet):
            tup, wght = pq.popitem()
        mst.append(tup)
        current = tup[1]

    return mst

if (__name__ == "__main__"):
    G = nx.read_weighted_edgelist('Davis_southern_club_women-cooccurance.txt')
    #G = nx.complete_graph(5)
    #prim_G = prim(G, '1')
    prim_G = nx.minimum_spanning_tree(G)
    othr = [n for n in G.edges() if n not in prim_G]
    pos = nx.spring_layout(prim_G, k = 0.15, iterations=50)
        # nodes
    nx.draw_networkx_nodes(G, pos, node_size=200)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=prim_G.edges(), width=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=othr, width=0.2, alpha=0.5, edge_color='b', style='dashed')

    # labels
    nx.draw_networkx_labels(G,pos,font_size=6,font_family='sans-serif')
    plt.savefig("example.png")

    plt.axis('off')
    print(len(prim_G.edges()))
    plt.show()