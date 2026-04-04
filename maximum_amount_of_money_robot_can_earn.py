from typing import List
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m , n , k = len(coins) , len(coins[0]) , 2
        dp = [[[float("-inf") for _ in range(n)] for _ in range(m)] for _ in range(k + 1)]
        # dp[k][row][col]


        dirs = [(1 , 0) , (0 , 1)] # down, right

        for block in range(k , -1 , -1):
            for row in range(m - 1 , -1 , -1):
                for col in range(n - 1 , -1 , -1):
                    
                    if row == m - 1 and col == n - 1:
                        if coins[row][col] >= 0:
                            dp[block][row][col] = coins[row][col]
                        else:
                            if block == k:
                                dp[block][row][col] = coins[row][col]
                            else:
                                dp[block][row][col] = 0 # use the blocker
                    

                    subans = float("-inf")
                    if coins[row][col] >= 0:
                        # collect
                        for dx , dy in dirs:
                            newx , newy = row + dx , col + dy
                            if 0 <= newx < m and 0 <= newy < n:
                                subans = max(subans , coins[row][col] + dp[block][newx][newy])

                        dp[block][row][col] = max(dp[block][row][col] , subans)  
                    else:
                        # steal
                        for dx, dy in dirs:
                            newx , newy = row + dx , col + dy
                            if 0 <= newx < m and 0 <= newy < n:
                                # allow steal
                                subans = max(subans , coins[row][col] + dp[block][newx][newy])
                                if block + 1 <= k:
                                    # block 
                                    subans = max(subans , dp[block + 1][newx][newy])
     
                        dp[block][row][col] = max(dp[block][row][col] , subans)  

        # print(dp[2][0][0])
        return dp[0][0][0]