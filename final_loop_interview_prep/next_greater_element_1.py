from typing import List

import collections
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for _ in range(len(nums1))]
        element_index_mapping = collections.defaultdict()

        # o nums1 
        for index, element in enumerate(nums1):
            element_index_mapping[element] = index
        
        # o nums2 
        # mono decreasing 
        s = []

        # all elements in nums2 are not in nums1 
        for element in nums2:
            while len(s) and s[-1] < element:
                frontier = s.pop()
                
                if frontier in element_index_mapping:
                    result[element_index_mapping[frontier]] = element
            
            # add the element 
            s.append(element)

        
        return result