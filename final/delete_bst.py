# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def minValue(node):
            # guaranteed the node is not None 
            # return minVal
            curr = node
            while curr and curr.left:
                curr = curr.left
            
            return curr.val

        def helper(node , val):
            if not node:
                return node
            
            if node.val == val:
                if node.left and node.right:
                    # find the min value from the right side
                    min_val = minValue(node.right)    
                    # replace with current one to maintain ordering 
                    node.val = min_val
                    print(min_val)
                    # now call the helper again on the right side and remove the leaf node (least one)
                    # and attach to the right side
                    node.right = helper(node.right , min_val)
                else:
                    if not node.left:
                        return node.right
                    if not node.right:
                        return node.left
            else:
                if val < node.val:
                    node.left = helper(node.left , val)
                else:
                    node.right = helper(node.right , val)
            
            return node

        return helper(root , key)