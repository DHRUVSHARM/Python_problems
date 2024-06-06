import collections
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n, minHeap, fixed = len(heights), len(heights[0]), [], {}
        # since the path is weighted, we will use a djikstra based minHeap algorithm
        heapq.heappush(minHeap, (0, (0, 0)))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while len(minHeap):
            # pop the frontier
            frontier_weight, frontier = heapq.heappop(minHeap)
            # check if frontier is already fixed
            if frontier in fixed:
                # we have already determined the min effort
                continue
            else:
                # we need to add this to fixed, this works because of the increasing
                # nature of the function (max( , , )) like with positive weights
                fixed[frontier] = frontier_weight
                # print("fixed : " , frontier , " : " , frontier_weight)
                # we also will add the neighbours into the minHeap
                x, y = frontier
                for dx, dy in directions:
                    newx, newy = x + dx, y + dy
                    if (
                        0 <= newx <= m - 1
                        and 0 <= newy <= n - 1
                        and (newx, newy) not in fixed
                    ):
                        heapq.heappush(
                            minHeap,
                            (
                                max(
                                    frontier_weight,
                                    abs(heights[x][y] - heights[newx][newy]),
                                ),
                                (newx, newy),
                            ),
                        )

        return fixed[(m - 1, n - 1)]
