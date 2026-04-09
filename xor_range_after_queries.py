from typing import List

"""
Input: nums = [1,1,1], queries = [[0,2,1,4]]


0       1       3
[1      1       1  ]


Output: 4

Explanation:

A single query [0, 2, 1, 4] multiplies every element from index 0 through index 2 by 4.
The array changes from [1, 1, 1] to [4, 4, 4].
The XOR of all elements is 4 ^ 4 ^ 4 = 4.


[[1,4,2,3],[0,2,1,2]]



0    1   2   3   4
[2,  3,  1,  5,  4]
     _       _

     brute force, 
     for each query:
        from l to r, 
            for all indexes in l , r skipping k at a time:
                multiply v and take mod m
    
    in the end xor of all the elements in the final updated array to get the result 

"""

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        m = 10**9 + 7
        # Brute force 
        for l, r, k, v in queries:
            index = l
            while index <= r:
                nums[index] = (nums[index] * v) % m
                index += k
        
        result = 0
        for element in nums:
            result ^= element
        
        return result
