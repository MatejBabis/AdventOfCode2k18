import re
import numpy as np
from collections import defaultdict

def input_parser(filename):
    f = open(filename)

    output = []
    for line in f.readlines():
        # expected string formay
        m = re.search(
            r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line.strip())
        # add extracted tuple
        output += [np.array([m.group(1), m.group(2)])]

    f.close()
    return np.array(output)


def visualise_graph(edges):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_edges(G, pos, width=0.5, arrows=True)
    plt.show()


def get_supporting_structures(filename):
    constraints = input_parser(filename)

    # using defaultdict means that if a key is not found in the dictionary,
    # then instead of a KeyError being thrown, a new entry is created
    incoming_edges = defaultdict(list)
    outgoing_edges = defaultdict(list)
    for start_n, end_n in constraints:
        outgoing_edges[start_n].append(end_n)
        incoming_edges[end_n].append(start_n)

    return incoming_edges, outgoing_edges


if __name__ == "__main__":
    # visualising can help understanding
    # constraints = input_parser("input.txt")
    # visualise_graph(constraints)

    incoming_edges, outgoing_edges = get_supporting_structures("input.txt")
    # start by creating a list of where we can start (i.e. have no inward edges)
    queue = [k for k in outgoing_edges if incoming_edges[k] == []]
    answer = ""

    # this is a DFS-like topological traversal
    while queue:
        vertex = sorted(queue)[0]   # get the head
        queue = sorted(queue)[1:]   # alphabetical preference within the queue
        answer += vertex
        for child in outgoing_edges[vertex]:
            # neat way to check if all we have visited all nodes required
            # to be able to proceed to this node
            if set(incoming_edges[child]).issubset(set(answer)):
                queue.append(child)

    print("Answer:", answer)
