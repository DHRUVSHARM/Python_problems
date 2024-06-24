from typing import List

# very imp sliding window with 3 pointer problem


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, mid, ans, odd_count = 0, 0, 0, 0

        for r in range(0, len(nums)):
            odd_count += 1 if (nums[r] % 2 != 0) else 0

            if odd_count > k:
                mid += 1
                left = mid
                odd_count -= 1

            if odd_count == k:
                while nums[mid] % 2 == 0:
                    mid += 1
                # found the first odd

                ans += mid - left + 1
                # print(left , " , " , mid , " , " , r)
                # print("index = " , r , " , " , "ans : " , ans)

        return ans
