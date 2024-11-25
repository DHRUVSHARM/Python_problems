from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_sum = 0
        for element in nums:
            xor_sum ^= element
        
        ans , n , mask = [] , len(nums) , 2**maximumBit - 1
        while n:
            ans.append((xor_sum ^ mask))
            n -= 1
            xor_sum ^= nums[n]

        return ans