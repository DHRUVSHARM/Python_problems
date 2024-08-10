from typing import List
import collections


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = collections.Counter(arr)

        ans, count = "", 0

        for element in arr:
            if freq[element] == 1:
                count += 1
                if count == k:
                    ans = element

        return ans
