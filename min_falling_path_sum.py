from typing import List


"""

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


at least one row 

"""


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        result , n = float("inf") , len(matrix)

        for row in range(n - 1 , -1 , -1):
            for col in range(0 , n):
                if row == n - 1:
                    # simple the value itself
                    pass
                else:
                    subans = matrix[row + 1][col]
                    if col - 1 >= 0:
                        subans = min(subans , matrix[row + 1][col - 1])
                    if col + 1 < n:
                        subans = min(subans , matrix[row + 1][col + 1])
                    
                    # we can change in place since we only use the next row 
                    matrix[row][col] += subans
                    

        result = min(matrix[0])
        return result
    
    