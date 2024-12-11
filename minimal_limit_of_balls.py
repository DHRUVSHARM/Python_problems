import math
from typing import List



class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # bs based solution
        # F....FFFFFFTTTTTT.....T

        def helper(minimal_value , maxOperations):
            if minimal_value == 0:
                return False
            
            ans = 0
            for element in nums:
                ans = ans + math.ceil((element - minimal_value) / minimal_value)
            return True if ans <= maxOperations else False

        
        left , right = 0 , max(nums)
        while right > left + 1:
            mid = (left + right) // 2
            if helper(mid , maxOperations):
                right = mid
            else:
                left = mid


        return right