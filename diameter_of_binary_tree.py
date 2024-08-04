# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def helper(node):
            height, diameter = 0, 0

            if node.left:
                left_max_height = helper(node.left)
                diameter += left_max_height
                height = max(height, left_max_height)

            if node.right:
                right_max_height = helper(node.right)
                height = max(height, right_max_height)
                diameter += right_max_height

            ans[0] = max(ans[0], diameter)
            return height + 1

        helper(root)

        return ans[0]
