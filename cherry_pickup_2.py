from itertools import product
from typing import List

"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # we will solve this problem using memoization first then try to optimize the
        # memory by trying to use iterative dp
        dp, diff = {}, [-1, 0, 1]

        def dfs(row, col1, col2) -> int:

            if (row, col1, col2) in dp:
                return dp[(row, col1, col2)]

            if row == len(grid) or col1 < 0 or col2 == len(grid[0]):
                # base case and we will not allow the robots to cross each other anyway
                return 0

            # print(row , " " , col1 , " " , col2)

            result = -1
            for col1_diff in diff:
                for col2_diff in diff:
                    new_col1, new_col2 = col1 + col1_diff, col2 + col2_diff
                    if new_col1 < new_col2:
                        result = max(
                            result,
                            grid[row][col1] + grid[row][col2] + dfs(row + 1, new_col1, new_col2)
                        )

            dp[(row, col1, col2)] = result
            return result

        return dfs(0, 0, len(grid[0]) - 1)
"""

if __name__ == '__main__':
    arr = [-1, 0, 1]
    for x, y in product(arr, arr):
        # nice way to print all possible combinations of moves
        print(x, " ", y)
    print("reversed iteration on a set of rows")
    for r in reversed(range(5, 10)):
        print(r)


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # we need to start by initializing the base case , that will be on the last row
        # we will model this as a map

        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid[0]))]
        for col1 in range(0, len(grid[0])):
            for col2 in range(col1 + 1, len(grid[0])):
                dp[col1][col2] = grid[-1][col1] + grid[-1][col2]

        diff, next_dp = [-1, 0, 1], []
        for row in range(len(grid) - 2, -1, -1):
            next_dp = [[0 for _ in range(0, len(grid[0]))] for _ in range(len(grid[0]))]
            for col1 in range(0, len(grid[0])):
                for col2 in range(col1 + 1, len(grid[0])):
                    result = -1
                    for col1_diff, col2_diff in product(diff, diff):
                        new_col1, new_col2 = col1 + col1_diff, col2 + col2_diff
                        # we are only populating the non-crossing cases,
                        # we can skip some checks, therefore
                        if new_col1 >= 0 and new_col2 < len(grid[0]):
                            result = max(
                                result,
                                grid[row][col1] + grid[row][col2] + dp[new_col1][new_col2]
                            )
                    next_dp[col1][col2] = result
            dp = next_dp

        return dp[0][len(grid[0]) - 1]