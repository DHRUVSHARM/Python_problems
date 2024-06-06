import collections
import heapq
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        elements = []
        for key, val in freq.items():
            elements.append((val, key))

        heapq.heapify(elements)

        while len(elements) and k - elements[0][0] >= 0:
            k -= elements[0][0]
            heapq.heappop(elements)

        return len(elements)
