from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        index , n = 0 , len(nums)
        steps = n // 2
        ans = float("inf")

        while steps:
            ans = min(ans , (nums[index] + nums[n - index - 1]) / 2 ) 
            steps -= 1
            index += 1
        
        return ans
        

    
