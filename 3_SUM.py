from typing import List

if __name__ == "__main__":
    for i in range(0, 0):
        print("in loop !!!")


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # print(nums)

        def twoSum(first_element, l, r):
            target = -1 * first_element
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([frontier, nums[l], nums[r]])
                    left_element = nums[l]
                    while l < len(nums) and nums[l] == left_element:
                        l += 1

                    right_element = nums[r]
                    while r >= 0 and nums[r] == right_element:
                        r -= 1

                elif nums[l] + nums[r] < target:
                    left_element = nums[l]
                    while l < len(nums) and nums[l] == left_element:
                        l += 1
                else:
                    right_element = nums[r]
                    while r >= 0 and nums[r] == right_element:
                        r -= 1

        i = 0
        while i < len(nums) - 2:
            frontier = nums[i]
            twoSum(frontier, i + 1, len(nums) - 1)
            while i < len(nums) and nums[i] == frontier:
                i += 1

        return result
