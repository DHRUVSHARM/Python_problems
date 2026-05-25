from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        dp = {}

        # dfs with memoization 
        def dfs(node):
            if node in dp:
                return dp[node]
            
            subans = 0
            # problem will loop infinitely but we constantly move to the 
            # point where we are reducing the value 
            # so bottom up once we reach the smallest -> second smallest -> so on...
            # move right
            for new_node in range(node + 1 , node + d + 1):
                if new_node < len(arr) and arr[node] > arr[new_node]:
                    # possible
                    subans = max(subans , dfs(new_node))
                else:
                    # we cant continue
                    break
            
            for new_node in range(node - 1 , node - d - 1 , -1):
                if new_node >= 0 and arr[node] > arr[new_node]:
                    subans = max(subans , dfs(new_node))
                else:
                    break
            
            dp[node] = 1 + subans
            return dp[node]

        for index in range(0 , len(arr)):
            dfs(index)
        
        result = 1 # can atleast get one index 
        # print(dp)
        for k , v in dp.items():
            result = max(result, v)
        
        return result
