from typing import List
# we will use kahns algo
"""
                                                    # should come before, higher priority 
Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]


item -> beforeitem, and no need to reverse

0   -1
1   -1   6
2
3
4
5
6
7


map 
element, group

and fill adj list
element -> [before items if any]

maintain incoming as well (element -> incoming edges)
incoming is global 

visited set is global
-------------------------------------------------
while not in visited, 
    find one call algo with pushed into q

check if len)visited = elements if not then []

    
while q:    kahn algo 
-----------------------------------

maintain 
group -> postorder list ordering 

final output across keys extend list values and return 

all -1 in one group
"""

import collections
class Solution:

    def kahn(self, nodes, adj , group , incoming , visited , ordering ):
        
        while len(nodes):
            # print(nodes)
            node = nodes.popleft()
            # print("node : " , node)
            # add to correct ordering
            ordering[group[node]].append(node)

            # collect all new nodes with no incoming edges
            new_nodes = []
            for nei in adj[node]:
                # print("nei : " , nei)
                if nei not in visited:
                    incoming[nei] -= 1
                    if incoming[nei] == 0:
                        new_nodes.append(nei)
                        visited.add(nei)
            # print(new_nodes)
            nodes.extend(new_nodes)

        

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        adj , incoming , visited , ordering = {element : [] for element in range(0 , n)} , {element : 0 for element in range(0 , n)} , set() , {element : [] for element in range(0 , m)} 
        ordering[-1] = [] # single group for all other group types
        keys = {element for element in range(0 , n)}

        # build graph element-> beforeitem 
        for key in keys:
            for before_item in beforeItems[key]:
                adj[key].append(before_item)
                incoming[before_item] += 1

        # print(incoming)
        # print("adj : " , adj)    

        # iterate over the keys that have no incoming edges and send them into the queue in one pass
        # this will be across components in one go 
        nodes = collections.deque()
        for key in keys:
            if incoming[key] == 0:
                nodes.append(key)
                visited.add(key)
        
        self.kahn(nodes, adj , group , incoming , visited , ordering)
        # this will give the group wise ordering with each reversed 

        # if any cycle we cannot partition or build graph
        if len(visited) != n:
            return []
        
        # after this point, it is about partitioning 
        # if there are no cycles, we can always break the graph into groups

        # rebuilding for group level 
        # only one ordering 
        # all elements belong to one group ie; 0

        # we cannot force all the -1 to be in one group
        ordering.pop(-1)
        group_keys, group_mapping,  key_index = set() , collections.defaultdict() , 1
        for key in keys:
            g = group[key]
            if g >= 0:
                group_keys.add(g)
                group_mapping[key] = g
            else:
                group_keys.add(key_index * -1)
                group_mapping[key] = (key_index * -1)
                ordering[key_index * -1] = [key]
                key_index += 1

        adj = {element : set() for element in group_keys}
        incoming , visited , group_ordering = {element : 0 for element in group_keys}, set() , {element : [] for element in range(1)} 
            

        for key in keys:
            for before_item in beforeItems[key]:
                sg , eg = group_mapping[key] , group_mapping[before_item]
                if sg != eg and eg not in adj[sg]:
                    adj[sg].add(eg)
                    incoming[eg] += 1

    
        nodes = collections.deque()

        # print("adj : " , adj)
        # print("incoming : " , incoming)

        for g in group_keys:
            if incoming[g] == 0:
                nodes.append(g)
                visited.add(g)
        
        self.kahn(nodes, adj , {element : 0 for element in group_keys} , incoming , visited , group_ordering)

        # print("group_ordering : " , group_ordering)
        # print("ordering : " , ordering)
        
        result = []
        for group in reversed(group_ordering[0]): 
            for partial in reversed(ordering[group]):
                result.append(partial)
        
        return result


