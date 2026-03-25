# Definition for a binary tree node.

"""

A path in a binary tree is 

a sequence of nodes where 

each pair of adjacent nodes 

in the sequence has an edge connecting them. 

A node can only appear in the sequence at most once. 

Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


from a leaf node it is probably the value itself, even if negative since zero nodes is not alllowed
at a point we have the following 
    the max path root to leaf can be empty from left
    same can be empty from the right 
    we must always include the current node to keep the non empty constraint 

    1) so we get max path with atleast the current node , find the max from what was sent up 
    2) to send up we can include or exclude the current one and return the max 

    the base cases have to be handled correctly
        for leaf node:
            return the lead node val, max(current node val  , 0)


"""


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
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            # for ease of programming we can handle the null node cases as a base case as well
            if not node:
                return float("-inf") , 0 # cannot select, and always exclude

            if not node.left and not node.right:
                return node.val , max(node.val , 0)

     
            
            left_result , left_val = dfs(node.left)
            right_result , right_val = dfs(node.right)

            return max(left_result , right_result , left_val + node.val + right_val) , max(node.val + max(left_val , right_val) , 0)


        result, _ = dfs(root)
        return result