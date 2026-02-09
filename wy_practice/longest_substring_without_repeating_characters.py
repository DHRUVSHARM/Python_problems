"""
Docstring for waymo.longest_substring_without_repeating_characters


"abc cab bb"
ab|c bac bb
"""
import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans , prev_occ , left = 0 , collections.defaultdict(int) , 0

        # we will need to do sliding window
        for r in range(0 , len(s)):
            if s[r] not in prev_occ:
                # keep left as aero
                pass
            else:
                # we see a repeat, need to look at the previous occ
                prev_index = prev_occ[s[r]] 
                # move left greater
                left = max(left , prev_index + 1)
            
            ans = max(ans , r - left + 1)
            # update 
            prev_occ[s[r]] = r


        return ans