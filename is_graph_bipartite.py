import collections
from typing import List

if __name__ == "__main__":
    my_list = [[1, 2, 3], [0, 1, 2], [2, 8], [7]]
    for i, lis in enumerate(my_list):
        print(str(i) + " : " + str(my_list[i]) + " | " + str(lis))


class Solution:

    def bfs(self, graph, src, info, level_number) -> bool:
        deq = collections.deque()
        deq.append(src)
        info[src][1] = level_number[0]
        info[src][0] = True

        while len(deq) != 0:

            level_len = len(deq)
            while level_len != 0:
                node = deq.popleft()
                for neighbour in graph[node]:
                    if not info[neighbour][0]:
                        deq.append(neighbour)
                        info[neighbour][0] = True
                        info[neighbour][1] = info[node][1] + 1

                    if info[neighbour][1] == info[node][1]:
                        return False
                level_len -= 1

            level_number[0] += 1

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        # we will do bfs with layering and check if we have 2 nodes in the same layer
        visited_info = {}
        for i in range(0, len(graph)):
            visited_info[i] = [False, int(-1)]

        level_number = [int(0)]

        for node in range(0, len(graph)):

            print(str(level_number))
            for i, ele in enumerate(visited_info):
                print(str(i) + " : " + str(visited_info[i]))

            if not visited_info[node][0]:
                print("start point is : " + str(node))
                verdict = self.bfs(graph, node, visited_info, level_number)
                print(str(verdict))

                # print(str(level_number))
                if not verdict:
                    return False

        return True
