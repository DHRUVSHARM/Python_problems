# Definition for a pair.
from typing import List

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = a[:]
    a[0], a[1] = a[1], a[0]
    print(a)
    print(b)


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


# insertion sort with intermediate steps (stable sort)
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        steps = []
        for i in range(0, len(pairs)):
            j = i - 1
            while j >= 0 and (pairs[j].key > pairs[j + 1].key):
                # print(i , " , " , j)
                pairs[j] , pairs[j + 1] = pairs[j+1] , pairs[j]
                j -= 1
            steps.append(pairs[:])

        return steps