from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        colors, neededTime = " " + colors, [float("inf")] + neededTime
        l, r = 0, 1

        while r < len(colors):
            # print(l , r)
            if colors[l] != colors[r]:
                # there is a mismatch , you do not need to do anything
                l = r
                r += 1
            else:
                if neededTime[r] < neededTime[l]:
                    # delete the element at r and move forward
                    ans += neededTime[r]
                    r += 1
                else:
                    # print("here")
                    ans += neededTime[l]
                    l = r
                    r += 1

        return ans