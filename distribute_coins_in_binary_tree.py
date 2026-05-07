# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def helper(curr):
            if not curr.left and not curr.right:
                # leaf node base case , (#nodes , #coins)
                ans[0] += abs(curr.val - 1)
                return (1, curr.val)

            total_nodes, total_coins = 1, curr.val

            if curr.left:
                node_num, coins_num = helper(curr.left)
                # print(node_num , " , " , coins_num)
                total_nodes += node_num
                total_coins += coins_num

            if curr.right:
                node_num, coins_num = helper(curr.right)
                # print(node_num , " , " , coins_num)
                total_nodes += node_num
                total_coins += coins_num

            # print(total_coins , " , " , total_nodes)
            ans[0] += abs(total_coins - total_nodes)
            return (total_nodes, total_coins)

        helper(root)

        return ans[0]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        if not root:
            return self.res
        

        def helper(node):
            if node is None:
                return 0 , 0

            
            total_coins, total_size = node.val , 1
            if node.left:
                lc , lsize = helper(node.left)
                self.res += abs(lc - lsize)
                total_size += lsize
                total_coins += lc
            
            if node.right:
                rc, rsize = helper(node.right)
                self.res += abs(rc - rsize)
                total_size += rsize
                total_coins += rc

            return total_coins, total_size

        helper(root)
        return self.res

    
      
