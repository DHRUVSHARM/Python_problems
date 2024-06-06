import collections
from typing import List

if __name__ == "__main__":
    a = {1: "3", 2: "4", 3: "4"}
    for e in a:
        print(e)


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # we will maintain a time_map that contains the snapshots of the graph at the different times
        time_map = {}
        for start, end, t in meetings:
            if t not in time_map:
                time_map[t] = collections.defaultdict(list)
            # already existing timestamp
            time_map[t][start].append(end)
            time_map[t][end].append(start)

        # print(time_map)

        # at time 0 the person 0 shares secret with firstPerson
        secrets = {0, firstPerson}
        visited = set()

        def dfs(node, adj):
            visited.add(node)
            secrets.add(node)

            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour, adj)

        for t in sorted(time_map.keys()):
            visited = set()
            for src in time_map[t]:
                if src not in visited and src in secrets:
                    dfs(src, time_map[t])

        return list(secrets)
