from typing import List


"""
Example 1:
                                lr
Input: s = "a   b   c   a   b   c   b   b"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result , left , prev_index =  0 , 0 , collections.defaultdict()

        for r in range(0 , len(s)):
            if s[r] in prev_index:
                # found the point where repeat
                # move to make the condition valid
                target_left = prev_index[s[r]] + 1
                while left < target_left:
                    prev_index.pop(s[left])
                    left += 1
                prev_index[s[r]] = r
            else:
                # can add and consider in result
                prev_index[s[r]] = r
                result = max(result , r - left + 1)


        return result