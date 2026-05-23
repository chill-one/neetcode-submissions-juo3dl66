class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0] * n


        def find(node):
            if node == parent[node]:
                return node

            root = parent[node]
            parent[node] = find(parent[root])
            return parent[node]

        def unionSet(v1, v2):
            root1 = find(v1)
            root2 = find(v2)
            
            if root1 == root2:
                return

            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                rank[root1] += 1


        for x, y in edges:
            unionSet(x, y)

        count = 0
        for idx, value in enumerate(parent):
            if idx == value:
                count += 1

        return count


            

            