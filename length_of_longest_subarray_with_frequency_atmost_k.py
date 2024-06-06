import collections
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, left, f_map = 0, 0, collections.defaultdict(int)

        for r in range(0, len(nums)):
            f_map[nums[r]] += 1
            if f_map[nums[r]] <= k:
                # we can include this
                ans = max(ans, r - left + 1)
            else:
                # we need to reduce len till this condition is reversed
                while left <= r and f_map[nums[r]] > k:
                    f_map[nums[left]] -= 1
                    left += 1

                ans = max(ans, r - left + 1)

        return ans
