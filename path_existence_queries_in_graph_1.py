from typing import List
from bisect import bisect_right

from typing import List
from bisect import bisect_right


# approach 1 bisect 

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # first we need to store components 
        # [l , r] start and end for the components

        left , right = 0 , 0
        components = []


        while right < len(nums):
            if nums[right] == nums[left] or (nums[right] - nums[right - 1] <= maxDiff):    
                right += 1
            else:
                components.append([left , right - 1])
                left = right
        
        components.append([left, right - 1])
        
        # l   r
        # [2 , 5 , 6, 8]
        # [[0 , 0] , [1 , 2] , [3 , 3]]

        # need to think about 
        # this is comparing element with the target
        # <= > bisect right if compare with end 

        """
        
        <=                |          >
        element <= target | elements > target
        
        last start <= target
        """

        # comp end
        # print(components)
        comp_end = [s for s , _ in components]
        ans = []

        for u , v in queries:
            if bisect_right(comp_end , u) - 1 == bisect_right(comp_end , v) - 1:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # first we need to store components 
        # [l , r] start and end for the components

        left , right = 0 , 0
        components = []


        while right < len(nums):
            if nums[right] == nums[left] or (nums[right] - nums[right - 1] <= maxDiff):    
                right += 1
            else:
                components.append([left , right - 1])
                left = right
        
        components.append([left, right - 1])
        
        # l   r
        # [2 , 5 , 6, 8]
        # [[0 , 0] , [1 , 2] , [3 , 3]]

        # create a mapping from node to component index
        node_comp = {}
        for index, element in enumerate(components):
            for c in element:
                node_comp[c] = index
        
        ans = []
        for u , v in queries:
            if node_comp[u] == node_comp[v]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans


# dict based solution 
class Solution1:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # first we need to store components 
        # [l , r] start and end for the components

        left , right = 0 , 0
        components = []


        while right < len(nums):
            if nums[right] == nums[left] or (nums[right] - nums[right - 1] <= maxDiff):    
                right += 1
            else:
                components.append([left , right - 1])
                left = right
            
        
        components.append([left, right - 1])
        
        # l   r
        # [2 , 5 , 6, 8]
        # [[0 , 0] , [1 , 2] , [3 , 3]]

        # create a mapping from node to component index
        node_comp = {}
        for index, element in enumerate(components):
            for c in range(element[0] , element[1] + 1):
                node_comp[c] = index
        
        # print(node_comp)
        # print(components)

        ans = []
        for u , v in queries:
            if node_comp[u] == node_comp[v]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
