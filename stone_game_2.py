from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # second problem in the series
        n = len(piles)
        total = 0
        for element in piles:
            total += element
        # cache
        dp = {}

        def dfs(l: int, r: int, m: int, player: int) -> int:
            """
            here the state is a range of the piles array , we also need to keep
            track of M also , so this style is best
            :param player: 0 for alice , 1 for bob
            :param m: M
            :param l: start pt
            :param r: end pt
            :return: result
            """

            if (l, r, m, player) in dp:
                return dp[(l, r, m, player)]

            if l > r:
                return 0

            dp[(l, r, m, player)] = float("-inf")
            sum = 0

            for x in range(1, 2 * m + 1):

                if l + x - 1 > r:
                    continue

                sum += piles[l + x - 1]

                dp[(l, r, m, player)] = max(
                    dp[(l, r, m, player)], sum - dfs(l + x, r, max(m, x), player ^ 1)
                )

            return dp[(l, r, m, player)]

        ans = dfs(0, n - 1, 1, 0) + total
        return ans // 2


# minmax algorithm based approach with dp 

# import collections 
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
            dp[i][m] = for all all 0 <= a <= 2m - 1
                sum(i , i + a) + dp[i + a + 1][max(m , a + 1)]
        """


        dp = {}
        prefix_sum = {}
        prefix_sum[-1] = 0
        for index, element in enumerate(piles):
            prefix_sum[index] = element + prefix_sum[index - 1]
        
        # in the minmax algorithm version of this problem 
        # dfs(i , m , alice) : represents the problem starting at i,m,player but alices score playing optimally 
        # if bob we do not add the stones since they are not collected 
        # key is to think of this as alice's score only regardless of player 
        def dfs(i , m , alice):
            # both players play optimally 
            if i == len(piles):
                return 0 # consider 0 pile at the end 

            if (i , m , alice) in dp:
                return dp[(i , m , alice)]
            
            ans = float("inf") if alice == 0 else float("-inf")
            for a in range(0 , 2*m):
                if i + a + 1 == len(piles) + 1:
                    break

                new_index = i + a + 1

                if alice == 1:
                    ans = max(
                        ans,
                        (prefix_sum[new_index - 1] - prefix_sum[i - 1]) + dfs(new_index, max(m , a + 1) , alice ^ 1)
                    )
                else:
                    # bob wants to minimize alice's score
                    # we take the minimal from this point to return to alic 
                    ans = min(
                        ans,
                        dfs(new_index, max(m , a + 1) , alice ^ 1)
                    )
            
            dp[(i , m , alice)] = ans
            return dp[(i , m , alice)]

        stones = dfs(0 , 1 , 1)
        return stones 


# bottom up dp solution memoized 
# import collections 
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        this approach will use dp 
        if it easier for the problem ordering to 
        consider the dp[i][m] the entire problem from i ...
        since we need to consider the entire variation of the problem

        not just the difference, hence the result has to be accumalated 

        dp[i][m] = max(suffix sum selected - dp[new_i][m] )
        # max stones collected by alex starting at m from i ...
        0 ... selected.....end - selected ... x .. end + x .. end
        
        = 0 ... selected + x .. end (sums up the alice value )
        """
        
        dp , n , suffix = {} , len(piles) , {}
        # suffix sum 
        suffix[n] = 0
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        def dfs(i , m):
            if i == len(piles):
                return 0
            
            if (i , m) in dp:
                return dp[(i , m)]
            
            ans = float("-inf")
            for a in range(0 , 2*m):
                if i + a + 1 <= len(piles):
                    new_index = i + a + 1
                    ans = max(
                        ans,
                        suffix[i] - dfs(new_index, max(m , a + 1))
                    )
                else:
                    break
            
            dp[(i , m)] = ans
            return dp[(i , m)]
        

        return dfs(0 , 1)