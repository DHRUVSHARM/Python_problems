from typing import List

"""
Given the array of integers nums, 
you will choose two different 
indices i and j of that array. 

Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
(x - 1) (y - 1)
 = xy - x - y + 1
max product and min sum 

so we want to try to find a balance 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3


maxprod - minsum 

if we increase prod, -> both positive issue we will need least 
so simple max prod but should have least product

if x + y = t

xy - (x + y)

x(t - x) -t
xt - x2 - t


try to choose closest to max from front and back and that should be enough 

                        one positive, -ve  still need least  # not considered here
                        both negative we will need max since it will be aded   # not considered here 

                        

        fm >= sm >= tm 

        if equal we will get it hopefully 
        """

import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        # equal elements will be found easily 
        ans = float("-inf")
        for index in range(1 , len(nums)):
            ans = max(
                ans,
                (nums[index] - 1) * (nums[index - 1] - 1)
            )

        return ans