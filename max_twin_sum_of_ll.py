# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

"""
In a linked list of size n, 

where n is even, 

the ith node (0-indexed) 

of the linked list is known as the twin of the 

(n-1-i)th node, if 0 <= i <= (n / 2) - 1.

n = 4

0   1   2   3



For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        ans = float("-inf")
        print(res)
        for index in range(0 , len(res) // 2):
            ans = max(ans , res[index] + res[len(res) - index - 1])

        return ans
"""


"""
           s     f
    1   2  3  4  null
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

"""
In a linked list of size n, 

where n is even, 

the ith node (0-indexed) 

of the linked list is known as the twin of the 

(n-1-i)th node, if 0 <= i <= (n / 2) - 1.

n = 4

0   1   2   3



For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        ans = float("-inf")
        print(res)
        for index in range(0 , len(res) // 2):
            ans = max(ans , res[index] + res[len(res) - index - 1])

        return ans
"""


"""
           s     f
    1   2  3  4  null
"""

# pure ll based solution 
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow , prev = head, head , None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # at this point slow is the middle 
        # head ... prev | slow ... null

        # print("prev : " , prev.val , " " , "slow : " , slow.val)

        # 1 <- 2 <- 3 <-4
        def reverse(node):
            if node.next is None:
                return node , node
            
            new_ll , new_h = reverse(node.next)
            new_ll.next = node
            return node , new_h

        new_tail , new_head = reverse(slow)

        slow.next = None
        reversed_head = new_head
        prev.next = None
    
        left, right = head, reversed_head

        ans = float("-inf")
        while left and right:
            # print(left.val , " : " , right.val)
            ans = max(ans , left.val + right.val)
            left = left.next
            right = right.next
        
        return ans

