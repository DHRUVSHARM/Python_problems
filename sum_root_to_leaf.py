# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def helper(node , acc):
            
            acc += node.val
            
            if not node.left and not node.right:
                return acc
            
            if node.left:
                left_sub_ans = helper(node.left , 10 * acc)

            if node.right:
                right_sub_ans = helper(node.right , 10 * acc)
            
            return left_sub_ans + right_sub_ans

        return helper(root , 0)