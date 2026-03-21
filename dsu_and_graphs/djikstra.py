import heapq
from typing import List , Optional , Dict


"""
n - the number of vertices in the graph, where (2 <= n <= 100). Each vertex is labeled from 0 to n - 1.

edges - a list of tuples, each representing a directed edge 
in the form (u, v, w), where u is the source vertex, v is the destination vertex, and w is the weight of the edge, where (1 <= w <= 10).

src - the source vertex from which to start the algorithm, where (0 <= src < n).

return dict
{node : dist from src mapping}

Note: If a vertex is unreachable from the source vertex, the shortest path distance for the unreachable vertex should be -1.
"""

import collections
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = collections.defaultdict()
        for node in range(0 , n):
            adj[node] = []
        

        for s , d , w in edges:
            adj[s].append((d , w))
        
        q , result , iterations = [(0 , src)] , {} , n

        while iterations and len(q):
            w , node = heapq.heappop(q)
            if node not in result:
                # update weight and add to result set
                result[node] = w
                iterations -= 1
            
                # update the heap by adding neighbours of the newly popped node
                for nei , nei_w in adj[node]:
                    if nei not in result:
                        # we only need to make sure we do not visit the fixed nodes again 
                        heapq.heappush(q , (w + nei_w , nei))


        # can add a check here to see in case the heap emptied before requrired iterations 
        for node in range(0 , n):
            if node not in result:
                result[node] = -1

        return result