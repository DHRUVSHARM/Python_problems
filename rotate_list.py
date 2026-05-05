# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""


              c
Input: head = [1,  2,  3,  4,  5], k = 2

Output: [4,5,1,2,3]




"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case 
        if not head:
            return head
        
        # alteast one node
        n , curr = 1 , head

        while curr.next:
            n += 1
            curr = curr.next

        # curr is now on the tail 
        k , tail = k % n , curr

        if k == 0:
            return head

        # we need to get the final state 
        temp = ListNode()
        temp.next = head

        curr , steps = temp , n - k # 1 - 0 steps
        # print("steps : " , steps)

        while steps:
            curr = curr.next
            steps -= 1
        
        
        # print(curr.val)

        temp_head = curr.next
        curr.next = None
        tail.next = head
        temp.next = None
        head = temp_head if temp_head is not None else head

        return head
