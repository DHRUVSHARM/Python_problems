from typing import List

"""

2 constrainsts : 1 is 
k is the max number of events we can attend 

end < start (strict req)

<   >= (bl(start)) - 1
<=  >

imp constraints
1 <= k <= events.length

note if k == 0 , 0 is the answer since that is the val you can pickup at best 
for i = 0, k = 0 0 
            k= 1 and above pick i 

that is enough for base cases 
value function is simple to pickup 

"""

from bisect import bisect_left
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda element : element[1]) # sort by end time     
        n = len(events)

        dp = [[float("-inf") for _ in range(0 , k + 1)] for _ in range(0 , n)]  
        for i in range(0 , n):
            dp[i][0] = 0

        for limit in range(1 , k + 1):
            dp[0][limit] = events[0][2] # simply pick what is available 



        for index in range(1 , n):
            for limit in range(1 , k + 1):
                dp[index][limit] = dp[index - 1][limit] # dont consider 
                idx = bisect_left(events, events[index][0] , 0 , index, key=lambda element : element[1]) - 1
                dp[index][limit] = max(
                    dp[index][limit],
                    (0 if idx == -1 else dp[idx][limit - 1]) + events[index][2]
                )


        return dp[n - 1][k]