from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        very interesting and perfect example of loop invariant style use of bs
        :param arr: mountain array
        :return: peak index
        """

        # the invariant is arr[ l ... mid ... r ] , base is 3 length size
        l, r, mid = 0, len(arr) - 1, (len(arr) - 1) // 2

        while not (arr[mid - 1] < arr[mid] > arr[mid + 1]):
            if arr[mid] < arr[mid + 1]:
                # peak is on the right side of the array
                l = mid
            elif arr[mid - 1] > arr[mid]:
                # peak is on the left side
                r = mid
            mid = (l + r) // 2

        return mid
