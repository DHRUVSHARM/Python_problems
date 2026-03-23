# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Given the root of a binary tree,
return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


so we can return the max len
leaf node return 0



        max(lh , rh) + 1  max height at node, and ans = max(lans , rans , lh + rh + 2)
final use returned ans
"""


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            lh , rh , lans , rans = 0 , 0 , 0 , 0
            if node.left:
                lh , lans = dfs(node.left)

            if node.right:
                rh , rans = dfs(node.right)

            return max(rh , lh) + 1 , max(lans , rans , rh + lh)            


        _ , ans = dfs(root)
        return ans