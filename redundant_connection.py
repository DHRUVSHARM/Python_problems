from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # to solve this we will need the union find algo
        # this needs a parent and a rank array
        n = len(edges)
        parent = [i for i in range(0, n + 1)]
        rank = [1 for _ in range(0, n + 1)]

        def find(v):
            while parent[v] != v:
                parent[v] = parent[parent[v]]  # path compression step
                v = parent[v]
            return v

        def union(u, v):
            if rank[u] >= rank[v]:
                # merge into u
                parent[v] = u
                rank[u] += rank[v]
            else:
                parent[u] = v
                rank[v] += rank[u]

        for edge in edges:
            start, end = edge
            start_frontier = find(start)
            end_frontier = find(end)

            # check if the two belong to the same
            if start_frontier == end_frontier:
                return [start, end]

            # otherwise we do a union based on rank
            union(start_frontier, end_frontier)


if __name__ == '__main__':
    pass
