from typing import List

"""
12345 // 123 = 100


1000 // 1   = 1000
1000 // 10  = 100
1000 // 100 = 10

max()

1 <= arr1[i], arr2[i] <= 108

arr1 =
[10]
arr2 =
[17, 11]

"""
from typing import List

"""
12345 // 123 = 100


1000 // 1   = 1000
1000 // 10  = 100
1000 // 100 = 10

max()

1 <= arr1[i], arr2[i] <= 108

arr1 =
[10]
arr2 =
[17, 11]

"""

class Solution:

    def find_len(self, n):
        digits = 0
        while n:
            digits += 1
            n = n // 10
        
        return digits

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # we can make a set of the second array 
        arr1_set = set()
        for element in arr1:
            while element:
                arr1_set.add(element)
                element = element // 10
        
        arr2_set = set()
        for element in arr2:
            while element:
                arr2_set.add(element)
                element = element // 10

        res = 0
        for element in arr1_set:
            if element in arr2_set:
                res = max(res, self.find_len(element))

        
        return res



