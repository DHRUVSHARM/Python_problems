from typing import List


from typing import List


# imp problem that shows how to reduce space complexity
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we will have to cleverly mark rows and cols to be zeroed
        zero_row, m, n = -1, len(matrix), len(matrix[0])

        for i in range(0, m):
            for j in range(0, n):
                if i == 0:
                    if matrix[i][j] == 0:
                        zero_row = 0
                else:
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # print(zero_row)
        # we will have to mark zeroes on the fly, so that previous assignments do not
        # affect the final ans

        for i in range(1, m):
            for j in range(1, n):
                # using the first row , first column and the zero_row as the markers
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    # any mark leads to zero
                    matrix[i][j] = 0

        for j in range(1, n):
            # marking the 1st row based only on zero_row , leave the 0,0 for column marking
            # print("here")
            if zero_row == 0:
                matrix[0][j] = 0

        for i in range(1, m):
            # 1st column marking based on 0,0
            # print("here")
            if matrix[0][0] == 0:
                matrix[i][0] = 0

        matrix[0][0] = 0 if zero_row == 0 else matrix[0][0]
