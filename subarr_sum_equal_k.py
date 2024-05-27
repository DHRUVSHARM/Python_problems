import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # o(n) solution uses a dictionary to store the prefix values
        prefixes, curr_prefix_sum, count = collections.defaultdict(int), 0, 0
        prefixes[0] = 1
        for element in nums:
            curr_prefix_sum += element
            if curr_prefix_sum - k in prefixes:
                count += prefixes[curr_prefix_sum - k]

            prefixes[curr_prefix_sum] += 1

        return count
