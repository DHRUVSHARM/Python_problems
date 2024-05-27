from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        base = [1]

        while rowIndex:
            new_row = [0 for _ in range(len(base) + 1)]
            for index, value in enumerate(base):
                new_row[index] += value
                new_row[index + 1] += value

            base = new_row
            # print(base)
            rowIndex -= 1

        return base

