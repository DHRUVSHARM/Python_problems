from typing import List
import collections

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        dp = collections.defaultdict(int)
        dp[0] = 0

        for value in range(1 , amount + 1):
            result = float("inf")
            for coin in coins:
                if value - coin < 0:
                    break
                result = min(
                    result,
                    dp[value - coin] + 1
                )
            dp[value] = result
        # print(dp)
        
        return -1 if dp[amount] == float("inf") else dp[amount]