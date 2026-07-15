from typing import List

"""


1 <= nums.length <= 200
1 <= nums[i] <= 200

number of elements in both sequences should be non empty

we may need to precompute the gcd using euclids algorithm


"""

# log(min(a , b))
def gcd(a , b):
    while a:
        a , b = b % a , a
    
    # once a is 0 b is the gcd
    # 0 % 3 = 0
    # 10 % 3 = 1
    # 1 % 3 = 1 # used to reverse 
    return b


N = 201
GCD_LOOKUP = [[0 for _ in range(0 , N)] for _ in range(0 , N)]

for i in range(0 , N):
    for j in range(0 , N):
        GCD_LOOKUP[i][j] = gcd(i , j)




import collections
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        """
        
        dp[0][0][0] = 1 # indicates equal gcd 

        # like a pull dp 
        bottom up we enumerate the index, g1, g2 and using the current nums we dervie the next state 
        
        """

        prev_dp = collections.defaultdict(int)
        m = 10**9 + 7

        prev_dp[(0 , 0)] = 1


        for i in range(1 , len(nums) + 1):
            curr_num = nums[i - 1]
            new_dp = collections.defaultdict(int)

            # use previous layer 
            for k , v in prev_dp.items():
                prev_g1 , prev_g2 = k
                new_dp[(GCD_LOOKUP[prev_g1][curr_num] , prev_g2)] += prev_dp[(prev_g1 , prev_g2)]
                new_dp[(prev_g1 , GCD_LOOKUP[prev_g2][curr_num])] += prev_dp[(prev_g1 , prev_g2)]
                new_dp[(prev_g1 , prev_g2)] += prev_dp[(prev_g1 , prev_g2)]

            prev_dp = new_dp

        # collect all in end 
        ans = 0
        for common_gcd in range(1 , N):
            ans = (ans + prev_dp[(common_gcd , common_gcd)]) % m
        
        return ans