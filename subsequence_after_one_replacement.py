"""
You are given two 
strings s and t 
consisting of lowercase English letters.

You may choose 
at most one index 
in s and replace the character 
at that index with any lowercase English letter.

Return true if it is 
possible to make s a subsequence of t; otherwise, return false.

# new definition : it can be a almost subsequence (atmost one change)

Example 1:

Input: s = "cat", t = "chat"
                              -1 0    1     2     
    c   a   t                  | c    h    |a     t
        i                                 j

        
        r - l - 1 >= 1 # need to have one or more elements in between 
        2 + 1 - 1

        c                       x

        0  1
    -1  0

     [0  2 3] 4: prefill with len(t)
  -1 [0  2 3] : prefill with -1

    # prefix i : the first index in t where s[:i + 1] is a matching prefix 
    # suffix i : the first index in t where s[i:] is a matching sufiix 

Output: true

Explanation:

Replace s[1] from 'a' to 'h'. The resulting string is "cht".
"cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.
Example 2:

Input: s = "plane", t = "apple"

Output: false

Explanation:

The characters 'p', 'l', and 'e' can be matched in t, but the remaining characters cannot be matched while preserving the required order.
Even after replacing any one character in s, it is impossible to make s a subsequence of t.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.

"""

"""
You are given two 
strings s and t 
consisting of lowercase English letters.

You may choose 
at most one index 
in s and replace the character 
at that index with any lowercase English letter.

Return true if it is 
possible to make s a subsequence of t; otherwise, return false.

# new definition : it can be a almost subsequence (atmost one change)

Example 1:

Input: s = "cat", t = "chat"
                              -1 0    1     2     
    c   a   t                  | c    h    |a     t
        i                                 j

        
        r - l - 1 >= 1 # need to have one or more elements in between 
        2 + 1 - 1

        c                       x

        0  1
    -1  0

     [0  2 3] 4: prefill with len(t)
  -1 [0  2 3] : prefill with -1

    # prefix i : the first index in t where s[:i + 1] is a matching prefix 
    # suffix i : the first index in t where s[i:] is a matching sufiix 

Output: true

Explanation:

Replace s[1] from 'a' to 'h'. The resulting string is "cht".
"cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.
Example 2:

Input: s = "plane", t = "apple"

Output: false

Explanation:

The characters 'p', 'l', and 'e' can be matched in t, but the remaining characters cannot be matched while preserving the required order.
Even after replacing any one character in s, it is impossible to make s a subsequence of t.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.

"""

class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        prefix = [len(t) for _ in range(len(s))]
        suffix = [-1 for _ in range(len(s))]

        # fill the prefix 
        i , j = 0 , 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                prefix[i] = j # store the index
                i += 1
                j += 1
            else:
                j += 1

        # fill the suffix 
        i , j = len(s) - 1 , len(t) - 1

        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                suffix[i] = j
                i -= 1
                j -= 1
            else:
                j -= 1

        # print(suffix)
        # print(prefix)
        
        # if len(s) > len(t):
            # return False

        for i in range(0 , len(s)):
            left = prefix[i - 1] if i > 0 else -1
            right = suffix[i + 1] if i < len(s) - 1 else len(t)
            if (right - left - 1) >= 1 and (len(t) - right + 1 >= len(s) - i):
                # we check if we have atleast one space between previous match and next match
                # also we check if the remaining letters in t are enough for all of s to be considered as the edge case 
                return True 

        return False