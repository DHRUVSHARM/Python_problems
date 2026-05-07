# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.
"""
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left is None and root.right is None:
                return root
        
        new_root = [None]
        def helper(node):
            if not node.left and not node.right:
                return node
            
            if node.left:
                new_lchild = node.left
                node.left = None
                new_lchild = helper(new_lchild)
                if new_root[0] is None:
                    new_root[0] = new_lchild
                
                new_lchild.right = node
            
                # right will have sibling
                new_rchild = helper(node.right) if node.right is not None else node.right
                new_lchild.left = new_rchild

                node.right = None
            
            return node

        helper(root)
        return new_root[0]