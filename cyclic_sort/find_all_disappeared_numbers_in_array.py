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