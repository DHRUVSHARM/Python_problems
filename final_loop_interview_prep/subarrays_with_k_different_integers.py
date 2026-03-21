from typing import List

"""
notes 
subarray problems are generally not very simple
especially if the constraint is exact 
if atmost , then fine otherwise think 3 pointer, or k , k - 1 trick

reasoning for k ,  k - 1


p..l is the valid left pointer range

result = 1 + 2 + 3 + 1 

             p    lr
[1,  2,  1,  2,  3], k = 2


Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:


lr:   3:1 , 4:!
pr: 1:1 , ,3:1 , 4:1


add to both the dicts
if the lr reaches the count 
    then, 
    then move the l to the correct place first drop
    move p to maintain and reach the k if it is not 
    add the count l - p
 

        p    l    r
1   2   1   3   4

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


2 + 3 + 
p           r
[2, 2,  1,  2,  2,  2,  1,  1]

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length


1 2 3

pr  l
1   1   1 
"""

import collections
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        pr , lr , left , p ,  result = collections.defaultdict(int) , collections.defaultdict(int) , 0 , 0,  0

        for r in range(0 , len(nums)):
            pr[nums[r]] += 1
            lr[nums[r]] += 1

    
            while left <= r and len(lr) == k:
                # we want to drop to k - 1
                lr[nums[left]] -= 1
                if lr[nums[left]] == 0:
                    lr.pop(nums[left])
                left += 1
                
                # at this point l ... r has k - 1 distinct integers
                # p ... r will maintain k distinct integers
                # so l - p will give the valid left start points, k = 1 so that edge case will handle when p will not cross over left

            while p < left and len(pr) > k:
                # we want to drop to k 
                pr[nums[p]] -= 1
                if pr[nums[p]] == 0:
                    pr.pop(nums[p])
                p += 1

            if len(pr) == k and len(lr) == k - 1:
                result += (left - p)


        return result