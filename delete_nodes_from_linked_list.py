# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # we will add an empty head to the front for ease of coding
        empty_head = ListNode(float("inf"), head)

        prev, curr = empty_head, head
        nums = set(nums)

        while curr:
            if curr.val in nums:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return empty_head.next
