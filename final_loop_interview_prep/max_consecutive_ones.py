from typing import List

"""
Given a binary array nums and an integer k, 

return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.

 

Example 1:
                             l          r
Input: nums = [1,1,1,0,0    ,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
      r 
1 1 1 0 0 0 0 0  

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window 
        left , flip_count , result = 0 , 0 , 0
        for r in range(0 , len(nums)):
            if nums[r] == 1:
                # we can move as is 
                result = max(
                    result,
                    r - left + 1
                )
            else:
                # value is 0 
                flip_count += 1
                while left <= r and flip_count > k:
                    # need to move left
                    flip_count -= 1 if nums[left] == 0 else 0
                    left += 1
                    
                result = max(
                    result,
                    r - left + 1
                )
                
        return result