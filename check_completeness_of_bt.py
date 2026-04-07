# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

        1
    3       3
3       _   3   _


            1
        2       3
    4     5    6   7
8     9  10 11 12 13 n n
"""


import collections
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q , level_size = collections.deque([root]) , 1

        seen_null = False 
        while len(q): 
            while level_size:
                node = q.popleft()

                if node and seen_null:
                    # seen a non null node after a null node 
                    return False

                if not node:
                    # track if null was seen 
                    seen_null = True
                else:
                    # non null node
                    q.append(node.left)
                    q.append(node.right)

                level_size -= 1
            

            level_size = len(q)

        
        return True