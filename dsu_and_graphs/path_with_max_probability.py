from typing import List

"""
n nodes
edge list input 

succprob maps edge index - probability 

0.5 * 0.5 = probability 

0.5 * 0.5 = 0.25
0.2

src .... result
src ...
"""

import collections
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)

        for index, edge in enumerate(edges):
            u , v = edge
            # undirected graph 
            adj[u].append((v , succProb[index]))
            adj[v].append((u , succProb[index]))

        # fixed will keep track of maximal probability 
        q , fixed = [(-1 , start_node)] , {}
        iterations = n

        while iterations and len(q):
            w , node = heapq.heappop(q)
            if node not in fixed:
                fixed[node] = -1 * w
                iterations -= 1
                if node == end_node:
                    return fixed[node]           

                # add the nei 
                for nei , nei_w in adj[node]:
                    if nei not in fixed:
                        heapq.heappush(q , (nei_w * w , nei))
        
        return 0