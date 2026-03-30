from typing import List

"""
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

0   1  2  3  4  5  6  7  8
[0, 1, 2, 3, 4, 5, 6, 7, 9]

[0, n] we know we will have numbers in this range

0 ,  1
[0 , 1]

0 , 1 , 2
[0 , 1 , 3]
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # we expect numbers from [0 .. n] and find which one is missing 

        for index in range(0 , n):
            while index != nums[index] and index != (nums[index] - 1):
                element = nums[index]
                if element < n:
                    if nums[element] == element:
                        # already in correct place
                        break
                    else:
                        nums[index] , nums[element] = nums[element] , nums[index]
                else:
                    if nums[element - 1] == (element - 1):
                        # already in correct place
                        break
                    else:
                        nums[index] , nums[element - 1] = nums[element - 1] , nums[index]

        missing_number = 0
        while missing_number < n:
            if nums[missing_number] != missing_number:
                break
            missing_number += 1
        
        return missing_number