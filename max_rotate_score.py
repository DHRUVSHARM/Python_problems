from typing import List
class Solution:
    # last element wraparound 
    def maxRotateFunction(self, nums: List[int]) -> int:
        prev_dp , arr_sum , n = 0 , 0 , len(nums)
        # dp[0] : 0 rotations base case
        for index, element in enumerate(nums):
            prev_dp += (element * index)
            arr_sum += element

        # print(prev_dp)

        result = prev_dp 
        for k in range(1 , n):
            prev_dp = prev_dp + arr_sum - n*nums[n - k]
            result = max(result , prev_dp)
        
        return result


    