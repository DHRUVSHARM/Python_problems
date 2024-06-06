import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        # we will try to use ladders to get as far then swap it and see how further we can
        # go

        index = 1
        while index < len(heights):
            if heights[index] - heights[index - 1] > 0:
                # we have to use something
                if ladders:
                    # we can use a ladder
                    ladders -= 1
                    heapq.heappush(
                        minHeap, (heights[index] - heights[index - 1], index)
                    )
                    # we do not have ladders
                elif (
                    len(minHeap)
                    and minHeap[0][0] < (heights[index] - heights[index - 1])
                    and bricks - minHeap[0][0] >= 0
                ):
                    # we can fill this by bricks and swap the current one with a ladder
                    # but doing this is optimal only if the current difference is greater than
                    # the current ladder position
                    bricks -= minHeap[0][0]
                    heapq.heappop(minHeap)
                    heapq.heappush(
                        minHeap, (heights[index] - heights[index - 1], index)
                    )
                elif bricks - (heights[index] - heights[index - 1]) >= 0:
                    # we will have to and can use bricks to continue at this point
                    bricks -= heights[index] - heights[index - 1]
                else:
                    # cannot use bricks or ladders at this point
                    break
            index += 1

        return index - 1
