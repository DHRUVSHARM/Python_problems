import collections
from typing import List

d = collections.deque()
d.append(1)
d.append(3)
d.append(5)
print(d)
d.popleft()
d.popleft()
print(d)


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        d = collections.deque()
        flips = 0

        for r in range(0, len(nums)):
            while d and r - k + 1 > d[0]:
                d.popleft()

            if (nums[r] + len(d)) % 2 == 1:
                pass
            else:
                if r + k - 1 < len(nums):
                    flips += 1
                    d.append(r)
                else:
                    flips = -1
                    break

        return flips
