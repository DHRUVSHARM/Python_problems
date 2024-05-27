class Solution:
    def countOrders(self, n: int) -> int:
        # combinations based question
        result, m = 1, 10 ** 9 + 7

        while n:
            result = (result * (((2 * n) * (2*n - 1)) // 2)) % m
            n -= 1

        return result
