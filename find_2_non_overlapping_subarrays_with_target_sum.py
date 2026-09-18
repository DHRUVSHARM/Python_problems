"""
[   3,  2,  2,  4,  3], target = 3
    3   5   7  11   14


since the values are positivie, so i think we can use sliding window 

prefix[i], maintain hashmap, with the largest index for prefix 

1 <= arr.length <= 105
1 <= arr[i] <= 1000
1 <= target <= 108


"""

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        prefix_sum_index = {0 : -1}
        n = len(arr)
        prefix_sum = 0

        prefix_dp = [float("inf") for _ in range(n)]
        # prefix i smallest len with target k but note not including the current element 

        # NOTE prefix[r] - prefix[l - 1] = target(r -l + 1) (taking diff of indices r - (l - 1) gives the len )
        for r in range(0 , n - 1):
            # consider the current element and use for the next one 
            if r != 0:
                prefix_dp[r + 1] = prefix_dp[r] # older answer seed
            
            prefix_sum += arr[r]

            if (prefix_sum - target) in prefix_sum_index:
                prefix_dp[r + 1] = min(prefix_dp[r + 1] , r - prefix_sum_index[prefix_sum - target])
            
            prefix_sum_index[prefix_sum] = r # take the latest anyway  

        # print("prefix : " , prefix_dp)

        # suffix_dp[i] the same thing from i ... n
        suffix_dp = [float("inf") for _ in range(n)]
        suffix_index = {0 : n} # the end 
        suffix_sum = 0

        for r in range(n - 1 , -1 , -1):
            # first consider and do for the same element
            if r != (n - 1):
                suffix_dp[r] = suffix_dp[r + 1] # older seed 

            suffix_sum += arr[r]

            if (suffix_sum - target) in suffix_index:
                suffix_dp[r] = min(suffix_dp[r] , suffix_index[suffix_sum - target] - r ) 

            
            suffix_index[suffix_sum] = r # store for next 

        # print("suffix : " , suffix_dp)

        ans = float("inf")
        for i in range(1 , n):
            # at 0 we have < 0 so only one exists therefore we do 1 
            ans = min(
                ans,
                prefix_dp[i] + suffix_dp[i]
            )

        return -1 if ans == float("inf") else ans