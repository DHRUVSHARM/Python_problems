class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (1 << 32) & n == 0:
            mask, steps = 1, 32
            while steps:
                if mask ^ n == 0:
                    return True
                mask = mask << 1
                steps -= 1

        return False
