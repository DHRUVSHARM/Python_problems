# Problem summary:
# - Find every value in 1..n that does not appear in an array whose values are
#   all in that same range.
#
# Approach:
# - Use each seen value v as a pointer to index v - 1 and mark that position
#   negative.
# - After all marks, every positive position i means value i + 1 was never seen.
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
# - Step 1: Mark indices abs(v)-1 for each value; nums becomes
#   [-4,-3,-2,-7,8,2,-3,-1].
# - Step 2: Scan for positive entries; indices 4 and 5 are positive.
# - Output: [5, 6], because values 5 and 6 were never marked as present.

from typing import List

"""
Given an array nums 
of n integers where nums[i] is in the range [1, n],

return an array of all the integers in the range [1, n] that do not appear in nums.

0     1    2   3    4   5     6    7
[4,  -3,  -2,  -7,  8,  2,  -3,   -1]

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

put in the index nums[i] - 1



"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # const space linear solution 
        result = []

        for element in nums:
            nums[abs(element) - 1] = -1 * abs(nums[abs(element) - 1])
        
        for index in range(0 , len(nums)):
            if nums[index] > 0:
                result.append(index + 1)
        
        return result
