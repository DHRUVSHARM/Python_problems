import collections
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # nodes are from 1 to c
        # we need a mapping from connected component to a heap 
        adj , visited , min_online_element , online , component_belong_to = collections.defaultdict(list) , set() , collections.defaultdict() , set([node for node in range(1 , c + 1)]) , {element : None for element in range(1 , c+1)}

        for u , v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        # we know c is atleast 1 
        def dfs(node):
            visited.add(node)
            component_elements.append(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(1 , c + 1):
            if node not in visited:
                # this node can be the repr for the component
                component_elements = []
                dfs(node)      
                # map the component elements to the component
                minHeap = [] 
                for element in component_elements:
                    component_belong_to[element] = node
                    heapq.heappush(minHeap , element)
                # map the node to the heap
                min_online_element[node] = minHeap                 
        
        def maintain(station):
            # find parent
            parent = component_belong_to[station]
            # use to get min element may need to pop offline ones
            while min_online_element[parent] and (min_online_element[parent][0] not in online):
                heapq.heappop(min_online_element[parent])
            
            if min_online_element[parent]:
                return min_online_element[parent][0]
            else:
                return -1


        res = []
        for q , v in queries:
            if q == 1:
                # maintainance
                if v in online:
                    res.append(v)
                else:
                    # need minimal to make online 
                    station = maintain(v)
                    res.append(station)
            else:
                # make offline if online
                if v in online:
                    online.remove(v)

        return res