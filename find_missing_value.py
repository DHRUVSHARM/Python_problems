import collections
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_missing_value = mean * (len(rolls) + n) - sum(rolls)

        ans = []

        for index in range(0, n):
            max_val = min(6, total_missing_value - (n - index - 1))
            if max_val < 1:
                return []
            ans.append(max_val)
            total_missing_value -= max_val

        if total_missing_value > 0:
            return []

        return ans
