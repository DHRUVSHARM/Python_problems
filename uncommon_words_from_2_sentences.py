import collections
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_freq, s2_freq = collections.Counter(s1.split(" ")), collections.Counter(
            s2.split(" ")
        )

        ans = []

        for k, v in s1_freq.items():
            if v == 1 and (k not in s2_freq):
                ans.append(k)
            else:
                if k in s2_freq:
                    s2_freq.pop(k)

        for k, v in s2_freq.items():
            if v == 1 and (k not in s1_freq):
                ans.append(k)

        return ans
