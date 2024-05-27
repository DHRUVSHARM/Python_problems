"""
testing program for starting in summer !!!!!!
first problem for the summer in python
"""
import collections
from typing import List


class Solution:
    def bfs(self, graph, start, end) -> float | int:
        # there is no contradiction ie; there is only one unique weight to reach every node
        deq, visited = collections.deque(), set()
        if start in graph:
            deq.append([start, 1])
            visited.add(start)

        answer = -1

        while len(deq) != 0:
            node_info = deq.popleft()
            node = node_info[0]
            weight_to_reach = node_info[1]
            if node == end:
                answer = weight_to_reach
            for neighbour in graph[node]:
                print("neighbour : " + str(neighbour))
                if neighbour[0] not in visited:
                    visited.add(neighbour[0])
                    deq.append([neighbour[0], weight_to_reach * neighbour[1]])

        return answer

    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            num, denom = eq
            graph[num].append([denom, values[i]])
            graph[denom].append([num, (1 / values[i])])

        print(str(graph))

        answers = []

        for query in queries:
            # we want to reach from start to end , else return -1
            start = query[0]
            end = query[1]
            answer = self.bfs(graph, start, end)
            answers.append(answer)

        return answers


if __name__ == '__main__':
    pass
