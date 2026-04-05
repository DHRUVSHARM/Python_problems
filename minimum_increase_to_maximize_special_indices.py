from typing import List


"""
An index i (0 < i < n - 1) is special if nums[i] > nums[i - 1] and nums[i] > nums[i + 1].
so at the corbers we cannot have special indices
    make
[1, 2, 2]

<    i   >
[2 , 1 , 1 , 3]



dp[i] = max changes 

dp[i] = max(dp[i - 1] ,    max( max(nums[i + 1] , nums[i - 1]) + 1 - nums[i],  0) 


Let dp[i] = (max_i, min_i), where max_i is the maximum number of special indices you can make using the first i elements, and min_i 
is the minimum number of operations needed to achieve that.



dp[i][max_i] # max special indices  we can make using the first i elements 
           =  max(
                    dp[i - 1][max_i], # exclude - x
                    1 + dp[i - 2][max_i] # include - y
                )

if x >= y:
    dp[i - 1][min_i] # always choose not to in equal case since we can just take prev problem
else:
    # need to make the current value 
    max( max(nums[i + 1] , nums[i - 1]) + 1 - nums[i],  0) + dp[i - 2][min_i]

    
iterate i : 1 to n - 2
dp[0][max_i] = 0
dp[0][min_i] = 0

dp[-1][max_i] = dp[i - 1][max_i] # always exclude
dp[-1][min_i] = dp[i - 1][min_i] # always prev one, since we cannot do anything for current


overall ans, 
dp[-1][min_i] # consider all and take min ops ? 



3 <= n <= 105
1 <= nums[i] <= 109
"""

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(nums))] # dp[i][max_i / min_ops]

        for index in range(1 , len(nums)):
            if index == len(nums) - 1:
                dp[index][0] = dp[index - 1][0]
                dp[index][1] = dp[index - 1][1]
            else:
                x = dp[index - 1][0] # exclude current index 
                y = (dp[index - 2][0] if index - 2 >= 0 else 0)  + 1 # include current index

                dp[index][0] = max(x , y)

                if x > y:
                    # print("index : " , index)
                    dp[index][1] = dp[index - 1][1]
                elif x < y:
                    # max( max(nums[i + 1] , nums[i - 1]) + 1 - nums[i],  0) + dp[i - 2][min_i]
                    dp[index][1] = max( max(nums[index + 1], nums[index - 1]) + 1 - nums[index] , 0 ) + (dp[index - 2][1] if index - 2 >= 0 else 0) 
                else:
                    dp[index][1] = min(
                        dp[index - 1][1],
                        max( max(nums[index + 1], nums[index - 1]) + 1 - nums[index] , 0 ) + (dp[index - 2][1] if index - 2 >= 0 else 0)
                    )

        # print(dp)
        return dp[-1][1]