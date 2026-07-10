"""
You are given an integer array nums of length n.

An integer k 

is called sortable if k divides n 

and you can sort 

nums in non-decreasing order by sequentially performing the following operations:

Partition nums into consecutive subarrays of length k.

Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers k.

A subarray is a contiguous non-empty sequence of elements within an array.©leetcode

3 , 1 , 2
n = 3 can get 1 and 3
sum of all ks that can work 

3 , 1 , 2

if we can get [      ]


[   3 , 1 , 2 ]

# we can first find the divisiors
# maybe a linear pass is ok

1 <= n == nums.length <= 105
1 <= nums[i] <= 105©leetcode


5 , 6  , 7

6 , 7 , 5

7 , 5 , 6

5 , 6 , 7



[           ]   [          ]
inc --------- | inc --------

inc | inc

"""


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        pass