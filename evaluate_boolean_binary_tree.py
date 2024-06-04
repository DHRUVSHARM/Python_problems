# Definition for a binary tree node.
import collections
from typing import Optional

"""
Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        leaves = collections.defaultdict(bool)
        leaves[0] = False
        leaves[1] = True

        s = [root]

        while len(s) > 1 or s[-1].val not in leaves:
            if s[-1].val not in leaves:
                s.append(s[-1].left)
            else:
                # leaf node , we have a leaf node at the top
                if s[-2].val not in leaves:
                    # we need to move to the right
                    s.append(s[-2].right)
                else:
                    # we have both the leaves and we need to combine them
                    l_op = s.pop()
                    r_op = s.pop()
                    op = s.pop()
                    if op.val == 2:
                        # or
                        node = TreeNode(l_op.val or r_op.val)
                    else:
                        # and
                        node = TreeNode(l_op.val and r_op.val)

                    s.append(node)

        return True if s[-1].val else False
