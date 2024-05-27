import math


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask, ans = 1, 0
        for i in range(0, 32):
            # first we will check if the ith bit is set or not
            if mask & left:
                # here means we have a one , we need to see if it gets to 0
                steps_to_zero = (mask << 1) - (((mask << 1) - 1) & left)
                if left + steps_to_zero > right:
                    # we cannot get to 0 , so this has to be 1
                    ans = ans | mask

            mask = mask << 1

        return ans
