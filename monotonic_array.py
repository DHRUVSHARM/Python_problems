from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True

        for index in range(1, len(nums)):
            increasing = increasing and (True if nums[index - 1] <= nums[index] else False)
            decreasing = decreasing and (True if nums[index - 1] >= nums[index] else False)

        return increasing or decreasing
