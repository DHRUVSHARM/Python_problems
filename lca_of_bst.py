# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we will use the same dfs solution as before with some changed to account for
        # the bst conditions

        def helper(root, p_val , q_val):
            node_found = None

            if root.val == p_val:
                node_found = p

            if root.val == q_val:
                node_found = q

            if node_found is not None:
                return node_found
            
            left_found , right_found = None , None
            
            # additionally we can leverage the values 

            
            if root.left and p_val < root.val and q_val < root.val:
                left_found = helper(root.left , p_val , q_val)

            elif root.right and p_val > root.val and q_val > root.val:
                right_found = helper(root.right , p_val , q_val)

            else:
                return root
            
            if left_found is not None:
                return left_found
            elif right_found is not None:
                return right_found
            else:
                return None

        return helper(root , p.val , q.val)