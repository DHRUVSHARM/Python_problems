from typing import List

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

0 : 0


Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


curr - x = target



0   1   2   3
    1   1   1

"""
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result , sub_sums , prefix = 0 , collections.defaultdict(int) , 0
        sub_sums[prefix] += 1

        for element in nums:
            prefix += element
            result += sub_sums[prefix - k]
            sub_sums[prefix] += 1
        
        return result