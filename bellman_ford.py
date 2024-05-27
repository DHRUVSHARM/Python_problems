"""
bellman ford algorithm implementation , used for directed graph with negative edges and
also can be used to detect negative weight cycles
"""
import math


def bellman_ford(edge_list, edges, vertices, source):
    """
    bellman ford algorithm that calculates the shortest path weight to each node from a
    defined source , else finds negative weight cycle
    :param edge_list: edge list
    :param edges: number of edges
    :param vertices: number of vertices
    :param source: source node
    :return: None
    """

    # here we assume that the graph is connected, else the answer will be infinity

    # initialization step , based on source
    node_information = {}

    # we are going to also include extra information that stores the path length as well
    for i in range(0, vertices):
        node_information[i] = [math.inf, None, 0]

    # initialize the start vertex , the source will always have 0 weight unless of
    # course you have a negative weight cycle
    node_information[source][0] = 0
    # the above is like the first iteration

    for it_number in range(1, vertices):
        # iterations are from 1 to n-1
        # at every iteration , the path length is atleast = it_number
        print("iteration number : " + str(it_number))
        updates = 0
        for edge_info in edge_list:
            if node_information[edge_info[0]][0] != math.inf:
                # we can consider his edge for update , since we can reach the parent
                # we can think of an edge as u -> v
                u = edge_info[0]
                v = edge_info[1]

                # the last condition added will ensure only 1 length progress in our
                # paths , forcing the consideration to be till n - 1

                # observation : shortest paths ARE of length  n-1 unless ,
                # disconnection (invalid G) or negative weight cycle

                # since we are building from the beginning , this is enough

                if node_information[u][0] + edge_info[2] < node_information[v][0] \
                        and node_information[u][2] + 1 <= it_number:
                    print("the edge considered is : " + str(u) + " -> " + str(v))
                    node_information[v][0] = node_information[u][0] + edge_info[2]
                    # update the parent of v as u
                    node_information[v][1] = u
                    # update the path length
                    node_information[v][2] = node_information[u][2] + 1
                    # change made counter
                    updates += 1

        print("the number of updates we have in this iteration are : " + str(updates))
        if updates == 0:
            print("actually we do not require only more update steps !!!")
        for node, info in node_information.items():
            print(str(node) + " : " + str(info))
        print("\n")

    # n'th iteration negative weight cycle check , if we have updates at this step -> problem
    updates = 0
    for edge_info in edge_list:
        if node_information[edge_info[0]][0] != math.inf:
            # we can consider his edge for update , since we can reach the parent
            if node_information[edge_info[0]][0] + edge_info[2] < node_information[edge_info[1]][0]:
                node_information[edge_info[1]][0] = node_information[edge_info[0]][0] + edge_info[2]
                node_information[edge_info[1]][1] = edge_info[0]
                updates += 1
    if updates != 0:
        print("negative cycle exists !!!")
    else:
        print("no negative cycle !!!")


if __name__ == '__main__':
    # the input will be read and stored as an edge-list
    line = list(input().strip().split())

    vertices = int(line[0])  # Read number of vertices
    print("the number of nodes are : " + str(vertices))

    edges = int(line[1])  # the number of edges
    print("the number of edges are : " + str(edges))

    # we will store the graph as an edge list
    edge_list = [[int(0) for j in range(3)] for i in range(edges)]

    for index in range(0, edges):
        line = list(input().strip().split())
        edge_list[index][0] = int(line[0])
        edge_list[index][1] = int(line[1])
        edge_list[index][2] = int(line[2])

    # the mapping is as
    # A : 0 , B : 1 , C : 2 , D : 3 , E : 4

    print("the edges stored are as : ")
    for edge_info in edge_list:
        print(str(edge_info))

    print()
    bellman_ford(edge_list, edges, vertices, 0)
