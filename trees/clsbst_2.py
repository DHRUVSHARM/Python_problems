# Definition for a binary tree node.
from typing import List, Optional

"""

            4

                
        2       5



    1       3


Input: root = [4,2,5,1,3], target = 3.714286, k = 2

Output: [4,3]

# heap to keep the top k
# key by (diff, value)
# do logn 


3 4 5

     3.71 , 3.71
     3              4 


4 , 2 , 3

3.71    3.71
    3 4

    

"""

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # we have at least k nodes 

        q = collections.deque()

        # inorder 
        def dfs(node):
            if not node:
                return
            # print(q)
            dfs(node.left)
            # current node add
            q.append(node.val)
            if len(q) > k:
                if abs(q[-1] - target) <= abs(q[0] - target):
                    q.popleft()
                else:
                    q.pop()
            dfs(node.right)

        dfs(root)
        return list(q)