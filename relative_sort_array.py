import collections
from typing import List

arr = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
f = collections.Counter(arr)
print(f)

for k in sorted(list(f.keys())):
    print(k, " , ", f[k])


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = collections.Counter(arr1)
        result = []
        removed = []
        for k in arr2:
            occur = freq[k]
            while occur:
                result.append(k)
                occur -= 1
            removed.append(k)

        for k in removed:
            freq.pop(k)

        for k in sorted(list(freq.keys())):
            occur = freq[k]
            while occur:
                result.append(k)
                occur -= 1

        return result
