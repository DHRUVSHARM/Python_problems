from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_f , max_s , max_t = float("-inf") , float("-inf") , float("-inf")
        min_f  , min_s = float("inf") , float("inf")

        for digit in nums:
            if digit > max_f:
                max_f , max_s , max_t = digit , max_f , max_s
            elif max_s < digit <= max_f:
                max_s , max_t = digit , max_s
            elif max_t < digit <= max_s:
                max_t = digit
            else:
                # ignore 
                pass

            # same pattern for minimal element 
            if digit < min_f:
                min_f , min_s = digit , min_f
            elif min_f <= digit < min_s:
                min_s = digit
            else:
                # ignore
                pass


        return max(
            max_f * max_s * max_t ,
            max_f * min_f * min_s
        )
