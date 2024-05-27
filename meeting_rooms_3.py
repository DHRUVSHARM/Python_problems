import heapq
from typing import List

if __name__ == '__main__':
    arr = [(float("-inf"), 0), (float("-inf"), 1), (float("-inf"), -1), (1000000, 1)]
    for a, b in arr:
        print("a , b ", a, " , ", b)
    heapq.heapify(arr)
    print("the top is : ", arr[0])
    while arr:
        print(heapq.heappop(arr))


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # we need a heap which will store the priority as (minimal_end_time , minimal_index)
        meetings.sort(key=lambda element: (element[0], element[1]))
        print(
            meetings
        )
        minHeap = [(float("-inf"), room) for room in range(0, n)]
        heapq.heapify(minHeap)
        conducted = {room: 0 for room in range(0, n)}

        for start, end in meetings:
            if minHeap[0][0] <= start:

                minimal_room = float("inf")
                temp = []
                while len(minHeap) and minHeap[0][0] <= start:
                    c_e, c_r = heapq.heappop(minHeap)
                    temp.append((c_e, c_r))
                    minimal_room = min(minimal_room, c_r)

                for e, r in temp:
                    if r != minimal_room:
                        heapq.heappush(minHeap , (e , r))

                heapq.heappush(minHeap, (end, minimal_room))
                conducted[minimal_room] += 1
            else:
                # we need to delay the meeting
                diff = minHeap[0][0] - start
                m_e, r = heapq.heappop(minHeap)
                heapq.heappush(minHeap, (end + diff, r))
                conducted[r] += 1

        ans, ms = 0, -1

        for room, val in conducted.items():
            if val > ms:
                ans = room
                ms = val

        return ans
