class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans, index = len(t) + 1, 0
        for r in range(0, len(s)):
            if index < len(t) and s[r] == t[index]:
                index += 1

        return min(ans, len(t) - index)
