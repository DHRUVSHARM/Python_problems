# Definition for a binary tree node.


"""
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


root to leaf (requirement)


        bottom up solution is wrong

        we need to keep track of the current path and move and make condiiton 
    
    """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curr_sum):
            if not node:
                return False
            
            if not node.left and not node.right:
                return curr_sum == targetSum
            
            # sort of a path pruning
            if node.left:
                left_result = dfs(node.left, curr_sum + node.left.val)
                if left_result:
                    return True

            if node.right:
                right_result = dfs(node.right , curr_sum + node.right.val)
                if right_result:
                    return True
            
            return False


        if not root:
            return False

        return dfs(root, root.val)
