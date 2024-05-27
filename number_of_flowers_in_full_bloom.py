import heapq
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        # sorting the people and the flowers by starting time
        count = 0
        res = {p: 0 for p in people}
        h = [end_time for _, end_time in flowers]
        heapq.heapify(h)
        # storing the endtimes in a minheap

        j = 0
        for p in sorted(people):
            while len(h) and h[0] < p:
                heapq.heappop(h)
                count -= 1
            while j < len(flowers) and flowers[j][0] <= p:
                count += 1
                j += 1
            res[p] = count

        ans = []
        for p in people:
            ans.append(res[p])

        return ans