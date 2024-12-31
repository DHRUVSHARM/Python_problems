import collections
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 0

        def find_key(current_day):
            """
            constant time helper that finds the day that covers the distance at a minimum
            """
            day , idx = 0 , -1
            # print("current day : " , current_day)
            while day < current_day:
                idx += 1
                day = days[idx]
                
            # print("day is : " , day)
            
            if day == current_day or day == 0:
                pass
            else:
                day = days[idx - 1]
            # print("day is : " , day)
            return day

        for day in days:
            dp[day] = min(
                costs[0] + dp[find_key(day - 1)],
                costs[1] + dp[find_key(day - 7)],
                costs[2] + dp[find_key(day - 30)]
            )
        
        # print(dp)

        return dp[days[-1]]