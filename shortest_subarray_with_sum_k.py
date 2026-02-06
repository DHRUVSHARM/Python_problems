from typing import List
import heapq

# [2,-1,2]
# [0] , 2 , 1 , 3] 

# heap solution
# [0] , 2  1 , 3]

# monotonic deque solution 
# the order is increasing 

# [0 ,  1 |, ... x ,  3]
# the stack will hold elements in increasing order, starting 
# from the closest local minima and increasing from that point on
# now if we want to consider something increasing 
import collections

# [0 , 2 , 1 , 3]
class Solution:
    def shortestSubarrayHeapSolution(self, nums: List[int], k: int) -> int:
        # heap based approach, o(nlogn)
        minHeap = []
        heapq.heappush(minHeap , (0 , -1))
        ans , prefix = float("inf") , 0

        for index, element in enumerate(nums):
            prefix += element
            
            while minHeap:
                e , i = heapq.heappop(minHeap)
                if prefix - e >= k:
                    ans = min(
                        ans,
                        index - i
                    )
                else:
                    # push back
                    heapq.heappush(minHeap , (e , i))
                    break
            
            heapq.heappush(minHeap , (prefix , index))

        return -1 if ans == float("inf") else ans
    
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # linear solution with monotonic deque
        ans , prefix , s = float("inf") , 0 , collections.deque()
        s.append((0 , -1))

        for index, element in enumerate(nums):
            prefix += element
            while s:
                if prefix <= s[-1][0]:
                    s.pop()
                else:
                    if prefix - s[0][0] >= k:
                        _ , i = s.popleft()
                        ans = min(ans , index - i)
                    else:
                        break
            s.append((prefix , index)) 

        return -1 if ans == float("inf") else ans
