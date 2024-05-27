from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(grid) - 2)] for _ in range(len(grid) - 2)]
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                element = grid[i][j]
                for dx, dy in dirs:
                    element = max(
                        element,
                        grid[i + dx][j + dy]
                    )

                result[i - 1][j - 1] = element

        return result