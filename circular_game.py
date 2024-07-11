# n*k solution ..
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index, start, deleted = 0, 0, set()

        # every 
        while len(deleted) < n - 1:
            if index in deleted:
                index = (index + 1) % n
            else:
                index = (index + k - 1) % n



        ans = -1
        for index in range(0, n):
            if index not in deleted:
                ans = index + 1
                break

        return ans
"""


# linear constant space solution ..
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for step in range(2, n + 1):
            winner = (winner + k) % step

        return winner + 1
