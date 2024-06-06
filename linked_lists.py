# collection of questions on linked lists
from typing import Optional

if __name__ == "__main__":
    pass

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # first we will use f , s algo to detect a cycle
        slow, fast = head, head

        while fast.next and fast.next.next:
            # both have to be not null
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not fast.next or not fast.next.next:
            # if anyone is null we are in , short circuit if first statement is true
            return None

        # we have a cycle
        cycle_head = head
        while cycle_head != slow:
            cycle_head = cycle_head.next
            slow = slow.next

        return cycle_head
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse_LL(node: ListNode):
            # we pass in the head first in this function, we return finally the tail of the
            # reversed list, so it is better that we fix the head before the list to be
            # reversed is passed
            if node is None or node.next is None:
                return node

            reverse_LL(node.next).next = node
            node.next = None
            return node

        # first we know that the ip is a non-zero even length list
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # print(prev.val , slow.val)

        result = 0
        # disconnecting the first half
        prev.next = None
        reverse_LL(head)

        while prev:
            # print(prev.val , slow.val)
            result = max(result , prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return result
"""
