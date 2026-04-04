from typing import List


"""
Given an array nums with n integers, 

your task is to check if it could 

become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



float("-inf")  |  [4 , 2 , 3]


if arr[i] == arr[i - 1]
    simple keep moving

    if arr[i] > arr[i - 1]
    increasing can keep going


1   ..  3   4   ...1

if arr[i - 1] > arr[i]
    
    but also decrease arr[i - 1] if the max arr[i - 2] == curr. 
    first try this

    else
    you have to increase at this point no choice


    1 100 0  
    
Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.
 

Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105

"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        second , first = float("-inf") , nums[0]

        moves = 0
        for index in range(1 , len(nums)):
            element = nums[index]
            # print(second , first, element)
            if first <= element:
                # nothing required
                pass
            else:
                # second first > element
                if element >= second:
                    first = element 
                else:
                    element = first
                moves += 1
                
            second , first = first, element

            if moves > 1:
                return False
        

        return True
             