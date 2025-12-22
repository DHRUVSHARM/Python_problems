# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # to ensure that the code is clean we can keep an empty node at the beginning
        temp = ListNode(float("inf") , head)
        curr , prev , numbers_to_delete = head , temp , set(nums)
    

        while curr:
            if curr.val in numbers_to_delete:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        result = temp.next
        temp.next = None

        return result