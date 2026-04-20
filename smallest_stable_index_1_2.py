"""
Example 1:

Input: nums = [ 5,  0,  1,  4], k = 3
                i


[5]             [0 , 1 , 4 , 5]
                
Output: 3

Explanation:

At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.
At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.
At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.
This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.


using prefix , suffix idea 

                        i
Input:          nums = [5,  0,  1,  4]            k = 3

"""

import heapq
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # store the suffix minimums 
        suffix_arr , suffix_min = [element for element in nums] , float("inf")
        for index in range(len(nums) - 1 , -1 , -1):
            suffix_min = min(suffix_min , suffix_arr[index])
            suffix_arr[index] = suffix_min
        
        prefix_max = float("-inf")
        for index, element in enumerate(nums):
            prefix_max = max(prefix_max , element)
            if prefix_max - suffix_arr[index] <= k:
                return index
        
        return -1