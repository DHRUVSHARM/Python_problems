from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []

        index = 2
        while index < len(nums):
            if nums[index] - nums[index - 2] <= k:
                result.append([nums[index - 2], nums[index - 1], nums[index]])
            index += 3

        return [] if len(result) != (len(nums) // 3) else result
