from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[float("inf") for _ in range(len(matrix))] for _ in range(len(matrix))]

        # the last row minimal sum is at the cell itself
        for index in range(0, len(matrix)):
            dp[-1][index] = matrix[-1][index]

        directions = [(1, 0), (1, -1), (1, 1)]

        # memoized solution using dp
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix):
                # out of bounds should not be considered
                return float("inf")

            if dp[i][j] != float("inf"):
                return dp[i][j]

            ans = float("inf")
            for dx, dy in directions:
                ans = min(ans, matrix[i][j] + dfs(i + dx, j + dy))

            dp[i][j] = ans
            return ans

        result = float("inf")
        for index in range(len(matrix)):
            result = min(result, dfs(0, index))

        return result
