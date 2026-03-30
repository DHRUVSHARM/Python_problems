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