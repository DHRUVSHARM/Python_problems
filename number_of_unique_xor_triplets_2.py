from typing import List

"""
You are given an integer array nums.

A XOR triplet is defined as the 

XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).
 

Example 1:

Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

(0, 0, 0) → 1 XOR 1 XOR 1 = 1
(0, 0, 1) → 1 XOR 1 XOR 3 = 3
(0, 1, 1) → 1 XOR 3 XOR 3 = 1
(1, 1, 1) → 3 XOR 3 XOR 3 = 3
The unique XOR values are {1, 3}. Thus, the output is 2.

Example 2:

Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

 

Constraints:

1 <= nums.length <= 1500
1 <= nums[i] <= 1500


    3    3    1    0  
    8   4   2   1 
    1   0   0   1

    2^msb + 1

min     ......       max
0                   2^msb + 1 (or 1 indexed msb)
result  = sum of all these if > 0


use a set = {all possible xor pairs}
iterate for all element min to max:
    add to set (element ^ (pair))

    take the len of the result set 
"""

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        max_val = max(nums)

        mask = 1 
        while max_val: 
            mask = mask << 1   
            max_val = max_val >> 1

        one = [0] * (mask)
        two = [0] * (mask)
        three = [0] * (mask)

        for element in nums:
            one[element] = 1

        for element in nums:
            for element1 in range(0 , len(one)): 
                if one[element1]:
                    two[element ^ element1] = 1

        for element in nums:  
            for element1 in range(0 , len(two)):
                if two[element1]:
                    three[element ^ element1] = 1

        ans = sum(three)
        return ans