from typing import List

a = [1, 2, 3]
b = [3, 4, 5]

print(b - a)


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        return sum([abs(b - a) for (a, b) in zip(seats, students)])
