import collections
from typing import List

# very imp ... , using the count subarrays with sum less < = k type style
"""
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(g):
            result, left, sub_ans = 0, 0, 0
            for r in range(0, len(nums)):
                sub_ans += nums[r]
                while left <= r and sub_ans > g:
                    sub_ans -= nums[left]
                    left += 1
                result += (r - left + 1)

            return result

        return helper(goal) - helper(goal - 1)
"""


# now doing it using subarray sum == k style of answer
# this will be done using prefix sums and a hashmap
# very imp style of question
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_f = collections.defaultdict(int)
        prefix_f[0] = 1
        # a prefix of 0 is used as dummy for ease
        p_sum, result = 0, 0
        for element in nums:
            p_sum += element
            result += prefix_f[p_sum - goal]
            prefix_f[p_sum] += 1

        return result