import collections
from typing import List

if __name__ == '__main__':
    # d = collections.defaultdict(list)
    # d[1] = [2 , None]
    # d[2] = [3 , "abs"]
    d = {1: [2, None], 2: [3, "abs"]}
    for val1, val2 in d.values():
        print(val1, " , ", val2)


# prims algo academic implementation
# uses the concept of the cut property to a great extent
# similar to djikstra but there is a diff in the update function
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # node info : node -> (cost to connect , parent)
        # fixed : keeps track of the nodes in the mst
        # tree : set of edges making up the mst
        node_information, fixed, tree = {node: [float("inf"), None] for node in range(n)}, \
                                        {node: False for node in range(n)}, []

        def update(node):
            # updates weights
            for neighbour, neighbour_wt in adj[node]:
                if not fixed[neighbour]:
                    if neighbour_wt < node_information[neighbour][0]:
                        node_information[neighbour][0] = neighbour_wt
                        # updating the parent
                        node_information[neighbour][1] = node

        def get_smallest():
            # gets the smallest node , None means nodes are unreachable
            minimal_node, minimal_wt = None, float("inf")
            for node, val in node_information.items():
                node_wt, _ = val
                if not fixed[node]:
                    if node_wt < minimal_wt:
                        minimal_wt = node_wt
                        minimal_node = node

            return minimal_node

        # we will start from the src = 0
        node_information[0][0] = 0
        fixed[0] = True
        update(0)

        for iteration in range(0, n - 1):
            # print("iteration ...")
            minimal_node = get_smallest()
            # print("minimal node:  " , minimal_node)
            if minimal_node is None:
                # disconnected graph
                break

            # fixing the minimal_node
            fixed[minimal_node] = True
            connection_cost, parent = node_information[minimal_node]
            # print("conncost , parent : " , connection_cost , " " , parent)
            tree.append((parent, minimal_node, connection_cost))

            update(minimal_node)

        if len(tree) < n - 1:
            return -1
        tree_wt = 0
        for _, _, w in tree:
            tree_wt += w

        return tree_wt
