# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [1, -1, 3, 4, 5]

    print(a == b)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1, seq2 = [], []

        def dfs(node, first):
            if not node.left and not node.right:
                if first:
                    seq1.append(node.val)
                else:
                    seq2.append(node.val)

            if node.left:
                dfs(node.left, first)

            if node.right:
                dfs(node.right, first)

        dfs(root1, True)
        dfs(root2, False)

        return seq1 == seq2
