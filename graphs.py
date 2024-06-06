# we are going to have a collection of nice solved graph problems here
import collections
from typing import List, Optional

if __name__ == "__main__":
    check_dict = {1: []}
    # we can add values like this if they do not exist
    print(check_dict)
    d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    s, y = 1, 1
    for dire in d:
        ds, dy = dire
        print("( ", s + ds, " , ", y + dy, " )")

    s = collections.deque([1, 2, 3])
    print(s[-1])

    test = set()
    test.add((1, 1))
    test.add((1, 1))
    print(test)

    A = [1, 100]
    print(1 in A)
    print(100 in A)
    print(50 in A)

    my_string = "hot"
    for i in range(len(my_string)):
        print(my_string[:i], "*", my_string[i + 1 :])
# to find the shortest path
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # the eight directions
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        n = len(grid)

        # we are given an n*n binary grid

        def bfs(start_x, start_y, target_x, target_y) -> int:
            # edge case
            if grid[start_x][start_y] == 1 or grid[target_x][target_y] == 1:
                return -1

            visited, distance = {(start_x, start_y)}, 0
            nodes = collections.deque([(start_x, start_y)])

            # we will do bfs layering approach
            while len(nodes):
                level_length = len(nodes)
                distance += 1
                # we consider the 0 , 0 level as 1
                # exploring the current layer
                while level_length:
                    x, y = nodes.popleft()
                    if x == target_x and y == target_y:
                        return distance

                    for dx, dy in directions:
                        cx, cy = x + dx, y + dy
                        if 0 <= cx <= n - 1 and 0 <= cy <= n - 1 and grid[cx][cy] == 0 and (cx, cy) not in visited:
                            nodes.append((cx, cy))
                            visited.add((cx, cy))

                    level_length -= 1

            return -1

        # starting from 0,0 to n-1, n-1 to find the shortest path
        return bfs(0, 0, n - 1, n - 1)
"""

# another bfs application , this way we just kept track of common progress of each rotten orange start
# point
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_info, m, n = {}, len(grid), len(grid[0])

        # orange info will store the minimal time it takes for an orange to become rotten
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    # fresh orange
                    orange_info[(i, j)] = float("inf")
                elif grid[i][j] == 2:
                    # rotten orange
                    orange_info[(i, j)] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start, end):
            visited, nodes = {(start, end)}, collections.deque([(start, end)])
            current_time = 0

            while len(nodes):

                level_length = len(nodes)

                while level_length:
                    x, y = nodes.popleft()
                    orange_info[(x, y)] = min(orange_info[(x, y)], current_time)

                    for dx, dy in directions:
                        cx, cy = x + dx, y + dy
                        if 0 <= cx <= m - 1 and 0 <= cy <= n - 1 and grid[cx][cy] != 0 and (cx, cy) not in visited:
                            visited.add((cx, cy))
                            nodes.append((cx, cy))
                    level_length -= 1

                current_time += 1

        time_taken = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    # possible infection start point
                    bfs(i, j)

        # print(orange_info)

        for time in orange_info.values():
            if time == float("inf"):
                return -1
            time_taken = max(time_taken, time)

        return time_taken
"""

# we can also do multi - source bfs to solve this problem, the solution is below
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_info, nodes, m, n = {}, collections.deque(), len(grid), len(grid[0])

        # orange info will store the minimal time it takes for an orange to become rotten
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    # fresh orange
                    orange_info[(i, j)] = float("inf")
                elif grid[i][j] == 2:
                    # rotten orange
                    orange_info[(i, j)] = 0
                    nodes.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # from this part we will do multi - source bfs
        def bfs():
            current_time, visited = 0, set()
            while len(nodes):

                level_length = len(nodes)

                while level_length:
                    x, y = nodes.popleft()
                    orange_info[(x, y)] = min(orange_info[(x, y)], current_time)

                    for dx, dy in directions:
                        cx, cy = x + dx, y + dy
                        if 0 <= cx <= m - 1 and 0 <= cy <= n - 1 and grid[cx][cy] != 0 and (cx, cy) not in visited:
                            visited.add((cx, cy))
                            nodes.append((cx, cy))
                    level_length -= 1

                current_time += 1

        bfs()

        time_taken = 0
        for time in orange_info.values():
            if time == float("inf"):
                return -1
            time_taken = max(time_taken, time)

        return time_taken
"""

# very imp conceptual questions of DAG
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we will maintain a dictionary with frequency of incoming edges
        incoming, adj_list = {i: 0 for i in range(0, numCourses)}, {i: [] for i in range(0, numCourses)}

        for course, pre in prerequisites:
            incoming[course] += 1
            adj_list[pre].append(course)

        # print(adj_list)
        # print(incoming)
        courses_taken = 0
        while courses_taken < numCourses:
            current_course = -1
            for course, prereq_number in incoming.items():
                if prereq_number == 0:
                    current_course = course
                    break

            if current_course == -1:
                # not enough courses
                return False
            # let -1 mean cannot be used again
            incoming[current_course] = -1
            # now we will use this course and break connections
            for neighbour in adj_list[current_course]:
                incoming[neighbour] -= 1

            courses_taken += 1

        return True
"""

# ********************************************* questions solved using iterative dfs *******#
# Definition for a binary tree node.
# class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right


"""
class BSTIterator:
    __slots__ = "curr", "nodes"

    def __init__(self, root: Optional[TreeNode]):
        self.curr = None
        self.nodes = collections.deque([root])
        self.push_till_end()

    def push_till_end(self):
        # function to push till the leftmost node in the stack , at the end this will be the leftmost
        # in the stack
        self.curr = self.nodes[-1]
        # the top element is required here
        while self.curr.left:
            self.nodes.append(self.curr.left)
            self.curr = self.curr.left

    def next(self) -> int:
        # assuming that the next calls are always valid
        current_node = self.nodes.pop()
        if current_node.right:
            # we have a valid right child
            self.nodes.append(current_node.right)
            self.push_till_end()

        return current_node.val

    def hasNext(self) -> bool:
        return True if len(self.nodes) else False
"""

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s, result = collections.deque(), []
        if root is not None:
            s.append(root)

        while len(s):
            current_node = s.pop()
            result.append(current_node.val)
            if current_node.right:
                s.append(current_node.right)
            if current_node.left:
                s.append(current_node.left)

        return result
"""

"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, s, seen_once = [], collections.deque(), collections.deque()
        if root:
            s.append(root)
            seen_once.append(False)

        while len(s):
            curr_node, seen = s.pop(), seen_once.pop()
            if seen:
                # we need to print this
                result.append(curr_node.val)
            else:
                # we need to put the children in the stack
                s.append(curr_node)
                seen_once.append(True)
                if curr_node.right:
                    s.append(curr_node.right)
                    seen_once.append(False)
                if curr_node.left:
                    s.append(curr_node.left)
                    seen_once.append(False)

        return result
"""

# continuing with graph problems
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # we will do the problem in reverse , think of the pacific and atlantic ocean as
        # separate nodes that are connected to both sides
        pacific_reachable, atlantic_reachable = set(), set()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(queue_pacific, queue_atlantic):
            while queue_pacific or queue_atlantic:
                if queue_pacific:
                    x, y = queue_pacific.popleft()
                    for dx, dy in directions:
                        newx, newy = x + dx, y + dy
                        if 0 <= newx < m and 0 <= newy < n and heights[newx][newy] >= heights[x][y] and (
                                newx, newy) not in pacific_reachable:
                            pacific_reachable.add((newx, newy))
                            queue_pacific.append((newx, newy))
                if queue_atlantic:
                    x, y = queue_atlantic.popleft()
                    for dx, dy in directions:
                        newx, newy = x + dx, y + dy
                        if 0 <= newx < m and 0 <= newy < n and heights[newx][newy] >= heights[x][y] and (
                                newx, newy) not in atlantic_reachable:
                            atlantic_reachable.add((newx, newy))
                            queue_atlantic.append((newx, newy))

        q_pac, q_atl = collections.deque(), collections.deque()
        for r in range(0, m):
            pacific_reachable.add((r, 0))
            atlantic_reachable.add((r, n - 1))
            q_pac.append((r, 0))
            q_atl.append((r, n - 1))
        for c in range(0, n):
            pacific_reachable.add((0, c))
            atlantic_reachable.add((m - 1, c))
            q_pac.append((0, c))
            q_atl.append((m - 1, c))


        # print("pacific queue : " , q_pac)
        # print("atlantic queue : " , q_atl)

        bfs(q_pac, q_atl)

        result = []
        for i in range(0, m):
            for j in range(0, n):
                if (i, j) in pacific_reachable and (i, j) in atlantic_reachable:
                    result.append([i, j])

        return result
"""

# surrounded regions
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # first we will mark the non-surrounded regions as T
        # these are at the edges or reachable from a node there
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(row, col):
            q = collections.deque([(row, col)])
            board[row][col] = 'T'

            while len(q):
                x, y = q.popleft()
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if 0 <= newx <= m - 1 and 0 <= newy <= n - 1 and board[newx][newy] == 'O':
                        # unsurrounded region
                        board[newx][newy] = 'T'
                        q.append((newx, newy))

        for r in range(0, m):
            for c in range(0, n):
                if (r in [0, m - 1] or c in [0, n - 1]) and board[r][c] == 'O':
                    # at the edges, unsurrounded region
                    # beware of the and or short ckting priority order
                    # print("corner start : " , r , " ", c)
                    bfs(r, c)
        # all the unsurrounded regions are now marked as T
        for r in range(0 , m):
            for c in range(0 , n):
                if board[r][c] == 'O':
                    # surrounded region
                    board[r][c] = 'X'
        # resetting the unsurrounded regions
        for r in range(0 , m):
            for c in range(0 , n):
                if board[r][c] == 'T':
                    # reset back to O
                    board[r][c] = 'O'
"""

# walls and gates, we use a reverse multi-sourced bfs approach
"""
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        # -1 represents an obstacle , 0 is a gate and INF is the empty-room
        # we will do the operations and update the distances in the grid itself
        m, n = len(rooms), len(rooms[0])
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def multi_source_bfs():
            q, visited = collections.deque(), set()
            # we fill it with the gates initially
            for r in range(0, m):
                for c in range(0, n):
                    if rooms[r][c] == 0:
                        visited.add((r, c))
                        q.append((r, c))

            # now we need to do bfs layer by layer so that the first change will
            # guarantee that the path from that empty room to the gate is the shortest

            level_number = 1
            while len(q):
                level_length = len(q)

                while level_length:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        newx, newy = x + dx, y + dy
                        if 0 <= newx <= m - 1 and 0 <= newy <= n - 1 and rooms[newx][newy] != -1 and (
                                newx, newy) not in visited:
                            # uninitialized empty room reached
                            # the way we are writing this code we are guaranteed to get the shortest path on
                            # the first try
                            rooms[newx][newy] = level_number
                            visited.add((newx, newy))
                            q.append((newx , newy))
                    level_length -= 1

                level_number += 1

        multi_source_bfs()
        return rooms
"""

# topological sort / ordering algo can be solved using incoming edges as well as recursive
# finish times
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adjacency list
        adj_list = collections.defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        ordering, finish_time, time, visit = [] , [-1 for _ in range(numCourses)], [1], set()

        def dfs(node):
            visit.add(node)

            for neighbour in adj_list[node]:
                if neighbour not in visit:
                    dfs(neighbour)

            finish_time[node] = time[0]
            time[0] += 1
            ordering.append(node)

        for index in range(0, len(finish_time)):
            if finish_time[index] == -1:
                dfs(index)

        ordering.reverse()

        for src , dest_vertices in adj_list.items():
            for des in dest_vertices:
                if finish_time[src] < finish_time[des]:
                    # top ordering is not possible
                    return []

        return ordering
"""

# problem to see how to use disjoint set union
"""
class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # initially, every element is parent of itself and rank is all 1
        parent, rank, components = [e for e in range(n)], [1 for _ in range(n)], [n]

        def get_parent(node):
            # gets the parent of the node
            while node != parent[node]:
                node = parent[node]

            return node

        def union(node1, node2):
            # performs union if possible based on the rank
            # also decreases the number of components by 1 after a successful union
            p1, p2 = get_parent(node1), get_parent(node2)

            if p1 != p2:
                if rank[p1] >= rank[p2]:
                    # smaller ranked components get merged to larger ranked components
                    parent[p2] =p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

                components[0] -= 1

        for src, dest in edges:
            union(src, dest)

        return components[0]
"""

# we see how to do cycle detection in an undirected graph using dfs only
"""
class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # for a tree we need to have no cycles and all the nodes must be connected
        # also we should have n - 1 edges , if any 2 are satisfied, the third property also holds
        visited, adj_list = set(), collections.defaultdict(list)

        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)

        def dfs(node, prev):
            visited.add(node)

            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour, node)
                else:
                    # visited node
                    if neighbour != prev:
                        return False

        dfs(0, -1)
        return len(visited) == n
"""

# unique way to build an adjacency list
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_list, adj_list = collections.defaultdict(list), collections.defaultdict(list)
        if beginWord not in wordList:
            # we need to add the word
            for index in range(0, len(beginWord)):
                pattern = beginWord[:index] + "*" + beginWord[index + 1:]
                pattern_list[pattern].append(beginWord)

        for word in wordList:
            # print(word)
            for index in range(0, len(word)):
                pattern = word[:index] + "*" + word[index + 1:]
                 #print(pattern)
                for neighbour in pattern_list[pattern]:
                    adj_list[word].append(neighbour)
                    adj_list[neighbour].append(word)
                pattern_list[pattern].append(word)


        def bfs(start, target) -> int:
            # returns the shortest way to get to target from start , else 0
            q, visit = collections.deque([(start, 1)]), set()

            while len(q):
                front_node, distance = q.popleft()
                if front_node == target:
                    # can return here
                    return distance
                for neighbour in adj_list[front_node]:
                    if neighbour not in visit:
                        visit.add(neighbour)
                        q.append((neighbour, distance + 1))

            # target not found
            return 0

        return bfs(beginWord, endWord)
"""
