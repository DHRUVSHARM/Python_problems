from typing import List

"""
[
[9,9,4],
[6,6,8],
[2,1,1]]

strictly increasing


_ _ _
_ _ _
_ _ _


dp[i][j] = lip starting at i, j  (strictly greater )
1 + max(dp[other directions] , 0)

quadratic 
"""
import collections
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n , dp , dirs = len(matrix) , len(matrix[0]) , collections.defaultdict() , [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]


        def dfs(x , y):
            
            if (x , y) in dp:
                return dp[(x , y)]

            ans = 1
            subans = 0 # possible that no path possible from here
            for dx, dy in dirs:
                newx, newy = x + dx, y + dy
                if 0 <= newx < m and 0 <= newy < n and matrix[x][y] < matrix[newx][newy]:
                    subans = max(subans , dfs(newx, newy))
            
            dp[(x , y)] = ans + subans
            return dp[(x , y)]

        ans = 1
        for i in range(0 , m):
            for j in range(0 , n):
                if (i , j) in dp:
                    # already stored 
                    ans = max(ans , dp[(i , j)])
                else:
                    # not in dp
                    ans = max(ans , dfs(i , j))

        
        return ans
    