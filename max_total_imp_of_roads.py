from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # outdegree
        outdegree = {i: 0 for i in range(n)}
        ans = 0

        for u, v in roads:
            outdegree[u] += 1
            outdegree[v] += 1

        curr_value = n
        for v in sorted(list(outdegree.values()), reverse=True):
            ans += n * v
            n -= 1

        # print(outdegree)

        return ans
