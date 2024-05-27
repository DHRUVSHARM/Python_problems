import collections
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, next, beams = 0, 1, 0

        while next < len(bank):
            while prev < next and bank[prev].count("1") == 0:
                prev += 1
            if prev < next and bank[next].count("1") != 0:
                beams += (
                    bank[prev].count("1") * bank[next].count("1")
                    )
                prev = next
            next += 1

        return beams