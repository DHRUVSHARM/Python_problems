class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for index in range(1, n + 1):
            perfect_sq = 1
            val = perfect_sq * perfect_sq
            while index - (val) >= 0:
                dp[index] = min(dp[index], 1 + dp[index - (val)])
                perfect_sq += 1
                val = perfect_sq * perfect_sq
        return dp[n]
