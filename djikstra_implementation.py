import collections
from typing import List, Dict


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = collections.defaultdict(list)
        for u, v, weight in edges:
            adj_list[u].append((v, weight))

        distance, fixed = {node: float("inf") for node in range(n)}, {
            node: -1 for node in range(n)
        }
        distance[src] = 0

        for iteration in range(0, n):
            minimal_distance, minimal_node = float("inf"), None
            # o(n) to find the minimal node
            for node, dist in distance.items():
                if fixed[node] == -1 and (
                    minimal_node is None or (dist < minimal_distance)
                ):
                    minimal_node, minimal_distance = node, dist

            # print("----> " , minimal_node , " " , minimal_distance)

            if minimal_node is None:
                # all other nodes are unreachable
                break

            # fix this minimal_node
            fixed[minimal_node] = (
                -1 if minimal_distance == float("inf") else minimal_distance
            )

            # we update connections wrt minimal node
            for neighbour, neighbour_dist in adj_list[minimal_node]:
                if minimal_distance + neighbour_dist < distance[neighbour]:
                    distance[neighbour] = minimal_distance + neighbour_dist

        return fixed
