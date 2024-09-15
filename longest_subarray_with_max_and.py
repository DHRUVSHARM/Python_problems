import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res, size, curr_max = 0, 0, 0
        for element in nums:
            if element > curr_max:
                curr_max = element
                size = 1
                res = 0
            elif element == curr_max:
                size += 1
            else:
                size = 0

            res = max(res, size)

        return res
