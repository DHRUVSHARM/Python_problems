from typing import List, Tuple

# structure to handle the queries online for identifying a bipartite graph
"""


1 2         5 6
4 3

1   0

2   1

3   0

4   0



5 0

-------------------------
                                                                5   0

1   0                                                           6   1

2   1  ,  3 , 1   4 , 1



3 6

"""

class DSUParity:
    """
    DSU with a 0/1 relation (parity) to parent.

    rel[x] = relation(x, parent[x])
      0 -> same
      1 -> opposite
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        # rel[node] = parity describing if the node is colored same 0 or diff 1 to the directly connected parent in the dsu structure 
        # there is no guarantee that there are edges that connect these nodes in the orignal graph
        # but they are in the same connected component 
        self.rel = [0] * n

    def find(self, x: int) -> Tuple[int, int]:
        """
        Returns (root, rx) where:
          rx = relation(x, root)  (0 same, 1 opposite)

        Path compression:
          parent[x] becomes root
          rel[x] becomes relation(x, root)
        """
        if self.parent[x] == x:
            return x, 0

        # direct parent
        p = self.parent[x]
        # return global root + parity of direct parent  
        root, rp = self.find(p)      # rp = relation(p, root)

        # relation(x, root) = relation(x, p) XOR relation(p, root)
        self.rel[x] ^= rp
        # calculate the running value, since we are rerooting 
        self.parent[x] = root


        # ultimately we get the component root, relative parity 
        return root, self.rel[x]

    def union_opposite(self, u: int, v: int) -> bool:
        """
        Enforce constraint: u and v must be opposite.
        Returns False if contradiction is found, else True.
        

        2 things
        1 return t / f
        2 union  
        """
        ru, xu = self.find(u)  # xu = relation(u, ru)
        # root, parity from root 
        rv, xv = self.find(v)  # xv = relation(v, rv)

        # Already connected: relation(u, v) is fixed = xu XOR xv
        if ru == rv:
            # must be different color (u ^ root) ^ (root ^ v) = 1 
            return (xu ^ xv) == 1

        # Union by rank
        if self.rank[ru] < self.rank[rv]:
            ru, rv = rv, ru
            xu, xv = xv, xu

        # Attach rv under ru
        # force in terms of notation
        # u bigger , v is smaller
        # connect v to u  
        self.parent[rv] = ru

        # Choose relation(rv, ru) so that relation(u, v) becomes 1:
        # xu XOR xv XOR rel[rv] = 1  => rel[rv] = xu XOR xv XOR 1
        self.rel[rv] = xu ^ xv ^ 1

        if self.rank[ru] == self.rank[rv]:
            self.rank[ru] += 1

        return True


def is_bipartite_dsu(graph: List[List[int]]) -> bool:
    """
    Graph is adjacency list (undirected).
    Works even if edges appear twice; DSU checks consistency.
    """
    n = len(graph)
    dsu = DSUParity(n)

    for u in range(n):
        for v in graph[u]:
            if not dsu.union_opposite(u, v):
                return False

    return True


# Optional: if you have an edge list (unique edges), use this:
def is_bipartite_edges(n: int, edges: List[Tuple[int, int]]) -> bool:
    dsu = DSUParity(n)
    for u, v in edges:
        if not dsu.union_opposite(u, v):
            return False
    return True