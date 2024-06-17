from math import sqrt


print(2**31)
print(int(sqrt(2**31)) + 1)


# so the first solution will run in O(sqrt(C)) , using 2 pointer method
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            if left**2 + right**2 == c:
                return True
            elif left**2 + right**2 < c:
                left += 1
            else:
                right -= 1

        return False
