from typing import List

if __name__ == "__main__":
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print("the points are : ", points)
    # points.sort(key=)

    foo = lambda x, y: x + y
    # there is an implicit return of sorts
    print(foo(2, 2))
    points.sort(key=lambda element: (element[0], -1 * element[1]))
    print("the points are : ", points)


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = float("-inf")
        points.sort(key=lambda element: (element[0], element[1]))

        for index in range(0, len(points) - 1):
            ans = max(ans, points[index + 1][0] - points[index][0])

        return ans
