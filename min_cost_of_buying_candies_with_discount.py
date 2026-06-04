from typing import List
import heapq
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # cost = [6,5,7,9,2,2]
        # 2 , 2 , 5,  6 , 7 , 9

        cost_heap = [-c for c in cost]
        heapq.heapify(cost_heap)
        ans = 0

        while len(cost_heap) >= 3:
            t = heapq.heappop(cost_heap)
            s = heapq.heappop(cost_heap)
            free = heapq.heappop(cost_heap)
            ans += ((-t) + (-s))

        while len(cost_heap):
            ans -= heapq.heappop(cost_heap)
        
        return ans 