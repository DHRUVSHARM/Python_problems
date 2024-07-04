# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        acc = 0

        while curr:
            if curr.val != 0:
                acc += curr.val
                curr.val = acc
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                curr.val = acc
                prev, curr = curr, curr.next
                acc = 0

        # detach the zero head
        temp = head
        head = head.next
        temp.next = None

        return head
