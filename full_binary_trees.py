#  Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        t = TreeNode()
        dp = {1: [t], 3: [TreeNode(0, t, t)]}

        # we map the number of nodes to the list of roots

        def create_trees(l, r, element):
            # print("left , right : ", len(l), len(r))
            for l_node in l:
                for r_node in r:
                    new_node = TreeNode()
                    new_node.left = l_node
                    new_node.right = r_node
                    dp[element].append(new_node)

        for node in range(5, n + 1, 2):
            # so the way we wil work is that we will start from 1 on the left
            # and keep moving till we get 1 on the right
            dp[node] = []
            left_wt, right_wt = 1, node - 2
            while right_wt >= 1:
                create_trees(dp[left_wt], dp[right_wt], node)
                left_wt += 2
                right_wt -= 2

        """
        for key, val in dp.items():
            print(key, " ", len(val))
        """

        return dp[n]