class Solution:
    def canReachUnoptimal(self, s: str, minJump: int, maxJump: int)->bool:
        # 011010
        dp = [False for _ in range(0 , len(s))]

        dp[0] = True

        if s[-1] == '1':
            return False

        for index in range(1 , len(s)):
            
            if s[index] == '1':
                # cannot land on a one
                continue

            lower , upper = index - maxJump , index - minJump 

            can_jump = False

            if upper < 0:
                continue

            lower = max(0 , lower)

            for j in range(lower , upper + 1):
                if s[j] == '0' and dp[j]:
                    can_jump = True
                    break
                
            dp[index] = can_jump

        return dp[-1]
    
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    
        dp = [False for _ in range(0 , len(s))]

        dp[0] = True

        if s[-1] == '1':
            return False

        jump_count = 0
        for index in range(1 , len(s)):
            if (index - maxJump - 1) >= 0 and dp[index - maxJump - 1]:
                jump_count -= 1
            if (index - minJump) >= 0 and dp[index - minJump]:
                jump_count += 1
            
            # check if the window created is valid or not
            if (index - minJump) >= 0:
                # print("jump count : " , jump_count)
                # we can say that the window is valid 
                if jump_count and s[index] == '0':
                    dp[index] = True
            else:
                # window is not valid
                pass



        return dp[-1]