from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # greedy
        nums.sort()
        running_sum, result = nums[0] + nums[1], -1
        for r in range(2, len(nums)):
            if running_sum > nums[r]:
                result = max(result, running_sum + nums[r])
            running_sum += nums[r]

        return result
