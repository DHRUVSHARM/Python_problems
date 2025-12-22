# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        level_sum = collections.defaultdict(int)
        def dfs_level_sum(node , level):
            level_sum[level] += node.val
            if node.left:
                dfs_level_sum(node.left , level + 1)
            if node.right:
                dfs_level_sum(node.right , level + 1)

        dfs_level_sum(root , 0)

        def dfs_modify(node , level):
            if not node.left and not node.right:
                # leaf node
                return    
            else:
                node_sum = 0
                if node.left:
                    node_sum += node.left.val
                if node.right:
                    node_sum += node.right.val
                
                node_sum = level_sum[level + 1] - node_sum
                if node.left:
                    node.left.val = node_sum
                    dfs_modify(node.left , level + 1)
                if node.right:
                    node.right.val = node_sum
                    dfs_modify(node.right , level + 1)
                
        
        dfs_modify(root , 0)
        root.val = 0
        return root
