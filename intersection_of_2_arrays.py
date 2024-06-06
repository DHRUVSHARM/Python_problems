from typing import List


# more difficult but interesting way to do the same thing
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()

        i, j = 0, 0

        smaller, p_s, larger, p_l = (
            (nums1, nums1[0], nums2, nums2[0])
            if nums1[0] < nums2[0]
            else (nums2, nums2[0], nums1, nums1[0])
        )

        while i < len(smaller) and j < len(larger):
            p_s, p_l = smaller[i], larger[j]
            if smaller[i] < larger[j]:
                while i < len(smaller) and smaller[i] == p_s:
                    i += 1
            elif smaller[i] == larger[j]:
                result.append(smaller[i])
                while i < len(smaller) and smaller[i] == p_s:
                    i += 1
                while j < len(larger) and larger[j] == p_l:
                    j += 1
            else:
                while j < len(larger) and larger[j] == p_l:
                    j += 1

        return result
