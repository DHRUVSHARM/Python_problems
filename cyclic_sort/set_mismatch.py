from typing import List

"""
You have a set of integers s, 

which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [] # will store the duplicate, missing

        for element in nums:
            if nums[abs(element) - 1] < 0:
                result.append(abs(element))
            else:
                nums[abs(element) - 1] *= -1


        for index in range(0 , len(nums)):
            if nums[index] > 0:
                result.append(index + 1) # missing number
        
        return result