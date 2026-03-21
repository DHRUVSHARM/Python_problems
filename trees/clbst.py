# Definition for a binary tree node.
from typing import Optional

"""
Given the root of a binary search tree 
and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.


        4
    2       5
1       3

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return 0
        
        result = [(root.val , abs(target - root.val))]

        def dfs(node):
            if not node:
                return
            
            # consider current node
            diff = abs(node.val - target)
            if diff <= result[0][1]:
                result[0] = (node.val , diff)
            
            # move to the closer value, lesser if possible
            if target <= node.val:
                # move left, smaller
                dfs(node.left)
            else:
                # move right , try to get from there
                dfs(node.right)


        dfs(root)
        return result[0][0]
