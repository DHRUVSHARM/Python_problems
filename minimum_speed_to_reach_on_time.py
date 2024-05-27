import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def check(speed):
            # we have to ceil all except the last destination
            time_taken = 0.0
            for index in range(0 , len(dist) - 1):
                time_taken += math.ceil(dist[index] / speed)

            time_taken += (dist[-1] / speed)
            return True if time_taken <= hour else False

        l, r = 0, 10 ** 7 + 1
        while l + 1 < r:
            # bs of the form [..FFFFFFFFFTTTT...]
            mid = l + int((r - l) / 2)
            if check(mid):
                r = mid
            else:
                l = mid

        return -1 if r == (10 ** 7 + 1) else r
