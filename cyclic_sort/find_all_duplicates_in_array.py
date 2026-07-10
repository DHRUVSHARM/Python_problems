# Problem summary:
# - Return all values that appear twice in an array of length n whose values are
#   in the range 1..n.
#
# Approach:
# - Treat each value v as pointing to index v - 1.
# - Negate that index the first time v is seen; if it is already negative, v is
#   a duplicate.
#
# Pattern:
# - Cyclic-sort-style index marking / in-place hashing.
#
# Complexity:
# - Time: O(n), where n is len(nums).
# - Space: O(1) auxiliary space, excluding the output list.
#
# Example dry run:
# - Input: nums = [4,3,2,7,8,2,3,1]
# - Step 1: Values 4, 3, 2, 7, 8 mark their target indices negative.
# - Step 2: Seeing the second 2 finds index 1 already negative, so append 2.
# - Step 3: Seeing the second 3 finds index 2 already negative, so append 3.
# - Output: [2, 3], the values encountered twice.

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
