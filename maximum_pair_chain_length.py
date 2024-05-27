import collections
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # greedy solution,we sort by the finish time
        pairs.sort(key=lambda p: p[1])
        s, max_length = collections.deque([pairs[0]]), 1
        for index in range(1, len(pairs)):
            f_start, f_end = s[-1]
            start, end = pairs[index]

            if f_end < start:
                s.append([start, end])

            max_length = max(max_length, len(s))

        return max_length
