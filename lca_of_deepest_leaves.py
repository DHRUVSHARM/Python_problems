# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:

    def helper(self,  root: Optional[TreeNode]) -> tuple[Optional[TreeNode] , int]:
        if not root:
            return root
        
        left_root , left_height = self.helper(root.left) if root.left else (root.left , 0)
        right_root , right_height = self.helper(root.right) if root.right else (root.right , 0)

        if not left_root and not right_root:
            # leaf node
            return root , 1        

        # normal case, atleast one will have a non zero height
        if left_height == right_height:
            # we have multiple nodes with the deepest height that are in 
            # in the left and the right part and culminate at the node currently
            return root , left_height + 1
        else:
            if left_height > right_height:
                # deeper node resides in left subtree
                return left_root , left_height + 1
            else:
                # deeper node resides in right subtree
                return right_root , right_height + 1


    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca, deepest_node_height = self.helper(root)
        return lca
