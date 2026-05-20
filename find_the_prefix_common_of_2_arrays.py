from typing import List

import collections
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        freq = collections.defaultdict(int)

        for a , b in zip(A, B):
            freq[a] += 1
            freq[b] += 1

            new_common = 0

            if a == b:
                if freq[a] == 2:
                    new_common += 1
            else:
                if freq[a] == 2:
                    new_common += 1
                
                if freq[b] == 2:
                    new_common += 1

            res.append((res[-1] if len(res) else 0) + new_common)

        
        return res