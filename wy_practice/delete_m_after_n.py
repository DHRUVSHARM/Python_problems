"""
Docstring for wy_practice.delete_m_after_n
Delete N Nodes After M Nodes of a Linked List



head , m , n
2 , 3
                mp mc
           np nc
[ 1,2, 3,4,5, 6,7, 8,9,10, 11,12 ,13]

mp.next = nc
np.next = None

mp = np
mc = nc

pointer replace should be without next
"""

# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # inplace
        mprev, mcurr , nprev, ncurr = head , head , head , head
        while True:
            
            for _ in range(m):
                mprev = mcurr
                mcurr = mcurr.next
                if not mcurr:
                    break
            if not mcurr:
                # ----m
                break

            nprev = mprev
            ncurr = mcurr
            for _ in range(n):
                nprev = ncurr
                ncurr = ncurr.next
                if not ncurr:
                    break
            # possible that part of ncurr is left
            mprev.next = ncurr
            nprev.next = None

            # mp mc-----np nc
            mprev = nprev
            mcurr = ncurr

            if not mcurr:
                break
            

        return head