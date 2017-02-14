def generate_sudoku_graph(matrix):



colorForK = {node: [1,2,3,4,5,6,7,8,9] for node in G.nodes()}
def wp_algorithm(G, colorForK):
    nodes_ordered_by_degree = sorted(G.nodes(), key = G.degree, reverse = True)
    for node in nodes_ordered_by_degree
        node_color = colorForK[node][0]
        G.node[node]['color'] = node_color
        for v in G.neighbors(node):
            colorForK[v].pop(node_color)