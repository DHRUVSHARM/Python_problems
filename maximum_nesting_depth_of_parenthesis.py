import collections


class Solution:
    def maxDepth(self, s: str) -> int:
        balance, ans = 0, 0

        for c in s:
            if c == "(":
                balance += 1
            elif c == ")":
                balance -= 1
            ans = max(ans, balance)

        return ans
