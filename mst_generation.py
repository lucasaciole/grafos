import prim_algorithm as prim
import dijkstra_algorithm as dijkstra
import networkx as nx
from plotter import create_plotly_graph

# Generates the sample graph from a edgelist
G = nx.read_weighted_edgelist('Davis_southern_club_women-cooccurance.txt')

# Compare the Graph with its MST generated by Prim's Algorithm
prim_G = prim.prim_algorithm(G)
pos  = nx.spring_layout(G,k=0.15,iterations=20)
prim_pos = nx.spring_layout(prim_G,k=0.15,iterations=20)
pos.update(prim_pos)
create_plotly_graph(G, pos,
    'davis_southern_club_women_coocurance_prim',
    "Davis' Southern Club Women Coocurance", 
    "Sample Weighted Undirected Graph for use in Prim's Algorithm.")
create_plotly_graph(prim_G, pos,
    'davis_southern_club_women_coocurance_mst_prim',
    "MST for Davis' Southern Club Women Coocurance",
    "MST found by Prim's Algorithm, starting with the {} node".format(prim_G.nodes()[0]))

# Compare the Graph with its MST generated by Dijkstra's Algorithm
dijkstra_G = dijkstra.dijkstra_algorithm(G)
pos  = nx.spring_layout(G,k=0.15,iterations=20)
djikstra_pos = nx.spring_layout(dijkstra_G,k=0.15,iterations=20)
pos.update(djikstra_pos)
create_plotly_graph(G, pos,
    'davis_southern_club_women_coocurance_djikstra',
    "Davis' Southern Club Women Coocurance", 
    "Sample Weighted Undirected Graph for use in Dijkstra's Algorithm.")
create_plotly_graph(dijkstra_G, pos,
    'davis_southern_club_women_coocurance_mst_djikstra',
    "MST for Davis' Southern Club Women Coocurance",
    "MST found by Dijkstra's Algorithm, starting with the {} node.".format(dijkstra_G.nodes()[0]))

# Compare the Graph with its MST generated by Dijkstra's Algorithm with k = 2
dijkstra_G_k_2 = dijkstra.dijkstra_algorithm_with_k_sources(G, 2)
pos  = nx.spring_layout(G,k=0.15,iterations=20)
djikstra_pos = nx.spring_layout(dijkstra_G_k_2,k=0.15,iterations=20)
pos.update(djikstra_pos)
create_plotly_graph(G, pos,
    'davis_southern_club_women_coocurance_djikstra2',
    "Davis' Southern Club Women Coocurance", 
    "Sample Weighted Undirected Graph for use in Dijkstra's Algorithm.")
create_plotly_graph(dijkstra_G_k_2, pos,
    'davis_southern_club_women_coocurance_mst_djikstra2',
    "MST for Davis' Southern Club Women Coocurance",
    "MST found by Dijkstra's Algorithm, starting with 2 source nodes: {}.".format(dijkstra_G_k_2.nodes()[0:2]))

# Compare the Graph with its MST generated by Dijkstra's Algorithm with k = 3
dijkstra_G_k_3 = dijkstra.dijkstra_algorithm_with_k_sources(G, 3)
pos  = nx.spring_layout(G,k=0.15,iterations=20)
djikstra_pos = nx.spring_layout(dijkstra_G_k_3,k=0.15,iterations=20)
pos.update(djikstra_pos)
create_plotly_graph(G, pos,
    'davis_southern_club_women_coocurance_djikstra3',
    "Davis' Southern Club Women Coocurance", 
    "Sample Weighted Undirected Graph for use in Dijkstra's Algorithm.")
create_plotly_graph(dijkstra_G_k_3, pos,
    'davis_southern_club_women_coocurance_mst_djikstra3',
    "MST for Davis' Southern Club Women Coocurance",
    "MST found by Dijkstra's Algorithm, starting with 3 source nodes: {}.".format(dijkstra_G_k_3.nodes()[0:3]))
