"""
1 <= nums.length <= 100
1 <= nums[i] <= 104
"""

from typing import List

class Solution:

    def digit_sum(self, num):
        res = 0
        while num:
            res = res + (num % 10)
            num = num // 10
        
        return res

    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")

        for num in nums:
            ans = min(ans, self.digit_sum(num))
        
        return ans