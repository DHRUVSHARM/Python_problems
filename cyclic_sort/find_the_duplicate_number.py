# Problem summary:
# - Find the single repeated value in an array of n + 1 values where every value
#   is in the range 1..n.
#
# Approach:
# - Interpret nums as a linked list where each index points to nums[index].
# - Use Floyd's cycle detection to find an intersection inside the cycle, then
#   move one pointer from index 0 and one from the intersection until they meet.
#
# Pattern:
# - Fast/slow pointers, cycle detection.
#
# Complexity:
# - Time: O(n), where n is the valid value range size.
# - Space: O(1).
#
# Example dry run:
# - Input: nums = [1,3,4,2,2]
# - Step 1: Following pointers gives 0 -> 1 -> 3 -> 2 -> 4 -> 2, so the cycle
#   starts at value/index 2.
# - Step 2: Fast and slow pointers meet somewhere in that cycle.
# - Step 3: Move one pointer from 0 and one from the meeting point one hop at a
#   time; they meet at 2.
# - Output: 2, the duplicate value that creates the cycle.

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 0   1   2   3   4
[1 , 3 , 4 , 2 , 2]

0 -> 3 -> 2 -> 4 ->
          |<------|

          0 -> 3

x  = p + (n - 1)c           
          
"""
  

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f , s = 0 , 0

        # find the point of intersection 
        while True:
            f = nums[nums[nums[f]]]
            s = nums[nums[s]]

            if f == s:
                break
        

        intersection = 0
        while intersection != s:
            intersection = nums[intersection]
            s = nums[s]

        return intersection
