import collections
from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # for optimization we will fill a subarray sum dictionary
        sums = collections.defaultdict(int)
        sub_sum = 0
        for index in range(0 , k):
            sub_sum += nums[index]
        sums[0] = sub_sum

        left = 0
        for r in range(k , len(nums)):
            sub_sum += nums[r]
            sub_sum -= nums[left]
            left += 1
            sums[left] = sub_sum

        dp = collections.defaultdict(int)
        # now we need a dp helper that will be used to solve the subproblems fast using cache 
        # a state may be defined with the start index , num_subarrays

        def dfs(index , subarrays):
            
            # base cases
            if subarrays == 0:
                # valid ans
                return 0
            
            if index >= len(nums):
                # invalid ans
                return float("-inf")

            if (index , subarrays) in dp:
                return dp[(index , subarrays)]
            
            ans = max(
                sums[index] + dfs(index + k , subarrays - 1),
                dfs(index + 1 , subarrays)
            )

            dp[(index , subarrays)] = ans
            return ans


        ans , index , subarrays = [] , 0 , 3
        while index < len(nums):
            include = sums[index] + dfs(index + k , subarrays - 1)
            exclude = dfs(index + 1 , subarrays)
            
            # print("index : " , index , " , " , " inc , exc : " , include , " , " , exclude)

            if include >= exclude:
                ans.append(index)
                index += k
                subarrays -= 1
            else:
                index += 1
        
        return ans