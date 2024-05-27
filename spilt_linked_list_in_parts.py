# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # first we need to find the size of the list (starting from 1)
        number_of_nodes, curr = 0, head
        while curr:
            number_of_nodes += 1
            curr = curr.next

        # we also keep a mapping of the kth part (0 indexed) to size
        base_length, rem_length = number_of_nodes // k, number_of_nodes % k

        part_length = {i: base_length for i in range(0, k)}
        i = 0
        while rem_length:
            part_length[i] += 1
            rem_length -= 1
            i += 1

        result, curr = [], head
        # now we will store the heads of each part in a list
        for _, length in part_length.items():
            part_head, prev = curr, None
            while length:
                prev, curr = curr, curr.next
                length -= 1
            if prev:
                prev.next = None
            result.append(part_head)

        return result
