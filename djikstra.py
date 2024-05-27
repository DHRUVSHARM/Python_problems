"""
implementation of the djikstra's algo with graph implemented as an adjacency matrix
"""
import math


def update(parent, graph, n, node_information, fixed):
    """
    update step of the djikstra's algo
    :param graph: ip graph
    :param parent the parent to be updated
    :param n: number of nodes
    :param node_information: node info
    :param fixed: fixed
    :return: None
    """

    for neighbour in range(0, n):
        if fixed[neighbour] is False and graph[parent][neighbour] != 0:
            # unfixed neighbour whose distance from source can be updated
            if node_information[neighbour][0] > node_information[parent][0] + graph[parent][neighbour]:
                node_information[neighbour][0] = node_information[parent][0] + graph[parent][neighbour]
                node_information[neighbour][1] = parent


def djikstra_algorithm(graph, n, source):
    """
    function to use djikstra algorithm to get the shortest path to every node from a single
    source
    :param graph: ip graph
    :param n: number of vertices
    :param source : single source to start from
    :return: None
    """

    # store the fixed nodes
    fixed = [False for _ in range(0, n)]

    # first we add the source node
    # dictionary to store the shortest path to a node from the source given and the parent
    node_information = {source: [0, None]}
    for node in range(1, n):
        node_information[node] = [math.inf, None]
    fixed[source] = True
    # now we need to update the node_information using this node
    update(source, graph, n, node_information, fixed)

    for _ in range(1, n):
        # first we find the minimal node to fix
        node_minimal = -1
        minimal_cost_to_fix = math.inf
        for node, node_info in node_information.items():
            if fixed[node] is False:
                # only non fixed nodes are considered
                if node_info[0] < minimal_cost_to_fix:
                    minimal_cost_to_fix = node_info[0]
                    node_minimal = node

        if node_minimal == -1:
            print("the graph is disconnected or some ip error !!!!")
            return None

        # now we have to do the update step
        fixed[node_minimal] = True
        update(node_minimal, graph, n, node_information, fixed)

    print("the final node information is as : ")
    for node, node_info in node_information.items():
        print(str(node) + " : " + str(node_info))


if __name__ == '__main__':

    line = list(input().strip().split())

    vertices = int(line[0])  # Read number of vertices
    print("the number of nodes are : " + str(vertices))

    edges = int(line[1])  # the number of edges
    print("the number of edges are : " + str(edges))

    # we will store the graph as an adjacency matrix
    graph = [[int(0) for j in range(vertices)] for i in range(vertices)]

    for _ in range(0, edges):
        line = list(input().strip().split())
        graph[int(line[0])][int(line[1])] = int(line[2])
        # graph[int(line[1])][int(line[0])] = int(line[2])

    print("the adjacency matrix is : ")
    for l in graph:
        print(l)

    djikstra_algorithm(graph, vertices, 0)
