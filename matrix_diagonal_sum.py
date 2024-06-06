from typing import List

if __name__ == "__main__":
    pass


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0
        for i in range(0, n):
            diagonal_sum += (
                mat[i][i] if (n - 1 - i == i) else (mat[i][i] + mat[i][n - 1 - i])
            )

        return diagonal_sum
