import collections
from typing import List

# triangle
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache_list, n = [triangle[len(triangle) - 1][i] for i in range(0, len(triangle))], len(triangle) - 1
        while n:
            current_list = []
            for index in range(0, n):
                current_list.append(
                    triangle[n-1][index] + min(
                        cache_list[index],
                        cache_list[index + 1]
                    )
                )
            cache_list = current_list
            n -= 1

        # in the end there will always be one final value
        return cache_list[0]
"""

# minimum path sum
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]

        # base cases
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(
                    dp[i-1][j],
                    dp[i][j-1]
                )

        return int(dp[m - 1][n - 1])
"""

# delete and earn , similar to the house robber problem with some modifications
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        unique_elements, count = [], collections.defaultdict(int)
        for element in sorted(nums):
            if element not in count:
                unique_elements.append(element)
            count[element] += 1

        # print(unique_elements)

        dp = [0 for _ in range(0, len(unique_elements) + 1)]
        dp[1] = unique_elements[0] * count[unique_elements[0]]

        for index in range(2, len(dp)):
            # print(index)
            element = unique_elements[index - 1]
            dp[index] = max(
                dp[index - 1],
                (count[element] * element) + (
                    dp[index - 2] if (element - 1) == unique_elements[index - 2] else dp[index - 1])
            )

        return dp[len(dp) - 1]
"""


# combination sum 4
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(0, target + 1)]
        dp[0] = 1
        for index in range(1, len(dp)):
            for num in nums:
                if index - num >= 0:
                    dp[index] += dp[index - num]

        return dp[target]
"""