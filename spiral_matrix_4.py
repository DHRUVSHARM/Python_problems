# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        filled, curr = set(), head
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        index = 0
        starter = (0, -1)

        while len(filled) < m * n and curr:
            # move first
            dx, dy = directions[index]
            new_starter = (starter[0] + dx, starter[1] + dy)

            if (
                0 <= new_starter[0] < m
                and 0 <= new_starter[1] < n
                and new_starter not in filled
            ):
                matrix[new_starter[0]][new_starter[1]] = curr.val
                curr = curr.next
                filled.add(new_starter)
                starter = new_starter
            else:
                # change the direction
                index = (index + 1) % 4

        return matrix
