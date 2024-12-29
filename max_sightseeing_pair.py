import heapq
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxHeap , ans = [] , 0

        for index , element in enumerate(values):
            if maxHeap:
                ans = max(
                    -1 * maxHeap[0] + (element - index) ,
                    ans
                )
            heapq.heappush(maxHeap , -1 * (element + index))
        
        return ans