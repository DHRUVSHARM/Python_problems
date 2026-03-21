# Definition for singly-linked list.
from typing import List , Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Input: lists = [[1,4,5],[1,3,4],[2,6]]

Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]

merging them into one sorted linked list:
1->1->2->3->4->4->5->6

# 
# [  () () | () () | () () | () ]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self , h1 , h2):
        #  4 5      4|
        # r -> 1 1 3
        result , curr1 , curr2 = ListNode(float("-inf")) , h1 , h2
        merged_pointer = result

        # print(curr1 , " : " , curr2)

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                merged_pointer.next = curr1
                merged_pointer = merged_pointer.next
                curr1 = curr1.next
            else:
                merged_pointer.next = curr2
                merged_pointer = merged_pointer.next
                curr2 = curr2.next
        # 4 5    
        # 1 1 3
        while curr1:
            merged_pointer.next = curr1
            curr1 = curr1.next
            merged_pointer = merged_pointer.next

        while curr2:
            merged_pointer.next = curr2
            curr2 = curr2.next
            merged_pointer = merged_pointer.next

        return result.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # [[],[-1,5,11],[],[6,10],[]]
        while len(lists) > 1:
            merged_list = []
            for index in range(0 , len(lists) , 2):
                if index + 1 < len(lists):
                    merged_root = self.merge(lists[index] , lists[index + 1])
                    merged_list.append(merged_root)
                else:
                    # otherwise single element need not merge
                    merged_list.append(lists[index])

            lists = merged_list
    
        return lists[0]
