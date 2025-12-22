# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue , ans , level_count = collections.deque([(0 , root)]) , True , 0

        while queue:
            level_size , node_indices , start_index = len(queue) , [] , 2**level_count - 1

            while level_size:
                
                node_index , node = queue.popleft()
                node_indices.append(node_index)

                if node.left:
                    queue.append((node_index * 2 + 1 , node.left))
                if node.right:
                    queue.append((node_index * 2 + 2 , node.right))
                    
                level_size -= 1
            
            # print("start index : " , start_index)
            # print("node indices : " , node_indices)

            # at this point we have the current level, we check
            # if the child level has anything and if yes then we 
            # ensure that the current level should be full with size 2** level_count nodes
            # for CBT

            if len(queue) and len(node_indices) != (2**level_count):
                return False

            # ensure we start with start index and is a consistent sequence
            for index in range(0 , len(node_indices)):
                if index == 0: 
                    if node_indices[index] != start_index:
                        return False
                else:
                    if node_indices[index] - node_indices[index - 1] != 1:
                        return False
            
            level_count += 1

        return ans