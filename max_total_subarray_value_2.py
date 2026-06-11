from typing import List

"""

segment tree for min max lookup 
"""
import heapq
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        seg = [[None, None] for _ in range(2*n)]
        # print(seg)
        # seg[range][0] : max
        # seg[range][1] : min

        for index in range(0 , n):
            seg[index + n][0] = nums[index]
            seg[index + n][1] = nums[index]
        
        for index in range(n - 1 , 0 , -1):
            seg[index][0] = max(seg[2*index][0] , seg[2*index + 1][0])
            seg[index][1] = min(seg[2*index][1] , seg[2*index + 1][1])
        
        def find(l , r):
            # return the max, min in the l, r range assuming valid range 
            
            max_res, min_res = float("-inf") , float("inf")
            while l <= r:
                if l % 2 == 1:
                    # consider
                    max_res = max(max_res , seg[l][0])
                    min_res = min(min_res, seg[l][1])
                    l += 1
                
                if r % 2 == 0:
                    # consider
                    max_res = max(max_res , seg[r][0])
                    min_res = min(min_res, seg[r][1])
                    r -= 1
                
                l = l // 2
                r = r // 2
            
            return max_res , min_res
        
        
        maxHeap , ans = [] , 0

        # first we put ...l , n - 1
        # if we pop we do l , r - 1

        for left in range(0 , n):
            x , y = find(left + n , n - 1 + n)
            heapq.heappush(maxHeap , (-(x - y) , left, n - 1))
        
        while k:
            res, i , j = heapq.heappop(maxHeap)
            ans += (-res)
            k -= 1
            if j - 1 >= i:
                x , y = find(i + n , j - 1 + n)
                heapq.heappush(maxHeap , (-(x - y) , i , j - 1))

        return ans
