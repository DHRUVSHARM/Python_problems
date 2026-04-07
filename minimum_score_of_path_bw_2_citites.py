"""
You are given a positive integer n 

representing n cities numbered from 1 to n. 

You are also given a 2D array roads where roads[i] = [ai, bi, distancei] 

indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. 

The cities graph is not necessarily connected. - imp 

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.



path  : thread that will cover all the nodes in a component 
there is at least one pat between 1 and n means, 1 and n are in the same connected component ? 
just finnd the minimal edge weight in the component starting from 1

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.


dp[i] = minimal edge weight from i to n

we need dp[1]

dp[i] min across i , nei edges, adn dp[edges] formed as a result of that

"""

from typing import List
import collections

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj , visited , edges_seen = collections.defaultdict(list) , set() , set()

        for u , v , dist in roads:
            adj[u].append((v , dist))
            adj[v].append((u , dist))
        

        result = [float("inf")]

        def dfs(node):
            visited.add(node)

            for nei , edge_wt in adj[node]:
                if edge_wt not in edges_seen:
                    result[0] = min(result[0] , edge_wt)
                    edges_seen.add(edge_wt)
                    
                if nei not in visited:
                    dfs(nei)
                
        # 1 and n in same component
        dfs(1)
        return result[0]