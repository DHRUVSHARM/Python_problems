from typing import List
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:      
        s = []

        for index , element in enumerate(nums):
            while s and element < s[-1] and (len(s) + (len(nums) - index) - 1) >= k:
                # earlier position and we can replace the element to make it 
                # more competetive and we need to have enough values
                s.pop() 
            s.append(element)   


        return s[:k]