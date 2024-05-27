import bisect
from typing import List

if __name__ == '__main__':
    a = [10, 20, 30, 40]
    # bisect
    print(bisect.bisect_left(a, 21))

    x = [(0, 2, 3), (1, 4, 3), (2, 2, 4), (5, 5, 3)]
    x.sort(key=lambda e: (e[1], e[0], e[2]))
    x.insert(0, (-1, -1, -1))
    print(x)


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        # sorting events by increasing end time
        events.sort(key=lambda e: (e[1], e[0], e[2]))
        events.insert(0, (-1, -1, -1))

        def bs(left, right, element):
            while right - left > 1:
                mid = (left + right) // 2
                if events[mid][1] <= element:
                    left = mid
                else:
                    right = mid

            return left

        dp = [0 for _ in range(len(events))]
        dp[1] = events[1][2]  # always better to select in case of one element

        for index in range(2, len(dp)):
            j = bs(0, index, events[index][0])
            dp[index] = max(
                dp[index - 1],
                events[index][2] + dp[j]
            )

        return dp[-1]
