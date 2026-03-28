from typing import List

"""
0    1   1   1
0    1   1   1
0    1   1   1  
0    1   1   1


dp[i][j - 1] width with dp[i - 1][j - 1]



            dp[i][j] : 
                            h : dp[i - 1][j] , dp[i - 1][j - 1] , dp[i][j - 1]
                            w : 

                            
                        min(dp[i - 1])                            
                            
"""

import collections
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m , n , dp = len(matrix) , len(matrix[0]) , collections.defaultdict()
        result = 0

        for i in range(0 , m):
            for j in range(0 , n):
                if matrix[i][j] == "1":
                    dp[(i , j)] = 1 + min(dp.get((i - 1 , j) , 0) , dp.get((i , j - 1) , 0) , dp.get((i - 1, j - 1) , 0))
                else:
                    dp[(i , j)] = 0

                result = max(result , dp[(i , j)])

        return result ** 2