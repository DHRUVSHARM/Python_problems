# 1 <= nums[i] <= 10
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # very imp and interesting style of dp problem
        m = -1 * (10 ** 5) + 1
        dp = {(0, '+'): m, (0, '-'): 0, (1, '+'): nums[0], (1, '-'): m}

        for index in range(1, len(nums)):
            dp[(index + 1, '+')] = max(
                dp[(index, '+')],
                dp[(index, '-')] + nums[index],
                nums[index]
            )
            dp[(index + 1, '-')] = max(
                dp[(index, '-')],
                dp[(index, '+')] - nums[index]
            )

        return max(dp[(len(nums), '+')], dp[(len(nums), '-')])