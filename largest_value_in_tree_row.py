# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        def bfs():
            q = collections.deque([root])

            while len(q):
                level_max, level_length = float("-inf"), len(q)

                while level_length:
                    frontier = q.popleft()
                    if frontier.left:
                        q.append(frontier.left)
                    if frontier.right:
                        q.append(frontier.right)
                    level_max = max(level_max, frontier.val)
                    level_length -= 1

                result.append(level_max)

        bfs()

        return result
