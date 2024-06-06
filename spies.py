"""
You are running a network of n spies that need to communicate together. Some pairs of
spies have a direct channel for communication. Every pair of spies that can communicate
together directly has a cost associated with keeping that channel of communication open.
There are a total of m channels of communication present among all of your spies.
You want to determine a minimum cost network to connect all of your spies so that
any spy can connect with any other spy through a series of open communication channels.
However, there is one problem. Some of your spies are unreliable. If a message is passed
through any of those spies as an intermediate step, the information is usually lost.
Thus, you must design a minimum cost network to connect all of your spies with the
additional requirement that a message can be passed from any spy to any other spy without
ever having to go through an unreliable spy as an intermediate step along the path.
Give an O(n
2
) (or an O(m log n)) algorithm that finds the minimum cost network to
connect your spies such that no message has to pass through an unreliable spy, or else
outputs that it is impossible to do so.
"""

import math


def update(parent, g, n, fixed, node_info, isunreliable):
    for neighbour in range(0, n):
        if (
            g[parent][neighbour] != 0
            and fixed[neighbour] is False
            and isunreliable[neighbour] is False
        ):
            # non fixed neighbour that is reliable
            if g[parent][neighbour] < node_info[neighbour][0]:
                node_info[neighbour][0] = g[parent][neighbour]
                node_info[neighbour][1] = parent


def solve(g, n, m, is_unreliable, k):
    """
    function to get minimal network cost if possible , concept used is Prim's algorithm
    :param k: unreliable count
    :param g: ip graph
    :param n: nodes
    :param m: edges
    :param is_unreliable: map to check reliability
    :return:
    """
    # stores if the current node is fixed in the algorithm
    fixed = [False for _ in range(0, n)]
    # store the attachment_weight and parent of the nodes , -1 represents no parent assigned yet
    node_info = [[math.inf, -1] for _ in range(0, n)]
    # we have guaranteed that atleast one node is reliable which we will store as the
    # begin source node for the algorithm

    start = -1
    for i in range(0, n):
        if is_unreliable[i] is False:
            start = i
            break
    node_info[start][0] = 0
    fixed[start] = True
    # we only update those nodes which are reliable
    update(start, g, n, fixed, node_info, is_unreliable)

    """
    print("the node information is : ")
    for i in range(0, n):
        print(str(i) + " : " + str(node_info[i]))
    """
    minimal_cost_weight = 0
    for _ in range(1, n - k):
        min_node = -1
        min_attach_wt = math.inf
        for node in range(0, n):
            if fixed[node] is False:
                if node_info[node][0] < min_attach_wt:
                    min_node = node
                    min_attach_wt = node_info[node][0]
        if min_node == -1:
            return None
        fixed[min_node] = True
        # print("the node fixed in this iteration is : " + str(min_node))
        # print("the edge added is : " + str(node_info[min_node][1]) + "-->" + str(min_node))
        # print("and the weight there is : " + str(node_info[min_node][0]))
        minimal_cost_weight += g[node_info[min_node][1]][min_node]
        if is_unreliable[min_node] is False:
            # reliable node
            update(min_node, g, n, fixed, node_info, is_unreliable)
        # print("the node information is : ")
        """
        for i in range(0, n):
            print(str(i) + " : " + str(node_info[i]))
        """
    # print("************* now adding unreliable nodes *****************")
    # print("fixed is : " + str(fixed))

    # now we will attach the nodes that are unreliable
    for i in range(0, n):
        if fixed[i] is False:
            # attach the node to minimal cost reliable node
            min_cost_node = -1
            min_attach_wt = math.inf
            for neighbour in range(0, n):
                if g[i][neighbour] != 0 and is_unreliable[neighbour] is False:
                    if g[i][neighbour] < min_attach_wt:
                        min_cost_node = neighbour
                        min_attach_wt = g[i][neighbour]
            if min_cost_node == -1:
                return None
            minimal_cost_weight += min_attach_wt

    return minimal_cost_weight


if __name__ == "__main__":

    line = list(input().strip().split())

    number_of_spies = int(line[0])  # Read number of vertices
    # print("the number of nodes are : " + str(number_of_spies))

    connections = int(line[1])  # the number of edges
    # print("the number of edges are : " + str(connections))

    k = int(input())  # the number of unreliable spies
    unreliable_spies = []
    line = list(input().strip().split())
    for element in line:
        unreliable_spies.append(int(element))

    is_unreliable = [False for _ in range(0, number_of_spies)]
    for element in unreliable_spies:
        is_unreliable[element] = True

    # we will store the graph as an adjacency matrix
    graph = [[int(0) for j in range(number_of_spies)] for i in range(number_of_spies)]
    # create a matrix of n rows and m columns with None (or any other default value)

    for _ in range(0, connections):
        line = list(input().strip().split())
        graph[int(line[0])][int(line[1])] = int(line[2])
        graph[int(line[1])][int(line[0])] = int(line[2])
    """
    print("the adjacency matrix is : ")
    for l in graph:
        print(l)
    """
    # print("unreliability map is : " + str(is_unreliable))
    # print("number of spies , connections : " + str(number_of_spies) + " , " + str(connections))

    # function to get the minimal network cost if possible and print it
    result = solve(graph, number_of_spies, connections, is_unreliable, k)
    if result is None:
        print("NONE")
    else:
        print(str(result))
