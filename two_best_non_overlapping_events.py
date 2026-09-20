from bisect import bisect_left
class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        events.sort(key = lambda element : (element[1] , element[0])) # sort by end times 

        # dp[i][k]

        dp = [[0 for _ in range(0 , 3)] for _ in range(0 , n)]

        # for all dp[i][0] it will be 0 
        # dp[0][for all ] will be value[0]

        for limit in range(1 , 3):
            dp[0][limit] = events[0][2] # always best to pick value 


        for i in range(1 , n):
            for limit in range(1 , 3):
                dp[i][limit] = dp[i - 1][limit] # consider previous answer 
                # strict boundary condition so we find first end < curr_start
                idx = bisect_left(events, events[i][0] , 0 , i , key = lambda element : element[1]) - 1
                dp[i][limit] = max(
                    dp[i][limit],
                    (0 if idx == -1 else dp[idx][limit - 1]) + events[i][2]
                )


        return dp[n - 1][2]