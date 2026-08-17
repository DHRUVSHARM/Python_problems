from typing import List

"""
each round, divide into 2 non empty rows 

alice : 
divides 
[           ] , [               ]

bob :
    calculate the sum : sum1 , sum2 
    max(sum1 , sum2)



dp[l .... r] = max(
    dp[l ... x] , dp[x .... r] take the minimal of the 2 add that prefix, if not then both 
)


l, r seems to be ok
current approach is cubic, if x can be found in constant time then will be quadratic 


[ , , ,, , , , x , ,, , , , ]
"""

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[None for _ in range(0 , n)] for _ in range(0 , n)]
        prefix_sum = []

        for element in stoneValue:
            prefix_sum.append((0 if len(prefix_sum) == 0 else prefix_sum[-1]) + element)

        def dfs(l , r):
            if dp[l][r] is not None:
                return dp[l][r]

            if (r - l + 1) == 1:
                dp[l][r] = 0
                return 0 # nothing to throw for alice 

            ans = 0 # minimal score possible, need to maximize  
            for x in range(l , r):
                # check maximal split
                left_sum , right_sum = prefix_sum[x] - (prefix_sum[l - 1] if l - 1 >= 0 else 0) , prefix_sum[r] - prefix_sum[x]
                if left_sum == right_sum:
                    # alice can choose she will try and choose the max path 
                    ans = max(
                        ans,
                        left_sum + dfs(l , x),
                        right_sum + dfs(x + 1 , r)
                    )
                elif left_sum < right_sum:
                    # alice can split but will be forced to pick the smaller path since 
                    # bob will select that 
                    ans = max(
                        ans,
                        left_sum + dfs(l , x)
                    )
                else:
                    ans = max(
                        ans,
                        right_sum + dfs(x + 1 , r)
                    )

            dp[l][r] = ans
            return ans


        return dfs(0 , len(stoneValue) - 1)
