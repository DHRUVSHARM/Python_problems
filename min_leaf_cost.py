import collections
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # very interesting problem
        s = collections.deque([float("inf")])
        # for ease
        res = 0

        for element in arr:
            if element < s[-1]:
                # decreasing
                s.append(element)
            else:
                while len(s) >= 2 and element >= s[-1]:
                    res += s[-1] * min(element, s[-2])
                    # print(res)
                    s.pop()
                s.append(element)

        # print(s)
        while len(s) > 2:
            res += s[-1] * s[-2]
            s.pop()

        return res
