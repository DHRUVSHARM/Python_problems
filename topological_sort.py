from typing import List 
import collections

# in this problem we will do both the cycle detection as well as finding the topological ordering 

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # directed graph
        # nodes : [ 0 , n - 1 ]
        adj , visited , path = collections.defaultdict(list) , set() , set()

        for u , v in edges:
            adj[u].append(v)
        
        def dfs(node) -> list:
            visited.add(node)
            path.add(node)

            ordering = []
            for nei in adj[node]:
                if nei in path:
                    # the node was found in current path 
                    return []
                if nei not in visited:
                    sub_ordering = dfs(nei)
                    if sub_ordering == []:
                        # cycle was detected , return with out exploring further 
                        return sub_ordering
                    ordering.extend(sub_ordering)
            
            path.remove(node)
            ordering.extend(node)

            return ordering

        result = []
        for start in range(0 , n):
            if start not in visited:
                ordering = dfs(start)
                
                if not len(ordering):
                    return ordering
                else:
                    result.extend(ordering)
        
        
        result.reverse()
        return result




