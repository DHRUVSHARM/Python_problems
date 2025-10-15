class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # first we will try the on n square approach
        prefix_sums = collections.defaultdict(int)
        prefix_sums[-1] = 0

        for index , element in enumerate(nums):
            prefix_sums[index] = prefix_sums[index - 1] + element
        
        # prefix sums enables o(1) lookup hence quadratic TC
        ans = False
        for start in range(0 , len(nums)):
            for end in range(start + 1 , len(nums)):
                sub_sum = prefix_sums[end] - prefix_sums[start - 1]
                if sub_sum % k == 0:
                    ans = True
                    return ans
        
        return ans