"""
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.


Example 1:

Input: s1 = "a b c d b a", s2 = "c a b d a b"

0 1 2 4 5


a c b       c b a 
b d a       a d b

Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.

"""
import collections
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # s1 , s2
        one , two = collections.defaultdict(int) , collections.defaultdict(int)
        for index in range(0 , len(s1)):
            if index % 2 == 0:
                one[s1[index]] += 1 # inc by one 
                one[s2[index]] -= 1 # dec by one 
            else:
                two[s1[index]] += 1
                two[s2[index]] -= 1
        
        
        for k , v in one.items():
            if v != 0:
                return False
        
        for k, v in two.items():
            if v != 0:
                return False
        
        return True