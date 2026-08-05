"""
You are given 
a palindromic string s.

Return the 
lexicographically smallest 
palindromic permutation of s.

 
Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.
"""
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [None] * n
        freq = [0] * 26

        for index in range(n // 2):
            freq[ord(s[index]) - ord('a')] += 2

        i , index = 0 , 0
        if (n % 2) == 1:
            ans[n // 2] = ord(s[n // 2]) - ord('a')
        # print(freq)

        while index < n // 2:
            while i < len(freq) and freq[i] == 0:
                i += 1
            # available
            if i < len(freq): 
                ans[index] , ans[n - index - 1] = i , i
                freq[i] -= 2
                index += 1
        
        
        
        return "".join([chr(c + ord('a')) for c in ans])




