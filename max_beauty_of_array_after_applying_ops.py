import math
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l , ans = 0 , 0

        for r in range(0 , len(nums)):
            while l < r and k < math.ceil((nums[r] - nums[l]) / 2):
                l += 1
            ans = max(ans , (r - l + 1))

        return ans