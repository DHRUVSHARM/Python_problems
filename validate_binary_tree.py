from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # the nodes available to us are numbered from 0 to n - 1
        # we keep track of the incoming edges number
        incoming_edges = {i: 0 for i in range(0, n)}
        for index in range(0, n):
            if leftChild[index] != -1:
                incoming_edges[leftChild[index]] += 1
            if rightChild[index] != -1:
                incoming_edges[rightChild[index]] += 1

        # print(incoming_edges)

        root = -1
        for key, value in incoming_edges.items():
            if value == 0:
                # this is a root
                root = key
                break

        if root == -1:
            # no root
            return False

        visited, cycle = set(), [False]

        # print(root)

        def dfs(node):
            """
            does dfs and detects cycle as well
            :param node: current node
            :return: None
            """

            # print(node)

            visited.add(node)
            # print(visited)

            if leftChild[node] != -1:
                if leftChild[node] not in visited:
                    dfs(leftChild[node])
                else:
                    # cycle condition
                    # print("here " , node)
                    cycle[0] = True

            if rightChild[node] != -1:
                if rightChild[node] not in visited:
                    dfs(rightChild[node])
                else:
                    # cycle condition
                    # print("here " , node)
                    cycle[0] = True

        dfs(root)

        # print("final : " , visited)

        if len(visited) == n and not cycle[0]:
            return True
        else:
            # print("here")
            return False