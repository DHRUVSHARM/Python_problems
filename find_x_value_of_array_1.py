from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        dp[i][rem] : is the number of subarrays ending at i , with product % k remainder as rem 

        dp[i][rem] += (if the current element can be divide and get rem)
        
        """


        n = len(nums)
        dp = [[0 for _ in range(0 , k)] for _ in range(n)]

        # dp[i][rem] the number of subarrays ending at i, with product remainder as rem 
        dp[0][nums[0] % k] += 1 # one subarray for the first element 

        for index in range(1 , n):
            # one added for taking the single size subarray starting at this point 
            dp[index][nums[index] % k] += 1 
            # for the remaining we take the remainders in the previous layers and use it to build out the current layer
            # multiplication can use modulo (a.b)modk = (amodk)(bmodk) and so on 
            for rem in range(0 , k):
                dp[index][(rem * (nums[index] % k))%k] += dp[index - 1][rem]

        return [sum([dp[i][rem] for i in range(n)]) for rem in range(0 , k)]