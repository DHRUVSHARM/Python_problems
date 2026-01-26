from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0 for _ in range(0 , len(costs) + 1)] for _ in range(3)]
        # i: color
        # j : house

        for index in range(1 , len(costs) + 1):
            dp[0][index] = costs[index - 1][0] + min(
                dp[1][index - 1],
                dp[2][index - 1]
            )

            dp[1][index] = costs[index - 1][1] + min(
                dp[0][index - 1],
                dp[2][index - 1]
            )

            dp[2][index] = costs[index - 1][2] + min(
                dp[0][index - 1],
                dp[1][index - 1]
            )



        return min(
            dp[0][-1],
            dp[1][-1],
            dp[2][-1]
        )