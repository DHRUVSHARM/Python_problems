from typing import List

print(ord("3") - ord("0"))


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # we will solve this using scratch with mergesort

        def compare(val1, val2):
            curr_val1, curr_val2 = 0, 0

            if val1 == 0:
                curr_val1 = mapping[val1]

            tens = 1
            while val1:
                curr_val1 += tens * mapping[(val1 % 10)]
                tens *= 100
                val1 //= 10

            if val2 == 0:
                curr_val2 = mapping[val2]

            tens = 1
            while val2:
                curr_val2 += tens * mapping[(val2 % 10)]
                tens *= 100
                val2 //= 10

            return True if curr_val1 <= curr_val2 else False

        def helper(left, right):
            if right - left + 1 == 1:
                return [nums[left]]

            mid = (left + right) // 2

            left_arr = helper(left, mid)
            right_arr = helper(mid + 1, right)

            result = []
            i, j = 0, 0

            while i < len(left_arr) and j < len(right_arr):
                if compare(left_arr[i], right_arr[j]):
                    result.append(left_arr[i])
                    i += 1
                else:
                    result.append(right_arr[j])
                    j += 1

            while i < len(left_arr):
                result.append(left_arr[i])
                i += 1

            while j < len(right_arr):
                result.append(right_arr[j])
                j += 1

            return result

        ans = helper(0, len(nums) - 1)

        return ans
