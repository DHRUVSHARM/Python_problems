import heapq
from typing import List

if __name__ == "__main__":
    # nums = [element for element in zip([1], [2])]
    # print(type(nums[0]))
    pass


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = [element for element in zip(nums1, nums2)]
        nums.sort(key=lambda element: element[1], reverse=True)

        # iterating over the second term
        ans, minHeap, runningSum, window_size = 0, [], 0, 0  # minimal score is 0

        for element1, element2 in nums:
            window_size += 1
            heapq.heappush(minHeap, element1)
            runningSum += element1
            if window_size < k:
                # not enough elements to consider this minimum
                continue
            elif window_size > k:
                e1 = heapq.heappop(minHeap)
                runningSum -= e1
            ans = max(ans, runningSum * element2)

        return ans
