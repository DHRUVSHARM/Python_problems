from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])

        ans , result = float("inf") , 0
        for row in range(0 , m):
            left, right = 0 , n - 1
            while left < right:
                if grid[row][left] != grid[row][right]:
                    result += 1
                left += 1
                right -= 1

        ans = min(ans  , result)
        result = 0

        for col in range(0 , n):
            left , right = 0 , m - 1
            while left < right:
                if grid[left][col] != grid[right][col]:
                    result += 1
                left += 1
                right -= 1
        
        ans = min(ans , result)
        return ans