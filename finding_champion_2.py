import collections
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = collections.defaultdict(int)
        for u , v in edges:
            incoming[v] += 1
        
        if len(incoming.keys()) == n - 1:
            for node in range(0 , n):
                if node not in incoming:
                    return node
        else:
            return -1