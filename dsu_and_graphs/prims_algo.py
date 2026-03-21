from typing import List

"""
Input:
n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]

Output:
11


greedy algo
maximizes the total weight of the tree created 
add the edges, 
pull out and fix the edge with the least weight 

simple minimal edge selection 
if you try to add something already fixed then 

does not have to have a src


"""

import heapq
import collections
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # we can start with 0 
        visited , q , adj = set() , [(0 , 0)] , collections.defaultdict(list)

        for u , v , w in edges:
            adj[u].append((v , w))
            adj[v].append((u , w))


        # now there will be at max n iterations 
        # we will pop each node once at max to finalize 

        iterations , result = n , 0 # in case of a connected graph 

        while iterations and len(q):
            # we can pop the least node 
            w , node = heapq.heappop(q)
            if node not in visited:
                visited.add(node)
                iterations -= 1
                # simple edge weight add 
                result += w
            
            for nei , nei_w in adj[node]:
                if nei not in visited:
                    heapq.heappush(q , (nei_w , nei))

        
        return -1 if iterations > 0 else result
