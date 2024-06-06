import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occur, ans = collections.defaultdict(int), -1

        for index in range(0, len(s)):
            if s[index] not in first_occur:
                first_occur[s[index]] = index
            else:
                ans = max(ans, index - first_occur[s[index]] - 1)

        return ans
