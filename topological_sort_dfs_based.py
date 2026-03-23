# practice topo sort again 
from typing import List


"""

top ordering from any point can be got by postorder dfs

put last node first in the end we reverse

5 10 3 3 100 1 4 2 

reverse in the end


visited : add means visited 
visited with false means in current 
mark true to before moving to be in the current path 
mark false when going back to indicate not in current path 

if we see a cycle in the current path means cycle 
return []
if []
from anywhere return [] again till end 

break and return since sending with one element the topo should be of size one atleast

forward loop is ok 



        1
    
    2       100 t

    4       3  t

    10      3  t

        5   f   10  t

"""

import collections
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # multiple edges and self loops will be handled
        # we will not add redundant nodes into the path 
        # so multiple edges should not affect
        # for self loops that will be detected as a cycle 
        # we know the nodes are 0 to n - 1
        
        visited , adj = {} , collections.defaultdict(list)

        for u , v in edges:
            adj[u].append(v)
        
        def dfs(node):
            # node here is unvisited 
            ordering = []
            visited[node] = True # mark in current path 
            
            for nei in adj[node]:
                if nei in visited and visited[nei] == True:
                    return []
                
                if nei not in visited:
                    sub_ordering = dfs(nei)
                    if len(sub_ordering) == 0:
                        return []
                    ordering.extend(sub_ordering)

            visited[node] = False # remove since not in current path 
            ordering.append(node)

            return ordering

        result = []
        for node in range(0 , n):
            if node not in visited:
                subans = dfs(node)
                if len(subans) == 0:
                    result = []
                    break
                result.extend(subans)


        result.reverse()
        return result
        


