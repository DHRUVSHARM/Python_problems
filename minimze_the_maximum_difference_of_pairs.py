from typing import List


# interesting binary search based problem
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        nums.sort()

        def check(maximum_difference):
            # check if we can get p pairs where absolute diff is <= max_diff
            # this is a greedy algorithm
            pairs, index = 0, 0
            while index < len(nums) - 1:
                if abs(nums[index] - nums[index + 1]) <= maximum_difference:
                    pairs += 1
                    index += 2
                else:
                    index += 1
            return pairs >= p

        l, r = -1, 10 ** 9 + 1

        while l + 1 < r:
            mid = l + int((r -l) / 2)
            if check(mid):
                r = mid
            else:
                l = mid

        return r
