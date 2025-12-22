from typing import List

import heapq
from math import *

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap , score = [-1 * element for element in nums] , 0
        heapq.heapify(maxHeap)

        while k:
            element = -1 * heapq.heappop(maxHeap)
            score += element
            heapq.heappush(maxHeap , -1 * ceil(element / 3))
            k -= 1
        
        return score
