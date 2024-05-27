# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # first we find the tail of the second list
        walker = list2
        while walker.next:
            walker = walker.next

        list_2_tail = walker

        walker_a , walker_b = list1 , list1
        index = 0
        while index < b:
            if index < a - 1:
                # we want to stop before the a index 0 based
                walker_a = walker_a.next
            # we want stop at b though
            walker_b = walker_b.next
            index += 1

        walker_a.next = list2
        new_end = walker_b.next
        walker_b.next = None
        list_2_tail.next = new_end

        return list1