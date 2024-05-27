from typing import (
    List,
)


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def min_cost(self, costs: List[List[int]]) -> int:
        # write your code here
        dp = [[0 for _ in range(3)] for _ in range(len(costs) + 1)]

        for index in range(1, len(costs) + 1):
            dp[index][0] = min(
                dp[index - 1][1],
                dp[index - 1][2]
            ) + costs[index - 1][0]

            dp[index][1] = min(
                dp[index - 1][0],
                dp[index - 1][2]
            ) + costs[index - 1][1]

            dp[index][2] = min(
                dp[index - 1][1],
                dp[index - 1][0]
            ) + costs[index - 1][2]

        return min(
            dp[len(costs)][0],
            dp[len(costs)][1],
            dp[len(costs)][2]
        )
