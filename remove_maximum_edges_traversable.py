from typing import List

if __name__ == '__main__':
    pass


class UnionFind:
    __slots__ = 'parent', 'rank', 'components'

    def __init__(self, n):
        self.parent = [i for i in range(0, n + 1)]
        self.rank = [1 for _ in range(0, n + 1)]
        self.components = n # will help us keep track of the status of the union find

    def find(self, v):
        """
        function to find the frontier of the component and return it
        :param v: vertex
        :return: leader of component
        """
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]  # path compression step
            v = self.parent[v]
        return v

    def union(self, u, v):
        """
        performs the union of 2 components given leaders
        :param u: leader u
        :param v: leader v
        :return: None
        """
        if self.rank[u] >= self.rank[v]:
            # merge into u
            self.parent[v] = u
            self.rank[u] += self.rank[v]
        else:
            self.parent[u] = v
            self.rank[v] += self.rank[u]

    def add(self, u, v):
        """
        function to add an edge , if it can be added decrease components, update and return 1
        else return 0
        :param u: u
        :param v: v
        :return: 0 / 1
        """

        u_frontier = self.find(u)
        v_frontier = self.find(v)

        if u_frontier == v_frontier:
            # no updates nothing can be added
            return 0

        self.union(u_frontier, v_frontier)
        self.components -= 1
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # we will maintain 2 instances of the UF algorithm
        aliceUF = UnionFind(n)
        bobUF = UnionFind(n)

        added_edges = 0

        # greedy strategy will be to first construct the uf's using type 3
        for edge in edges:
            edge_type, start, end = edge
            if edge_type == 3:
                added_edges += (aliceUF.add(start, end) | bobUF.add(start, end))

        # now we will add edges and check accordingly
        for edge in edges:
            edge_type, start, end = edge
            if edge_type == 1:
                added_edges += aliceUF.add(start, end)
            elif edge_type == 2:
                added_edges += bobUF.add(start, end)

        # print(len(edges) - added_edges)

        if aliceUF.components == 1 and bobUF.components == 1:
            return len(edges) - added_edges
        else:
            return -1
