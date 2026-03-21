from typing import List
from union_find import UnionFind

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edges.sort(key= lambda element : (element[2] , element[0] , element[1]))

        iterations , result = n - 1, 0
        for u, v, w in edges:
            # try to build and connect components based on minimal edge
            r = uf.union(u , v)
            if not r:
                # this is a cycle forming edge, or you can say both were already in visited
                continue
            else:
                # we add an edge 
                result += w
                iterations -= 1

        return result if iterations == 0 else -1