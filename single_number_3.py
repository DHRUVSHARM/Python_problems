from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for element in nums:
            xor_sum ^= element

        mask = 1
        # to find the first set bit
        while not (mask & xor_sum):
            mask = mask << 1

        one, zero = 0, 0
        for element in nums:
            if element & mask:
                one = one ^ element
            else:
                zero = zero & element

        return [one, zero]
