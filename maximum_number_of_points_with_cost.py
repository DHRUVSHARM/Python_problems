
"""

[   

    [1,2,3],
    [1,5,1],
    [3,1,1]

]



points[i][j] 

# max coin value from 
0 .. i, selection ....j available

 = max(
    # till prev dp[i][j - 1] ,
    coins[i][j] + 
 )

 
 
 (coins[i][j1] + j1) + (coins[i - 1][j2] - j2)                  look at prev j1 >= j2
 (coins[i][j1] - j1) + (coins[i - 1][j2] + j2)                  look forward 

coin j2 - j2 max       suffix coin j2 + j2
r-1              |          
r                k
prefix max + j1  |


also , while running store, element + index, element - index, as pair prefix and suffix 


FINAL ALGO : 

        precompute
            for r:
                for c:
                    prefix max : left to right -> (element - index) and (element + index)
                    also suffix max (n - c - 1) -> (element - index) and (element + index)
        
        # quadratic

        dp[r][k] = max(
            prefix max (element - index) [r- 1][k] + coins[r][k] + k,
            suffix max (element + index) [r- 1][k + 1] + coins[r][k] - k, 
            # not choose, dp[r][k - 1]
        )

        final ans will be dp[m - 1][n - 1]
        # considered m - 1 rows, n - 1 cols

atleast one row and col 
1 <= m, n <= 105
1 <= m * n <= 105



    for all r
        for c:
            dp[r][c] = max(
                dp[r][c - 1],
                prefix : dp[r - 1][c] + points[r][c] + c,
                suffix : dp[r - 1][c + 1] + points[r][c] - c
            )
            

"""


from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m , n = len(points) , len(points[0])

        for row in range(1 , m):
            # calculate the prefix and suffix arr 
            prefix, suffix = float("-inf") , float("-inf")
            prefix_arr = [None for _ in range(0 , n)]
            suffix_arr = [None for _ in range(0 , n)]

            # calculate the dp prefix / suffix for the prev row dp 
            for col in range(0 , n):
                prefix , suffix = max(prefix , points[row - 1][col] + col) , max(suffix , points[row - 1][n - col - 1] - (n - col - 1) )
                prefix_arr[col] , suffix_arr[n - col - 1] = prefix , suffix
            
            for col in range(0 , n):
                # compute using prev value 
                points[row][col] = max(
                    points[row][col] - col + prefix_arr[col],
                    points[row][col] + col + suffix_arr[col]
                )
            # as a result we will have points[row][c] consider all rows till r and ending at c

        # finally we need to take the max of the last row to return the final answer
        return max(points[-1])
