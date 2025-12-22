from typing import List
import heapq 

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # initially we sort by the start time, if same start time then it still does not matter since we will put everything into a heap anyways
        intervals.sort()

        # print(intervals , "\n")

        # keeping a heap where we have the minimal finish time at the top always
        minHeap , ans = [] , 0    

        for s , e in intervals:
            while minHeap and minHeap[0][0] < s:
                te , ts = heapq.heappop(minHeap)
            heapq.heappush(minHeap , (e , s))
            
            # print(minHeap)
            ans = max(ans , len(minHeap))
        
        return ans