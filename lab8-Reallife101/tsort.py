from sys import argv
from stack_array import *


class vertex:
    def __init__(self):
        self.in_degree = 0
        self.adjacent_vertices = []

    def in_deg_change(self, delta):
        self.in_degree += delta

    def adjacent_add(self, item):
        self.adjacent_vertices.append(item)


def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility "tsort".  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''

    # catching error
    if len(vertices) == 0:
        raise ValueError("input contains no edges")

    # declaring variables
    adj_table = {}
    i = 0
    total_nodes = 0

    # creating adjacency dictionary
    while i < len(vertices):

        try:
            if vertices[i + 1] in adj_table:
                adj_table[vertices[i + 1]].in_deg_change(1)
            else:
                v2 = vertex()
                v2.in_deg_change(1)
                adj_table[vertices[i + 1]] = v2
                total_nodes += 1
        except IndexError:
            raise ValueError("input contains an odd number of tokens")

        if vertices[i] in adj_table:
            adj_table[vertices[i]].adjacent_add(vertices[i + 1])
        else:
            v1 = vertex()
            v1.adjacent_add(vertices[i + 1])
            adj_table[vertices[i]] = v1
            total_nodes += 1
        i += 2

    # Create Stack
    stack = Stack(len(adj_table))
    order = []
    num_node = 0

    for key in adj_table.keys():
        if adj_table[key].in_degree == 0:
            stack.push(key)

    while not stack.is_empty():
        pop = stack.pop()
        num_node += 1
        order.append(pop)

        for vert in adj_table[pop].adjacent_vertices:
            adj_table[vert].in_deg_change(-1)
            if adj_table[vert].in_degree == 0:
                stack.push(vert)

    if num_node != total_nodes:
        raise ValueError("input contains a cycle")
    final_string = order[0]
    i = 1
    while i < len(order):
        final_string = final_string + "\n" + order[i]
        i += 1
    return final_string


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
