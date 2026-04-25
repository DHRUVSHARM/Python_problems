"""
Number of Islands II
Hard
Topics
Company Tags
You are given an empty 2D binary grid grid of size m x n. 
The grid represents a map where 0's represent water and 1's represent land. 
Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at 
position into a land. 

You are given an array positions where positions[i] = [rᵢ, cᵢ] is the position (rᵢ, cᵢ) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (rᵢ, cᵢ) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.



algorithm 

maintain union find, for all the nodes (mn)
maintain count of the components 

    a cell already converted to land, do nothing return
    new cell to land:
        comp += 1
        check 4 directions , valid nei in the boundary or water :
            if nei is land
                if cycle skip union false
                else extending component, comp -=1  union true,  
      
        return comp

"""


class UnionFind:
    def __init__(self , m , n):
        self.m = m
        self.n = n
        self.directions = [(-1 , 0) , (0 , -1) , (1 , 0) , (0 , 1)]
        self.land = set() # identify the land cells
        self.components = 0 # number of components
        self.par = {}
        self.rank = {}
        for r in range(0 , m):
            for c in range(0 , n):
                self.par[(r , c)] = (r , c)
                self.rank[(r , c)] = 0

    def find(self, node):
        if node == self.par[node]:
            return node
        self.par[node] =  self.find(self.par[node])
        return self.par[node]

    def union(self, node1 , node2):
        # true if we can add the edge, false, 
        # input is 2 nodes, node1 and node2 that represent a valid edge between 2 land cells and in the grid 
        par_u , par_v = self.find(node1) , self.find(node2)
        if par_u == par_v:
            return False # cycle 

        else:
            # not cycle 
            if self.rank[par_u] < self.rank[par_v]:
                par_u , par_v = par_v , par_u
            
            if self.rank[par_u] == self.rank[par_v]:
                self.rank[par_u] += 1
            
            # into u 
            self.par[par_v] = par_u
            return True


    def add_and_calculate_components(self, u , v):
        # this will add and alter the component state
        if (u , v) in self.land:
            return
        else:
            # new land cell ?
            # 0 <= rᵢ < m , 0 <= cᵢ < n so vald cell
            self.components += 1 # add a component
            self.land.add((u , v)) # new land cell created 
            for du , dv in self.directions:
                new_u , new_v = u + du , v + dv
                if 0 <= new_u < self.m and 0 <= new_v < self.n and (new_u , new_v) in self.land:
                    if self.union((u , v) , (new_u , new_v)):
                        # can add  
                        self.components -= 1
                    else:
                        # cycle , skip 
                        pass


    def get_components(self):
        return self.components



from typing import List
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        uf , result = UnionFind(m , n) , []

        for r , c in positions:
            uf.add_and_calculate_components(r , c)
            ans = uf.get_components()
            result.append(ans)

        return result