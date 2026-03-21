# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""

  1,2,3, 4,5,6 
               
k = 3 

[1,2,3,4,5,6], k = 3

0 , 1 , 2  , k = 4 % len(3)

1 2 3 4 5 6 7
              t  
h- 1 2 3 6 5 4

4 5 6 1 2 3   , k = 3

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        n , curr , tail = 0 , head , None
        while curr:
            tail = curr
            curr = curr.next
            n +=1
        # ---------prev,none

        remainder_list , prev , curr = n - (k % n) , None , head
        while remainder_list:
            prev = curr
            curr = curr.next
            remainder_list -= 1
        
        if not prev or not curr:
            # no need to reverse 
            return head

        prev.next = None
        # head----none 1 2 3

        def reverse_ll(node):
            # 1 < 2 < 3  <  4 
            # we return the tail in this solution             
            if not node.next:
                return node
            curr = node
            new_tail = reverse_ll(curr.next)
            new_tail.next = curr
            return curr

        # reverse_ll(curr) no need to reverse question misunderstood
        tail.next = head
        return curr



        
        
