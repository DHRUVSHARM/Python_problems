from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, left, prod = 0, 0, 1

        for r in range(0, len(nums)):
            prod *= nums[r]
            # the r endpoint is used to count
            if prod < k:
                ans += (r - left + 1)
            else:
                # we need to move the left pointer to get rid of the ones
                while left <= r and prod >= k:
                    prod = prod // nums[left]
                    left += 1
                ans += (r - left + 1)

        return ans