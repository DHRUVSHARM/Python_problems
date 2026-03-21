"""
Design a Disjoint Set (aka Union-Find) class.

Your UnionFind class should support the following operations:

1. UnionFind(int n) will initialize a disjoint set of size n.


2. int find(int x) will return the root of the component that x belongs to.


bool isSameComponent(int x, int y) will return whether x and y belong to the same component.

bool union(int x, int y) will union the components that x and y belong to. If they are already in the same component, return false, otherwise return true.

int getNumComponents() will return the number of components in the disjoint set.

Example 1:

Input:
["UnionFind", 10, "isSameComponent", 1, 3, "union", 1, 2, "union", 2, 3, "getNumComponents", "isSameComponent", 1, 3]

Output:
[null, 1, false, true, true, 8, true]
Note: The find method will not be directly tested, but you will need to use it in the implementation of the other methods. Thus, it will be tested indirectly.



n
0 to n - 1
parent dict map the node -> parent 
num_components = n # reduction by 1 everytime we union unless in the same component , least value can be 1


1 2 3 4 - 4
1 - 2    - 3
3 - 4    - 2

1-2 3-4 = 1
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

