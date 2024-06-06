if __name__ == "__main__":
    s = "abciiidef"
    # strings can be iterated over like this
    for ele in s:
        print(ele)

"""
Given a string s and an integer k, return the maximum 
number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # we have the case of fixed sliding window
        vowels, curr_ans, ans, l = {"a", "e", "i", "o", "u"}, 0, 0, 0
        # the outer loop moves forward 1 at a time always
        for r in range(0, len(s)):
            if s[r] in vowels:
                curr_ans += 1

            # now we check if max-len should not be exceeded
            if r - l + 1 == k:
                ans = max(curr_ans, ans)
                if s[l] in vowels:
                    curr_ans -= 1
                l += 1

        return ans
