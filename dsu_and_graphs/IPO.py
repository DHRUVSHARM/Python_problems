from typing import List

"""

n projects

Input: k = 2, w = 0, 

profits = [1,   2,3], 
capital = [0,   1,1]


sort by capital

(0 , 1) (1 , 2) (1 , 3)

min cost max profit


max_profit, cost
dp[k = 0] = [0 , 0]

# iterate over 
dp[k = 1] = 


Output: 4


initial state dp[w][i] : (w capital , i .. number of projects )


dp[i][w] = w capital , 0 ... i

 w - capital[i] >= 0
 k - 1 >= 0

dp[i][w][k] = max(  dp[i - 1][w][k]  , dp[i - 1][w - capital[i]][k - 1] + profit[i]  )

max profit from w capacity, atmost k jobs, 0 ... i


dp 0   1   2


"""
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # we will need k rounds
        jobs = [(cap , profit) for cap , profit in zip(capital , profits)]
        jobs.sort()

        q = []

        result , index = w , 0
        # the built capacity is stored in result
        for _ in range(0 , k):
            # try to add as many jobs in capacity 
            while index < len(jobs) and result >= jobs[index][0]:
                # we can start this job and potentially increase capacity 
                heapq.heappush(q , -1 * jobs[index][1])
                index += 1
            
            if len(q):
                # we can pop out max profit and add it to cap 
                profit = heapq.heappop(q)
                result += (-profit)

        return result