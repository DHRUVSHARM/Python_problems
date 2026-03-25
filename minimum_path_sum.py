from typing import List

"""
Given a m x n grid 
filled with non-negative numbers, 

find a path from top left to bottom right, 

which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

down or right movement allowed at any time 
(1 , 0) or (0 , 1)


dp[i . j] = max(dp[i + 1 , j] , dp[i , j + 1]) + current element 
 
# in memory solution ?

"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m , n = len(grid) , len(grid[0])

        # we can store on the dp grid technically 
        for row in range(m - 1, -1 , -1):
            for col in range(n - 1 , -1 , -1):
                subans = float("inf")
                if row + 1 < m:
                    subans = min(subans , grid[row + 1][col])

                if col + 1 < n:
                    subans = min(subans , grid[row][col + 1])

                grid[row][col] += (0 if subans == float("inf") else subans)
        
        return grid[0][0]

        
        