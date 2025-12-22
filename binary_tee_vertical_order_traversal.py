# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q , result = collections.deque([(root , 0)]) , collections.defaultdict(list)

        while q and root:
            level_size = len(q)
            while level_size:
                node , vertical_level = q.popleft()
                result[vertical_level].append(node.val)
                if node.left:
                    q.append((node.left , vertical_level - 1))
                if node.right:
                    q.append((node.right , vertical_level + 1))
                level_size -= 1
        
        ans = []
        for k in sorted(result.keys()):
            ans.append(result[k])

        return ans

