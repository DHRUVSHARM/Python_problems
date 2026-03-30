from typing import List

"""
Given an integer array nums of length n 
where all the integers of nums are in the range [1, n] 
and each integer appears at most twice, 
return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Note : finding duplicate is easy , missing requires the second pass in general 

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for element in nums:
            if nums[abs(element) - 1] < 0:
                result.append(abs(element)) # found twice
            else:
                nums[abs(element) - 1] *= -1
        
        return result 