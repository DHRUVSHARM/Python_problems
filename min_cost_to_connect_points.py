import collections
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, adj = len(points), collections.defaultdict(list)

        def cost(xi, yi, xj, yj):
            return abs(xi - xj) + abs(yi - yj)

        # we will create a graph that is completely connected graph
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                connection_cost = cost(xi, yi, xj, yj)
                adj[(xi, yi)].append((xj, yj, connection_cost))
                adj[(xj, yj)].append((xi, yi, connection_cost))

        node_information = {tuple(point): [float("inf"), None] for point in points}
        src = tuple(points[0])
        node_information[src][0] = 0
        fixed = {tuple(point): False for point in points}
        fixed[src] = True
        tree = []

        def update(node):
            for nx, ny, edge_wt in adj[node]:
                if not fixed[(nx, ny)]:
                    if edge_wt < node_information[(nx, ny)][0]:
                        node_information[(nx, ny)][0] = edge_wt
                        node_information[(nx, ny)][1] = node

        def get_min():
            minimal_node, minimal_wt = None, float("inf")
            for node in node_information:
                if not fixed[node]:
                    if node_information[node][0] < minimal_wt:
                        minimal_wt = node_information[node][0]
                        minimal_node = node
            return minimal_node

        update(src)

        for iteration in range(0, n - 1):
            curr_node = get_min()
            if curr_node is None:
                break

            tree.append((curr_node, node_information[curr_node][1], node_information[curr_node][0]))
            fixed[curr_node] = True
            update(curr_node)

        # the graph is guaranteed to be connected, so no need for a disconnected graph check
        minimal_connection_cost = 0
        for _, _, edge_wt in tree:
            minimal_connection_cost += edge_wt

        return minimal_connection_cost