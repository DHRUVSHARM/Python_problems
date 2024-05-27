from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1
        while even < odd:
            # print("even : " , even , " , " , "odd : " , odd)
            if nums[even] % 2 != 0 and nums[odd] % 2 == 0:
                # print("here 0")
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 1
                odd -= 1
            elif nums[even] % 2 == 0 and nums[odd] % 2 != 0:
                # print("here 1")
                even += 1
                odd -= 1
            elif nums[even] % 2 != 0:
                # print("here 2")
                odd -= 1
            else:
                # print("here 3")
                even += 1

        return nums
