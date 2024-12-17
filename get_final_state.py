import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = [(element , index) for index , element in enumerate(nums)]
        heapq.heapify(minHeap)

        ans = [0 for _ in range(0 , len(nums))]

        while k:
            element , index = heapq.heappop(minHeap)
            element *= multiplier
            heapq.heappush(minHeap , (element , index))
            k -= 1

        while len(minHeap):
            element , index = heapq.heappop(minHeap)
            ans[index] = element
        
        return ans