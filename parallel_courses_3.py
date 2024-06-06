import collections
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj, incoming_edges, minimal_time = (
            {node + 1: [] for node in range(n)},
            {node + 1: 0 for node in range(n)},
            -1,
        )

        for pre_req, course in relations:
            adj[pre_req].append(course)
            incoming_edges[course] += 1

        sources, dp = [], {}
        for node, incoming_edges_count in incoming_edges.items():
            if incoming_edges_count == 0:
                sources.append(node)

        # print(sources)

        def dfs(node) -> int:
            if node in dp:
                return dp[node]

            result = time[node - 1]
            for neighbour in adj[node]:
                result = max(result, time[node - 1] + dfs(neighbour))
            # print(node , result)

            dp[node] = result
            return result

        for src in sources:
            minimal_time = max(minimal_time, dfs(src))
        return minimal_time
