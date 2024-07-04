import heapq
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        ans = float("inf")
        minHeap, maxHeap = [element for element in nums], [
            -1 * element for element in nums
        ]
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)

        steps = 4
        min_element_arr, max_element_arr = [], []
        while steps:
            min_element = heapq.heappop(minHeap)
            max_element = -1 * heapq.heappop(maxHeap)
            min_element_arr.append(min_element)
            max_element_arr.append(max_element)
            steps -= 1

        for u, v in zip(min_element_arr, reversed(max_element_arr)):
            ans = min(ans, v - u)

        return ans
