# goal is to return the parent or earliest known ancestor
from graph import Graph


def earliest_ancestor(ancestors, starting_node):

    g = Graph()
    # g is an instance of the class Graph
    for i in ancestors:
        g.add_vertex(i[0])  # add a vertex from graph.py # takes 1 param each
        g.add_vertex(i[1])  # add the second one
    for i in ancestors:
        # want to travel UP # add a edge from graph.py # takes 2 params
        g.add_edge(i[1], i[0])

    print(g.vertices)
    print(g.ancestor_finder(starting_node))
    # take the last of the entire list
    if g.ancestor_finder(starting_node) == []:
        return -1
    # else:


    return(g.ancestor_finder(starting_node))[-1]
    # ^ find the shortest path from 9,4 using def bfs from graph.py
