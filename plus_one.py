import collections
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        result = collections.deque()

        carry = (digits[index] + 1) // 10
        result.appendleft((digits[index] + 1) % 10)
        index -= 1

        while index >= 0:
            result.appendleft((digits[index] + carry) % 10)
            carry = (digits[index] + carry) // 10
            index -= 1

        if carry:
            result.appendleft(carry)

        return list(result)
