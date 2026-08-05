from typing import List

"""

n methods from 0 to n - 1
a , b => a invokes b 

# so starting from the bug, we can touch all reachable and mark them or store them in a set 

# then we can iterate remaining ones that are not marked and see where all we can touch 
if we touch something already in there remove from the set 

in the end we have an infected set that is 

"""

import collections
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # first get infected set 
        adj = collections.defaultdict(list)
        for u , v in invocations:
            adj[u].append(v)

        infected = set()
        def find_infected(node):
            infected.add(node)

            for nei in adj[node]:
                if nei not in infected:
                    find_infected(nei)


        find_infected(k)

        normal_nodes = set()
        for node in range(0 , n):
            if node not in infected:
                normal_nodes.add(node)

        # we can use the normal nodes as src points to remove nodes 
        can_remove = True
        visited = set()

        def check(node):
            if node in infected:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    subans = check(nei)
                    if not subans:
                        return False
            
            return True

        for node in normal_nodes:
            if node not in visited:
                res = check(node)
                if not res:
                    can_remove = False
                    break

        if can_remove:
            return list(normal_nodes)
        else:
            return [node for node in range(0 , n)]