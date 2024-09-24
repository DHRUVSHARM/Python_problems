class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        ans, vowels, curr_mask, prefix_map = (
            0,
            {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4},
            0,
            {0: -1},
        )

        for index, ele in enumerate(s):
            if ele in vowels:
                curr_mask = curr_mask ^ (1 << vowels[ele])
            if curr_mask not in prefix_map:
                prefix_map[curr_mask] = index
            else:
                ans = max(ans, index - prefix_map[curr_mask])

        return ans
