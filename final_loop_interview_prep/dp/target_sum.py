"""
[2 , 1]

+2 -1 = 1
-2 +1 = -1
-2 -1 = -3
+2 + 1 = 3


dp[target][i] = ways to form target with numbers [0  .. i ] ? 
2 , 1
dp[t][i] = dp[t - element][i - 1] + dp[t + element][i - 1]

intuition is multiple base cases 


dp[0][-1] = 1


                     7 - 15
-target              target 
-sum nums, --- sum nums



                                0          
               -3   -2    -1    0        1     2    3
                            dp[0][-1] = 1

# we need an ordering to solve the problem 


dp[2][0] = dp[2-2][-1] + dp[2 + 2][-1]
dp[t][i] = dp[t - e]

"""

from typing import List

import collections
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # we can leverage the symmetric property as well
        dp = collections.defaultdict(int)
        dp[(0 , -1)] = 1
        lower = -1 * sum([abs(element) for element in nums])
        upper = -1 * lower

        for index in range(0 , len(nums)):
            for t in range(0 , upper + 1):
                dp[(t , index)] = dp.get((t - nums[index] , index - 1) , 0) + dp.get((t + nums[index] , index - 1) , 0)
                dp[(-t , index)] = dp[(t , index)] # mirror the problem by taking the opp selection of each element 
        

        return dp[(target , len(nums) - 1)]