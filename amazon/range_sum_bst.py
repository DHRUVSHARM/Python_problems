# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # to store by reference 
        ans = [0]

        # represents a state where [lb , ub] is the potential values in that part of tree
        def helper(root , lb , ub , low , high):
            
            if lb > ub:
                return 

            if high < lb or low > ub:
                return
            
            # otherwise what this implies is that you are in the range 
            # iff the value itself is in the range
            # the decision to travel is different from the one to include does not guarantee it
            if  low <= root.val <= high:     
                ans[0] += root.val

            if root.left:
                helper(root.left  , lb , root.val - 1 , low , high)

            if root.right:
                helper(root.right  , root.val + 1 , ub , low , high)
                
        
        # we know that the range is [1 , 10**5]
        helper(root, 1 , 10**5 , low , high)

        return ans[0]