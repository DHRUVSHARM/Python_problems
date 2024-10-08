# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev, curr = head, head.next

        def gcd(a, b):
            while b > 0:
                a, b = b, a % b

            return a

        while curr:
            new_node = ListNode(gcd(prev.val, curr.val), curr)
            prev.next = new_node

            prev, curr = curr, curr.next

        return head
