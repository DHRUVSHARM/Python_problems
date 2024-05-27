import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we will use djikstra concepts but with some changes to ensure that the complexity is
        # around quadratic

        rows, cols = len(grid), len(grid[0])
        # we can move down or right
        directions = {(1, 0), (0, 1)}

        visited, minHeap = {0, 0}, [(grid[0][0], 0, 0)]
        heapq.heapify(minHeap)

        result = 0
        while len(minHeap):
            elevation, x, y = heapq.heappop(minHeap)
            if x == rows - 1 and y == cols - 1:
                result = elevation
            for dx, dy in directions:
                if x + dx < rows and y + dy < cols and (x + dx, y + dy) not in visited:
                    visited.add((x + dx, y + dy))
                    heapq.heappush(minHeap, (
                        max(elevation, grid[x + dx][y + dy]),
                        x + dx,
                        y + dy
                    ))

        return result
