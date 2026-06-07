# Definition for a binary tree node.
from typing import List, Optional

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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # values are unique in our bt 
        # map value to the node reference
        # keep node value -> parent value for the final root determination since the tree is valid 
        
        node_ref_map = {}
        parent = {}


        for par, child, isleft in descriptions:
            if par not in node_ref_map:
                # create and store lookup ref
                node_ref_map[par] = TreeNode(par)
                parent[par] = par # itself for now 
            
            if child not in node_ref_map:
                node_ref_map[child] = TreeNode(child)
            
            # connection to be made even if one is there
            if isleft == 1:
                node_ref_map[par].left = node_ref_map[child]
            else:
                node_ref_map[par].right = node_ref_map[child]

            parent[child] = par

        # we can take any value 
        root = list(node_ref_map.keys())[0]

        while root != parent[root]:
            root = parent[root]
        
        return node_ref_map[root]
        
                
