from typing import List

"""



    2   5   4
    1   5   1

    2   7   11              prefix
    7   6    1              suffix

    0   0   11              prefix zeroes from 0 to i 
    7   0    0              suffix zeroes from end to j



    wiping out max prefix
    wiping out max suffix 

    or you can think liek 
    
    max(row1sum - prefix , row2sum - suffix) is minimized since we can only pick that as the second robot
    
"""


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1_sum , row2_sum , n = sum(grid[0]) , sum(grid[1]) , len(grid[0])

        prefix , suffix = grid[0][:] , grid[1][:]

        # print(prefix)
        # print(suffix)

        for i in range(1 , n):
            prefix[i] += prefix[i - 1]

        for j in range(n - 2 , -1 , -1):
            suffix[j] += suffix[j + 1]
        
        # print(prefix)

        # print(suffix)

        score = float("inf")

        for c in range(0 , n):
            score = min(
                score,
                max(row1_sum - prefix[c] , row2_sum - suffix[c])
            )
        
        return score

