from typing import List

# the key here is to understand the bottom up notation
# dp[i][j][rem] -> we are coming in with a rem (summed modulo) , and we want to see how many paths that are valid
# start from i , j position 
# we would want dp[0][0][0] , start from the top left, and you dont have any remainder to begin with  

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # we need to first have the base case, and the dp array
        m , n , MOD = len(grid) , len(grid[0]) , 7 + 10**9
        
        # dp[i][j][k] -> the number of paths that start at (i , j) end at the bottom right with incoming modulo sum as k 
        dp = [ [[0 for _ in range(k)] for _ in range(n)] for _ in range(m) ]

        # i , j , rem -> i + 1 , j , some rem |  + i , j + 1 , some rem
        # base case 
        # will be the end node 
        dp[m-1][n-1][(k - (grid[m-1][n-1] % k)) % k] = 1

        for i in range(m - 1 , -1 , -1):
            for j in range(n - 1 , -1, -1):
                for rem in range(0 , k):
                    if i == m - 1 and j == n - 1:
                        continue
                    
                    # take incoming k value and add it to the current element for future consideration modulo k
                    result , new_remainder = 0 , (rem + grid[i][j]) % k
                    if i + 1 < m:
                        result = (result +  dp[i+1][j][new_remainder]) % MOD 
                    if j + 1 < n:
                        result = (result +  dp[i][j+1][new_remainder]) % MOD

                    dp[i][j][rem] = result


        return dp[0][0][0]
