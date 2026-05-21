from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr_sum = nums[0]

        for index in range(1 , len(nums)):
            # try to add, -ve means current will be taken, if positive the positive one, otherwise keep adding 
            curr_sum = max(nums[index] , nums[index] + curr_sum)
            res = max(res, curr_sum) # record in res 

        return res