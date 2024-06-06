import collections
import math
from typing import List

if __name__ == "__main__":
    pass


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list[tuple])
        # building a directed graph to track detonation
        # note we need to store the nodes with the entry index to differentiate between
        # bombs at the same location (imp !!!!)
        for i in range(0, len(bombs)):
            for j in range(0, len(bombs)):
                if i != j:
                    xi, yi, radius_i = bombs[i]
                    xj, yj, radius_j = bombs[j]
                    if math.pow(radius_i, 2) >= math.pow((xi - xj), 2) + math.pow(
                        (yi - yj), 2
                    ):
                        adj_list[(xi, yi, i)].append((xj, yj, j))

        print(adj_list)

        max_detonations_possible = 0

        def dfs(node: tuple, visited: set) -> int:
            visited.add(node)
            detonations = 0
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    detonations += dfs(neighbour, visited)
            return detonations + 1

        for index, bomb in enumerate(bombs):
            max_detonations_possible = max(
                max_detonations_possible, dfs((bomb[0], bomb[1], index), set())
            )

        return max_detonations_possible
