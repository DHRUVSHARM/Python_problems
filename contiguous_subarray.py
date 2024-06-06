import collections
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # a prefix sum based approach
        ans = 0

        diff_prefix = collections.defaultdict(int)
        ones, zeros = 0, 0

        diff_prefix[0] = -1  # ease

        for index, element in enumerate(nums):
            if element == 1:
                ones += 1
            else:
                zeros += 1

            diff = ones - zeros
            if diff not in diff_prefix:
                diff_prefix[diff] = index
            else:
                ans = max(ans, index - diff_prefix[diff])

        return ans
