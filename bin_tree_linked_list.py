# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def helper(self, curr: Optional[ListNode], node: Optional[TreeNode]):

        if not curr:
            # we have reached the end of the path, so it means that we have done our job so return
            return True

        if not node or curr.val != node.val:
            # means that the tree is finished with ll not done yet or non match so no point continuing
            return False

        return self.helper(curr.next, node.left) or self.helper(curr.next, node.right)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        if not root:
            # no point comparing when there is an empty tree and a ll of atleast one node
            return False

        if self.helper(head, root):
            # means we found a possible path solution
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
