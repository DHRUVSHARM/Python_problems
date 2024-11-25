from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []

        if k == 0:
            return [0] * len(code)
        elif k > 0:
            # we pick the [l , r] from [1 , k]
            l , r = 1 , k
        else:
            l , r = len(code) - abs(k) , len(code) - 1

        cum_sum = 0
        for i in range(l , r + 1):
            cum_sum += code[i]
            
        ans.append(cum_sum)

        for i in range(1 , len(code)):
            cum_sum -= code[l]
            l = (l + 1) % len(code)
            r = (r + 1) % len(code)
            cum_sum += code[r]
            ans.append(cum_sum)

        return ans