# Definition for a binary tree node.
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
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node, start, end):
            # print(start , " " , end)
            if not node:
                return 0
            if start <= node.val <= end:
                return dfs(node.left, start, end) + node.val + dfs(node.right, start, end)
            elif end < node.val:
                return dfs(node.left, start, end)
            else:
                return dfs(node.right, start, end)

        return dfs(root, low, high)
