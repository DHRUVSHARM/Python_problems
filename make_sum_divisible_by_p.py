class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder , curr_sum = total % p , 0

        # idea is :
        # is to think in 2 dimensions.
        # one is ending at a particular index
        # so we take the running sum of sorts
        # the other is to think about how we can minimize the answer selected at each step

        # so say we select a subarray
        # currsum % p = remainder 
        # so we need that after removing it from the left the remainder will have %p as 0

        # but in this also if we keep track of the closest end
        # such that subarray % p - x  = remainder
        # then subarray % p - remainder = x

        if not remainder:
            return 0
        
        indices = collections.defaultdict(int)

        indices[0] = -1

        ans = float("inf")

        for index, element in enumerate(nums):
            curr_sum += element
            curr_sum %= p

            # print("----------------------------------------------------")

            # print("curr sum : " , curr_sum)

            prefix_sum = (curr_sum - remainder + p) % p

            # print(prefix_sum)
            
            # print(indices)

            if prefix_sum in indices and (index - indices[prefix_sum] < len(nums)):
                ans = min(
                    ans , 
                    index - indices[prefix_sum] 
                )
            
            # print("ans : " , ans)
            
            indices[curr_sum] = index

        return -1 if ans == float("inf") else ans