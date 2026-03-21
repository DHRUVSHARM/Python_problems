from typing import List

"""
Example 1:
  l   r

        r
1 1 1 3 2
1 2 3 2


                          l      r
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result , left , curr_sum = float("inf") , 0 , 0

        for r in range(0 , len(nums)):
            curr_sum += nums[r]

            while left <= r and curr_sum >= target:
                result = min(
                    result , 
                    r - left + 1
                )

                curr_sum -= nums[left]
                left += 1
            


        return 0 if result == float("inf") else result

