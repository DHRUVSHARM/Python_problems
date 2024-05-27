# interesting divide and conquer style problem
import math

if __name__ == '__main__':
    print(math.fmod(-4, 2))
    print(int(-5 / 2))
    print(5 // 2)


    def chop(n: int):
        if n == 1:
            print("n : ", n)
            return
        print(int(n / 2))
        chop(int(n / 2))


    chop(2147483647)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        return (self.myPow(x, int(n / 2)) ** 2) * self.myPow(x, int(math.fmod(n, 2)))
