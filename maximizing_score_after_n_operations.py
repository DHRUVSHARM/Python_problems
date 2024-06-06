# this is an important problem for bitwise operations and gcd builtin in Python
"""
x << y
Returns x with the bits shifted to the left by y places
(and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

x >> y
Returns x with the bits shifted to the right by y places.
This is the same as //'ing x by 2**y.

x & y
Does a "bitwise and". Each bit of the output is 1 if the
 corresponding bit of x AND of y is 1, otherwise it's 0.

x | y
Does a "bitwise or". Each bit of the output is 0 if the
corresponding bit of x AND of y is 0, otherwise it's 1.

~ x
Returns the complement of x - the number you get by
switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding
bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
Just remember about that infinite series of 1 bits in a negative number, and these should all make sense.
"""
import math
from typing import List

if __name__ == "__main__":
    print(math.gcd(7, 67))


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        dp = {}

        def dfs(mask, operation_number):
            """
            state in this function refers to the number not available for selection from
            nums
            :param operation_number: number of operation , 1 indexed
            :param mask: state representative
            :return: final o/p
            """

            if mask in dp:
                return dp[mask]

            ans, n = 0, len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    # selecting i and j numbers , check if they are not used before
                    if (mask & (1 << (n - i - 1))) | (mask & (1 << (n - j - 1))):
                        # atleast one is occupied, pair cannot be used
                        continue
                    # none is occupied
                    new_mask = mask | (1 << (n - i - 1)) | (1 << (n - j - 1))
                    ans = max(
                        ans,
                        operation_number * math.gcd(nums[i], nums[j])
                        + dfs(new_mask, operation_number + 1),
                    )

            dp[mask] = ans
            return dp[mask]

        return dfs(0, 1)
