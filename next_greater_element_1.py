from typing import List

"""
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.


need to find for the element in nums1, the index of next greater in nums[2] , they all exist and unique
"""

from typing import List

"""
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.


need to find for the element in nums1, the index of next greater in nums[2] , they all exist and unique
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        s = []
        lookup = {}
        for index, element in enumerate(nums1):
            lookup[element] = index

        # print(lookup)

        for element in nums2:

            while len(s) and element > s[-1]:
                # element is the next greater
                ans[lookup[s[-1]]] = element
                s.pop()
            
            # only add if the element is in the nums1
            if element in lookup:
                s.append(element)
            
            # print(s)

        return ans