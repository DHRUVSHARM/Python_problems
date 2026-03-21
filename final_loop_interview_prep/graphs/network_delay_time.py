"""

You are given a network of n nodes, 
labeled from 1 to n. 

You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



input

times : (ui, vi, wi)
src node : k
Return the minimum time it takes for all the n

djikstra minimal weight pull 
weight calculated from the src
max of the minimal times from all the nodes, 

if the fixed node size is not n, return -1
nodes labelled 1 to n

directed graph 

"""


from typing import List
import heapq
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        fixed , q , adj = {} , [(0 , k)] , collections.defaultdict(list)

        for u , v , w in times:
            adj[u].append((v , w))
        
        iterations , max_time = n , -1

        while iterations and len(q):
            # we will push the node and the weight 
            w , node = heapq.heappop(q)
            if node not in fixed:
                # double check needed here since we can have multiple inserted but removed later 
                iterations -= 1
                fixed[node] = w
                max_time = max(max_time , fixed[node])

                # only non fixed nodes have the ability for us to add more paths to reach nodes
                # that are also not yet reached, but we add them in for consideration 

                for nei_n , nei_w in adj[node]:
                    if nei_n not in fixed:
                        heapq.heappush(q,  (w + nei_w , nei_n))

        # print("iterations : " , iterations )
        if iterations != 0:
            return -1
        else:
            return max_time