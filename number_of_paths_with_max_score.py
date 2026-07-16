from typing import List

"""
Example 1:

Input: board = 

[   "E  2   3   ",
"   2   X   2   ",
"   1   2   S   "]


Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]



dp[i][j][0] # max path score from i , j to m - 1 , n - 1
dp[i][j][1] # number of paths with max score from i , j to m - 1 , n - 1



if X, skip put 0 , 0 # never possible minimal 0 , count 0 
# if i, j is X 

else val = grid[i][j] 
dp[i][j][0] = val + max(
    dp[i + 1][j][0],
    dp[i][j + 1][0],
    dp[i + 1][j + 1][0] 

)

# find the number of paths can be as simple as 
# the idea is to find the paths that are equal to current maximal
# since weights are positive, it makes sense to only have the best weights contribute to the path weight 
# best choice will always be max, and the max will be formed by using max from the three places 
# only it is possible that the max from some side is reduced, due to obstacle 
# in that case only we do not add it, as it will be suboptimal , and future increases can always be made better
# monotonic djikstra property 


dp[i][j][1] = (
    dp[i + 1][j][1] if dp[i][j][0] == dp[i + 1][j][0] + grid[i][j],
    dp[i][j + 1][1] if dp[i][j][0] == dp[i][j + 1][0] + grid[i][j],
    dp[i + 1][j + 1][1] if dp[i][j][0] == dp[i + 1][j + 1][0] + grid[i1][j1]

)


"""


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m , n = len(board) , len(board[0])
        MOD = 10**9 + 7

        dp = [[[float("-inf") , 0] for _ in range(0 , n)] for _ in range(0 , m)]    

        # base case
        dp[m - 1][n - 1][0] = 0 # 0 path weight 
        dp[m - 1][n - 1][1] = 1 # indicating valid path 

        for r in range(m - 1 , -1 , -1):
            for c in range(n - 1 , -1, -1):
                if board[r][c] == 'X':
                    continue

                
                element = 0 if board[r][c] == 'E' else ord(board[r][c]) - ord('0') 

                if r == m - 1 and c == n - 1:
                    pass
                elif r == m - 1:
                    # last row only right
                    dp[r][c][0] = (element + dp[r][c + 1][0])
                    dp[r][c][1] = (dp[r][c][1] + (dp[r][c + 1][1] if dp[r][c][0] == element + dp[r][c + 1][0] else 0) ) % MOD
                elif c == n - 1:
                    # last col only down 
                    dp[r][c][0] = (element + dp[r + 1][c][0])
                    dp[r][c][1] = (dp[r][c][1] + (dp[r + 1][c][1] if dp[r][c][0] == element + dp[r + 1][c][0] else 0) ) % MOD
                else:
                    # simple case 
                    # last row only right
                    dp[r][c][0] = (element + max(
                        dp[r][c + 1][0],
                        dp[r + 1][c][0],
                        dp[r + 1][c + 1][0]
                    ))
                    
                    dp[r][c][1] = (dp[r][c][1] + (dp[r][c + 1][1] if dp[r][c][0] == element + dp[r][c + 1][0] else 0) ) % MOD
                    dp[r][c][1] = (dp[r][c][1] + (dp[r + 1][c][1] if dp[r][c][0] == element + dp[r + 1][c][0] else 0) ) % MOD
                    dp[r][c][1] = (dp[r][c][1] + (dp[r + 1][c + 1][1] if dp[r][c][0] == element + dp[r + 1][c + 1][0] else 0) ) % MOD

        return [0 if dp[0][0][0] == float("-inf") else dp[0][0][0] , dp[0][0][1]]