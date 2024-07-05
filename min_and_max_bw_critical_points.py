# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # distances will be stored as : min , max
        distances = [float("inf"), 0]

        # atleast 2 nodes
        prev = head
        curr = head.next

        # no point checking last node
        index, prev_critical_index = 2, -1
        while curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (
                curr.val > prev.val and curr.val > curr.next.val
            ):
                if prev_critical_index == -1:
                    pass
                else:
                    distances[0] = min(distances[0], index - prev_critical_index)
                    distances[1] += index - prev_critical_index
                    # print(index)
                    # print("distances : " , distances)

                prev_critical_index = index
            else:
                pass

            prev = curr
            curr = curr.next
            index += 1

        if distances[0] == float("inf"):
            return [-1, -1]
        else:
            return distances
