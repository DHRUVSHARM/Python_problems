from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # people are named 1 to n
        indeg = {i: 0 for i in range(1, n + 1)}
        outdeg = {i: 0 for i in range(1, n + 1)}

        for a, b in trust:
            indeg[b] += 1
            outdeg[a] += 1

        for i in range(1, n + 1):
            if indeg[i] == n - 1 and outdeg[i] == 0:
                return i

        return -1
