import collections


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # another interesting problem that combines bitmask with while loop dp
        dp = collections.defaultdict(int)
        dp[0] = 1
        
        ans = 0
        for index in range(1 , high + 1):
            dp[index] = (
                dp.get(index - zero , 0) + dp.get(index - one , 0)
            ) % (10 ** 9 + 7)
            if low <= index <= high:
                ans = (ans + dp[index]) % (10**9 + 7)
        return ans