class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for index, element in enumerate(s):
            res += ((index + 1) * (1 + 25 - (ord(element) - ord('a')) ))

        return res