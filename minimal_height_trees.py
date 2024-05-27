import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        d = {index: set() for index in range(0, n)}

        for u, v in edges:
            d[u].add(v)
            d[v].add(u)

        while len(d) > 2:
            # print(d)
            removed_keys = []
            single_keys = []
            for sk in d.keys():
                if len(d[sk]) == 1:
                    single_keys.append(sk)

            for node in single_keys:
                if len(d[node]) == 1:
                    neighbour = d[node].pop()
                    d[neighbour].remove(node)
                    removed_keys.append(node)
            # print(removed_keys)
            for r_k in removed_keys:
                d.pop(r_k)
            # print(d)

        return list(d.keys())
