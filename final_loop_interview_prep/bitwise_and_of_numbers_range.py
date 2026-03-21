"""
Given two integers left and right that represent the range [left, right],     
    
return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:




Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1

approach :



    16 8 4 2 1 
10   0 1 0 1 0 
  

31




101 0110

101 0111

101 1000

101 1110



1010000


left        1101010101111 0 suffix
right       1101010101111 1 suffix

"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # there will be a rollover from 0 to 1 after the common prefix 
        # has been identified

        shifts = 0

        while left != right:
            # print(left, " : " , right)
            left = left >> 1
            right = right >> 1
            shifts += 1
        
        left = left << shifts

        return left