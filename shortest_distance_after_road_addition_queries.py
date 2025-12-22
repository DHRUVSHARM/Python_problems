import collections
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        distances , ans , adj = [i for i in range(0 , n)] , [] , collections.defaultdict(list)
        for u in range(0 , n - 1):
            adj[u].append(u + 1)

        def bfs(start):
            seen , nodes = set([start]) , collections.deque([(start , distances[start])])
            while len(nodes):
                node , dist = nodes.popleft()
                # fix the distance
                distances[node] = min(distances[node] , dist)
                for v in adj[node]:
                    if v not in seen:
                        seen.add(v)
                        nodes.append((v , dist + 1))


        for u , v in queries:
            # this step will always reduce the distance or keep it the same since u < v always
            distances[v] = min( distances[v] ,  distances[u] + 1)
            
            # we will have to do bfs from this point, from v onwards
            bfs(v)

            ans.append(distances[n-1])
            adj[u].append(v)

        return ans