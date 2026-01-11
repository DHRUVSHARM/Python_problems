from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # we will work on the iterative solution 
        dp = [ 0 for _ in range(0 , len(stoneValue) + 1 ) ]

        for index in range(len(stoneValue) - 1 , -1 , -1):

            dp[index] = stoneValue[index] - dp[index + 1]
            if index + 2 < len(dp):
                dp[index] = max(
                    dp[index],
                    (stoneValue[index] + stoneValue[index + 1]) - dp[index + 2]
                )
            if index + 3  < len(dp):
                dp[index] = max(
                    dp[index],
                    (stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2]) - dp[index + 3]
                )                


        # print(dp)
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"