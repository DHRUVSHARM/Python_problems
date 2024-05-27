import collections
from typing import List

if __name__ == '__main__':
    n = [11, 1, 1, 1, 3, 4, 5, 5, 4]
    fq = collections.Counter(n)
    print(fq)


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = collections.Counter(nums)
        pairs = 0

        for freq in frequency.values():
            pairs += (
                    ((freq - 1) * (freq)) // 2
            )

        return pairs
