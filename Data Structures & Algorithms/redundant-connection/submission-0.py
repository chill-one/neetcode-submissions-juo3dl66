class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n))
        rank = [0] * n

        def find(node):
            if node == parent[node]:
                return node

            parent[node] = find(parent[node])
            return parent[node]



        def unionSet(v1, v2):
            root1, root2 = find(v1), find(v2)

            if root1 == root2:
                return False

            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                rank[root2] += 1

            return True

        for x, y in edges:
            if not unionSet(x-1, y-1):
                return [x, y]

        return []