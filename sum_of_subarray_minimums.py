import collections
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s = collections.deque()
        # we will do this like the graham scan or largest rectangle style problem
        s.append((-1, float("-inf")))
        arr = arr + [float("-inf")]

        ans = 0

        for index, value in enumerate(arr):
            if value >= s[-1][1]:
                # monotonic increase , keep adding
                s.append((index, value))
            else:
                while len(s) and s[-1][1] > value:
                    # we will always have access to top after popping impl
                    # print("stack : " , s)
                    top_index, top_value = s.pop()
                    right = index - top_index
                    left = top_index - s[-1][0]
                    ans += top_value * (left * right)
                s.append((index, value))

        return ans % (10**9 + 7)
