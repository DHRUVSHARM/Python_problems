import collections
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        prev = 0
        for x in range(max(nums), -1, -1):
            curr = prev + freq[x]
            if curr == x:
                return x
            prev = curr

        return -1
