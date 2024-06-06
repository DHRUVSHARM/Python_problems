import collections
import heapq
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        final_ans, max_frontier = -1 * (10**4) + 7, []

        # efficient heap based dp solution
        for index, element in enumerate(nums):
            curr_max_sum = element  # we have to select the element

            while len(max_frontier) and (index - max_frontier[0][1]) > k:
                # remove elements who cannot be considered
                # maxheap ordered by elements value , in case of same elements , the
                # minimal index will be removed first ( if it exceeds the constraint)
                heapq.heappop(max_frontier)

            if len(max_frontier):
                curr_max_sum = max(curr_max_sum, (-1 * max_frontier[0][0]) + element)

            # print(curr_max_sum)

            final_ans = max(final_ans, curr_max_sum)
            heapq.heappush(max_frontier, (-1 * curr_max_sum, index))

        return final_ans
