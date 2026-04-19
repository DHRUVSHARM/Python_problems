"""

A pair of indices (i, j),
where 0 <= i < nums1.length 
and 0 <= j < nums2.length, 
is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Example 1:

Input: 
        i
nums1 = [55,30,5,4,2],
         j
nums2 = [100,20,10,10,5]


while i >= 0 and nums[i] <= nums2[j]:
    i -= 1

Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).


        i
nums1 = [25,25,25,25,25]
            j
nums2 = [30,29,19,5]

"""
from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int: 
        n , m , result = len(nums1) , len(nums2) , 0

        j = m - 1
        for i in range(n - 1 , -1 , -1):

            while j >= i and nums1[i] > nums2[j]:
                j -= 1
            
            if j >= i:
                result = max(result , j - i)

        return result