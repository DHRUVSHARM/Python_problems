from typing import List

"""
given n
there is an undirected graph 
n nodes
0 - n - 1 

[ui , vi , wi]  0 or 1 


"""


# weighted dsu 
class UnionFind:
    def __init__(self , n):
        self.par = {node : node for node in range(0 , n)}
        self.rank = {node : 0 for node in range(0 , n)}
        self.dsu = {node : 0 for node in range(0 , n)} # initially , these represent the parity of the node to itself 

    
    def find(self, node) ->int:
        """ finds and returns the parent node, along with path compression """
        if self.par[node] == node:
            return node 
        
        new_parent = self.find(self.par[node])
        self.dsu[node] ^= self.dsu[self.par[node]] # recompute wrt to the new parent, node --- par --- new parent
        self.par[node] = new_parent
        return new_parent

    def union(self, u , v , w) -> bool:
        """ in this case we will find the parents and return true if no cycle 
            and add it, or if cycle, then even weight and not add it, else false 
        """
        par_u , par_v = self.find(u) , self.find(v)

        if par_u != par_v:
            # need to do union 
            # do union by rank, try to add to the smaller one so that we can maintain equal 
            if self.rank[par_u] > self.rank[par_v]:
                u , v = v , u
                par_u , par_v = par_v , par_u
            
            # always connect v to u 
            # u ---- par[u]   par[v] --- v 
            self.par[par_v] = par_u
            self.dsu[par_v] = self.dsu[u] ^ self.dsu[v] ^ w
            # after this step parv is also wrt to paru, v is still wrt its parv buy when we run find again
            # in the future this will be fixed during the rerooting step 

            if self.rank[par_u] == self.rank[par_v]:
                self.rank[par_u] += 1

            return True
        else:
            # cycle do not add , check the weight to return true or false
            weight = self.dsu[u] ^ self.dsu[v] ^ w
            return weight == 0 # need to have even parity 

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        uf = UnionFind(n)

        for u , v , w in edges:
            if uf.union(u , v , w):
                result += 1

        return result