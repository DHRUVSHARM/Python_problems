# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        ans , nodes = 0 , collections.deque([root])

        def helper(arr):
            
            ans = 0

            real_indexes = {node.val : index for index , node in enumerate(arr)}
            sorted_arr = [node.val for node in arr]
            sorted_arr.sort()

            for index , node in enumerate(arr):
                real , sort_ele = node.val , sorted_arr[index]
                to_find_index = real_indexes[sort_ele]
                if to_find_index == index:
                    pass
                else:
                    ans += 1
                    real_indexes[sort_ele] , real_indexes[real] = real_indexes[real] , real_indexes[sort_ele]
                    arr[index].val , arr[to_find_index].val = arr[to_find_index].val , arr[index].val 
            
            return ans

        while nodes:
            level , level_nodes = len(nodes) , []

            while level:
                frontier = nodes.popleft()
                level_nodes.append(frontier)
                if frontier.left:
                    nodes.append(frontier.left)
                if frontier.right:
                    nodes.append(frontier.right)
                level -= 1
            
            # we have the level currently
            ans += helper(level_nodes)
        
        return ans

        