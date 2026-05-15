"""
			

a + 1 <= c <= a + limit
b + 1 <= c <= b + limit

A + limit >= 1 + limit >= b + 1

A + limit >= b + 1 => overlap

A+ b >= 1 + b
B + a<= limit + a

B > a , so 

A + 1 ⇐ c <= b+ limit



2 <= C < a + 1				b + limit < c <= 2*limit 


—------------------------------------------

The below will show c as chosen variable over the intervals.

[2 , a+1)  = 2
(b + limit, 2*limit] = 2

[a + 1 , b + limit] = 1

For 0 moves, 
A + b			=	0

So for any c over, 2 … 2*limit (both limit) the above describes moves 



—--------------------------------------------------
proof

A >= 1
B <= limit 

1 + b<=  A + b <= limit + a
So a + b is a point in the interval

A >= 1
B <= limit


observations 

c varies from 2 to 2*limit 
# we can map the variation of selected c in terms of moves over this range, and do 
# queries by calculating preffix sums take minimal 


we need to choose, c

if c = a + x
x = c - a

a , b should be 1 <= limit 

1 <= c - a <= limit
a + 1 <= c <= limit + 1

similarly 

c - b = x 
b + 1 <= c <= limit + 1

min(a + 1 , b + 1) <= c <= limit + 1

-----------------------------------------------------------------------------------------
a + 1 <= c <= limit + 1 : 1 op
c in [2 , a + 1) or c in (limt + 1 , 2*limit]   : 2op
c = a + b is 1 op

------------------------------------------------------------------------------------------

The below will show c as chosen variable over the intervals.

[2 , a+1)  = 2

[a + b] = 1

[a + 1 , b + limit] = 1

(b + limit, 2*limit] = 2



For 0 moves, 
A + b			=	0

So for any c over, 2 … 2*limit (both limit) the above describes moves 



-----------------------------------------------------------------------------------------
dp[0 .. 2 .. 2*limit + 1]
2*limit  + 2

+2              -1  .......   -1     +1     ........  +1         .........   +1 
2   .....     a + 1 .......  a+b    a+b+1   ........  limit + 2  .........   2*limit + 1


"""

from typing import List
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        dp = [0] * (2*limit + 2)
        n = len(nums)

        for i in range(0 , n // 2):
            a = min(nums[i] , nums[n - i - 1])
            b = max(nums[i] , nums[n - i - 1])

            dp[2] += 2
            dp[a + 1] -= 1
            dp[a + b] -= 1
            dp[a + b + 1] += 1
            dp[1 + limit + b] += 1
            dp[2*limit + 1] += 1


        ans , res = float("inf") ,  0
        for c in range(2 , 2*limit + 1):
            res += dp[c]
            ans = min(ans , res)
        
        return ans


        

    