from typing import List

"""
Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.

first occ of 5 ?

first occ of target to the left and to the right of start 

"""

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = float("inf")
        
        left = start
        while left >= 0:
            if nums[left] == target:
                result = min(result , abs(left - start))
                break
            left -= 1

        right = start
        # print(right)
        while right < len(nums):
            if nums[right] == target:
                result = min(result , abs(right - start))
                break
            right += 1
        
        return result