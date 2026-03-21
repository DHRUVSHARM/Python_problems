# Definition for a binary tree node.
"""
Docstring for wy_practice.bst_iterator

    7
 3     15 
      9  20

      
s = [20  ]
if curr null then pop
check the left child if null, then pop and put right child as curr

"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root  # represents the current state of the iterator 
        self.s = []
        # [7 , 3] c = null

    def next(self) -> int:
        # we return the current element and move to the next 
        # we can push and move to the left most point 
        while self.curr:
            self.s.append(self.curr)
            self.curr = self.curr.left
         # [  ] c = none

        value = None
        if self.s:
            self.curr = self.s.pop()
            value = self.curr.val
            self.curr = self.curr.right
        else:
            raise Exception("invalid next call")

        return value


    def hasNext(self) -> bool:
        # check to see if the current state does not represent empty 
        if self.s or self.curr:
            return True
        else:
            return False  


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()