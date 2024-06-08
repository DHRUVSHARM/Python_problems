import collections
from typing import List

print("here")
arr = [1, 1, 1, 1, 1]
# for traversal
for sub_size in range(0, len(arr)):
    for i in range(0, len(arr)):
        k = i + sub_size
        if k >= len(arr):
            break
        print(i, " , ", k)
    print("****************************")


# brute force n^3
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        dp = collections.defaultdict(int)
        # result = set()
        for sub_size in range(0, len(arr)):
            for i in range(0, len(arr)):
                k = i + sub_size
                if k < len(arr):
                    if sub_size == 0:
                        dp[(i, k)] = arr[i]
                    elif sub_size == 1:
                        dp[(i, k)] = arr[i] ^ arr[k]
                        if arr[i] == arr[k]:
                            ans += 1
                    else:
                        for j in range(i + 1, k + 1):
                            dp[(i, k)] = dp[(i, j - 1)] ^ dp[(j, k)]
                            # print(i , " , " , j , " , " , k)
                            # print(dp[(i , k)])

                            if dp[(i, j - 1)] == dp[(j, k)]:
                                # print("here")
                                ans += 1

                else:
                    break

        # print(result)
        return ans
"""


# again bf but cubic but in better way less memory
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(0, len(arr) - 1):
            a = 0
            for j in range(i + 1, len(arr)):
                a ^= arr[j - 1]
                b = 0
                for k in range(j, len(arr)):
                    b ^= arr[k]
                    if a == b:
                        ans += 1

        return ans
"""


# quadratic solution
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        for i in range(0, len(arr) - 1):
            curr_xor = arr[i]
            for j in range(i + 1, len(arr)):
                curr_xor ^= arr[j]
                if curr_xor == 0:
                    ans += j - i

        return ans
"""


# linear solution
# very smart solution , used in tiktok oa
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        prefix_sum = 0
        prev_occ = collections.defaultdict(int)
        prev_occ[0] = 1
        index_sum = collections.defaultdict(int)

        for index in range(0, len(arr)):
            prefix_sum ^= arr[index]

            ans += (prev_occ[prefix_sum] * index) - index_sum[prefix_sum]

            # print("prefix sum : " , prefix_sum)
            # print("ans : " , ans)

            prev_occ[prefix_sum] += 1
            index_sum[prefix_sum] += index + 1

        return ans
