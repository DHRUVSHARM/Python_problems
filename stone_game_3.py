from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        # cache , default out of bound request will be 0
        n = len(stoneValue)
        for start_point in range(n - 1, -1, -1):
            sum, res = 0, float("-inf")
            for x in range(1, 4):
                if start_point + x - 1 < n:
                    sum += stoneValue[start_point + x - 1]
                    res = max(res, sum - dp.get(start_point + x, 0))
            dp[start_point] = res

        if dp[0] > 0:
            return "Alice"
        elif dp[0] == 0:
            return "Tie"
        else:
            return "Bob"
