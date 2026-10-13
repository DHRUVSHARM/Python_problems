from typing import List

"""
1 <= k <= nums.length <= 105
1 <= nums[i] <= 109


we have fixed number of 1 bits

using a 1 bit could be using from an existing number -= 1 locking it 
using a 1 bit could be also getting it from another number all 1 bits

if we take all the bits from a number it is like taking filling all zeroes from one number, until when you can , 
uf both are ones we use only the ones from the current number so we can always use, 
once the bit is used and is set it does not consume any more bits regardless of where the bit comes from 

100000
011110
111111

"""

import collections
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        index_set_count = collections.defaultdict(int)

        for element in nums:
            for shifts in range(0 , 32):
                index_set_count[shifts] += (0 if ((1 << shifts) & element) == 0 else 1) 

        # we have the number of set bits from 0 to 31 bit 
        # 31 is msb down to 0 lsb 
        # we need to select k numbers 

        ans = 0
        # print(index_set_count)
        # every element can start fresh from 0
        # also note it does not matter where we start a bit can never be used in any other position 
        # and also not that it is always benefitial to add as many set bits to each number 
        # since one bit can be set once and a number is alwasy 2**place index and so on it does not matter 
        # these are added once overall , so packing them all in one number will always be better
        # as it leaves more open spaces in subsequent numbers
        while k:
            element = 0
            for shifts in range(0 , 32):

                if index_set_count[shifts] > 0:
                    index_set_count[shifts] -= 1
                    element = (element | (1 << shifts))

            # print("element : " , element)
            ans += (element ** 2)
            k -= 1
        
        return ans % (10 ** 9 + 7)
