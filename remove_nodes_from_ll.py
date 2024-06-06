# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(curr):
            if not curr or not curr.next:
                return curr
            tmp = helper(curr.next)
            if curr.val >= tmp.val:
                # keep the node
                curr.next = tmp
                return curr
            else:
                # remove the node
                curr.next = None
                return tmp

        return helper(head)
