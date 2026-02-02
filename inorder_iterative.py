# Definition for a binary tree node.
from typing import List , Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



# s = [1 , 2 , 3]
# result = []

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ITERATIVE SOLUTION
        s , result = [root] , []
        # 4
        # [1 , 2 ]
        while s:
            # push till last where no left found
            if s and s[-1] is None:
                # means previous has completed the left subtree and has to be popped to consider right  
                s.pop()
            else:
                while s and s[-1].left:
                    s.append(s[-1].left)

            # in the stack means left has been considered for the top node at this point
            # so we add it and push it's right child
            if s:  
                node = s.pop()
                result.append(node.val)

                # push the right part
                s.append(node.right)

        return result
        