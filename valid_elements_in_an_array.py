"""

    1  , 2 , 4 , 2 , 3 , 2
l   t   t     t   f  f                           
-inf
"""

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        left , right = float("-inf") , float("-inf")
        result = []
        dp = [False for _ in range(0 , len(nums))]

        for index in range(0 , len(nums)):
            if left < nums[index]:
                dp[index] = True
            left = max(left, nums[index])

            if right < nums[len(nums) - index - 1]:
                dp[len(nums) - index - 1] = True
            right = max(right , nums[len(nums) - index - 1])
        
        for index in range(0 , len(dp)):
            if dp[index]:
                result.append(nums[index])
        
        return result