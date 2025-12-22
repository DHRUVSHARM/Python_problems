from typing import List



class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maximal_nums = [element for element in nums]
        index = len(nums) - 1 - 1
        while index >= 0:
            maximal_nums[index] = max(
                maximal_nums[index],
                maximal_nums[index + 1]
            )
            index -= 1

        left , ans = 0 , 0
        for r in range(0 , len(maximal_nums)):
            while left < r and nums[left] > maximal_nums[r]:
                left += 1
            ans = max(
                ans,
                r - left
            )

        return ans