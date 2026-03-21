"""

You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:
                    l           r                      
Input: s = "A   A   B   A   B   B   A", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

"""
import collections
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        left , result , max_freq = 0  , 1 , 0



        for r in range(0 , len(s)):
            # add the frequency
            freq[s[r]] += 1

            # only update when the max freq updated 
            if freq[s[r]] > max_freq:
                max_freq = freq[s[r]]
            
            # window limits will be if we can allow the previously seen max in size atleast
            while left < r and (r - left + 1 - max_freq) > k:
                freq[s[left]] -= 1
                left += 1
            
            # can consider, even if window is invalid, it can atleast hold the previous value, so it is valid to take
            result = max(result , r - left + 1)

        return result
