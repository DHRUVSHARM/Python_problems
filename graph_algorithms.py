import math
from collections import deque

"""
some sample code for deque that will help with queue o(1) implementation

queue = deque()

# adding elements to the queue
queue.append(10)
queue.append(20)
queue.append(30)

# removing elements from the queue
x = queue.popleft()
y = queue.popleft()

print(x)  # prints 10
print(y)  # prints 20
print(queue)  # prints deque([30])

"""


class Graph:
    def __init__(self):
        # dictionary of vertices with values as a list of vertex neighbours
        self.adj_list = {}

    def add_edge(self, u, v):
        # this adds edge function assumes directed graph ,
        # for undirected graphs the ip should handle it
        # directed edge from u -> v
        if u not in self.adj_list:
            self.adj_list[u] = []

        self.adj_list[u].append(v)
        # self.adj_list[v].append(u)

    def print_graph(self):
        # for every vertex , we print their neighbours
        for vertex in self.adj_list:
            print(vertex + " : ", end="")
            for neighbor in self.adj_list[vertex]:
                print(" -> ", neighbor, end="")
            print()


def bipartite_graph_test(graph, root):
    """
    this function uses bfs to detect odd cycles. Graph with no odd cycle is
    bipartite otherwise no
    :param graph: the graph that uses an adjacency list to store the graph
    :param root: the start point
    :return: true if bipartite else false
    """
    # o(m + n) algorithm

    queue = deque()
    queue.append(root)
    # used to check if nodes were visited , and also stores the layered distance and parent
    # for building a path if required
    node_information = {root: (0, None)}
    # root has 0 distance and None as the parent
    while not len(queue) == 0:
        frontier = queue.popleft()
        for neighbour in graph.adj_list[frontier]:
            if neighbour not in node_information:
                queue.append(neighbour)
                node_information[neighbour] = (
                    node_information[frontier][0] + 1,
                    frontier,
                )
            else:
                # here we have neighbours that are already visited by some other way
                # so here we check if there is a neighbour which is at the same level
                # as the frontier
                if node_information[neighbour][0] == node_information[frontier][0]:
                    # means we have an odd cycle . so not possible to be bipartite
                    return False

    return True


def bfs(graph, root):
    """
    bfs with layered approach
    :param graph: the graph that uses an adjacency list to store the graph
    :param root: the start point
    :return:
    """
    # o(m + n) algorithms

    queue = deque()
    queue.append(root)
    # used to check if nodes were visited , and also stores the layered distance and parent
    # for building a path if required
    node_information = {root: (0, None)}
    # root has 0 distance and None as the parent
    while not len(queue) == 0:
        frontier = queue.popleft()
        for neighbour in graph.adj_list[frontier]:
            if neighbour not in node_information:
                queue.append(neighbour)
                node_information[neighbour] = (
                    node_information[frontier][0] + 1,
                    frontier,
                )

    print("after traversal printing the bfs node information : ")
    for node, info in node_information.items():
        print(node + " " + str(info))


def dfs_stack(graph, root):
    """
    this function does dfs using a stack
    :param graph: the graph that uses an adjacency list to store the graph
    :param root: the start point
    :return:
    """

    # O(m + n) algorithm
    # again we will use deque to implement the stack , actually this is one of the
    # few things that change from our bfs algorithm

    stack = deque()
    stack.append(root)
    # no sense of storing distance as it is not the shortest like bfs
    node_information = {root: None}

    while not len(stack) == 0:
        frontier = stack.pop()
        for neighbour in graph.adj_list[frontier]:
            if neighbour not in node_information:
                stack.append(neighbour)
                node_information[neighbour] = frontier

    print("after traversal printing the dfs stack node information : ")
    for node, info in node_information.items():
        print(node + " " + str(info))


def dfs_recursive(graph, root, node_info):
    """
    recursive function for dfs
    :param node_info: stores the node information
    :param graph: the graph that uses an adjacency list to store the graph
    :param root: the start point
    :return:
    """
    """
    we mark the node as visited and store some info on it
    """
    if root not in node_info:
        node_info[root] = None
        # this is the only time we will be here other times we will already add a parent
        # and send nodes for further recursive calls

    for neighbour in graph.adj_list[root]:
        if neighbour not in node_info:
            node_info[neighbour] = root
            dfs_recursive(graph, neighbour, node_info)

    return


def top_ordering_no_incoming_algo(graph):
    """
    this o(m+n) function uses a stack and keeps track of incoming edges
    :param graph: ip
    :return: None
    """

    # we initialize the incoming edge array
    incoming_edges = {}
    for node in graph.adj_list:
        incoming_edges[node] = 0

    for node, neighbours in graph.adj_list.items():
        for neighbour in neighbours:
            incoming_edges[neighbour] += 1

    print("the initial count of incoming edges are as : ")
    print(str(incoming_edges))

    # initialization is O(n)
    stack = deque()
    for node in incoming_edges:
        if incoming_edges[node] == 0:
            stack.append(node)

    # this is O(m+n) as we process every edge once to delete ,we find the value in
    # incoming edge in o(1)

    topological_ordering = []

    while len(stack) != 0:
        frontier = stack.pop()
        # we have to remove incoming edges coming from frontier
        # and we put it into the topological ordering
        topological_ordering.append(frontier)
        for neighbour in graph.adj_list[frontier]:
            incoming_edges[neighbour] -= 1
            if incoming_edges[neighbour] == 0:
                # newly created node candidate
                stack.append(neighbour)

    is_dag = True
    for node, left_incoming in incoming_edges.items():
        if left_incoming != 0:
            is_dag = False
            break

    if is_dag:
        print("this is a DAG and has a valid topological ordering : ")
        print(str(topological_ordering))
    else:
        print("stack is empty but there are nodes , -> there is a cycle !!!")


def dfs_finish_and_visit(root, graph2: Graph, visit_and_finish, node_information):
    """
    recursive function with finish time implemented
    :param root: root
    :param graph2: graph
    :param visit_and_finish: visit , finish
    :return: None
    """

    # we have visited this node
    visit_and_finish[0] += 1
    node_information[root][0] = visit_and_finish[0]

    for neighbours in graph2.adj_list[root]:
        for neighbour in neighbours:
            if node_information[neighbour][0] == -1:
                # unvisited node is a neighbour , we need to visit it now
                dfs_finish_and_visit(
                    neighbour, graph2, visit_and_finish, node_information
                )

    # this node's work is finished
    visit_and_finish[1] += 1
    node_information[root][1] = visit_and_finish[1]


def top_ordering_dfs_finish_times(graph2):
    """
    we will use dfs finish times to check if the graph is a DAG and provide
    the topological ordering
    :param graph2: ip
    :return: None
    """

    node_information = {}
    # we will store the visit order and the finish times in this dictionary
    # this will also serve as a visited marker
    for node in graph2.adj_list:
        node_information[node] = [-1, math.inf]

    print("the initial node information dictionary is : ")
    for node, node_info in node_information.items():
        print(node + " : " + str(node_info))

    # we are visiting the nodes in a particular order
    # the visit order and the finish time are as a list

    visit_and_finish = [0, 0]

    for node in graph2.adj_list:
        if node_information[node][0] == -1:
            # unvisited node
            dfs_finish_and_visit(node, graph2, visit_and_finish, node_information)

    print("the final node information for our algo is as : ")
    for node, node_info in node_information.items():
        print(node + " : " + str(node_info))

    """
    the topological order is reverse finish times nodes
    if there is a cycle , then when you go through the DAG you will see that there 
    is an edge from low to high finish time
    """


if __name__ == "__main__":
    graph = Graph()
    # building the graph
    """
    ip = {
        'S': ('A', 'F', 'H'),
        'A': ('B', 'D', 'G', 'S'),
        'B': ('A', 'C'),
        'C': ('B', 'D'),
        'D': ('A', 'C', 'F'),
        'F': ('D', 'S'),
        'H': 'S'
    }
    """
    """
    ip = {
        'S': ('A', 'F', 'H'),
        'A': ('B', 'D', 'G', 'S'),
        'B': ('A', 'D'),
        'C': ('E', 'F', 'H'),
        'D': ('A', 'B'),
        'F': ('C', 'E', 'S'),
        'H': ('C', 'I', 'S'),
        'G': 'A',
        'E': ('C', 'F', 'I'),
        'I': ('E', 'H')
    }
    """
    """
    ip = {
        '1': ('2', '3'),
        '2': ('1', '4'),
        '3': ('1', '4'),
        '4': ('2', '3')

    }

    for node, neighbours in ip.items():
        print("neighbour list:  " + str(neighbours))
        for neighbour in neighbours:
            graph.add_edge(node, neighbour)

    print("printing the graph")
    graph.print_graph()
    print("bfs traversal")
    root = '1'
    bfs(graph, root)
    print("\n *********************************************************** \n")
    # now we will also use dfs
    print("dfs traversal with a stack")
    dfs_stack(graph, root)
    print("\n *********************************************************** \n")
    # now we will also use dfs
    print("dfs traversal recursive")
    recursive_dfs_information = {}
    dfs_recursive(graph, root, recursive_dfs_information)
    print("after traversal printing the dfs recursive node information : ")
    for node, info in recursive_dfs_information.items():
        print(node + " " + str(info))
    print("is bipartite : ")
    print(bipartite_graph_test(graph, root))
    """

    # directed graph ip to get topological order and thus conclude if the graph is a DAG
    directed_ip = {
        "A": "C",
        "B": (),
        "C": "B",
        "D": ("A", "B", "C", "E"),
        "E": ("A", "B"),
    }

    for node, neighbours in directed_ip.items():
        # print("neighbour list:  " + str(neighbours))
        for neighbour in neighbours:
            graph.add_edge(node, neighbour)

        if node not in graph.adj_list:
            graph.adj_list[node] = []

    print("the graph ip is : ")
    graph.print_graph()

    top_ordering_no_incoming_algo(graph)
    print("****************************************************\n")
    graph2 = Graph()
    directed_ip_2 = {
        "A": ("B", "C", "E"),
        "B": "H",
        "C": (),
        "D": ("A", "C", "E"),
        "E": (),
        "F": ("C", "G", "H"),
        "G": ("C", "E", "H"),
        "H": (),
    }

    for node, neighbours in directed_ip_2.items():
        # print("neighbour list:  " + str(neighbours))
        for neighbour in neighbours:
            graph2.add_edge(node, neighbour)

        if node not in graph2.adj_list:
            graph2.adj_list[node] = []

    print("the graph ip 2 is : ")
    graph2.print_graph()

    top_ordering_dfs_finish_times(graph2)
