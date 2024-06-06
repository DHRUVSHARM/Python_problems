import collections
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(target) -> int:

            left, ans, freq = 0, 0, collections.defaultdict(int)
            for r in range(len(nums)):
                freq[nums[r]] += 1
                # print(freq)
                if len(freq.keys()) <= target:
                    ans += r - left + 1
                else:
                    while left <= r and len(freq.keys()) > target:
                        freq[nums[left]] -= 1
                        if not freq[nums[left]]:
                            freq.pop(nums[left])
                        left += 1
                    ans += r - left + 1
                # print("ans : " , ans)
            return ans

        return helper(k) - helper(k - 1)
