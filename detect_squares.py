from typing import List

if __name__ == '__main__':
    dp = {}
    dp.get(2, 1)
    print(dp)


class DetectSquares:
    __slots__ = "point_frequency"

    def __init__(self):
        self.point_frequency = {}

    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        if pt not in self.point_frequency:
            self.point_frequency[pt] = 0
        self.point_frequency[pt] += 1

    def count(self, point: List[int]) -> int:
        query_pt = tuple(point)
        qx, qy = query_pt
        result = 0
        # print(self.point_frequency)
        for a, b in self.point_frequency:
            # print("a , b : " , (a , b))
            if (qx, b) in self.point_frequency and (a, qy) in self.point_frequency:
                if abs(qx - a) == abs(qy - b) and (qx - a) != 0 and (qy - b) != 0:
                    result += (
                            1
                            * self.point_frequency.get((qx, b))
                            * self.point_frequency.get((a, qy))
                            * self.point_frequency.get((a, b))
                    )
        return result
