# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(left , right , level):
            if not left and not right:
                return 
            
            if (level) % 2 != 0:
                left.val , right.val = right.val , left.val
            
            helper(left.left , right.right , level + 1)
            helper(left.right , right.left , level + 1)

        helper(root.left , root.right , 1)
        return root

"""
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = collections.deque([root])
        level_number = -1

        while nodes:
            level = len(nodes)
            level_number += 1

            reversed_nodes = [element.val for element in nodes]
            

            if level_number % 2 != 0:
                for element , reversed_element in zip(nodes , reversed(reversed_nodes)):
                    # print(" ( " ,  element.val , " , " , reversed_element.val , " ) " , end = " , ")
                    element.val = reversed_element
            # print("")

            while level:
                frontier = nodes.popleft()
                if frontier.left:
                    nodes.append(frontier.left)
                if frontier.right:
                    nodes.append(frontier.right)
                level -= 1
            
        return root
"""