"""
n = 1 , [0] -> 2^0
[0 , 1] -> 2^1
[0 , 1 , 1 , 0] > 2^2
[0 , 1  , 1 ,0 , 1 ,0 , 0 , 1]

"""

if __name__ == '__main__':
    x = 2
    print(x >> 1)


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        left, right, curr = 1, 2 ** (n - 1), 0

        while right != left:
            mid = (left + right) // 2
            if k <= mid:
                # move to the left , the curr moves to the left from top
                right = mid
            else:
                # move to the right , the curr move to the right from the top
                curr = 0 if curr else 1
                left = mid + 1

        return curr