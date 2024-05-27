from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for _ in range(n + 1)]
        # dp[n] is when we have no questions left to solve
        # dp[i] refers to problem where questions i to n - 1 are available

        for index in range(n - 1, -1, -1):
            points, brainpower = questions[index]
            dp[index] = max(
                dp[index + 1],
                points + dp[min(index + brainpower + 1, n)]
            )

        return dp[0]
