from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



"""
You are given two non-empty linked lists
representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

stored in reverse order

3   4   2
4   6   5

C = 0
        
2 - 4 - 3 - 9 - 8
5 - 6 - 4 - 0 - 0


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        # equalize the lengths by adding leading zeroes
        # we can also keep track if inserted and the location 

        loc = None # we know we will insert zeroes once at a point only
        i , j = l1 , l2
        while i.next or j.next:
            if not i.next and j.next:
                if not loc:
                    loc = i
                i.next = ListNode(0)

            if not j.next and i.next:
                if not loc:
                    loc = j
                j.next = ListNode(0)

            i = i.next
            j = j.next
        
        i , j , c , curr = l1 , l2 , 0 , dummy
        while (i and j) or c:
            
            if not (i and j):
                # considering the carry 
                sum = c
                rem , c = sum % 10 , sum // 10
                curr.next = ListNode(rem)
                curr = curr.next
            else:
                # addition of the digits
                sum = c + i.val + j.val
                rem , c = sum % 10 , sum // 10
                curr.next = ListNode(rem)
                curr = curr.next
                i = i.next
                j = j.next

        result = dummy.next
        dummy.next = None

        if loc:
            loc.next = None

        return result    

        # remove the zeroes added by setting the loc.next = None if loc is set 
        # remove the dummy and return dummy.next 
