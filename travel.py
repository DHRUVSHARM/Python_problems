
"""
author : Dhruv Sharma , Mona Anil Udasi

Problem 1 (20 points: 12 for implementation / 8 for writeup)
You are trying to get home in time to attend your sister’s opening night performance. You have
limited time and limited money to do so. Given is an undirected graph G, containing n nodes and
m edges. One of these nodes is your current location. Another of the nodes is your destination.
Each edge represents a potential travel route from one location to another. Each edge has two
positive integer values associated with it: a monetary cost (any integer greater than or equal to 1)
as well as a time cost (either a 1, 2 or 3) to travel along that edge.
Design an O(mn) algorithm that determines whether it is possible for you to safely reach your
destination without exceeding your budget or being late for the performance.
"""
import math


def bellman_ford_modified(edge_list, vertices, source, destination, cost_budget, time_budget):
    """
    bellman ford algorithm that calculates the shortest path weight to each node from a
    defined source , else finds negative weight cycle
    :param destination: the destination
    :param time_budget: time budget
    :param cost_budget: cost budget
    :param edge_list: edge list
    :param vertices: number of vertices
    :param source: source node
    :return: None
    """

    # here we assume that the graph is connected, else the answer will be infinity

    # initialization step , based on source
    node_information = {}

    # we are going to also include extra information that stores the path length as well
    # the node info is as : [cost of path to node from src , parent , path_length]
    for i in range(0, vertices):
        node_information[i] = [float('inf'), None, 0]

    # initialize the start vertex , the source will always have 0 weight unless of
    # course you have a negative weight cycle
    node_information[source][0] = float(0)
    # the above is like the first iteration

    new_node_information = {}
    for key, val in node_information.items():
        new_node_information[key] = val.copy()

    # print("the new node information is : ")
    # print(str(new_node_information))

    for it_number in range(1, min(vertices, time_budget + 1)):
        # iterations are from 1 to n-1
        # at every iteration , the path length is atleast = it_number
        # print("iteration number : " + str(it_number))
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

                if node_information[u][0] + edge_info[2] < new_node_information[v][0] \
                        and node_information[u][2] + 1 <= it_number:
                    # print("the edge considered is : " + str(u) + " -> " + str(v))
                    new_node_information[v][0] = node_information[u][0] + edge_info[2]
                    # update the parent of v as u
                    new_node_information[v][1] = u
                    # update the path length
                    new_node_information[v][2] = node_information[u][2] + 1
                    # change made counter
                    updates += 1

        # print("the number of updates we have in this iteration are : " + str(updates))

        '''
        if updates == 0:
            print("actually we do not require only more update steps !!!")
        
        print("****")
        # print(str(node_information))
        for node, info in node_information.items():
            print(str(node) + " : " + str(info))
        print("\n")

        # print(str(new_node_information))
        for node, info in new_node_information.items():
            print(str(node) + " : " + str(info))
        print("\n")
        print("****")
        '''
        for key, val in new_node_information.items():
            node_information[key] = val.copy()

    # print("the cost is : " + str(new_node_information[destination][0]))
    # print("the budget is : " + str(float(cost_budget)))

    # so we to compare floats and avoid precision errors i use epsilon
    e = 0.00000000001
    if (new_node_information[destination][0] < float(cost_budget)) \
            or (abs(new_node_information[destination][0] - float(cost_budget)) <= e):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    # the input will be read and stored as an edge-list
    line = list(input().strip().split())
    number_of_travel_locations = int(line[0])  # Read number of vertices
    # print("the number of nodes are : " + str(number_of_travel_locations))

    line = list(input().strip().split())
    travel_edges = int(line[0])  # Read number of edges
    # print("the number of edges are : " + str(travel_edges))

    line = list(input().strip().split())
    cost_budget = int(line[0])  # Read cost budget
    # print("the cost budget is : " + str(cost_budget))

    line = list(input().strip().split())
    time_budget = int(line[0])  # Read time budget
    # print("the time budget is : " + str(time_budget))

    # we will store the graph as an edge list
    # info is as : [u , v , cost , time]
    edge_list = []

    for index in range(0, travel_edges):
        line = list(input().strip().split())
        edge_list.append([min(int(line[0]), int(line[1])), max(int(line[0]), int(line[1])),
                          int(line[2]), int(line[3])])
    '''
    print("the edges stored are as : ")
    for edge_info in edge_list:
        print(str(edge_info))

    print()
    '''
    # print("the number of edges are : " + str(travel_edges))

    # we are going to modify the edges for 1 length time only
    new_node_number = number_of_travel_locations
    modified_edge_list = []
    for edge_info in edge_list:
        start = edge_info[0]
        end = edge_info[1]
        cost = edge_info[2]
        time = edge_info[3]

        nodes = []

        if time == 1:
            nodes = [start, end]

        elif time == 2:
            nodes = [start, new_node_number, end]
            new_node_number += 1

        else:
            nodes = [start, new_node_number, new_node_number + 1, end]
            new_node_number += 2

        for index in range(1, len(nodes)):
            modified_edge_list.append((nodes[index], nodes[index - 1], float(cost / time)))
            modified_edge_list.append((nodes[index - 1], nodes[index], float(cost / time)))

    travel_edges = len(modified_edge_list)
    # print("the number of edges are : " + str(travel_edges))
    new_number_of_travel_locations = new_node_number
    # print("the new number of vertices are : " + str(number_of_travel_locations))

    '''
    print("the modified edge list : ")
    for info in modified_edge_list:
        print(str(info))
    '''
    bellman_ford_modified(modified_edge_list, new_number_of_travel_locations, 0, number_of_travel_locations - 1,
                          cost_budget, time_budget)
