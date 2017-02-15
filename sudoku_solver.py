import pdb
import itertools
import networkx as nx
from random import randint
from plotter import create_plotly_graph, create_plotly_colored_graph

def generate_sudoku_graph():
    """Generates Graph based on a Sudoku puzzle
    """
    G = nx.Graph()
    for i in range(1,10):
        for j in range(1,10):
            if i < 4:
                if j < 4:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=1)
                elif j < 7:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=4)
                else:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=7)
            elif i < 7:
                if j < 4:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=2)
                elif j < 7:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=5)
                else:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=8)
            else:
                if j < 4:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=3)
                elif j < 7:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=6)
                else:
                    G.add_node('v{}{}'.format(i,j),row=i,column=j,cube=9)
    
    for i in range(1,10):
        edgelist = [node for node, data in G.nodes(data=True) if data['cube'] == i]
        edgelist = [edge for edge in itertools.product(edgelist,edgelist) if edge[0] != edge[1]]
        G.add_edges_from(edgelist)
        edgelist = [node for node, data in G.nodes(data=True) if data['row'] == i]
        edgelist = [edge for edge in itertools.product(edgelist,edgelist) if edge[0] != edge[1]]
        G.add_edges_from(edgelist)
        edgelist = [node for node, data in G.nodes(data=True) if data['column'] == i]
        edgelist = [edge for edge in itertools.product(edgelist,edgelist) if edge[0] != edge[1]]
        G.add_edges_from(edgelist)

    return G


def initialize_graph_color(G, puzzle, colorForNode):
    """Updates color array for each node with given puzzle color array"""
    for node, number in puzzle:
        G.node[node]['number'] = number
        for neighbor in G.neighbors(node):
            if number in colorForNode[neighbor]:
                colorForNode[neighbor].remove(number)


def wp_algorithm(G, numberForNode):
    """Completes a Sudoku puzzle using the Welsh-Powell Algorithm"""

    stop = False

    # Orders nodes ascending by size of remaining possible numbers
    nodes_ordered_by_available_numbers = {node:len(numberForNode[node]) for node in G.nodes()}
    nodes_ordered_by_available_numbers = sorted(nodes_ordered_by_available_numbers, key=nodes_ordered_by_available_numbers.get)
    
    while len(nodes_ordered_by_available_numbers) > 0:
        node = nodes_ordered_by_available_numbers.pop(0)
        # If no numbers are left for current node, puzzle is impossible
        if len(numberForNode[node]) < 1:
            print("Could not solve puzzle.")
            return
        
        number = numberForNode[node][0] # Pick first possible number
        G.node[node]['number'] = number
        for v in G.neighbors(node):
            # Remove used number from possibility list of all neighbors of current node
            if number in colorForNode[v]:
                colorForNode[v].remove(number)                
        nodes_ordered_by_available_numbers = {node:len(numberForNode[node]) for node in nodes_ordered_by_available_numbers}
        nodes_ordered_by_available_numbers = sorted(nodes_ordered_by_available_numbers, key=nodes_ordered_by_available_numbers.get)


if __name__ == "__main__":
    G = generate_sudoku_graph()

    # Sets existing numbers from given puzzle
    '''
    puzzle = [('v11',9), ('v12',5), ('v16',1), ('v19',8),
              ('v22',2), ('v23',1), ('v24',8), ('v25',9), ('v27',6),
              ('v31',3), ('v35',4), ('v36',2), ('v37',1), ('v38',5),('v39',9),
              ('v41',2), ('v42',4), ('v45',7), ('v46',8), ('v49',1),
              ('v51',1), ('v53',9), ('v54',3), ('v55',2), ('v58',6), ('v59',5),
              ('v61',8), ('v64',1), ('v68',7), ('v62',3),
              ('v71',4), ('v72',9), ('v75',1), ('v77',5), ('v78',8),
              ('v81',6), ('v82',8), ('v83',2), ('v84',9), ('v89',4),
              ('v94',4), ('v95',8), ('v96',3), ('v98',9), ('v99',6)
              ]
    '''
    puzzle = [('v11',9), ('v12',5),
              ('v22',2), ('v23',1), ('v24',8),
              ('v31',3), ('v35',4), ('v36',2), ('v37',1),
              ('v41',2), ('v42',4), ('v45',7),
              ('v51',1), ('v53',9), ('v54',3), ('v55',2),
              ('v61',8), ('v64',1),
              ('v71',4), ('v72',9), ('v75',1),
              ('v81',6), ('v82',8), ('v83',2),
              ('v94',4), ('v95',8), ('v96',3),
              ]
    pos = {}
    groups = {}
    colorForNode = {}
    for i in range(1,10):
        for j in range(1,10):
            pos['v{}{}'.format(i,j)] = [j,10 - i]
            colorForNode['v{}{}'.format(i,j)] = [1,2,3,4,5,6,7,8,9]

    initialize_graph_color(G, puzzle, colorForNode)
    
    for i in range(1,10):
        groups[i] = [node for node, data in G.nodes(data=True) if 'number' in data and data['number'] == i]

    wp_algorithm(G, colorForNode)
    print([node for node, data in G.nodes(data=True) if 'number' not in data])
    '''create_plotly_colored_graph(G, pos, groups,
    'sudoku-less-starting-state',
    'Sudoku Problem - Graph Coloration Algorithm',
    "Sudoku Problem Example to be used by Welsh-Powell's Graph Coloration Algorithm with less starting numbers")
    
    groups = {}
    for i in range(1,10):
        groups[i] = [node for node, data in G.nodes(data=True) if 'number' in data and data['number'] == i]
    create_plotly_colored_graph(G, pos, groups,
    'sudoku-solved-less',
    'Sudoku Problem - Graph Coloration Algorithm',
    "Sudoku Problem Solved by Welsh-Powell's Graph Coloration Algorithm with less starting numbers")

    
    G = generate_sudoku_graph()

    # Sets existing numbers from given puzzle
    puzzle = [('v11',9), ('v12',5), ('v16',1), ('v19',8),
              ('v22',2), ('v23',1), ('v24',8), ('v25',9), ('v27',6),
              ('v31',3), ('v35',4), ('v36',2), ('v37',1), ('v38',5),('v39',9),
              ('v41',2), ('v42',4), ('v45',7), ('v46',8), ('v49',1),
              ('v51',1), ('v53',9), ('v54',3), ('v55',2), ('v58',6), ('v59',5),
              ('v61',8), ('v64',1), ('v68',7), ('v62',3),
              ('v71',4), ('v72',9), ('v75',1), ('v77',5), ('v78',8),
              ('v81',6), ('v82',8), ('v83',2), ('v84',9), ('v89',4),
              ('v94',4), ('v95',8), ('v96',3), ('v98',9), ('v99',6)
              ]
    pos = {}
    groups = {}
    colorForNode = {}
    for i in range(1,10):
        for j in range(1,10):
            pos['v{}{}'.format(i,j)] = [j,10 - i]
            colorForNode['v{}{}'.format(i,j)] = [1,2,3,4,5,6,7,8,9]

    initialize_graph_color(G, puzzle, colorForNode)

    wp_algorithm(G, colorForNode)
    groups = {}
    for i in range(1,10):
        groups[i] = [node for node, data in G.nodes(data=True) if 'number' in data and data['number'] == i]
    create_plotly_colored_graph(G, pos, groups,
    'sudoku-solved2',
    'Sudoku Problem - Graph Coloration Algorithm',
    "Sudoku Problem Solved by Welsh-Powell's Graph Coloration Algorithm - 2th Run")

    G = generate_sudoku_graph()

    # Sets existing numbers from given puzzle
    puzzle = [('v11',9), ('v12',5), ('v16',1), ('v19',8),
              ('v22',2), ('v23',1), ('v24',8), ('v25',9), ('v27',6),
              ('v31',3), ('v35',4), ('v36',2), ('v37',1), ('v38',5),('v39',9),
              ('v41',2), ('v42',4), ('v45',7), ('v46',8), ('v49',1),
              ('v51',1), ('v53',9), ('v54',3), ('v55',2), ('v58',6), ('v59',5),
              ('v61',8), ('v64',1), ('v68',7), ('v62',3),
              ('v71',4), ('v72',9), ('v75',1), ('v77',5), ('v78',8),
              ('v81',6), ('v82',8), ('v83',2), ('v84',9), ('v89',4),
              ('v94',4), ('v95',8), ('v96',3), ('v98',9), ('v99',6)
              ]
    pos = {}
    groups = {}
    colorForNode = {}
    for i in range(1,10):
        for j in range(1,10):
            pos['v{}{}'.format(i,j)] = [j,10 - i]
            colorForNode['v{}{}'.format(i,j)] = [1,2,3,4,5,6,7,8,9]

    initialize_graph_color(G, puzzle, colorForNode)

    wp_algorithm(G, colorForNode)
    groups = {}
    for i in range(1,10):
        groups[i] = [node for node, data in G.nodes(data=True) if 'number' in data and data['number'] == i]
    create_plotly_colored_graph(G, pos, groups,
    'sudoku-solved3',
    'Sudoku Problem - Graph Coloration Algorithm',
    "Sudoku Problem Solved by Welsh-Powell's Graph Coloration Algorithm - 3th Run")

    G = generate_sudoku_graph()

    # Sets existing numbers from given puzzle
    puzzle = [('v11',9), ('v12',5), ('v16',1), ('v19',8),
              ('v22',2), ('v23',1), ('v24',8), ('v25',9), ('v27',6),
              ('v31',3), ('v35',4), ('v36',2), ('v37',1), ('v38',5),('v39',9),
              ('v41',2), ('v42',4), ('v45',7), ('v46',8), ('v49',1),
              ('v51',1), ('v53',9), ('v54',3), ('v55',2), ('v58',6), ('v59',5),
              ('v61',8), ('v64',1), ('v68',7), ('v62',3),
              ('v71',4), ('v72',9), ('v75',1), ('v77',5), ('v78',8),
              ('v81',6), ('v82',8), ('v83',2), ('v84',9), ('v89',4),
              ('v94',4), ('v95',8), ('v96',3), ('v98',9), ('v99',6)
              ]
    pos = {}
    groups = {}
    colorForNode = {}
    for i in range(1,10):
        for j in range(1,10):
            pos['v{}{}'.format(i,j)] = [j,10 - i]
            colorForNode['v{}{}'.format(i,j)] = [1,2,3,4,5,6,7,8,9]

    initialize_graph_color(G, puzzle, colorForNode)

    wp_algorithm(G, colorForNode)
    groups = {}
    for i in range(1,10):
        groups[i] = [node for node, data in G.nodes(data=True) if 'number' in data and data['number'] == i]
    create_plotly_colored_graph(G, pos, groups,
    'sudoku-solved4',
    'Sudoku Problem - Graph Coloration Algorithm',
    "Sudoku Problem Solved by Welsh-Powell's Graph Coloration Algorithm - 4th Run")
    '''
