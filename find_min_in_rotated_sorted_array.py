from typing import List

"""
Example 1:

Input: nums = [3,4,5,   |   1,2]
if nums[0] < mid -> in the left side of the array 
else: in the right side of the array
base size 3 simple scan  



Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right = 0 , len(nums) - 1

        result = float("inf")

        while right - left + 1 >= 3:
            mid = (left + right) // 2
            result = min(result, nums[mid])

            if nums[left] < nums[mid]:
                # if left partition 
                if nums[mid] > nums[-1]:
                    # there exists a right partiton, move there 
                    left = mid
                else:
                    # simple sort move to the left 
                    right = mid
            else:
                # right partition always move left if within partition 
                if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                    right = mid
                else:
                    # at inflection from right found min early return 
                    return result # found min already 

        for index in range(left, right + 1):
            result = min(result, nums[index])
        
        return result