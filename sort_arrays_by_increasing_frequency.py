from typing import List


import collections
import heapq


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = collections.Counter(nums)
        result, minHeap = [], []

        for key, value in freq.items():
            heapq.heappush(minHeap, (value, -1 * key))

        while len(minHeap):
            f, val = heapq.heappop(minHeap)
            while f:
                result.append(-1 * val)
                f -= 1

        return result
