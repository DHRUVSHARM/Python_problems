import collections
from typing import List

"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans , subsum , l , freq = 0 , 0 , 0 , collections.defaultdict(int)

        for r in range(0 , len(nums)):
            freq[nums[r]] += 1
            if freq[nums[r]] == 1:
                subsum += nums[r]
            
            if len(freq) == k:
                #print("before : " , freq)    
                while l < r and (r -l + 1) > len(freq):
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        freq.pop(nums[l])
                        subsum -= nums[l]
                    l += 1
                #print("after : " , freq)
                if (r - l + 1) == k:
                    ans = max(ans , subsum)
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        freq.pop(nums[l])
                        subsum -= nums[l]
                    l += 1
                

        return ans

"""

# much simpler
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans , subsum , freq , l = 0 , 0 , collections.defaultdict(int) , 0

        for r in range(0 , k):
            freq[nums[r]] += 1
            if freq[nums[r]] == 1:
                subsum += nums[r]

        if len(freq) == k:
            ans = max(ans , subsum)

        for r in range(k , len(nums)):
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                subsum -= nums[l]
                freq.pop(nums[l])
            l += 1

            freq[nums[r]] += 1
            if freq[nums[r]] == 1:
                subsum += nums[r]
            
            if len(freq) == k:
                ans = max(ans , subsum)

        return ans