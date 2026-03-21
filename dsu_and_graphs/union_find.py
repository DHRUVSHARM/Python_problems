"""

maintain disjoint sets
effectively union them
and find

find : find the correct disjoint set
union : combine 2 disjoint sets 

assert condition, "error message"

"""

class UnionFind:
    def __init__(self , n):
        # n is the number of nodes
        self.par = {}
        self.rank = {}

        for i in range(0 , n):
            self.par[i] = i
            self.rank[i] = 0 
    

    def find(self, node):
        # path compression + find
        if self.par[node] == node:
            return node # root
        root = self.find(self.par[node])
        self.par[node] = root
        return root
    
    def union(self , node1 , node2):
        # return false if same component
        # true if succes
        # by rank , always attach to the bigger tree 
        par1 , par2 = self.find(node1) , self.find(node2)
        
        if par1 == par2:
            return False
        
        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.par[par1] = par2
        else:
            self.par[par2] = par1
            self.rank[par1] += 1

        return True

if __name__ == "__main__":
    uf = UnionFind(10)
    assert uf.find(1) == 1 , "wrong init condition"

    # 1) Initialization: each node is its own parent/root
    for i in range(10):
        assert uf.find(i) == i, f"init failed: find({i}) != {i}"
        assert uf.par[i] == i, f"init failed: par[{i}] != {i}"
        assert uf.rank[i] == 0, f"init failed: rank[{i}] != 0"

    # 2) Basic union: union connects components
    assert uf.union(1, 2) is True, "union(1,2) should succeed"
    assert uf.find(1) == uf.find(2), "1 and 2 should be connected after union"

    # 3) Union on same component should return False
    assert uf.union(1, 2) is False, "union(1,2) again should return False"

    # 4) Transitivity: if 1~2 and 2~3 then 1~3
    assert uf.union(2, 3) is True, "union(2,3) should succeed"
    assert uf.find(1) == uf.find(3), "1 and 3 should be connected via 2"

    # 5) Separation: untouched node should not be connected
    assert uf.find(4) != uf.find(1), "4 should not be connected to {1,2,3}"

    # 6) Another component, then merge components
    assert uf.union(5, 6) is True, "union(5,6) should succeed"
    assert uf.find(5) == uf.find(6), "5 and 6 should be connected"
    assert uf.find(5) != uf.find(1), "component {5,6} should be separate from {1,2,3}"

    assert uf.union(3, 6) is True, "union(3,6) should merge the two components"
    assert uf.find(1) == uf.find(5), "after merging, 1 and 5 should be connected"
    assert uf.find(2) == uf.find(6), "after merging, 2 and 6 should be connected"

    # 7) Path compression sanity (internal): after find(x), parent[x] should become root
    x = 6
    r = uf.find(x)
    assert uf.par[x] == r, "path compression expected: par[x] should be root after find(x)"

    print("All UnionFind tests passed ✅")
