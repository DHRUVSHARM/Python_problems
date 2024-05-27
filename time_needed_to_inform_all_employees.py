import collections
from typing import List

if __name__ == '__main__':
    adj_list = collections.defaultdict(list)
    adj_list[1].append(2)
    print(adj_list)
    for key, val in adj_list.items():
        print(key, val)
    # another way ...
    # adj_list_1 = {i: [] for i in range(0, 5)}
    # print(adj_list_1)


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        max_inform_time = 0
        adj_list = collections.defaultdict(list[int])
        # -1 is above the head manager , ignored
        for subordinate, direct_manager in enumerate(manager):
            adj_list[direct_manager].append(subordinate)

        # represents the employee , information reach time
        q = collections.deque([[headID, 0]])
        while q:
            id, time = q.popleft()
            max_inform_time = max(max_inform_time, time)

            for subordinate in adj_list[id]:
                q.append([subordinate, time + informTime[id]])

        return max_inform_time
