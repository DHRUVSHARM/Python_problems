import collections
import heapq
from typing import List
import itertools


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        smallest_pairs, result, visited = [], [], set()
        i, j = 0, 0
        heapq.heappush(smallest_pairs, (nums1[0] + nums2[0], (i, j)))
        visited.add((i, j))
        nodes = collections.deque([(i, j)])

        while len(nodes) and k:
            minimal_sum = smallest_pairs[0][0]
            while len(smallest_pairs) and k and minimal_sum == smallest_pairs[0][0]:
                x, y = heapq.heappop(smallest_pairs)[1]
                result.append([nums1[x], nums2[y]])
                k -= 1

            level_size = len(nodes)
            print("level size : ", level_size)
            while level_size:
                front_x, front_y = nodes.popleft()

                if front_x < len(nums1) - 1 and (front_x + 1, front_y) not in visited:
                    visited.add((front_x + 1, front_y))
                    nodes.append((front_x + 1, front_y))
                    heapq.heappush(
                        smallest_pairs,
                        (nums1[front_x + 1] + nums2[front_y], (front_x + 1, front_y)),
                    )

                if front_y < len(nums2) - 1 and (front_x, front_y + 1) not in visited:
                    visited.add((front_x, front_y + 1))
                    nodes.append((front_x, front_y + 1))
                    heapq.heappush(
                        smallest_pairs,
                        (nums1[front_x] + nums2[front_y + 1], (front_x, front_y + 1)),
                    )

                level_size -= 1

        while len(smallest_pairs) and k:
            x, y = heapq.heappop(smallest_pairs)[1]
            result.append([nums1[x], nums2[y]])
            k -= 1

        return result
