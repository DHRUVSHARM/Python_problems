from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        start_vals = [nums[0], nums[1], nums[2], nums[3]]
        start_vals.sort(reverse=True)
        ans = 0
        max1, max2, min1, min2 = start_vals

        ans = max(ans, (max1 * max2) - (min1 * min2))

        # print(max1, max2, min1, min2)

        for index in range(4, len(nums)):
            if nums[index] >= max1:
                max2, max1 = max1, nums[index]
            elif max2 <= nums[index] < max1:
                max2 = nums[index]
            elif nums[index] <= min2:
                min2, min1 = nums[index], min2
            elif min2 < nums[index] <= min1:
                min1 = nums[index]

            ans = max(ans, (max1 * max2) - (min1 * min2))

            # print(max1, max2, min1, min2)

        return ans
