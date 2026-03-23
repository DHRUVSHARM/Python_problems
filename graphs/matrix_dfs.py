"""
You are given a binary matrix Grid 
where 0s represent land and 1s represent rocks that can not be traversed.

Return the number of unique paths from the top-left corner of 
Grid to the bottom-right corner such that all traversed cells are land cells. 
You may only move vertically or horizontally through land cells. For an individual unique path you cannot visit the same cell twice.

Example 1:

Input: grid = [
  [0, 0, 0, 0],
  [1, 1, 0, 0],
  [0, 0, 0, 1],
  [0, 1, 0, 0]
]

Output:
2

vertical, horizontal allowed ony
top left to right count valid paths 
we need to consider each of the paths one by one, and make sure that the previous steps are blocked
for that case like a backtracking sort of solution
we can use a hashset add or remove as well, but we will do the other one since i think that uses less memory
"""

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m , n , dirs = len(grid) , len(grid[0]) , [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]

        def dfs(x , y):
            if not(0 <= x < m and 0 <= y < n) or grid[x][y] == 1:
                # base cases 
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1 # target acheived 
            
            # we will always be at a valid block which is 0 and in the grid
            result = 0
            grid[x][y] = 1 # block this current block
            for dx , dy in dirs:
                newx, newy = x + dx , y + dy
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 0:
                    result += dfs(newx , newy)
            
            # unblock
            grid[x][y] = 0
            return result
            
            
        return dfs(0 , 0)

    