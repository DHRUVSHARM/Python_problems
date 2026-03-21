# Definition for singly-linked list.
from typing import Optional

"""

k = 2

dummy - 1 - 2 - 3 - 4 - 5


len // k  , len % k

           
          1 - 2                 3 - 4     5
              dummy
              head
                      
                                    
                                  head       
          dummy - 2 - 1     -   4 - 3   -   5

reach till c (move k) , if we stop before then break out
head.next = c # break the link
new_c = c.next
while c.next is not none
    reverse
c.next = new_c
head = c
c  keep it
    

return dummy node .next
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
          1 - 2                 3 - 4     5
              dummy
              head
                      
                                    
                                  head       
          dummy - 2 - 1     -   4 - 3   -   5

h       c   nc
d  1 <- 2    3 - 4 - 5

h    c          nc
d -> 2 -> 1     3->4->5

reach till c (move k) , if we stop before then break out
head.next = c # break the link
new_c = c.next
while c.next is not none
    reverse
c.next = new_c
head = c
c  keep it

return dummy node .next


 th             c
 1 -> 2 -> 3  <  4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_ll(self, start , end):
        if start == end:
            return end
        
        reversed_node = self.reverse_ll(start.next , end)
        reversed_node.next = start
        return start

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(float("inf"))
        dummy.next = head
        head = dummy
        curr = dummy
        group_size = k


        while curr:
            curr = curr.next
            group_size -= 1

            if not curr:
                break

            if group_size == 0:
                # found k group
                temp_head = head.next
                head.next = curr
                new_curr = curr.next

                # reverse from th -> c
                reversed_end = self.reverse_ll(temp_head , curr)

                # connect
                reversed_end.next = new_curr
                head = reversed_end
                curr = head

                # reset group size 
                group_size = k



        # in the end we will remove the dummy node
        # and we will also make sure to move head to the correct place before that
        # ultimately we return head again 
        head = dummy.next
        dummy.next = None
        return head