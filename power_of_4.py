from math import log


def f(a, b):
    return (b - a + 1) * a + (b - a) * (b - a + 1) // 2


def g(i, j, k):
    return f(i, j) + f(k, j - 1)


if __name__ == "__main__":
    x = 1.4
    print(x % 1)
    print(log(4, 4) % 1 == 0)
    # nice way to check if a number is properly divisible

    i, j, k = 0, 5, -1
    ans = ((j * (j + 1) / 2) - ((i - 1) * i / 2)) + (
        (j * (j - 1) / 2) - ((k + 1) * k / 2)
    )
    print(ans)

    print(g(-5, -1, -3))


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        return (n % 4 == 0) and self.isPowerOfFour(n // 4)
