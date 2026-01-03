class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(0 , n + 1)]
        # ignoring dp[0]
        dp[1] = 1
        dp[2] = 1 if n == 2 else 2  # 1 * 1

        for element in range(3 , len(dp)):
            result = element if element != (len(dp) - 1) else 0
            # consider if the element itself is the best selection except at the end since we need to split 
            # into 2 elements atleast 
            for i in range(1 , element):
                result = max(
                    result, 
                    dp[i] * dp[element - i]
                )
            dp[element] = result

        # print(dp)
        return dp[n]
