# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        d, index, prev_even, prev_odd = collections.deque([root]), 0, float("-inf"), float("inf")

        while d:
            level_size = len(d)
            while level_size:
                node = d.popleft()
                element = node.val
                if index:
                    # odd row
                    if (element % 2) or prev_odd <= element:
                        return False
                    prev_odd = element
                else:
                    # even row
                    if  not (element % 2) or prev_even >= element:
                        return False
                    prev_even = element

                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)

                level_size -= 1

            # reset the level
            prev_even, prev_odd = float("-inf"), float("inf")
            index = index ^ 1

        return True