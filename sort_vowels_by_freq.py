"""
Example 1:

Input: s = "leetcode"

Output: "leetcedo"

Explanation:​​​​​​​

Vowels in the string are ['e', 'e', 'o', 'e'] with frequencies: e = 3, o = 1.
Sorting in non-increasing order of frequency and placing them back into the vowel positions results in "leetcedo".
Example 2:

Input: s = "aeiaaioooa"

Output: "aaaaoooiie"

Explanation:​​​​​​​

Vowels in the string are ['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a'] with frequencies: a = 4, o = 3, i = 2, e = 1.
Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in "aaaaoooiie".
Example 3:

Input: s = "baeiou"

Output: "baeiou"

Explanation:

Each vowel appears exactly once, so all have the same frequency.
Thus, they retain their relative order based on first occurrence, and the string remains unchanged.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters
"""

import collections
class Solution:
    def sortVowels(self, s: str) -> str:
        freq = collections.Counter(s)
        seen , vowels = set() , {'a' , 'e' , 'i' , 'o' , 'u'}
        details = []

        for index, element in enumerate(s):
            if element in vowels and element not in seen:
                details.append([freq[element] , index , element])
                seen.add(element)
            
        
        details.sort(key=lambda x : (-x[0] , x[1] , x[2]))

        i , j , result = 0 , 0 , []
        while i < len(s) and j < len(details):
            if s[i] in vowels:
                # replace with vowel 
                result.append(details[j][2])
                details[j][0] -= 1
                if details[j][0] == 0:
                    j += 1
            else:
                # simple add
                result.append(s[i])
            i += 1
        
        while i < len(s):
            # no vowels left 
            result.append(s[i])
            i += 1

        return "".join(result)