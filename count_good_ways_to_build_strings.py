class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {0: 1}
        # 1 way to build nothing !!
        for length in range(1, high + 1):
            dp[length] = (dp.get(length - zero, 0) + dp.get(length - one, 0)) % MOD

        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[i]) % MOD

        # print("the dp array is : " , dp)
        return ans
