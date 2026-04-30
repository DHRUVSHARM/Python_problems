"""
3742. Maximum Path Score in a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1. ​​​​​​​
Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.

dp[i][j][k] = # max path score from 0 to i , j , with cost <= k 
max(
    dp[i-1][j][k - cost(gridi,j)] + score(i , j),
    dp[i][j - 1][k - cost(gridi, j)] + score(i , j)
)

any -k will be -1 

0   1
2   0

dp[i][j][k < 0] will always be -1 

dp[i][j][k = - 1] = float("-inf), for all i, j
dp[i][j][k = 0] 
will all work i think 

final ans at dp[m - 1][n - 1][k]

for k in range(-1  , k + 1):
    for i in range(0 , m):
        for j in range(0 , n)

"""
from typing import List
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        dp = [[[float("-inf") for _ in range(0 , k + 1)] for _ in range(0 , n)] for _ in range(0 , m)] # dp i , j , limit

        # base case 
        for i in range(0 , m):
            for j in range(0 , n):
                # only k = 0 will be considered
                if i == 0 and j == 0:
                    dp[i][j][0] = 0
                    continue

                if grid[i][j] == 0:
                    dp[i][j][0] = max(
                        (dp[i - 1][j][0] if (i - 1 >= 0) else float("-inf")) + 0,
                        (dp[i][j - 1][0] if (j - 1 >= 0) else float("-inf")) + 0
                    )
        

        for limit in range(1 , k + 1):
            for i in range(0 , m):
                for j in range(0 , n):
                    if i == 0 and j == 0:
                        dp[i][j][limit] = 0
                        continue

                    if grid[i][j] == 0:
                        # 0: adds 0 to your score and costs 0.
                        dp[i][j][limit] = max(
                            (dp[i - 1][j][limit] if (i - 1 >=0 ) else float("-inf")),
                            (dp[i][j - 1][limit] if (j - 1 >=0 ) else float("-inf")),

                        )
                    else:
                        # 1: adds 1 to your score and costs 1.
                        # 2: adds 2 to your score and costs 1. ​​​​​​​
                        dp[i][j][limit] = max(
                            (dp[i - 1][j][limit - 1] if (i - 1 >=0 ) else float("-inf")) + grid[i][j],
                            (dp[i][j - 1][limit - 1] if (j - 1 >=0 ) else float("-inf")) + grid[i][j]
                        )
        
        return -1 if dp[m - 1][n - 1][k] == float("-inf") else dp[m - 1][n - 1][k]