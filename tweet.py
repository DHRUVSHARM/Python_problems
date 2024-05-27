"""
Q4) Tweet! Given is a social network of n Twitter users. Each user “follows” some collection
of other individuals and will “retweet” messages received from those individuals. There
are a total of m instances of one user following another across the network of individuals.
Design an O(m+n) algorithm that determines the minimum number of individuals that
must be provided with an initial item to “tweet” to guarantee that all the individuals
in the network end up “tweeting” or “retweeting” the item.

"""
import math
import sys
from collections import deque

sys.setrecursionlimit(3000)


def dfs_finish_and_visit(root, nodes_list, finish, finish_time_and_is_visited, stack):
    # we have visited this node
    finish_time_and_is_visited[root][1] = True

    for neighbour in nodes_list[root]:
        if finish_time_and_is_visited[neighbour][1] is False:
            # unvisited node is a neighbour , we need to visit it now
            dfs_finish_and_visit(neighbour, nodes_list, finish, finish_time_and_is_visited, stack)

    # this node's work is finished
    finish[0] += 1
    finish_time_and_is_visited[root][0] = finish[0]
    stack.append(root)


def bfs(root, nodes_list, seen):
    """
    simple bfs to find visitable nodes
    :param root:
    :param nodes_list:
    :param seen:
    :return:
    """

    queue = deque()
    queue.append(root)
    seen[root] = True
    while not len(queue) == 0:
        frontier = queue.popleft()
        for neighbour in nodes_list[frontier]:
            if seen[neighbour] is False:
                queue.append(neighbour)
                seen[neighbour] = True


def minimal_items_required(adj_list, n):
    """
    function to calculate the minimal number of items required
    :param adj_list:
    :param n:
    :return:
    """

    # print("the number of nodes: " + str(n))

    finish_time_and_is_visited = []
    for _ in range(0, n):
        finish_time_and_is_visited.append([math.inf, False])

    # to pass finish by reference
    finish = [0]

    # stack to store the topological order efficiently in reverse order of finish time
    stack = deque()

    for node in range(0, n):
        if finish_time_and_is_visited[node][1] is False:
            # unvisited node
            dfs_finish_and_visit(node, nodes_list, finish, finish_time_and_is_visited, stack)

    # print("the final node information for our algo is as : ")
    '''
    for i in range(0, n):
        print(str(i) + " : " + str(finish_time_and_is_visited[i]))
    '''
    # now we will store the nodes in a topological order
    '''
    print("the reverse finish order : ")
    print(str(stack))
    '''
    # reinitializing the seen array
    seen = []
    for _ in range(0, n):
        seen.append(False)

    components = 0
    while len(stack) != 0:
        element = stack.pop()
        if seen[element] is False:
            bfs(element, nodes_list, seen)
            components += 1

    return components


if __name__ == '__main__':
    n = int(input())  # Read number of vertices
    # print("the number of nodes are : " + str(n))

    nodes_list = []
    # we will store the adjacency list as a tuple of tuples named nodes_list where the index
    # represents a node and the tuple at that point represent directed edges from it
    for i in range(0, n):
        line = list(input().strip().split())
        # print("the line read is : ")
        # print(str(line))
        followers = []
        for j in range(0, len(line)):
            if line[j] == '-1':
                break
            followers.append(int(line[j]))
        nodes_list.append(followers)

    # print("the adjacency list created is : ")
    '''
    for i in range(0, len(nodes_list)):
        print(str(i) + " : " + str(nodes_list[i]))
    '''
    print(str(minimal_items_required(nodes_list, n)))
