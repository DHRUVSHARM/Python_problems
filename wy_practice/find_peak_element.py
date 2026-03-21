from typing import List

"""
You must write an algorithm that runs in O(log n) time.

       -inf     m        -inf
nums =      [10,2,12,1]
op 2
                          l          r
Input: nums = -inf [1,2,1,3,5,6,4] -inf
Output: 5

if m-1 < m < m+1
l->m

if peak then return
m-1 < m > m + 1

 can move to the left
 m < m-1  m+1 

   l  m      r
-inf [10 12] -inf

"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = -1 , len(nums)

        # we will always have a peak 
        index = None
        while right - left > 1:
            mid = (right + left) // 2
            element_left = nums[mid - 1] if (mid - 1) >= 0 else float("-inf")
            element_right = nums[mid + 1] if (mid + 1) < len(nums) else float("-inf")

            if element_left < nums[mid] > element_right:
                index = mid
                break
            elif element_left < nums[mid] < element_right:
                left = mid
            else:
                right = mid
        
        return index
        
