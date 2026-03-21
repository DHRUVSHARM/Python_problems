from typing import List


"""
UnionFind(int n) will initialize a disjoint set of size n.
  
int find(int x) will return the root of the component that x belongs to.

bool isSameComponent(int x, int y) will return whether x and y belong to the same component.

bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.

int getNumComponents() will return the number of components in the disjoint set.
"""


"""
Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST).

find the weight of mst, kruskal

# iterate over the edges, 
    force include the edge and check weight 
        if == mst weight:
            # may be critical or pseudocritical
            try again without including 
            if == mst:
                pserudo
            else:
                critical
        else:
            neither critical nor pseudocritical 

An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge.

On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

All pairs (ai, bi) are distinct.

collect edges and make a map , 
edge tuple -> original index

return [critical , pseudo critical]
"""


class UnionFind:
    
    def __init__(self, n: int):
        # initialize a dsu of size n
        self.n = n  # num of components
        self.parent = {element : element for element in range(0 , n)}  # parent of itself     
        self.rank = {element : 0 for element in range(0 , n)} # upper bound on the component size   

    def find(self, x: int) -> int:
        # return the root of the component that x belongs to
        # flatten the tree
        # 1 - 2 - 3
        if x == self.parent[x]: 
            return x # found the root 
        self.parent[x] = self.find(self.parent[x]) # flatten 
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        parent_x , parent_y = self.find(x) , self.find(y) # find the components 
        return parent_x == parent_y # true if same component 

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x , y):
            return False
        # not same component , need to union by rank 
        # conceptually , minimal rank goes to bigger rank
        # 1 - 2
        #  3 
        # 1 - 2
        # - 3
        # 3 -1 - 2

        # 1  - 2
        # - 3 - 4

        # number of components will decrease at this point 
        # where to store rank ? 
        # store it at the parent 

        parent_x , parent_y = self.find(x) , self.find(y)
        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[self.rank[parent_y]]:
            self.parent[parent_x] = parent_y
        else:
            # attach to x
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1 # increase rank
        
        self.n -= 1
        return True

    def getNumComponents(self) -> int:
        return self.n




import collections
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edge_index_map = collections.defaultdict() 
        for index, edge in enumerate(edges):
            u , v , w = edge
            edge_index_map[(u , v)] = index

        
        critical , pseudo_critical = [] , []
        # sort by weight
        edges.sort(key=lambda e: (e[2] , e[0] , e[1]))


        def find_mst(skip_edge=None , consider_edge=None):
            # we will use kruskal to find the mst 
            # edges are sorted, we iterate over them one by one in increasing order of weight 
            # tuple skip or consider to find weight 
            # also graph is undirected connected graph
            # for skip edge maybe ok to just skip when we see it 
            # consider edge can be handled by taking that edge first 
            # then skip it further down the line 
            # otherwise nothing doing 

            # kruskal we initialize a disjoint set
            mst_w , ds = 0 , UnionFind(n)
            # for each edge we try to union , if false, means same part of the graph has been considered
            # else we can add the edge weight 

            if consider_edge is not None:
                s , e , w = consider_edge
                ds.union(s , e)
                mst_w += w

            for u , v , w in edges:
                if (u , v , w) == skip_edge or (u , v , w) == consider_edge:
                    # need to skip edge
                    pass
                else:
                    # normal processing
                    if not ds.union(u , v):
                        pass
                    else:
                        mst_w += w

                
            return mst_w

        # find the mst 
        mst = find_mst()    

        # print("mst : " , mst)

        for u , v , w in edges:
            edge_index = edge_index_map[(u , v)]
            include_edge_w = find_mst(consider_edge=(u , v , w))
            if include_edge_w == mst:
                exclude_edge_w = find_mst(skip_edge=(u , v , w))
                if exclude_edge_w == mst:
                    pseudo_critical.append(edge_index)
                else:
                    critical.append(edge_index)
            else:
                # skip 
                pass
        
        return [critical , pseudo_critical]