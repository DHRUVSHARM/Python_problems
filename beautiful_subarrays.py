import collections
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xor_sum, xor_prefixes, count = 0, collections.defaultdict(int), 0
        xor_prefixes[0] = 1

        for element in nums:
            xor_sum = xor_sum ^ element
            if xor_sum in xor_prefixes:
                count += xor_prefixes[xor_sum]
            xor_prefixes[xor_sum] += 1

        return count