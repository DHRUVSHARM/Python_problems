
"""

hard question revision 

You are given a list of airline tickets 

where tickets[i] = [fromi, toi] 

represent the departure and the arrival airports of one flight. 



All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
If there are multiple valid itineraries,



Reconstruct the itinerary in order and return it.
# itinary is a list of strings 
# begin from JFK 
#  you should return the itinerary that has the smallest lexical order when read as a single string.

# ord('A') < ord('B')
# length is always 3
# all tickets to be used only once, visited set 

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



        score
JFK,  -  SFO 
      -  ATL

      
      current 
      jfk , atl , sfo , atl , jfk , sfo

      
jfk , atl , sfo , atl , jfk
      
# will have to explore cycles 
# can keep a path or visited with three states no key present, key present with false (in current path)

Euler Path:
  - all edges once
  - 0 or 2 odd vertices

Euler Circuit:
  - all edges once
  - start = end
  - 0 odd vertices

"""

# all tickets form atleast one valid itinerary 

from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)
        edge_map = collections.defaultdict(int)

        # we can also maintain a map that keeps the count of edges available at each point in the iteration ? 

        for src, dest in tickets:
            # we will store an edge one time only 
            if (src, dest) not in edge_map:
                adj[src].append(dest)
            edge_map[(src , dest)] += 1 
            # idea is to track multiple edges as well

        # print("edge map")
        # print(edge_map)

        # heirholzer algorithm uses each edge only once and is immune to exponential 
        # blowup in case of backtracking 

        result , s = [] , ['JFK']

        while len(s):
            # the frontier is the currently explored node
            # print(edge_map)
            # print(s , "\n")
            explore = False
            for nei in adj[s[-1]]:
                # greedily select first available
                if edge_map[(s[-1] , nei)] > 0:
                    edge_map[(s[-1] , nei)] -= 1
                    s.append(nei)
                    explore = True
                    break
            
            if not explore:
                # no further edges to expand
                node = s.pop()
                result.append(node)
        
        result.reverse()
        return result 