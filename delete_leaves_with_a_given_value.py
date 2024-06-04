# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# recursive solution
"""
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        def helper(curr, target):
            if curr.left:
                curr.left = helper(curr.left, target)
            if curr.right:
                curr.right = helper(curr.right, target)

            if not curr.left and not curr.right and curr.val == target:
                return None
            else:
                return curr

        return helper(root, target)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        visited = set()
        # the time we check if something is in visited , we analyze it if it has become a leaf node
        s = [root]
        parent = {root: None}

        while len(s):
            node = s.pop()
            if node in visited:
                if not node.left and not node.right:
                    if node.val == target:
                        p = parent[node]
                        if not p:
                            # root is deleted
                            return None
                        if p.left == node:
                            p.left = None
                        else:
                            p.right = None
            else:
                # unvisited
                visited.add(node)
                s.append(node)
                if node.left:
                    s.append(node.left)
                    parent[node.left] = node
                if node.right:
                    s.append(node.right)
                    parent[node.right] = node

        return root
