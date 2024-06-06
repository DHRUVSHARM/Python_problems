from typing import List

if __name__ == "__main__":
    points = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 3], [1, -1]]
    points.sort(key=lambda element: (element[0], -1 * element[1]))
    print(points)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        c_s, c_e, ans = points[0][0], points[0][1], 0

        for r in range(1, len(points)):
            s, e = points[r][0], points[r][1]
            if c_e >= s:
                c_e = min(c_e, e)
            else:
                ans += 1
                c_s = s
                c_e = e
        return ans + 1
