# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import Optional
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root1 , root2):
            if not root1 and not root2:
                # base case 
                return None

            result = None
            if root1 and root2:
                # can merge
                result = TreeNode(root1.val + root2.val)
            elif root1:
                result = TreeNode(root1.val)
            else:
                result = TreeNode(root2.val)

            
            result.left = helper(root1.left if root1 else root1  , root2.left if root2 else root2)
            result.right = helper(root1.right if root1 else root1 , root2.right if root2 else root2)                

            return result
        
        ans = helper(root1 , root2)  
        return ans