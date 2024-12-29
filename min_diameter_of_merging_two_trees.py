import collections
import heapq
from math import ceil
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def helper(edges):
            adj , visited = collections.defaultdict(list) , set()
            for u , v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            # this dfs will return (maximal leaf_path starting from the node , maximal_diameter through the (overall))
            def dfs(node):
                visited.add(node)
                max_diameter , maxHeap = 0 , []
                for v in adj[node]:
                    if v not in visited:
                        path , diameter = dfs(v)
                        max_diameter = max(max_diameter , diameter)
                        heapq.heappush(maxHeap , -1 * path)
                
                # find the top 2 longest paths if available
                path1 , path2 = 0 , 0
                if len(maxHeap) >= 2:
                    path1 = -1 * heapq.heappop(maxHeap)
                    path2 = -1 * heapq.heappop(maxHeap)
                elif len(maxHeap) == 1:
                    path1 = -1 * heapq.heappop(maxHeap)
                else:
                    pass

                max_diameter = max(max_diameter , path1 + path2)
                return path1 + 1 , max_diameter
            
            # return maximal diameter
            _ , ans = dfs(0)
            return ans

        dia_1 , dia_2 = helper(edges1) , helper(edges2)
        return max(
            dia_1,
            dia_2,
            1 + ceil(dia_1 / 2) + ceil(dia_2 / 2)
        )