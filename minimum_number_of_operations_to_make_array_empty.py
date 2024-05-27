import collections
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1

        ops = 0

        for _, value in freq.items():
            if value == 1:
                return -1
            else:
                if value % 3 == 0:
                    ops += (value // 3)
                elif value % 3 == 1:
                    ops += ((value // 3) - 1) + 2
                else:
                    ops += (value // 3) + 1

        return ops