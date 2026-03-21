# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        curr = root
        while curr:
            if val < curr.val:
                # move left 
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                # move right
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right 

        return root
