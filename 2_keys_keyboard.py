class Solution:

    def minStepsSuboptimal(self, n:int) -> int:
        
        dp = {}

        # recursive solution
        def dfs(screen_chars, copied_chars):
            
            if (screen_chars , copied_chars) in dp:
                return dp[(screen_chars , copied_chars)]

            if screen_chars == n:
                # correct method
                dp[(screen_chars , copied_chars)] = 0
                return dp[(screen_chars , copied_chars)]

            result = float("inf")

            if screen_chars != copied_chars:
                # we can do the copy all operation
                result = min(
                    result , 
                    1 + dfs(screen_chars , screen_chars)
                )

            # paste
            if copied_chars and (screen_chars + copied_chars) <= n:
                result = min(result , 1 + dfs(screen_chars + copied_chars , copied_chars))           
            
            dp[(screen_chars , copied_chars)] = result
            return dp[(screen_chars , copied_chars)]

        
        # start with one character and nothing copied
        result = dfs(1 , 0)
        return 0 if result == float("inf") else result
    

    def minSteps(self, n: int) -> int:
        # we will try to work on the iterative solution here 
        dp = [0 for _ in range(0 , n + 1)]

        # 0 means nothing, dp[1] = 0
        # dp[i] min steps to reach length i on the screen

        for index in range(2 , n + 1):
            # we will have the length here 
            result = float("inf")
            for j in range(1 , (index // 2) + 1):
                if index % j == 0:
                    result = min(
                        result,
                        (index // j) + dp[j]
                     )
            dp[index] = result

        # print(dp)

        return dp[n]    