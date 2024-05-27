from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        t_l, t_r, b_r, b_l = [0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]

        def rotate(tl, tr, br, bl):
            """
            rotates one square
            :return:
            """
            x, y = tl
            element = matrix[x][y]
            x, y = tr
            matrix[x][y], element = element, matrix[x][y]
            x, y = br
            matrix[x][y], element = element, matrix[x][y]
            x, y = bl
            matrix[x][y], element = element, matrix[x][y]
            x, y = tl
            matrix[x][y], element = element, matrix[x][y]

        while b_l[0] - t_l[0] + 1 > 1:

            width = t_r[1] - t_l[1]

            for i in range(0, width):
                rotate([t_l[0], t_l[1] + i], [t_r[0] + i, t_r[1]],
                       [b_r[0], b_r[1] - i], [b_l[0] - i, b_l[1]])

            t_l = [t_l[0] + 1, t_l[1] + 1]
            t_r = [t_r[0] + 1, t_r[1] - 1]
            b_r = [b_r[0] - 1, b_r[1] - 1]
            b_l = [b_l[0] - 1, b_l[1] + 1]

            print(t_l , t_r , b_r ,b_l)
