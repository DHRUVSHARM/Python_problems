from typing import List

"""
You are given an integer array nums. 
We consider an array good if it is a permutation of an array base[n].


perm of 1 .. n- 1 + n +  n one more time)

base[n] = 
[1, 2, ..., n - 1, n, n] 

(in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.
"""

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # let us try to do some variation of the counting sort algo 
        # we have indexes : [0 .......... n] # n + 1 size
        # num : index num - 1, 1 ->0        n -> n-1  if we see 2 maps to n - 1 means ok and no other 
        
        # we want [1 ... n]
        
        
        n = len(nums) - 1
        for element in nums:
            if not (1 <= abs(element) <= n):
                return False # out of bounds

            nums[abs(element) - 1] *= -1 # mark seen 
            if nums[abs(element) - 1] > 0 and abs(element) - 1 != n - 1:
                return False

        # print(nums)
        return nums[n - 1] > 0 # needs to be flipped twice
            