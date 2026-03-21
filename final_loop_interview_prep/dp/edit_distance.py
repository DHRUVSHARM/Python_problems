import collections
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # need to convert word1 to word2 
        dp = collections.defaultdict()

        # base cases 
        dp[(-1 , -1)] = 0

        for j in range(0 , len(word2)):
            dp[(-1 , j)] = 1 + dp[(-1 , j - 1)] # keep inserting  
        
        for i in range(0 , len(word1)):
            dp[(i , -1)] = 1 + dp[(i - 1 , -1)] # keep deleting   
            

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    # always better to have no op and use prev result 
                    dp[(i , j)] = dp[(i - 1 , j - 1)]
                else:
                    dp[(i , j)] = min(
                        1 + dp[(i , j - 1)],
                        1 + dp[(i - 1 , j - 1)],
                        1 + dp[(i - 1 , j)]
                    )

        
        return dp[(len(word1) - 1 , len(word2) - 1)]
        