"""
class Solution:
    def totalMoney(self, n: int) -> int:
        prev, curr, start, ans, index = 0, 1, 0, 0, 0

        while index < n:

            if index % 7 == 0:
                prev = start

            curr = prev + 1
            ans += curr
            prev = curr

            if index % 7 == 0:
                start = curr

            index += 1

        return ans
"""

from math import ceil


class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        start = n // 7
        ans = ans + int((start / 2) * (28 + 28 + (start - 1) * 7))
        print(ans)
        start += 1
        ans = ans + int(((n % 7) / 2) * (start + start + (n % 7) - 1))

        return ans
