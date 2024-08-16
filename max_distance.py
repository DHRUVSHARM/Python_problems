from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0

        curr_min, curr_max = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            for j in range(0, len(arrays[i])):
                # print("curr min and max : " , curr_min , " " , curr_max )

                ans = max(
                    ans,
                    abs(arrays[i][-1] - curr_min),
                    abs(arrays[i][0] - curr_max),
                )

            curr_min = min(curr_min, arrays[i][0])
            curr_max = max(curr_max, arrays[i][-1])

        return ans
