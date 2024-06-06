"""
author : Dhruv Sharma , Mona Anil Udasi

Consider the problem of students registering for courses. For each student, you are given a set of
courses that the student is willing and able to take. No student may take more than 3 courses. Each
course also has a maximum number of students than can enroll, though this may be different for
different courses. Create an efficient algorithm that will compute the maximum sum of registered
students over all courses.
"""

import copy
import math
from collections import deque


def bfs(graph, src, dest, n, capacity):
    """
    bfs algo that returns path from src to dest , else None
    :param capacity: capacity in graph
    :param n: number of nodes
    :param graph: ip
    :param src:  source
    :param dest: destination

    :return:

    """
    # o(m + n) algorithms
    # here graph is an adjacency list
    queue = deque()
    queue.append(src)
    # parent is enough
    node_information = [[False, None] for _ in range(n)]
    node_information[src][0] = True
    while not len(queue) == 0:
        frontier = queue.popleft()
        for neighbour in graph[frontier]:
            if (
                node_information[neighbour][0] is False
                and capacity[frontier][neighbour] != 0
            ):
                # only unvisited and neighbours with some cap to reach
                queue.append(neighbour)
                node_information[neighbour][0] = True
                node_information[neighbour][1] = frontier

    """
    print("after traversal printing the bfs node information : ")
    for i in range(0, n):
        print(str(i) + " : " + str(node_information[i]))
    """
    if node_information[dest][0] is False:
        # cannot reach dest
        return None
    else:
        # get the path
        path = []
        curr = dest
        while curr is not None:
            path.append(curr)
            curr = node_information[curr][1]
        path.reverse()
        # print("the path from src to dest : " + str(path))
        return path


def ford_fulkerson(al, c, f, residual_al, residual_c, n, s, t, forward):
    """
    function to get the maximal flow (ans)
    :param forward: to check if an edge is a forward edge
    :param t:dest
    :param s:src
    :param al:real graph
    :param c:real graph cap'
    :param f:real graph flow
    :param residual_al: residual graph
    :param residual_c: residual graph cap
    :param n: number of nodes
    :return: None
    """

    while True:
        path = bfs(residual_al, s, t, n, residual_c)
        if path is None:
            break
        bottleneck = math.inf
        for i in range(1, len(path)):
            start = path[i - 1]
            end = path[i]
            bottleneck = min(bottleneck, residual_c[start][end])
        # now iterate over the edges
        for i in range(1, len(path)):
            start = path[i - 1]
            end = path[i]
            if forward[start][end]:
                f[start][end] += bottleneck
            else:
                f[end][start] -= bottleneck
            # also have to update Gf alongside
            # since start -> end was done , we subtract from this capacity
            residual_c[start][end] -= bottleneck
            if residual_c[end][start] == 0:
                residual_al[end].append(start)
            residual_c[end][start] += bottleneck
            # backward edges are taken care of

    max_flow = 0
    for neighbour in al[s]:
        max_flow += f[s][neighbour]

    print(str(max_flow))


if __name__ == "__main__":
    line = list(input().strip().split())
    number_of_students = int(line[0])  # Read the number of students
    number_of_courses = int(line[1])  # Read the number of courses

    # print("the number of students are : " + str(number_of_students))
    # print("the number of courses are : " + str(number_of_courses))

    # so in our graph the src imagined will be 0 (s)
    # the course nodes are numbered as [1 - c]
    # the student nodes will be numbered from [c+1 - c+s]
    # c + s + 1 is the sink node (t)

    number_of_nodes = number_of_courses + number_of_students + 2
    # print("the final number of nodes are : " + str(number_of_nodes))

    # stores the graph as an adjacency list
    adj_list = [[] for _ in range(number_of_nodes)]
    # capacity
    capacity = [[0 for j in range(number_of_nodes)] for i in range(number_of_nodes)]
    # flow
    flow = [[0 for j in range(number_of_nodes)] for i in range(number_of_nodes)]
    # flow and capacity of our directed graph
    is_forward = [
        [False for j in range(number_of_nodes)] for i in range(number_of_nodes)
    ]

    # the src is connected to all the student nodes

    for student in range(
        number_of_courses + 1, number_of_courses + number_of_students + 1
    ):
        adj_list[0].append(int(student))
        capacity[0][student] = 3  # each student can take max 3 courses
        flow[0][student] = 0
        is_forward[0][student] = True
        # keeping track of forward edges

    # the students are connected to courses of their choice
    for student in range(
        number_of_courses + 1, number_of_courses + number_of_students + 1
    ):
        courses_willing = list(input().strip().split())
        # print("the courses willing for student " + str(student) + " is : " + str(courses_willing))
        for course in courses_willing:
            adj_list[student].append(int(course))
            capacity[student][int(course)] = 1  # each student can take 1 course once
            flow[student][int(course)] = 0
            is_forward[student][int(course)] = True
            # keeping track of forward edges

    # the capacity edges are at the end to sink , which is number of nodes - 1
    for course in range(1, number_of_courses + 1):
        line = list(input().strip().split())
        course_capacity = int(line[0])
        # print("the course capacity for course : " + str(course) + " is " + str(course_capacity))
        adj_list[course].append(number_of_nodes - 1)
        capacity[course][
            number_of_nodes - 1
        ] = course_capacity  # capacity bound courses
        flow[course][number_of_nodes - 1] = 0
        is_forward[course][number_of_nodes - 1] = True
        # keeping track of forward edges

    """
    print("capacity : ")
    for r in capacity:
        print(str(r))

    print("flow : ")
    for r in flow:
        print(str(r))

    print("adj list : ")
    for index in range(0, len(adj_list)):
        print(str(index) + " : " + str(adj_list[index]))
    """
    # this is our main graph
    residual_adjacency_list = copy.deepcopy(adj_list)
    residual_capacity = copy.deepcopy(capacity)
    residual_flow = copy.deepcopy(flow)

    """
    print("the residual graph is : ")
    for index in range(0, len(residual_adjacency_list)):
        print(str(index) + " : " + str(residual_adjacency_list[index]))
    """
    ford_fulkerson(
        adj_list,
        capacity,
        flow,
        residual_adjacency_list,
        residual_capacity,
        number_of_nodes,
        0,
        number_of_nodes - 1,
        is_forward,
    )
