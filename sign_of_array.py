# Problem summary:
# - Return the sign of the product of all numbers in the array without
#   computing the full product.
#
# Approach:
# - Scan each number once.
# - If any number is zero, the product is zero, so return 0 immediately.
# - Otherwise, toggle the sign parity every time a negative number appears.
# - After the scan, odd negative parity means a negative product; even parity
#   means a positive product.
#
# Pattern:
# - Linear scan with parity tracking.
#
# Complexity:
# - Time: O(n), where n is the length of nums.
# - Space: O(1).

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for element in nums:
            if element == 0:
                return 0
            elif element < 0:
                result = result ^ 1

        if result == 0:
            return -1
        else:
            return 1
