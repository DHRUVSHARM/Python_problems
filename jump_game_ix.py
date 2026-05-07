from typing import List

"""

You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

Jump to index j where j > i is allowed only if nums[j] < nums[i].
Jump to index j where j < i is allowed only if nums[j] > nums[i].
For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

larger                   smaller
j             i           j




Return an array ans where ans[i] is the maximum value reachable starting from index i.

Example 1:

Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

For i = 0: No jump increases the value.
For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
Thus, ans = [2, 2, 3].


# forward pass 
iterate l to r, 
maintain increasing stack 
if small, from popped -> front index edge

# back pass 
iterate r to l 

2 , 1, 3

    2    |1 3

"""

import collections
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # we will use the monotonic stack approach to solve the problem
        # prev | next 
        # i < j, val prev > val next 
        # this means we can take some value and connect to it 
        # if these components are made incrementally
        # |can reach max|   |can reach some min| means we can merge since for all elements in the first component we can move to right min
        # otherwise these will not be merged and kept
        # [|| || ] max, min and use the min , to check and pop and merge 
        # else add 
        # these components will be distinct based on the boundary conditions 
        # a non intersecting comp {max , min} <=  {max1 , min1} unless the one on the right does not change we cannot move
        # prefix maxes and suffix mins will be computed on the fly with this approach 

        n = len(nums)
        res = [0] * n
        s = []

        for index, element in enumerate(nums):
            # pop and create the largest merged interval 
            cur_max, cur_min = element , element
            s_index, end_index = index, index

            # sindex, eindex, currmax, currmin
            while s and s[-1][2] > cur_min:
                # can merge
                fsi , fei, fmax, fmin = s.pop()
                s_index = min(s_index , fsi)
                end_index = max(end_index , fei)
                cur_max = max(cur_max , fmax)
                cur_min = min(cur_min , fmin)
                
            # push in the merged interval 
            s.append((s_index , end_index , cur_max , cur_min))
        

        # print(s)
        for element in s:
            s , e , cmax , _ = element
            for index in range(s , e + 1):
                res[index] = cmax
        
        return res
