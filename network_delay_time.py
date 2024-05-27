import collections
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj, node_information, fixed = collections.defaultdict(list) \
            , {node: float("inf") for node in range(1, n + 1)}, {node: False for node in range(1, n + 1)}

        for u, v, edge_wt in times:
            adj[u].append((v, edge_wt))

        def update(node):
            """
            update the neighbours of node
            :param node: current node
            :return: None
            """
            for neighbour, neighbour_wt in adj[node]:
                if not fixed[neighbour]:
                    if node_information[node] + neighbour_wt < node_information[neighbour]:
                        node_information[neighbour] = node_information[node] + neighbour_wt

        def get_min():
            """
            return the minimal node that is reachable and not fixed , else return None
            :return: minimal node / None
            """
            minimal_node, minimal_wt = None, float("inf")
            for node, node_wt in node_information.items():
                if not fixed[node] and node_wt < minimal_wt:
                    minimal_wt = node_wt
                    minimal_node = node

            return minimal_node

        fixed[k] = True
        # we only map nodes to the distance from src node k in this algo
        node_information[k] = 0
        update(k)
        disconnected = False

        for _ in range(0, n - 1):
            curr_node = get_min()
            if curr_node is None:
                disconnected = True
                break

            fixed[curr_node] = True
            update(curr_node)

        if disconnected:
            return -1
        else:
            time = float("-inf")
            for t in node_information.values():
                time = max(time, t)
            return time
