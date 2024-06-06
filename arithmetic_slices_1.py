from typing import List

# very imp question that i am doing in 2 different ways
# the first one is the 2 pointer type sol
# the next one will be the dp solution 1d
# then we will also look at the slices 2 one
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        ans, left, right = 0, 0, 1
        cd = nums[right] - nums[left]

        while right + 1 < len(nums):
            if nums[right + 1] - nums[right] == cd:
                # can extend the window
                pass
            else:
                # calc and reset
                n = right - left + 1
                ans += ((n - 1) * (n - 2)) // 2
                left = right
                cd = nums[right + 1] - nums[left]

            right += 1

        if len(nums) - left >= 3:
            n = right - left + 1
            ans += ((n - 1) * (n - 2)) // 2

        return ans
"""


# dp
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        dp = [0 for _ in range(0, len(nums))]
        ans = 0

        for i in range(2, len(nums)):
            if (nums[i] - nums[i - 1]) == (nums[i - 1] - nums[i - 2]):
                dp[i] = 1 + dp[i - 1]
                ans += dp[i]

        return ans
