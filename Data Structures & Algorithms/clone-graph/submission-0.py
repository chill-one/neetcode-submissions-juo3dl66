"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        dic = {}
        root = Node()

        def dfs(curr, copy):
            copy.val = curr.val
            for neighbors in curr.neighbors:
                if neighbors in dic:
                    copy.neighbors.append(dic[neighbors])
                else:
                    new_neighbors = Node(neighbors.val)
                    copy.neighbors.append(new_neighbors)
                    dic[curr] = copy
                    dfs(neighbors, new_neighbors)

        dfs(node, root)
        return root
            

            