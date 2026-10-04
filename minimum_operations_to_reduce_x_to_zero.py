"""

x = 5

[   1,   1,   4,   2,   3   ]

1   +   1   +   4   +   2   +   3 = 11 
11 - OUTER_SUM = middle part 
we want x - middlepart = 0
x = middlepart

so 



total - outersum = subarr_sum

we can use sliding window approach 



"""

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:   
        total = sum(nums)

        # idea is to find longest subarray that will keep out x - (total - outer) negative or 0 if positive, increasing further is not useful 
        # so when we incr sum incr, means outer dec, so x - outer inc, so a positive sum will keep increasing 

        left , n , curr_sum = 0 , len(nums) , 0
        ans = float("inf")

        for r in range(0 , len(nums)):
            curr_sum += nums[r] # add current 

            while left <= r and (total - curr_sum) > 0:
                # reduce to negative
                curr_sum -= nums[left]
                left += 1

            if (total - curr_sum) == 0:
                # we can consider this 
                # this will catch the overall case 
                # and also keep extending the window
                ans = min(
                    ans,
                    (left) + (n - 1 - r)
                )


        return -1 if ans == float("inf") else ans

