class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp, m = [
            [0 for _ in range(0, min(arrLen + 2, steps + 2))]
            for _ in range(0, steps + 1)
        ], 10**9 + 7
        dp[0][1] = 1

        col_length = len(dp[0])
        # print(col_length)
        for step in range(1, steps + 1):
            for a_l in range(1, col_length):
                if a_l == arrLen + 1:
                    break
                dp[step][a_l] = (
                    dp[step - 1][a_l]
                    + (dp[step - 1][a_l - 1])
                    + (dp[step - 1][a_l + 1] if ((a_l + 1) < col_length) else 0)
                )

        return dp[steps][1] % m
