"""
You are given a string s consisting 
of the characters 'a', 'b', and 'c' 
and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes 
needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.


0 + 

increase r till we can get atleast k in the remainders , take minimal overall
while condition ok again move left 


                            l           r
Input: s = "a   a   b       a   a   a   a       c   a   a   b   c", k = 2
Output: 8


Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length

"""

import collections
class Solution:

    def check(self, curr , freq ,  k):
        # can be constant time check 
        result = True
        for key in ['a' , 'b' , 'c']:
            if (freq[key] - curr[key]) < k :
                result = False
                break
        
        return result

    def takeCharacters(self, s: str, k: int) -> int:
        # 0 condition can be handled with the sliding window 
        left , result , curr , freq = 0 , float("inf") , collections.defaultdict(int) , collections.Counter(s)

        for c in "abc":
            if freq[c] < k:
                return -1

        for r in range(0 , len(s)):
            curr[s[r]] += 1

            # shrink left to keep the condition 
            while left <= r and not self.check(curr , freq , k):
                curr[s[left]] -= 1
                left += 1
            
            # note we do not include the [l..r] boundaries here
            result = min(result , left + len(s) - 1 - r)


        return result
        
        