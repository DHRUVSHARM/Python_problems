"""
Given is a d1 × d2 array of integer values, representing a maze. One cell is marked as
the entry point. Another cell is marked as the exit point. The remainder of the cells are
either open, or blocked. You enter the maze with one stick of dynamite, that can be used
on any blocked location to convert it into an open location. Give an O(d1d2) algorithm
that determines the shortest path from the entry point to the exit point that uses no more
than one stick of dynamite.
"""

import math
from collections import deque


def bfs_shortest_possible_path(graph, d1, d2, start, end, end_with_blown):
    """

    :param graph:
    :param d1:
    :param d2:
    :param start:
    :param end:
    :param end_with_blown:
    :return:
    """

    queue = deque()
    queue.append(start)

    # every entry in this 3d matrix is a list containing 2 values in order , layered path length
    # and visited or not
    node_information = [
        [[[math.inf, False] for k in range(2)] for j in range(d2)] for i in range(d1)
    ]
    # print("the node info 3d matrix is : ")
    """
    node_num = 1
    for i in range(0 , d1):
        for j in range(0 , d2):
            for k in range(0 , 2):
                print("node num : " + str(node_num))
                node_num += 1
                print(str(node_information[i][j][k]))
    """

    node_information[start[0]][start[1]][start[2]][1] = True
    node_information[start[0]][start[1]][start[2]][0] = 0

    # the start point is visited

    # the directions are
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    while not len(queue) == 0:
        frontier = queue.popleft()
        x = frontier[0]
        y = frontier[1]
        z = frontier[2]
        neighbours = []
        for element in directions:
            x_new = x + element[0]
            y_new = y + element[1]
            z_new = z

            if 0 <= x_new < d1 and 0 <= y_new < d2:
                # the base grid is in range
                if grid[x_new][y_new] == "0" or grid[x_new][y_new] == "3":
                    # we have no restriction and can move in the same grid
                    neighbours.append((x_new, y_new, z_new))
                else:
                    # there is a dynamite at this position , only if we are at level 0 can we move up
                    # else we need to exclude this
                    if z_new == 0:
                        neighbours.append((x_new, y_new, z_new + 1))

        for neighbour in neighbours:
            x = neighbour[0]
            y = neighbour[1]
            z = neighbour[2]
            if node_information[x][y][z][1] is False:
                # unvisited
                queue.append(neighbour)
                node_information[x][y][z][0] = (
                    node_information[frontier[0]][frontier[1]][frontier[2]][0] + 1
                )
                node_information[x][y][z][1] = True

        """
        print("node info after traversal is as : ")
        for i in range(0, d1):
            for j in range(0, d2):
                for k in range(0, 2):
                    print("node is : " + str(i) + " , " + str(j) + " , " + str(k))
                    print(str(node_information[i][j][k]))
        """
    print(
        str(
            min(
                node_information[end[0]][end[1]][end[2]][0],
                node_information[end_with_blown[0]][end_with_blown[1]][
                    end_with_blown[2]
                ][0],
            )
        )
    )


if __name__ == "__main__":
    d1 = int(input())
    d2 = int(input())
    grid = []
    for _ in range(0, d1):
        line = list(input().strip().split())
        grid.append(line)

    """
    print("d1 , d2 and grid is as : ")
    print(str(d1))
    print(str(d2))
    for l in grid:
        print(str(l))
    """
    # start is at 2 and end is at 3 always
    # every node is represented as a tuple of 3 values (i , j , 0/1 depending on weather object was blown
    start = ()
    end = ()
    end_with_blown = ()
    for i in range(0, d1):
        for j in range(0, d2):
            if grid[i][j] == "2":
                start = (i, j, 0)
            elif grid[i][j] == "3":
                end = (i, j, 0)
    end_with_blown = (end[0], end[1], 1)

    """
    print("the start and end / end-blown nodes are as : " + str(start) + " , " + str(end) + ", " +
          str(end_with_blown))
    """
    bfs_shortest_possible_path(grid, d1, d2, start, end, end_with_blown)
