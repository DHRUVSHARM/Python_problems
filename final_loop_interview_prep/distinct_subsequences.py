"""

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

distince subsequences are of s 
# check if they equal to target t

rabbbit 
   
rabbit 

dp[i , j] = number of subsequences from i... , j...
= dp[i + 1][j + 1] move j only if s[i] == t[j] 
 dp[i + 1][j] , match something further anyways 

 dp[....][len(t)] , using some ending we are able to cover t ,  return 1
 anything else where len(s) reached, but not full t return 0 

"""

import collections
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = collections.defaultdict(int)

        result = 0
        for j in range(len(t) - 1 , -1 , -1):
            for i in range(len(s) - 1 , -1 , -1):
                # fix a j start on t
                # consider from start of s
                if j == len(t) - 1:
                    if s[i] == t[j]:
                        dp[(i , j)] += 1
                else:
                    if s[i] == t[j]:
                        dp[(i , j)] += dp.get((i + 1 , j + 1) , 0)
                dp[(i , j)] += dp.get((i + 1 , j) , 0)
                
                
        result = dp[(0 , 0)]
        
        return result