from typing import List
import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap, maxHeap = [], []
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)

        deleted = {index: True for index in range(len(nums))}

        left, ans = 0, 0
        for r in range(0, len(nums)):
            # add the element first,
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))
            deleted[r] = False

            while abs(minHeap[0][0] + maxHeap[0][0]) > limit:
                # there is a guarantee of atleast one element in both due to limit constraint
                # now we will remove lazily and find the ans
                # we need to delete the left part
                deleted[left] = True

                while deleted[minHeap[0][1]]:
                    heapq.heappop(minHeap)

                while deleted[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)

                left += 1

            # we have got some answer
            ans = max(ans, r - left + 1)

        return ans
