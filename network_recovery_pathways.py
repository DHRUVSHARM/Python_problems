from typing import List

"""
You are given a directed acyclic graph of 
n nodes numbered from 0 to n − 1. 
This is represented by a 2D array edges of length m, where edges[i] = [ui, vi, costi] indicates a one‑way communication from node ui to node vi with a recovery cost of costi.

Some nodes may be offline. 
You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n − 1 are always online.

A path from 0 to n − 1 is valid if:

All intermediate nodes on the path are online.
The total recovery cost of all edges on the path does not exceed k.
For each valid path, define its score as the minimum edge‑cost along that path.

Return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.


algorithm:
-   if no valid path (can use simple dfs) we can return -1 

if we can fix a min cost x, 
    then we can use topological ordering dfs to get minimal cost from 0 to n - 1 valid and check if <= k  alll online and at least x edge cost

T T T T T T T F F F F F F 
l = 0 , r = k + 1 will always be false 


online is already mapped 
0 - n - 1


dp[n - 1] = 0

dp[u] = min(
    for all v , u - v + dp[v] (and v is after u in topological order)
)

final answer in dp[0]

since we are guaranteed DAG, should be able to correctly do the dp 
"""
import collections
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        adj = collections.defaultdict(list)

        n = len(online) - 1 # n - 1

        for u , v , c in edges:
            # n = max(n , u , v)
            adj[u].append((v , c))

        # print("n : " , n)

        # visited = set()
        dp = {}

        # dfs node is minimal cost to reach 
        def dfs(node , min_cost):
            nonlocal n
            # visited.add(node)
            if node in dp:
                return dp[(node)]
            
            dp[node] = float("inf")
            if node == n:
                dp[node] = 0 
            else:
                for nei, nei_w in adj[node]:
                    if online[nei] and nei_w >= min_cost:
                        # can explore 
                        dp[node] = min(
                            dp[node],
                            nei_w + dfs(nei , min_cost)
                        )

            return dp[node]

        # reachable
        path_score = float("inf")
        if n >= 0: 
            path_score = dfs(0 , 0)
        # print(dp)

        if path_score > k:
            return -1 

        left , right = 0 , k + 1

        while left + 1 < right:
            # visited = set()
            dp = {}
            
            mid = (left + right) // 2
            path_score = dfs(0 , mid)

            if path_score <= k:
                left = mid
            else:
                right = mid

        return left