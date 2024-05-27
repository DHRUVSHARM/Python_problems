"""
we will use hashset in this problem
"""
from typing import List

if __name__ == '__main__':
    check = set()
    arr = [1, 2, 3, 1, 4]
    # duplicates are automatically ignored when adding to a set
    for element in arr:
        check.add(element)
    print(check)

    ans = [[], []]
    ans[0].append(1)
    print(ans)

    arr1 = [1 , 2 , 3]
    arr2 = [2 ,4,5 ,4 , 3]

    for x , y in zip(arr1 , arr2):
        print(x , y)

"""
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)

        print(set1)
        print(set2)

        ans1, ans2 = set(), set()
        for element in set1:
            if element not in set2:
                ans1.add(element)

        for element in set2:
            if element not in set1:
                ans2.add(element)

        return [list(ans1), list(ans2)]
