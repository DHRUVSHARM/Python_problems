"""
You are given an integer n.

An integer x is considered good 
if there exist at 
least two distinct pairs (a, b) such that:

a and b are positive integers.
a <= b
x = a3 + b3
Return an array containing all good integers less than or equal to n, sorted in ascending order.

 

Example 1:

Input: n = 4104

Output: [1729,4104]

Explanation:

Among integers less than or equal to 4104, the good integers are:

1729: 13 + 123 = 1729 and 93 + 103 = 1729.
4104: 23 + 163 = 4104 and 93 + 153 = 4104.
Thus, the answer is [1729, 4104].

Example 2:

Input: n = 578

Output: []

Explanation:

There are no good integers less than or equal to 578, so the answer is an empty array.

 

Constraints:

1 <= n <= 109

a iterate from 1 to n
    b iterate from a + 1 to n
        if acube + bcube <= n:
            if (a , b) will be unique because of ordering  we wont do b, a also a < b is maintained
            if (a , b) count  == 1:
                add to result, the number 
            += 1
        else
            break

return result 

"""

import collections
class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        
        result , pair_count = [] , collections.defaultdict(int)

        for a in range(1 , n):
            if a**3 > n:
                break
            for b in range(a + 1 , n):
                num = a**3 + b**3
                if num > n:
                    break
                
                if num in pair_count and pair_count[num] == 1:
                    result.append(num)
                
                pair_count[num] += 1
        
        result.sort()
        return result