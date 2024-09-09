# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def helper(self, tree: Optional[TreeNode], subtree: Optional[TreeNode]):
        """
        this function will check if the tree is an exact copy of the subtree
        """

        if tree and subtree:
            # have to check
            if tree.val == subtree.val:
                return self.helper(tree.left, subtree.left) and self.helper(
                    tree.right, subtree.right
                )
            else:
                return False
        elif not subtree and not tree:
            # both none
            return True
        else:
            # one is empty and the other not empty
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if self.helper(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
