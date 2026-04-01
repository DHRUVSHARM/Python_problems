from typing import List

"""

Given an unsorted integer array nums. 
Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:


-ve numbers and even zero is not useful since we want the first missing positive
so it is like doing 1 .. n
we can remove the negative ones to zero 

we can replace all negative numbers as 0 initially 
then when we iterate we can see a zero which no need to store 
if we have to make it -1 , that means we are using that to store

               0   1    2      3
Input: nums = [-3, 4,  -3 ,  -1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:


[we try to fix till we touch 1 ]



               0  1  2  3   4
Input: nums = [7, 8, 9, 11, 12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1


so 0 : skip since that was a zero or a negative number basically we can also do [1 .. n]

and if we have to touch a zero we can put the same positive number that we saw with -ve sign 

if any else abs(num) - 1 and - abs(whatever store)

if bet 1 to n then also skip

final iterate to check from 1 to n pick first one 

"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for index in range(0 , n):
            if not (1 <= nums[index] <= n):
                nums[index] = 0 # fix zero
        
        for index in range(0 , n):
            if nums[index] == 0:
                # was an out of range value so no point considering 
                continue
            else:
                if nums[abs(nums[index]) - 1] == 0:
                    # can replace with an occ of the same 
                    nums[abs(nums[index]) - 1] = abs(nums[index])
                # in both cases take the abs and mark with negative to show that it was seen
                nums[abs(nums[index]) - 1] = -1 * (abs(nums[abs(nums[index]) - 1])) # for simplicity 
                
        # finally iterate and stop at the first positive
        # we know in best case we have all from 1 ..... n
        missing_positive = 0
        while missing_positive < n:
            if nums[missing_positive] < 0:
                missing_positive += 1
            else:
                break
        
        return missing_positive + 1