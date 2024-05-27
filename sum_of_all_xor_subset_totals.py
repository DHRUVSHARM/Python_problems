from typing import List

# basic recursive solution
"""
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(index, xor_sum) -> int:
            if index == len(nums):
                return xor_sum

            return helper(index + 1, xor_sum) + helper(index + 1, xor_sum ^ nums[index])

        return helper(0, 0)
"""


# more optimized linear solution
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_sum = 0
        for element in nums:
            or_sum = or_sum | element

        return or_sum << (len(nums) - 1)
