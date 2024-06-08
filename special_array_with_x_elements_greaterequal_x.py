import collections
from typing import List

print("hello ....")
arr = [1, 1, 1, 2, 32, 4]
f = collections.Counter(arr)
print(f)
print(f[-1])


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        return -1


if __name__ == "main":
    print("hello ....")
    arr = [1, 1, 1, 2, 32, 4]
    f = collections.Counter(arr)
    print(f)
    print(f[-1])
