# range sum of sorted subarray sums
from typing import List
import collections
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        minHeap = [(element , index)  for index , element in enumerate(nums)]
        heapq.heapify(minHeap)

        ans , checked = 0 , 1

        while checked <= right:
            current_element , index = heapq.heappop(minHeap)
            if  left <= checked <= right:
                ans += current_element
            checked += 1

            if index + 1 < len(nums):                    
                current_element = current_element + nums[index + 1]
                heapq.heappush(minHeap , (current_element , index + 1))
            
        return ans % (10**9 + 7)