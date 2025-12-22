from typing import List
import collections

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        adj = collections.defaultdict(list)

        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        # we recognize that at least the final compiled answer will be 1 at the minimum
        # we will select 0 as the root since the graph is connected and has nodes from 0 - n-1
        ans , visited = 0 . set()

        def dfs(node):
            visited.add(node)
            component_count , component_sum = 0 , values[node]
            
            
            for neighbour in adj[node]:
                if neighbour not in visited:
                    neighbour_component_count , neighbour_component_sum = dfs(neighbour)
                    component_count += neighbour_component_count
                    component_sum += neighbour_component_sum
            
            if component_sum % k == 0:
                return component_count + 1 , component_sum
            else:
                return component_count , component_sum
            

        ans , _ = dfs(0)
        return ans