import collections
import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # the start times are guaranteed to be distinct
        times_sorted = [(element[0] , element[1] , index) for index , element in enumerate(times)]
        times_sorted.sort()

        ans , minHeap , chairs = collections.defaultdict(int) , [] , [0]

        for start , end , index in times_sorted:
            # first we release chairs
            while len(minHeap) and start >= minHeap[0][0]:
                end_time , chair = heapq.heappop(minHeap)
                heapq.heappush(chairs , chair)
            
            # now we use the smallest unoccupied chair
            chair = heapq.heappop(chairs)
            if not len(chairs):
                heapq.heappush(chairs , chair + 1)
            
            # now we set the chair and the new endtime
            ans[index] = chair
            heapq.heappush(minHeap , (end , chair))

        return ans[targetFriend]