import collections
from typing import List

if __name__ == '__main__':
    nums = [1, 1, 1]
    freq = collections.Counter(nums)
    unique = []
    for num in nums:
        if freq[num] > 1:
            freq[num] -= 1
        else:
            unique.append(num)
    print(unique)


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_operations, left = len(nums), 0
        freq = collections.Counter(nums)
        unique = []
        for num in nums:
            if freq[num] > 1:
                freq[num] -= 1
            else:
                unique.append(num)
        unique.sort()
        n = len(nums)
        for r in range(0, len(unique) + 1):
            if r < len(unique) and (unique[left] <= unique[r] <= unique[left] + n - 1):
                # we can extend the window
                pass
            else:
                # we have to stop the window, and consider the next starting point
                min_operations = min(
                    min_operations,
                    n - (r - left)
                )
                left += 1

        return min_operations
