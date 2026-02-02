# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(root , p_val , q_val):

            # ultimately we will find the lca here 
            node_found = None

            if root.val == p_val:
                node_found = p
            
            if root.val == q_val:
                node_found = q

            # if node is found means either, if in the remaining tree the node
            # is there then this is the lca , else if it something else in another tree
            # and lca is way upper still ok since no need to go through remaining tree

            if node_found is not None:
                return node_found

            # try to find the remaining in the 2 sides
            left_node_found , right_node_found = None , None
            if root.left:
                left_node_found = helper(root.left, p_val , q_val)

            if root.right:
                right_node_found = helper(root.right , p_val , q_val)
            
            if left_node_found is not None and right_node_found is not None:
                # found lca at this point 
                return root
            elif left_node_found is not None:
                return left_node_found
            elif right_node_found is not None:
                return right_node_found
            else:
                return None
            


        return helper(root , p.val , q.val)