from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0

        for j in range(0, n):
            for i in range(1, m):
                matrix[i][j] += matrix[i - 1][j] * matrix[i][j]

        for i in range(0, m):
            prev = -1
            for j, element in enumerate(sorted(matrix[i])):
                if element != prev:
                    ans = max(ans, element * (n - j))
                    prev = element

        return ans
