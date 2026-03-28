# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.


count = 1 (1 indexed)
start at back 
              l         r
                                  
        back                 front
dummy -> 1 -> 2 -> 3 -> 4 -> 5


l - r reverse it 

s         e
2 <- 3 <- 4

back.next = end
s.next = front 

"""

"""
from typing import Optional
class Solution:
    
    def reverse_ll(self, start , end):
        if start == end:
            return start 
        
        node = self.reverse_ll(start.next , end)
        node.next = start
        return start

    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        back , curr , left , right , index , front = dummy , head , None , None , 1 , None

        # assign the left and right based on the right index 
        while index < l:
            back = curr
            curr = curr.next
            index += 1
        
        left = curr

        # at this point we have the left
        while index < r:
            curr = curr.next
            index += 1

        right = curr
        front = right.next

        self.reverse_ll(left, right)
        left.next = front
        back.next = right

        head = dummy.next
        dummy.next = None

        return head
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_ll(self, curr, index, l_bound, r_bound, back , l):
        if index < l_bound:
            return self.reverse_ll(curr.next, index + 1 , l_bound , r_bound , back.next , l.next)
        elif l_bound <= index <= r_bound:

            if index == r_bound:
                # reached the end of the reversal 
                #             r
                # 1 -> 2 -> 3
                # at r
                back.next = curr
                l.next = curr.next

            elif l_bound <= index < r_bound:
                # hold the left and keep moving 
                node = self.reverse_ll(curr.next, index + 1 , l_bound , r_bound , back , l)
                node.next = curr
                
            return curr
            
    

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # single pass solution attempt 
        dummy = ListNode()
        dummy.next = head

        # we need to track , back , l, r, front  and the index 
        self.reverse_ll(head, 1 , left, right, dummy, head)
        head = dummy.next
        dummy.next = None

        return head
        