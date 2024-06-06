from locale import atoi


class Solution:
    def scoreOfString(self, s: str) -> int:
        # at least 2
        score = 0
        for index in range(1, len(s)):
            score += abs(ord(s[index]) - ord(s[index - 1]))

        return score


print(int("a"))

# print(abs(ord("o") - ord("l")))
# print(111 - 108)
