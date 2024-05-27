import collections
from typing import List


def kadane(arr):
    """
    kadane algorithm to find the maximum subarray sum with atleast one element
    :param arr: ip
    :return: none
    """
    maximal_subarr_sum, maximal_window, left, curr_sum = float("-inf"), (-1, -1), 0, 0
    for r in range(0, len(arr)):
        curr_sum += arr[r]
        if curr_sum > maximal_subarr_sum:
            maximal_window, maximal_subarr_sum = (left, r), curr_sum

        while left <= r and curr_sum < 0:
            # in this algo this will always bring left to r and close the window
            curr_sum -= arr[left]
            left += 1

    print("the maximal subarray sum is : ", maximal_subarr_sum, " the window is : ", maximal_window)


if __name__ == '__main__':
    a = [4, -1, 2, -7, 3, 4]
    kadane(a)

# kadane based problems
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # we need to keep track of both the maximal and the minimal sum
        curr_sum_max, curr_sum_min, maximal_sum, minimal_sum, left_min = 0, 0, float("-inf"), float("inf"), 0

        for r in range(0, len(nums)):
            curr_sum_max += nums[r]
            curr_sum_min += nums[r]

            # print(curr_sum_max , " " , curr_sum_min)

            maximal_sum = max(maximal_sum, curr_sum_max)

            # we do not want to include solutions where all the elements are unused
            if r - left_min + 1 < len(nums):
                minimal_sum = min(minimal_sum, curr_sum_min)

            # print(maximal_sum , " --- " , minimal_sum)

            if curr_sum_max < 0:
                curr_sum_max = 0

            if curr_sum_min > 0:
                curr_sum_min = 0
                left_min = r + 1

        return max(maximal_sum, sum(nums) - minimal_sum)
"""

"""
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maximal_size, left, sign = 1, 0, None
        for r in range(1, len(arr)):
            if r - left + 1 == 2:
                if arr[r] == arr[left]:
                    left = r
                elif arr[r] > arr[r - 1]:
                    sign = ">"
                else:
                    sign = "<"
                print(left, " -- ", r)
                maximal_size = max(maximal_size, r - left + 1)
            else:
                if ((arr[r] > arr[r - 1]) and sign == "<") or ((arr[r] < arr[r - 1]) and sign == ">"):
                    print(left, " ", r)
                    maximal_size = max(maximal_size, r - left + 1)
                    if arr[r] > arr[r - 1]:
                        sign = ">"
                    elif arr[r] < arr[r - 1]:
                        sign = "<"
                elif arr[r - 1] == arr[r]:
                    left = r
                else:
                    left = r - 1

        return maximal_size
"""

# sliding window fixed size based problems
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        frequency, left, result = collections.defaultdict(int), 0, False

        for r in range(0, len(nums)):
            frequency[nums[r]] += 1

            if frequency[nums[r]] > 1:
                # print(left , " , " , r)
                result = True
                break

            if r - left >= k:
                frequency[nums[left]] -= 1
                left += 1

        return result
"""

"""
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count, left, window_sum = 0, 0, 0

        for r in range(0, len(arr)):
            window_sum += arr[r]

            if r - left + 1 == k:

                if (window_sum / (r - left + 1)) >= threshold:
                    # print((window_sum / (r - left + 1)))
                    count += 1

                window_sum -= arr[left]
                left += 1

        return count
"""

# sliding window variable size
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimal_size, window_sum, left = float("inf"), 0, 0

        for r in range(0, len(nums)):
            window_sum += nums[r]

            while left <= r and window_sum >= target:
                minimal_size = min(minimal_size, r - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if minimal_size == float("inf") else minimal_size
"""

# two pointers
# nums = [0,0,1,1,1,2,2,3,3,4]
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, k = 0, 0

        for right in range(1, len(nums)):
            # print("left : " , left , " " , "right " , right , "k : " , k)
            if nums[left] == nums[right]:
                pass
            else:
                # new element
                k += 1
                nums[k] = nums[right]
                left = right
                # print(nums)

        return k + 1
"""

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, k = 0, 0
        for r in range(0, len(nums)):
            if nums[left] == nums[r]:
                if r - left + 1 <= 2:
                    nums[k] = nums[r]
                    k += 1
            else:
                nums[k] = nums[r]
                k += 1
                left = r

        return k
"""