import collections
from typing import List


arr = [1 , 0 , 1, 0 , 1 , 1]
print("".join(arr))


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        
        masks = collections.defaultdict(int)

        for row in matrix:
            key = "".join([str(element) for element in row])
            inverse_key = "".join([str(element ^ 1) for element in row])

            if key in masks or inverse_key in masks:
                if key in masks:
                    masks[key] += 1
                else:
                    masks[inverse_key] += 1
            else:
                masks[key] += 1
            

        for v in masks.values():
            ans = max(ans , v)

        return ans