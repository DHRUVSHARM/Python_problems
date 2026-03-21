"""

You are given n balloons, indexed from 0 to n - 1.

Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 

If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]

8 + [3 , 1, 5]
1.3.8 + 8 + 3.5.8 + 1.3.5

[3] ? 3 is the max
[1]
[5]
[8]
--------------



1 [3 , 1] 5

3 * 1 * 5 + dp[i + 1, j] + dp[...i - 1]

Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100


dp[l , r] = for all l <= k <= r max
                pop k last, collect residues
                dp[l..k-1] + dp[k + 1...r] + nums[l - 1] * nums[k] * nums[r + 1] , 1 default for out of bounds
                0 default for invalid size intervals 

"""


from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(0 , n)] for _ in range(0 , n)]
        
        for off in range(0 , n):
            i , j = 0 , off
            while i < n and j < n:
                
                for k in range(i , j + 1):
                    left_boundary = 1 if i - 1 < 0 else nums[i - 1]
                    right_boundary = 1 if j + 1 == len(nums) else nums[j + 1] 
                    left = dp[i][k - 1] if i <= (k - 1) else 0  # cross over means zero 
                    right = dp[k + 1][j] if (k + 1) <= j else 0

                    dp[i][j] = max(
                        dp[i][j],
                        left_boundary * nums[k] * right_boundary + left + right
                    )

                i += 1
                j += 1
        
        # print(dp[0][0])
        return dp[0][n-1]