class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # map the length modulo to the minimal sum
        subarr_sums = {index : float("inf") for index in range(0 , k)}
        subarr_sums[0] = 0

        ans , curr_sum = float("-inf") , 0

        for index , element in enumerate(nums):
            curr_sum += element
            ans = max(
                ans,
                curr_sum - subarr_sums[(index + 1) % k]
            )

            
            subarr_sums[(index + 1) % k] = min(
                subarr_sums[(index + 1) % k],
                curr_sum
            ) 
        
        # print(subarr_sums)
        # print(ans)

        return ans

