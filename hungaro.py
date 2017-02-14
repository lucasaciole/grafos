import networkx as nx
import copy
from plotter import create_plotly_graph
from networkx.algorithms import bipartite
import pdb

def hungarian_method(G, M, X, Y):
    # Select first m_not_matched node on bipartite=0 from G
    while not fully_matches(G,M):
        #even_distance from starting_node
        S = [current_node]
        path = [current_node]
        #odd_distance from starting_node
        T = []
        if T == neighbors_of(G,S)   :
            # No matching possible, S denies the Matching Theorem
            return (False,S)
        else:
            for n in neighbors_of(G,S):
                if n not in T:
                    y = n
                    break
            print("y:", y)
            print("S:", S)
            print("T:", T) 
            print("N(S):",'' neighbors_of(G,S))
            while is_m_matched(M, y):
                print("y is m_matched.")
                S.append(matched_node_of(M, y))
                T.append(y)
                print("S:", S)
                print("T:", T)
                path.append(y)
                path.append(z)
                if T == neighbors_of(G,S):
                    # No matching possible, S denies the Matching Rule
                    return (False,S)
                for n in neighbors_of(G,S):
                    if n not in T:
                        y = n
                        break
            #y is m_not_matched
            

            


    return (True,M)

def neighbors_of(G,S):
    lista = []
    for node in S:
        lista += G.neighbors(node)
    return lista

def is_m_matched(M, n):
    for u, v in M:
        if u == n or v == n:
            return True
    return False

def matched_node_of(M, y):
    for u, v in M:
        if u == n:
            return v;
        elif v == n:
            return u;
    return None


def fully_matches(G, M):
    for n in G.nodes():
        if not is_m_matched(M, n):
            return False;
    return True;

G = nx.Graph()
G.add_nodes_from(['0','1','2','3','4','5','6','7','8','9'], bipartite=0)
G.add_nodes_from(['10','11','12','13','14','15','16','17','18','19'], bipartite=1)

F = nx.read_edgelist('bipartidoA.txt')
G.add_edges_from(F.edges())
pos = nx.circular_layout(G)

create_plotly_graph(G, pos,
    "hungarian-method-sample-graph",
    'Hungarian Method Sample Bipartite Graph',
    "Sample Bipartite Graph for use in Hungarian Algorithm.")

M = [('0','11'), ('1','13')]
matched_graph = hungarian_method(G,M)
print(matched_graph)
#create_plotly_graph(G, pos,
#    "hungarian-method-sample-graph-paired",
#    'Hungarian Method Paired Bipartite Graph',
#    "Sample Bipartite Graph Paired by Hungarian Algorithm using M = {}.".format(M))