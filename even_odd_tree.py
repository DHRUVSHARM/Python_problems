# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


level order traversal 
even : odd values for all incr strictly 
odd : even values strictly decr 
0
1
2
3


"""

import collections
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        level_size , level_count  = len(q) , 0

        while len(q):

            is_odd = (level_count % 2) != 0 # true if level is odd 
            element = float("inf") if is_odd else float("-inf")

            while level_size:
                # iterate through the current level 
                node = q.popleft()
            
                if is_odd:
                    if element <= node.val or node.val % 2 != 0:
                        return False
                else:
                    if element >= node.val or node.val % 2 == 0:
                        return False

                element = node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level_size -= 1
            
            # store data for the next level
            level_size = len(q)
            level_count += 1

            

        return True