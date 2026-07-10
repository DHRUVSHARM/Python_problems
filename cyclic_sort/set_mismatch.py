# Problem summary:
# - In a set that should contain 1..n, one value is duplicated and one value is
#   missing; return [duplicate, missing].
#
# Approach:
# - Mark each seen value v by negating index v - 1.
# - If the target index is already negative, v is the duplicate.
# - After marking, the positive index i reveals missing value i + 1.
#
# Pattern:
# - Cyclic-sort-style index marking / in-place hashing.
#
# Complexity:
# - Time: O(n), where n is len(nums).
# - Space: O(1) auxiliary space, excluding the output list.
#
# Example dry run:
# - Input: nums = [1,2,2,4]
# - Step 1: Mark values 1 and 2 by negating indices 0 and 1.
# - Step 2: Seeing the second 2 finds index 1 already negative, so duplicate is
#   2.
# - Step 3: Scan finds index 2 still positive, so missing value is 3.
# - Output: [2, 3].

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
