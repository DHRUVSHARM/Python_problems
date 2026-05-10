from typing import List
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float("-inf")] * n
        dp[0] = 0

        for i in range(1 , n):
            max_jumps = float("-inf")
            for j in range(i - 1 , -1 , -1):
                if -target <= (nums[i] - nums[j]) <= target:
                    max_jumps = max(max_jumps , dp[j] + 1)
            dp[i] = max_jumps
        
        # print(dp)
        
        return -1 if dp[n - 1] == float("-inf") else dp[n - 1]