from typing import List

"""

You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [1, n].

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).



permutation : we have each element exactly once from 1 to n 
nums[i] XOR nums[j] XOR nums[k] where i <= j <= k


so, 0 ^ x = x

so we have dp[val] = 1 for all 1 <= val <= n

so we know for sure about n values, 
the question is are ther n + 1 values ? iel is a triplet going to make 0 



3 , 1 , 2







    8 4 2 1
---------
    0 0 0 1 - 1
    0 0 1 0 - 2
    0 0 1 1 - 3
    -------
    0 1 0 0 - 4
    0 1 0 1 - 5
    0 1 1 0 - 6
    0 1 1 1 - 7
    ---------------------
    1 0 0 0 - 8

possible values : 0 , 1 , 2 , 3 , 4  5 , 6, 7  - 4 
                  0   1   2    3    5   6 7  - 5
                  same for 6, 7

0 to 7 , 8, 9, 10, 11 ,12 , 
0 to 15 , basically 2^(msb + 1) if n >= 3 else n 


0 1 0 1 - 5
0 1 1 0 - 6
0 1 1 1 - 7
1 0 0 0 - 8





"""

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        else:
            # find msb 
            msb = 0
            while n :
                n = n >> 1
                msb += 1

            return 1 << msb
