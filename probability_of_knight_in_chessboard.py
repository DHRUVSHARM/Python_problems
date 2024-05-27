if __name__ == '__main__':
    pass


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # we need to find the probability that the knight will be able to stay on the board
        # there are 8 moves possible from each point
        moves = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
        dp = {}

        def calculate_probability(x: int, y: int, k: int) -> float:
            """
            calculates probability to stay with k moves remaining starting from
            point x , y
            :param x: x
            :param y: y
            :param k: moves
            :return:
            """
            if k == 0:
                return 1

            if (x, y, k) in dp:
                return dp[(x, y, k)]

            res = 0
            for move in moves:
                mx, my = move
                newx, newy = x + mx, y + my

                if 0 <= newx <= n - 1 and 0 <= newy <= n - 1:
                    res += calculate_probability(newx, newy, k - 1)

            dp[(x, y, k)] = res / 8
            return dp[(x, y, k)]

        return calculate_probability(row, column, k)
