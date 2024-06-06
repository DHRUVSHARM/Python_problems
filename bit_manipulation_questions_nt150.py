import math
from typing import List

if __name__ == "__main__":
    print(math.log2(1))
    print(((2 & 3) << 1) & (2**31 - 1))
    element = 2**31 - 1
    print((1 << 31) & element)
    print((1 << 30) & element)
    element = -(2**31)
    print((1 << 31) & element)
    print((1 << 32) & element)

    print(" " + bin(2**31 - 1))
    # print(" " + bin(2**31))
    print(bin(-(2**31)))
    print(" " + bin(~(-(2**31))))
    lower_limit = -(2**31)
    upper_limit = 2**31 - 1

    print(~lower_limit == upper_limit)
    print("reversing")
    rev = 0
    x = -123
    # print(math.fmod(-123 , 10))
    # print(-123 // 10)
    while x:
        digit = int((math.fmod(x, 10)))
        rev = 10 * rev + digit
        print(rev)
        x = int(x / 10)
    print(rev)

# single number
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for element in nums:
            res = res ^ element
        return res
"""
# n & n-1 gives the lsb 1 bit removed value except when n was originally 0
# number of 1 bits
# The input must be a binary string of length 32.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:

        
        one_bits, mask = 0, 1
        for i in range(0, 32):
            if n & mask:
                one_bits += 1
            mask = mask << 1
        return one_bits
        
        # this is the better and more advanced solution
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
"""
# my very nice interesting dp solution
# idea : before every number , say like 00000(1st one bit)000(next 1 bit)...(0/1)
# we get 00000(1st one bit) power of 2 (with single pne bit) so we can do dp solution
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        # dp[0] = 0 means no 1 bits for 0

        for index in range(1, n + 1):
            dp[index] = 1 + dp[index & (index - 1)]
        return dp
"""
# highly optimized solution
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans_mask = 0
        base = 2**31

        while n:
            power = int(math.log2(n ^ (n & (n-1))))
            print(power)
            ans_mask = ans_mask | (base >> power)
            n = n & (n-1)

        return ans_mask
"""
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mask = 0
        for element in nums:
            mask = mask ^ element
        for number in range(0 , len(nums) + 1):
            mask = mask ^ number
        return mask
"""

# very imp problem to understand how to restrict and work with 32 bits in python
# like in java or in c++
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # we can use a mask to add and get carry separately
        mask = 2 ** 32 - 1
        # mask is 000...01111..1 (32 1's at the end)
        parity_bit_checker = 1 << 31
        # to check the 31st bit , if set then number is negative
        # else positive

        a = a & mask
        b = b & mask

        sum, carry = (a ^ b) & mask, ((a & b) << 1) & mask
        while carry:
            # print("sum , carry : " , sum , carry)
            sum, carry = (sum ^ carry) & mask, ((sum & carry) << 1) & mask

        # in the above loop since there are 32 1's everything happens
        # normaly at the end answer can be negative (32 nd 1 set)
        # or not. now if negative we want to make all the leading
        # zeroes one of sum after bit at 31 index of sum
        return sum if not (parity_bit_checker & sum) else ~(sum ^ mask)
"""


class Solution:
    def reverse(self, x: int) -> int:
        lower_limit = -(2**31)
        upper_limit = 2**31 - 1
        rev = 0
        while x:
            digit = int((math.fmod(x, 10)))
            # to ignore -ve sign and do mod
            rev = 10 * rev + digit
            if lower_limit <= rev <= upper_limit:
                pass
            else:
                return 0
            # print(rev)
            # to round towards 0
            x = int(x / 10)

        return rev
