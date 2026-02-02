from typing import List

# ans = 2
# [1,3,1,2,4,3]
#            lr
# [1,1,1,1,1,1,1,11]
#                 lr

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans , left , curr_sum = float("inf") , 0 , 0

        for r in range(0 , len(nums)):
            curr_sum += nums[r]
            while left <= r and curr_sum >= target:
                ans = min(ans , r - left + 1)     
                curr_sum -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans