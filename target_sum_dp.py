import collections
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = collections.defaultdict(int)
        # note : 0 <= nums[i] <= 1000
        # most basic case
        dp[(-1 , 0)] , total = 1 , sum(nums)

        for index in range(0 , len(nums)):
            for t in range(-total , total + 1):
                dp[(index , t)] = dp.get(
                    (index - 1 , t - nums[index]) , 0
                ) + dp.get((
                    index - 1 , t + nums[index]
                ) , 0)

        return dp[(len(nums) - 1 , target)]