from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        result = []
        i, j = -1, 0
        row = []

        while i < m and j < len(original):

            if j % n == 0:
                if i != -1:
                    result.append(row.copy())
                i += 1
                row = []

            # print(i , " , " , j)

            row.append(original[j])
            j += 1

        if j % n == 0:
            if i != -1:
                result.append(row.copy())
            i += 1
            row = []

        if i == m and j == len(original):
            return result
        else:
            return []
